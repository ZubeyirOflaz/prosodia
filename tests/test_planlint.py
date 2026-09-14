"""The plan linter: the deterministic half of reviewing a Planner outline.

Each test names the real defect it stands for. All of them were found by hand, on the first
generated plan for projects/ai_act, by scripts that lived in a scratch directory — which is
the reason this module exists at all.
"""

import pytest

from prosodia.author.planlint import ERROR, WARN, lint_plan

OUTLINE = """# Outline

## The through-line

One organising question.

## The coverage map

| Part | Taught in |
|---|---|
| Arts. 1, 2, 3 | **Ep 1** |
| Arts. 8-21, 26, 27 | **Ep 2** |

## Episode 1 — The Gate

**Length:** 27 min

**Prerequisites:** none

**Opening instance** — *type: a decided case.* Something real, 1 January 2020.

**The operative text:** Art. 3 says "a machine-based system that is designed to operate".

**The variants:** change a fact.

**Transfer questions:** what would you ask?

**Sources:** the docket.

## Episode 2 — The Weight

**Length:** 40 min

**Prerequisites:** Eps 1, 3

**Opening instance** — *type: a decided case.* Another one, 2 February 2021.

> Art. 8 · Art. 9 · Art. 10 · Art. 11 · Art. 12 · Art. 13 · Art. 14 · Art. 15 · Art. 16 · Art. 17

**The variants:** Art. 14 again.

**Transfer questions:** more.

**Sources:** the docket.
"""

DOCKET = """
Articles 1 to 3 of the Regulation, and Arts. 8-21, 26 and 27.
Art. 3 defines it as "a machine-based system that is designed to operate".
The EUR 47 million figure is UNVERIFIED and must not be used.
"""


@pytest.fixture
def findings():
    return lint_plan(OUTLINE, docket=DOCKET, target_minutes=27)


def codes(fs, level=None):
    return {f.code for f in fs if level is None or f.level == level}


def test_bare_range_in_the_coverage_map_is_an_error(findings):
    """A range covers whatever is inside it, including provisions nobody read.

    The real plan assigned 77 of 110 articles only inside ranges, reported itself complete,
    and thereby "covered" six articles inserted by the governing amendment that its 854
    lines never named — one of which reversed what it taught about who may fine whom.
    """
    assert "bare-range" in codes(findings, ERROR)
    assert any("8-21" in f.message or "8–21" in f.message for f in findings)


def test_a_forward_prerequisite_is_an_error(findings):
    assert "forward-prereq" in codes(findings, ERROR)
    assert any("Episode 3" in f.message and f.episode == 2 for f in findings)


def test_a_citation_the_docket_never_supplied_is_an_error():
    fs = lint_plan(OUTLINE.replace("Art. 14 again.", "Art. 99 again."), docket=DOCKET)
    assert "cite-not-in-docket" in codes(fs, ERROR)
    assert any("Article 99" in f.message for f in fs)


def test_docket_ranges_are_expanded_before_a_citation_is_called_missing(findings):
    """The docket says "Arts. 8-21", so Article 14 IS supplied.

    The first version of this module compared against raw docket text and so committed the
    exact error it exists to catch in the plan.
    """
    assert not any("Article 14" in f.message for f in findings)
    assert not any("Article 26" in f.message for f in findings)


def test_a_quotation_must_be_verbatim_in_the_docket():
    bad = OUTLINE.replace(
        '"a machine-based system that is designed to operate"',
        '"a machine based system which is designed to operate"',
    )
    fs = lint_plan(bad, docket=DOCKET)
    assert "quote-not-verbatim" in codes(fs, ERROR)


def test_short_quotations_do_not_mispair_into_a_phantom_span():
    """`"([^"]+)"` matches from one quotation's CLOSING mark to the next one's OPENING mark.

    On the real plan that invented a 'quotation' out of ordinary prose between the word
    "infers" and the next quoted phrase, and reported it as not verbatim.
    """
    text = OUTLINE.replace(
        "**The variants:** change a fact.",
        'Nobody can read "infers" off the page and know where it stops, which is why the '
        'Commission published guidelines saying "the list is not exhaustive".',
    )
    fs = lint_plan(text, docket=DOCKET)
    assert not any("off the page" in f.message for f in fs)


