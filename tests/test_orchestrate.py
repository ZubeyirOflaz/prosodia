import pytest

from prosodia.author import orchestrate
from prosodia.author.orchestrate import (
    EDITOR_SCHEMA,
    ClaudeRunner,
    author_episode,
    plan_series,
)
from prosodia.core.trace import Run, Trace


class FakeRunner:
    """A stand-in for ClaudeRunner: serves canned drafts/verdicts, records calls."""

    def __init__(self, drafts, verdicts):
        self.drafts = list(drafts)
        self.verdicts = list(verdicts)
        self.calls = []

    def run(self, prompt, *, system=None, schema=None):
        self.calls.append(("schema" if schema else "text", prompt))
        if schema:
            return "", self.verdicts.pop(0)
        return self.drafts.pop(0), None


def test_author_episode_loops_until_ready():
    runner = FakeRunner(
        drafts=["draft1", "draft2"],
        verdicts=[{"ready": False, "notes": "fix the opening"}, {"ready": True, "notes": ""}],
    )
    out = author_episode("BRIEF", runner=runner, max_rounds=3)
    assert out == "draft2"  # accepted on the second round
    assert sum(1 for k, _ in runner.calls if k == "text") == 2  # writer twice
    assert sum(1 for k, _ in runner.calls if k == "schema") == 2  # editor twice
    # The editor's notes are fed back into the writer's next prompt.
    second_writer_prompt = [p for k, p in runner.calls if k == "text"][1]
    assert "fix the opening" in second_writer_prompt


def test_an_unresolved_loop_ends_on_a_writer_fix_not_another_review():
    """The last editorial round is otherwise pure cost.

    Its notes describe defects in the draft that is about to ship, and nothing downstream
    acts on them — so the most expensive call in the run buys a review nobody reads. Spend
    it on a writer pass that applies the notes instead.
    """
    runner = FakeRunner(
        drafts=["## d1", "## d2", "## d3", "## fixed"],
        verdicts=[{"ready": False, "notes": "fix the third-country variant"}] * 3,
    )
    out = author_episode("BRIEF", runner=runner, max_rounds=3)
    assert out == "## fixed"
    # three writer rounds, three editor rounds, then ONE writer call and no further review
    kinds = [k for k, _ in runner.calls]
    assert kinds == ["text", "schema"] * 3 + ["text"]
    final_prompt = runner.calls[-1][1]
    assert "FINAL FIX PASS" in final_prompt
    assert "fix the third-country variant" in final_prompt


def test_a_degenerate_final_fix_keeps_the_last_good_draft():
    runner = FakeRunner(
        drafts=["## d1", "## d2", ""],
        verdicts=[{"ready": False, "notes": "n"}] * 2,
    )
    assert author_episode("BRIEF", runner=runner, max_rounds=2) == "## d2"


def test_a_ready_verdict_skips_the_fix_pass():
    runner = FakeRunner(drafts=["## d1"], verdicts=[{"ready": True, "notes": "ok"}])
    assert author_episode("BRIEF", runner=runner, max_rounds=3) == "## d1"
    assert [k for k, _ in runner.calls] == ["text", "schema"]


def test_plan_series_calls_planner():
    runner = FakeRunner(drafts=["OUTLINE"], verdicts=[])
    assert plan_series("goal", runner=runner) == "OUTLINE"


def test_editor_schema_shape():
    assert EDITOR_SCHEMA["required"] == ["ready", "notes"]


def test_author_episode_traces(tmp_path):  # finding 25
    trace = Trace(tmp_path / "trace.jsonl")
    runner = FakeRunner(
        drafts=["draft1", "draft2"],
        verdicts=[{"ready": False, "notes": "fix it"}, {"ready": True, "notes": ""}],
    )
    author_episode("BRIEF", runner=runner, trace=trace, max_rounds=3)
    events = trace.read()
    writes = [e for e in events if e["step"] == "write"]
    edits = [e for e in events if e["step"] == "edit"]
    assert [e["round"] for e in writes] == [1, 2]
    assert [e["round"] for e in edits] == [1, 2]
    assert edits[0]["ready"] is False and edits[1]["ready"] is True


def test_author_episode_none_verdict_is_ready(tmp_path):  # finding 25
    # A runner returning structured=None on the editor call is treated as ready.
    runner = FakeRunner(drafts=["only-draft"], verdicts=[None])
    out = author_episode("BRIEF", runner=runner, max_rounds=3)
    assert out == "only-draft"
    assert sum(1 for k, _ in runner.calls if k == "text") == 1  # ended after round 1


def test_first_round_prompt_has_none_placeholders():  # finding 25
    runner = FakeRunner(drafts=["d"], verdicts=[{"ready": True, "notes": ""}])
    author_episode("BRIEF", runner=runner, max_rounds=1)
    first_writer_prompt = [p for k, p in runner.calls if k == "text"][0]
    assert first_writer_prompt.count("(none)") == 2  # notes + previous draft


