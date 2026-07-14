"""HTML views for the authoring dashboard (standard-library only).

Views are functions of the filesystem (and the in-memory job registry). Read-only
pages reuse the project's existing self-contained renderers (``plan_view`` /
``trace_view``) verbatim — one rendering core, served two ways. Action endpoints
(compile/lint/diagnose/edit) run fast, deterministic CLI steps inline via
``jobs.run_sync``; the long ``plan``/``write`` steps go through the serialized job
registry and stream into a self-refreshing panel.
"""

from __future__ import annotations

import html
import sys
from pathlib import Path

import yaml

from prosodia.author.web.jobs import JobRegistry, run_sync

_CSS = """
:root{--bg:#f6f7f9;--card:#fff;--ink:#182029;--muted:#5c6672;--line:#e2e6ec;
  --accent:#0f7c8c;--accent-ink:#0b5c68;--ok:#2f855a;--off:#96a0ac;--warn:#b57314;--err:#c0392b;
  --mono:ui-monospace,SFMono-Regular,Consolas,monospace;
  --sans:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;}
@media(prefers-color-scheme:dark){:root{--bg:#0e131b;--card:#161d27;--ink:#e8edf3;
  --muted:#9aa6b4;--line:#26313f;--accent:#3fb8c7;--accent-ink:#7ad3de;--ok:#48b07a;
  --off:#5a6674;--warn:#d69233;--err:#e0685a;}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--sans);line-height:1.55}
header{position:sticky;top:0;display:flex;align-items:center;gap:16px;padding:12px 22px;
  background:var(--card);border-bottom:1px solid var(--line);z-index:5}
header .k{font-family:var(--mono);font-size:12px;letter-spacing:.12em;text-transform:uppercase;
  color:var(--accent);font-weight:700}
header a{color:var(--accent);text-decoration:none;font-size:14px}
main{max-width:960px;margin:0 auto;padding:26px 22px 90px}
h1{font-size:26px;margin:.2em 0 .3em}
h2{font-size:18px;margin:26px 0 10px;padding-top:14px;border-top:1px solid var(--line)}
a{color:var(--accent)}
.muted{color:var(--muted)}
.meta{font-family:var(--mono);font-size:13px;color:var(--muted)}
.desc{color:var(--muted);max-width:70ch}
code{font-family:var(--mono);background:var(--card);border:1px solid var(--line);
  border-radius:5px;padding:.06em .36em;font-size:.86em}
ul.projects{list-style:none;padding:0}
ul.projects li{padding:11px 2px;border-bottom:1px solid var(--line)}
.twrap{overflow-x:auto;border:1px solid var(--line);border-radius:10px}
table{border-collapse:collapse;width:100%;background:var(--card);font-size:14px;min-width:640px}
th,td{text-align:left;padding:9px 12px;border-bottom:1px solid var(--line);vertical-align:top}
th{background:var(--bg);font-size:11px;text-transform:uppercase;letter-spacing:.04em;color:var(--muted)}
tr:last-child td{border-bottom:0}
.badge{display:inline-block;font-family:var(--mono);font-size:11px;padding:2px 7px;
  border-radius:6px;margin-right:5px}
.badge.on{background:color-mix(in srgb,var(--ok) 20%,transparent);color:var(--ok)}
.badge.off{color:var(--off);border:1px solid var(--line)}
.badge.running{background:color-mix(in srgb,var(--warn) 20%,transparent);color:var(--warn)}
.badge.queued{color:var(--muted);border:1px solid var(--line)}
.badge.done{background:color-mix(in srgb,var(--ok) 20%,transparent);color:var(--ok)}
.badge.failed{background:color-mix(in srgb,var(--err) 20%,transparent);color:var(--err)}
.actions{display:flex;flex-wrap:wrap;gap:8px;margin:14px 0}
.btn{font:inherit;font-size:13px;cursor:pointer;color:var(--accent-ink);background:var(--card);
  border:1px solid var(--line);border-radius:7px;padding:5px 11px}
.btn:hover{border-color:var(--accent)}
.btn.sm{font-size:12px;padding:3px 8px}
.panel{margin-top:20px}
.job{background:var(--card);border:1px solid var(--line);border-radius:11px;padding:14px 16px;margin-top:14px}
.jobhead{display:flex;align-items:center;gap:10px;flex-wrap:wrap;font-size:14px}
.joblog{background:var(--bg);border:1px solid var(--line);border-radius:8px;padding:10px 12px;
  max-height:320px;overflow:auto;font-family:var(--mono);font-size:12.5px;white-space:pre-wrap;margin:10px 0 0}
.banner{border-radius:9px;padding:11px 14px;margin:14px 0;font-size:14px}
.banner.ok{background:color-mix(in srgb,var(--ok) 14%,transparent);border:1px solid var(--ok)}
.banner.err{background:color-mix(in srgb,var(--err) 12%,transparent);border:1px solid var(--err)}
.field{margin:12px 0}
.field label{display:block;font-size:13px;color:var(--muted);margin-bottom:4px}
input[type=text],input[type=number]{font:inherit;padding:7px 10px;border:1px solid var(--line);
  border-radius:7px;background:var(--card);color:var(--ink);width:min(520px,100%)}
textarea.editor{width:100%;min-height:60vh;font-family:var(--mono);font-size:13px;line-height:1.5;
  padding:12px;border:1px solid var(--line);border-radius:9px;background:var(--card);color:var(--ink)}
.err{color:var(--err);font-family:var(--mono);white-space:pre-wrap}
.empty{color:var(--muted)}
.rowacts{white-space:nowrap}
.rowacts .btn,.rowacts a{margin-right:6px}
"""


