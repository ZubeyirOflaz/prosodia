"""Render a plan (the Planner's Markdown outline) into a lightweight HTML review page.

The plan is the highest-value point for a quick human check — before any episode is
written or rendered. This turns the outline into a clean, self-contained HTML file
you open in a browser: driving question, coverage map, and per-episode cards laid
out for skimming. Pure standard-library (no torch, no markdown dependency) so it
stays inside the authoring boundary.
"""

from __future__ import annotations

import html
import re
from pathlib import Path

_HR = re.compile(r"^\s*([-*_])\1{2,}\s*$")
_HEADING = re.compile(r"^(#{1,6})\s+(.*)$")
_ULI = re.compile(r"^\s*[-*]\s+(.*)$")
_OLI = re.compile(r"^\s*\d+\.\s+(.*)$")
_QUOTE = re.compile(r"^\s*>\s?(.*)$")
_TABLE_SEP = re.compile(r"^\s*\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)+\|?\s*$")


def _inline(text: str) -> str:
    """Escape HTML, then apply a safe subset of inline Markdown."""
    out = html.escape(text, quote=False)
    out = re.sub(r"`([^`]+)`", r"<code>\1</code>", out)
    out = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", out)
    out = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", out)
    return out


def _split_row(line: str) -> list[str]:
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    return [c.strip() for c in line.split("|")]


def _render_body(md: str) -> str:
    lines = md.replace("\r\n", "\n").split("\n")
    out: list[str] = []
    i, n = 0, len(lines)
    para: list[str] = []

    def flush_para() -> None:
        if para:
            out.append("<p>" + _inline(" ".join(para).strip()) + "</p>")
            para.clear()

    while i < n:
        line = lines[i]

        # table: a header row followed by a |---| separator
        if "|" in line and i + 1 < n and _TABLE_SEP.match(lines[i + 1]):
            flush_para()
            header = _split_row(line)
            out.append('<div class="twrap"><table><thead><tr>'
                        + "".join(f"<th>{_inline(c)}</th>" for c in header)
                        + "</tr></thead><tbody>")
            i += 2
            while i < n and "|" in lines[i] and lines[i].strip():
                cells = _split_row(lines[i])
                out.append("<tr>" + "".join(f"<td>{_inline(c)}</td>" for c in cells) + "</tr>")
                i += 1
            out.append("</tbody></table></div>")
            continue

        if _HR.match(line):
            flush_para(); out.append("<hr>"); i += 1; continue

        m = _HEADING.match(line)
        if m:
            flush_para()
            level = len(m.group(1))
            out.append(f"<h{level}>{_inline(m.group(2))}</h{level}>")
            i += 1
            continue

        if _QUOTE.match(line):
            flush_para()
            buf = []
            while i < n and _QUOTE.match(lines[i]):
                buf.append(_QUOTE.match(lines[i]).group(1))
                i += 1
            out.append("<blockquote>" + _inline(" ".join(buf)) + "</blockquote>")
            continue

        if _ULI.match(line) or _OLI.match(line):
            flush_para()
            ordered = bool(_OLI.match(line))
            tag = "ol" if ordered else "ul"
            pat = _OLI if ordered else _ULI
            out.append(f"<{tag}>")
            while i < n and pat.match(lines[i]):
                out.append("<li>" + _inline(pat.match(lines[i]).group(1)) + "</li>")
                i += 1
            out.append(f"</{tag}>")
            continue

        if not line.strip():
            flush_para(); i += 1; continue

        para.append(line.strip())
        i += 1

    flush_para()
    return "\n".join(out)


_CSS = """
:root { --ink:#1a1a1a; --muted:#6b6b6b; --line:#e6e3dd; --accent:#7c4a2d; --bg:#faf8f5; --card:#fff; }
* { box-sizing: border-box; }
body { margin:0; background:var(--bg); color:var(--ink);
  font:16px/1.65 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif; }
header.top { position:sticky; top:0; background:rgba(250,248,245,.92); backdrop-filter:blur(6px);
  border-bottom:1px solid var(--line); padding:14px 24px; z-index:5; }
header.top .k { font-size:12px; letter-spacing:.14em; text-transform:uppercase; color:var(--accent); font-weight:700; }
header.top h1 { margin:2px 0 0; font-size:19px; font-weight:650; }
main { max-width:860px; margin:0 auto; padding:32px 24px 80px; }
h1,h2,h3,h4 { line-height:1.25; }
main > h2 { margin:34px 0 10px; padding-top:18px; border-top:1px solid var(--line); font-size:23px; }
main > h2:first-child { border-top:0; padding-top:0; }
h3 { font-size:18px; margin:22px 0 6px; color:#333; }
p,li { color:#242424; }
strong { color:#111; }
code { background:#efe9e1; padding:.08em .35em; border-radius:4px; font-size:.9em; }
hr { border:0; border-top:1px solid var(--line); margin:26px 0; }
blockquote { margin:14px 0; padding:10px 16px; background:var(--card); border-left:3px solid var(--accent);
  border-radius:0 8px 8px 0; color:#3a3a3a; }
ul,ol { padding-left:22px; }
li { margin:3px 0; }
.twrap { overflow-x:auto; margin:14px 0; }
table { border-collapse:collapse; width:100%; background:var(--card); border:1px solid var(--line); border-radius:8px; font-size:14.5px; }
th,td { text-align:left; padding:8px 12px; border-bottom:1px solid var(--line); vertical-align:top; }
th { background:#f1ece4; font-weight:650; }
tr:last-child td { border-bottom:0; }
"""


def render_page(md: str, title: str = "Plan review") -> str:
    body = _render_body(md)
    return (
        "<!doctype html><html lang=\"en\"><head><meta charset=\"utf-8\">"
        "<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">"
        f"<title>{html.escape(title)}</title><style>{_CSS}</style></head><body>"
        f'<header class="top"><div class="k">Prosodia · plan review</div>'
        f"<h1>{html.escape(title)}</h1></header><main>{body}</main></body></html>"
    )


def render_file(plan_path: str | Path, out_path: str | Path | None = None, title: str | None = None) -> Path:
    plan_path = Path(plan_path)
    md = plan_path.read_text(encoding="utf-8")
    if title is None:
        m = re.search(r"^#\s+(.*)$", md, re.M)
        title = m.group(1).strip() if m else plan_path.stem
    out = Path(out_path) if out_path else plan_path.with_suffix(".html")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render_page(md, title), encoding="utf-8")
    return out
