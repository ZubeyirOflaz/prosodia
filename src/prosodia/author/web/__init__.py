"""Local authoring dashboard (``prosodia ui``).

A dependency-free web UI over the authoring workspace: browse projects and episodes;
run the planner/writer as background jobs; compile, edit transcripts, repetition-lint,
diagnose, and package render jobs; and open the plan outline and per-episode run trace
(interactive). Standard-library ``http.server`` plus a small in-house htmx-style JS
layer — no torch, no framework, no build step — so it stays inside the authoring
boundary (see ``docs/authoring-ui.md``).
"""

from __future__ import annotations


def serve(*args, **kwargs):
    """Start the dashboard server. Imported lazily so importing this package stays
    cheap (and provably torch-free)."""
    from prosodia.author.web.server import serve as _serve

    return _serve(*args, **kwargs)


__all__ = ["serve"]
