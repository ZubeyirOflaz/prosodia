"""Watch the synced inbox and render jobs as they arrive (GPU box).

For each job directory whose manifest validates (sha256 + size of every payload
file — the atomic claim, repair B1/A2), atomically move it to ``processing/``,
render it, and move it to ``outbox/`` with a ``done`` status; on failure move it
to ``failed/`` with the error. Jobs whose manifest does not yet validate are
skipped (still syncing). The TTS backend is loaded once and kept warm across jobs.
"""

from __future__ import annotations

import os
import shutil
import time
from pathlib import Path

from prosodia.core import protocol
from prosodia.render.render import render_job


def _move(src: Path, dst_root: Path, name: str) -> Path:
    dst_root = Path(dst_root)
    dst_root.mkdir(parents=True, exist_ok=True)
    dst = dst_root / name
    if dst.exists():
        shutil.rmtree(dst)
    os.replace(src, dst)  # atomic within a filesystem
    return dst


def render_one(job_dir, root, *, fast_preview=True, voices_dir=None, backend=None) -> Path:
    job_dir, root = Path(job_dir), Path(root)
    name = job_dir.name
    proc = _move(job_dir, root / protocol.PROCESSING, name)  # claim
    status = proc / protocol.STATUS_NAME
    status.write_text(protocol.JobStatus(job_id=name, state="rendering").to_json(), encoding="utf-8")
    try:
        audio = render_job(
            proc, proc / "episode.wav", fast_preview=fast_preview, voices_dir=voices_dir, backend=backend
        )
        status.write_text(
            protocol.JobStatus(job_id=name, state="done", message=audio.name, progress=1.0).to_json(),
            encoding="utf-8",
        )
        return _move(proc, root / protocol.OUTBOX, name)
    except Exception as exc:  # noqa: BLE001 - record any failure and quarantine the job
        status.write_text(
            protocol.JobStatus(job_id=name, state="failed", message=str(exc)[:300]).to_json(),
            encoding="utf-8",
        )
        return _move(proc, root / protocol.FAILED, name)


def watch(root, *, interval: float = 5.0, fast_preview: bool = True, voices_dir=None, once: bool = False):
    root = Path(root)
    inbox = root / protocol.INBOX
    backend = None
    print(f"watching {inbox} (fast_preview={fast_preview}) ...")
    warned_missing = False
    reported: dict[str, str] = {}  # job -> last skip reason logged (avoid spamming each poll)
    while True:
        if not inbox.exists():
            if not warned_missing:
                print(
                    f"  note: {inbox} does not exist yet. Submit a job with "
                    f"`prosodia submit <episode> --root {root}` (it creates inbox/), then let it sync."
                )
                warned_missing = True
        else:
            warned_missing = False
            jobs = sorted(p for p in inbox.iterdir() if p.is_dir())
            for job in jobs:
                problems = protocol.validate_job(job)
                if problems:  # not yet claimable: still syncing, or a manifest mismatch
                    msg = "; ".join(problems)
                    if reported.get(job.name) != msg:  # log only when the reason changes
                        print(f"  skipping {job.name}: {msg}")
                        reported[job.name] = msg
                    continue
                reported.pop(job.name, None)
                if backend is None:  # warm the model once, on the first real job
                    from prosodia.render.backends.chatterbox_backend import ChatterboxBackend

                    backend = ChatterboxBackend()
                    backend.load()
                print(f"rendering {job.name} ...")
                dest = render_one(job, root, fast_preview=fast_preview, voices_dir=voices_dir, backend=backend)
                print(f"  done -> {dest}")
        if once:
            break
        time.sleep(interval)
