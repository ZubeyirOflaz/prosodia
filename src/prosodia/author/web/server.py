"""The dashboard server: a localhost ``ThreadingHTTPServer`` with a small router.

GET serves pages and fragments; POST triggers actions (enqueue a job, compile, save,
diagnose). Long ``plan``/``write`` steps go on the serialized :class:`JobRegistry`;
fast steps run inline. Bound to loopback only — single user, no auth. Std-lib only.
"""

from __future__ import annotations

import re
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, unquote

from prosodia.author.web import assets, views
from prosodia.author.web.jobs import JobRegistry

_GET = [
    (re.compile(r"^/$"), "index"),
    (re.compile(r"^/assets/app\.js$"), "appjs"),
    (re.compile(r"^/p/([^/]+)$"), "project"),
    (re.compile(r"^/p/([^/]+)/outline$"), "outline"),
    (re.compile(r"^/p/([^/]+)/lint$"), "lint"),
    (re.compile(r"^/p/([^/]+)/ep/([^/]+)/trace$"), "trace"),
    (re.compile(r"^/p/([^/]+)/ep/([^/]+)/trace/fragment$"), "trace_fragment"),
    (re.compile(r"^/p/([^/]+)/ep/([^/]+)/edit$"), "edit_form"),
    (re.compile(r"^/p/([^/]+)/ep/([^/]+)/diagnose$"), "diagnose_form"),
    (re.compile(r"^/p/([^/]+)/ep/([^/]+)/submit$"), "submit_form"),
    (re.compile(r"^/jobs/([^/]+)$"), "job_page"),
    (re.compile(r"^/jobs/([^/]+)/fragment$"), "job_fragment"),
]
_POST = [
    (re.compile(r"^/p/([^/]+)/plan$"), "plan"),
    (re.compile(r"^/p/([^/]+)/ep/([^/]+)/write$"), "write"),
    (re.compile(r"^/p/([^/]+)/ep/([^/]+)/compile$"), "compile"),
    (re.compile(r"^/p/([^/]+)/ep/([^/]+)/edit$"), "edit_save"),
    (re.compile(r"^/p/([^/]+)/ep/([^/]+)/diagnose$"), "diagnose"),
    (re.compile(r"^/p/([^/]+)/ep/([^/]+)/submit$"), "submit"),
]


class _Handler(BaseHTTPRequestHandler):
    server_version = "prosodia-ui/0.2"

    def log_message(self, *args) -> None:  # keep the console quiet
        pass

    def _send(self, body: str, status: int = 200, ctype: str = "text/html; charset=utf-8") -> None:
        data = body.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    @property
    def root(self) -> Path:
        return self.server.root  # type: ignore[attr-defined]

    @property
    def jobs(self) -> JobRegistry:
        return self.server.jobs  # type: ignore[attr-defined]

    def do_GET(self) -> None:
        path = self.path.split("?", 1)[0]
        try:
            for rx, name in _GET:
                m = rx.match(path)
                if not m:
                    continue
                a = [unquote(g) for g in m.groups()]
                if name == "appjs":
                    return self._send(assets.APP_JS, ctype="application/javascript; charset=utf-8")
                out = self._get(name, a)
                if out is None:
                    return self._send(views.not_found(path), 404)
                return self._send(out)
            return self._send(views.not_found(path), 404)
        except Exception as exc:  # noqa: BLE001 - never crash the dev server on one request
            return self._send(views.error_page(exc), 500)

    def _get(self, name: str, a: list[str]) -> str | None:
        r = self.root
        if name == "index":
            return views.render_index(r)
        if name == "project":
            return views.render_project(r, a[0])
        if name == "outline":
            return views.render_outline(r, a[0])
        if name == "lint":
            return views.action_lint(r, a[0])
        if name == "trace":
            return views.render_trace(r, a[0], a[1])
        if name == "trace_fragment":
            return views.render_trace_fragment(r, a[0], a[1])
        if name == "edit_form":
            return views.render_editor(r, a[0], a[1])
        if name == "diagnose_form":
            return views.render_diagnose_form(r, a[0], a[1])
        if name == "submit_form":
            return views.render_submit_form(r, a[0], a[1])
        if name == "job_page":
            return views.render_job_page(self.jobs, r, a[0])
        if name == "job_fragment":
            return views.render_job_panel(self.jobs, r, a[0])
        return None

    def do_POST(self) -> None:
        path = self.path.split("?", 1)[0]
        try:
            length = int(self.headers.get("Content-Length", 0) or 0)
            raw = self.rfile.read(length).decode("utf-8") if length else ""
            form = parse_qs(raw, keep_blank_values=True)
            for rx, name in _POST:
                m = rx.match(path)
                if not m:
                    continue
                a = [unquote(g) for g in m.groups()]
                out = self._post(name, a, form)
                if out is None:
                    return self._send(views.not_found(path), 404)
                return self._send(out)
            return self._send(views.not_found(path), 404)
        except Exception as exc:  # noqa: BLE001
            return self._send(views.error_page(exc), 500)

    def _post(self, name: str, a: list[str], form: dict) -> str | None:
        r = self.root
        if name == "plan":
            return views.action_plan(self.jobs, r, a[0])
        if name == "write":
            return views.action_write(self.jobs, r, a[0], a[1])
        if name == "compile":
            return views.action_compile(r, a[0], a[1])
        if name == "edit_save":
            return views.action_edit_save(r, a[0], a[1], form.get("content", [""])[0])
        if name == "diagnose":
            beat_raw = form.get("beat", [""])[0].strip()
            beat = int(beat_raw) if beat_raw.isdigit() else None
            return views.action_diagnose(r, a[0], a[1], form.get("complaint", [""])[0], beat)
        if name == "submit":
            return views.action_submit(r, a[0], a[1], form.get("root", [""])[0])
        return None


class _Server(ThreadingHTTPServer):
    daemon_threads = True
    allow_reuse_address = True

    def __init__(self, addr, root: Path):
        self.root = root
        self.jobs = JobRegistry()
        super().__init__(addr, _Handler)


def serve(root, *, host: str = "127.0.0.1", port: int = 8765, open_browser: bool = True) -> None:
    root = Path(root)
    srv = _Server((host, port), root)
    url = f"http://{host}:{port}/"
    print(f"prosodia ui · serving {root} at {url}  (Ctrl-C to stop)")
    if open_browser:
        import webbrowser

        try:
            webbrowser.open(url)
        except Exception:
            pass
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        print("\nstopping…")
    finally:
        srv.server_close()
