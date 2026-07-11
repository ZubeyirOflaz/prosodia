from prosodia.core.diagnosis import (
    apply_agent_result,
    build_agent_context,
    build_diagnosis,
    gather_signals,
)
from prosodia.core.lineage import Lineage, SegmentLineage
from prosodia.core.trace import TraceEvent


def _lineage_with_fallback():
    return Lineage(
        episode=6, title="The euro", editor_approved=True,
        tone_warnings=["segment 1: unknown tone 'brooding' -> fell back to 'measured'"],
        segments=[
            SegmentLineage(segment_id=0, beat_index=0, beat_title="A", tone="somber", cfg_weight=0.35),
            SegmentLineage(segment_id=1, beat_index=1, beat_title="B", tone="brooding",
                           tone_fallback=True, cfg_weight=0.50,
                           fallback_detail="segment 1: unknown tone 'brooding' -> fell back to 'measured'"),
        ],
    )


def test_tone_fallback_is_top_cause_for_flat_complaint():
    lin = _lineage_with_fallback()
    diag = build_diagnosis("the opening feels flat and lifeless", lin, events=[], episode=6)
    assert diag.most_likely is not None
    assert diag.most_likely.stage == "tone"
    assert diag.most_likely.confidence >= 0.8  # "flat"/"lifeless" boost the tone signal
    assert diag.most_likely.segment_ids == [1]
    assert any("brooding" in e for e in diag.most_likely.evidence)
    assert "voice_profiles.yaml" in (diag.most_likely.fix_command or "")
    assert "tone" in diag.summary.lower()


def test_error_event_outranks_everything():
    lin = _lineage_with_fallback()
    events = [TraceEvent(id="e09", stage="render", status="error", warnings=["CUDA out of memory"])]
    cands = gather_signals(lin, events, complaint="a word is garbled")
    assert cands[0].stage == "render" and cands[0].confidence >= 0.9


def test_pace_complaint_points_at_rate():
    lin = _lineage_with_fallback()
    cands = gather_signals(lin, [], complaint="the middle really drags, way too slow")
    assert any(c.stage == "tone" and "pac" in c.hypothesis.lower() for c in cands)


def test_catch_all_when_no_signal():
    lin = Lineage(episode=1, editor_approved=True,
                  segments=[SegmentLineage(segment_id=0, beat_index=0, beat_title="A",
                                           tone="measured", authored_preview="Once upon a time.")])
    diag = build_diagnosis("the ending is weird", lin, events=[], episode=1)
    assert diag.most_likely is not None
    assert diag.most_likely.stage == "write"  # falls back to the writing itself
    assert diag.candidates  # never empty


def test_apply_agent_result_merges_and_falls_back():
    lin = _lineage_with_fallback()
    base = build_diagnosis("flat open", lin, events=[], episode=6)
    out = {
        "summary": "Agent confirms the tone fallback.",
        "most_likely_index": 0,
        "candidates": [
            {"stage": "tone", "hypothesis": "unmapped tone", "confidence": 0.9, "recommended_fix": "add it"}
        ],
    }
    refined = apply_agent_result(base, out)
    assert refined.method == "agent"
    assert refined.most_likely.stage == "tone"
    assert refined.summary == "Agent confirms the tone fallback."
    # Bad / empty agent output leaves the deterministic diagnosis untouched.
    assert apply_agent_result(base, None).method == "signals"
    assert apply_agent_result(base, {"candidates": []}).method == "signals"


def test_build_agent_context_is_grounded():
    lin = _lineage_with_fallback()
    base = build_diagnosis("flat", lin, events=[], episode=6)
    ctx = build_agent_context(base, lin, events=[])
    assert "COMPLAINT: flat" in ctx
    assert "brooding" in ctx  # the fallback signal is surfaced to the agent
    assert "DETERMINISTIC CANDIDATES" in ctx
