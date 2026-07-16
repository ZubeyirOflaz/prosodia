"""Per-project pronunciation lexicon.

Chatterbox has no SSML phonemes, so proper nouns it would mangle are respelled
at compile time. The lexicon maps a source spelling to a respelling the engine
pronounces correctly; it is applied to ``spoken_text`` only, so the authored
transcript stays clean. Loaded from a project YAML (``{lexicon: {...}}`` or a
bare mapping). Matching is whole-word; longer keys win.
"""

from __future__ import annotations

import re
from pathlib import Path

import yaml


class Lexicon:
    def __init__(self, entries: dict[str, str] | None = None):
        self.entries = dict(entries or {})
        self._compiled = self._compile()

    def _compile(self) -> re.Pattern | None:
        if not self.entries:
            return None
        keys = sorted(self.entries, key=len, reverse=True)
        return re.compile(r"\b(" + "|".join(re.escape(k) for k in keys) + r")\b")

    def _compile_reverse(self) -> tuple[re.Pattern | None, dict[str, str]]:
        """Build the inverse (respelling -> source) matcher. When two sources map to
        the same respelling the last one wins (harmless for scoring). Respellings need
        not be \b-bounded on both sides (they may start/end with '-' or spaces), so we
        match them literally, longest-first."""
        if not self.entries:
            return None, {}
        rev: dict[str, str] = {}
        for src, resp in self.entries.items():
            rev[resp] = src
        keys = sorted(rev, key=len, reverse=True)
        pattern = re.compile("|".join(re.escape(k) for k in keys))
        return pattern, rev

    @classmethod
    def load(cls, path: Path | None) -> "Lexicon":
        if path is None or not Path(path).exists():
            return cls({})
        data = yaml.safe_load(Path(path).read_text(encoding="utf-8")) or {}
        entries = data.get("lexicon", data) if isinstance(data, dict) else {}
        return cls({str(k): str(v) for k, v in entries.items()})

    def apply(self, text: str) -> str:
        if not self._compiled:
            return text
        return self._compiled.sub(lambda m: self.entries[m.group(1)], text)

    def reverse(self, text: str) -> str:
        """Map respellings back to their source spellings. Used to build a
        Whisper-comparable reference for the render-side STT gate: a correct
        pronunciation of a respelled name is transcribed as the ORIGINAL name, so
        the gate must score against the original spelling, not the respelling."""
        pattern, rev = self._compile_reverse()
        if pattern is None:
            return text
        return pattern.sub(lambda m: rev[m.group(0)], text)
