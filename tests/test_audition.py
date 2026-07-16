"""Voice-audition pure helpers (clip discovery, the A/B page, param resolution)."""

import pytest

from prosodia.author.tone import VoiceProfiles
from prosodia.render.audition import (
    RANGE_SUITE,
    Passage,
    _index_html,
    _load_profiles,
    _resolve_params,
    _Section,
    discover_clips,
)


def test_discover_clips_dir_only_wavs_sorted(tmp_path):
    (tmp_path / "b.wav").write_bytes(b"x")
    (tmp_path / "a.wav").write_bytes(b"x")
    (tmp_path / "notes.txt").write_text("x", encoding="utf-8")
    got = discover_clips(tmp_path)
    assert [p.name for p in got] == ["a.wav", "b.wav"]  # only .wav, sorted


def test_discover_clips_list_dedupes(tmp_path):
    (tmp_path / "a.wav").write_bytes(b"x")
    (tmp_path / "b.wav").write_bytes(b"x")
    got = discover_clips([tmp_path / "a.wav", tmp_path])  # file + dir overlap
    assert [p.name for p in got] == ["a.wav", "b.wav"]  # a.wav not duplicated


def test_index_html_players_text_and_chip():
    s = _Section(
        label="Measured — baseline", tone="measured", rate="normal",
        params="exaggeration 0.50", text="Hello world.",
        players=[("narrator", "00_measured__00_narrator__seed1.wav")],
    )
    h = _index_html([s])
    assert "Hello world." in h
    assert h.count("<audio") == 1
    assert "00_measured__00_narrator__seed1.wav" in h
    assert "measured · normal" in h  # tone/rate chip rendered
    assert "exaggeration 0.50" in h  # resolved params shown


def test_index_html_escapes_and_shows_fallback_note():
    s = _Section(
        label="X", tone="made-up", rate="normal", params="p", text="<b>hi</b>",
        note="tone 'made-up' not in the tone table -> fell back to 'measured'",
        players=[],
    )
    h = _index_html([s])
    assert "<b>hi</b>" not in h and "&lt;b&gt;hi&lt;/b&gt;" in h  # escaped
    assert "fell back to" in h  # unknown-tone note surfaced


def test_range_suite_covers_wide_tonal_and_cadence_span():
    tones = {p.tone for p in RANGE_SUITE}
    rates = {p.rate for p in RANGE_SUITE}
    # a genuinely wide register spread, not one corner of the voice
    assert {"measured", "warm", "wry", "tense", "urgent", "dramatic", "grave"} <= tones
    # cadence range exercises slow AND fast, not just normal
    assert {"slow", "fast", "very-slow"} <= rates
    assert {p.key for p in RANGE_SUITE}.__len__() == len(RANGE_SUITE)  # unique keys


def test_resolve_params_uses_tone_table_pace_and_rate():
    profiles = VoiceProfiles(
        {
            "pace": 0.5,
            "default_tone": "measured",
            "tones": {
                "measured": {"exaggeration": 0.50, "cfg_weight": 0.40, "temperature": 0.78},
                "urgent": {"exaggeration": 0.74, "cfg_weight": 0.42, "temperature": 0.85},
            },
        }
    )
    p = Passage("urgent", "Urgent", "go", tone="urgent", rate="fast")
    exa, cfg, tmp, mult, ok = _resolve_params(
        profiles, p, exaggeration=None, cfg_weight=None, temperature=None
    )
    assert ok
    assert exa == pytest.approx(0.74)
    assert tmp == pytest.approx(0.85)
    assert cfg == pytest.approx(0.42 * 0.5)  # global pace dial applied
    assert mult == pytest.approx(1.10)       # "fast" rate multiplier


def test_resolve_params_clamps_cfg_low():
    profiles = VoiceProfiles(
        {"pace": 0.1, "default_tone": "measured",
         "tones": {"measured": {"exaggeration": 0.5, "cfg_weight": 0.4, "temperature": 0.8}}}
    )
    p = Passage("m", "M", "x", tone="measured", rate="normal")
    _, cfg, *_ = _resolve_params(profiles, p, exaggeration=None, cfg_weight=None, temperature=None)
    assert cfg == pytest.approx(0.15)  # clamped to the floor, not 0.04


def test_resolve_params_explicit_overrides_win_and_flag_unknown_tone():
    profiles = VoiceProfiles(
        {"default_tone": "measured",
         "tones": {"measured": {"exaggeration": 0.5, "cfg_weight": 0.4, "temperature": 0.8}}}
    )
    p = Passage("x", "X", "x", tone="does-not-exist", rate="normal")
    exa, cfg, tmp, mult, ok = _resolve_params(
        profiles, p, exaggeration=0.9, cfg_weight=0.3, temperature=0.6
    )
    assert not ok  # unknown tone fell back
    assert (exa, cfg, tmp) == pytest.approx((0.9, 0.3, 0.6))  # explicit overrides win


def test_load_profiles_explicit_object_passthrough():
    vp = VoiceProfiles({"tones": {"measured": {"exaggeration": 0.5}}})
    assert _load_profiles(vp, "ignored-when-object-given") is vp


def test_load_profiles_by_persona_name():
    # "thinkers" is not a file -> resolved as a persona name from the built-in library.
    vp = _load_profiles(None, "thinkers")
    assert "measured" in vp.known_tones() and len(vp.known_tones()) > 5


def test_load_profiles_by_file_path(tmp_path):
    f = tmp_path / "vp.yaml"
    f.write_text("pace: 0.7\ntones:\n  measured: {exaggeration: 0.5}\n", encoding="utf-8")
    vp = _load_profiles(None, str(f))
    assert vp.pace == pytest.approx(0.7)


def test_load_profiles_bad_name_raises_helpful():
    with pytest.raises(FileNotFoundError, match="not found"):
        _load_profiles(None, "no-such-persona-xyz")
