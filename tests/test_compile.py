from prosodia.author.compile import compile_text, compile_with_plan, parse_directives
from prosodia.author.lexicon import Lexicon

SAMPLE = """---
voice: narrator
title: "T"
episode: 1
defaults: { tone: measured, rate: normal }
seed: 7
---

<!-- not spoken -->

## The ruin {tone: somber, rate: slow}
Picture the continent in 1945. {pause: 1.0}
It might happen *again*.

## Next {tone: tense}
They believed it.
"""


def test_compile_basic_segments_and_pauses():
    ir, warns = compile_text(SAMPLE, lexicon=Lexicon({"Monnet": "Moh-nay"}))
    assert ir.voice == "narrator" and ir.episode == 1 and ir.seed == 7
    assert len(ir.segments) == 3  # beat0 splits at the pause; beat1 has one

    s0, s1, s2 = ir.segments
    assert s0.intent.tone == "somber" and s0.intent.rate == "slow"
    assert "nineteen forty-five" in s0.spoken_text  # normalization applied
    assert s0.pause_before_ms == 0

    assert s1.pause_before_ms == 1000  # explicit {pause: 1.0}
    assert "again" in s1.emphasis  # *again*

    assert s2.intent.tone == "tense"
    assert s2.pause_before_ms >= 1  # beat-boundary pause

    joined = " ".join(s.authored_text for s in ir.segments)
    assert "<!--" not in joined and "not spoken" not in joined  # comment stripped


def test_chunks_present():
    ir, _ = compile_text(SAMPLE)
    assert all(seg.chunks for seg in ir.segments)


def test_parse_directives_quote_aware():  # repair D1
    d = parse_directives('note: "a, b: c", tone: wry')
    assert d["note"] == "a, b: c"
    assert d["tone"] == "wry"


def test_body_thematic_break_not_front_matter():  # repair D2
    ir, _ = compile_text("## A\nLine one.\n\n---\n\nLine two.")
    spoken = " ".join(s.authored_text for s in ir.segments)
    assert "Line one." in spoken and "Line two." in spoken
    assert "---" not in spoken


def test_beat_title_trailing_brace():  # repair D3
    ir, _ = compile_text("## A {literal} title {tone: wry}\nHello.")
    assert ir.segments[0].intent.tone == "wry"
    assert ir.segments[0].beat_title == "A {literal} title"


def test_voice_precedence():  # repair C1
    txt = "---\nvoice: fm_voice\n---\n## A\nHi."
    assert compile_text(txt, config={"voice": "cfg"}, voice_override="instr")[0].voice == "instr"
    assert compile_text(txt, config={"voice": "cfg"})[0].voice == "fm_voice"
    assert compile_text("## A\nHi.", config={"voice": "cfg"})[0].voice == "cfg"


def test_inline_tone_shift_creates_segment():
    ir, _ = compile_text("## A {tone: measured}\nCalm here. {tone: dramatic} Loud now.")
    tones = [s.intent.tone for s in ir.segments]
    assert tones == ["measured", "dramatic"]


def test_compile_with_plan_aligns():
    ir, plan, warns = compile_with_plan(SAMPLE)
    assert len(plan.params) == len(ir.segments)
    assert plan.voice == "narrator" and plan.seed == 7
    # somber segment -> lower cfg_weight than the 0.5 default
    assert plan.params[0].cfg_weight < 0.5


TWO_HOST = """---
speakers: { narrator: anna, guest: ben }
---

## Dialogue
@narrator
The question was colder than we'd ask today.

@guest
Colder how?

## Back to narration
And so it went.
"""


def test_speaker_tags_segment_and_strip():  # finding 17
    ir, warns = compile_text(TWO_HOST)
    # Two paragraphs in the dialogue beat -> two speakers.
    beat0 = [s for s in ir.segments if s.beat_index == 0]
    assert [s.speaker for s in beat0] == ["narrator", "guest"]
    # @tags never appear in spoken or authored text.
    for s in ir.segments:
        assert "@narrator" not in s.authored_text and "@guest" not in s.authored_text
        assert "@narrator" not in s.spoken_text and "@guest" not in s.spoken_text
    # A following beat resets the speaker to the first declared speaker.
    beat1 = [s for s in ir.segments if s.beat_index == 1]
    assert beat1 and beat1[0].speaker == "narrator"
    assert not warns  # all tags declared


def test_unknown_speaker_warns():  # findings 8, 30
    txt = "---\nspeakers: { narrator: anna }\n---\n## A\n@stranger\nHello."
    ir, warns = compile_text(txt)
    assert any("@stranger" in w and "not declared" in w for w in warns)


def test_default_speaker_from_speakers_map():  # finding 31
    txt = "---\nspeakers: { host: anna, guest: ben }\n---\n## A\nHi."
    ir, _ = compile_text(txt)
    assert ir.segments[0].speaker == "host"  # first declared, not hardcoded narrator
    # No speakers map -> default narrator.
    ir2, _ = compile_text("## A\nHi.")
    assert ir2.segments[0].speaker == "narrator"


