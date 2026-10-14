"""Render a job (IR + render_plan) to an episode audio file on the GPU box.

The render is a deterministic function of the IR + render plan, in two passes:
1. **Generate.** Each ~300-char chunk is rendered with the Tone-specialist's params,
   quality-gated (unless in fast-preview mode) and trimmed.
2. **Assemble.** Room tone is measured from all the generations; each chunk's inner pauses
   (IR ``chunk_pauses``) are spliced into it (``splice.py``); then chunks are joined —
   crossfaded where they run on, with room tone where a pause sits between them — and the
   whole episode is loudness-normalized ONCE. The lead-in and tail are digital silence.

Fast-preview mode (default): 1 candidate per chunk, no STT validation — fast, for
finding common failures. Final mode: N candidates + faster-whisper validation,
keep the best.
"""

from __future__ import annotations

import logging
import re
from pathlib import Path

import numpy as np

from prosodia.core.ir import EpisodeIR, RenderPlan, Segment
from prosodia.render import audio as A
from prosodia.render.splice import splice_pauses

logger = logging.getLogger(__name__)

DEFAULT_CANDIDATES = 2
SIM_THRESHOLD = 0.85
# Shared fallback params (mirrors tone.py's _FALLBACK) used only when a segment id
# is genuinely absent from the plan; that is a contract violation, so we also warn.
_FALLBACK = (0.40, 0.50, 0.75, 1.0)


def _resolve_voice_ref(
    ir: EpisodeIR, job_dir: Path, voices_dir: str | None, *, exclude: frozenset = frozenset()
) -> str | None:
    """A bundled voice clip in the job wins; else voices_dir/<voice>.wav; else None.

    A ``preset:`` voice cannot be resolved to a reference clip here; we warn so the
    request is not silently downgraded to Chatterbox's built-in default (the backend
    will also refuse a preset it is handed). Render outputs (``episode.wav``,
    ``*.raw.wav``) are skipped so a re-render never adopts its own previous output as
    the reference clip.
    """
    for p in sorted(Path(job_dir).glob("*.wav")):
        if p.name in exclude or p.name.endswith(".raw.wav"):
            continue
        return str(p)
    if voices_dir and ir.voice and not ir.voice.startswith("preset:"):
        cand = Path(voices_dir) / f"{ir.voice}.wav"
        if cand.exists():
            return str(cand)
    if ir.voice and ir.voice.startswith("preset:"):
        logger.warning(
            "voice %r requests a preset, which the Chatterbox backend cannot "
            "resolve to a reference clip; bundle a .wav to clone instead",
            ir.voice,
        )
    return None


_UNSAFE_IN_FILENAME = re.compile(r'[<>:"/\\|?*\x00-\x1f]')


def episode_filename(ir: EpisodeIR, ext: str = ".mp3") -> str:
    """``"7. The Science of Rise and Fall.mp3"`` — the name a listener's player shows.

    Characters Windows refuses in a filename are dropped (the render box runs Windows), as are
    trailing dots and spaces, which Windows silently strips and Syncthing then fights over.
    """
    title = (ir.title or "").strip()
    if ir.episode is not None and title:
        stem = f"{ir.episode}. {title}"
    else:
        stem = title or (f"Episode {ir.episode}" if ir.episode is not None else "episode")
    stem = _UNSAFE_IN_FILENAME.sub("", stem).strip().rstrip(". ")
    return (stem or "episode") + ext


