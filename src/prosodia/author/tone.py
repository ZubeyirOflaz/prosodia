"""The Tone specialist (stage 1, deterministic).

Loads ``voice_profiles.yaml`` and compiles an ``EpisodeIR``'s engine-neutral
intents into a Chatterbox ``RenderPlan``. This is the single place delivery is
tuned, and the single source of truth for the tone vocabulary (repair C2) and
default pause durations (repair C3). A later, optional LLM-driven Tone specialist
can replace this behind the same ``build_render_plan`` interface.
"""

from __future__ import annotations

from importlib import resources
from pathlib import Path

import yaml

from prosodia.core.ir import EpisodeIR, RenderPlan, SegmentParams

_FALLBACK = {"exaggeration": 0.40, "cfg_weight": 0.50, "temperature": 0.75}


class VoiceProfiles:
    def __init__(self, data: dict):
        self.engine: str = data.get("engine", "chatterbox")
        self.default_tone: str = data.get("default_tone", "measured")
        self.tones: dict[str, dict] = data.get("tones", {})
        pauses = data.get("pauses", {}) or {}
        self.paragraph_ms = int(pauses.get("paragraph_ms", 400))
        self.beat_ms = int(pauses.get("beat_ms", 800))

    @classmethod
    def load(cls, path: Path | None = None) -> "VoiceProfiles":
        if path is None:
            text = (
                resources.files("prosodia.author")
                .joinpath("voice_profiles.yaml")
                .read_text(encoding="utf-8")
            )
        else:
            text = Path(path).read_text(encoding="utf-8")
        return cls(yaml.safe_load(text))

    def known_tones(self) -> set[str]:
        return set(self.tones)

    def params_for_tone(self, tone: str) -> tuple[dict, bool]:
        """Return (params, ok); ok=False means the tone was unknown and we fell back."""
        if tone in self.tones:
            return self.tones[tone], True
        return self.tones.get(self.default_tone, _FALLBACK), False


def build_render_plan(
    ir: EpisodeIR, profiles: VoiceProfiles | None = None
) -> tuple[RenderPlan, list[str]]:
    """Compile an IR into a RenderPlan. Returns (plan, warnings)."""
    profiles = profiles or VoiceProfiles.load()
    warnings: list[str] = []
    params: list[SegmentParams] = []
    for seg in ir.segments:
        p, ok = profiles.params_for_tone(seg.intent.tone)
        if not ok:
            warnings.append(
                f"segment {seg.id}: unknown tone '{seg.intent.tone}' -> "
                f"fell back to '{profiles.default_tone}'"
            )
        params.append(
            SegmentParams(
                segment_id=seg.id,
                exaggeration=float(p.get("exaggeration", _FALLBACK["exaggeration"])),
                cfg_weight=float(p.get("cfg_weight", _FALLBACK["cfg_weight"])),
                temperature=float(p.get("temperature", _FALLBACK["temperature"])),
                rate_multiplier=seg.intent.rate_multiplier,
            )
        )
    return RenderPlan(engine=profiles.engine, voice=ir.voice, seed=ir.seed, params=params), warnings
