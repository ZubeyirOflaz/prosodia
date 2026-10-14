"""Compile a transcript (``formats/SPEC.md``) into the IR.

Parsing implements the repair items:
* front-matter is ONLY the leading ``---`` fence (D2); later ``---`` lines are
  treated as non-spoken thematic breaks;
* a beat's directives are the *trailing* ``{...}`` group on its ``##`` header (D3);
* directive parsing is quote-aware, so commas/colons inside a quoted value are
  safe (D1).

Segmentation: a ``Segment`` is a contiguous run of speech with a single intent. It ends
where the delivery changes (a tone/rate/note directive that changes something, a speaker
tag, a quotation's edges) and at a beat boundary; a pause there becomes the next segment's
``pause_before_ms``. A paragraph break or ``{pause: N}`` INSIDE the run is an inner pause
(``Segment.chunk_pauses``), and the spoken text before it is given a comma if it has no
punctuation, so the engine voices "more to come" and the renderer has a gap to stretch.
``spoken_text`` is normalized and lexicon-respelled; ``authored_text`` is kept for provenance.

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
from prosodia.core.ir import EpisodeIR, InnerPause, RenderPlan, Segment

_COMMENT = re.compile(r"<!--.*?-->", re.S)
_H1 = re.compile(r"^#\s+")
_H2 = re.compile(r"^##\s+")
_HN = re.compile(r"^#{3,}\s+")
_THEMATIC = re.compile(r"^\s*([-*_])\1{2,}\s*$")
_BEAT_HDR = re.compile(r"^##\s+(.*?)(?:\s*\{([^{}]*)\})?\s*$")
# A blockquote is a QUOTATION SPAN (SPEC §4.4): the compiler brackets each run of `>` lines
# with these two sentinels, and the token loop turns them into "switch to the quoting delivery"
# and "restore whatever was in force before it". The scope is the syntax itself, so the quoting
# voice cannot leak past the quotation the way a sticky `{tone: quoting}` directive did — in
# seven beats of The Collisions it carried on through ~2,200 words of the narrator's own gloss.
_QOPEN, _QCLOSE = "\x02", "\x03"
_BLOCKQUOTE = re.compile(r"(?m)(?:^[ \t]*>[^\n]*(?:\n|$))+")
_QUOTE_INTENT = {"tone": "quoting", "rate": "slow"}
_TOKEN = re.compile(
    r"(?P<qopen>\x02)|(?P<qclose>\x03)"
    r"|(?P<para>\n[ \t]*\n)"
    r"|(?P<speaker>(?<![^\n])@[A-Za-z0-9_]+)"
    r"|(?P<directive>(?<!\\)\{[^{}]*\})"
    # Emphasis: any asterisk fence — *emph*, **strong**, ***both***. All fence asterisks
    # are stripped so none leak into spoken_text; writers reach for **bold**/***x*** and a
    # fixed-count rule left literal '*' in the audio. (?<!\\) keeps escaped \* literal.
    # The span may cross a single newline — an emphasised phrase that happened to wrap in
    # the source used to fall through and put a literal '*' in front of the engine — but
    # never a blank line, which is the paragraph delimiter.
    r"|(?P<emph>(?<!\\)\*+(?:[^*\n]|\n(?![ \t]*\n))+\*+)"
    # Underscore emphasis was not handled at all, so _like this_ reached spoken_text with
    # its underscores. Guarded on both sides so snake_case words are left alone.
    r"|(?P<uemph>(?<!\\)(?<![\w])_+(?:[^_\n]|\n(?![ \t]*\n))+_+(?![\w]))"
)
_INTENT_KEYS = {"tone", "rate", "note"}
# An inner pause in the token buffer: the run continues, with ``ms`` of silence at this point.
_PAUSE = "\x01"
# Spoken text that already ends on punctuation (closing quotes/brackets allowed after it).
_BOUNDARY_END = re.compile(r"[,;:.!?…—–-][\"'”’)\]]*$")


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


def _mark_blockquotes(body: str, *, scoped: bool) -> str:
    """Strip blockquote markers; when ``scoped``, bracket each blockquote as a quotation span.

    ``scoped`` is true only for a persona whose voice profile defines a ``quoting`` tone.
    Elsewhere a blockquote is plain text, exactly as before.
    """
    def repl(m: re.Match) -> str:
        inner = re.sub(r"(?m)^[ \t]*>[ \t]?", "", m.group(0)).strip()
        return f"\n\n{_QOPEN}\n\n{inner}\n\n{_QCLOSE}\n\n" if scoped else f"{inner}\n"
    return _BLOCKQUOTE.sub(repl, body)


def _unescape(t: str) -> str:
    return t.replace(r"\{", "{").replace(r"\}", "}").replace(r"\*", "*").replace(r"\_", "_")


def _place_pauses(spoken: str, chunks: list[str], after_words: list[tuple[int, int]]) -> list[list[InnerPause]]:
    """Map pauses at global word counts of ``spoken`` onto (chunk, word count within it).

    Chunks are whole words of ``spoken`` in order, except that a soft split may drop a bare
    dash token, so tokens are matched rather than counted.
    """
    gtok = spoken.split()
    owners: list[list[int]] = []
    g = 0
    for c in chunks:
        idx = []
        for tok in c.split():
            while g < len(gtok) and gtok[g] != tok:
                g += 1
            idx.append(g)
            g += 1
        owners.append(idx)
    out: list[list[InnerPause]] = [[] for _ in chunks]
    for after, ms in after_words:
        last = after - 1  # global index of the word the pause follows
        ci = max((i for i, idx in enumerate(owners) if idx and idx[0] <= last), default=None)
        if ci is None:
            continue
        local = sum(1 for x in owners[ci] if x <= last)
        if local:
            out[ci].append(InnerPause(after_word=local, ms=ms))
    return out


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

    def emit(buf, emph, pauses, intent, speaker, bi, title):
        # Split the run at its inner pauses: (text, pause after it). A pause with no words
        # before it belongs to this segment's start, one with none after it to the next's.
        runs: list[list] = []
        lead = 0
        for i, piece in enumerate("".join(buf).split(_PAUSE)):
            text = " ".join(piece.split())
            after = pauses[i] if i < len(pauses) else 0
            if text:
                runs.append([text, after])
            elif runs:
                runs[-1][1] = max(runs[-1][1], after)
            else:
                lead = max(lead, after)
        state["pending"] = max(state["pending"], lead)
        if not runs:
            return
        trailing, runs[-1][1] = runs[-1][1], 0
        authored = " ".join(t for t, _ in runs)
        pieces = [lexicon.apply(normalize_text(t)) for t, _ in runs]
        after_words: list[tuple[int, int]] = []
        count = 0
        for k, (piece, (_, ms)) in enumerate(zip(pieces, runs)):
            if ms and not _BOUNDARY_END.search(piece):
                pieces[k] = piece = piece + ","  # spoken text only: "more to come"
            count += len(piece.split())
            if ms:
                after_words.append((count, ms))
        spoken = " ".join(pieces)
        chunks = chunk_text(spoken, max_chars)
        chunk_pauses = _place_pauses(spoken, chunks, after_words) if after_words else []
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
                chunk_pauses=chunk_pauses if any(chunk_pauses) else [],
            )
        )
        state["seg_id"] += 1
        state["pending"] = trailing

    for bi, (title, bdir, bbody) in enumerate(split_beats(body)):
        # A line-leading '>' is a markdown blockquote. It must never reach the engine — eight
        # segments of quoted statute in The Collisions went to render starting with "> " — and
        # for a persona with a `quoting` tone it marks the quotation's scope (see _QOPEN).
        bbody = _mark_blockquotes(bbody, scoped="quoting" in profiles.known_tones())
        saved_intent: dict | None = None
        cur_intent = {**default_intent, **_intent_keys(bdir, warnings, f"beat {bi} '{title}'")}
        speaker = default_speaker
        if bi > 0:
            state["pending"] = max(state["pending"], beat_ms)
        buf: list[str] = []
        emph: list[str] = []
        pauses: list[int] = []  # one per _PAUSE marker in buf
        pos = 0
        for m in _TOKEN.finditer(bbody):
            buf.append(_unescape(bbody[pos:m.start()]))
            kind = m.lastgroup
            if kind == "qopen":
                emit(buf, emph, pauses, cur_intent, speaker, bi, title)
                buf, emph, pauses = [], [], []
                saved_intent, cur_intent = cur_intent, {**cur_intent, **_QUOTE_INTENT}
            elif kind == "qclose":
                emit(buf, emph, pauses, cur_intent, speaker, bi, title)
                buf, emph, pauses = [], [], []
                if saved_intent is not None:
                    cur_intent, saved_intent = saved_intent, None
            elif kind == "para":
                buf.append(_PAUSE)
                pauses.append(paragraph_ms)
            elif kind == "speaker":
                emit(buf, emph, pauses, cur_intent, speaker, bi, title)
                buf, emph, pauses = [], [], []
                speaker = m.group()[1:]
                if speakers_map and speaker not in speakers_map:
                    warnings.append(
                        f"beat {bi}: speaker '@{speaker}' is not declared in "
                        f"front-matter speakers: {sorted(speakers_map)}"
                    )
            elif kind == "directive":
                d = parse_directives(m.group()[1:-1])
                new_intent = {**cur_intent, **_intent_keys(d, warnings, f"beat {bi} inline")}
                pause_ms = None
                if "pause" in d:
                    try:
                        pause_ms = int(float(d["pause"]) * 1000)
                    except ValueError:
                        warnings.append(f"beat {bi}: bad pause value {d['pause']!r}")
                if new_intent != cur_intent:
                    # The delivery changes: a new generation, and any pause goes before it.
                    emit(buf, emph, pauses, cur_intent, speaker, bi, title)
                    buf, emph, pauses = [], [], []
                    cur_intent = new_intent
                    if pause_ms is not None:
                        state["pending"] = max(state["pending"], pause_ms)
                elif pause_ms is not None:
                    buf.append(_PAUSE)
                    pauses.append(pause_ms)
            elif kind in ("emph", "uemph"):
                phrase = _unescape(m.group().strip("*_"))  # handles **strong**, *emph*, _emph_
                buf.append(phrase)
                emph.append(phrase)
            pos = m.end()
        buf.append(_unescape(bbody[pos:]))
        emit(buf, emph, pauses, cur_intent, speaker, bi, title)

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
