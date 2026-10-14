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


def final_answer_text(events: list[dict], result: str) -> str:
    """The model's whole final answer, rejoined across messages.

    ``claude -p`` reports in ``result`` only the LAST assistant message. An answer too long for one
    message — past the per-message output limit — is continued in the next message, so ``result``
    held only its tail: the Series C plan (129,000 characters) arrived as 119,999 + 9,012, split
    mid-word at "pre|amble", and ``prosodia plan`` received the last 9,012. Series B's plan was cut
    the same way.

    The final answer is every assistant text block written after the last tool call (narration
    before a tool call is not part of it), joined as written: a continuation resumes mid-word.
    It is used only when ``result`` is exactly its tail; otherwise ``result`` stands unchanged.
    """
    pieces: list[str] = []
    for e in events:
        if e.get("type") != "assistant":
            continue
        for block in (e.get("message") or {}).get("content") or []:
            if not isinstance(block, dict):
                continue
            if block.get("type") == "tool_use":
                pieces = []
            elif block.get("type") == "text" and block.get("text"):
                pieces.append(block["text"])
    joined = "".join(pieces)
    tail = (result or "").rstrip()
    if tail and len(joined.rstrip()) > len(tail) and joined.rstrip().endswith(tail):
        return joined
    return result or ""


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
        # stream-json (which -p requires --verbose for) rather than json: json reports only the
        # last assistant message, and a long answer can span several — see final_answer_text.
        cmd = ["claude", "-p", "--output-format", "stream-json", "--verbose",
               "--permission-mode", "dontAsk"]
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
        events = []
        for line in proc.stdout.splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                events.append(json.loads(line))
            except json.JSONDecodeError:
                continue
        data = next((e for e in reversed(events) if e.get("type") == "result"), None)
        if data is None and len(events) == 1 and "result" in events[0]:
            data = events[0]  # a single --output-format json object
        if data is None:
            raise RuntimeError(f"claude -p returned no result event: {proc.stdout.strip()[-1000:]!r}")
        result = final_answer_text(events, data.get("result", ""))
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


def _extract_lexicon_yaml(raw: str) -> str:
    """Recover the bare lexicon YAML from a lexicographer response (drop a stray code
    fence or preamble; ensure a top-level ``lexicon:`` key)."""
    t = raw.strip()
    fence = re.search(r"```[A-Za-z0-9]*\s*\n(.*?)\n```", t, re.DOTALL)
    if fence:
        t = fence.group(1).strip()
    m = re.search(r"(?m)^lexicon:\s*$", t)
    if m:
        return t[m.start():].strip() + "\n"
    # The agent may have emitted a bare mapping without the wrapper key — wrap it.
    return "lexicon:\n" + t + "\n" if t else "lexicon: {}\n"


def build_lexicon(
    names: list[str],
    *,
    runner,
    prons=None,
    existing_lexicon: str | None = None,
    trace: Trace | None = None,
) -> str:
    """Run the Lexicographer: fetch each name's Wikipedia pronunciation (unless ``prons``
    is supplied), hand it plus the respelling guidelines to a dedicated agent, and return
    the lexicon YAML it produces (source spelling -> natural respelling). This is the
    delegated pronunciation step — the Planner emits the name list; it does NOT do this."""
    from dataclasses import asdict

    if prons is None:
        from prosodia.author.wiki_pron import fetch_pronunciations

        prons = fetch_pronunciations(names)
    rows = [p if isinstance(p, dict) else asdict(p) for p in prons]
    guidelines = _load_role("RESPELL_GUIDELINES")  # roles/RESPELL_GUIDELINES.md
    prompt = (
        "RESPELLING GUIDELINES (authoritative — follow exactly):\n\n"
        f"{guidelines}\n\n"
        + (f"EXISTING PROJECT LEXICON (preserve good entries):\n{existing_lexicon}\n\n"
           if existing_lexicon else "")
        + "NAMES + WIKIPEDIA PRONUNCIATION DATA (from wiki_pron.py):\n"
        + json.dumps(rows, ensure_ascii=False, indent=2)
        + "\n\nProduce the lexicon YAML now (only names that genuinely need help)."
    )
    text, _ = runner.run(prompt, system=_load_role("lexicographer"))
    yaml_text = _extract_lexicon_yaml(text)
    if trace:
        trace.append("lexicon", "lexicographer", names=len(names), chars=len(yaml_text))
    return yaml_text


_NOTE_HEADING = re.compile(r"^[#*\s]*([A-Z][A-Z ]{3,}?)[*:\s]*$")


def editor_improvements(notes: str) -> str:
    """The ``IMPROVEMENTS`` section of an editor verdict, or "" when it has nothing in it.

    The casework editor heads its notes BLOCKING / IMPROVEMENTS / CLEARED. A persona whose
    editor writes no such heading gets "" — and so no extra pass on a ready verdict.
    """
    kept, inside = [], False
    for line in notes.splitlines():
        m = _NOTE_HEADING.match(line)
        if m:
            inside = m.group(1).strip() == "IMPROVEMENTS"
            continue
        if inside:
            kept.append(line)
    text = "\n".join(kept).strip()
    return "" if re.fullmatch(r"(?i)\(?\s*(none|n/?a|nothing)\b[^\n]{0,40}", text or "none") else text


