"""Rate -> cfg_weight coupling must run in the correct direction.

Lower cfg_weight = slower/more deliberate (Chatterbox), so a slower rate must
LOWER cfg and a faster rate must RAISE it. This guards against the inverted
formula (cfg = cfg / rate) that made `rate: slow` speed the audio up.
"""

from prosodia.render.pacing import CFG_FLOOR, rate_adjusted_cfg


def test_normal_rate_is_identity():
    assert rate_adjusted_cfg(0.5, 1.0) == 0.5


def test_slow_rate_lowers_cfg():  # slower delivery
    assert rate_adjusted_cfg(0.5, 0.9) < 0.5
    assert rate_adjusted_cfg(0.5, 0.8) < rate_adjusted_cfg(0.5, 0.9)


def test_fast_rate_raises_cfg():  # faster delivery
    assert rate_adjusted_cfg(0.5, 1.1) > 0.5


def test_clamped_to_safe_range():
    assert rate_adjusted_cfg(0.1, 0.5) >= CFG_FLOOR  # never below the floor
    assert rate_adjusted_cfg(0.95, 1.5) <= 0.95
    assert rate_adjusted_cfg(0.5, 0.0) == 0.5  # guard against a zero multiplier
