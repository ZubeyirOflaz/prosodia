"""Diagnosis: rank the probable sources of a reported problem across the pipeline.

Two layers, mirroring the rest of the system:

* a deterministic **signal pass** (:func:`gather_signals`) turns concrete trace
  evidence — tone fallbacks, error events, an unresolved Editor loop, compile
  warnings — plus keyword cues in the complaint into ranked
  :class:`CauseCandidate`s. It always yields a usable answer, with no model call.
* the ``diagnose`` command can then hand these to a Claude agent to re-rank and
  enrich them (see ``roles/diagnostician.md``); the agent's output is validated
  back into this same :class:`Diagnosis` model.

The models are plain pydantic — no agent harness.
"""

from __future__ import annotations

import re

from pydantic import BaseModel, Field

from prosodia.core.lineage import Lineage
from prosodia.core.trace import TraceEvent

# Complaint keyword cues -> the stage they implicate (used only to *boost*
# confidence of an already-evidenced candidate, never to invent one).
KEYWORDS: dict[str, list[str]] = {
    "tone": ["flat", "monotone", "lifeless", "dull", "emotion", "delivery", "tone",
             "dramatic", "somber", "energy", "feeling", "wooden", "robotic"],
    "rate": ["drag", "drags", "slow", "fast", "rush", "pace", "pacing", "speed", "plod", "hurried"],
    "compile": ["mispronounce", "pronounce", "pronunciation", "garbled", "number",
                "date", "abbreviation", "spelled", "acronym"],
    "write": ["boring", "weak", "writing", "confusing", "unclear", "awkward",
              "cliche", "repetitive", "generic", "bland"],
    "plan": ["repeat", "repeats", "overlap", "skip", "skips", "missing", "covered", "recap", "order"],
}


class CauseCandidate(BaseModel):
    stage: str  # plan | write | edit | compile | tone | submit | render
    event_id: str | None = None
    segment_ids: list[int] = Field(default_factory=list)
    hypothesis: str
    evidence: list[str] = Field(default_factory=list)
    confidence: float = 0.5  # 0..1
    recommended_fix: str = ""
    fix_command: str | None = None


class Diagnosis(BaseModel):
    id: str = "diag-001"
    complaint: str = ""
    scope_episode: int | None = None
    scope_beat: int | None = None
    created: str = ""
    method: str = "signals"  # "signals" (deterministic) | "agent" (LLM-refined)
    most_likely: CauseCandidate | None = None
    candidates: list[CauseCandidate] = Field(default_factory=list)
    summary: str = ""

    def to_json(self, indent: int = 2) -> str:
        return self.model_dump_json(indent=indent)

    @classmethod
    def from_json(cls, data: str) -> "Diagnosis":
        return cls.model_validate_json(data)


def _mentions(complaint: str, stage: str) -> bool:
    # Whole-word match: a plain substring test fired on benign complaints (e.g. "space"
    # matched "pace", "update" matched "date"), inventing spurious cause candidates.
    c = complaint.lower()
    return any(re.search(rf"\b{re.escape(k)}\b", c) for k in KEYWORDS.get(stage, []))