def author_episode(
    brief: str,
    *,
    runner,
    persona: Persona | None = None,
    lint_context: dict | None = None,
    trace: Trace | None = None,
    run: Run | None = None,
    max_rounds: int = 3,
) -> str:
    """Run the Writer <-> Editor loop until the Editor says ready (or max_rounds).

    The loop always ends on the writer: the last verdict's notes are applied in one final pass
    with no further review — its BLOCKING notes when rounds run out, its IMPROVEMENTS when it
    says ready. When a ``run`` is given, every round is persisted with enriched trace events:
    the Writer's prompt and its ``transcript.vN`` draft, and the Editor's verdict.
    A loop that exhausts ``max_rounds`` without approval is flagged ``warn`` — a
    signal the diagnosis pass can surface. ``trace`` (the thin log) is still honored.
    """
    persona = persona or Persona.resolve()
    writer_sys = persona.role("writer")
    editor_sys = persona.role("editor")
    notes = ""
    transcript = ""
    ready = False
    note_txt = ""
    last_round = 0
    brief_art = run.write_artifact("brief.md", brief, label="brief") if run is not None else None
    for rnd in range(1, max_rounds + 1):
        last_round = rnd
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

        # Hand the editor the deterministic counts rather than asking it to count. It cannot:
        # episode 2 came back `ready` with four forward references against a budget of three
        # and one inside the opening five minutes, both of which it is explicitly told to
        # count. A model judges well and tallies badly, so tally for it.
        measured = ""
        if lint_context is not None:
            from prosodia.author.scriptlint import lint_script

            findings = lint_script(transcript, **lint_context)
            if findings:
                measured = (
                    "MEASURED ON THIS DRAFT (counted mechanically — trust these over your own\n"
                    "counting, and treat every `error` line as BLOCKING):\n"
                    + "\n".join(f.render() for f in findings)
                    + "\n\n"
                )
        eprompt = f"{measured}BRIEF:\n{brief}\n\nTRANSCRIPT:\n{transcript}"
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

    # A loop that ends on an editor spends its most expensive call on a review nothing acts on.
    # Not ready: the notes describe defects in the draft about to ship. Ready: its IMPROVEMENTS
    # went to no one — about ninety across Series B, some of them accuracy defects filed one
    # heading too low. Either way, spend one last writer call applying them.
    improvements = editor_improvements(note_txt) if ready else ""
    if transcript.strip() and (not ready or improvements):
        if ready:
            task = (
                "--- FINAL FIX PASS. The editor approved this draft; there is no further review. ---\n"
                "Apply the editor's improvements below to your draft and return the corrected\n"
                "transcript. Change only what they name; when an item quotes a sentence, fix that\n"
                "sentence. Skip any item addressed to the producer or about the tooling rather than\n"
                "the script.\n\n"
                f"--- Improvements to apply ---\n{improvements}\n\n"
            )
        else:
            task = (
                "--- FINAL FIX PASS. There is no further review. ---\n"
                "Apply the editorial notes below to your previous draft and return the corrected\n"
                "transcript. Fix what they name and change nothing else. Skip any item addressed to\n"
                "the producer or about the tooling rather than the script.\n\n"
                f"--- Editorial notes to address ---\n{note_txt}\n\n"
            )
        fprompt = f"{brief}\n\n{task}--- Your previous draft (revise it) ---\n{transcript}"
        fixed, _ = runner.run(fprompt, system=writer_sys)
        fixed = _extract_transcript(fixed)
        problem = ""
        if not (fixed.strip() and "##" in fixed):
            problem = "final fix pass returned no usable transcript; kept the last draft"
        elif ready and lint_context is not None:
            # Nobody reviews this pass, so it must not undo what the editor approved.
            before = _lint_errors(transcript, lint_context)
            after = _lint_errors(fixed, lint_context)
            if after > before:
                problem = (f"final fix pass added script-lint errors ({before} -> {after}); "
                           "kept the approved draft")
        kept = not problem
        fix_round = last_round + 1
        if trace:
            trace.append("write", "writer", round=fix_round, chars=len(fixed), final_fix=True)
        if run is not None:
            run.write_artifact(f"stages/write.r{fix_round}/prompt.md", fprompt)
            art = run.write_artifact(
                f"stages/write.r{fix_round}/transcript.final.md",
                fixed if kept else transcript, label="final fix",
            )
            run.event(
                "write", "writer", round=fix_round, outputs=[art],
                status="ok" if kept else "warn", chars=len(fixed),
                warnings=[problem] if problem else [], final_fix=True, after_ready=ready,
            )
            run.write_index()
        if kept:
            transcript = fixed
    return transcript


