"""Authoring dashboard: job runner, views/actions (Phases 1–4), and live routing.

Deterministic and torch-free. ``plan``/``write`` are never invoked with a real
``claude`` — the job registry is exercised with harmless stub commands; the fast
steps (``compile``/``lint``/``diagnose``/edit) run for real (they're offline).
"""

from __future__ import annotations

import sys
import threading
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

from prosodia.author.web import views
from prosodia.author.web.jobs import JobRegistry, run_sync

TRANSCRIPT = (
    "---\nepisode: 1\ntitle: Intro\ndefaults: { tone: measured, rate: normal }\n---\n"
    "## Opening {tone: measured}\nHello, world. This is a short test sentence.\n"
)


def _mk_project(root: Path) -> Path:
    proj = root / "demo"
    (proj / "episodes" / "ep01-intro").mkdir(parents=True)
    (proj / "plan").mkdir(parents=True)
    (proj / "series.yaml").write_text(
        "series: Demo Series\npersona: thinkers\nengine: chatterbox\nvoice: narrator\n"
        "description: A demo series.\n"
        "episodes:\n  - n: 1\n    slug: ep01-intro\n    title: Intro\n",
        encoding="utf-8",
    )
    (proj / "episodes" / "ep01-intro" / "transcript.md").write_text(TRANSCRIPT, encoding="utf-8")
    (proj / "plan" / "outline.md").write_text(
        "# Demo Series\n\n## EP 1 — Intro\nScope.\n", encoding="utf-8"
    )
    return proj


def _mk_write_run(proj: Path, slug: str = "ep01-intro"):
    """Build a run/ with a write stage + a transcript artifact (no claude)."""
    from prosodia.core.trace import Run

    run = Run(proj / "episodes" / slug / "run")
    art = run.write_artifact(
        "stages/write.r1/transcript.v1.md", "## Opening\nDraft body text for the round.\n",
        label="draft r1",
    )
    run.event("write", "writer", round=1, outputs=[art], chars=40)
    run.write_index(episode=1, title="Intro")
    return run


# ── Phase 1: read-only views ─────────────────────────────────────────────────

def test_index_lists_projects(tmp_path):
    _mk_project(tmp_path)
    out = views.render_index(tmp_path)
    assert "Demo Series" in out and "/p/demo" in out


def test_index_empty(tmp_path):
    assert "No projects" in views.render_index(tmp_path)


def test_project_dashboard(tmp_path):
    _mk_project(tmp_path)
    out = views.render_project(tmp_path, "demo")
    assert out is not None
    assert "Intro" in out
    assert 'class="badge on">drafted' in out
    assert 'class="badge off">compiled' in out
    # action affordances present
    assert 'data-post="/p/demo/plan"' in out
    assert 'data-post="/p/demo/ep/ep01-intro/write"' in out
    assert 'data-post="/p/demo/ep/ep01-intro/compile"' in out
    assert '/p/demo/ep/ep01-intro/edit' in out
    assert 'id="panel"' in out


def test_project_missing_returns_none(tmp_path):
    assert views.render_project(tmp_path, "nope") is None


def test_outline_renders(tmp_path):
    _mk_project(tmp_path)
    out = views.render_outline(tmp_path, "demo")
    assert out is not None and "Demo Series" in out


def test_trace_none_without_run(tmp_path):
    _mk_project(tmp_path)
    assert views.render_trace(tmp_path, "demo", "ep01-intro") is None


def test_discover_and_status(tmp_path):
    proj = _mk_project(tmp_path)
    assert views.discover_projects(tmp_path) == [proj]
    st = views._episode_status(proj, {"n": 1, "slug": "ep01-intro"})
    assert st["drafted"] and not st["compiled"] and not st["traced"]


# ── job runner ───────────────────────────────────────────────────────────────

def test_run_sync_ok_and_fail():
    rc, out = run_sync([sys.executable, "-c", "print('hi-there')"])
    assert rc == 0 and "hi-there" in out
    rc, _ = run_sync([sys.executable, "-c", "import sys; sys.exit(3)"])
    assert rc == 3


def test_registry_runs_job():
    reg = JobRegistry()
    job = reg.submit("x", "echo", [sys.executable, "-c", "print('done-marker')"])
    reg.wait(job)
    assert job.status == "done" and job.returncode == 0 and "done-marker" in job.tail()


def test_registry_failed_job():
    reg = JobRegistry()
    job = reg.submit("x", "boom", [sys.executable, "-c", "import sys; sys.exit(2)"])
    reg.wait(job)
    assert job.status == "failed" and job.returncode == 2


def test_registry_launch_error():
    reg = JobRegistry()
    job = reg.submit("x", "nope", ["this-binary-does-not-exist-xyz"])
    reg.wait(job)
    assert job.status == "failed" and "failed to launch" in job.tail()


