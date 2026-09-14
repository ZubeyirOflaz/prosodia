"""Comprehension checks on a finished transcript.

These exist because an LLM editor cannot count. The first episode made fifteen cross-episode
references in thirty-four minutes and four editorial rounds never reported the number.
"""

from prosodia.author.scriptlint import ERROR, WARN, lint_script, spoken_body

HEAD = "---\nepisode: 1\n---\n\n"


def codes(fs, level=None):
    return {f.code for f in fs if level is None or f.level == level}


def test_beat_titles_and_directives_never_reach_the_ear():
    body = spoken_body(HEAD + "## A title {tone: measured}\nSpoken words {pause: 1.0} here.\n")
    assert "A title" not in body and "tone" not in body and "pause" not in body
    assert "Spoken words" in body


def test_forward_references_are_counted_and_capped():
    t = HEAD + "## B\n" + ("Filler. " * 900) + (
        "We meet that in Episode 4. Episode 7 takes it up. Episode 9 has the timeline. "
        "Episode 12 lands the verdict. We will return to this."
    )
    fs = lint_script(t, episode=1)
    assert "forward-refs" in codes(fs, ERROR)
    assert any("5 forward references" in f.message for f in fs)


def test_a_reference_to_an_earlier_episode_is_not_a_debt():
    """Looking back costs the listener nothing — they have already heard it."""
    t = HEAD + "## B\n" + ("Filler. " * 900) + "As Episode 1 showed, the gate is narrow."
    fs = lint_script(t, episode=3)
    assert "forward-refs" not in codes(fs, ERROR)
    assert "back-refs" in codes(fs)


def test_the_opening_five_minutes_must_be_clear_of_pointers():
    t = HEAD + "## B\nEpisode 7 will explain. " + ("Filler. " * 900)
    assert "early-forward-ref" in codes(lint_script(t, episode=1), ERROR)


def test_an_enumerated_sentence_is_flagged():
    t = HEAD + "## B\nThe exclusions are national security, military use, pure research, " \
               "personal use, and open-source software."
    assert "enumeration" in codes(lint_script(t), WARN)


def test_missing_mid_episode_orientation_is_flagged():
    """Episode 1 had none at all, which is what made it hard to rejoin."""
    t = HEAD + "## B\n" + ("A sentence about the rule. " * 200)
    assert "no-recap" in codes(lint_script(t), WARN)
    t2 = t + " So far we have two things. Where we are now is the second gate."
    assert "no-recap" not in codes(lint_script(t2), WARN)


def test_a_spoken_bibliography_is_an_error():
    t = HEAD + "## B\n" + ("Filler. " * 400) + (
        "Sources. Collingridge 1980. Lessig 2006. Reidenberg 1998. Easterbrook 1996."
    )
    assert "spoken-sources" in codes(lint_script(t), ERROR)


def test_spatial_deixis_and_the_series_watchlist():
    t = HEAD + "## B\nAs you can see, the rule is however clear."
    fs = lint_script(t, banned=["however"])
    assert "spatial-deixis" in codes(fs, ERROR)
    assert "banned-phrase" in codes(fs, WARN)


def test_rhythm_is_reported_and_written_register_flagged():
    short = HEAD + "## B\n" + "The rule is narrow. It bites once. Nobody checked. " * 40
    assert any(f.code == "rhythm" and f.level == "note" for f in lint_script(short))
    long = HEAD + "## B\n" + (
        "The provision in question, which the Commission drafted in a period of considerable "
        "legislative uncertainty and against a background of competing institutional demands, "
        "applies to a class of systems that nobody had yet defined with any precision. " * 12
    )
    assert "rhythm" in codes(lint_script(long), WARN)
