"""Personas — a switchable, self-contained authoring voice.

A persona fully owns how a show is authored: the role prompts (planner / writer /
editor / tone), the tone table (``voice_profiles.yaml``), and defaults (target
length, host mode, default voice, freshness watchlist). Ownership is complete —
there is no shared base — so a persona can diverge as far as its topic needs.

Personas resolve by name across a search path: a project-local ``personas/`` dir
(project-specific personas or overrides) first, then the packaged library shipped
under ``prosodia/author/personas/``. An omitted persona defaults to
``hardcore-history`` (the original voice), so existing projects are unaffected.

The ``diagnostician`` role is intentionally NOT part of a persona — it reasons
about the pipeline, not the content style, and stays package-level.
"""

from __future__ import annotations

from pathlib import Path

import yaml
from pydantic import BaseModel, Field

DEFAULT_PERSONA = "hardcore-history"


class PersonaDefaults(BaseModel):
    target_minutes: int = 30
    host_mode: str = "single"  # single | two-host
    voice: str = "narrator"
    freshness_watchlist: list[str] = Field(default_factory=list)


class Persona:
    """A persona resolved to a directory on disk."""

    def __init__(self, name: str, root: Path, meta: dict | None = None):
        self.name = name
        self.root = Path(root)
        meta = meta or {}
        self.title: str = meta.get("title", name)
        self.description: str = meta.get("description", "")
        self.defaults = PersonaDefaults(**(meta.get("defaults") or {}))

    def role(self, role_name: str) -> str:
        """Return the persona's prompt for a role (planner/writer/editor/tone)."""
        path = self.root / "roles" / f"{role_name}.md"
        if not path.exists():
            raise FileNotFoundError(
                f"persona {self.name!r} has no role {role_name!r} (expected {path})"
            )
        return path.read_text(encoding="utf-8")

    def has_role(self, role_name: str) -> bool:
        return (self.root / "roles" / f"{role_name}.md").exists()

    def voice_profiles_path(self) -> Path:
        return self.root / "voice_profiles.yaml"

    # -- resolution -----------------------------------------------------------

    @staticmethod
    def _builtin_library() -> Path:
        """The packaged persona library (ships as package data)."""
        return Path(__file__).resolve().parent / "personas"

    @classmethod
    def search_dirs(cls, project: str | Path | None = None) -> list[Path]:
        dirs: list[Path] = []
        if project is not None:
            dirs.append(Path(project) / "personas")  # project-local override / additions
        dirs.append(cls._builtin_library())  # shared built-in library
        return dirs

    @classmethod
    def resolve(cls, name: str | None = None, *, project: str | Path | None = None) -> "Persona":
        """Resolve a persona by name (default ``hardcore-history``). Project-local
        personas take precedence over the built-in library."""
        name = name or DEFAULT_PERSONA
        for d in cls.search_dirs(project):
            root = d / name
            if (root / "roles").is_dir():
                meta: dict = {}
                pm = root / "persona.yaml"
                if pm.exists():
                    loaded = yaml.safe_load(pm.read_text(encoding="utf-8"))
                    meta = loaded if isinstance(loaded, dict) else {}
                return cls(name, root, meta)
        avail = ", ".join(cls.available(project)) or "(none found)"
        raise FileNotFoundError(f"persona {name!r} not found. Available: {avail}")

    @classmethod
    def available(cls, project: str | Path | None = None) -> list[str]:
        """Names of resolvable personas across the search path (dedup, project first)."""
        names: list[str] = []
        for d in cls.search_dirs(project):
            if d.is_dir():
                for child in sorted(d.iterdir()):
                    if child.is_dir() and (child / "roles").is_dir() and child.name not in names:
                        names.append(child.name)
        return names