# ── jobs surfaced in the UI (plan/write) — no real claude ────────────────────

def _stub_cli(monkeypatch):
    monkeypatch.setattr(views, "_python_cli", lambda *a: [sys.executable, "-c", "print('stub-run')"])


def test_action_write_submits(tmp_path, monkeypatch):
    _mk_project(tmp_path)
    _stub_cli(monkeypatch)
    reg = JobRegistry()
    panel = views.action_write(reg, tmp_path, "demo", "ep01-intro")
    assert "write ep01-intro" in panel
    job = reg.recent()[0]
    reg.wait(job)
    assert job.kind == "write" and job.meta["slug"] == "ep01-intro" and job.status == "done"


def test_action_write_bad_slug(tmp_path):
    _mk_project(tmp_path)
    reg = JobRegistry()
    out = views.action_write(reg, tmp_path, "demo", "ep99-nope")
    assert "not in series.yaml" in out


def test_action_plan_submits(tmp_path, monkeypatch):
    _mk_project(tmp_path)
    _stub_cli(monkeypatch)
    reg = JobRegistry()
    panel = views.action_plan(reg, tmp_path, "demo")
    assert "plan demo" in panel
    reg.wait(reg.recent()[0])
    assert reg.recent()[0].status == "done"


def test_job_panel(tmp_path):
    reg = JobRegistry()
    job = reg.submit("write", "write x", [sys.executable, "-c", "print('ok')"],
                     meta={"project": "demo", "slug": "ep01-intro"})
    reg.wait(job)
    panel = views.render_job_panel(reg, tmp_path, job.id)
    assert job.id in panel and "done" in panel
    assert "no such job" in views.render_job_panel(reg, tmp_path, "job-nope")


# ── fast actions: compile / lint (real, offline) ─────────────────────────────

def test_action_compile(tmp_path):
    proj = _mk_project(tmp_path)
    out = views.action_compile(tmp_path, "demo", "ep01-intro")
    assert "exit 0" in out
    assert (proj / "episodes" / "ep01-intro" / "ir.json").is_file()
    assert (proj / "episodes" / "ep01-intro" / "run" / "run.json").is_file()


def test_action_compile_no_transcript(tmp_path):
    proj = _mk_project(tmp_path)
    (proj / "episodes" / "ep01-intro" / "transcript.md").unlink()
    out = views.action_compile(tmp_path, "demo", "ep01-intro")
    assert "write it first" in out


def test_action_lint(tmp_path):
    _mk_project(tmp_path)
    out = views.action_lint(tmp_path, "demo")
    assert "Repetition lint" in out


# ── editing (Phase 3) ─────────────────────────────────────────────────────────

def test_editor_renders(tmp_path):
    _mk_project(tmp_path)
    page = views.render_editor(tmp_path, "demo", "ep01-intro")
    assert page is not None and "textarea" in page and "Opening" in page


def test_edit_save_recompiles(tmp_path):
    proj = _mk_project(tmp_path)
    new = TRANSCRIPT + "\n## Second {tone: measured}\nAnother sentence entirely.\n"
    res = views.action_edit_save(tmp_path, "demo", "ep01-intro", new)
    assert res is not None and "Saved" in res
    assert "Second" in (proj / "episodes" / "ep01-intro" / "transcript.md").read_text(encoding="utf-8")
    assert (proj / "episodes" / "ep01-intro" / "ir.json").is_file()


# ── diagnosis (Phase 4) ───────────────────────────────────────────────────────

def test_diagnose_form_gate(tmp_path):
    _mk_project(tmp_path)
    before = views.render_diagnose_form(tmp_path, "demo", "ep01-intro")
    assert before is not None and "compile" in before.lower()
    views.action_compile(tmp_path, "demo", "ep01-intro")
    after = views.render_diagnose_form(tmp_path, "demo", "ep01-intro")
    assert "What feels wrong" in after


def test_action_diagnose(tmp_path):
    _mk_project(tmp_path)
    views.action_compile(tmp_path, "demo", "ep01-intro")
    out = views.action_diagnose(tmp_path, "demo", "ep01-intro", "the opening feels flat", None)
    assert out is not None and "flat" in out


# ── submit render job (Phase 4) ───────────────────────────────────────────────

def test_submit_form_gate(tmp_path):
    _mk_project(tmp_path)
    assert "Compile the episode first" in views.render_submit_form(tmp_path, "demo", "ep01-intro")
    views.action_compile(tmp_path, "demo", "ep01-intro")
    assert "exchange root" in views.render_submit_form(tmp_path, "demo", "ep01-intro").lower()


