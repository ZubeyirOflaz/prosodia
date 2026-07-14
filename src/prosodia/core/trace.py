"""Process trace: the low-level append-only log plus the richer ``Run``.

Two layers, both pure-Python (no torch):

* ``Trace`` — the original append-only JSONL writer (``append(step, role, **fields)``).
  Kept unchanged for back-compat with existing call sites.
* ``Run`` — manages a per-episode ``run/`` folder: id-linked, status-bearing
  :class:`TraceEvent` records in ``events.jsonl``, content-hashed
  :class:`Artifact` files under ``stages/``, and a ``run.json`` index. This is the
  substrate both the HTML trace viewer and agentic diagnosis read, so a complaint
  about the final audio can be routed back to the stage that caused it.
"""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from pydantic import BaseModel, Field


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


class Trace:
    """Low-level append-only JSONL trace (one line per stage). Unchanged."""

    def __init__(self, path: Path):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def append(self, step: str, role: str, **fields: Any) -> None:
        event: dict[str, Any] = {
            "ts": _now(),
            "step": step,
            "role": role,
        }
        event.update(fields)
        with open(self.path, "a", encoding="utf-8") as f:
            f.write(json.dumps(event, ensure_ascii=False) + "\n")

    def read(self) -> list[dict[str, Any]]:
        if not self.path.exists():
            return []
        return [
            json.loads(line)
            for line in self.path.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]


# --- Enriched run trace ------------------------------------------------------

#: Pipeline stages, in canonical order (used for sorting / display).
STAGES = ("plan", "write", "edit", "compile", "tone", "submit", "render", "diagnose")

STATUS_RANK = {"ok": 0, "warn": 1, "error": 2}


class Artifact(BaseModel):
    """A content-hashed file produced or consumed by a stage.

    ``rel`` is POSIX-style and relative to the run directory, so a run folder is
    portable and the viewer/agent can resolve every reference the same way.
    """

    rel: str
    sha256: str
    size: int
    label: str | None = None


class TraceEvent(BaseModel):
    """One stage's record. ``meta`` holds stage-specific extras (model, params,
    the Editor's ``{ready, notes}`` verdict, segment ids touched, …)."""

    id: str
    parent: str | None = None
    stage: str
    role: str = ""
    status: str = "ok"  # ok | warn | error
    ts: str = Field(default_factory=_now)
    round: int | None = None
    inputs: list[Artifact] = Field(default_factory=list)
    outputs: list[Artifact] = Field(default_factory=list)
    warnings: list[str] = Field(default_factory=list)
    meta: dict[str, Any] = Field(default_factory=dict)


class RunIndex(BaseModel):
    """The ordered event DAG + a rolled-up status — written to ``run.json``."""

    episode: int | None = None
    title: str | None = None
    created: str = Field(default_factory=_now)
    updated: str = Field(default_factory=_now)
    status: str = "ok"
    events: list[TraceEvent] = Field(default_factory=list)


class Run:
    """Manager for one episode's ``run/`` folder.

    Append events with :meth:`event`; persist stage outputs with
    :meth:`write_artifact` (which hashes them); call :meth:`write_index` to
    refresh ``run.json``. Re-opening an existing run continues the event counter,
    so a resumed pipeline keeps one coherent, append-only history.
    """

    def __init__(self, run_dir: str | Path):
        self.dir = Path(run_dir)
        self.dir.mkdir(parents=True, exist_ok=True)
        self.events_path = self.dir / "events.jsonl"
        self.index_path = self.dir / "run.json"
        self.stages_dir = self.dir / "stages"
        self._events: list[TraceEvent] = self._load_events()
        self._counter = len(self._events)

    def _load_events(self) -> list[TraceEvent]:
        if not self.events_path.exists():
            return []
        events: list[TraceEvent] = []
        for line in self.events_path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            try:
                events.append(TraceEvent.model_validate_json(line))
            except Exception:  # noqa: BLE001 - tolerate a partial/corrupt trailing line
                continue
        return events

    def _next_id(self) -> str:
        self._counter += 1
        return f"e{self._counter:02d}"

    def stage_dir(self, name: str) -> Path:
        d = self.stages_dir / name
        d.mkdir(parents=True, exist_ok=True)
        return d

    def write_artifact(self, rel: str | Path, content: str | bytes, *, label: str | None = None) -> Artifact:
        """Write ``content`` to ``rel`` (relative to the run dir) and hash it."""
        rel_posix = Path(rel).as_posix()
        path = self.dir / rel_posix
        path.parent.mkdir(parents=True, exist_ok=True)
        data = content.encode("utf-8") if isinstance(content, str) else content
        path.write_bytes(data)
        return Artifact(rel=rel_posix, sha256=sha256_bytes(data), size=len(data), label=label)

    def ref(self, rel: str | Path, *, label: str | None = None) -> Artifact:
        """Hash a file that already lives under the run dir (no write)."""
        rel_posix = Path(rel).as_posix()
        data = (self.dir / rel_posix).read_bytes()
        return Artifact(rel=rel_posix, sha256=sha256_bytes(data), size=len(data), label=label)

    def event(
        self,
        stage: str,
        role: str = "",
        *,
        status: str = "ok",
        parent: str | None | object = "auto",
        round: int | None = None,
        inputs: list[Artifact] | None = None,
        outputs: list[Artifact] | None = None,
        warnings: list[str] | None = None,
        **meta: Any,
    ) -> TraceEvent:
        """Append one event. ``parent="auto"`` links to the previous event; pass
        an explicit id (or ``None``) to override. Any extra kwargs land in ``meta``."""
        if parent == "auto":
            parent = self._events[-1].id if self._events else None
        warnings = warnings or []
        # An event with warnings but an unset status is at least a warning.
        if warnings and status == "ok":
            status = "warn"
        ev = TraceEvent(
            id=self._next_id(),
            parent=parent,  # type: ignore[arg-type]
            stage=stage,
            role=role,
            status=status,
            round=round,
            inputs=inputs or [],
            outputs=outputs or [],
            warnings=warnings,
            meta=dict(meta),
        )
        with open(self.events_path, "a", encoding="utf-8") as f:
            f.write(ev.model_dump_json() + "\n")
        self._events.append(ev)
        return ev

    def events(self) -> list[TraceEvent]:
        return list(self._events)

    def rollup_status(self) -> str:
        worst = "ok"
        for ev in self._events:
            if STATUS_RANK.get(ev.status, 0) > STATUS_RANK[worst]:
                worst = ev.status
        return worst

    def write_index(self, *, episode: int | None = None, title: str | None = None) -> Path:
        idx = RunIndex(
            episode=episode,
            title=title,
            created=self._events[0].ts if self._events else _now(),
            updated=_now(),
            status=self.rollup_status(),
            events=self._events,
        )
        self.index_path.write_text(idx.model_dump_json(indent=2), encoding="utf-8")
        return self.index_path
