"""Headless multi-agent authoring orchestrator.

Drives Claude Code in headless mode (``claude -p --output-format json``,
subscription auth, no API key) through the pipeline: Planner -> Writer <-> Editor
loop -> (Tone specialist = the deterministic compile step). Each role is a
``claude -p`` call; the Editor returns a structured ``{ready, notes}`` verdict via
``--json-schema``.

The claude invocation is injectable (the ``runner`` argument) so the loop logic is
unit-testable without real calls or subscription quota. Every stage appends to the
trace so feedback can later be routed to the stage that produced a given result.
"""

from __future__ import annotations

import json
import shutil
import subprocess
from dataclasses import dataclass, field
from importlib import resources

from prosodia.core.trace import Run, Trace

EDITOR_SCHEMA = {
    "type": "object",
    "properties": {"ready": {"type": "boolean"}, "notes": {"type": "string"}},
    "required": ["ready", "notes"],
}


def _load_role(name: str) -> str:
    return (
        resources.files("prosodia.author")
        .joinpath("roles")
        .joinpath(f"{name}.md")
        .read_text(encoding="utf-8")
    )


@dataclass
class ClaudeRunner:
    """Runs a role as a headless ``claude -p`` call on the local subscription."""

    model: str | None = None
    extra_dirs: tuple[str, ...] = field(default_factory=tuple)
    allowed_tools: tuple[str, ...] = field(default_factory=tuple)
    timeout: int = 1200

    def run(self, prompt: str, *, system: str | None = None, schema: dict | None = None):
        if shutil.which("claude") is None:
            raise RuntimeError("claude CLI not found on PATH (Claude Code is required for authoring)")
        cmd = ["claude", "-p", "--output-format", "json", "--permission-mode", "dontAsk"]
        if system:
            cmd += ["--append-system-prompt", system]
        if schema:
            cmd += ["--json-schema", json.dumps(schema)]
        if self.model:
            cmd += ["--model", self.model]
        if self.allowed_tools:  # e.g. WebSearch/WebFetch so the planner can verify anecdotes
            cmd += ["--allowedTools", *self.allowed_tools]
        for d in self.extra_dirs:
            cmd += ["--add-dir", d]
        proc = subprocess.run(
            cmd, input=prompt, capture_output=True, text=True, encoding="utf-8", timeout=self.timeout
        )
        if proc.returncode != 0:
            raise RuntimeError(f"claude -p failed (exit {proc.returncode}): {proc.stderr[:500]}")
        data = json.loads(proc.stdout)
        result = data.get("result", "")
        structured = data.get("structured_output")
        if schema and structured is None:
            try:
                structured = json.loads(result)
            except Exception:
                structured = None
        return result, structured


def plan_series(
    prompt: str, *, runner, trace: Trace | None = None, run: Run | None = None
) -> str:
    outline, _ = runner.run(prompt, system=_load_role("planner"))
    if trace:
        trace.append("plan", "planner", chars=len(outline))
    if run is not None:
        art = run.write_artifact("stages/plan/outline.md", outline, label="outline")
        run.event("plan", "planner", outputs=[art], chars=len(outline))
    return outline


def author_episode(
    brief: str,
    *,
    runner,
    trace: Trace | None = None,
    run: Run | None = None,
    max_rounds: int = 3,
) -> str:
    """Run the Writer <-> Editor loop until the Editor says ready (or max_rounds).

    When a ``run`` is given, every round is persisted with enriched trace events:
    the Writer's prompt and its ``transcript.vN`` draft, and the Editor's verdict.
    A loop that exhausts ``max_rounds`` without approval is flagged ``warn`` — a
    signal the diagnosis pass can surface. ``trace`` (the thin log) is still honored.
    """
    writer_sys = _load_role("writer")
    editor_sys = _load_role("editor")
    notes = ""
    transcript = ""
    brief_art = run.write_artifact("brief.md", brief, label="brief") if run is not None else None
    for rnd in range(1, max_rounds + 1):
        wprompt = (
            f"{brief}\n\n"
            f"--- Editorial notes to address (from the previous round) ---\n{notes or '(none)'}\n\n"
            f"--- Your previous draft (revise it) ---\n{transcript or '(none)'}"
        )
        transcript, _ = runner.run(wprompt, system=writer_sys)
        if trace:
            trace.append("write", "writer", round=rnd, chars=len(transcript))
        if run is not None:
            run.write_artifact(f"stages/write.r{rnd}/prompt.md", wprompt)
            draft_art = run.write_artifact(
                f"stages/write.r{rnd}/transcript.v{rnd}.md", transcript, label=f"draft r{rnd}"
            )
            run.event(
                "write", "writer", round=rnd,
                inputs=[brief_art] if brief_art else [],
                outputs=[draft_art], chars=len(transcript),
            )

        eprompt = f"BRIEF:\n{brief}\n\nTRANSCRIPT:\n{transcript}"
        _, verdict = runner.run(eprompt, system=editor_sys, schema=EDITOR_SCHEMA)
        verdict = verdict or {"ready": True, "notes": ""}
        ready = bool(verdict.get("ready"))
        note_txt = str(verdict.get("notes", ""))
        if trace:
            trace.append("edit", "editor", round=rnd, ready=ready, notes=note_txt[:300])
        if run is not None:
            verdict_art = run.write_artifact(
                f"stages/edit.r{rnd}/verdict.json",
                json.dumps({"ready": ready, "notes": note_txt}, ensure_ascii=False, indent=2),
            )
            unresolved = (not ready) and (rnd == max_rounds)
            run.event(
                "edit", "editor", round=rnd,
                status="warn" if unresolved else "ok",
                outputs=[verdict_art], ready=ready, notes=note_txt[:500],
                warnings=["reached max_rounds without Editor approval"] if unresolved else [],
            )
        if ready:
            break
        notes = note_txt
    return transcript