def test_action_submit(tmp_path):
    proj = _mk_project(tmp_path)
    (proj / "voices").mkdir()
    (proj / "voices" / "narrator.wav").write_bytes(b"RIFF0000WAVEfmt ")
    views.action_compile(tmp_path, "demo", "ep01-intro")
    exch = tmp_path / "exchange"
    exch.mkdir()
    out = views.action_submit(tmp_path, "demo", "ep01-intro", str(exch))
    assert out is not None and "exit 0" in out
    assert (exch / "inbox").exists()


def test_action_submit_unknown_slug(tmp_path):
    _mk_project(tmp_path)
    assert views.action_submit(tmp_path, "demo", "ep99-nope", "/tmp/x") is None


# ── deeper trace interaction ──────────────────────────────────────────────────

def test_trace_interactive(tmp_path):
    _mk_project(tmp_path)
    views.action_compile(tmp_path, "demo", "ep01-intro")   # writes lineage.json (segments)
    _mk_write_run(tmp_path / "demo")                        # adds a write stage + artifact
    page = views.render_trace(tmp_path, "demo", "ep01-intro")
    assert page is not None
    assert 'id="tracepane"' in page                          # inspector pane
    assert "/p/demo/ep/ep01-intro/artifact?rel=" in page     # artifact drill-down
    assert 'data-post="/p/demo/ep/ep01-intro/write"' in page  # re-run the write stage
    assert 'class="seglink"' in page                         # segment→producing-round link
    assert "/assets/app.js" in page


def test_render_artifact(tmp_path):
    proj = _mk_project(tmp_path)
    _mk_write_run(proj)
    out = views.render_artifact(tmp_path, "demo", "ep01-intro", "stages/write.r1/transcript.v1.md")
    assert "Draft body text" in out


def test_render_artifact_traversal_blocked(tmp_path):
    proj = _mk_project(tmp_path)
    _mk_write_run(proj)
    # ../../../series.yaml resolves to the REAL project series.yaml (which exists); the
    # guard must reject it. Without the guard this input would leak "Demo Series".
    out = views.render_artifact(tmp_path, "demo", "ep01-intro", "../../../series.yaml")
    assert "Demo Series" not in out and "series:" not in out
    assert "invalid" in out.lower()


def test_render_artifact_missing(tmp_path):
    proj = _mk_project(tmp_path)
    _mk_write_run(proj)
    out = views.render_artifact(tmp_path, "demo", "ep01-intro", "stages/nope.md")
    assert "not found" in out.lower()


def test_standalone_trace_not_interactive(tmp_path):
    proj = _mk_project(tmp_path)
    _mk_write_run(proj)
    from prosodia.author.trace_view import render_trace_html
    from prosodia.core.trace import RunIndex

    idx = RunIndex.model_validate_json(
        (proj / "episodes" / "ep01-intro" / "run" / "run.json").read_text(encoding="utf-8")
    )
    out = render_trace_html(idx)
    # no interactive elements (the .tracepane CSS class may appear; an element must not)
    assert 'data-get="' not in out and 'data-post="' not in out and 'id="tracepane"' not in out


# ── live server routing ───────────────────────────────────────────────────────

def _start_server(root: Path):
    from prosodia.author.web.server import _Server

    srv = _Server(("127.0.0.1", 0), root)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv, f"http://127.0.0.1:{srv.server_address[1]}"


def _req(url: str, method: str = "GET", body: bytes | None = None):
    req = urllib.request.Request(url, method=method, data=body)
    if body is not None:
        req.add_header("Content-Type", "application/x-www-form-urlencoded")
    try:
        r = urllib.request.urlopen(req, timeout=10)
        return r.status, r.read().decode("utf-8"), r.headers.get("Content-Type", "")
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8"), e.headers.get("Content-Type", "")


def test_server_end_to_end(tmp_path):
    _mk_project(tmp_path)
    srv, base = _start_server(tmp_path)
    try:
        assert _req(base + "/")[0] == 200
        code, _, ctype = _req(base + "/assets/app.js")
        assert code == 200 and "javascript" in ctype
        assert _req(base + "/p/demo")[0] == 200
        assert _req(base + "/p/demo/outline")[0] == 200
        # POST compile runs for real (offline) and reports success
        code, body, _ = _req(base + "/p/demo/ep/ep01-intro/compile", method="POST", body=b"")
        assert code == 200 and "exit 0" in body
        # trace now exists
        assert _req(base + "/p/demo/ep/ep01-intro/trace")[0] == 200
        # write stage + artifact drill-down
        _mk_write_run(tmp_path / "demo")
        code, body, _ = _req(
            base + "/p/demo/ep/ep01-intro/artifact?rel=stages/write.r1/transcript.v1.md"
        )
        assert code == 200 and "Draft body text" in body
        assert _req(base + "/p/demo/ep/ep01-intro/edit")[0] == 200
        assert _req(base + "/p/demo/ep/nope/edit")[0] == 404
        assert _req(base + "/bogus")[0] == 404
    finally:
        srv.shutdown()
        srv.server_close()


