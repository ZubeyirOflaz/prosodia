"""Command-line entry point for the rendering side (``prosodia-render``).

Requires the ``render`` extra (torch + Chatterbox) and ffmpeg on PATH. A GPU is
preferred but no longer mandatory: with none available the renderer falls back
to CPU (slower, but it produces identical output). Heavy imports are deferred so
a base, torch-free install fails with a helpful message instead of an opaque
ImportError. ``doctor`` reports what's missing and which device will be used.
"""

from __future__ import annotations

import argparse
import os
import shutil
import sys
from pathlib import Path


def _ffmpeg_hint() -> str:
    if sys.platform == "win32":
        return "install with `winget install Gyan.FFmpeg`"
    if sys.platform == "darwin":
        return "install with `brew install ffmpeg`"
    return "install with your package manager, e.g. `sudo dnf install ffmpeg` / `sudo apt install ffmpeg`"


def check_render_env() -> list[str]:
    """Return human-readable problems with the render environment (empty == OK).

    A missing GPU is NOT a problem — it is a performance note (see
    ``render_env_notes``). Only genuinely blocking conditions belong here.
    """
    problems: list[str] = []

    # 3.14 is fine: chatterbox-tts >= 0.1.7 declares torch >= 2.9 for it. The gate
    # exists only to catch a Python the TTS wheels genuinely do not build for yet.
    if sys.version_info >= (3, 15):
        problems.append(
            f"Python {sys.version_info.major}.{sys.version_info.minor} is newer than the "
            "TTS stack supports; use Python 3.11-3.14 on the render box."
        )

    try:
        import torch  # noqa: F401
    except Exception:
        problems.append(
            "PyTorch is not installed. Install the right wheel FIRST, then "
            "`pip install prosodia[render]` (see scripts/RENDERER_SETUP.md)."
        )

    try:
        import chatterbox  # noqa: F401  (provided by the chatterbox-tts package)
    except Exception:
        problems.append("chatterbox-tts is not installed (`pip install prosodia[render]`).")

    if shutil.which("ffmpeg") is None:
        problems.append(f"ffmpeg is not on PATH ({_ffmpeg_hint()}).")

    return problems


def render_env_notes() -> list[str]:
    """Non-blocking notes about the render environment (device choice, speed)."""
    notes: list[str] = []
    try:
        from prosodia.render.device import advice_for, describe_gpu, gpu_status, resolve_device
    except Exception:
        return notes

    device = resolve_device()
    forced = os.environ.get("PROSODIA_DEVICE")
    usable, reason = gpu_status()

    if forced:
        notes.append(f"device: {device} (forced by PROSODIA_DEVICE)")
    else:
        notes.append(f"device: {device} (auto)")
    notes.append(f"GPU: {describe_gpu()}" if usable else f"GPU unusable: {reason}")
    if device == "cpu":
        notes.append(
            "CPU rendering works but is far slower than a discrete GPU - expect "
            "roughly 3x realtime (3 s of compute per second of audio) on a modern "
            "8-core laptop, so budget hours per episode."
        )
    advice = advice_for(device)
    if advice:
        notes.append(f"note: {advice}")
    return notes


