"""Render a job (IR + render_plan) to an episode audio file on the GPU box.

The render loop is a simple, deterministic function of the IR + render plan:
for each segment, emit ``pause_before_ms`` of real silence, then render each
~300-char chunk with the Tone-specialist's params, quality-gate it (unless in
fast-preview mode), trim and crossfade-join, and finally loudness-normalize the
whole episode ONCE.

Fast-preview mode (default): 1 candidate per chunk, no STT validation — fast, for
finding common failures. Final mode: N candidates + faster-whisper validation,
keep the best.
"""

from __future__ import annotations

import logging
from pathlib import Path

import numpy as np

from prosodia.core.ir import EpisodeIR, RenderPlan
from prosodia.render import audio as A

logger = logging.getLogger(__name__)

DEFAULT_CANDIDATES = 2
SIM_THRESHOLD = 0.85
# Shared fallback params (mirrors tone.py's _FALLBACK) used only when a segment id
# is genuinely absent from the plan; that is a contract violation, so we also warn.
_FALLBACK = (0.40, 0.50, 0.75, 1.0)


def _resolve_voice_ref(ir: EpisodeIR, job_dir: Path, voices_dir: str | None) -> str | None:
    """A bundled voice clip in the job wins; else voices_dir/<voice>.wav; else None.

    A ``preset:`` voice cannot be resolved to a reference clip here; we warn so the
    request is not silently downgraded to Chatterbox's built-in default (the
    backend will also refuse a preset it is handed).
    """
    for p in sorted(Path(job_dir).glob("*.wav")):
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


def _render_chunk(backend, text, params, base_seed, seg_id, ci, ref, *,
                  fast_preview, candidates, validator, sr, voice=None) -> np.ndarray:
    n = 1 if fast_preview else max(1, candidates)
    best: np.ndarray | None = None
    best_score = -1.0
    for k in range(n):
        seed = None if base_seed is None else int(base_seed) + seg_id * 1000 + ci * 10 + k
        try:
            wav = backend.generate(
                text,
                exaggeration=params[0],
                cfg_weight=params[1],
                temperature=params[2],
                rate_multiplier=params[3],
                seed=seed,
                audio_prompt_path=ref,
                voice=voice,
            )
        except Exception:
            continue
        if fast_preview or validator is None:
            return wav
        score = validator.score(wav, sr, text)
        if score > best_score:
            best, best_score = wav, score
        if score >= SIM_THRESHOLD:
            break
    return best if best is not None else np.zeros(0, dtype=np.float32)


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
    ref = _resolve_voice_ref(ir, job_dir, voices_dir)
    if validator is None and not fast_preview:
        from prosodia.render.quality import WhisperValidator

        validator = WhisperValidator()

    out = np.zeros(0, dtype=np.float32)
    total = max(1, len(ir.segments))
    for i, seg in enumerate(ir.segments):
        just_paused = seg.pause_before_ms > 0
        if just_paused:
            out = np.concatenate([out, A.silence(seg.pause_before_ms, sr)])
        p = params.get(seg.id)
        if p is None:  # plan/IR drift — a real contract violation, do not hide it.
            logger.warning(
                "segment %d has no SegmentParams in the render plan; using fallback %r",
                seg.id, _FALLBACK,
            )
            p = _FALLBACK
        for ci, chunk in enumerate(seg.chunks):
            wav = _render_chunk(
                backend, chunk, p, ir.seed, seg.id, ci, ref,
                fast_preview=fast_preview, candidates=candidates, validator=validator, sr=sr,
                # If a reference clip resolved, cloning wins; otherwise hand the
                # voice id to the backend so a preset request fails loudly.
                voice=None if ref else (ir.voice or None),
            )
            wav = A.trim_silence(wav, sr)
            if not out.size:
                out = wav
            elif just_paused:
                # Don't crossfade into freshly-inserted silence — the fade would
                # eat up to ~20 ms of every authored pause. Plain-concatenate the
                # first chunk after a pause so explicit {pause} durations stay exact.
                out = np.concatenate([out, wav])
            else:
                out = A.crossfade(out, wav, sr)
            just_paused = False  # only the first chunk follows the pause
        if on_progress:
            on_progress((i + 1) / total)

    out_path = Path(out_path)
    if not out_path.suffix:
        out_path = out_path.with_suffix(".wav")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    raw = out_path.with_suffix(".raw.wav")
    A.write_wav(raw, out, sr)
    if not A.loudness_normalize(raw, out_path, target_lufs):
        A.write_wav(out_path, A.peak_normalize(out), sr)  # fallback if ffmpeg missing
    raw.unlink(missing_ok=True)
    return out_path