# ── helpers ──────────────────────────────────────────────────────────────────

def _esc(s) -> str:
    # quote=True escapes " and ' too — required because _esc output is interpolated
    # into double-quoted HTML attributes (data-post, href, …), not just text nodes.
    return html.escape("" if s is None else str(s), quote=True)


def _layout(title: str, body: str, *, back: bool = True) -> str:
    nav = '<a href="/">&larr; projects</a>' if back else ""
    return (
        '<!doctype html><html lang="en"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        f"<title>{_esc(title)}</title><style>{_CSS}</style></head><body>"
        f'<header><div class="k">Prosodia &middot; authoring</div>{nav}</header>'
        f"<main>{body}</main><script src=\"/assets/app.js\"></script></body></html>"
    )


def _load_series(proj: Path) -> dict:
    f = proj / "series.yaml"
    if not f.is_file():
        return {}
    try:
        data = yaml.safe_load(f.read_text(encoding="utf-8"))
    except Exception:
        return {}
    return data if isinstance(data, dict) else {}


def _episodes(cfg: dict) -> list[dict]:
    return cfg.get("episodes") or []


def _slug_for(ep: dict) -> str:
    return ep.get("slug") or f"ep{ep.get('n')}"


def _find_episode(cfg: dict, slug: str) -> dict | None:
    for ep in _episodes(cfg):
        if _slug_for(ep) == slug:
            return ep
    return None


def _python_cli(*args: str) -> list[str]:
    return [sys.executable, "-m", "prosodia.author.cli", *args]


def discover_projects(root: Path) -> list[Path]:
    if not root.is_dir():
        return []
    return sorted((p for p in root.iterdir() if (p / "series.yaml").is_file()), key=lambda p: p.name)


def _episode_status(proj: Path, ep: dict) -> dict:
    slug = _slug_for(ep)
    d = proj / "episodes" / slug
    return {
        "slug": slug,
        "drafted": (d / "transcript.md").is_file(),
        "compiled": (d / "ir.json").is_file(),
        "traced": (d / "run" / "run.json").is_file(),
    }


def _trace_body(root: Path, name: str, slug: str) -> str | None:
    run_dir = root / name / "episodes" / slug / "run"
    idx = run_dir / "run.json"
    if not idx.is_file():
        return None
    from prosodia.author.trace_view import render_trace_fragment
    from prosodia.core.lineage import Lineage
    from prosodia.core.trace import RunIndex

    try:
        index = RunIndex.model_validate_json(idx.read_text(encoding="utf-8"))
        lin = run_dir / "lineage.json"
        lineage = Lineage.from_json(lin.read_text(encoding="utf-8")) if lin.is_file() else None
    except Exception:
        return None  # transient partial read during a non-atomic rewrite — retry next poll
    return render_trace_fragment(index, lineage)


# ── read-only pages ──────────────────────────────────────────────────────────