def _render_chunk(backend, text, params, base_seed, seg_id, ci, ref, *,
                  fast_preview, candidates, validator, sr, voice=None,
                  score_text=None, fallback_texts: tuple[str, ...] = ()) -> tuple[np.ndarray, bool]:
    # ``text`` is what the engine SPEAKS first; ``score_text`` is what the STT gate compares
    # against (lexicon respellings mapped back to source spellings). They differ only for
    # chunks containing a respelled name — scoring against the respelling is exactly what
    # made the gate pick the WORSE, spelled-out pronunciation. Default to ``text`` when no
    # score reference is supplied (no lexicon token in this chunk).
    #
    # ``fallback_texts`` are alternate spellings to try, in order, ONLY when the current
    # spelling's best-of-N stays under SIM_THRESHOLD (see render_job's lexicon_fallback).
    # All spellings are scored against the same ``score_ref``, so the comparison is fair.
    # Returns (wav, fell_back) where fell_back is True when a fallback spelling won.
    n = 1 if fast_preview else max(1, candidates)
    score_ref = score_text if score_text is not None else text
    variants = (text, *fallback_texts)
    best: np.ndarray | None = None
    best_score = -1.0
    best_vi = 0
    last_exc: Exception | None = None
    for vi, variant in enumerate(variants):
        # Keep variant 0 on the original seed formula so flag-off renders stay
        # bit-identical; offset fallback variants far enough to avoid seed reuse.
        vbase = vi * 100000
        for k in range(n):
            seed = None if base_seed is None else int(base_seed) + vbase + seg_id * 1000 + ci * 10 + k
            try:
                wav = backend.generate(
                    variant,
                    exaggeration=params[0],
                    cfg_weight=params[1],
                    temperature=params[2],
                    rate_multiplier=params[3],
                    seed=seed,
                    audio_prompt_path=ref,
                    voice=voice,
                )
            except Exception as exc:  # noqa: BLE001 - try the next candidate, but never silently
                last_exc = exc
                logger.warning("segment %d chunk %d variant %d candidate %d failed: %s", seg_id, ci, vi, k, exc)
                continue
            if fast_preview or validator is None:
                return wav, vi > 0
            score = validator.score(wav, sr, score_ref)
            if score > best_score:
                best, best_score, best_vi = wav, score, vi
            if score >= SIM_THRESHOLD:
                return best, vi > 0
        # This spelling cleared nothing above threshold; escalate to the next fallback.
        if vi + 1 < len(variants):
            logger.info(
                "segment %d chunk %d: spelling %d best score %.2f < %.2f, trying fallback spelling",
                seg_id, ci, vi, max(best_score, 0.0), SIM_THRESHOLD,
            )
    if best is not None:
        return best, best_vi > 0
    # Every candidate failed. Returning np.zeros() here would splice SILENCE into the
    # episode and still let the job be marked "done" — fail loudly so it's quarantined.
    raise RuntimeError(
        f"segment {seg_id} chunk {ci}: all {n * len(variants)} generation attempt(s) failed"
        + (f" — {last_exc}" if last_exc is not None else "")
    )


def _remap_after_word(after: int, src: str, dst: str) -> int:
    """Carry a pause position from the chunk text to the text actually spoken.

    They differ only when the lexicon fallback spoke the unrespelled name, and a respelling
    can change the word count. The pause follows punctuation, which both share, so count it.
    """
    s, d = src.split(), dst.split()
    if len(s) == len(d) or not d:
        return after
    nth = sum(1 for t in s[:after] if t[-1:] in ",;:.!?—–-")
    marks = [k for k, t in enumerate(d, start=1) if t[-1:] in ",;:.!?—–-"]
    if 0 < nth <= len(marks):
        return marks[nth - 1]
    return max(1, min(len(d), round(after * len(d) / len(s))))


def _chunk_pauses(seg: Segment, ci: int, spoken: str) -> tuple[list[tuple[int, int]], int]:
    """(pauses inside the chunk as (after_word, ms) in ``spoken``'s words, pause after it)."""
    if ci >= len(seg.chunk_pauses):
        return [], 0
    n = len(seg.chunks[ci].split())
    inner, tail = [], 0
    for p in seg.chunk_pauses[ci]:
        if p.after_word >= n:
            tail = max(tail, p.ms)
        else:
            inner.append((_remap_after_word(p.after_word, seg.chunks[ci], spoken), p.ms))
    return inner, tail


