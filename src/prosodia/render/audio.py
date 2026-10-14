"""Audio assembly: room tone, lead/trail trim, click-free joins, loudness norm.

Pauses inside the episode are room tone (Chatterbox has no SSML break): noise shaped like the
background the generations themselves carry, so the background does not drop out at a pause.
The lead-in and tail stay digital silence: the final loudness pass is single-pass ``loudnorm``,
which adjusts gain over a few seconds at a time, and with no speech in that window it raised a
room-tone lead-in by ~33 dB — to nearly the level of the speech (Series B findings §6). Chunk
joins use a short linear crossfade to avoid clicks. Loudness normalization runs ONCE on the
final concatenation (per-chunk normalization would amplify volume drift).
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


FRAME_WIN_MS, FRAME_HOP_MS = 20, 10


def frame_db(wav: np.ndarray, sr: int) -> np.ndarray:
    """RMS level per 20 ms frame, every 10 ms, in dBFS."""
    win, hop = int(sr * FRAME_WIN_MS / 1000), int(sr * FRAME_HOP_MS / 1000)
    if wav.size < win or hop <= 0:
        return np.zeros(0, dtype=np.float32)
    wav = np.ascontiguousarray(wav)
    n = 1 + (wav.size - win) // hop
    frames = np.lib.stride_tricks.as_strided(
        wav, shape=(n, win), strides=(wav.strides[0] * hop, wav.strides[0]), writeable=False)
    return (10 * np.log10(np.mean(frames.astype(np.float64) ** 2, axis=1) + 1e-12)).astype(np.float32)


class RoomTone:
    """Background noise matched to the generations, for every silence the renderer inserts.

    Estimated from the quietest frames inside the generated chunks — the gaps between words,
    where only the background the engine copied from the reference clip remains — as a power
    spectrum and a level. Played back from a circular buffer of noise with that spectrum, so it
    loops without a seam. With too little quiet audio to measure, it is digital silence, which
    is what every pause was before.
    """

    _NFFT = 1024
    _BUFFER_S = 10.0

    def __init__(self, sr: int, spectrum: np.ndarray | None = None, rms: float = 0.0, seed: int = 0):
        self.sr, self.rms = sr, float(rms)
        self._buf = np.zeros(0, dtype=np.float32)
        self._rng = np.random.default_rng(seed)
        if spectrum is not None and self.rms > 0:
            n = int(sr * self._BUFFER_S)
            white = np.fft.rfft(self._rng.standard_normal(n))
            bins = np.linspace(0, len(spectrum) - 1, white.size)
            shape = np.sqrt(np.interp(bins, np.arange(len(spectrum)), spectrum))
            noise = np.fft.irfft(white * shape, n)
            level = float(np.sqrt(np.mean(noise ** 2)))
            if level > 0:
                self._buf = (noise * (self.rms / level)).astype(np.float32)

    @classmethod
    def estimate(cls, wavs: list[np.ndarray], sr: int, *, seed: int = 0,
                 max_seconds: float = 30.0, gain_db: float = 0.0) -> RoomTone:
        hop = int(sr * FRAME_HOP_MS / 1000)
        win = int(sr * FRAME_WIN_MS / 1000)
        quiet: list[np.ndarray] = []
        total = 0
        for wav in wavs:
            db = frame_db(wav, sr)
            if db.size < 10:
                continue
            low = db <= float(np.percentile(db, 10)) + 3.0
            i = 0
            while i < db.size:  # runs of at least three quiet frames
                if low[i]:
                    j = i
                    while j < db.size and low[j]:
                        j += 1
                    if j - i >= 3:
                        piece = wav[i * hop: (j - 1) * hop + win]
                        quiet.append(piece)
                        total += piece.size
                    i = j
                else:
                    i += 1
            if total >= sr * max_seconds:
                break
        if total < cls._NFFT * 4:
            return cls(sr, seed=seed)
        x = np.concatenate(quiet).astype(np.float64)
        rms = float(np.sqrt(np.mean(x ** 2)))
        win_fn = np.hanning(cls._NFFT)
        frames = [x[k:k + cls._NFFT] * win_fn for k in range(0, x.size - cls._NFFT, cls._NFFT // 2)]
        spectrum = np.mean(np.abs(np.fft.rfft(frames, axis=1)) ** 2, axis=0)
        return cls(sr, spectrum, rms * 10 ** (gain_db / 20), seed=seed)

    def __call__(self, n: int) -> np.ndarray:
        """``n`` samples of room tone (zeros when there is none)."""
        n = max(0, int(n))
        if not self._buf.size:
            return np.zeros(n, dtype=np.float32)
        start = int(self._rng.integers(self._buf.size))
        return np.take(self._buf, np.arange(start, start + n), mode="wrap")

    def gap(self, ms: int) -> np.ndarray:
        return self(int(self.sr * ms / 1000))


def join_with_gap(a: np.ndarray, gap: np.ndarray, b: np.ndarray, sr: int, ms: int = 10) -> np.ndarray:
    """``a`` + ``gap`` + ``b``, crossfaded at both seams; the overlap comes out of ``gap``'s ends,
    so pass a gap ``2 * ms`` longer than the pause it stands for."""
    return crossfade(crossfade(a, gap, sr, ms), b, sr, ms)


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
