import pytest

from prosodia.author.submit import package_job
from prosodia.core import protocol
from prosodia.core.ir import EpisodeIR, RenderPlan, Segment, SegmentParams


def _ir():
    return EpisodeIR(episode=1, voice="narrator", segments=[])


def _plan():
    return RenderPlan(voice="narrator")


def test_package_job_produces_valid_inbox_job(tmp_path):
    ir = EpisodeIR(
        episode=1, voice="narrator", seed=7,
        segments=[Segment(id=0, spoken_text="hi", chunks=["hi"])],
    )
    plan = RenderPlan(
        voice="narrator", seed=7,
        params=[SegmentParams(segment_id=0, exaggeration=0.4, cfg_weight=0.5, temperature=0.75)],
    )
    dest = package_job(tmp_path, "ep1", ir, plan)

    assert dest == tmp_path / protocol.INBOX / "ep1"
    assert (dest / "ir.json").exists() and (dest / "render_plan.json").exists()
    assert (dest / protocol.MANIFEST_NAME).exists()
    assert protocol.validate_job(dest) == []  # manifest matches the payload
    assert not (tmp_path / protocol.BUILDING / "ep1").exists()  # staging cleaned up


def test_package_job_with_voice_ref(tmp_path):
    vr = tmp_path / "voice.wav"
    vr.write_bytes(b"RIFFfake")
    dest = package_job(
        tmp_path, "ep2",
        EpisodeIR(episode=2, voice="narrator", segments=[]),
        RenderPlan(voice="narrator"),
        voice_ref=vr,
    )
    assert (dest / "voice.wav").exists()
    assert protocol.validate_job(dest) == []


def test_status_not_in_manifest(tmp_path):
    # A status.json written into a claimed job must not break manifest validation.
    dest = package_job(
        tmp_path, "ep3",
        EpisodeIR(episode=3, voice="narrator", segments=[]),
        RenderPlan(voice="narrator"),
    )
    (dest / protocol.STATUS_NAME).write_text(
        protocol.JobStatus(job_id="ep3", state="rendering").to_json(), encoding="utf-8"
    )
    assert protocol.validate_job(dest) == []


def test_resubmit_same_job_id_overwrites(tmp_path):  # finding 3 (Windows rename)
    package_job(tmp_path, "dup", _ir(), _plan())
    dest = package_job(tmp_path, "dup", _ir(), _plan())  # must not raise
    assert protocol.validate_job(dest) == []


def test_missing_voice_ref_errors(tmp_path):  # finding 11
    with pytest.raises(FileNotFoundError):
        package_job(tmp_path, "ep", _ir(), _plan(), voice_ref=tmp_path / "nope.wav")


def test_basename_collision_errors(tmp_path):  # finding 11
    d1 = tmp_path / "a"
    d2 = tmp_path / "b"
    d1.mkdir()
    d2.mkdir()
    (d1 / "clip.wav").write_bytes(b"a")
    (d2 / "clip.wav").write_bytes(b"b")
    with pytest.raises(ValueError, match="basename collision"):
        package_job(tmp_path, "ep", _ir(), _plan(), extra_files=[d1 / "clip.wav", d2 / "clip.wav"])
