"""Tests for the deterministic, backend-injectable render loop (finding 29).

Requires numpy (render.py imports it) and soundfile (write_wav). Skipped on the
strict authoring install where they are absent. ffmpeg is intentionally allowed
to fail so the peak_normalize fallback path produces the output .wav.
"""

import pytest

np = pytest.importorskip("numpy")
pytest.importorskip("soundfile")

from prosodia.core.ir import EpisodeIR, RenderPlan, Segment, SegmentParams  # noqa: E402
from prosodia.render import render as R  # noqa: E402


class FakeBackend:
    def __init__(self, sample_rate=16000, length=4000):
        self._sr = sample_rate
        self._length = length
        self.calls = []

    @property
    def sample_rate(self):
        return self._sr

    def load(self):
        pass

    def generate(self, text, **kwargs):
        self.calls.append((text, kwargs))
        # A simple non-silent tone so trim_silence keeps it.
        return (np.ones(self._length, dtype=np.float32) * 0.5)


class ScriptedValidator:
    """Returns scores from a scripted list, cycling per chunk."""

    def __init__(self, scores):
        self._scores = list(scores)
        self._i = 0

    def score(self, wav, sr, text):
        s = self._scores[self._i % len(self._scores)]
        self._i += 1
        return s


def _write_job(tmp_path, ir, plan):
    (tmp_path / "ir.json").write_text(ir.to_json(), encoding="utf-8")
    (tmp_path / "render_plan.json").write_text(plan.to_json(), encoding="utf-8")
    return tmp_path


def _simple_ir(voice="", seed=7):
    return EpisodeIR(
        episode=1, voice=voice, seed=seed,
        segments=[Segment(id=0, pause_before_ms=500, spoken_text="hello", chunks=["hello"])],
    )


def _simple_plan(voice=""):
    return RenderPlan(
        voice=voice, seed=7,
        params=[SegmentParams(segment_id=0, exaggeration=0.4, cfg_weight=0.5,
                              temperature=0.75, rate_multiplier=1.0)],
    )


def test_resolve_voice_ref_prefers_job_wav(tmp_path):
    (tmp_path / "bundled.wav").write_bytes(b"RIFFfake")
    voices = tmp_path / "voices"
    voices.mkdir()
    (voices / "narrator.wav").write_bytes(b"RIFFfake2")
    ref = R._resolve_voice_ref(_simple_ir(voice="narrator"), tmp_path, str(voices))
    assert ref.endswith("bundled.wav")  # job-dir clip wins over voices_dir


def test_resolve_voice_ref_preset_returns_none(tmp_path):
    ref = R._resolve_voice_ref(_simple_ir(voice="preset:foo"), tmp_path, None)
    assert ref is None


def test_render_job_fast_preview_one_generate_per_chunk(tmp_path):
    job = _write_job(tmp_path, _simple_ir(), _simple_plan())
    backend = FakeBackend()
    out = R.render_job(job, tmp_path / "episode.wav", backend=backend, fast_preview=True)
    assert out.exists() and out.suffix == ".wav"
    assert len(backend.calls) == 1  # one chunk, one candidate


def test_render_job_passes_rate_multiplier(tmp_path):
    plan = RenderPlan(
        voice="", seed=7,
        params=[SegmentParams(segment_id=0, exaggeration=0.4, cfg_weight=0.5,
                              temperature=0.75, rate_multiplier=0.9)],
    )
    job = _write_job(tmp_path, _simple_ir(), plan)
    backend = FakeBackend()
    R.render_job(job, tmp_path / "episode.wav", backend=backend, fast_preview=True)
    assert backend.calls[0][1]["rate_multiplier"] == 0.9  # finding 1: rate threaded through


def test_render_job_final_picks_best_and_stops_early(tmp_path):
    job = _write_job(tmp_path, _simple_ir(), _simple_plan())
    backend = FakeBackend()
    validator = ScriptedValidator([0.5, 0.9])  # second candidate clears the threshold
    R.render_job(
        job, tmp_path / "episode.wav", backend=backend,
        fast_preview=False, candidates=3, validator=validator,
    )
    # Stops at the 0.9 candidate (>= SIM_THRESHOLD), so only 2 generates, not 3.
    assert len(backend.calls) == 2


class RecordingValidator:
    """Records the reference text the gate scored against; always scores high."""

    def __init__(self):
        self.seen = []

    def score(self, wav, sr, text):
        self.seen.append(text)
        return 0.99


def test_gate_scores_against_derespelled_reference():
    """The engine SPEAKS the respelling but the STT gate must score against the source
    spelling (what Whisper writes for a correct take) — otherwise it prefers the
    spelled-out mispronunciation."""
    ir = EpisodeIR(
        episode=1, voice="", seed=7,
        segments=[Segment(
            id=0, spoken_text="he said Thoo-sid-ih-deez",
            chunks=["he said Thoo-sid-ih-deez"],
            score_chunks=["he said Thucydides"],
        )],
    )
    backend = FakeBackend()
    val = RecordingValidator()
    import tempfile
    from pathlib import Path
    d = Path(tempfile.mkdtemp())
    _write_job(d, ir, _simple_plan())
    # lexicon_fallback=False: exercise the respelling-first path (speak the respelling, score
    # against the de-respelled reference). The default path is covered separately below.
    R.render_job(d, d / "episode.wav", backend=backend,
                 fast_preview=False, candidates=1, validator=val, lexicon_fallback=False)
    assert backend.calls[0][0] == "he said Thoo-sid-ih-deez"  # engine speaks the respelling
    assert "he said Thucydides" in val.seen  # gate scores against the source spelling
    assert "Thoo-sid-ih-deez" not in " ".join(val.seen)  # never the respelling