def test_claude_runner_missing_cli(monkeypatch):  # finding 26
    monkeypatch.setattr(orchestrate.shutil, "which", lambda _: None)
    with pytest.raises(RuntimeError, match="claude"):
        ClaudeRunner().run("hi")


def test_claude_runner_parses_structured_from_result(monkeypatch):  # finding 26
    import json
    import subprocess

    monkeypatch.setattr(orchestrate.shutil, "which", lambda _: "/usr/bin/claude")

    def fake_run(cmd, **kwargs):
        # structured_output is null; result holds the JSON the schema expects.
        payload = {"type": "result", "result": json.dumps({"ready": True, "notes": "ok"}),
                   "structured_output": None}
        return subprocess.CompletedProcess(cmd, 0, stdout=json.dumps(payload), stderr="")

    monkeypatch.setattr(orchestrate.subprocess, "run", fake_run)
    result, structured = ClaudeRunner().run("prompt", schema=EDITOR_SCHEMA)
    assert structured == {"ready": True, "notes": "ok"}


def test_author_episode_run_versions_rounds(tmp_path):
    run = Run(tmp_path / "run")
    runner = FakeRunner(
        drafts=["draft1", "draft2"],
        verdicts=[{"ready": False, "notes": "fix open"}, {"ready": True, "notes": ""}],
    )
    author_episode("BRIEF", runner=runner, run=run, max_rounds=3)

    # Each round is kept as its own versioned draft (no overwrite).
    assert (run.dir / "stages/write.r1/transcript.v1.md").read_text() == "draft1"
    assert (run.dir / "stages/write.r2/transcript.v2.md").read_text() == "draft2"
    assert (run.dir / "brief.md").read_text() == "BRIEF"

    writes = [e for e in run.events() if e.stage == "write"]
    edits = [e for e in run.events() if e.stage == "edit"]
    assert [e.round for e in writes] == [1, 2]
    assert edits[0].meta["ready"] is False and edits[1].meta["ready"] is True
    assert edits[0].status == "ok"  # not-ready mid-loop is normal, not a warning
    assert run.rollup_status() == "ok"


def test_author_episode_run_flags_unresolved_loop(tmp_path):
    run = Run(tmp_path / "run")
    runner = FakeRunner(
        drafts=["## d1", "## d2", "## d3", "## fixed"],
        verdicts=[{"ready": False, "notes": "n"}] * 3,
    )
    author_episode("BRIEF", runner=runner, run=run, max_rounds=3)
    last_edit = [e for e in run.events() if e.stage == "edit"][-1]
    assert last_edit.status == "warn"
    assert "max_rounds" in last_edit.warnings[0]
    assert run.rollup_status() == "warn"
    # and the fix pass is recorded as its own writer round, after that verdict
    last_write = [e for e in run.events() if e.stage == "write"][-1]
    assert last_write.round == 4


def test_the_editor_is_handed_the_counts_rather_than_asked_to_count():
    """Episode 2 came back `ready` with four forward references against a budget of three,
    and one inside the opening five minutes — both things the editor is explicitly told to
    count. A model judges well and tallies badly, so the tally is done for it."""
    draft = "---\nepisode: 1\n---\n\n## B\n" + ("Filler. " * 900) + (
        "We meet that in Episode 4. Episode 7 takes it up. Episode 9 has it. Episode 12 lands it."
    )
    runner = FakeRunner(drafts=[draft], verdicts=[{"ready": True, "notes": "ok"}])
    author_episode("BRIEF", runner=runner, max_rounds=1,
                   lint_context={"episode": 1, "target_minutes": 27})
    editor_prompt = next(p for k, p in runner.calls if k == "schema")
    assert "MEASURED ON THIS DRAFT" in editor_prompt
    assert "forward-refs" in editor_prompt
    assert "treat every `error` line as BLOCKING" in editor_prompt


def test_no_lint_context_means_no_measurement_block():
    runner = FakeRunner(drafts=["## d1"], verdicts=[{"ready": True, "notes": "ok"}])
    author_episode("BRIEF", runner=runner, max_rounds=1)
    editor_prompt = next(p for k, p in runner.calls if k == "schema")
    assert "MEASURED ON THIS DRAFT" not in editor_prompt
    assert editor_prompt.startswith("BRIEF:")


# ---- the delivery pass ----------------------------------------------------------------

WRITTEN = (
    "---\nepisode: 1\ntitle: T\ndefaults: { tone: measured, rate: normal }\n---\n\n"
    "## The machine {tone: pointed}\n"
    "The radar saw her six seconds out, and the system changed its mind about her repeatedly.\n\n"
    "## The rule {tone: precise}\n"
    "The Directive says, and I am quoting: a product is defective where it lacks expected safety.\n"
)
TONED = (
    "---\nepisode: 1\ntitle: T\ndefaults: { tone: measured, rate: normal }\n---\n\n"
    "## The machine {tone: measured}\n"
    "The radar saw her six seconds out, {pause: 1.2} and {tone: pointed} the system changed its "
    "mind about her *repeatedly*. {tone: measured}\n\n"
    "## The rule {tone: precise}\n"
    "The Directive says, and I am quoting:\n\n> a product is defective where it lacks expected safety.\n"
)


