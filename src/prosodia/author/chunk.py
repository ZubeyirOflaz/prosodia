"""Sentence-aware chunking under the engine's per-generation cap.

Chatterbox degrades / hallucinates past a few hundred characters per call, so
spoken text is split at sentence boundaries and packed up to a target size.
Cascade for an over-long single sentence: split at ``; : , -`` then a hard
character cut (on a word boundary) as a last resort, so we never feed an
unbounded string to the engine.
"""

from __future__ import annotations

import re

DEFAULT_MAX_CHARS = 300

_SENT_END = re.compile(r"(?<=[.!?])\s+")
_SOFT_SPLIT = re.compile(r"(?<=[;:,])\s+|\s+-+\s+")


def split_sentences(text: str) -> list[str]:
    text = " ".join(text.split())
    if not text:
        return []
    return [s.strip() for s in _SENT_END.split(text) if s.strip()]


def _soft_split(s: str) -> list[str]:
    parts = [p.strip() for p in _SOFT_SPLIT.split(s) if p.strip()]
    return parts or [s]


def _hard_split(s: str, max_chars: int) -> list[str]:
    out: list[str] = []
    for piece in _soft_split(s):
        while len(piece) > max_chars:
            cut = piece.rfind(" ", 0, max_chars)
            if cut <= 0:
                cut = max_chars
            out.append(piece[:cut].strip())
            piece = piece[cut:].strip()
        if piece:
            out.append(piece)
    return out


def chunk_text(text: str, max_chars: int = DEFAULT_MAX_CHARS) -> list[str]:
    """Pack sentences into chunks <= max_chars; split over-long sentences."""
    chunks: list[str] = []
    cur = ""
    for sent in split_sentences(text):
        pieces = [sent] if len(sent) <= max_chars else _hard_split(sent, max_chars)
        for piece in pieces:
            if not cur:
                cur = piece
            elif len(cur) + 1 + len(piece) <= max_chars:
                cur = f"{cur} {piece}"
            else:
                chunks.append(cur)
                cur = piece
    if cur:
        chunks.append(cur)
    return chunks
