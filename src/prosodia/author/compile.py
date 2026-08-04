"""Compile a transcript (``formats/SPEC.md``) into the IR.

Parsing implements the repair items:
* front-matter is ONLY the leading ``---`` fence (D2); later ``---`` lines are
  treated as non-spoken thematic breaks;
* a beat's directives are the *trailing* ``{...}`` group on its ``##`` header (D3);
* directive parsing is quote-aware, so commas/colons inside a quoted value are
  safe (D1).

Segmentation: a ``Segment`` is a contiguous run of speech with a single intent
and no internal pause. Paragraph breaks, beat boundaries, and ``{pause: N}``
become the ``pause_before_ms`` of the following segment. ``spoken_text`` is
normalized and lexicon-respelled; ``authored_text`` is kept for provenance.

Voice resolution precedence (repair C1): instruction-time override ->
front-matter ``voice`` -> project-config default.
"""

from __future__ import annotations

import re
from pathlib import Path

import yaml

from prosodia.author.chunk import DEFAULT_MAX_CHARS, chunk_text
from prosodia.author.lexicon import Lexicon
from prosodia.author.normalize import normalize_text
from prosodia.author.tone import VoiceProfiles, build_render_plan
from prosodia.core.intents import Intent
from prosodia.core.ir import EpisodeIR, RenderPlan, Segment

_COMMENT = re.compile(r"<!--.*?-->", re.S)
_H1 = re.compile(r"^#\s+")
_H2 = re.compile(r"^##\s+")
_HN = re.compile(r"^#{3,}\s+")
_THEMATIC = re.compile(r"^\s*([-*_])\1{2,}\s*$")
_BEAT_HDR = re.compile(r"^##\s+(.*?)(?:\s*\{([^{}]*)\})?\s*$")
_TOKEN = re.compile(
    r"(?P<para>\n[ \t]*\n)"
    r"|(?P<speaker>(?<![^\n])@[A-Za-z0-9_]+)"
    r"|(?P<directive>(?<!\\)\{[^{}]*\})"
    # Emphasis: any asterisk fence — *emph*, **strong**, ***both***. All fence asterisks
    # are stripped so none leak into spoken_text; writers reach for **bold**/***x*** and a
    # fixed-count rule left literal '*' in the audio. (?<!\\) keeps escaped \* literal.
    r"|(?P<emph>(?<!\\)\*+[^*\n]+\*+)"
)
_INTENT_KEYS = {"tone", "rate", "note"}


# ---- quote-aware directive parsing (repair D1) ------------------------------

def _split_top(s: str, sep: str) -> list[str]:
    parts, buf, q = [], [], None
    for ch in s:
        if q:
            buf.append(ch)
            if ch == q:
                q = None
        elif ch in "\"'":
            q = ch
            buf.append(ch)
        elif ch == sep:
            parts.append("".join(buf))
            buf = []
        else:
            buf.append(ch)
    parts.append("".join(buf))
    return parts


def _split_first(s: str, sep: str) -> tuple[str, str]:
    q = None
    for i, ch in enumerate(s):
        if q:
            if ch == q:
                q = None
        elif ch in "\"'":
            q = ch
        elif ch == sep:
            return s[:i], s[i + 1:]
    return s, ""


def _strip_quotes(v: str) -> str:
    v = v.strip()
    if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
        return v[1:-1]
    return v


def parse_directives(inner: str) -> dict[str, str]:
    out: dict[str, str] = {}
    for pair in _split_top(inner, ","):
        if not pair.strip():
            continue
        key, val = _split_first(pair, ":")
        out[key.strip().lower()] = _strip_quotes(val)
    return out


# ---- structure parsing ------------------------------------------------------

def split_front_matter(text: str) -> tuple[dict, str]:
    """Front-matter is ONLY a leading ``---`` fence (repair D2)."""
    lines = text.splitlines()
    if lines and lines[0].strip() == "---":
        for j in range(1, len(lines)):
            if lines[j].strip() == "---":
                try:
                    fm = yaml.safe_load("\n".join(lines[1:j])) or {}
                except yaml.YAMLError as exc:
                    raise ValueError(f"malformed YAML front-matter: {exc}") from exc
                return (fm if isinstance(fm, dict) else {}), "\n".join(lines[j + 1:])
    return {}, text


