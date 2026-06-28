"""The intermediate representation (IR) the renderer consumes.

Compiled from a transcript (``formats/SPEC.md``). The IR carries engine-neutral
*intent*; the engine-specific render plan is a separate, derived artifact
(``RenderPlan``), so the transcript never contains engine settings (design goal
#5: swappable engines).

A ``Segment`` is a contiguous run of speech with a single intent and no internal
pause — so every pause (paragraph break, beat boundary, explicit ``{pause}``)
becomes the ``pause_before_ms`` of the following segment. That makes the renderer
a simple loop: emit ``pause_before_ms`` of silence, then render the segment's
chunks with the params the Tone specialist assigned.
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from prosodia.core.intents import Intent

IR_VERSION = "0.1"


class Segment(BaseModel):
    id: int
    beat_index: int = 0
    beat_title: str | None = None
    speaker: str = "narrator"
    intent: Intent = Field(default_factory=Intent)
    pause_before_ms: int = 0
    authored_text: str = ""  # what the author wrote (provenance / traceability)
    spoken_text: str = ""  # normalized + lexicon-applied (what the engine says)
    # Emphasis spans, as the AUTHORED phrases (pre-normalization). These are NOT
    # guaranteed to appear verbatim in ``spoken_text`` — e.g. authored ``*1945*``
    # is recorded here as "1945" while spoken_text has "nineteen forty-five".
    # Renderers must not assume an emphasis span is locatable inside spoken_text.
    emphasis: list[str] = Field(default_factory=list)  # v0.1: informational
    chunks: list[str] = Field(default_factory=list)  # spoken_text split for the engine cap


class EpisodeIR(BaseModel):
    ir_version: str = IR_VERSION
    episode: int | None = None
    title: str | None = None
    voice: str = ""  # resolved voice id (see voice-resolution precedence in the SPEC)
    seed: int | None = None
    segments: list[Segment] = Field(default_factory=list)

    def to_json(self, indent: int = 2) -> str:
        return self.model_dump_json(indent=indent)

    @classmethod
    def from_json(cls, data: str) -> "EpisodeIR":
        return cls.model_validate_json(data)


class SegmentParams(BaseModel):
    """Engine-specific parameters for one segment (Chatterbox fields for v0.1)."""

    segment_id: int
    exaggeration: float
    cfg_weight: float
    temperature: float
    rate_multiplier: float = 1.0


class RenderPlan(BaseModel):
    """Derived from the IR by the Tone specialist; consumed by the renderer."""

    plan_version: str = "0.1"
    engine: str = "chatterbox"
    voice: str = ""
    seed: int | None = None
    params: list[SegmentParams] = Field(default_factory=list)

    def to_json(self, indent: int = 2) -> str:
        return self.model_dump_json(indent=indent)

    @classmethod
    def from_json(cls, data: str) -> "RenderPlan":
        return cls.model_validate_json(data)
