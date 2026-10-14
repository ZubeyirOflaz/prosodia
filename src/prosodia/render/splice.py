"""Authored pauses inside one generation.

The compiler keeps the words on both sides of a ``{pause}`` or paragraph break in one chunk, so
the engine voices the sentence as unfinished (IR ``chunk_pauses``). Chatterbox has no pause
token, so the pause is made afterwards: the engine leaves a short gap at punctuation, and this
module finds that gap and lengthens it to the authored duration with room tone.

Finding the right gap: punctuation in the text and gaps in the audio come in the same order.
A monotonic alignment pairs punctuation boundaries with gaps (a gap can go unmatched — a stop
consonant, a breath; so can a boundary — a comma said without a break); long gaps are preferred,
since on real Chatterbox narration punctuation left 200–750 ms and gaps inside a sentence stayed
under ~150 ms. The matched boundaries then anchor the timeline, and each pause is looked for
only within ``_NEAR_S`` of the time interpolated between its neighbouring anchors. A pause the
engine ran straight through is left at the engine's own timing and reported — never moved to
another gap, and never cut into a word. (The first version used one whole-chunk estimate and,
on real narration, handed a comma the engine never voiced to a breath 3.5 s later.)

Pure numpy, testable without the engine.
"""

from __future__ import annotations

import re
from collections.abc import Callable
from dataclasses import dataclass

import numpy as np

from prosodia.render import audio as A

MIN_GAP_MS = 60     # shorter dips are inside words
MAJOR_GAP_MS = 150  # punctuation-sized
_NEAR_S = 0.35      # how far from its expected time a pause's gap may be
_PUNCT_END = re.compile(r"[,;:.!?…—–-][\"'”’)\]]*$")
_SENTENCE_END = re.compile(r"[.!?…][\"'”’)\]]*$")


@dataclass
class Gap:
    start: float  # seconds
    end: float

    @property
    def center(self) -> float:
        return (self.start + self.end) / 2

    @property
    def ms(self) -> float:
        return (self.end - self.start) * 1000


def find_gaps(wav: np.ndarray, sr: int) -> tuple[list[Gap], float, float]:
    """Low-energy stretches inside the speech, plus where the speech starts and ends."""
    db = A.frame_db(wav, sr)
    if db.size == 0:
        return [], 0.0, len(wav) / sr
    hop = A.FRAME_HOP_MS / 1000
    floor = float(np.percentile(db, 10))
    thr = min(floor + 8.0, float(np.percentile(db, 95)) - 20.0)
    loud = np.flatnonzero(db >= thr)
    if loud.size == 0:
        return [], 0.0, len(wav) / sr
    first, last = int(loud[0]), int(loud[-1])
    gaps: list[Gap] = []
    i = first
    while i <= last:
        if db[i] < thr:
            j = i
            while j <= last and db[j] < thr:
                j += 1
            if (j - i) * A.FRAME_HOP_MS >= MIN_GAP_MS:
                gaps.append(Gap(i * hop + hop / 2, j * hop + hop / 2))
            i = j
        else:
            i += 1
    return gaps, first * hop, (last + 1) * hop


def _units(text: str) -> tuple[list[float], list[float]]:
    """Per token: its share of speaking time (letters + 1), and the pause allowance after it."""
    units, marks = [], []
    for tok in text.split():
        units.append(sum(ch.isalnum() for ch in tok) + 1.0)
        marks.append(6.0 if _SENTENCE_END.search(tok) else 3.0 if _PUNCT_END.search(tok) else 0.0)
    return units, marks


def boundary_times(text: str, start: float, end: float) -> list[tuple[int, float, bool]]:
    """``(after_word, expected_time, is_punctuation)`` for each token boundary that may pause.

    Time is shared out by letters, with an allowance for the pause itself at punctuation.
    """
    units, marks = _units(text)
    total = sum(units) + sum(marks) or 1.0
    out, acc = [], 0.0
    for k, (u, m) in enumerate(zip(units, marks), start=1):
        acc += u
        if m and k < len(units):
            out.append((k, start + (end - start) * (acc + m / 2) / total, True))
        acc += m
    return out


def _position(text: str, after: int) -> float:
    """Where the boundary after word ``after`` falls, in the same units as ``boundary_times``."""
    units, marks = _units(text)
    return sum(units[:after]) + sum(marks[: after - 1]) + marks[after - 1] / 2 if after else 0.0


