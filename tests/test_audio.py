"""Tests for the pure-numpy audio helpers (finding 28).

These need numpy; the file is skipped on the strict authoring install where numpy
is absent. soundfile (write_wav/loudness_normalize) is not exercised here.
"""

import pytest

np = pytest.importorskip("numpy")

from prosodia.render import audio as A  # noqa: E402  (after importorskip)

SR = 16000


def test_silence_length():
    assert len(A.silence(1000, SR)) == SR
    assert len(A.silence(0, SR)) == 0
    assert len(A.silence(-10, SR)) == 0


def test_crossfade_identity():
    a = np.ones(100, dtype=np.float32)
    b = np.ones(100, dtype=np.float32)
    empty = np.zeros(0, dtype=np.float32)
    assert np.array_equal(A.crossfade(empty, b, SR), b)
    assert np.array_equal(A.crossfade(a, empty, SR), a)
    n = 100
    fade = min(int(SR * 20 / 1000), n, n)  # crossfade default ms=20
    joined = A.crossfade(a, b, SR)
    assert len(joined) == 2 * n - fade


def test_peak_normalize():
    wav = np.array([0.1, -0.2, 0.05], dtype=np.float32)
    out = A.peak_normalize(wav, peak=0.97)
    assert abs(float(np.abs(out).max()) - 0.97) < 1e-5
    zeros = np.zeros(10, dtype=np.float32)
    assert np.array_equal(A.peak_normalize(zeros), zeros)  # no-op on silence


def test_trim_silence_keeps_padding():
    sr = 1000  # 1 ms == 1 sample, easy to reason about
    speech = np.ones(500, dtype=np.float32)
    padded = np.concatenate([np.zeros(300, dtype=np.float32), speech, np.zeros(300, dtype=np.float32)])
    trimmed = A.trim_silence(padded, sr, pad_ms=50)  # keep 50 samples padding
    # Trimmed length is the speech plus up to 2*pad, and well under the original.
    assert 500 <= len(trimmed) <= 500 + 2 * 50
    assert len(trimmed) < len(padded)


def test_trim_silence_all_silent_collapses():
    # An entirely-silent chunk collapses to empty (finding 12), not full length.
    silent = np.zeros(1000, dtype=np.float32)
    assert A.trim_silence(silent, SR).size == 0
