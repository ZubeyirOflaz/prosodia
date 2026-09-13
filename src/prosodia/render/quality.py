"""Per-chunk quality gate via STT validation.

The single most impactful long-form technique: transcribe each generated chunk
with faster-whisper, compare to the intended text, and keep the best of N
candidates (retry-on-bad). Catches Chatterbox's hallucinations / repeats /
off-prompt continuation that crossfading cannot fix.

``similarity`` is pure-Python (no torch), so it is unit-testable on any machine;
``WhisperValidator`` imports faster-whisper lazily (render box only). It runs on
CPU too — the STT gate is cheap next to synthesis (~0.07x realtime), so a
CPU-only renderer pays almost nothing for it.
"""

from __future__ import annotations

import difflib
import re

_WORD = re.compile(r"[a-z0-9']+")


def _norm(s: str) -> str:
    return " ".join(_WORD.findall(s.lower()))


def similarity(a: str, b: str) -> float:
    """Word-level similarity ratio in [0, 1] between two strings."""
    return difflib.SequenceMatcher(None, _norm(a), _norm(b)).ratio()


class WhisperValidator:
    """faster-whisper wrapper. ``device``/``compute_type`` default to the best
    available: fp16 on a GPU, int8 on CPU (faster-whisper has no fp16 CPU path).
    """

    def __init__(
        self,
        model_size: str = "base.en",
        device: str | None = None,
        compute_type: str | None = None,
    ):
        from faster_whisper import WhisperModel

        from prosodia.render.device import resolve_device

        device = resolve_device(device)
        if compute_type is None:
            compute_type = "float16" if device.startswith("cuda") else "int8"
        self._model = WhisperModel(model_size, device=device, compute_type=compute_type)

    def transcribe(self, wav, sr: int) -> str:
        import numpy as np

        audio = wav
        if sr != 16000 and len(wav) > 0:  # faster-whisper expects 16 kHz mono float32
            n = int(round(len(wav) * 16000 / sr))
            if n > 0:
                audio = np.interp(
                    np.linspace(0, len(wav), n, endpoint=False),
                    np.arange(len(wav)),
                    wav,
                ).astype("float32")
        segments, _ = self._model.transcribe(audio, language="en")
        return " ".join(s.text for s in segments)

    def score(self, wav, sr: int, intended: str) -> float:
        try:
            return similarity(intended, self.transcribe(wav, sr))
        except Exception:
            return 0.0
