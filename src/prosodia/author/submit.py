"""Package a compiled episode into a render job and publish it to the inbox.

Writes the immutable inputs (ir.json, render_plan.json, optional voice reference)
into a ``building/`` staging dir, computes the manifest LAST, then atomically
renames the folder into ``inbox/``. The renderer owns the mutable status.json
downstream, so status is not part of the manifest.
"""

from __future__ import annotations

import shutil
from pathlib import Path

from prosodia.core import protocol
from prosodia.core.ir import EpisodeIR, RenderPlan


def package_job(
    exchange_root: str | Path,
    job_id: str,
    ir: EpisodeIR,
    render_plan: RenderPlan,
    *,
    voice_ref: str | Path | None = None,
    extra_files: list[str | Path] | None = None,
) -> Path:
    """Stage, manifest, and atomically publish a job. Returns the inbox path."""
    exchange_root = Path(exchange_root)
    building = exchange_root / protocol.BUILDING / job_id
    if building.exists():
        shutil.rmtree(building)
    building.mkdir(parents=True)

    (building / "ir.json").write_text(ir.to_json(), encoding="utf-8")
    (building / "render_plan.json").write_text(render_plan.to_json(), encoding="utf-8")

    # Copy bundled assets by basename, but refuse silent overwrites: two sources
    # sharing a basename would clobber each other and the manifest would list only
    # the survivor (quiet data loss). A missing source is an error, not a no-op.
    seen: set[str] = {"ir.json", "render_plan.json"}
    sources: list[Path] = []
    if voice_ref:
        sources.append(Path(voice_ref))
    sources += [Path(f) for f in (extra_files or [])]
    for src in sources:
        if not src.exists():
            raise FileNotFoundError(f"bundled asset not found: {src}")
        if src.name in seen:
            raise ValueError(f"basename collision in job assets: {src.name!r}")
        seen.add(src.name)
        shutil.copy2(src, building / src.name)

    protocol.write_manifest(building, protocol.compute_manifest(building, job_id))  # LAST
    return protocol.atomic_publish(building, exchange_root / protocol.INBOX)
