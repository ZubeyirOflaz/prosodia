"""The written source reference, which exists so the episodes need no spoken bibliography."""

import pytest

from prosodia.author.references import build_references

OUTLINE = """# Outline

## Episode 1 — The Gate

**Length:** 34 min

**Sources:** Regulation (EU) 2024/1689, Art. 3(1). Collingridge, *The Social Control of
Technology* (1980). Something, *An Unsourced Work* (2099).

body

## Names for the lexicon

- Nederlandse Politie
- CEN
- Frank Easterbrook
"""

TRANSCRIPT = """---
episode: 1
---

## A system runs {tone: measured}
The Nederlandse Politie switched it off. Article 3 is the gate, and Article 2 the reach.
A licence is not a recent thing, and Annexes are not annexes.
"""


@pytest.fixture
def proj(tmp_path):
    p = tmp_path / "proj"
    (p / "plan").mkdir(parents=True)
    (p / "episodes" / "ep01-the-gate").mkdir(parents=True)
    (p / "research").mkdir()
    (p / "series.yaml").write_text('series: "The Instrument"\n', encoding="utf-8")
    (p / "plan" / "outline.md").write_text(OUTLINE, encoding="utf-8")
    (p / "episodes" / "ep01-the-gate" / "transcript.md").write_text(TRANSCRIPT, encoding="utf-8")
    (p / "research" / "07_operative_text.md").write_text(
        "# Docket 07 — Operative text\n\nCollingridge, *The Social Control of Technology*.\n",
        encoding="utf-8")
    return p


def test_lists_the_provisions_each_episode_actually_cites(proj):
    md, _ = build_references(proj)
    assert "- Article 3" in md and "- Article 2" in md
    # in first-mention order, which is the order a listener met them
    assert md.index("- Article 3") < md.index("- Article 2")
    assert "**Article 3** — episode 1" in md


def test_names_are_matched_on_word_boundaries(proj):
    """A substring test put CEN inside "licence" and "recent", and Annex inside "Annexes",
    so the first run credited the episode with institutions it never mentions."""
    md, _ = build_references(proj)
    assert "Nederlandse Politie" in md
    assert "CEN" not in md.split("## Where each provision")[0].split("named aloud")[1]
    assert "Frank Easterbrook" not in md  # in the lexicon, never spoken


def test_reports_a_plan_source_the_docket_cannot_support(proj):
    md, warnings = build_references(proj)
    assert any("An Unsourced Work" in w for w in warnings)
    assert not any("Social Control of Technology" in w for w in warnings)
    # the beat itself is still reproduced, gaps and all
    assert "Collingridge" in md


def test_an_unwritten_episode_is_named_not_skipped(proj):
    (proj / "plan" / "outline.md").write_text(
        OUTLINE.replace("## Names for the lexicon",
                        "## Episode 2 — The Ladder\n\n**Length:** 27 min\n\nbody\n\n"
                        "## Names for the lexicon"), encoding="utf-8")
    md, warnings = build_references(proj)
    assert "## Episode 2 — The Ladder" in md
    assert "*Not yet written.*" in md
    assert any("episode 2: no transcript" in w for w in warnings)


def test_missing_plan_is_an_error_not_a_crash(tmp_path):
    md, warnings = build_references(tmp_path)
    assert md == "" and warnings
