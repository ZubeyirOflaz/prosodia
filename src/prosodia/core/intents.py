"""Engine-neutral delivery intent — the vocabulary the transcript carries.

The transcript expresses *what* delivery is wanted (somber, slow, a long beat),
never engine knobs. A separate mapping layer (the "Tone specialist",
``voice_profiles.yaml``) compiles intent into a specific engine's parameters, so
transcripts stay portable and durable.

Tone is an OPEN vocabulary (a free string): the canonical set and its parameter
mappings live in ``voice_profiles.yaml`` — the single source of truth (repair
item C2), not here. This module defines only the *structure* of an intent and
the closed ``rate`` vocabulary.
"""

from __future__ import annotations

from enum import Enum

from pydantic import BaseModel, Field


class Rate(str, Enum):
    very_slow = "very-slow"
    slow = "slow"
    normal = "normal"
    fast = "fast"
    very_fast = "very-fast"


# Normalized speech-rate multipliers for the closed rate words (1.0 == normal).
RATE_MULTIPLIERS: dict[str, float] = {
    Rate.very_slow.value: 0.80,
    Rate.slow.value: 0.90,
    Rate.normal.value: 1.00,
    Rate.fast.value: 1.10,
    Rate.very_fast.value: 1.20,
}


def rate_to_multiplier(rate: str | float | None) -> float:
    """Resolve a rate word or numeric multiplier to a float (1.0 == normal)."""
    if rate is None:
        return 1.0
    if isinstance(rate, (int, float)):
        return float(rate)
    key = str(rate).strip().lower()
    if key in RATE_MULTIPLIERS:
        return RATE_MULTIPLIERS[key]
    try:  # allow a bare numeric string, e.g. "1.05"
        return float(key)
    except ValueError as exc:
        raise ValueError(f"unknown rate: {rate!r}") from exc


class Intent(BaseModel):
    """Engine-neutral delivery intent for a span of speech."""

    tone: str = "measured"
    rate: str = Rate.normal.value
    note: str | None = Field(default=None, description="free-text nuance for the mapping layer")

    @property
    def rate_multiplier(self) -> float:
        return rate_to_multiplier(self.rate)