def render_job(
    job_dir: str | Path,
    out_path: str | Path,
    *,
    backend=None,
    fast_preview: bool = True,
    voices_dir: str | None = None,
    candidates: int = DEFAULT_CANDIDATES,
    target_lufs: float = -16.0,
    validator=None,
    on_progress=None,
    edge_silence_ms: int = 4000,
    speak_title: bool = True,
    title_gap_ms: int = 1000,
    lexicon_fallback: bool = True,
) -> Path:
    job_dir = Path(job_dir)
    ir = EpisodeIR.from_json((job_dir / "ir.json").read_text(encoding="utf-8"))
    plan = RenderPlan.from_json((job_dir / "render_plan.json").read_text(encoding="utf-8"))
    params = {
        p.segment_id: (p.exaggeration, p.cfg_weight, p.temperature, p.rate_multiplier)
        for p in plan.params
    }

    if backend is None:
        from prosodia.render.backends.chatterbox_backend import ChatterboxBackend

        backend = ChatterboxBackend()
    backend.load()
    sr = backend.sample_rate
    out_path = Path(out_path)
    if out_path.is_dir():
        # Given the job folder: write the listener-facing file, "N. Title.mp3".
        out_path = out_path / episode_filename(ir)
    elif not out_path.suffix:
        out_path = out_path.with_suffix(".wav")
    ref = _resolve_voice_ref(
        ir, job_dir, voices_dir,
        exclude=frozenset({out_path.name, out_path.with_suffix(".raw.wav").name}),
    )
    if validator is None and not fast_preview:
        from prosodia.render.quality import WhisperValidator

        validator = WhisperValidator()

    # Pass 1 — generate. `pieces` is the episode in order: ("gap", ms) and
    # ("audio", wav, spoken_text, inner_pauses).
    pieces: list[tuple] = []
    total = max(1, len(ir.segments))
    fb_covered = 0  # respelled chunks eligible for the unassisted-first fallback
    fb_used = 0     # ... of those, how many actually needed the respelling
    for i, seg in enumerate(ir.segments):
        if seg.pause_before_ms > 0:
            pieces.append(("gap", seg.pause_before_ms))
        p = params.get(seg.id)
        if p is None:  # plan/IR drift — a real contract violation, do not hide it.
            logger.warning(
                "segment %d has no SegmentParams in the render plan; using fallback %r",
                seg.id, _FALLBACK,
            )
            p = _FALLBACK
        for ci, chunk in enumerate(seg.chunks):
            # De-respelled reference for the STT gate, when this segment carries one.
            score_text = seg.score_chunks[ci] if ci < len(seg.score_chunks) else None
            # lexicon_fallback (final mode only): speak the UNASSISTED name first (the
            # de-respelled score_text), and only fall back to the respelled ``chunk`` if
            # the unassisted take fails the gate. Both are scored against score_text.
            use_fb = lexicon_fallback and not fast_preview and score_text is not None
            if use_fb:
                primary, fallbacks = score_text, (chunk,)
                fb_covered += 1
            else:
                primary, fallbacks = chunk, ()
            wav, fell_back = _render_chunk(
                backend, primary, p, ir.seed, seg.id, ci, ref,
                fast_preview=fast_preview, candidates=candidates, validator=validator, sr=sr,
                # If a reference clip resolved, cloning wins; otherwise hand the
                # voice id to the backend so a preset request fails loudly.
                voice=None if ref else (ir.voice or None),
                score_text=score_text, fallback_texts=fallbacks,
            )
            if use_fb and fell_back:
                fb_used += 1
            spoken = chunk if (fell_back or not use_fb) else primary
            inner, tail = _chunk_pauses(seg, ci, spoken)
            pieces.append(("audio", A.trim_silence(wav, sr), spoken, inner))
            if tail:
                pieces.append(("gap", tail))
        if on_progress:
            on_progress((i + 1) / total)

    if fb_covered:
        logger.info(
            "lexicon fallback: %d/%d respelled chunk(s) needed the respelling "
            "(the rest rendered fine unassisted)", fb_used, fb_covered,
        )

    # Pass 2 — assemble: room tone from the generations themselves, inner pauses spliced in,
    # chunks joined (crossfaded when they run on; room tone where a pause sits between them).
    room = A.RoomTone.estimate([pc[1] for pc in pieces if pc[0] == "audio"], sr,
                               seed=0 if ir.seed is None else int(ir.seed))
    xf_ms = 10
    xf = int(sr * xf_ms / 1000)

    def gap(ms: int) -> np.ndarray:  # a pause, plus the two crossfades it is joined with
        return room(int(sr * ms / 1000) + 2 * xf)

    out = np.zeros(0, dtype=np.float32)
    pending = 0
    spliced = missed = 0
    for pc in pieces:
        if pc[0] == "gap":
            pending = max(pending, pc[1])
            continue
        _, wav, spoken, inner = pc
        if inner:
            wav, rep = splice_pauses(wav, sr, spoken, inner, room, xfade_ms=xf_ms)
            spliced, missed = spliced + rep.spliced, missed + rep.missed
            for note in rep.notes or []:
                logger.debug("%s: %s", spoken[:40], note)
        if not out.size:
            out = A.crossfade(room(int(sr * pending / 1000) + xf), wav, sr, xf_ms) if pending else wav
        elif pending:
            out = A.join_with_gap(out, gap(pending), wav, sr, xf_ms)
        else:
            out = A.crossfade(out, wav, sr)
        pending = 0
    if spliced or missed:
        logger.info("inner pauses: %d spliced into their generation, %d left at the engine's own "
                    "length (no gap found)", spliced, missed)

    # QoL: speak the episode title at the top (best-effort — a title glitch must never
    # fail an otherwise-good render), then bookend the whole thing with lead/tail silence
    # so it doesn't start or end abruptly.
    intro = np.zeros(0, dtype=np.float32)
    if speak_title and ir.title:
        tparams = (params.get(ir.segments[0].id) if ir.segments else None) or _FALLBACK
        try:
            tw, _ = _render_chunk(
                backend, ir.title, tparams, ir.seed, -1, 0, ref,
                fast_preview=fast_preview, candidates=candidates, validator=None, sr=sr,
                voice=None if ref else (ir.voice or None),
            )
            tw = A.trim_silence(tw, sr)
            if tw.size:
                intro = tw
        except Exception as exc:  # noqa: BLE001 - the title is a nicety, not worth aborting for
            logger.warning("could not render episode title %r: %s", ir.title, exc)
    if intro.size and out.size:
        out = A.join_with_gap(intro, gap(title_gap_ms), out, sr, xf_ms)
    elif intro.size:
        out = intro
    # The lead-in and tail stay DIGITAL silence. The final loudnorm is single-pass, so it sets
    # its gain over a few seconds at a time: with no speech in that window it raised a room-tone
    # lead-in by ~33 dB, to nearly the level of the speech (2026-10-14, Series B findings §6).
    fade = np.linspace(0.0, 1.0, min(xf, out.size // 2), dtype=np.float32)
    if fade.size:  # no click where the episode meets the silence
        out = out.copy()
        out[: fade.size] *= fade
        out[-fade.size:] *= fade[::-1]
    edge = A.silence(edge_silence_ms, sr)
    out = np.concatenate([edge, out, edge])

    out_path.parent.mkdir(parents=True, exist_ok=True)
    raw = out_path.with_suffix(".raw.wav")
    A.write_wav(raw, out, sr)
    tags = {"title": ir.title, "track": ir.episode}
    if not A.finalize_audio(raw, out_path, target_lufs, sr=sr, tempo=plan.tempo, tags=tags):
        # ffmpeg missing or failed: no tempo, no MP3. Keep a playable, normalized WAV rather than
        # fail the job, and say so — the episode is then at the engine's raw ~170 wpm.
        fallback = out_path.with_suffix(".wav")
        logger.warning("ffmpeg finishing pass failed; wrote %s WITHOUT tempo %.2f", fallback.name, plan.tempo)
        A.write_wav(fallback, A.peak_normalize(out), sr)
        out_path = fallback
    raw.unlink(missing_ok=True)
    return out_path
