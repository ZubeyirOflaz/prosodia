"""Voice audition — render the SAME text with several reference clips, side by side.

Isolates the variation that comes from the *reference clip* by holding the written
content constant, so you can A/B candidate voices before committing to one. Runs on
the GPU box (needs the render extra); it's a thin loop over the warm ChatterboxBackend
plus the existing audio helpers, and writes an ``index.html`` with players for quick
comparison.
"""

from __future__ import annotations

import html
from pathlib import Path

from prosodia.render import audio as A

# A short, already-spoken-form narration sample (numbers spelled out) so the reference
# clip is the ONLY thing that changes between outputs.
DEFAULT_TEXT = (
    "Picture the continent in the spring of nineteen forty-five. Not a map — a smell. "
    "Brick dust and cordite, and something worse underneath it. They did not believe it "
    "was over; they believed it might happen again."
)


def discover_clips(voices) -> list[Path]:
    """Resolve ``voices`` (a dir of ``*.wav``, or a list of files/dirs) to clip paths."""
    items = [voices] if isinstance(voices, (str, Path)) else list(voices)
    clips: list[Path] = []
    for v in items:
        p = Path(v)
        if p.is_dir():
            clips += sorted(p.glob("*.wav"))
        elif p.exists():
            clips.append(p)
    seen: set[Path] = set()
    out: list[Path] = []
    for c in clips:  # de-dupe, preserve order
        if c not in seen:
            seen.add(c)
            out.append(c)
    return out


def _index_html(text: str, rows: list[tuple[str, list[str]]]) -> str:
    """Rows are (clip_name, [wav_filenames]); build a self-contained A/B player."""
    blocks = []
    for name, files in rows:
        players = "".join(
            f'<div class="take"><span>{html.escape(Path(f).stem)}</span>'
            f'<audio controls preload="none" src="{html.escape(f)}"></audio></div>'
            for f in files
        )
        blocks.append(f"<section><h2>{html.escape(name)}</h2>{players}</section>")
    return (
        "<!doctype html><meta charset='utf-8'>"
        "<meta name=viewport content='width=device-width,initial-scale=1'>"
        "<title>Prosodia voice audition</title>"
        "<style>body{font:16px/1.6 -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;"
        "max-width:760px;margin:0 auto;padding:28px;background:#faf8f5;color:#1a1a1a}"
        "h1{font-size:20px}.txt{background:#fff;border-left:3px solid #7c4a2d;padding:10px 14px;"
        "border-radius:0 8px 8px 0;margin:14px 0}section{border-top:1px solid #e6e3dd;padding:14px 0}"
        "h2{font-size:16px;margin:0 0 8px}.take{display:flex;align-items:center;gap:12px;margin:6px 0}"
        ".take span{width:150px;color:#6b6b6b;font-size:13px}audio{flex:1}</style>"
        "<h1>Voice audition — same text, different reference clips</h1>"
        f"<div class=txt>{html.escape(text)}</div>" + "".join(blocks)
    )


def audition(
    text: str,
    voices,
    out_dir,
    *,
    backend=None,
    takes: int = 2,
    base_seed: int = 12345,
    exaggeration: float = 0.4,
    cfg_weight: float = 0.45,
    temperature: float = 0.75,
    target_lufs: float = -16.0,
) -> list[Path]:
    """Render ``text`` with each clip in ``voices`` — ``takes`` per clip, with seeds
    matched across clips so the clip is the only variable at each take index (extra
    takes also reveal seed-to-seed variance). Writes one .wav per take + ``index.html``.
    Returns the written .wav paths."""
    clips = discover_clips(voices)
    if not clips:
        raise ValueError("no reference .wav clips found in the given path(s)")
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    if backend is None:
        from prosodia.render.backends.chatterbox_backend import ChatterboxBackend

        backend = ChatterboxBackend()
    backend.load()
    sr = backend.sample_rate

    seeds = [base_seed + k for k in range(max(1, takes))]
    written: list[Path] = []
    rows: list[tuple[str, list[str]]] = []
    for clip in clips:
        files: list[str] = []
        for seed in seeds:
            wav = backend.generate(
                text, exaggeration=exaggeration, cfg_weight=cfg_weight,
                temperature=temperature, seed=seed, audio_prompt_path=str(clip),
            )
            wav = A.trim_silence(wav, sr)
            name = f"{clip.stem}__seed{seed}.wav"
            raw = out_dir / f"_raw_{name}"
            A.write_wav(raw, wav, sr)
            final = out_dir / name
            if not A.loudness_normalize(raw, final, target_lufs):
                A.write_wav(final, A.peak_normalize(wav), sr)
            raw.unlink(missing_ok=True)
            written.append(final)
            files.append(name)
        rows.append((clip.name, files))

    (out_dir / "index.html").write_text(_index_html(text, rows), encoding="utf-8")
    return written
