"""Segment-level lineage — the spine the diagnosis walks.

For each final IR segment this joins, in one record, everything that decided how
it turns out: which beat it belongs to, the engine-neutral intent the Writer
gave it, the concrete params the Tone specialist resolved (matched by segment id
through the render plan), and whether that tone fell back to a default. It also
rolls up episode-level context from the trace — how many Writer rounds ran,
whether the Editor ever approved, and each stage's warnings.

Built from ``(EpisodeIR, RenderPlan, events)`` so it is pure and testable; the
CLI persists it to ``run/lineage.json`` at compile time.
"""

from __future__ import annotations

import re

from pydantic import BaseModel, Field

from prosodia.core.ir import EpisodeIR, RenderPlan
from prosodia.core.trace import TraceEvent

_SEG_RE = re.compile(r"segment\s+(\d+)\b")


class SegmentLineage(BaseModel):
    segment_id: int
    beat_index: int = 0
    beat_title: str | None = None
    speaker: str = "narrator"
    tone: str = ""
    rate: str = ""
    note: str | None = None
    tone_fallback: bool = False
    fallback_detail: str | None = None
    pause_before_ms: int = 0
    exaggeration: float | None = None
    cfg_weight: float | None = None
    temperature: float | None = None
    rate_multiplier: float | None = None
    authored_preview: str = ""
    spoken_preview: str = ""


class Lineage(BaseModel):
    episode: int | None = None
    title: str | None = None
    voice: str = ""
    seed: int | None = None
    num_write_rounds: int = 0
    final_round: int | None = None
    editor_approved: bool | None = None
    editor_notes: list[str] = Field(default_factory=list)
    compile_warnings: list[str] = Field(default_factory=list)
    tone_warnings: list[str] = Field(default_factory=list)
    segments: list[SegmentLineage] = Field(default_factory=list)

    def to_json(self, indent: int = 2) -> str:
        return self.model_dump_json(indent=indent)

    @classmethod
    def from_json(cls, data: str) -> "Lineage":
        return cls.model_validate_json(data)

    def beat(self, index: int) -> list[SegmentLineage]:
        return [s for s in self.segments if s.beat_index == index]


def _preview(text: str, n: int = 90) -> str:
    text = " ".join(text.split())
    return text if len(text) <= n else text[: n - 1] + "…"


def build_lineage(
    ir: EpisodeIR, plan: RenderPlan, events: list[TraceEvent] | None = None
) -> Lineage:
    """Join the IR, the render plan, and the trace into a per-segment lineage."""
    events = events or []
    params_by_id = {p.segment_id: p for p in plan.params}

    fallback_by_seg: dict[int, str] = {}
    tone_warnings: list[str] = []
    compile_warnings: list[str] = []
    editor_notes: list[str] = []
    write_rounds: list[int] = []
    editor_approved: bool | None = None
    for ev in events:
        if ev.stage == "tone":
            for w in ev.warnings:
                tone_warnings.append(w)
                m = _SEG_RE.search(w)
                if m:
                    fallback_by_seg[int(m.group(1))] = w
        elif ev.stage == "compile":
            compile_warnings.extend(ev.warnings)
        elif ev.stage == "edit":
            note = ev.meta.get("notes")
            if note:
                editor_notes.append(f"r{ev.round}: {note}")
            editor_approved = bool(ev.meta.get("ready"))  # last edit wins
        elif ev.stage == "write" and ev.round is not None:
            write_rounds.append(ev.round)

    segments = [
        SegmentLineage(
            segment_id=seg.id,
            beat_index=seg.beat_index,
            beat_title=seg.beat_title,
            speaker=seg.speaker,
            tone=seg.intent.tone,
            rate=seg.intent.rate,
            note=seg.intent.note,
            tone_fallback=seg.id in fallback_by_seg,
            fallback_detail=fallback_by_seg.get(seg.id),
            pause_before_ms=seg.pause_before_ms,
            exaggeration=(p.exaggeration if (p := params_by_id.get(seg.id)) else None),
            cfg_weight=(params_by_id[seg.id].cfg_weight if seg.id in params_by_id else None),
            temperature=(params_by_id[seg.id].temperature if seg.id in params_by_id else None),
            rate_multiplier=(params_by_id[seg.id].rate_multiplier if seg.id in params_by_id else None),
            authored_preview=_preview(seg.authored_text),
            spoken_preview=_preview(seg.spoken_text),
        )
        for seg in ir.segments
    ]

    return Lineage(
        episode=ir.episode,
        title=ir.title,
        voice=ir.voice,
        seed=ir.seed,
        num_write_rounds=len(write_rounds),
        final_round=max(write_rounds) if write_rounds else None,
        editor_approved=editor_approved,
        editor_notes=editor_notes,
        compile_warnings=compile_warnings,
        tone_warnings=tone_warnings,
        segments=segments,
    )
