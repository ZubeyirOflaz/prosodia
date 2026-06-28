"""Pluggable TTS backend interface.

A backend turns text + per-segment parameters into a mono float32 waveform at a
fixed sample rate. Chatterbox is the first implementation; cloud engines (Gemini,
ElevenLabs) and other local engines can be added behind this interface (design
goal #5). numpy is referenced only in annotations so the interface is importable
without the heavy render deps.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import numpy as np


class TTSBackend(ABC):
    @property
    @abstractmethod
    def sample_rate(self) -> int:
        ...

    @abstractmethod
    def load(self) -> None:
        """Load model weights into memory (called once; keep the model warm)."""

    @abstractmethod
    def generate(
        self,
        text: str,
        *,
        exaggeration: float = 0.5,
        cfg_weight: float = 0.5,
        temperature: float = 0.8,
        rate_multiplier: float = 1.0,
        seed: int | None = None,
        audio_prompt_path: str | None = None,
        voice: str | None = None,
    ) -> "np.ndarray":
        """Return a mono float32 waveform at ``sample_rate`` for one short chunk.

        ``rate_multiplier`` is the engine-neutral pace (1.0 == normal; <1 slower,
        >1 faster); a backend realizes it however it can. ``voice`` is an
        engine-resolvable voice/preset id (e.g. ``preset:<name>``); a backend that
        cannot honor it should raise rather than silently substitute a default.
        """
