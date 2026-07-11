from prosodia.core.intents import Intent
from prosodia.core.ir import EpisodeIR, RenderPlan, Segment, SegmentParams
from prosodia.core.lineage import build_lineage
from prosodia.core.trace import TraceEvent


def _fixture():
    ir = EpisodeIR(
        episode=6,
        title="The euro",
        voice="narrator",
        seed=7,
        segments=[
            Segment(id=0, beat_index=0, beat_title="A", intent=Intent(tone="somber", rate="slow"),
                    authored_text="Picture the ruin.", spoken_text="Picture the ruin."),
            Segment(id=1, beat_index=1, beat_title="B", intent=Intent(tone="brooding"),
                    authored_text="It might happen again.", spoken_text="It might happen again."),
        ],
    )
    plan = RenderPlan(params=[
        SegmentParams(segment_id=0, exaggeration=0.35, cfg_weight=0.35, temperature=0.75),
        SegmentParams(segment_id=1, exaggeration=0.40, cfg_weight=0.50, temperature=0.75),
    ])
    events = [
        TraceEvent(id="e01", stage="write", role="writer", round=1),
        TraceEvent(id="e02", stage="edit", role="editor", round=1, meta={"ready": False, "notes": "tighten open"}),
        TraceEvent(id="e03", stage="write", role="writer", round=2),
        TraceEvent(id="e04", stage="edit", role="editor", round=2, meta={"ready": True, "notes": ""}),
        TraceEvent(id="e05", stage="compile", role="compile", warnings=["beat 2: bad pause value 'x'"]),
        TraceEvent(id="e06", stage="tone", role="tone-specialist",
                   warnings=["segment 1: unknown tone 'brooding' -> fell back to 'measured'"]),
    ]
    return ir, plan, events


def test_build_lineage_joins_ir_plan_and_trace():
    ir, plan, events = _fixture()
    lin = build_lineage(ir, plan, events)

    assert lin.episode == 6 and lin.voice == "narrator" and lin.seed == 7
    assert lin.num_write_rounds == 2 and lin.final_round == 2
    assert lin.editor_approved is True
    assert lin.editor_notes == ["r1: tighten open"]  # empty r2 note is dropped
    assert lin.compile_warnings == ["beat 2: bad pause value 'x'"]

    s0, s1 = lin.segments
    assert s0.tone == "somber" and s0.tone_fallback is False
    assert s0.cfg_weight == 0.35  # params matched by segment id
    assert s1.tone == "brooding" and s1.tone_fallback is True
    assert "brooding" in s1.fallback_detail


def test_lineage_beat_filter_and_missing_params():
    ir, plan, _ = _fixture()
    lin = build_lineage(ir, plan, events=[])  # no trace -> no fallbacks, no rounds
    assert lin.final_round is None and lin.editor_approved is None
    assert all(s.tone_fallback is False for s in lin.segments)
    assert [s.segment_id for s in lin.beat(1)] == [1]