def test_an_enumerated_paragraph_is_flagged_as_unsayable(findings):
    assert "unsayable" in codes(findings, WARN)
    assert any("names 10 provisions in sequence" in f.message for f in findings)


def test_runtime_flags_only_a_large_drift_from_the_series_anchor(findings):
    """The anchor is soft. The first version flagged any overshoot above 5%, which punished
    a planner for sizing a dense episode properly and saying so."""
    # 27 + 40 = 67 against 2 x 27 = 54 is 24% over: within tolerance, no finding
    assert "runtime" not in codes(findings, WARN)
    # a plan that has drifted far from its anchor is worth a look, either way
    long_plan = OUTLINE.replace("**Length:** 40 min", "**Length:** 80 min")
    fs = lint_plan(long_plan, docket=DOCKET, target_minutes=27)
    assert "runtime" in codes(fs, WARN)
    assert any("the series default is wrong for this material" in f.message for f in fs)


def test_a_repeated_opening_type_is_flagged(findings):
    assert "opening-repeat" in codes(findings, WARN)


def test_a_claim_the_docket_vetoes_is_flagged():
    fs = lint_plan(OUTLINE.replace("change a fact.", "the EUR 47 million fines."), docket=DOCKET)
    assert "docket-veto" in codes(fs, WARN)


def test_checks_needing_a_docket_are_skipped_not_failed():
    """The linter must run on a project with no research/ at all."""
    fs = lint_plan(OUTLINE, docket="", target_minutes=27)
    assert "no-docket" in codes(fs)
    assert "cite-not-in-docket" not in codes(fs)
    assert "bare-range" in codes(fs, ERROR)  # structural checks still run


def test_a_superseded_docket_file_is_citable_but_not_quotable():
    """Episode 1's writer quoted Art. 2(1)(c) out of a file headed SUPERSEDED.

    The editor caught it; this check had not, because it compared against the whole
    directory. A superseded file is still a legitimate place to learn that a provision
    exists — it is normally kept for the articles its replacement does not carry — but it is
    not a place to take words from.
    """
    from prosodia.author.planlint import lint_plan

    all_text = DOCKET + '\nArticle 7 says "the second making available of a thing".\n'
    quotable = DOCKET  # the Article 7 file is the superseded one
    plan = OUTLINE.replace(
        "**The variants:** change a fact.",
        'Art. 7 says "the second making available of a thing".',
    )
    # cited and quoted, with the words present only in the superseded file
    fs = lint_plan(plan, docket=all_text, quotable=quotable)
    assert "cite-not-in-docket" not in codes(fs, ERROR)      # citing it is fine
    assert "quote-not-verbatim" in codes(fs, ERROR)          # quoting it is not
    # and with the same file quotable, the quotation passes
    fs2 = lint_plan(plan, docket=all_text, quotable=all_text)
    assert "quote-not-verbatim" not in codes(fs2, ERROR)


def test_a_quoted_misreading_is_not_a_quotation_of_the_instrument():
    """The load-bearing-terms beat quotes the listener's WRONG reading beside the article
    that defines the term. That is the plan doing its job; flagging it made twelve of the
    twenty errors on the first re-plan noise."""
    plan = OUTLINE.replace(
        "**The variants:** change a fact.",
        '**Load-bearing terms.**\n- **intended purpose** (Art. 3) — wrong: "what it is used '
        'for". Right: the use the provider intends.',
    )
    fs = lint_plan(plan, docket=DOCKET)
    assert not any("what it is used for" in f.message for f in fs)
    # a genuine unverbatim quotation of the instrument is still caught
    plan2 = OUTLINE.replace(
        '"a machine-based system that is designed to operate"',
        '"a machine-based system which was designed to operate"')
    assert "quote-not-verbatim" in codes(lint_plan(plan2, docket=DOCKET), ERROR)