def render_index(root: Path) -> str:
    projs = discover_projects(root)
    if not projs:
        body = (
            f'<h1>Projects</h1><p class="empty">No projects with a <code>series.yaml</code> '
            f"under <code>{_esc(root)}</code>.</p>"
        )
        return _layout("Projects", body, back=False)
    rows = []
    for p in projs:
        cfg = _load_series(p)
        eps = _episodes(cfg)
        title = cfg.get("series") or p.name
        persona = cfg.get("persona", "hardcore-history")
        rows.append(
            f'<li><a href="/p/{_esc(p.name)}"><b>{_esc(title)}</b></a>'
            f'<div class="muted">{_esc(p.name)} &middot; {len(eps)} episodes '
            f"&middot; persona {_esc(persona)}</div></li>"
        )
    body = f'<h1>Projects</h1><ul class="projects">{"".join(rows)}</ul>'
    return _layout("Projects", body, back=False)


def render_project(root: Path, name: str) -> str | None:
    proj = root / name
    if not (proj / "series.yaml").is_file():
        return None
    cfg = _load_series(proj)
    title = cfg.get("series") or name

    meta = [
        ("persona", cfg.get("persona", "hardcore-history")),
        ("engine", cfg.get("engine", "")),
        ("voice", cfg.get("voice", "")),
        ("target_minutes", cfg.get("target_minutes", "")),
    ]
    meta_html = " &middot; ".join(
        f'<span class="muted">{_esc(k)}:</span> {_esc(v)}' for k, v in meta if v not in ("", None)
    )
    parts = [f"<h1>{_esc(title)}</h1>", f'<p class="meta">{meta_html}</p>']
    if cfg.get("description"):
        parts.append(f'<p class="desc">{_esc(" ".join(str(cfg["description"]).split()))}</p>')

    outline_link = (
        f'<a class="btn" href="/p/{_esc(name)}/outline">View outline</a>'
        if (proj / "plan" / "outline.md").is_file()
        else ""
    )
    parts.append(
        '<div class="actions">'
        f'<button class="btn" data-post="/p/{_esc(name)}/plan" data-target="#panel">Run planner</button>'
        f'<button class="btn" data-get="/p/{_esc(name)}/lint" data-target="#panel">Repetition lint</button>'
        f"{outline_link}</div>"
    )

    eps = _episodes(cfg)
    if eps:
        parts.append(
            '<h2>Episodes</h2><div class="twrap"><table><thead><tr>'
            "<th>#</th><th>title</th><th>status</th><th>actions</th></tr></thead><tbody>"
        )
        for ep in eps:
            st = _episode_status(proj, ep)
            slug = st["slug"]
            badges = "".join(
                f'<span class="badge {"on" if on else "off"}">{label}</span>'
                for label, on in (
                    ("drafted", st["drafted"]),
                    ("compiled", st["compiled"]),
                    ("traced", st["traced"]),
                )
            )
            acts = [
                f'<button class="btn sm" data-post="/p/{_esc(name)}/ep/{_esc(slug)}/write" '
                'data-target="#panel">write</button>',
                f'<button class="btn sm" data-post="/p/{_esc(name)}/ep/{_esc(slug)}/compile" '
                'data-target="#panel">compile</button>',
                f'<a class="btn sm" href="/p/{_esc(name)}/ep/{_esc(slug)}/edit">edit</a>',
                f'<a class="btn sm" href="/p/{_esc(name)}/ep/{_esc(slug)}/diagnose">diagnose</a>',
                f'<a class="btn sm" href="/p/{_esc(name)}/ep/{_esc(slug)}/submit">submit</a>',
            ]
            if st["traced"]:
                acts.append(f'<a class="btn sm" href="/p/{_esc(name)}/ep/{_esc(slug)}/trace">trace</a>')
            parts.append(
                f"<tr><td>{_esc(ep.get('n'))}</td>"
                f"<td>{_esc(ep.get('title') or slug)}</td>"
                f"<td>{badges}</td>"
                f'<td class="rowacts">{"".join(acts)}</td></tr>'
            )
        parts.append("</tbody></table></div>")
    else:
        parts.append('<p class="muted">No episodes defined in <code>series.yaml</code>.</p>')

    try:
        from prosodia.author.persona import Persona

        names = Persona.available(proj)
        if names:
            items = []
            for pn in names:
                try:
                    desc = " ".join(Persona.resolve(pn, project=proj).description.split())
                except Exception:
                    desc = ""
                items.append(f'<li><b>{_esc(pn)}</b> <span class="muted">{_esc(desc[:100])}</span></li>')
            parts.append(f"<h2>Personas available</h2><ul>{''.join(items)}</ul>")
    except Exception:
        pass

    parts.append('<div id="panel" class="panel"></div>')
    return _layout(title, "\n".join(parts))


