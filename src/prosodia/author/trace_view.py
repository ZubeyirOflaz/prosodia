"""Render the run trace and a diagnosis into self-contained HTML pages.

Two views, both pure standard-library (no torch, no markdown dep), so they stay
inside the authoring boundary and open with a double-click:

* :func:`render_trace_html` — the pipeline as a status-colored timeline, each
  stage's inputs/outputs/warnings, and the per-segment lineage table.
* :func:`render_diagnosis_html` — a reported problem, the most-likely source, and
  every candidate source across the process with its evidence and recommended fix.
"""

from __future__ import annotations

import html

from prosodia.core.diagnosis import Diagnosis
from prosodia.core.lineage import Lineage
from prosodia.core.trace import RunIndex

_CSS = """
:root{ --bg:#eef1f5; --card:#fff; --card2:#f6f8fa; --ink:#151d2a; --muted:#5a6472;
  --line:#dde3ea; --accent:#0f7c8c; --accent-ink:#0b5c68; --soft:#dcecef;
  --ok:#2f855a; --warn:#b57314; --err:#c0392b;
  --mono:ui-monospace,"SF Mono","Cascadia Code",Consolas,monospace;
  --sans:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif; }
@media (prefers-color-scheme:dark){ :root{ --bg:#0e131b; --card:#161d27; --card2:#131922;
  --ink:#e8edf3; --muted:#9aa6b4; --line:#26313f; --accent:#3fb8c7; --accent-ink:#7ad3de;
  --soft:rgba(63,184,199,.14); --ok:#48b07a; --warn:#d69233; --err:#e0685a; } }
*{box-sizing:border-box;}
body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--sans);line-height:1.55;}
.doc{max-width:920px;margin:0 auto;padding:36px 22px 80px;}
.eyebrow{font-family:var(--mono);font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:var(--accent-ink);}
h1{font-size:26px;line-height:1.15;margin:.3em 0 .2em;}
h2{font-size:18px;margin:30px 0 12px;padding-top:14px;border-top:1px solid var(--line);}
.meta{font-family:var(--mono);font-size:12.5px;color:var(--muted);}
.summary{background:var(--card);border:1px solid var(--line);border-left:3px solid var(--accent);
  border-radius:0 9px 9px 0;padding:12px 15px;margin:16px 0;}
.dot{display:inline-block;width:9px;height:9px;border-radius:50%;vertical-align:middle;margin-right:6px;}
.s-ok{background:var(--ok);} .s-warn{background:var(--warn);} .s-error{background:var(--err);}
code{font-family:var(--mono);background:var(--card2);border:1px solid var(--line);border-radius:5px;
  padding:.06em .36em;font-size:.86em;color:var(--accent-ink);}
.timeline{display:flex;gap:7px;overflow-x:auto;padding-bottom:8px;}
.node{flex:0 0 auto;border:1px solid var(--line);border-radius:9px;background:var(--card);padding:8px 11px;min-width:96px;}
.node .st{font-family:var(--mono);font-size:12px;font-weight:600;}
.node .rl{font-family:var(--mono);font-size:11px;color:var(--muted);}
.ev{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:12px 15px;margin:10px 0;}
.ev.warn{border-color:color-mix(in srgb,var(--warn) 45%,var(--line));}
.ev.error{border-color:color-mix(in srgb,var(--err) 55%,var(--line));}
.ev h3{margin:0 0 6px;font-size:14px;font-family:var(--mono);}
.arts{font-family:var(--mono);font-size:12px;color:var(--muted);margin:4px 0;}
.arts b{color:var(--ink);font-weight:600;}
.warnlist{margin:6px 0 0;padding-left:18px;color:var(--warn);font-size:13px;}
.twrap{overflow-x:auto;border:1px solid var(--line);border-radius:10px;}
table{border-collapse:collapse;width:100%;background:var(--card);font-size:13px;min-width:560px;}
th,td{text-align:left;padding:7px 10px;border-bottom:1px solid var(--line);font-variant-numeric:tabular-nums;}
th{background:var(--card2);font-size:11px;text-transform:uppercase;letter-spacing:.04em;color:var(--muted);}
tr.fb td{background:color-mix(in srgb,var(--warn) 12%,transparent);}
.cand{background:var(--card);border:1px solid var(--line);border-radius:11px;padding:14px 16px;margin:12px 0;}
.cand.top{border-color:var(--accent);box-shadow:0 0 0 1px var(--accent) inset;}
.chead{display:flex;align-items:center;gap:10px;flex-wrap:wrap;}
.stage-chip{font-family:var(--mono);font-size:12px;font-weight:600;background:var(--soft);color:var(--accent-ink);
  border-radius:6px;padding:3px 8px;}
.conf{font-family:var(--mono);font-size:12px;color:var(--muted);}
.bar{flex:1;min-width:80px;height:6px;background:var(--card2);border-radius:3px;overflow:hidden;}
.bar i{display:block;height:100%;background:var(--accent);}
.topflag{font-family:var(--mono);font-size:11px;color:var(--accent-ink);text-transform:uppercase;letter-spacing:.08em;}
.hyp{margin:9px 0;}
.fix{background:var(--card2);border-radius:8px;padding:9px 12px;margin-top:8px;font-size:14px;}
ul.ev-list{margin:6px 0 0;padding-left:18px;font-size:13px;color:var(--muted);}
"""