def gather_signals(
    lineage: Lineage,
    events: list[TraceEvent],
    *,
    complaint: str = "",
    beat: int | None = None,
) -> list[CauseCandidate]:
    """Deterministically rank candidate sources from trace evidence + the complaint."""
    cands: list[CauseCandidate] = []
    focus = [s for s in lineage.segments if beat is None or s.beat_index == beat]

    # 1) A stage that errored is the strongest possible signal.
    for ev in events:
        if ev.status == "error":
            cands.append(CauseCandidate(
                stage=ev.stage, event_id=ev.id,
                hypothesis=f"The {ev.stage} stage failed (status=error); nothing downstream can be right.",
                evidence=ev.warnings or [f"{ev.stage}: status=error"],
                confidence=0.92,
                recommended_fix=f"Inspect the {ev.stage} stage's output in the trace and re-run it.",
            ))

    # 2) Tone fell back to a default -> delivery won't match the authored intent.
    fb = [s for s in focus if s.tone_fallback]
    if fb:
        tones = sorted({s.tone for s in fb})
        cands.append(CauseCandidate(
            stage="tone",
            segment_ids=[s.segment_id for s in fb],
            hypothesis=(
                f"{len(fb)} segment(s) asked for tone(s) {tones} that aren't in the tone "
                "table, so the Tone specialist silently used the default — the delivery "
                "won't match what the Writer intended."
            ),
            evidence=[s.fallback_detail for s in fb if s.fallback_detail][:6],
            confidence=0.85 if _mentions(complaint, "tone") else 0.6,
            recommended_fix=(
                f"Add {tones} to voice_profiles.yaml with tuned exaggeration/cfg_weight, "
                "or change the beat's tone to a mapped one; then recompile."
            ),
            fix_command="edit the persona's voice_profiles.yaml",
        ))

    # 3) The Editor never approved the episode (loop hit max_rounds).
    unresolved = [ev for ev in events if ev.stage == "edit" and ev.status == "warn"]
    if unresolved or lineage.editor_approved is False:
        cands.append(CauseCandidate(
            stage="write", event_id=(unresolved[-1].id if unresolved else None),
            hypothesis=(
                "The Editor never approved this episode (the loop hit max_rounds), so the "
                "shipped draft still had open editorial notes."
            ),
            evidence=lineage.editor_notes[-2:],
            confidence=0.7 if _mentions(complaint, "write") else 0.5,
            recommended_fix="Re-run `write` with a higher --max-rounds, or address the last editorial note directly.",
        ))

    # 4) Compile warnings can distort the spoken text (bad directive / normalization).
    if lineage.compile_warnings:
        cands.append(CauseCandidate(
            stage="compile",
            hypothesis="Compile emitted warnings (a malformed directive or normalization issue) that can change what is actually spoken.",
            evidence=lineage.compile_warnings[:6],
            confidence=0.75 if _mentions(complaint, "compile") else 0.4,
            recommended_fix="Fix the flagged directive; for a mispronounced name add a lexicon entry, then recompile.",
        ))

    # 5) Complaint is explicitly about pace -> point at rate / cfg_weight.
    if _mentions(complaint, "rate") and focus:
        cands.append(CauseCandidate(
            stage="tone",
            segment_ids=[s.segment_id for s in focus],
            hypothesis="The complaint is about pacing; the beat's rate (and the tone's cfg_weight) may not match the delivery you want.",
            evidence=[f"beat {s.beat_index}: rate={s.rate}, cfg_weight={s.cfg_weight}" for s in focus[:4]],
            confidence=0.55,
            recommended_fix="Adjust the beat's rate, or lower the tone's cfg_weight in voice_profiles.yaml (lower = slower/more deliberate).",
            fix_command="edit the persona's voice_profiles.yaml",
        ))

    # 6) Complaint is about coverage/repetition -> plan / cross-episode freshness.
    if _mentions(complaint, "plan"):
        cands.append(CauseCandidate(
            stage="plan",
            hypothesis="The complaint is about coverage or repetition; the outline's episode boundary or the cross-episode avoid-list is the likely lever.",
            evidence=[],
            confidence=0.5,
            recommended_fix="Review the outline's coverage map and run lint-repetition; adjust the boundary or the feed-forward avoid-list, then re-write.",
            fix_command="python -m prosodia.author.cli lint-repetition --project <project>",
        ))

    # Catch-all: if nothing is strong, the cause is most likely the writing itself.
    if not cands or max(c.confidence for c in cands) < 0.5:
        cands.append(CauseCandidate(
            stage="write",
            segment_ids=[s.segment_id for s in focus[:6]],
            hypothesis="No single automated signal isolates this — most likely the writing itself (word choice, rhythm), or an intent that reads fine but renders weakly.",
            evidence=[f"beat {s.beat_index} '{s.beat_title}': {s.authored_preview}" for s in focus[:3]],
            confidence=0.35,
            recommended_fix="Re-read the beat's authored text; if the words are right, adjust its tone/rate; if not, re-run the Writer for that beat with a specific note.",
        ))

    cands.sort(key=lambda c: c.confidence, reverse=True)
    return cands


def _summarize(cands: list[CauseCandidate], complaint: str) -> str:
    if not cands:
        return "No candidate sources were identified."
    top = cands[0]
    return (
        f"Most likely source: the {top.stage} stage "
        f"({int(round(top.confidence * 100))}% confidence). {top.hypothesis} "
        f"{len(cands)} candidate source(s) considered across the process."
    )


