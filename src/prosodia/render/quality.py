"""Per-chunk quality gate via STT validation.

The single most impactful long-form technique: transcribe each generated chunk
with faster-whisper, compare to the intended text, and keep the best of N
candidates (retry-on-bad). Catches Chatterbox's hallucinations / repeats /
off-prompt continuation that crossfading cannot fix.

``similarity`` is pure-Python (no torch), so it is unit-testable on any machine;
``WhisperValidator`` imports faster-whisper lazily (GPU box only).
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
    def __init__(self, model_size: str = "base.en", device: str = "cuda", compute_type: str = "float16"):
        from faster_whisper import WhisperModel

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
