"""Extract a single episode's section from a Planner outline (Markdown).

Lets the writer receive only the relevant episode's plan — including the
Planner-sourced anecdotes, human anchor, and contested points — so it selects and
places them rather than inventing. Heading-format tolerant; returns None when the
episode's section can't be located (the caller then falls back to the coarse brief).
"""

from __future__ import annotations

import re


def _heading_level(line: str) -> int | None:
    m = re.match(r"^(#{1,6})\s+\S", line)
    return len(m.group(1)) if m else None


def _heading_episode(line: str) -> int | None:
    """If ``line`` is a Markdown heading that names an episode, return its number."""
    m = re.match(r"^#{1,6}\s+(.*)$", line)
    if not m:
        return None
    text = m.group(1).strip()
    m2 = re.search(r"(?i)\b(?:episode|ep)\s+0*(\d+)\b", text)  # "Episode 3", "EP 3", "EPISODE 3:"
    if m2:
        return int(m2.group(1))
    m3 = re.match(r"^0*(\d+)\s*(?:[—:-]|\.(?!\d))", text)  # "3 — Title/3. Title/3: Title"; not "3.5"
    if m3:
        return int(m3.group(1))
    return None


def extract_episode_section(outline_md: str, episode: int) -> str | None:
    """Return the Markdown block for ``episode`` (heading through the next
    same-or-higher heading), or None if not found."""
    lines = outline_md.replace("\r\n", "\n").split("\n")
    start = start_level = None
    for i, line in enumerate(lines):
        if _heading_episode(line) == episode:
            start, start_level = i, _heading_level(line)
            break
    if start is None:
        return None
    end = len(lines)
    for j in range(start + 1, len(lines)):
        lvl = _heading_level(lines[j])
        if lvl is not None and lvl <= start_level:
            end = j
            break
    return "\n".join(lines[start:end]).strip() or None


_TITLE_SEP = re.compile(r"^\s*(?:episode|ep)\s*0*\d+\s*[—:.–-]\s*", re.IGNORECASE)
_LENGTH = re.compile(r"(?im)^[^\n]*?\*\*Length:?\*\*[^\n\d]{0,20}(\d{1,3})\s*(?:min|minutes)?")


def episode_title(heading: str) -> str:
    """'## Episode 3 — What counts as a system' -> 'What counts as a system'."""
    text = re.sub(r"^#{1,6}\s+", "", heading).strip()
    return _TITLE_SEP.sub("", text).strip(" —-:·").strip()


_TYPE_TAG = re.compile(r"^\[([A-Za-z]+)\]\s*")


def split_type(title: str) -> tuple[str, str]:
    """'[LENS] The Pacing Problem' -> ('lens', 'The Pacing Problem').

    The planner marks lens and verdict episodes in the heading. Downstream roles need
    that mark — a lens episode has no opening instance and no single-fact flip, so an
    editor judging it against the apparatus spine fails it for what it is.
    """
    m = _TYPE_TAG.match(title)
    if not m:
        return "apparatus", title
    return m.group(1).lower(), title[m.end():].strip()


def slugify(n: int, title: str) -> str:
    base = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    return f"ep{n:02d}" + (f"-{base}" if base else "")


def planned_length(section: str) -> int | None:
    """The episode's own planned length in minutes, if the section states one."""
    m = _LENGTH.search(section)
    return int(m.group(1)) if m else None


def parse_episode_index(outline_md: str) -> list[dict]:
    """Every episode the outline defines, as ``series.yaml``-shaped entries.

    The planner's episodes live only in ``plan/outline.md``; ``write`` looks them up in
    ``series.yaml``. Without a bridge the two never meet: a freshly planned series has no
    episodes at all, and a hand-transcribed list silently drops the per-episode lengths the
    planner chose (which is how a 38-minute verdict episode gets written to a 27-minute
    series default).
    """
    lines = outline_md.replace("\r\n", "\n").split("\n")
    out: list[dict] = []
    for i, line in enumerate(lines):
        n = _heading_episode(line)
        if n is None or any(e["n"] == n for e in out):
            continue
        section = extract_episode_section(outline_md, n) or ""
        etype, title = split_type(episode_title(line))
        entry = {"n": n, "slug": slugify(n, title), "title": title, "type": etype}
        mins = planned_length(section)
        if mins:
            entry["target_minutes"] = mins
        out.append(entry)
    return sorted(out, key=lambda e: e["n"])


_LEXICON_HEADING = re.compile(r"(?i)^#{1,6}\s+names for the lexicon\b")


def extract_series_sections(outline_md: str) -> str | None:
    """Everything in the outline that is NOT one episode's section.

    ``extract_episode_section`` hands the writer only its own ``## Episode N`` block, so
    every series-level decision the Planner made was dropped on the way: the through-line
    the writer must place the episode against, the list of explainer tics banned across the
    series, the material reserved for a later series that must be named aloud rather than
    covered, and which episode lands the held verdict. The writer was then asked to honour
    all four and given none of them.

    The lexicon name-list is left out: it is a different agent's input, and it is long.
    """
    lines = outline_md.replace("\r\n", "\n").split("\n")
    keep: list[str] = []
    skipping = False
    skip_level = 0
    for line in lines:
        lvl = _heading_level(line)
        if lvl is not None:
            if skipping and lvl <= skip_level:
                skipping = False
            if not skipping and (_heading_episode(line) is not None or _LEXICON_HEADING.match(line)):
                skipping, skip_level = True, lvl
        if not skipping:
            keep.append(line)
    return "\n".join(keep).strip() or None
