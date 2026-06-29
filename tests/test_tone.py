from prosodia.author.tone import VoiceProfiles, build_render_plan
from prosodia.core.intents import Intent
from prosodia.core.ir import EpisodeIR, Segment

# The tones documented in formats/SPEC.md sec 5.1 must all be mapped (repair C2).
SPEC_TONES = [
    "measured", "neutral", "warm", "somber", "grave", "tense",
    "urgent", "dramatic", "wry", "wistful", "reverent", "matter-of-fact",
]


def test_all_spec_tones_are_mapped():
    profiles = VoiceProfiles.load()
    missing = [t for t in SPEC_TONES if t not in profiles.known_tones()]
    assert not missing, f"tones in the SPEC missing from voice_profiles.yaml: {missing}"


def test_default_pauses_present():
    profiles = VoiceProfiles.load()
    assert profiles.paragraph_ms > 0 and profiles.beat_ms > profiles.paragraph_ms


def test_global_pace_scales_cfg():
    base = {"default_tone": "measured",
            "tones": {"measured": {"exaggeration": 0.4, "cfg_weight": 0.5, "temperature": 0.75}}}
    ir = EpisodeIR(segments=[Segment(id=0, intent=Intent(tone="measured"), spoken_text="a", chunks=["a"])])
    full = build_render_plan(ir, VoiceProfiles({**base, "pace": 1.0}))[0]
    slow = build_render_plan(ir, VoiceProfiles({**base, "pace": 0.8}))[0]
    assert full.params[0].cfg_weight == 0.5
    assert slow.params[0].cfg_weight < full.params[0].cfg_weight  # 0.5 * 0.8 = 0.4


def test_build_render_plan_and_unknown_tone():
    ir = EpisodeIR(
        voice="narrator",
        seed=1,
        segments=[
            Segment(id=0, intent=Intent(tone="somber", rate="slow"), spoken_text="a", chunks=["a"]),
            Segment(id=1, intent=Intent(tone="zzz-unknown"), spoken_text="b", chunks=["b"]),
        ],
    )
    plan, warnings = build_render_plan(ir)
    assert plan.voice == "narrator" and plan.seed == 1 and len(plan.params) == 2
    # somber maps to a lower cfg_weight (slower/more deliberate) than the 0.5 default.
    assert plan.params[0].cfg_weight < 0.5
    assert plan.params[0].rate_multiplier < 1.0  # rate: slow
    assert any("unknown tone" in w for w in warnings)