def build_diagnosis(
    complaint: str,
    lineage: Lineage,
    events: list[TraceEvent],
    *,
    episode: int | None = None,
    beat: int | None = None,
    diag_id: str = "diag-001",
    created: str = "",
) -> Diagnosis:
    """Assemble a full deterministic Diagnosis from the signal pass."""
    cands = gather_signals(lineage, events, complaint=complaint, beat=beat)
    return Diagnosis(
        id=diag_id,
        complaint=complaint,
        scope_episode=episode,
        scope_beat=beat,
        created=created,
        method="signals",
        most_likely=cands[0] if cands else None,
        candidates=cands,
        summary=_summarize(cands, complaint),
    )


# --- Agent refinement (optional) ---------------------------------------------
# The ``diagnose`` command may hand the deterministic candidates + trace digest to
# a Claude agent (roles/diagnostician.md) to re-rank and enrich them. The agent
# returns THIS shape; it is validated straight back into CauseCandidate/Diagnosis
# (no agent harness — just structured output).

DIAGNOSIS_SCHEMA = {
    "type": "object",
    "properties": {
        "summary": {"type": "string"},
        "most_likely_index": {"type": "integer"},
        "candidates": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "stage": {"type": "string"},
                    "hypothesis": {"type": "string"},
                    "evidence": {"type": "array", "items": {"type": "string"}},
                    "confidence": {"type": "number"},
                    "recommended_fix": {"type": "string"},
                    "fix_command": {"type": "string"},
                    "segment_ids": {"type": "array", "items": {"type": "integer"}},
                },
                "required": ["stage", "hypothesis", "confidence", "recommended_fix"],
            },
        },
    },
    "required": ["summary", "candidates"],
}


def build_agent_context(diag: Diagnosis, lineage: Lineage, events: list[TraceEvent]) -> str:
    """A compact, model-legible digest of the run for the diagnostician agent."""
    lines = [
        f"COMPLAINT: {diag.complaint}",
        f"SCOPE: episode {diag.scope_episode}, "
        + (f"beat {diag.scope_beat}" if diag.scope_beat is not None else "whole episode"),
        "",
        "PIPELINE TRACE (stage [status] round :: warnings):",
    ]
    for ev in events:
        rnd = f" r{ev.round}" if ev.round is not None else ""
        warns = f" :: {'; '.join(ev.warnings)}" if ev.warnings else ""
        lines.append(f"  {ev.stage} [{ev.status}]{rnd}{warns}")
    if lineage.editor_notes:
        lines += ["", "EDITOR NOTES:"] + [f"  {n}" for n in lineage.editor_notes]

    focus = [s for s in lineage.segments if diag.scope_beat is None or s.beat_index == diag.scope_beat]
    lines += ["", f"SEGMENTS (showing {min(len(focus), 12)} of {len(focus)}): beat · tone/rate · exagg/cfg · fallback"]
    for s in focus[:12]:
        fb = " · TONE-FALLBACK" if s.tone_fallback else ""
        lines.append(
            f"  seg {s.segment_id} b{s.beat_index} '{s.beat_title}': {s.tone}/{s.rate} · "
            f"{s.exaggeration}/{s.cfg_weight}{fb} · \"{s.spoken_preview}\""
        )
    lines += ["", "DETERMINISTIC CANDIDATES (baseline ranking; refine, re-rank, and enrich):"]
    for c in diag.candidates:
        lines.append(f"  [{c.confidence:.2f}] {c.stage}: {c.hypothesis}")
    lines += [
        "",
        "Return a ranked `candidates` list (most likely first), `most_likely_index`, and a `summary`. "
        "Only cite evidence present in the trace above. Every candidate needs a concrete recommended_fix.",
    ]
    return "\n".join(lines)


def apply_agent_result(base: Diagnosis, out: dict | None) -> Diagnosis:
    """Merge a validated agent result into ``base``; fall back to ``base`` on any problem."""
    if not out:
        return base
    try:
        cands = [CauseCandidate.model_validate(c) for c in out.get("candidates", [])]
    except Exception:
        return base
    if not cands:
        return base
    idx = out.get("most_likely_index", 0)
    if not isinstance(idx, int) or not (0 <= idx < len(cands)):
        idx = 0
    return base.model_copy(update={
        "method": "agent",
        "candidates": cands,
        "most_likely": cands[idx],
        "summary": out.get("summary") or base.summary,
    })
