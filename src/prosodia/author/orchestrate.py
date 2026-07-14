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
import re
import shutil
import subprocess
from dataclasses import dataclass, field
from importlib import resources

from prosodia.author.persona import Persona
from prosodia.core.trace import Run, Trace

EDITOR_SCHEMA = {
    "type": "object",
    "properties": {"ready": {"type": "boolean"}, "notes": {"type": "string"}},
    "required": ["ready", "notes"],
}


def _extract_transcript(raw: str) -> str:
    """Recover the bare transcript from a Writer response.

    Writers occasionally wrap the script in explanatory prose and/or a ```markdown code
    fence — especially on a revision round ("Here is the revised transcript: ```..."). The
    transcript itself always begins at a YAML front-matter ``---`` line and contains no code
    fences, so: prefer the contents of a fenced block that holds front-matter; otherwise drop
    any preamble before the first front-matter line. Idempotent on already-clean input.
    """
    t = raw.strip()
    fence = re.search(r"```[A-Za-z0-9]*\s*\n(.*?)\n```", t, re.DOTALL)
    if fence and re.search(r"(?m)^---\s*$", fence.group(1)):
        return fence.group(1).strip()
    fm = re.search(r"(?m)^---\s*$", t)
    if fm and fm.start() > 0:
        return t[fm.start():].strip()
    return t


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
            # claude -p --output-format json writes its error to STDOUT, not stderr,
            # so surface both (tail — the message is usually at the end).
            detail = (proc.stderr.strip() or proc.stdout.strip() or "(no output)")[-1000:]
            raise RuntimeError(f"claude -p failed (exit {proc.returncode}): {detail}")
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
    prompt: str, *, runner, persona: Persona | None = None,
    trace: Trace | None = None, run: Run | None = None,
) -> str:
    persona = persona or Persona.resolve()
    outline, _ = runner.run(prompt, system=persona.role("planner"))
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
    persona: Persona | None = None,
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
    persona = persona or Persona.resolve()
    writer_sys = persona.role("writer")
    editor_sys = persona.role("editor")
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
        transcript = _extract_transcript(transcript)
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
            run.write_index()  # persist per round so a live viewer sees each round land

        eprompt = f"BRIEF:\n{brief}\n\nTRANSCRIPT:\n{transcript}"
        _, verdict = runner.run(eprompt, system=editor_sys, schema=EDITOR_SCHEMA)
        # A missing/unparseable verdict is treated as ready (deliberate — don't wedge on a
        # flaky editor), but record WHY so it isn't a silent pass in the trace.
        verdict = verdict or {"ready": True, "notes": "(no parseable editor verdict — treated as ready)"}
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
            run.write_index()
        if ready:
            break
        notes = note_txt
    return transcript
