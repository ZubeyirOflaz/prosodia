"""Pace coupling for Chatterbox — pure, torch-free, so it is unit-testable.

Chatterbox has no direct speech-rate dial; pace is governed by ``cfg_weight``:
**lower cfg_weight = slower, more deliberate delivery** (per the Chatterbox docs
and DESIGN sec 10-G). So the engine-neutral ``rate`` is realized by scaling
cfg_weight: a slower rate (multiplier < 1) lowers cfg, a faster rate raises it.
"""

from __future__ import annotations

CFG_FLOOR = 0.20  # below this Chatterbox delivery degrades / slurs
CFG_CEIL = 0.95


def rate_adjusted_cfg(
    cfg_weight: float, rate_multiplier: float, *, floor: float = CFG_FLOOR, ceil: float = CFG_CEIL
) -> float:
    """Scale a tone's base ``cfg_weight`` by the engine-neutral rate multiplier.

    ``rate_multiplier`` is 1.0 at normal pace, <1 slower, >1 faster (see
    ``prosodia.core.intents``). Multiplying lowers cfg for a slow rate (slower
    delivery) and raises it for a fast rate, then clamps to a safe range.
    """
    if rate_multiplier <= 0:
        rate_multiplier = 1.0
    return max(floor, min(ceil, float(cfg_weight) * float(rate_multiplier)))
