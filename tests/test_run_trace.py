from prosodia.core.trace import Artifact, Run, RunIndex


def test_write_artifact_hashes_and_persists(tmp_path):
    run = Run(tmp_path / "run")
    art = run.write_artifact("stages/06_compile/ir.json", '{"segments": []}', label="ir")
    assert isinstance(art, Artifact)
    assert art.rel == "stages/06_compile/ir.json"
    assert art.size == len('{"segments": []}')
    assert len(art.sha256) == 64
    assert (run.dir / "stages/06_compile/ir.json").read_text() == '{"segments": []}'
    # ref() re-hashes an existing file to the same digest
    assert run.ref("stages/06_compile/ir.json").sha256 == art.sha256


def test_events_get_sequential_ids_and_auto_parent(tmp_path):
    run = Run(tmp_path / "run")
    e1 = run.event("plan", "planner")
    e2 = run.event("write", "writer", round=1)
    e3 = run.event("edit", "editor", round=1)
    assert [e.id for e in (e1, e2, e3)] == ["e01", "e02", "e03"]
    assert e1.parent is None
    assert e2.parent == "e01" and e3.parent == "e02"


def test_warnings_promote_status_and_rollup(tmp_path):
    run = Run(tmp_path / "run")
    run.event("compile", "compile")  # ok
    ev = run.event("tone", "tone-specialist", warnings=["seg 4: unknown tone 'brooding' -> measured"])
    assert ev.status == "warn"  # warnings promote an unset ok -> warn
    assert run.rollup_status() == "warn"
    run.event("submit", "submit", status="error")
    assert run.rollup_status() == "error"  # worst wins


def test_index_roundtrips_and_run_resumes(tmp_path):
    run = Run(tmp_path / "run")
    run.event("plan", "planner")
    run.event("write", "writer", round=1, outputs=[run.write_artifact("stages/02_write.r1/transcript.v1.md", "hi")])
    idx_path = run.write_index(episode=6, title="The euro")
    idx = RunIndex.model_validate_json(idx_path.read_text())
    assert idx.episode == 6 and idx.status == "ok" and len(idx.events) == 2
    assert idx.events[1].outputs[0].rel == "stages/02_write.r1/transcript.v1.md"

    # Re-opening the same run continues the counter (append-only history).
    run2 = Run(tmp_path / "run")
    assert len(run2.events()) == 2
    assert run2.event("compile", "compile").id == "e03"


def test_meta_captures_stage_extras(tmp_path):
    run = Run(tmp_path / "run")
    ev = run.event("edit", "editor", round=2, ready=True, notes="tighten the open")
    assert ev.meta["ready"] is True and ev.meta["notes"] == "tighten the open"
    # survives a round-trip through the event log
    reloaded = Run(tmp_path / "run").events()[0]
    assert reloaded.meta["ready"] is True
