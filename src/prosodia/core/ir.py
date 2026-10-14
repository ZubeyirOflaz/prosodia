"""The intermediate representation (IR) the renderer consumes.

Compiled from a transcript (``formats/SPEC.md``). The IR carries engine-neutral
*intent*; the engine-specific render plan is a separate, derived artifact
(``RenderPlan``), so the transcript never contains engine settings (design goal
#5: swappable engines).

A ``Segment`` is a contiguous run of speech with a single intent: it ends only where the
delivery changes (tone, rate, note, speaker), at a beat boundary, or at a quotation. A pause
or paragraph break INSIDE that run is an inner pause — ``chunk_pauses``: "N ms after the k-th
word of this chunk" — so the words on both sides are generated together and the voice knows
the sentence is not finished. A pause where the delivery changes is the next segment's
``pause_before_ms``. (IR 0.1 had no inner pauses: every pause split the segment, and every
split became a separate generation that ended like a full stop.)
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from prosodia.core.intents import Intent

IR_VERSION = "0.2"


class InnerPause(BaseModel):
    """A pause inside one generation: ``ms`` of silence after the first ``after_word`` words.

    Words are the chunk's whitespace-separated tokens. ``after_word`` equal to the chunk's word
    count means the pause falls between this chunk and the next.
    """

    after_word: int = Field(ge=1)
    ms: int = Field(ge=0)


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
    # Per-chunk reference text for the render-side STT quality gate, with lexicon
    # respellings mapped BACK to their source spellings (what Whisper writes for a
    # correct pronunciation). Populated only when it differs from ``chunks`` (i.e. a
    # respelling was applied in this segment); empty otherwise, and the renderer then
    # scores against ``chunks``. Parallel to ``chunks`` when present.
    score_chunks: list[str] = Field(default_factory=list)
    # Pauses inside the segment, per chunk (parallel to ``chunks``); empty when there are none.
    chunk_pauses: list[list[InnerPause]] = Field(default_factory=list)


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
    # Playback tempo for the finished episode, applied once by the renderer (ffmpeg `atempo`,
    # pitch kept). 1.0 = as generated. Plans written before this field existed read as 1.0.
    tempo: float = Field(1.0, ge=0.5, le=2.0)

    def to_json(self, indent: int = 2) -> str:
        return self.model_dump_json(indent=indent)

    @classmethod
    def from_json(cls, data: str) -> "RenderPlan":
        return cls.model_validate_json(data)
