"""Voice reference-clip preparation.

Cuts a ~10s narration reference clip from a longer source WAV, starting at a
user-given timestamp and ending at a *good* point — a natural pause near the
target length, so the clip never ends mid-word. Downmixes to mono and trims
trailing silence. The endpoint search (``find_clip_end``) is pure NumPy so it is
unit-testable without any audio I/O.

Needs the ``audio`` extra (``pip install prosodia[audio]`` -> soundfile + numpy);
no torch, so it runs on the authoring machine. Chatterbox resamples the reference
internally, so we keep the source sample rate (recommend >= 24 kHz).
"""

from __future__ import annotations

from pathlib import Path

import numpy as np

# Endpoint search defaults.
FRAME_MS = 20  # RMS frame size for silence detection
SILENCE_DB = -25.0  # a frame this far below the window's loud frames counts as a pause


def parse_timestamp(value: str | float | int) -> float:
    """Parse seconds (``12.5``) or clock form (``M:SS`` / ``H:MM:SS``) to seconds."""
    if isinstance(value, (int, float)):
        return float(value)
    s = str(value).strip()
    if ":" in s:
        parts = [float(p) for p in s.split(":")]
        secs = 0.0
        for p in parts:
            secs = secs * 60 + p
        return secs
    return float(s)


def find_clip_end(
    audio: np.ndarray, sr: int, start: int, target_s: float, min_s: float, max_s: float
) -> int:
    """Return the end sample for a clip starting at ``start``.

    Looks for a natural pause (a low-energy frame) in the window
    ``[start+min_s, start+max_s]`` and cuts at the one nearest ``target_s``. If no
    pause is found, cuts at exactly ``target_s`` (clamped to the audio length).
    """
    n = len(audio)
    target_end = min(n, start + int(target_s * sr))
    lo = start + int(min_s * sr)
    hi = min(n, start + int(max_s * sr))
    if hi <= lo:  # not enough audio to search — take the target (or whatever's left)
        return target_end

    frame = max(1, int(FRAME_MS / 1000 * sr))
    window = audio[start:hi]
    nf = len(window) // frame
    if nf == 0:
        return target_end
    rms = np.sqrt(np.mean(window[: nf * frame].reshape(nf, frame) ** 2, axis=1))
    peak = float(rms.max()) or 1.0
    threshold = peak * (10.0 ** (SILENCE_DB / 20.0))

    f_lo = int((lo - start) / frame)
    f_target = int((target_end - start) / frame)
    silent = [i for i in range(f_lo, nf) if rms[i] < threshold]
    if not silent:
        return target_end
    best = min(silent, key=lambda i: abs(i - f_target))
    return start + best * frame


def _trim_trailing_silence(clip: np.ndarray, sr: int, pad_ms: int = 120) -> np.ndarray:
    """Trim trailing near-silence, leaving a short pad so the cut isn't abrupt."""
    if clip.size == 0:
        return clip
    threshold = float(np.abs(clip).max()) * (10.0 ** (-30.0 / 20.0))
    loud = np.where(np.abs(clip) > threshold)[0]
    if loud.size == 0:
        return clip
    end = min(len(clip), int(loud[-1]) + int(pad_ms / 1000 * sr))
    return clip[:end]


def prepare_clip(
    source: str | Path,
    start: str | float,
    out: str | Path,
    *,
    target_s: float = 10.0,
    min_s: float | None = None,
    max_s: float | None = None,
) -> dict:
    """Cut a mono reference clip from ``source`` starting at ``start``.

    ``target_s`` sets the desired length; the endpoint snaps to a natural pause
    near it. ``min_s``/``max_s`` bound that pause search and, when not given,
    DEFAULT TO scaling with ``target_s`` — so any ``target_s`` works and the clip
    is no longer capped at ~14 s. Pass them explicitly for full control.

    Returns ``{duration, sr, start, warnings}``. Raises ``ValueError`` if the
    start is past the end of the audio.
    """
    import soundfile as sf

    # Scale the search window to the requested length unless the caller overrides,
    # so a longer neutral clip (more of the narrator's range) is reachable.
    if min_s is None:
        min_s = max(3.0, target_s * 0.8)
    if max_s is None:
        max_s = max(target_s + 3.0, target_s * 1.35)

    start_s = parse_timestamp(start)
    audio, sr = sf.read(str(source), always_2d=False)
    if audio.ndim > 1:  # downmix to mono
        audio = audio.mean(axis=1)
    audio = np.asarray(audio, dtype=np.float32)

    warnings: list[str] = []
    if sr < 24000:
        warnings.append(f"source is {sr} Hz; Chatterbox cloning prefers >= 24 kHz")

    start_sample = int(start_s * sr)
    if start_sample >= len(audio):
        raise ValueError(
            f"start {start_s:.1f}s is past the audio length ({len(audio) / sr:.1f}s)"
        )

    end_sample = find_clip_end(audio, sr, start_sample, target_s, min_s, max_s)
    clip = _trim_trailing_silence(audio[start_sample:end_sample], sr)

    duration = len(clip) / sr
    if duration < min_s - 1.0:
        warnings.append(
            f"clip is only {duration:.1f}s (wanted ~{target_s:.0f}s); "
            "try another start or a longer clean stretch"
        )

    out = Path(out)
    out.parent.mkdir(parents=True, exist_ok=True)
    sf.write(str(out), clip, sr)
    return {"duration": duration, "sr": sr, "start": start_s, "warnings": warnings}