def _esc(s) -> str:
    return html.escape("" if s is None else str(s), quote=False)


def _pct(conf: float) -> int:
    return int(round(max(0.0, min(1.0, conf)) * 100))


def _page(title: str, body: str, kicker: str) -> str:
    return (
        '<!doctype html><html lang="en"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        f"<title>{_esc(title)}</title><style>{_CSS}</style></head><body>"
        f'<div class="doc"><div class="eyebrow">{_esc(kicker)}</div>{body}</div></body></html>'
    )


def render_diagnosis_html(diag: Diagnosis) -> str:
    beat = f"beat {diag.scope_beat}" if diag.scope_beat is not None else "whole episode"
    parts = [
        f"<h1>{_esc(diag.complaint)}</h1>",
        f'<div class="meta">episode {_esc(diag.scope_episode)} · {_esc(beat)} · '
        f"method: {_esc(diag.method)} · {_esc(diag.created)}</div>",
        f'<div class="summary">{_esc(diag.summary)}</div>',
        f"<h2>Candidate sources across the process ({len(diag.candidates)})</h2>",
    ]
    top_id = id(diag.most_likely) if diag.most_likely else None
    for i, c in enumerate(diag.candidates):
        is_top = (top_id is not None and id(c) == top_id) or (top_id is None and i == 0)
        pct = _pct(c.confidence)
        block = [f'<div class="cand{" top" if is_top else ""}">', '<div class="chead">']
        if is_top:
            block.append('<span class="topflag">Most likely</span>')
        block += [
            f'<span class="stage-chip">{_esc(c.stage)}</span>',
            f'<span class="conf">{pct}%</span>',
            f'<div class="bar"><i style="width:{pct}%"></i></div>',
            "</div>",
            f'<p class="hyp">{_esc(c.hypothesis)}</p>',
        ]
        if c.segment_ids:
            block.append(f'<div class="meta">segments: {_esc(", ".join(map(str, c.segment_ids)))}</div>')
        if c.evidence:
            block.append('<ul class="ev-list">' + "".join(f"<li>{_esc(e)}</li>" for e in c.evidence) + "</ul>")
        block.append(f'<div class="fix"><b>Fix:</b> {_esc(c.recommended_fix)}')
        if c.fix_command:
            block.append(f"<br><code>{_esc(c.fix_command)}</code>")
        block.append("</div></div>")
        parts.append("".join(block))
    return _page(f"Diagnosis · {diag.id}", "\n".join(parts), f"Prosodia · diagnosis · {diag.id}")