def render_outline(root: Path, name: str) -> str | None:
    f = root / name / "plan" / "outline.md"
    if not f.is_file():
        return None
    from prosodia.author.plan_view import render_page

    return render_page(f.read_text(encoding="utf-8"), title=f"{name} · plan")


def render_trace(root: Path, name: str, slug: str) -> str | None:
    """The interactive trace page: artifact drill-down, segment→round links, and
    re-run buttons. Rendered with the trace viewer's own styling plus the UI's JS."""
    proj = root / name
    run_dir = proj / "episodes" / slug / "run"
    idx = run_dir / "run.json"
    if not idx.is_file():
        return None
    from urllib.parse import quote

    from prosodia.author.trace_view import _CSS as TRACE_CSS
    from prosodia.author.trace_view import TraceLinks, render_trace_fragment
    from prosodia.core.lineage import Lineage
    from prosodia.core.trace import RunIndex

    try:
        index = RunIndex.model_validate_json(idx.read_text(encoding="utf-8"))
        lin = run_dir / "lineage.json"
        lineage = Lineage.from_json(lin.read_text(encoding="utf-8")) if lin.is_file() else None
    except Exception:
        return None

    base = f"/p/{quote(name)}/ep/{quote(slug)}"
    # "the round that produced it" = the last write stage's transcript artifact.
    final_write_rel = None
    for ev in index.events:
        if ev.stage == "write":
            for a in ev.outputs:
                if a.rel.endswith(".md"):
                    final_write_rel = a.rel

    def rerun_url(stage: str) -> str | None:
        if stage == "write":
            return f"{base}/write"
        if stage in ("compile", "tone"):
            return f"{base}/compile"
        return None

    links = TraceLinks(
        artifact_url=lambda rel: f"{base}/artifact?rel={quote(rel)}",
        rerun_url=rerun_url,
        segment_url=(
            (lambda _sid: f"{base}/artifact?rel={quote(final_write_rel)}") if final_write_rel else None
        ),
    )
    body = render_trace_fragment(index, lineage, links=links)
    title = index.title or (f"Episode {index.episode}" if index.episode is not None else "Run")
    return (
        '<!doctype html><html lang="en"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        f"<title>Trace · {_esc(title)}</title><style>{TRACE_CSS}</style></head><body>"
        '<div class="doc"><div class="eyebrow">Prosodia &middot; trace &middot; '
        f'<a href="/p/{_esc(name)}">&larr; {_esc(name)}</a></div>{body}</div>'
        '<script src="/assets/app.js"></script></body></html>'
    )


def render_trace_fragment(root: Path, name: str, slug: str) -> str:
    """The (non-interactive) trace body — used for the live poll embed in a job panel."""
    body = _trace_body(root, name, slug)
    return body if body is not None else '<p class="muted">Waiting for the trace to appear…</p>'


def render_artifact(root: Path, name: str, slug: str, rel: str) -> str:
    """Lazy-load a single run artifact's content into the trace inspector pane.
    Guards against path traversal — ``rel`` must resolve inside the episode's run/."""
    proj = root / name
    if not (proj / "series.yaml").is_file() or _find_episode(_load_series(proj), slug) is None:
        return '<div class="art"><p class="muted">unknown episode</p></div>'
    run_dir = (proj / "episodes" / slug / "run").resolve()
    if not run_dir.is_dir():
        return '<div class="art"><p class="muted">no trace yet</p></div>'
    try:
        target = (run_dir / rel).resolve()
        target.relative_to(run_dir)
    except (ValueError, OSError):
        return '<div class="art"><p class="err">invalid artifact path</p></div>'
    if not target.is_file():
        return f'<div class="art"><p class="muted">not found: {_esc(rel)}</p></div>'
    try:
        text = target.read_text(encoding="utf-8", errors="replace")
    except Exception as exc:  # noqa: BLE001
        return f'<div class="art"><p class="err">could not read: {_esc(exc)}</p></div>'
    if len(text) > 40000:
        text = text[:40000] + "\n… (truncated)"
    return f'<div class="art"><h3>{_esc(rel)}</h3><pre>{_esc(text)}</pre></div>'


