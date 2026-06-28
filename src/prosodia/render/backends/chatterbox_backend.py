"""Chatterbox TTS backend.

Runs on the GPU box (requires the ``render`` extra). Loads the model once and
keeps it warm in VRAM; each call renders one short chunk. A fixed seed gives
reproducible-ish output (Chatterbox does not enable cuDNN-deterministic mode, so
it is perceptually identical, not bit-identical).
"""

from __future__ import annotations

import random

import numpy as np
import torch
from chatterbox.tts import ChatterboxTTS

from prosodia.render.backends.base import TTSBackend
from prosodia.render.pacing import rate_adjusted_cfg


def _set_seed(seed: int) -> None:
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)
    random.seed(seed)
    np.random.seed(seed)


class ChatterboxBackend(TTSBackend):
    def __init__(self, device: str | None = None):
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        self._model: ChatterboxTTS | None = None

    @property
    def sample_rate(self) -> int:
        self.load()
        return int(self._model.sr)

    def load(self) -> None:
        if self._model is None:
            self._model = ChatterboxTTS.from_pretrained(device=self.device)

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
    ) -> np.ndarray:
        self.load()
        if seed is not None:
            _set_seed(int(seed))
        # Chatterbox has no preset-voice catalog (it conditions on a reference
        # clip). A `preset:<name>` request can only be honored if it resolves to a
        # bundled clip upstream; reaching here with one means we cannot honor it,
        # so fail loudly rather than silently render the built-in default.
        if voice and voice.startswith("preset:"):
            raise ValueError(
                f"ChatterboxBackend cannot resolve preset voice {voice!r}; "
                "provide a reference .wav (cloning) instead"
            )
        # Tone/pace coupling (DESIGN sec 10-G): lower cfg_weight = slower/more
        # deliberate, so a slower rate (multiplier < 1) lowers cfg. See pacing.py.
        cfg = rate_adjusted_cfg(cfg_weight, rate_multiplier)
        wav = self._model.generate(
            text,
            audio_prompt_path=audio_prompt_path,
            exaggeration=exaggeration,
            cfg_weight=cfg,
            temperature=temperature,
        )
        arr = wav.detach().cpu().numpy() if hasattr(wav, "detach") else np.asarray(wav)
        return arr.astype(np.float32).reshape(-1)