def align(bounds: list[tuple[int, float, bool]], gaps: list[Gap], span: float,
          must: frozenset[int] = frozenset()) -> dict[int, int]:
    """Monotonic pairing of boundaries with gaps; returns ``{after_word: gap index}``.

    ``must`` holds the boundaries carrying an authored pause, which are costlier to leave
    unmatched (the compiler gave each one punctuation, so the engine should have paused).
    """
    m, n = len(bounds), len(gaps)
    span = max(span, 1e-3)
    inf = float("inf")
    cost = np.full((m + 1, n + 1), inf)
    move = np.zeros((m + 1, n + 1), dtype=np.int8)  # 1 match, 2 skip boundary, 3 skip gap
    cost[0, 0] = 0.0

    def skip_b(i: int) -> float:
        return 0.30 if bounds[i][0] in must else 0.10

    def skip_g(j: int) -> float:
        return 0.12 if gaps[j].ms >= MAJOR_GAP_MS else 0.01

    for i in range(m + 1):
        for j in range(n + 1):
            c = cost[i, j]
            if c == inf:
                continue
            if i < m and j < n:
                mc = c + abs(bounds[i][1] - gaps[j].center) / span \
                    + (0.0 if gaps[j].ms >= MAJOR_GAP_MS else 0.05)
                if mc < cost[i + 1, j + 1]:
                    cost[i + 1, j + 1], move[i + 1, j + 1] = mc, 1
            if i < m and c + skip_b(i) < cost[i + 1, j]:
                cost[i + 1, j], move[i + 1, j] = c + skip_b(i), 2
            if j < n and c + skip_g(j) < cost[i, j + 1]:
                cost[i, j + 1], move[i, j + 1] = c + skip_g(j), 3
    pairs: dict[int, int] = {}
    i, j = m, n
    while i or j:
        mv = move[i, j]
        if mv == 1:
            pairs[bounds[i - 1][0]] = j - 1
            i, j = i - 1, j - 1
        elif mv == 2:
            i -= 1
        else:
            j -= 1
    return pairs


@dataclass
class SpliceReport:
    spliced: int = 0
    missed: int = 0
    notes: list[str] | None = None


def splice_pauses(
    wav: np.ndarray, sr: int, text: str, pauses: list[tuple[int, int]],
    fill: Callable[[int], np.ndarray], *, xfade_ms: int = 10,
) -> tuple[np.ndarray, SpliceReport]:
    """Lengthen the engine's gap at each ``(after_word, ms)`` pause to ``ms``, with ``fill``.

    A gap already as long as the authored pause is left alone. A pause with no matching gap
    is left at whatever the engine did and reported — inserting silence at a guessed time
    would cut into a word.
    """
    report = SpliceReport(notes=[])
    if not pauses:
        return wav, report
    gaps, start, end = find_gaps(wav, sr)
    bounds = boundary_times(text, start, end)
    pairs = align(bounds, gaps, end - start)
    # Anchors: where matched punctuation actually fell. A pause's expected time is interpolated
    # between its neighbouring anchors — a whole-chunk estimate drifts by seconds, and on real
    # narration it handed a pause the engine never voiced to a breath three seconds later.
    anchors = sorted((_position(text, a), gaps[j].center, a) for a, j in pairs.items())
    xf = int(sr * xfade_ms / 1000)
    inserts: list[tuple[int, int]] = []
    for after, ms in pauses:
        pts = [(0.0, start)] + [(u, t) for u, t, a in anchors if a != after] \
            + [(_position(text, len(text.split())), end)]
        expect = float(np.interp(_position(text, after), [u for u, _ in pts], [t for _, t in pts]))
        taken = {j for a, j in pairs.items() if a != after}
        near = [j for j, g in enumerate(gaps) if j not in taken and abs(g.center - expect) <= _NEAR_S]
        j = min(near, key=lambda k: abs(gaps[k].center - expect), default=None)
        if j is None:
            report.missed += 1
            report.notes.append(f"no gap near the pause after word {after} ({ms} ms): the engine "
                                "ran straight through; left at its own length")
            continue
        extra = int(sr * (ms - gaps[j].ms) / 1000)
        report.spliced += 1
        if extra > 0:
            inserts.append((int(gaps[j].center * sr), extra))
    for pos, extra in sorted(inserts, reverse=True):  # back to front: positions stay valid
        left, right = wav[:pos], wav[pos:]
        wav = A.crossfade(A.crossfade(left, fill(extra + 2 * xf), sr, xfade_ms), right, sr, xfade_ms)
    return wav, report