def _parse_beat_header(line: str) -> tuple[str | None, dict]:
    m = _BEAT_HDR.match(line)
    title = (m.group(1) or "").strip() or None
    directives = parse_directives(m.group(2)) if m.group(2) else {}
    return title, directives


def split_beats(body: str) -> list[tuple[str | None, dict, str]]:
    """Split a body into ``(title, directives, beat_body)`` beats by ``##`` headers.

    ``#`` (episode title), ``###+`` (reserved), and thematic breaks are skipped
    (not spoken). Content before the first ``##`` becomes an implicit beat.
    """
    beats: list[tuple[str | None, dict, str]] = []
    cur: dict | None = None
    pre: list[str] = []

    def push(c: dict | None) -> None:
        if c is not None:
            beats.append((c["title"], c["directives"], "\n".join(c["lines"]).strip()))

    for line in body.splitlines():
        if _H2.match(line):
            push(cur)
            title, directives = _parse_beat_header(line)
            cur = {"title": title, "directives": directives, "lines": []}
        elif _H1.match(line) or _HN.match(line) or _THEMATIC.match(line):
            continue
        elif cur is None:
            pre.append(line)
        else:
            cur["lines"].append(line)
    push(cur)
    pre_body = "\n".join(pre).strip()
    if pre_body:
        beats.insert(0, (None, {}, pre_body))
    return beats


def _unescape(t: str) -> str:
    return t.replace(r"\{", "{").replace(r"\}", "}").replace(r"\*", "*")


def _intent_keys(d: dict, warnings: list[str], where: str) -> dict:
    out = {}
    for k, v in d.items():
        if k in _INTENT_KEYS:
            out[k] = v
        elif k != "pause":
            warnings.append(f"{where}: unknown directive key '{k}' (ignored)")
    return out


# ---- compile ----------------------------------------------------------------