def build_parser() -> argparse.ArgumentParser:
    # Shared options, accepted either before or after the subcommand. SUPPRESS is
    # load-bearing: with a normal default the subparser parses last and would
    # clobber a value given before the subcommand with None.
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument(
        "--device", default=argparse.SUPPRESS,
        help="force the torch device ('cuda' or 'cpu'); default: auto-detect. "
             "Equivalent to setting PROSODIA_DEVICE.",
    )
    parser = argparse.ArgumentParser(
        prog="prosodia-render",
        parents=[common],
        description="Render Prosodia jobs to audio (Chatterbox); GPU if available, else CPU.",
    )
    sub = parser.add_subparsers(dest="command")
    sub.add_parser(
        "doctor", parents=[common],
        help="check the render environment (Python, torch, device, ffmpeg)",
    )

    p_render = sub.add_parser("render", parents=[common], help="render a single job directory")
    p_render.add_argument("job", help="path to a job directory (holds ir.json + render_plan.json)")
    p_render.add_argument("--final", action="store_true", help="final mode (N candidates + STT gate)")
    p_render.add_argument("--voices", help="directory of voice reference .wav files")
    p_render.add_argument("--no-title", action="store_true", help="don't speak the episode title at the start")
    p_render.add_argument(
        "--lexicon-fallback", action=argparse.BooleanOptionalAction, default=True,
        help="final mode only (default ON): speak each respelled name UNASSISTED first and "
             "fall back to the lexicon respelling only if the plain name fails the STT gate. "
             "Pass --no-lexicon-fallback to always speak the respelling instead.",
    )

    p_watch = sub.add_parser(
        "watch", parents=[common],
        help="watch an exchange root and render jobs as they arrive",
    )
    p_watch.add_argument("root", help="synced exchange root (holds inbox/ processing/ outbox/ failed/)")
    p_watch.add_argument("--final", action="store_true", help="final mode (N candidates + STT gate)")
    p_watch.add_argument("--voices", help="directory of voice reference .wav files")
    p_watch.add_argument("--interval", type=float, default=5.0, help="poll interval seconds")
    p_watch.add_argument("--once", action="store_true", help="process the current inbox once and exit")
    p_watch.add_argument("--no-title", action="store_true", help="don't speak the episode title at the start")
    p_watch.add_argument(
        "--lexicon-fallback", action=argparse.BooleanOptionalAction, default=True,
        help="final mode only (default ON): unassisted-first pronunciation with the respelling "
             "as a rescue (see `render`). Pass --no-lexicon-fallback to always speak the respelling.",
    )

    p_aud = sub.add_parser(
        "audition", parents=[common],
        help="A/B voice clips across the full delivery range (or a single custom text)",
    )
    p_aud.add_argument("--voices", nargs="+", required=True, help="a voices/ dir and/or .wav files to compare")
    p_aud.add_argument("--out", default="voice_audition", help="output directory (default: ./voice_audition)")
    p_aud.add_argument(
        "--text",
        help="single-passage mode: speak this one text instead of the built-in range suite",
    )
    p_aud.add_argument("--text-file", help="read the single-passage text from a file instead of --text")
    p_aud.add_argument("--tone", default="measured", help="tone for --text mode (default: measured)")
    p_aud.add_argument("--rate", default="normal", help="rate for --text mode (default: normal)")
    p_aud.add_argument(
        "--voice-profiles", "--persona", dest="voice_profiles",
        help="persona NAME (e.g. thinkers) or path to a voice_profiles.yaml whose tone table "
             "drives the params (default: the built-in persona's)",
    )
    p_aud.add_argument("--takes", type=int, default=1, help="takes per cell, seeds matched across clips (default 1)")
    p_aud.add_argument(
        "--exaggeration", type=float, default=None,
        help="override exaggeration for every passage (default: from the tone table)",
    )
    p_aud.add_argument(
        "--cfg", type=float, default=None, dest="cfg_weight",
        help="override cfg_weight for every passage (default: from the tone table)",
    )
    p_aud.add_argument(
        "--temperature", type=float, default=None,
        help="override temperature for every passage (default: from the tone table)",
    )

    p_lex = sub.add_parser(
        "lexicon-audition", parents=[common],
        help="hear each lexicon respelling across seeds to pick stable pronunciations",
    )
    p_lex.add_argument("--voices", nargs="+", required=True, help="a voices/ dir and/or .wav files")
    p_lex.add_argument("--lexicon", required=True, help="path to a project lexicon.yaml")
    p_lex.add_argument("--out", default="lexicon_audition", help="output directory (default: ./lexicon_audition)")
    p_lex.add_argument("--names", nargs="+", help="only audition these source names (default: all)")
    p_lex.add_argument(
        "--variants",
        help="YAML mapping {name: [respelling, ...]} of candidate respellings to A/B",
    )
    p_lex.add_argument("--frame", default=None, help="carrier sentence with a '{}' placeholder for the name")
    p_lex.add_argument("--takes", type=int, default=3, help="seeds per variant (default 3)")
    p_lex.add_argument("--no-raw", action="store_true", help="skip the raw-name baseline take")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if not args.command:
        parser.print_help()
        return 0

    if getattr(args, "device", None):
        os.environ["PROSODIA_DEVICE"] = args.device

    problems = check_render_env()
    if args.command == "doctor":
        if problems:
            print("Render environment problems:")
            for p in problems:
                print(f"  - {p}")
            return 1
        print("Render environment OK (Python, torch, chatterbox, ffmpeg).")
        for note in render_env_notes():
            print(f"  {note}")
        return 0

    if problems:
        print("Cannot run - environment not ready:", file=sys.stderr)
        for p in problems:
            print(f"  - {p}", file=sys.stderr)
        return 1

    if args.command == "render":
        from prosodia.render.render import render_job

        out = render_job(
            args.job, Path(args.job) / "episode.wav", fast_preview=not args.final,
            voices_dir=args.voices, speak_title=not args.no_title,
            lexicon_fallback=args.lexicon_fallback,
        )
        print(f"rendered -> {out}")
        return 0

    if args.command == "watch":
        from prosodia.render.watch_and_render import watch

        watch(
            args.root, interval=args.interval, fast_preview=not args.final,
            voices_dir=args.voices, once=args.once, speak_title=not args.no_title,
            lexicon_fallback=args.lexicon_fallback,
        )
        return 0

    if args.command == "audition":
        from prosodia.render.audition import audition

        # None => render the full built-in range suite; a value => single-passage mode.
        if args.text_file:
            text = Path(args.text_file).read_text(encoding="utf-8")
        else:
            text = args.text
        written = audition(
            args.voices, args.out, text=text, tone=args.tone, rate=args.rate,
            takes=args.takes, voice_profiles_path=args.voice_profiles,
            exaggeration=args.exaggeration, cfg_weight=args.cfg_weight, temperature=args.temperature,
        )
        mode = "custom text" if text is not None else "full range suite"
        print(f"rendered {len(written)} sample(s) ({mode}) -> {args.out}")
        print(f"open {Path(args.out) / 'index.html'} to A/B the voices")
        return 0

    if args.command == "lexicon-audition":
        import yaml

        from prosodia.render.lexicon_audition import DEFAULT_FRAME, lexicon_audition

        variants = None
        if args.variants:
            loaded = yaml.safe_load(Path(args.variants).read_text(encoding="utf-8")) or {}
            variants = loaded if isinstance(loaded, dict) else None
        written = lexicon_audition(
            args.voices, args.out, lexicon_path=args.lexicon, names=args.names,
            variants=variants, frame=args.frame or DEFAULT_FRAME, include_raw=not args.no_raw,
            takes=args.takes,
        )
        print(f"rendered {len(written)} sample(s) -> {args.out}")
        print(f"open {Path(args.out) / 'index.html'} to pick stable respellings")
        return 0

    return 2


if __name__ == "__main__":
    raise SystemExit(main())