def render_trace_fragment(index: RunIndex, lineage: Lineage | None = None) -> str:
    """The trace body — timeline + stages + segments — WITHOUT page chrome.

    Shared rendering core: :func:`render_trace_html` composes this into a
    self-contained file, and the authoring UI serves the same markup as a live
    (poll-refreshed) fragment. One store, two readers.
    """
    title = index.title or (f"Episode {index.episode}" if index.episode is not None else "Run")
    parts = [
        f"<h1>{_esc(title)}</h1>",
        f'<div class="meta"><span class="dot s-{_esc(index.status)}"></span>'
        f"status: {_esc(index.status)} · {len(index.events)} events · updated {_esc(index.updated)}</div>",
        "<h2>Pipeline</h2>",
        '<div class="timeline">',
    ]
    for ev in index.events:
        rnd = f" r{ev.round}" if ev.round is not None else ""
        parts.append(
            f'<div class="node"><div class="st"><span class="dot s-{_esc(ev.status)}"></span>'
            f'{_esc(ev.stage)}{_esc(rnd)}</div><div class="rl">{_esc(ev.role)}</div></div>'
        )
    parts.append("</div>")

    parts.append("<h2>Stages</h2>")
    for ev in index.events:
        cls = "ev" + (f" {ev.status}" if ev.status in ("warn", "error") else "")
        rnd = f" · round {ev.round}" if ev.round is not None else ""
        block = [
            f'<div class="{cls}">',
            f'<h3><span class="dot s-{_esc(ev.status)}"></span>{_esc(ev.id)} · {_esc(ev.stage)} '
            f"({_esc(ev.role)}){_esc(rnd)}</h3>",
        ]
        for kind, arts in (("in", ev.inputs), ("out", ev.outputs)):
            for a in arts:
                block.append(f'<div class="arts">{kind} <b>{_esc(a.rel)}</b> · {_esc(a.sha256[:10])} · {a.size} B</div>')
        if ev.meta:
            meta = ", ".join(f"{k}={_esc(v)}" for k, v in ev.meta.items())
            block.append(f'<div class="arts">{meta}</div>')
        if ev.warnings:
            block.append('<ul class="warnlist">' + "".join(f"<li>{_esc(w)}</li>" for w in ev.warnings) + "</ul>")
        block.append("</div>")
        parts.append("".join(block))

    if lineage and lineage.segments:
        parts.append("<h2>Segments</h2>")
        parts.append('<div class="twrap"><table><thead><tr>'
                     "<th>seg</th><th>beat</th><th>tone / rate</th><th>exagg</th><th>cfg</th>"
                     "<th>pause ms</th><th>text</th></tr></thead><tbody>")
        for s in lineage.segments:
            row_cls = ' class="fb"' if s.tone_fallback else ""
            tone = _esc(s.tone) + (" ⚠" if s.tone_fallback else "")
            parts.append(
                f"<tr{row_cls}><td>{s.segment_id}</td><td>{s.beat_index} · {_esc(s.beat_title)}</td>"
                f"<td>{tone} / {_esc(s.rate)}</td><td>{_esc(s.exaggeration)}</td><td>{_esc(s.cfg_weight)}</td>"
                f"<td>{s.pause_before_ms}</td><td>{_esc(s.spoken_preview)}</td></tr>"
            )
        parts.append("</tbody></table></div>")

    return "\n".join(parts)


def render_trace_html(index: RunIndex, lineage: Lineage | None = None) -> str:
    title = index.title or (f"Episode {index.episode}" if index.episode is not None else "Run")
    ep = index.episode if index.episode is not None else ""
    return _page(
        f"Trace · {title}", render_trace_fragment(index, lineage), f"Prosodia · trace · ep{ep}"
    )
