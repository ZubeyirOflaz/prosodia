"""The synced job-folder protocol and its atomic-claim mechanism.

A job is a directory of files exchanged through a cloud-synced folder. The hazard
is that a job may be only partially synced when the renderer first sees it. The
guard is a content **manifest** (sha256 + size of every payload file): the
renderer claims a job only when every file in the manifest exists and matches.
Writing the manifest LAST makes its presence the readiness trigger, and a
``building/`` -> ``inbox/`` folder rename shrinks the race window further.

Single-writer zones avoid sync conflicts: the author writes only ``inbox/``, the
renderer writes only ``processing/``, ``outbox/``, and ``failed/``.
"""

from __future__ import annotations

import hashlib
import os
import shutil
from pathlib import Path

from pydantic import BaseModel, Field

# Folder names in the synced exchange root.
INBOX = "inbox"
PROCESSING = "processing"
OUTBOX = "outbox"
FAILED = "failed"
BUILDING = "building"

MANIFEST_NAME = "manifest.json"
STATUS_NAME = "status.json"

_HASH_BLOCK = 1 << 20  # 1 MiB


def _is_sync_temp(name: str) -> bool:
    """Transient files cloud-sync tools (Syncthing, Dropbox, Office) leave behind.

    These appear and vanish while a job syncs; treating them as 'unlisted file
    present' would needlessly block an otherwise-complete job, so they are
    ignored by both the manifest and the validator.
    """
    return (
        name.startswith(".")
        or name.startswith("~$")
        or name.endswith(".tmp")
        or name.endswith(".part")
        or name.endswith(".crdownload")
    )


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(_HASH_BLOCK), b""):
            h.update(block)
    return h.hexdigest()


class FileEntry(BaseModel):
    name: str  # POSIX-style relative path within the job dir
    size: int
    sha256: str


class Manifest(BaseModel):
    job_id: str
    files: list[FileEntry] = Field(default_factory=list)

    def to_json(self, indent: int = 2) -> str:
        return self.model_dump_json(indent=indent)

    @classmethod
    def from_json(cls, data: str) -> "Manifest":
        return cls.model_validate_json(data)


def _iter_payload_files(job_dir: Path) -> list[Path]:
    """All files under job_dir except the manifest itself, in stable order."""
    # The manifest is excluded (it lists the others) and status.json is excluded
    # because the renderer mutates it after claiming — it is control state, not an
    # immutable payload covered by the integrity check.
    return [
        p
        for p in sorted(job_dir.rglob("*"))
        if p.is_file()
        and p.name not in (MANIFEST_NAME, STATUS_NAME)
        and not _is_sync_temp(p.name)
    ]


def compute_manifest(job_dir: Path, job_id: str) -> Manifest:
    job_dir = Path(job_dir)
    entries = [
        FileEntry(
            name=p.relative_to(job_dir).as_posix(),
            size=p.stat().st_size,
            sha256=sha256_file(p),
        )
        for p in _iter_payload_files(job_dir)
    ]
    return Manifest(job_id=job_id, files=entries)


def write_manifest(job_dir: Path, manifest: Manifest) -> Path:
    """Write the manifest LAST — its presence is the readiness trigger."""
    path = Path(job_dir) / MANIFEST_NAME
    path.write_text(manifest.to_json(), encoding="utf-8")
    return path


def validate_job(job_dir: Path) -> list[str]:
    """Return a list of problems; an empty list means the job is complete & intact."""
    job_dir = Path(job_dir)
    manifest_path = job_dir / MANIFEST_NAME
    if not manifest_path.exists():
        return ["manifest.json is missing (job not finished syncing)"]
    try:
        manifest = Manifest.from_json(manifest_path.read_text(encoding="utf-8"))
    except Exception as exc:
        return [f"manifest.json is unreadable: {exc}"]

    problems: list[str] = []
    listed = {e.name for e in manifest.files}
    for entry in manifest.files:
        fp = job_dir / entry.name
        if not fp.exists():
            problems.append(f"missing file: {entry.name}")
        elif fp.stat().st_size != entry.size:
            problems.append(f"size mismatch: {entry.name}")
        elif sha256_file(fp) != entry.sha256:
            problems.append(f"hash mismatch: {entry.name}")
    for p in _iter_payload_files(job_dir):
        rel = p.relative_to(job_dir).as_posix()
        if rel not in listed:
            problems.append(f"unlisted file present: {rel}")
    return problems


def atomic_publish(building_job_dir: Path, inbox_dir: Path) -> Path:
    """Move a fully-written job from building/ into inbox/ via a single rename.

    ``building/`` and ``inbox/`` must be on the same filesystem for the rename to
    be atomic.
    """
    building_job_dir = Path(building_job_dir)
    inbox_dir = Path(inbox_dir)
    inbox_dir.mkdir(parents=True, exist_ok=True)
    dest = inbox_dir / building_job_dir.name
    # On Windows, os.replace onto an existing non-empty directory raises
    # PermissionError, so a re-submitted job_id would crash. Clear the previous
    # destination first (mirrors watch_and_render._move).
    if dest.exists():
        shutil.rmtree(dest)
    os.replace(building_job_dir, dest)  # atomic within a filesystem
    return dest


class JobStatus(BaseModel):
    job_id: str
    state: str = "queued"  # queued | rendering | done | failed
    message: str = ""
    progress: float = 0.0

    def to_json(self, indent: int = 2) -> str:
        return self.model_dump_json(indent=indent)