# ── jobs (plan / write) ──────────────────────────────────────────────────────

def render_job_panel(registry: JobRegistry, root: Path, jid: str) -> str:
    job = registry.get(jid)
    if job is None:
        return f'<div class="job"><p class="err">no such job: {_esc(jid)}</p></div>'
    running = not job.done
    poll = (
        f' data-get="/jobs/{_esc(jid)}/fragment" data-poll="1500" data-swap="outer" data-target="self"'
        if running
        else ""
    )
    rc = "" if job.returncode is None else f" &middot; exit {job.returncode}"
    head = (
        f'<div class="jobhead"><span class="badge {_esc(job.status)}">{_esc(job.status)}</span>'
        f"<b>{_esc(job.label)}</b><span class=\"muted\">{_esc(jid)}{rc}</span></div>"
    )
    inner = [head, f'<pre class="joblog">{_esc(job.tail() or "(waiting…)")}</pre>']

    if job.done:
        name = job.meta.get("project")
        slug = job.meta.get("slug")
        links = []
        if name and job.kind == "plan":
            links.append(f'<a class="btn sm" href="/p/{_esc(name)}/outline">view outline</a>')
        if name and slug and job.kind == "write":
            links.append(f'<a class="btn sm" href="/p/{_esc(name)}/ep/{_esc(slug)}/edit">edit</a>')
            if (root / name / "episodes" / slug / "run" / "run.json").is_file():
                links.append(f'<a class="btn sm" href="/p/{_esc(name)}/ep/{_esc(slug)}/trace">trace</a>')
        links.append(f'<a class="btn sm" href="/p/{_esc(name)}">back to project</a>' if name else "")
        if links:
            inner.append('<div class="actions">' + "".join(links) + "</div>")
    elif job.kind == "write":
        name, slug = job.meta.get("project"), job.meta.get("slug")
        if name and slug:
            body = _trace_body(root, name, slug)
            if body:
                inner.append('<h2>Live trace</h2>' + body)

    return f'<div class="job"{poll}>' + "".join(inner) + "</div>"


def render_job_page(registry: JobRegistry, root: Path, jid: str) -> str:
    return _layout(f"Job {jid}", f'<h1>Job {_esc(jid)}</h1>{render_job_panel(registry, root, jid)}')


def action_plan(registry: JobRegistry, root: Path, name: str) -> str:
    proj = root / name
    if not (proj / "series.yaml").is_file():
        return '<div class="job"><p class="err">no such project</p></div>'
    job = registry.submit("plan", f"plan {name}", _python_cli("plan", "--project", str(proj)),
                          meta={"project": name})
    return render_job_panel(registry, root, job.id)


def action_write(registry: JobRegistry, root: Path, name: str, slug: str) -> str:
    proj = root / name
    cfg = _load_series(proj)
    ep = _find_episode(cfg, slug)
    if ep is None:
        return f'<div class="job"><p class="err">episode {_esc(slug)} not in series.yaml</p></div>'
    argv = _python_cli("write", "--project", str(proj), "--episode", str(ep.get("n")))
    job = registry.submit("write", f"write {slug}", argv, meta={"project": name, "slug": slug})
    return render_job_panel(registry, root, job.id)


# ── fast inline actions (compile / lint) ─────────────────────────────────────

def action_compile(root: Path, name: str, slug: str) -> str:
    proj = root / name
    transcript = proj / "episodes" / slug / "transcript.md"
    if not transcript.is_file():
        return f'<div class="banner err">No transcript at <code>{_esc(transcript)}</code> — write it first.</div>'
    rc, out = run_sync(_python_cli("compile", str(transcript), "--config", str(proj / "series.yaml")))
    cls = "ok" if rc == 0 else "err"
    links = ""
    if rc == 0:
        links = (
            f'<div class="actions"><a class="btn sm" href="/p/{_esc(name)}/ep/{_esc(slug)}/trace">trace</a>'
            f'<a class="btn sm" href="/p/{_esc(name)}/ep/{_esc(slug)}/edit">edit</a></div>'
        )
    return (
        f'<div class="banner {cls}"><b>compile {slug}</b> — exit {rc}</div>'
        f'<pre class="joblog">{_esc(out.strip() or "(no output)")}</pre>{links}'
    )


