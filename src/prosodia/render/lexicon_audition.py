"""Lexicon audition — hear each respelling in the chosen voice, across seeds.

A pronunciation respelling (``Thucydides -> "Thoo-sid-ih-deez"``) is only a HINT to a
neural TTS with no phoneme API, not a hard spec: the model honors it probabilistically,
and every occurrence in a real episode is an independent generation, so the same name
can come out right in one place and wrong in another. This tool surfaces that directly —
it renders each lexicon entry inside a short carrier sentence across N seeds, so you can
hear whether a respelling is STABLE (comes out the same, correct way every time) or not,
and A/B it against the raw name and against alternative respellings you want to try.

Workflow: audition -> keep the respellings that render stably -> edit the lexicon ->
recompile. Runs on the GPU box (needs the render extra); a thin loop over the warm
backend plus the existing audio helpers, writing an ``index.html`` grouped by name.
"""

from __future__ import annotations

import html
from dataclasses import dataclass, field
from pathlib import Path

from prosodia.render import audio as A
from prosodia.render.audition import discover_clips

# A neutral carrier sentence; ``{}`` is where the name/respelling goes. A real sentence
# (not a bare token) gives realistic coarticulation and prosody.
DEFAULT_FRAME = "The place to begin is with {}, and the argument it started."


@dataclass
class Variant:
    label: str   # e.g. "as written", "lexicon", "variant 1"
    token: str   # the text actually spoken (raw name or a respelling)


@dataclass
class _Section:
    source: str
    caption: str                                    # the respelling(s) at a glance
    players: list[tuple[str, str]] = field(default_factory=list)  # (label, wav_name)


def expand_entries(
    entries: dict[str, str],
    *,
    names: "list[str] | None" = None,
    variants: "dict[str, list[str]] | None" = None,
    include_raw: bool = True,
) -> list[tuple[str, list[Variant]]]:
    """For each source name, the ordered list of Variants to render: the raw name
    (optional baseline), the lexicon respelling, then any extra candidate respellings.
    ``names`` filters to a subset; ``variants`` maps a source name to extra respellings
    to A/B. Names are kept in lexicon order; unknown filter names are ignored."""
    variants = variants or {}
    wanted = None if not names else {n for n in names}
    out: list[tuple[str, list[Variant]]] = []
    # Include any names present in `variants` even if absent from the lexicon (lets you
    # trial a respelling for a name you haven't added yet).
    ordered = list(entries) + [n for n in variants if n not in entries]
    for src in ordered:
        if wanted is not None and src not in wanted:
            continue
        vs: list[Variant] = []
        if include_raw:
            vs.append(Variant("as written", src))
        if src in entries:
            vs.append(Variant("lexicon", entries[src]))
        for i, extra in enumerate(variants.get(src, []), 1):
            vs.append(Variant(f"variant {i}", extra))
        if vs:
            out.append((src, vs))
    return out


def _index_html(sections: list[_Section], frame: str) -> str:
    blocks = []
    for s in sections:
        players = "".join(
            f'<div class="take"><span>{html.escape(label)}</span>'
            f'<audio controls preload="none" src="{html.escape(wav)}"></audio></div>'
            for label, wav in s.players
        )
        blocks.append(
            "<section>"
            f"<h2>{html.escape(s.source)}</h2>"
            f'<div class="cap">{html.escape(s.caption)}</div>'
            f"{players}</section>"
        )
    return (
        "<!doctype html><meta charset='utf-8'>"
        "<meta name=viewport content='width=device-width,initial-scale=1'>"
        "<title>Prosodia lexicon audition</title>"
        "<style>body{font:16px/1.6 -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;"
        "max-width:820px;margin:0 auto;padding:28px;background:#faf8f5;color:#1a1a1a}"
        "h1{font-size:20px;margin:0 0 4px}.lead{color:#6b6b6b;font-size:14px;margin:0 0 8px}"
        ".frame{font:13px/1.5 ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;color:#8a7d70;"
        "background:#fff;border-left:3px solid #7c4a2d;padding:8px 12px;border-radius:0 8px 8px 0;margin:8px 0 14px}"
        "section{border-top:1px solid #e6e3dd;padding:14px 0}h2{font-size:17px;margin:0 0 2px}"
        ".cap{color:#8a7d70;font-size:13px;margin:0 0 8px}"
        ".take{display:flex;align-items:center;gap:12px;margin:6px 0}"
        ".take span{width:170px;color:#6b6b6b;font-size:13px}audio{flex:1}</style>"
        "<h1>Lexicon audition — is each respelling stable?</h1>"
        "<p class=lead>Each name rendered across several seeds. A good respelling comes out the "
        "same, correct way every time; an unstable one drifts seed to seed — replace it.</p>"
        f"<div class=frame>carrier: {html.escape(frame)}</div>" + "".join(blocks)
    )


