from prosodia.author.trace_view import render_diagnosis_html, render_trace_html
from prosodia.core.diagnosis import build_diagnosis
from prosodia.core.lineage import Lineage, SegmentLineage
from prosodia.core.trace import Artifact, RunIndex, TraceEvent


def test_render_diagnosis_html_shows_cause_and_fix():
    lin = Lineage(
        episode=6, editor_approved=True,
        segments=[SegmentLineage(
            segment_id=1, beat_index=1, beat_title="B", tone="brooding", tone_fallback=True,
            cfg_weight=0.5, fallback_detail="segment 1: unknown tone 'brooding' -> fell back to 'measured'")],
    )
    diag = build_diagnosis("the opening feels flat", lin, events=[], episode=6, beat=1)
    html = render_diagnosis_html(diag)
    assert html.startswith("<!doctype html>") and html.rstrip().endswith("</html>")
    assert "the opening feels flat" in html
    assert "Most likely" in html
    assert "voice_profiles.yaml" in html
    assert "brooding" in html


def test_render_trace_html_shows_stages_and_fallback():
    index = RunIndex(episode=6, title="The euro", status="warn", events=[
        TraceEvent(id="e01", stage="compile", role="compile",
                   outputs=[Artifact(rel="stages/compile/ir.json", sha256="a" * 64, size=10)]),
        TraceEvent(id="e02", stage="tone", role="tone-specialist", status="warn",
                   warnings=["segment 1: unknown tone 'brooding' -> fell back to 'measured'"]),
    ])
    lineage = Lineage(episode=6, segments=[
        SegmentLineage(segment_id=1, beat_index=1, beat_title="B", tone="brooding", rate="normal",
                       tone_fallback=True, spoken_preview="It might happen again."),
    ])
    html = render_trace_html(index, lineage)
    assert html.startswith("<!doctype html>") and html.rstrip().endswith("</html>")
    assert "The euro" in html
    assert "compile" in html and "tone" in html
    assert "brooding" in html and "⚠" in html
    assert "fell back" in html
