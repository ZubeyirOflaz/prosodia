from prosodia.author.repetition import (
    analyze,
    feedforward_context,
    opening,
    phrase_count,
    spoken_text,
    tokens,
)

EP_A = """---
episode: 1
title: A
---

## Beat one {tone: measured}

I want to tell you about a man. *Sit* with that for a moment. {pause: 1.0}
Here is the part that matters.
"""

EP_B = """---
episode: 2
title: B
---

## Beat one {tone: grave}

I want to describe a different scene entirely, far away and long ago.
Sit with that for a moment, truly.
"""


def test_spoken_text_strips_markup():
    s = spoken_text(EP_A)
    assert "beat one" not in s  # beat header dropped (not spoken)
    assert "tone" not in s  # delivery directive dropped
    assert "pause" not in s
    assert "i want to tell you about a man" in s


def test_opening_and_tokens():
    assert opening(EP_A, 4) == "i want to tell"
    assert tokens("Hello, world!") == ["hello", "world"]


def test_phrase_count():
    assert phrase_count(spoken_text(EP_A), "sit with that") == 1
    assert phrase_count(spoken_text(EP_A), "i want to") == 1


def test_analyze_detects_collision_and_stock():
    r = analyze({"ep1": EP_A, "ep2": EP_B})
    assert "i want to" in r["opening_collisions"]  # both open the same way
    assert set(r["opening_collisions"]["i want to"]) == {"ep1", "ep2"}
    assert r["stock"]["sit with that"]["total"] == 2
    assert "i want to" in r["stock"]


def test_feedforward_context_lists_openings_and_phrases():
    ff = feedforward_context({"ep1": EP_A})
    assert "Openings already used" in ff
    assert "i want to tell you about" in ff
    assert "sit with that" in ff
    assert feedforward_context({}) == ""  # no prior episodes -> empty note
