"""Voice clip-prep: endpoint finding lands on a pause, timestamp parsing."""

import numpy as np
import pytest

from prosodia.author.voiceprep import find_clip_end, parse_timestamp


def test_parse_timestamp():
    assert parse_timestamp(12.5) == 12.5
    assert parse_timestamp("12.5") == 12.5
    assert parse_timestamp("1:30") == 90.0
    assert parse_timestamp("1:02:03") == 3723.0


def _speech_with_gaps(sr=22050, speech_s=1.5, gap_s=0.4, blocks=12, seed=0):
    """Bursts of noise (speech) separated by silent gaps."""
    rng = np.random.default_rng(seed)
    speech = rng.normal(0, 0.3, int(speech_s * sr)).astype(np.float32)
    gap = np.zeros(int(gap_s * sr), dtype=np.float32)
    return np.concatenate([np.concatenate([speech, gap]) for _ in range(blocks)])


def test_find_clip_end_lands_in_a_pause():
    sr = 22050
    audio = _speech_with_gaps(sr=sr)
    end = find_clip_end(audio, sr, start=0, target_s=10.0, min_s=8.0, max_s=14.0)
    # The end must be within the allowed window ...
    assert 8.0 * sr <= end <= 14.0 * sr
    # ... and sit in a low-energy region (a real pause), not mid-burst.
    frame = audio[max(0, end - int(0.02 * sr)): end + int(0.02 * sr)]
    assert float(np.sqrt(np.mean(frame**2))) < 0.1


def test_find_clip_end_falls_back_to_target_when_no_pause():
    sr = 22050
    audio = np.random.default_rng(1).normal(0, 0.3, 20 * sr).astype(np.float32)  # no gaps
    end = find_clip_end(audio, sr, start=0, target_s=10.0, min_s=8.0, max_s=14.0)
    assert end == 10 * sr  # exact target


def test_find_clip_end_handles_short_audio():
    sr = 16000
    audio = np.zeros(3 * sr, dtype=np.float32)  # shorter than min_s
    end = find_clip_end(audio, sr, start=0, target_s=10.0, min_s=8.0, max_s=14.0)
    assert end == len(audio)


@pytest.mark.skip(reason="manual: writes a file; exercised via the CLI")
def test_prepare_clip_smoke():
    pass