def action_lint(root: Path, name: str) -> str:
    proj = root / name
    rc, out = run_sync(_python_cli("lint-repetition", "--project", str(proj)))
    return (
        f'<h2>Repetition lint — {_esc(name)}</h2>'
        f'<pre class="joblog">{_esc(out.strip() or "(no output)")}</pre>'
    )


# ── editing (Phase 3) ────────────────────────────────────────────────────────

def render_editor(root: Path, name: str, slug: str, *, banner: str = "") -> str | None:
    proj = root / name
    if not (proj / "series.yaml").is_file() or _find_episode(_load_series(proj), slug) is None:
        return None
    transcript = proj / "episodes" / slug / "transcript.md"
    content = transcript.read_text(encoding="utf-8") if transcript.is_file() else ""
    body = (
        f"<h1>Edit &middot; {_esc(name)} / {_esc(slug)}</h1>"
        f'<p class="meta"><a href="/p/{_esc(name)}">&larr; back to project</a></p>'
        f"{banner}"
        f'<form method="post" action="/p/{_esc(name)}/ep/{_esc(slug)}/edit">'
        f'<textarea class="editor" name="content" spellcheck="false">{_esc(content)}</textarea>'
        '<div class="actions"><button class="btn" type="submit">Save &amp; recompile</button></div>'
        "</form>"
    )
    return _layout(f"Edit {slug}", body)


def action_edit_save(root: Path, name: str, slug: str, content: str) -> str | None:
    proj = root / name
    d = proj / "episodes" / slug
    if not (proj / "series.yaml").is_file() or _find_episode(_load_series(proj), slug) is None:
        return None
    d.mkdir(parents=True, exist_ok=True)
    transcript = d / "transcript.md"
    # normalize CRLF the browser may send; keep a trailing newline
    text = content.replace("\r\n", "\n")
    transcript.write_text(text if text.endswith("\n") else text + "\n", encoding="utf-8")
    rc, out = run_sync(_python_cli("compile", str(transcript), "--config", str(proj / "series.yaml")))
    cls = "ok" if rc == 0 else "err"
    verb = "compiled" if rc == 0 else "compile FAILED"
    banner = (
        f'<div class="banner {cls}"><b>Saved.</b> {verb} (exit {rc}).'
        f'<pre class="joblog">{_esc(out.strip() or "(no output)")}</pre></div>'
    )
    return render_editor(root, name, slug, banner=banner)


# ── diagnosis (Phase 4) ──────────────────────────────────────────────────────

def render_diagnose_form(root: Path, name: str, slug: str, *, note: str = "") -> str | None:
    proj = root / name
    if not (proj / "series.yaml").is_file() or _find_episode(_load_series(proj), slug) is None:
        return None
    d = proj / "episodes" / slug
    compiled = (d / "ir.json").is_file() and (d / "render_plan.json").is_file()
    warn = "" if compiled else (
        '<div class="banner err">This episode isn\'t compiled yet — run <code>compile</code> '
        "first so there's an IR + trace to diagnose against.</div>"
    )
    body = (
        f"<h1>Diagnose &middot; {_esc(name)} / {_esc(slug)}</h1>"
        f'<p class="meta"><a href="/p/{_esc(name)}">&larr; back to project</a></p>'
        f"{note}{warn}"
        f'<form method="post" action="/p/{_esc(name)}/ep/{_esc(slug)}/diagnose">'
        '<div class="field"><label>What feels wrong? (plain words)</label>'
        '<input type="text" name="complaint" placeholder="the opening feels flat" required></div>'
        '<div class="field"><label>Focus on a beat index (optional)</label>'
        '<input type="number" name="beat" min="0"></div>'
        '<div class="actions"><button class="btn" type="submit">Diagnose</button></div>'
        "</form>"
        '<p class="muted">Runs the deterministic signal pass (no model call). For the '
        "agent-refined version, use <code>prosodia diagnose</code> on the CLI.</p>"
    )
    return _layout(f"Diagnose {slug}", body)