def test_gate_falls_back_to_chunk_when_no_score_chunks():
    ir = EpisodeIR(
        episode=1, voice="", seed=7,
        segments=[Segment(id=0, spoken_text="plain words", chunks=["plain words"])],
    )
    backend = FakeBackend()
    val = RecordingValidator()
    import tempfile
    from pathlib import Path
    d = Path(tempfile.mkdtemp())
    _write_job(d, ir, _simple_plan())
    R.render_job(d, d / "episode.wav", backend=backend,
                 fast_preview=False, candidates=1, validator=val)
    assert val.seen == ["plain words"]  # no score_chunks -> score against the chunk itself


# --- lexicon fallback (unassisted-first, per-occurrence, binary) ---

def _respelled_ir():
    return EpisodeIR(
        episode=1, voice="", seed=7,
        segments=[Segment(
            id=0, spoken_text="he said Thoo-sid-ih-deez",
            chunks=["he said Thoo-sid-ih-deez"],
            score_chunks=["he said Thucydides"],
        )],
    )


def _render(tmp_path, ir, backend, validator, **kw):
    _write_job(tmp_path, ir, _simple_plan())
    return R.render_job(tmp_path, tmp_path / "episode.wav", backend=backend,
                        validator=validator, **kw)


def test_lexicon_fallback_off_speaks_respelling(tmp_path):
    """Opt-out (--no-lexicon-fallback): the engine speaks the respelling directly."""
    backend, val = FakeBackend(), RecordingValidator()
    _render(tmp_path, _respelled_ir(), backend, val,
            fast_preview=False, candidates=1, lexicon_fallback=False)
    assert [t for t, _ in backend.calls] == ["he said Thoo-sid-ih-deez"]


def test_lexicon_fallback_on_by_default(tmp_path):
    """Default (no flag) is unassisted-first: the raw name is spoken first and, when it clears
    the gate, the respelling is never generated."""
    backend = FakeBackend()
    val = ScriptedValidator([0.95])  # raw take clears SIM_THRESHOLD
    _render(tmp_path, _respelled_ir(), backend, val, fast_preview=False, candidates=1)
    assert [t for t, _ in backend.calls] == ["he said Thucydides"]  # raw only, no respelling


def test_lexicon_fallback_prefers_unassisted_when_it_clears_gate(tmp_path):
    """Flag on: speak the raw name first; if it clears the gate, the respelling is
    never generated. The gate scores against the (de-respelled) source spelling."""
    backend = FakeBackend()
    val = ScriptedValidator([0.95])  # the unassisted take clears SIM_THRESHOLD
    _render(tmp_path, _respelled_ir(), backend, val,
            fast_preview=False, candidates=1, lexicon_fallback=True)
    assert [t for t, _ in backend.calls] == ["he said Thucydides"]  # unassisted only
    assert not any("Thoo-sid-ih-deez" in t for t, _ in backend.calls)  # never respelled


def test_lexicon_fallback_rescues_with_respelling(tmp_path):
    """Flag on: when the unassisted take fails the gate, escalate to the respelling
    and keep the better take. Order: unassisted THEN respelled."""
    backend = FakeBackend()
    val = ScriptedValidator([0.5, 0.95])  # unassisted fails, respelling clears
    _render(tmp_path, _respelled_ir(), backend, val,
            fast_preview=False, candidates=1, lexicon_fallback=True)
    assert [t for t, _ in backend.calls] == [
        "he said Thucydides",        # 1) unassisted first
        "he said Thoo-sid-ih-deez",  # 2) respelled rescue
    ]


def test_lexicon_fallback_noop_without_score_chunks(tmp_path):
    """Flag on but the segment carries no respelling -> single spelling, unchanged."""
    ir = EpisodeIR(
        episode=1, voice="", seed=7,
        segments=[Segment(id=0, spoken_text="plain words", chunks=["plain words"])],
    )
    backend = FakeBackend()
    val = ScriptedValidator([0.5, 0.5])  # low, but there's nothing to fall back to
    _render(tmp_path, ir, backend, val,
            fast_preview=False, candidates=1, lexicon_fallback=True)
    assert [t for t, _ in backend.calls] == ["plain words"]


def test_lexicon_fallback_disabled_in_fast_preview(tmp_path):
    """Fallback is a final-mode feature; fast preview speaks the primary chunk once."""
    backend = FakeBackend()
    _render(tmp_path, _respelled_ir(), backend, None,
            fast_preview=True, lexicon_fallback=True)
    assert [t for t, _ in backend.calls] == ["he said Thoo-sid-ih-deez"]
