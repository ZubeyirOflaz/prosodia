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


# MP3 settings matching the episodes that were converted by hand before the renderer did it:
# LAME VBR, mono, ~70 kbps at Chatterbox's 24 kHz — transparent for one speaking voice.
MP3_QUALITY = 2


def finalize_audio(
    in_path: str | Path,
    out_path: str | Path,
    target_lufs: float = -16.0,
    *,
    sr: int | None = None,
    tempo: float = 1.0,
    tags: dict | None = None,
) -> bool:
    """Tempo, EBU R128 loudness and the output encoding, in ONE ffmpeg pass. True on success.

    ``tempo`` < 1 slows the episode with ``atempo`` (WSOLA, pitch kept). It runs before
    ``loudnorm`` so loudness is measured on what is actually heard, and it scales the
    authored pauses with the speech — a slower speaker, not stretched words in fixed gaps.
    The encoding follows the suffix of ``out_path``: ``.mp3`` gets LAME VBR mono with ID3v2.3
    ``tags``; anything else is written as ffmpeg infers.

    ffmpeg's ``loudnorm`` filter resamples internally to 192 kHz; without an explicit
    output rate the final file is written at 192 kHz. Pass ``sr`` to pin the output
    back to the backend's sample rate.
    """
    filters = []
    if abs(float(tempo) - 1.0) > 1e-9:
        filters.append(f"atempo={float(tempo):g}")
    filters.append(f"loudnorm=I={target_lufs}:TP=-1.5:LRA=11")
    cmd = ["ffmpeg", "-y", "-i", str(in_path), "-af", ",".join(filters)]
    if sr:
        cmd += ["-ar", str(int(sr))]
    if Path(out_path).suffix.lower() == ".mp3":
        cmd += ["-ac", "1", "-c:a", "libmp3lame", "-q:a", str(MP3_QUALITY), "-id3v2_version", "3"]
        for key, value in (tags or {}).items():
            if value not in (None, ""):
                cmd += ["-metadata", f"{key}={value}"]
    cmd.append(str(out_path))
    try:
        subprocess.run(cmd, check=True, capture_output=True)
        return True
    except Exception:
        return False


def loudness_normalize(
    in_path: str | Path, out_path: str | Path, target_lufs: float = -16.0, *, sr: int | None = None
) -> bool:
    """EBU R128 loudness normalization only (no tempo, encoding from the suffix)."""
    return finalize_audio(in_path, out_path, target_lufs, sr=sr)
