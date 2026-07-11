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


def test_author_episode_stops_at_max_rounds():
    runner = FakeRunner(drafts=["d1", "d2", "d3"], verdicts=[{"ready": False, "notes": "n"}] * 3)
    out = author_episode("BRIEF", runner=runner, max_rounds=3)
    assert out == "d3"


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
        payload = {"result": json.dumps({"ready": True, "notes": "ok"}), "structured_output": None}
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
    runner = FakeRunner(drafts=["d1", "d2", "d3"], verdicts=[{"ready": False, "notes": "n"}] * 3)
    author_episode("BRIEF", runner=runner, run=run, max_rounds=3)
    last_edit = [e for e in run.events() if e.stage == "edit"][-1]
    assert last_edit.status == "warn"
    assert "max_rounds" in last_edit.warnings[0]
    assert run.rollup_status() == "warn"