def compile_text(
    text: str,
    *,
    config: dict | None = None,
    lexicon: Lexicon | None = None,
    profiles: VoiceProfiles | None = None,
    voice_override: str | None = None,
    max_chars: int = DEFAULT_MAX_CHARS,
) -> tuple[EpisodeIR, list[str]]:
    """Compile transcript text into an ``EpisodeIR``. Returns (ir, warnings)."""
    profiles = profiles or VoiceProfiles.load()
    lexicon = lexicon or Lexicon({})
    config = config or {}
    warnings: list[str] = []

    fm, body = split_front_matter(text)
    body = _COMMENT.sub("", body)

    defaults = fm.get("defaults")
    if not isinstance(defaults, dict):
        defaults = {}
    default_intent = {
        # SPEC allows a numeric rate multiplier in front-matter defaults; Intent.rate is a
        # str and pydantic v2 won't coerce float->str, so stringify (None -> "normal").
        "tone": str(defaults.get("tone", "measured")),
        "rate": str(defaults.get("rate") or "normal"),
        "note": defaults.get("note"),
    }
    voice = voice_override or fm.get("voice") or config.get("voice") or ""
    seed = fm.get("seed", config.get("seed"))

    # Two-host mode: front-matter `speakers:` maps @tag -> voice id (SPEC sec 8).
    # The first declared speaker is the per-beat default; absent a map it is
    # "narrator". @tags are validated against the map (unknown -> warn).
    speakers_map = fm.get("speakers") or {}
    if not isinstance(speakers_map, dict):
        speakers_map = {}
    default_speaker = next(iter(speakers_map), "narrator")

    paragraph_ms, beat_ms = profiles.paragraph_ms, profiles.beat_ms
    fmp = fm.get("pauses")
    if not isinstance(fmp, dict):
        fmp = {}
    if "paragraph" in fmp:
        paragraph_ms = int(float(fmp["paragraph"]) * 1000)
    if "beat" in fmp:
        beat_ms = int(float(fmp["beat"]) * 1000)

    segments: list[Segment] = []
    state = {"seg_id": 0, "pending": 0}

    def emit(buf, emph, intent, speaker, bi, title):
        authored = " ".join("".join(buf).split())
        if not authored:
            return
        spoken = lexicon.apply(normalize_text(authored))
        chunks = chunk_text(spoken, max_chars)
        # De-respelled per-chunk reference for the render STT gate (see Segment docs).
        # Only carried when a respelling was actually applied here — otherwise it would
        # duplicate `chunks` verbatim and bloat the IR.
        score_chunks = [lexicon.reverse(c) for c in chunks]
        if score_chunks == chunks:
            score_chunks = []
        segments.append(
            Segment(
                id=state["seg_id"],
                beat_index=bi,
                beat_title=title,
                speaker=speaker,
                intent=Intent(tone=intent["tone"], rate=intent["rate"], note=intent.get("note")),
                pause_before_ms=int(state["pending"]),
                authored_text=authored,
                spoken_text=spoken,
                emphasis=list(emph),
                chunks=chunks,
                score_chunks=score_chunks,
            )
        )
        state["seg_id"] += 1
        state["pending"] = 0

    for bi, (title, bdir, bbody) in enumerate(split_beats(body)):
        cur_intent = {**default_intent, **_intent_keys(bdir, warnings, f"beat {bi} '{title}'")}
        speaker = default_speaker
        if bi > 0:
            state["pending"] = max(state["pending"], beat_ms)
        buf: list[str] = []
        emph: list[str] = []
        pos = 0
        for m in _TOKEN.finditer(bbody):
            buf.append(_unescape(bbody[pos:m.start()]))
            kind = m.lastgroup
            if kind == "para":
                emit(buf, emph, cur_intent, speaker, bi, title)
                buf, emph = [], []
                state["pending"] = max(state["pending"], paragraph_ms)
            elif kind == "speaker":
                emit(buf, emph, cur_intent, speaker, bi, title)
                buf, emph = [], []
                speaker = m.group()[1:]
                if speakers_map and speaker not in speakers_map:
                    warnings.append(
                        f"beat {bi}: speaker '@{speaker}' is not declared in "
                        f"front-matter speakers: {sorted(speakers_map)}"
                    )
            elif kind == "directive":
                d = parse_directives(m.group()[1:-1])
                emit(buf, emph, cur_intent, speaker, bi, title)
                buf, emph = [], []
                if "pause" in d:
                    try:
                        state["pending"] = max(state["pending"], int(float(d["pause"]) * 1000))
                    except ValueError:
                        warnings.append(f"beat {bi}: bad pause value {d['pause']!r}")
                cur_intent = {**cur_intent, **_intent_keys(d, warnings, f"beat {bi} inline")}
            elif kind == "emph":
                phrase = _unescape(m.group().strip("*"))  # handles both ** and *
                buf.append(phrase)
                emph.append(phrase)
            pos = m.end()
        buf.append(_unescape(bbody[pos:]))
        emit(buf, emph, cur_intent, speaker, bi, title)

    ir = EpisodeIR(
        episode=fm.get("episode"),
        title=fm.get("title"),
        voice=voice,
        seed=seed,
        segments=segments,
    )
    return ir, warnings


def compile_file(path: str | Path, **kwargs) -> tuple[EpisodeIR, list[str]]:
    return compile_text(Path(path).read_text(encoding="utf-8"), **kwargs)


def compile_with_plan(text: str, **kwargs) -> tuple[EpisodeIR, RenderPlan, list[str]]:
    """Compile to IR and also produce the derived Chatterbox RenderPlan."""
    profiles = kwargs.get("profiles") or VoiceProfiles.load()
    kwargs["profiles"] = profiles
    ir, warns = compile_text(text, **kwargs)
    plan, plan_warns = build_render_plan(ir, profiles)
    return ir, plan, warns + plan_warns
