"""Pauses inside one generation, and room tone (2026-10-09).

Synthetic "speech": a tone burst per word, a short dip between words, and the longer gap an
engine leaves at punctuation, over a noise floor — the shape measured on real Chatterbox
narration (punctuation gaps 200–750 ms, gaps inside a sentence under ~150 ms).
"""

import pytest

np = pytest.importorskip("numpy")
sf = pytest.importorskip("soundfile")

from prosodia.render import audio as A
from prosodia.render.splice import find_gaps, splice_pauses

SR = 16000


def speech(text, *, noise=0.003, comma=0.20, stop=0.40, word_gap=0.02, seed=0, after=None):
    """``after`` overrides the gap after given words: {word number: seconds}."""
    rng = np.random.default_rng(seed)
    parts = []
    for k, tok in enumerate(text.split(), start=1):
        n = int(SR * 0.055 * max(2, sum(c.isalnum() for c in tok)))
        t = np.arange(n) / SR
        env = np.minimum(1.0, np.minimum(t, t[::-1]) / 0.01)
        parts.append(0.3 * np.sin(2 * np.pi * 180 * t) * env)
        gap = stop if tok[-1] in ".!?" else comma if tok[-1] in ",;:—" else word_gap
        gap = (after or {}).get(k, gap)
        parts.append(np.zeros(int(SR * gap)))
    x = np.concatenate(parts[:-1])
    return (x + noise * rng.standard_normal(x.size)).astype(np.float32)


TEXT = "The first is the controller, the body that decides. Then the processor, which acts."


def _longest_gap(wav):
    gaps, _, _ = find_gaps(wav, SR)
    return max(gaps, key=lambda g: g.ms)


def test_the_gaps_found_are_the_punctuation_gaps():
    gaps, _, _ = find_gaps(speech(TEXT), SR)
    assert [round(g.ms, -1) for g in gaps] == pytest.approx([200, 400, 200], abs=30)


def test_a_pause_is_lengthened_at_its_own_comma():
    wav = speech(TEXT)
    out, rep = splice_pauses(wav, SR, TEXT, [(12, 900)], A.RoomTone.estimate([wav], SR))
    assert (rep.spliced, rep.missed) == (1, 0)
    assert (out.size - wav.size) / SR == pytest.approx(0.700, abs=0.03)
    before = find_gaps(wav, SR)[0]
    longest = _longest_gap(out)
    assert longest.ms == pytest.approx(900, abs=40)
    assert longest.start == pytest.approx(before[2].start, abs=0.05)  # "processor," not "controller,"


def test_among_close_commas_the_right_one_is_chosen():
    text = "One, two, three, four, five, six."
    wav = speech(text)
    out, rep = splice_pauses(wav, SR, text, [(3, 1200)], A.RoomTone.estimate([wav], SR))
    before = find_gaps(wav, SR)[0]
    assert rep.spliced == 1
    assert _longest_gap(out).start == pytest.approx(before[2].start, abs=0.05)


def test_a_pause_with_no_gap_to_grow_is_left_alone_and_reported():
    wav = speech(TEXT, comma=0.02, stop=0.02)  # the engine ran straight through
    out, rep = splice_pauses(wav, SR, TEXT, [(12, 900)], A.RoomTone.estimate([wav], SR))
    assert (rep.spliced, rep.missed) == (0, 1)
    assert out.size == wav.size


def test_a_comma_the_engine_ran_through_is_not_moved_to_a_later_breath():
    """Series C Ep 1, "in force, {pause: 0.4} is settled": Chatterbox voiced no break at the
    comma, and the first matcher gave the pause to a breath after "content", 3.5 s later."""
    text = ("The directive is invalid, from its first day in force, is settled. "
            "That records without content sit below the core of private life is settled as law.")
    wav = speech(text, after={11: 0.02, 16: 0.25})   # no gap after "force,"; a breath after "content"
    out, rep = splice_pauses(wav, SR, text, [(11, 400)], A.RoomTone.estimate([wav], SR))
    assert (rep.spliced, rep.missed) == (0, 1)
    assert out.size == wav.size


def test_a_gap_already_long_enough_is_not_touched():
    wav = speech(TEXT)
    out, rep = splice_pauses(wav, SR, TEXT, [(5, 150)], A.RoomTone.estimate([wav], SR))
    assert rep.spliced == 1 and out.size == wav.size


def test_room_tone_matches_the_background_level_and_colour():
    rng = np.random.default_rng(3)
    low = np.convolve(rng.standard_normal(SR * 8), np.ones(16) / 16, mode="same") * 0.01
    wav = speech(TEXT, noise=0.0)
    wav = wav + low[: wav.size].astype(np.float32)
    room = A.RoomTone.estimate([wav], SR)
    tone = room(SR)
    floor = float(np.sqrt(np.mean(low ** 2)))
    assert float(np.sqrt(np.mean(tone ** 2))) == pytest.approx(floor, rel=0.35)
    spec = np.abs(np.fft.rfft(tone)) ** 2
    assert spec[: spec.size // 8].sum() > 0.8 * spec.sum()   # low-passed, like the background


def test_with_no_background_room_tone_is_silence():
    wav = speech(TEXT, noise=0.0)
    assert not np.any(A.RoomTone.estimate([wav], SR)(1000))


# ---- through the renderer ----------------------------------------------------------------------

from prosodia.core.ir import EpisodeIR, InnerPause, RenderPlan, Segment, SegmentParams
from prosodia.render import render as R


class SpeechBackend:
    sample_rate = SR

    def load(self):
        pass

    def generate(self, text, **kw):
        return speech(text)


def _render(tmp_path, chunks, chunk_pauses):
    tmp_path.mkdir(parents=True, exist_ok=True)
    ir = EpisodeIR(segments=[Segment(id=0, spoken_text=" ".join(chunks), chunks=chunks,
                                     chunk_pauses=chunk_pauses)])
    plan = RenderPlan(params=[SegmentParams(segment_id=0, exaggeration=0.5, cfg_weight=0.5,
                                            temperature=0.8)])
    (tmp_path / "ir.json").write_text(ir.to_json(), encoding="utf-8")
    (tmp_path / "render_plan.json").write_text(plan.to_json(), encoding="utf-8")
    out = R.render_job(tmp_path, tmp_path / "episode.wav", backend=SpeechBackend(),
                       fast_preview=True, speak_title=False)
    wav, sr = sf.read(out, dtype="float32")
    return wav, sr


def test_the_renderer_splices_an_inner_pause_and_never_writes_digital_silence(tmp_path):
    plain, sr = _render(tmp_path / "a", [TEXT], [])
    paused, _ = _render(tmp_path / "b", [TEXT], [[InnerPause(after_word=12, ms=1000)]])
    assert (paused.size - plain.size) / sr == pytest.approx(0.800, abs=0.05)
    # lead-in, tail and every pause are room tone: the background never drops to zero
    assert A.frame_db(paused, sr).min() > -100


def test_a_pause_after_the_last_word_of_a_chunk_goes_between_chunks(tmp_path):
    a, b = "The first is the controller.", "Then the processor acts."
    joined, sr = _render(tmp_path / "a", [a, b], [])
    gapped, _ = _render(tmp_path / "b", [a, b], [[InnerPause(after_word=5, ms=1500)], []])
    assert (gapped.size - joined.size) / sr == pytest.approx(1.5 + 0.02, abs=0.05)
