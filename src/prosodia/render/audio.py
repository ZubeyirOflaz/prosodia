"""Audio assembly: silence, lead/trail trim, click-free joins, loudness norm.

Pauses are inserted as real silence (Chatterbox has no SSML break). Chunk joins
use a short linear crossfade to avoid clicks. Loudness normalization runs ONCE on
the final concatenation (per-chunk normalization would amplify volume drift).
"""

from __future__ import annotations

import subprocess
from pathlib import Path

import numpy as np
import soundfile as sf


def silence(ms: int, sr: int) -> np.ndarray:
    return np.zeros(max(0, int(sr * ms / 1000)), dtype=np.float32)


def trim_silence(wav: np.ndarray, sr: int, threshold_db: float = -40.0, pad_ms: int = 50) -> np.ndarray:
    """Trim leading/trailing near-silence (keeps ``pad_ms`` of padding).

    An entirely-silent chunk collapses to empty: it carries no speech, so keeping
    its full length would inflate the episode duration when crossfaded in.
    """
    if wav.size == 0:
        return wav
    amp = 10.0 ** (threshold_db / 20.0)
    mask = np.abs(wav) > amp
    if not mask.any():
        return np.zeros(0, dtype=wav.dtype)
    first = int(np.argmax(mask))
    last = len(mask) - int(np.argmax(mask[::-1]))
    pad = int(sr * pad_ms / 1000)
    return wav[max(0, first - pad): min(len(wav), last + pad)]


def crossfade(a: np.ndarray, b: np.ndarray, sr: int, ms: int = 20) -> np.ndarray:
    """Concatenate a + b with a short equal-power-ish linear crossfade."""
    if a.size == 0:
        return b
    if b.size == 0:
        return a
    n = min(int(sr * ms / 1000), len(a), len(b))
    if n <= 0:
        return np.concatenate([a, b])
    fade = np.linspace(1.0, 0.0, n, dtype=np.float32)
    middle = a[-n:] * fade + b[:n] * (1.0 - fade)
    return np.concatenate([a[:-n], middle, b[n:]])


def peak_normalize(wav: np.ndarray, peak: float = 0.97) -> np.ndarray:
    m = float(np.abs(wav).max()) if wav.size else 0.0
    return (wav * (peak / m)).astype(np.float32) if m > 0 else wav


def write_wav(path: str | Path, wav: np.ndarray, sr: int) -> None:
    sf.write(str(path), wav, sr)


def loudness_normalize(in_path: str | Path, out_path: str | Path, target_lufs: float = -16.0) -> bool:
    """EBU R128 loudness normalization via ffmpeg. Returns True on success."""
    try:
        subprocess.run(
            [
                "ffmpeg", "-y", "-i", str(in_path),
                "-af", f"loudnorm=I={target_lufs}:TP=-1.5:LRA=11",
                str(out_path),
            ],
            check=True,
            capture_output=True,
        )
        return True
    except Exception:
        return False
