"""Regressions for the project-wide bug-hunt fixes (non-UI components)."""

from __future__ import annotations

import pytest

from prosodia.author.compile import compile_text
from prosodia.author.tone import VoiceProfiles, build_render_plan
from prosodia.core.intents import rate_to_multiplier

_PROFILES = VoiceProfiles(
    {"default_tone": "measured",
     "tones": {"measured": {"exaggeration": 0.4, "cfg_weight": 0.5, "temperature": 0.75}}}
)


def test_unknown_rate_warns_not_crash():
    ir, _ = compile_text("## Intro {tone: measured, rate: quick}\nHello there.\n", profiles=_PROFILES)
    plan, warns = build_render_plan(ir, _PROFILES)  # must not raise
    assert any("unknown rate" in w for w in warns)
    assert plan.params[0].rate_multiplier == 1.0


def test_numeric_rate_default_compiles():
    ir, _ = compile_text(
        "---\ndefaults: {rate: 0.9}\n---\n## B {tone: measured}\nHi there.\n", profiles=_PROFILES
    )
    assert ir.segments[0].intent.rate == "0.9"
    assert rate_to_multiplier(ir.segments[0].intent.rate) == pytest.approx(0.9)


def test_malformed_front_matter_raises_clean_valueerror():
    with pytest.raises(ValueError):
        compile_text("---\nfoo: [unclosed\n---\n## B {tone: measured}\nHi.\n", profiles=_PROFILES)


def test_voiceprofiles_none_is_safe():
    vp = VoiceProfiles(None)  # empty / comment-only voice_profiles.yaml parses to None
    assert vp.engine == "chatterbox" and vp.default_tone == "measured"


def test_mentions_word_initial_prefix():
    from prosodia.core.diagnosis import _mentions

    assert _mentions("the pacing really drags", "rate")             # base cue words
    assert _mentions("it keeps dragging", "rate")                   # inflected (regression guard)
    assert _mentions("the opening is too slowly paced", "rate")     # 'slowly' from 'slow'
    assert not _mentions("we talked over breakfast", "rate")        # 'fast' mid-word — no
    assert not _mentions("give it more space", "rate")              # 'pace' mid-word — no


def test_planparse_ignores_decimal_subheadings():
    from prosodia.author.planparse import _heading_episode

    assert _heading_episode("## 3. The Deal") == 3
    assert _heading_episode("## 10 — Title") == 10
    assert _heading_episode("## Episode 4: X") == 4
    assert _heading_episode("## 3.5 A sub-point") is None           # decimal, not an episode


def test_non_dict_defaults_compiles():
    ir, _ = compile_text("---\ndefaults: oops\n---\n## B {tone: measured}\nHi there.\n", profiles=_PROFILES)
    assert ir.segments  # a non-dict `defaults` is coerced to {}, not a crash


def test_run_counter_accounts_for_skipped_corrupt_line(tmp_path):
    from prosodia.core.trace import Run

    run = Run(tmp_path / "run")
    run.event("a", "x")  # one valid event (line 1)
    with (tmp_path / "run" / "events.jsonl").open("a", encoding="utf-8") as f:
        f.write("{corrupt line\n")  # line 2 (unparseable)
    reloaded = Run(tmp_path / "run")
    assert reloaded._counter == 2  # counts the skipped line too, so a new event won't reuse an id


def test_run_tolerates_partial_jsonl_line(tmp_path):
    from prosodia.core.trace import Run

    run = Run(tmp_path / "run")
    run.event("write", "writer", round=1)
    with (tmp_path / "run" / "events.jsonl").open("a", encoding="utf-8") as f:
        f.write('{"id": "e02", "stage": ')  # a truncated trailing line (crash mid-write)
    reloaded = Run(tmp_path / "run")  # must not raise
    assert len(reloaded.events()) == 1


# ── render side (needs the audio extra; skipped otherwise) ────────────────────

def test_render_chunk_all_fail_raises():
    pytest.importorskip("numpy")
    pytest.importorskip("soundfile")
    from prosodia.render.render import _render_chunk

    class BadBackend:
        def generate(self, *a, **k):
            raise RuntimeError("boom")

    with pytest.raises(RuntimeError):  # must NOT silently return empty audio
        _render_chunk(
            BadBackend(), "hi", (0.4, 0.5, 0.75, 1.0), 0, 0, 0, None,
            fast_preview=True, candidates=1, validator=None, sr=24000,
        )


def test_resolve_voice_ref_excludes_render_output(tmp_path):
    pytest.importorskip("numpy")
    pytest.importorskip("soundfile")
    from prosodia.render.render import _resolve_voice_ref

    (tmp_path / "episode.raw.wav").write_bytes(b"x")  # a prior render output
    (tmp_path / "narrator.wav").write_bytes(b"x")     # the real bundled clip

    class _IR:
        voice = "narrator"

    ref = _resolve_voice_ref(
        _IR(), tmp_path, None, exclude=frozenset({"episode.wav", "episode.raw.wav"})
    )
    assert ref is not None and ref.endswith("narrator.wav")


def test_render_job_edge_silence_and_spoken_title(tmp_path):
    np = pytest.importorskip("numpy")
    sf = pytest.importorskip("soundfile")
    from prosodia.core.ir import EpisodeIR, RenderPlan, Segment, SegmentParams
    from prosodia.render.render import render_job

    class FakeBackend:
        sample_rate = 24000

        def __init__(self):
            self.texts = []

        def load(self):
            pass

        def generate(self, text, **kw):
            self.texts.append(text)
            return np.full(self.sample_rate // 2, 0.1, dtype=np.float32)  # 0.5s of signal

    job = tmp_path / "job"
    job.mkdir()
    ir = EpisodeIR(episode=1, title="Test Title", voice="", seed=0,
                   segments=[Segment(id=0, chunks=["hello world"], spoken_text="hello world")])
    plan = RenderPlan(params=[SegmentParams(segment_id=0, exaggeration=0.4, cfg_weight=0.5,
                                            temperature=0.75, rate_multiplier=1.0)])
    (job / "ir.json").write_text(ir.to_json(), encoding="utf-8")
    (job / "render_plan.json").write_text(plan.to_json(), encoding="utf-8")

    fake = FakeBackend()
    out = render_job(job, job / "episode.wav", backend=fake, fast_preview=True)
    data, sr = sf.read(str(out))
    assert len(data) / sr >= 8.0            # two 4s edges bookend the episode
    assert "Test Title" in fake.texts       # title spoken at the start
    assert "hello world" in fake.texts

    fake2 = FakeBackend()
    render_job(job, job / "ep2.wav", backend=fake2, fast_preview=True, speak_title=False)
    assert "Test Title" not in fake2.texts  # --no-title path