def _lint_errors(transcript: str, lint_context: dict) -> int:
    from prosodia.author.scriptlint import ERROR, lint_script

    return sum(1 for f in lint_script(transcript, **lint_context) if f.level == ERROR)


# ---- the delivery pass ------------------------------------------------------------------
#
# The tone specialist (roles/tone.md) owns DELIVERY: pauses, tone shifts, emphasis. It was
# written, tuned against measured narration, run once by hand for eu_history_v2 — and never
# wired into `write`. Two whole casework series went to render with the writer's markup alone:
# no mid-clause pause in 22 episodes, `pointed` carried by whole beats. This is that pass.

TONE_ATTEMPTS = 2


def _spoken_words(text: str) -> list[str]:
    from prosodia.author.scriptlint import spoken_body

    return re.findall(r"[A-Za-z0-9]+(?:['\u2019][A-Za-z]+)?", spoken_body(text))


def _beat_titles(text: str) -> list[str]:
    return [re.sub(r"\{[^{}]*\}", "", h).strip() for h in re.findall(r"(?m)^## (.*)$", text)]


def invariance_problems(original: str, toned: str) -> list[str]:
    """What the tone pass changed that it may not: a spoken word, or the beat structure.

    The transcript is the source of truth (CLAUDE.md); the specialist may move markup and
    nothing else. Returned as quotable diffs so a retry can be told exactly what to restore.
    """
    import difflib

    problems: list[str] = []
    a, b = _spoken_words(original), _spoken_words(toned)
    if a != b:
        sm = difflib.SequenceMatcher(a=a, b=b, autojunk=False)
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            if op == "equal":
                continue
            was = " ".join(a[max(0, i1 - 4):i2 + 4])
            now = " ".join(b[max(0, j1 - 4):j2 + 4])
            problems.append(f'{op}: the writer said "{was}" — your version says "{now}"')
            if len(problems) >= 8:
                problems.append("(further differences not listed)")
                break
    if _beat_titles(original) != _beat_titles(toned):
        problems.append("beat titles were changed, or beats were added or removed")
    return problems


def tone_pass(
    transcript: str,
    *,
    runner,
    persona: Persona,
    run: Run | None = None,
    attempts: int = TONE_ATTEMPTS,
) -> tuple[str, list[str]]:
    """Refine the delivery markup of a finished transcript. Returns (transcript, warnings).

    Every attempt is checked mechanically: a spoken word or a beat changed rejects it outright;
    a delivery `error` left standing (scriptlint.lint_delivery) earns one retry with the
    findings quoted. The best clean attempt wins; if none keeps the words, the writer's own
    markup ships and the pass says so.
    """
    from prosodia.author.scriptlint import lint_delivery

    if not persona.has_role("tone"):
        return transcript, [f"persona '{persona.name}' has no tone role; delivery left as written"]
    system = persona.role("tone")
    before = lint_delivery(transcript)
    if run is not None:
        run.write_artifact("stages/delivery/before.md", transcript, label="before the tone pass")
    measured = "\n".join(f.render() for f in before) or "  (nothing flagged)"
    feedback = ""
    best: tuple[int, str] | None = None
    for k in range(1, attempts + 1):
        prompt = (
            "MEASURED ON THE WRITER'S DELIVERY MARKUP (counted mechanically — resolve every "
            "`error`; the warnings are where to look):\n"
            f"{measured}\n\n"
            + (
                "YOUR PREVIOUS ATTEMPT WAS REJECTED. Start again from the transcript below and "
                f"avoid this:\n{feedback}\n\n" if feedback else ""
            )
            + f"TRANSCRIPT:\n{transcript}"
        )
        raw, _ = runner.run(prompt, system=system)
        toned = _extract_transcript(raw)
        problems = invariance_problems(transcript, toned) if "##" in toned else ["no transcript returned"]
        errors = [f for f in lint_delivery(toned) if f.level == "error"] if not problems else []
        if run is not None:
            run.write_artifact(f"stages/delivery.r{k}/prompt.md", prompt)
            art = run.write_artifact(f"stages/delivery.r{k}/transcript.toned.md", toned or raw,
                                     label=f"toned r{k}")
            run.event(
                "delivery", "tone", round=k, outputs=[art],
                status="error" if problems else ("warn" if errors else "ok"),
                warnings=problems or [f.render().strip() for f in errors],
                words_kept=not problems, delivery_errors=len(errors),
            )
            run.write_index()
        if problems:
            feedback = ("You changed what is SPOKEN. Only markup may change; every word, its order "
                        "and the beat titles are fixed:\n" + "\n".join(problems))
            continue
        if best is None or len(errors) < best[0]:
            best = (len(errors), toned)
        if not errors:
            break
        feedback = "These delivery errors were still in your version:\n" + "\n".join(
            f.render() for f in errors)
    if best is None:
        return transcript, [f"tone pass changed spoken words on all {attempts} attempt(s); "
                            f"the writer's delivery markup was kept"]
    return best[1], ([f"tone pass left {best[0]} delivery error(s) standing"] if best[0] else [])
