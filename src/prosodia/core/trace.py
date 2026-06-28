"""Append-only process trace.

Each authoring stage appends one JSON line recording what it did and which
artifact it produced, so a complaint about the final audio can be routed back to
the stage that caused it (Planner / Writer / Editor / Tone specialist / compile
/ render). The versioned artifacts hold the content; this log links them in
order.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class Trace:
    def __init__(self, path: Path):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def append(self, step: str, role: str, **fields: Any) -> None:
        event: dict[str, Any] = {
            "ts": datetime.now(timezone.utc).isoformat(),
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
