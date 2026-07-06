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
    m2 = re.search(r"(?i)\bepisode\s+0*(\d+)\b", text)  # "Episode 3", "EPISODE 3:"
    if m2:
        return int(m2.group(1))
    m3 = re.match(r"^0*(\d+)\s*[—:.\-]", text)  # "3 — Title", "3. Title", "3: Title"
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