def _safe(name: str) -> str:
    return "".join(c if c.isalnum() else "-" for c in name).strip("-")[:40] or "name"


def lexicon_audition(
    voices,
    out_dir,
    *,
    lexicon_path=None,
    lexicon: "dict[str, str] | None" = None,
    names: "list[str] | None" = None,
    variants: "dict[str, list[str]] | None" = None,
    frame: str = DEFAULT_FRAME,
    include_raw: bool = True,
    backend=None,
    takes: int = 3,
    base_seed: int = 7000,
    target_lufs: float = -16.0,
) -> list[Path]:
    """Render every lexicon entry (raw name + respelling + any variants) across ``takes``
    seeds, for each clip in ``voices``, and write ``index.html`` grouped by name. Supply
    ``lexicon`` (a dict) or ``lexicon_path`` (a project ``lexicon.yaml``). Returns the
    written .wav paths."""
    if "{}" not in frame:
        raise ValueError("frame must contain a '{}' placeholder for the name")
    if lexicon is None:
        from prosodia.author.lexicon import Lexicon

        lexicon = Lexicon.load(Path(lexicon_path) if lexicon_path else None).entries
    plan = expand_entries(lexicon, names=names, variants=variants, include_raw=include_raw)
    if not plan:
        raise ValueError("no lexicon entries to audition (empty lexicon or names filter matched nothing)")

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

    n_takes = max(1, takes)
    written: list[Path] = []
    sections: list[_Section] = []
    for ni, (source, vs) in enumerate(plan):
        caption = " | ".join(f"{v.label}: {v.token}" for v in vs if v.label != "as written")
        section = _Section(source=source, caption=caption or "(raw name only)")
        for vi, v in enumerate(vs):
            text = frame.format(v.token)
            for ci, clip in enumerate(clips):
                for ti in range(n_takes):
                    seed = base_seed + ni * 1000 + vi * 100 + ti
                    wav = backend.generate(
                        text, exaggeration=0.5, cfg_weight=0.4, temperature=0.78,
                        seed=seed, audio_prompt_path=str(clip),
                    )
                    wav = A.trim_silence(wav, sr)
                    name = f"{ni:02d}_{_safe(source)}__{vi}_{_safe(v.label)}__{ci:02d}_{clip.stem}__seed{seed}.wav"
                    raw = out_dir / f"_raw_{name}"
                    A.write_wav(raw, wav, sr)
                    final = out_dir / name
                    if not A.loudness_normalize(raw, final, target_lufs, sr=sr):
                        A.write_wav(final, A.peak_normalize(wav), sr)
                    raw.unlink(missing_ok=True)
                    written.append(final)
                    clip_tag = f" · {clip.stem}" if len(clips) > 1 else ""
                    section.players.append((f"{v.label} · seed {seed}{clip_tag}", name))
        sections.append(section)

    (out_dir / "index.html").write_text(_index_html(sections, frame), encoding="utf-8")
    return written
