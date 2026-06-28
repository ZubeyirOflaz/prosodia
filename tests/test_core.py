from pathlib import Path

from prosodia.core import protocol
from prosodia.core.intents import Intent, rate_to_multiplier
from prosodia.core.ir import EpisodeIR, RenderPlan, Segment, SegmentParams
from prosodia.core.trace import Trace


def test_ir_round_trip():
    ir = EpisodeIR(
        episode=1,
        title="T",
        voice="narrator",
        seed=7,
        segments=[
            Segment(
                id=0,
                beat_title="b",
                intent=Intent(tone="somber", rate="slow"),
                spoken_text="hello",
                chunks=["hello"],
            )
        ],
    )
    again = EpisodeIR.from_json(ir.to_json())
    assert again == ir
    assert again.segments[0].intent.tone == "somber"


def test_rate_multiplier():
    assert rate_to_multiplier("normal") == 1.0
    assert rate_to_multiplier("slow") < 1.0
    assert rate_to_multiplier(1.15) == 1.15
    assert Intent(rate="fast").rate_multiplier > 1.0


def test_render_plan_round_trip():
    rp = RenderPlan(
        voice="narrator",
        seed=7,
        params=[SegmentParams(segment_id=0, exaggeration=0.3, cfg_weight=0.5, temperature=0.8)],
    )
    assert RenderPlan.from_json(rp.to_json()) == rp


def test_manifest_validate_and_tamper(tmp_path: Path):
    job = tmp_path / "job1"
    job.mkdir()
    (job / "ir.json").write_text("{}", encoding="utf-8")
    (job / "render_plan.json").write_text("{}", encoding="utf-8")
    protocol.write_manifest(job, protocol.compute_manifest(job, "job1"))
    assert protocol.validate_job(job) == []
    # Tamper after the manifest was written.
    (job / "ir.json").write_text("{ }", encoding="utf-8")
    assert any("ir.json" in p for p in protocol.validate_job(job))


def test_manifest_missing_file(tmp_path: Path):
    job = tmp_path / "job2"
    job.mkdir()
    (job / "a.txt").write_text("hi", encoding="utf-8")
    protocol.write_manifest(job, protocol.compute_manifest(job, "job2"))
    (job / "a.txt").unlink()
    assert any("missing" in p for p in protocol.validate_job(job))


def test_atomic_publish(tmp_path: Path):
    building = tmp_path / "building" / "job3"
    building.mkdir(parents=True)
    (building / "x").write_text("y", encoding="utf-8")
    dest = protocol.atomic_publish(building, tmp_path / "inbox")
    assert dest.exists() and (dest / "x").read_text(encoding="utf-8") == "y"
    assert not building.exists()


def test_validate_unreadable_manifest(tmp_path: Path):  # finding 22
    job = tmp_path / "jobu"
    job.mkdir()
    (job / "a.txt").write_text("hi", encoding="utf-8")
    (job / protocol.MANIFEST_NAME).write_text("{not json", encoding="utf-8")
    problems = protocol.validate_job(job)
    assert any("unreadable" in p for p in problems)


def test_validate_unlisted_file(tmp_path: Path):  # finding 22
    job = tmp_path / "jobl"
    job.mkdir()
    (job / "a.txt").write_text("hi", encoding="utf-8")
    protocol.write_manifest(job, protocol.compute_manifest(job, "jobl"))
    (job / "b.txt").write_text("extra", encoding="utf-8")
    assert any("unlisted file present: b.txt" in p for p in protocol.validate_job(job))


def test_validate_size_mismatch(tmp_path: Path):  # finding 22
    job = tmp_path / "jobs"
    job.mkdir()
    (job / "a.txt").write_text("hello", encoding="utf-8")
    protocol.write_manifest(job, protocol.compute_manifest(job, "jobs"))
    (job / "a.txt").write_text("hello world longer", encoding="utf-8")  # size changes
    assert any("size mismatch: a.txt" in p for p in protocol.validate_job(job))


def test_validate_nested_dir_posix_names(tmp_path: Path):  # finding 22
    job = tmp_path / "jobn"
    (job / "sub").mkdir(parents=True)
    (job / "sub" / "c.txt").write_text("nested", encoding="utf-8")
    manifest = protocol.compute_manifest(job, "jobn")
    assert any(e.name == "sub/c.txt" for e in manifest.files)  # forward-slash
    protocol.write_manifest(job, manifest)
    assert protocol.validate_job(job) == []


def test_missing_manifest_is_not_ready(tmp_path: Path):  # finding 23
    job = tmp_path / "jobm"
    job.mkdir()
    (job / "ir.json").write_text("{}", encoding="utf-8")
    (job / "render_plan.json").write_text("{}", encoding="utf-8")
    problems = protocol.validate_job(job)
    assert problems == ["manifest.json is missing (job not finished syncing)"]


def test_status_excluded_from_payload(tmp_path: Path):  # finding 23
    # A job with only manifest + status (no payload) and an empty file list
    # validates clean — locking the STATUS_NAME exclusion.
    job = tmp_path / "jobst"
    job.mkdir()
    protocol.write_manifest(job, protocol.compute_manifest(job, "jobst"))  # empty payload
    (job / protocol.STATUS_NAME).write_text(
        protocol.JobStatus(job_id="jobst").to_json(), encoding="utf-8"
    )
    assert protocol.validate_job(job) == []


def test_validate_ignores_sync_temp(tmp_path: Path):  # finding 10
    job = tmp_path / "jobt"
    job.mkdir()
    (job / "a.txt").write_text("hi", encoding="utf-8")
    protocol.write_manifest(job, protocol.compute_manifest(job, "jobt"))
    (job / ".syncthing.tmp").write_text("partial", encoding="utf-8")
    (job / "~$lock").write_text("x", encoding="utf-8")
    assert protocol.validate_job(job) == []  # temp files do not block the job


def test_atomic_publish_creates_inbox(tmp_path: Path):  # finding 24
    building = tmp_path / "building" / "jobp"
    building.mkdir(parents=True)
    (building / "x").write_text("y", encoding="utf-8")
    dest = protocol.atomic_publish(building, tmp_path / "deep" / "inbox")
    assert dest.exists() and (dest / "x").read_text(encoding="utf-8") == "y"


def test_atomic_publish_overwrites_existing(tmp_path: Path):  # findings 3, 24
    inbox = tmp_path / "inbox"
    for content in ("first", "second"):
        building = tmp_path / "building" / "dup"
        building.mkdir(parents=True)
        (building / "x").write_text(content, encoding="utf-8")
        dest = protocol.atomic_publish(building, inbox)
    assert (dest / "x").read_text(encoding="utf-8") == "second"  # re-submit wins, no crash


def test_job_status_defaults(tmp_path: Path):  # finding 24
    import json

    s = protocol.JobStatus(job_id="x")
    assert s.state == "queued" and s.message == "" and s.progress == 0.0
    data = json.loads(s.to_json())
    assert data["state"] == "queued" and data["progress"] == 0.0 and data["job_id"] == "x"


def test_trace(tmp_path: Path):
    t = Trace(tmp_path / "trace.jsonl")
    t.append("write", "writer", draft="v1", note="first")
    t.append("edit", "editor", ready=False)
    events = t.read()
    assert len(events) == 2
    assert events[0]["role"] == "writer"
    assert events[1]["ready"] is False