class ToneRunner:
    def __init__(self, outputs):
        self.outputs, self.prompts = list(outputs), []

    def run(self, prompt, *, system=None, schema=None):
        self.prompts.append(prompt)
        return self.outputs.pop(0), None


def _casework():
    from prosodia.author.persona import Persona

    return Persona.resolve("casework")


def test_markup_changes_are_not_invariance_problems():
    assert orchestrate.invariance_problems(WRITTEN, TONED) == []


def test_a_changed_word_or_beat_is_an_invariance_problem():
    reworded = TONED.replace("repeatedly", "again and again")
    assert any("repeatedly" in p for p in orchestrate.invariance_problems(WRITTEN, reworded))
    retitled = TONED.replace("## The rule", "## The test")
    assert orchestrate.invariance_problems(WRITTEN, retitled)


def test_tone_pass_accepts_markup_only_and_fixes_the_header_tone():
    runner = ToneRunner([TONED])
    out, warns = orchestrate.tone_pass(WRITTEN, runner=runner, persona=_casework())
    assert out.strip() == TONED.strip() and warns == []
    assert "header-tone" in runner.prompts[0]          # the specialist is told what was measured


def test_tone_pass_rejects_a_changed_word_and_retries_with_the_diff(tmp_path):
    runner = ToneRunner([TONED.replace("repeatedly", "again and again"), TONED])
    run = Run(tmp_path / "run")
    out, warns = orchestrate.tone_pass(WRITTEN, runner=runner, persona=_casework(), run=run)
    assert out.strip() == TONED.strip() and warns == []
    assert "repeatedly" in runner.prompts[1] and "REJECTED" in runner.prompts[1]
    assert [e.status for e in run.events() if e.stage == "delivery"] == ["error", "ok"]


def test_tone_pass_keeps_the_writers_markup_when_every_attempt_changes_words():
    bad = TONED.replace("six seconds", "five seconds")
    out, warns = orchestrate.tone_pass(WRITTEN, runner=ToneRunner([bad, bad]), persona=_casework())
    assert out == WRITTEN
    assert warns and "kept" in warns[0]


def test_tone_pass_retries_once_on_a_delivery_error_and_keeps_the_better_attempt():
    still_headed = TONED.replace("## The machine {tone: measured}", "## The machine {tone: pointed}")
    runner = ToneRunner([still_headed, TONED])
    out, warns = orchestrate.tone_pass(WRITTEN, runner=runner, persona=_casework())
    assert out.strip() == TONED.strip() and len(runner.prompts) == 2
    assert "header-tone" in runner.prompts[1]


# ---- the final answer, across messages (2026-10-09) ----------------------------------------

def _stream(*events):
    import json

    return "\n".join(json.dumps(e) for e in events) + "\n"


def _say(*blocks):
    return {"type": "assistant", "message": {"content": list(blocks)}}


def _text(t):
    return {"type": "text", "text": t}


def test_an_answer_split_across_messages_is_rejoined():
    """The Series C plan arrived as two messages split mid-word; `result` held only the tail."""
    events = [
        _say(_text("Reading the docket first.")),
        _say({"type": "tool_use", "name": "Read", "input": {}}),
        {"type": "user", "message": {"content": [{"type": "tool_result", "content": "..."}]}},
        _say(_text("# PLAN\n\n## Episode 1 — x\n\nthe pre")),
        _say(_text("amble recital and the rest")),
        {"type": "result", "result": "amble recital and the rest"},
    ]
    assert orchestrate.final_answer_text(events, events[-1]["result"]) == \
        "# PLAN\n\n## Episode 1 — x\n\nthe preamble recital and the rest"


def test_a_single_message_answer_is_unchanged():
    events = [_say(_text("Checking.")), _say({"type": "tool_use", "name": "Read", "input": {}}),
              _say(_text("The answer.")), {"type": "result", "result": "The answer."}]
    assert orchestrate.final_answer_text(events, "The answer.") == "The answer."


def test_result_stands_when_it_is_not_the_tail_of_the_text():
    events = [_say(_text("something else entirely")), {"type": "result", "result": "The answer."}]
    assert orchestrate.final_answer_text(events, "The answer.") == "The answer."


def test_runner_reads_the_stream_and_returns_the_whole_answer(monkeypatch):
    import subprocess

    monkeypatch.setattr(orchestrate.shutil, "which", lambda _: "/usr/bin/claude")
    seen = {}

    def fake_run(cmd, **kwargs):
        seen["cmd"] = cmd
        out = _stream({"type": "system", "subtype": "init"}, _say(_text("first half, pre")),
                      _say(_text("amble second half")),
                      {"type": "result", "result": "amble second half", "is_error": False})
        return subprocess.CompletedProcess(cmd, 0, stdout=out, stderr="")

    monkeypatch.setattr(orchestrate.subprocess, "run", fake_run)
    result, structured = ClaudeRunner().run("prompt")
    assert result == "first half, preamble second half" and structured is None
    assert "stream-json" in seen["cmd"] and "--verbose" in seen["cmd"]
