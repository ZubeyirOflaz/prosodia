"""Local authoring dashboard (Phase 1 — read-only).

A dependency-free web UI over the authoring workspace: browse projects and their
episodes, and open the plan outline and per-episode run traces the pipeline already
produces. Standard-library only (``http.server``) — no torch, no framework, no build
step — so it stays inside the authoring boundary (see ``docs/authoring-ui.md``).

Phase 1 is read-only. Triggering jobs, live status, and in-browser editing arrive in
later phases; htmx is introduced with the live job console (Phase 2).
"""

from __future__ import annotations


def serve(*args, **kwargs):
    """Start the dashboard server. Imported lazily so importing this package stays
    cheap (and provably torch-free)."""
    from prosodia.author.web.server import serve as _serve

    return _serve(*args, **kwargs)


__all__ = ["serve"]
