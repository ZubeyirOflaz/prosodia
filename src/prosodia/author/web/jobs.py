"""Background job runner for the authoring dashboard.

Long authoring steps (``plan``, ``write``) shell out to ``claude -p`` and take
minutes; concurrent ``claude -p`` sessions contend, so they run on a **single
serialized worker**. Fast, deterministic steps (``compile``, ``lint``, deterministic
``diagnose``) don't go through here — the server runs them inline via :func:`run_sync`.

Standard-library only. Job state is in-memory (the durable record is the per-episode
``run/`` trace on disk); status is derived from the subprocess.
"""

from __future__ import annotations

import itertools
import os
import queue
import subprocess
import threading
from collections import deque
from dataclasses import dataclass, field

_TERMINAL = {"done", "failed"}

# Wall-clock ceiling for a single job (generous — real jobs run minutes), and how many
# jobs to retain in memory (the durable record lives in the on-disk run/ trace).
_JOB_TIMEOUT_S = 3600
_MAX_JOBS = 100

# Force child prosodia/claude processes to emit UTF-8 on Windows (their default is
# the console codepage, e.g. cp1252, which mangles em-dashes); decode leniently too.
_UTF8_ENV = {**os.environ, "PYTHONUTF8": "1", "PYTHONIOENCODING": "utf-8"}


@dataclass
class Job:
    id: str
    kind: str            # "plan" | "write" | ...
    label: str           # human label, e.g. "write ep2"
    argv: list[str]
    status: str = "queued"   # queued | running | done | failed
    returncode: int | None = None
    log: deque = field(default_factory=lambda: deque(maxlen=4000))  # capped; only tail() is read
    meta: dict = field(default_factory=dict)   # e.g. {"project":..., "slug":...}

    @property
    def done(self) -> bool:
        return self.status in _TERMINAL

    def tail(self, chars: int = 6000) -> str:
        text = "".join(self.log)
        return text[-chars:]


def run_sync(argv: list[str], cwd: str | None = None, timeout: int = 300) -> tuple[int, str]:
    """Run a fast command to completion, returning ``(returncode, combined_output)``."""
    try:
        proc = subprocess.run(
            argv, cwd=cwd, capture_output=True, text=True, encoding="utf-8", errors="replace",
            env=_UTF8_ENV, timeout=timeout,
        )
    except subprocess.TimeoutExpired:
        return 124, f"timed out after {timeout}s"
    except Exception as exc:  # noqa: BLE001
        return -1, f"failed to launch: {exc}"
    return proc.returncode, (proc.stdout or "") + (proc.stderr or "")


class JobRegistry:
    """In-memory registry with one worker thread (serializes LLM jobs)."""

    def __init__(self) -> None:
        self._jobs: dict[str, Job] = {}
        self._q: queue.Queue[Job] = queue.Queue()
        self._lock = threading.Lock()
        self._counter = itertools.count(1)
        self._worker = threading.Thread(target=self._run_loop, daemon=True)
        self._worker.start()

    def submit(self, kind: str, label: str, argv: list[str], meta: dict | None = None) -> Job:
        with self._lock:
            jid = f"job-{next(self._counter):04d}"
            job = Job(id=jid, kind=kind, label=label, argv=list(argv), meta=meta or {})
            self._jobs[jid] = job
            self._evict()
        self._q.put(job)
        return job

    def _evict(self) -> None:
        """Drop the oldest terminal jobs beyond the retention cap (caller holds the lock)."""
        while len(self._jobs) > _MAX_JOBS:
            for jid, j in self._jobs.items():
                if j.done:
                    del self._jobs[jid]
                    break
            else:
                break  # nothing evictable (all still running/queued)

    def get(self, jid: str) -> Job | None:
        with self._lock:
            return self._jobs.get(jid)

    def recent(self, limit: int = 20) -> list[Job]:
        with self._lock:
            return list(self._jobs.values())[-limit:][::-1]

    def wait(self, job: Job, timeout: float = 15.0) -> Job:
        """Poll until ``job`` reaches a terminal state or ``timeout`` (used by tests)."""
        import time

        deadline = time.monotonic() + timeout
        while not job.done and time.monotonic() < deadline:
            time.sleep(0.02)
        return job

    def _run_loop(self) -> None:
        while True:
            job = self._q.get()
            try:
                self._execute(job)
            except Exception as exc:  # noqa: BLE001 - one bad job must never kill the worker
                job.log.append(f"\n[runner] worker error: {exc}\n")
                job.status = "failed"
                if job.returncode is None:
                    job.returncode = -1
            finally:
                self._q.task_done()

    def _execute(self, job: Job) -> None:
        job.status = "running"
        try:
            proc = subprocess.Popen(
                job.argv,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                encoding="utf-8",
                errors="replace",
                env=_UTF8_ENV,
                bufsize=1,
            )
        except Exception as exc:  # noqa: BLE001
            job.log.append(f"[runner] failed to launch: {exc}\n")
            job.status = "failed"
            job.returncode = -1
            return

        # Watchdog: kill a job that overruns the wall-clock ceiling — covers a silently
        # hung child (no output) that the blocking read loop could never detect itself.
        timed_out = {"v": False}

        def _kill() -> None:
            timed_out["v"] = True
            job.log.append(f"\n[runner] timed out after {_JOB_TIMEOUT_S}s — killing\n")
            try:
                proc.kill()
            except Exception:  # noqa: BLE001
                pass

        watchdog = threading.Timer(_JOB_TIMEOUT_S, _kill)
        watchdog.daemon = True
        watchdog.start()
        try:
            if proc.stdout is not None:
                for line in proc.stdout:
                    job.log.append(line)
            proc.wait()
            job.returncode = 124 if timed_out["v"] else proc.returncode
            job.status = "failed" if (timed_out["v"] or proc.returncode != 0) else "done"
        except Exception as exc:  # noqa: BLE001 - streaming/wait must not kill the worker
            job.log.append(f"\n[runner] error while running: {exc}\n")
            try:
                proc.kill()
            except Exception:  # noqa: BLE001
                pass
            job.status = "failed"
            if job.returncode is None:
                job.returncode = -1
        finally:
            watchdog.cancel()