def test_web_import_is_torch_free():
    import prosodia.author.web  # noqa: F401

    assert "torch" not in sys.modules


# ── regressions for the bug-hunt fixes ────────────────────────────────────────

def test_action_submit_not_compiled(tmp_path):
    _mk_project(tmp_path)
    out = views.action_submit(tmp_path, "demo", "ep01-intro", "/tmp/exchange")
    assert out is not None and "Compile" in out


def test_action_submit_empty_root(tmp_path):
    _mk_project(tmp_path)
    views.action_compile(tmp_path, "demo", "ep01-intro")
    out = views.action_submit(tmp_path, "demo", "ep01-intro", "   ")
    assert out is not None and "exchange root" in out.lower()


def test_slug_html_attribute_escaped(tmp_path):
    # a slug carrying a double-quote must be escaped where it lands in HTML attributes
    proj = tmp_path / "demo"
    (proj / "episodes").mkdir(parents=True)
    (proj / "series.yaml").write_text(
        "series: X\nepisodes:\n  - n: 1\n    slug: 'a\"b'\n    title: T\n", encoding="utf-8"
    )
    out = views.render_project(tmp_path, "demo")
    assert out is not None
    assert 'a"b' not in out       # raw double-quote never survives into markup
    assert "a&quot;b" in out      # it was escaped


def test_index_survives_malformed_series(tmp_path):
    good = tmp_path / "good"
    (good / "episodes").mkdir(parents=True)
    (good / "series.yaml").write_text("series: Good\n", encoding="utf-8")
    bad = tmp_path / "bad"
    bad.mkdir()
    (bad / "series.yaml").write_text("- just\n- a\n- list\n", encoding="utf-8")  # top-level list
    out = views.render_index(tmp_path)  # must not raise
    assert "Good" in out and "bad" in out


def test_trace_body_survives_partial_runjson(tmp_path):
    proj = _mk_project(tmp_path)
    run_dir = proj / "episodes" / "ep01-intro" / "run"
    run_dir.mkdir(parents=True)
    (run_dir / "run.json").write_text('{"events": [', encoding="utf-8")  # truncated JSON
    assert views._trace_body(tmp_path, "demo", "ep01-intro") is None     # no exception
    assert views.render_trace(tmp_path, "demo", "ep01-intro") is None


def test_registry_worker_survives_bad_job():
    reg = JobRegistry()
    bad = reg.submit("x", "bad", ["this-binary-does-not-exist-xyz"])
    reg.wait(bad)
    assert bad.status == "failed"
    good = reg.submit("x", "good", [sys.executable, "-c", "print('after')"])
    reg.wait(good)
    assert good.status == "done" and "after" in good.tail()


def test_job_log_bounded():
    reg = JobRegistry()
    job = reg.submit("x", "chatty", [sys.executable, "-c", "[print(i) for i in range(5000)]"])
    reg.wait(job)
    assert job.status == "done"
    assert len(job.log) <= 4000


def test_registry_evicts_old_terminal_jobs():
    from prosodia.author.web.jobs import Job, _MAX_JOBS

    reg = JobRegistry()
    with reg._lock:
        for i in range(_MAX_JOBS + 10):
            reg._jobs[f"job-x{i}"] = Job(id=f"job-x{i}", kind="x", label="x", argv=[], status="done")
        reg._evict()
    assert len(reg._jobs) <= _MAX_JOBS


def test_csrf_cross_origin_blocked(tmp_path):
    _mk_project(tmp_path)
    srv, base = _start_server(tmp_path)
    try:
        req = urllib.request.Request(
            base + "/p/demo/ep/ep01-intro/compile", method="POST", data=b""
        )
        req.add_header("Origin", "http://evil.example")
        try:
            code = urllib.request.urlopen(req, timeout=10).status
        except urllib.error.HTTPError as e:
            code = e.code
        assert code == 403                                   # cross-origin POST refused
        assert _req(base + "/p/demo/ep/ep01-intro/compile", method="POST", body=b"")[0] == 200
    finally:
        srv.shutdown()
        srv.server_close()


def test_diagnose_unicode_beat_no_500(tmp_path):
    _mk_project(tmp_path)
    views.action_compile(tmp_path, "demo", "ep01-intro")
    srv, base = _start_server(tmp_path)
    try:
        body = urllib.parse.urlencode({"complaint": "flat", "beat": "²"}).encode()
        code, out, _ = _req(base + "/p/demo/ep/ep01-intro/diagnose", method="POST", body=body)
        assert code == 200 and "flat" in out                 # unicode-digit beat -> None, no crash
    finally:
        srv.shutdown()
        srv.server_close()