def test_escapes():  # finding 18
    ir, _ = compile_text(r"## A" + "\n" + r"a \* b and *emph* c")
    s = ir.segments[0]
    assert "*" in s.spoken_text  # literal asterisk kept
    assert "emph" in s.spoken_text  # emphasis markers removed, word kept
    assert s.emphasis == ["emph"]  # only the real emphasis recorded
    ir2, _ = compile_text(r"## A" + "\n" + r"an escaped \{x\} here")
    assert "{x}" in ir2.segments[0].spoken_text  # not parsed as a directive


def test_double_asterisk_emphasis_leaves_no_literal_stars():
    # Writers reach for **strong**; the old single-* rule matched only the inner pair and
    # left literal '*' in spoken_text (and thus in the audio). Both ** and * must be stripped.
    ir, _ = compile_text("## A\nthe **greatest happiness** of the *greatest* number, ***virtù***")
    s = ir.segments[0]
    assert "*" not in s.spoken_text  # single, double, AND triple fences all stripped
    assert s.spoken_text == "the greatest happiness of the greatest number, virtù"
    assert s.emphasis == ["greatest happiness", "greatest", "virtù"]


def test_bad_pause_warns_and_ignored():  # finding 19
    ir, warns = compile_text("## A\nBefore. {pause: abc} After.")
    assert any("bad pause value" in w for w in warns)
    # The bad pause does not become a pause_before_ms on the next segment.
    assert ir.segments[1].pause_before_ms == 0


def test_unknown_directive_key_warns():  # finding 19
    ir, warns = compile_text("## A {color: blue}\nHi.")
    assert any("unknown directive key 'color'" in w for w in warns)


def test_pre_first_beat_implicit_segment():  # finding 20
    ir, _ = compile_text("Some intro text.\n\n## A\nBeat body.")
    assert ir.segments[0].beat_title is None
    assert "Some intro text." in ir.segments[0].authored_text


def test_h1_and_h3_excluded_from_spoken():  # finding 20
    ir, _ = compile_text("# Episode Title\n## A\nBody line.\n### a note\nstill body")
    spoken = " ".join(s.authored_text for s in ir.segments)
    assert "Episode Title" not in spoken and "a note" not in spoken
    assert "Body line." in spoken and "still body" in spoken


def test_front_matter_pauses_override():  # finding 20
    txt = (
        "---\npauses: { paragraph: 0.2, beat: 1.5 }\n---\n"
        "## A\nPara one.\n\nPara two.\n\n## B\nNext beat."
    )
    ir, _ = compile_text(txt)
    # second segment follows a paragraph break -> 200 ms
    para_seg = ir.segments[1]
    assert para_seg.pause_before_ms == 200
    # the first segment of beat B follows a beat boundary -> 1500 ms
    beat_b = [s for s in ir.segments if s.beat_index == 1][0]
    assert beat_b.pause_before_ms == 1500


def test_pause_max_merge():  # finding 21
    # A beat boundary (1500) and a small explicit pause at the next beat's start
    # -> the larger (beat) wins.
    txt = (
        "---\npauses: { paragraph: 0.4, beat: 1.5 }\n---\n"
        "## A\nFirst.\n\n## B\n{pause: 0.2} Second."
    )
    ir, _ = compile_text(txt)
    beat_b = [s for s in ir.segments if s.beat_index == 1][0]
    assert beat_b.pause_before_ms == 1500  # max(1500, 200)
    # A large explicit pause wins over the paragraph default.
    txt2 = "## A\nOne.\n\n{pause: 2.0} Two."
    ir2, _ = compile_text(txt2)
    assert ir2.segments[1].pause_before_ms == 2000


def test_compile_populates_score_chunks_only_when_respelled():
    src = """---
voice: narrator
title: "T"
episode: 1
---

## A
The historian Thucydides wrote it down.

## B
Nothing tricky here at all.
"""
    ir, _ = compile_text(src, lexicon=Lexicon({"Thucydides": "Thoo-sid-ih-deez"}))
    s_name, s_plain = ir.segments[0], ir.segments[1]
    # The segment WITH a respelling carries a parallel, de-respelled score reference...
    assert "Thoo-sid-ih-deez" in " ".join(s_name.chunks)
    assert s_name.score_chunks and len(s_name.score_chunks) == len(s_name.chunks)
    assert "Thucydides" in " ".join(s_name.score_chunks)
    assert "Thoo-sid-ih-deez" not in " ".join(s_name.score_chunks)
    # ...the plain segment carries none (no bloat), so the renderer scores against chunks.
    assert s_plain.score_chunks == []


def test_compile_no_lexicon_no_score_chunks():
    src = "---\nvoice: n\nepisode: 1\n---\n\n## A\nPlain text only.\n"
    ir, _ = compile_text(src, lexicon=Lexicon({}))
    assert all(s.score_chunks == [] for s in ir.segments)