def action_diagnose(root: Path, name: str, slug: str, complaint: str, beat: int | None) -> str | None:
    proj = root / name
    d = proj / "episodes" / slug
    if not (proj / "series.yaml").is_file() or _find_episode(_load_series(proj), slug) is None:
        return None
    if not ((d / "ir.json").is_file() and (d / "render_plan.json").is_file()):
        return render_diagnose_form(
            root, name, slug,
            note='<div class="banner err">Compile the episode first.</div>',
        )
    if not complaint.strip():
        return render_diagnose_form(
            root, name, slug, note='<div class="banner err">Describe the problem first.</div>'
        )
    from datetime import datetime, timezone

    from prosodia.author.trace_view import render_diagnosis_html
    from prosodia.core.diagnosis import build_diagnosis
    from prosodia.core.ir import EpisodeIR, RenderPlan
    from prosodia.core.lineage import Lineage, build_lineage
    from prosodia.core.trace import Run

    ir = EpisodeIR.from_json((d / "ir.json").read_text(encoding="utf-8"))
    plan = RenderPlan.from_json((d / "render_plan.json").read_text(encoding="utf-8"))
    run = Run(d / "run")
    events = run.events()
    lin_path = run.dir / "lineage.json"
    lineage = (
        Lineage.from_json(lin_path.read_text(encoding="utf-8"))
        if lin_path.is_file()
        else build_lineage(ir, plan, events)
    )
    diag = build_diagnosis(
        complaint, lineage, events,
        episode=ir.episode, beat=beat, diag_id="diag-web",
        created=datetime.now(timezone.utc).isoformat(),
    )
    return render_diagnosis_html(diag)


# ── submit a render job (Phase 4) ────────────────────────────────────────────

def render_submit_form(root: Path, name: str, slug: str, *, note: str = "") -> str | None:
    proj = root / name
    if not (proj / "series.yaml").is_file() or _find_episode(_load_series(proj), slug) is None:
        return None
    d = proj / "episodes" / slug
    compiled = (d / "ir.json").is_file() and (d / "render_plan.json").is_file()
    warn = "" if compiled else '<div class="banner err">Compile the episode first.</div>'
    body = (
        f"<h1>Submit render job &middot; {_esc(name)} / {_esc(slug)}</h1>"
        f'<p class="meta"><a href="/p/{_esc(name)}">&larr; back to project</a></p>'
        f"{note}{warn}"
        f'<form method="post" action="/p/{_esc(name)}/ep/{_esc(slug)}/submit">'
        '<div class="field"><label>Synced exchange root (the folder holding inbox/)</label>'
        '<input type="text" name="root" placeholder="/path/to/synced/folder" required></div>'
        '<div class="actions"><button class="btn" type="submit">Package &amp; publish</button></div>'
        "</form>"
        '<p class="muted">Bundles the compiled IR + render plan (and the matching voice clip) '
        "into the synced folder for the GPU box to render.</p>"
    )
    return _layout(f"Submit {slug}", body)


def action_submit(root: Path, name: str, slug: str, exchange_root: str) -> str | None:
    proj = root / name
    d = proj / "episodes" / slug
    if not (proj / "series.yaml").is_file() or _find_episode(_load_series(proj), slug) is None:
        return None
    if not ((d / "ir.json").is_file() and (d / "render_plan.json").is_file()):
        return render_submit_form(root, name, slug, note='<div class="banner err">Compile first.</div>')
    if not exchange_root.strip():
        return render_submit_form(
            root, name, slug, note='<div class="banner err">Enter an exchange root.</div>'
        )
    rc, out = run_sync(_python_cli("submit", str(d), "--root", exchange_root.strip()))
    cls = "ok" if rc == 0 else "err"
    body = (
        f"<h1>Submit render job &middot; {_esc(name)} / {_esc(slug)}</h1>"
        f'<p class="meta"><a href="/p/{_esc(name)}">&larr; back to project</a></p>'
        f'<div class="banner {cls}"><b>submit</b> — exit {rc}</div>'
        f'<pre class="joblog">{_esc(out.strip() or "(no output)")}</pre>'
    )
    return _layout(f"Submit {slug}", body)


# ── errors ───────────────────────────────────────────────────────────────────

def not_found(path: str) -> str:
    return _layout(
        "Not found", f'<h1>404</h1><p class="muted">No route for <code>{_esc(path)}</code>.</p>'
    )


def error_page(exc: Exception) -> str:
    return _layout("Error", f'<h1>Something went wrong</h1><pre class="err">{_esc(exc)}</pre>')
