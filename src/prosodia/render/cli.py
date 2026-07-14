"""Command-line entry point for the rendering side (``prosodia-render``).

Requires the ``render`` extra (torch + Chatterbox), a CUDA GPU, and ffmpeg on
PATH. Heavy imports are deferred so a base, torch-free install fails with a
helpful message instead of an opaque ImportError. ``doctor`` reports what's
missing (repair B1/B2).
"""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path


def check_render_env() -> list[str]:
    """Return human-readable problems with the render environment (empty == OK)."""
    problems: list[str] = []

    if sys.version_info >= (3, 13):
        problems.append(
            f"Python {sys.version_info.major}.{sys.version_info.minor} is too new for the "
            "TTS stack; use Python 3.11 or 3.12 on the render box."
        )

    try:
        import torch
    except Exception:
        problems.append(
            "PyTorch is not installed. Install a CUDA wheel FIRST, then "
            "`pip install prosodia[render]` (see scripts/setup.ps1)."
        )
    else:
        try:
            if not torch.cuda.is_available():
                problems.append(
                    "torch.cuda.is_available() is False - no usable CUDA GPU detected "
                    "(check the NVIDIA driver and that torch is a CUDA build, not CPU-only)."
                )
        except Exception as exc:  # pragma: no cover - defensive
            problems.append(f"Could not query CUDA: {exc}")

    try:
        import chatterbox  # noqa: F401  (provided by the chatterbox-tts package)
    except Exception:
        problems.append("chatterbox-tts is not installed (`pip install prosodia[render]`).")

    if shutil.which("ffmpeg") is None:
        problems.append("ffmpeg is not on PATH (install with `winget install Gyan.FFmpeg`).")

    return problems


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="prosodia-render",
        description="Render Prosodia jobs to audio on a CUDA GPU (Chatterbox).",
    )
    sub = parser.add_subparsers(dest="command")
    sub.add_parser("doctor", help="check the render environment (Python, torch/CUDA, ffmpeg)")

    p_render = sub.add_parser("render", help="render a single job directory")
    p_render.add_argument("job", help="path to a job directory (holds ir.json + render_plan.json)")
    p_render.add_argument("--final", action="store_true", help="final mode (N candidates + STT gate)")
    p_render.add_argument("--voices", help="directory of voice reference .wav files")
    p_render.add_argument("--no-title", action="store_true", help="don't speak the episode title at the start")

    p_watch = sub.add_parser("watch", help="watch an exchange root and render jobs as they arrive")
    p_watch.add_argument("root", help="synced exchange root (holds inbox/ processing/ outbox/ failed/)")
    p_watch.add_argument("--final", action="store_true", help="final mode (N candidates + STT gate)")
    p_watch.add_argument("--voices", help="directory of voice reference .wav files")
    p_watch.add_argument("--interval", type=float, default=5.0, help="poll interval seconds")
    p_watch.add_argument("--once", action="store_true", help="process the current inbox once and exit")
    p_watch.add_argument("--no-title", action="store_true", help="don't speak the episode title at the start")

    p_aud = sub.add_parser("audition", help="render the SAME text with several voice clips, side by side (A/B)")
    p_aud.add_argument("--voices", nargs="+", required=True, help="a voices/ dir and/or .wav files to compare")
    p_aud.add_argument("--out", default="voice_audition", help="output directory (default: ./voice_audition)")
    p_aud.add_argument("--text", help="text to speak (default: a short built-in narration sample)")
    p_aud.add_argument("--text-file", help="read the text from a file instead of --text")
    p_aud.add_argument("--takes", type=int, default=2, help="takes per clip, seeds matched across clips (default 2)")
    p_aud.add_argument("--exaggeration", type=float, default=0.4)
    p_aud.add_argument("--cfg", type=float, default=0.45, dest="cfg_weight")
    p_aud.add_argument("--temperature", type=float, default=0.75)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if not args.command:
        parser.print_help()
        return 0

    problems = check_render_env()
    if args.command == "doctor":
        if problems:
            print("Render environment problems:")
            for p in problems:
                print(f"  - {p}")
            return 1
        print("Render environment OK (Python, torch/CUDA, chatterbox, ffmpeg).")
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
        )
        print(f"rendered -> {out}")
        return 0

    if args.command == "watch":
        from prosodia.render.watch_and_render import watch

        watch(
            args.root, interval=args.interval, fast_preview=not args.final,
            voices_dir=args.voices, once=args.once, speak_title=not args.no_title,
        )
        return 0

    if args.command == "audition":
        from prosodia.render.audition import DEFAULT_TEXT, audition

        if args.text_file:
            text = Path(args.text_file).read_text(encoding="utf-8")
        else:
            text = args.text or DEFAULT_TEXT
        written = audition(
            text, args.voices, args.out, takes=args.takes,
            exaggeration=args.exaggeration, cfg_weight=args.cfg_weight, temperature=args.temperature,
        )
        print(f"rendered {len(written)} sample(s) -> {args.out}")
        print(f"open {Path(args.out) / 'index.html'} to A/B the voices")
        return 0

    return 2


if __name__ == "__main__":
    raise SystemExit(main())
