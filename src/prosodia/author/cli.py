"""Command-line entry point for the authoring side (``prosodia``).

Pure-Python, no torch. ``plan`` and ``write`` drive the headless Claude Code
orchestrator (they require the ``claude`` CLI). ``compile`` and ``submit`` are
fully offline. Handlers import lazily so ``--help`` stays fast.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def _todo(name: str) -> int:
    print(f"prosodia: '{name}' is not implemented yet.", file=sys.stderr)
    return 2


def _load_series(project: Path) -> dict:
    import yaml

    return yaml.safe_load((project / "series.yaml").read_text(encoding="utf-8")) or {}


def _cmd_compile(args: argparse.Namespace) -> int:
    import yaml

    from prosodia.author.compile import compile_with_plan
    from prosodia.author.lexicon import Lexicon

    text = Path(args.transcript).read_text(encoding="utf-8")
    config: dict = {}
    config_dir: Path | None = None
    if args.config:
        config_path = Path(args.config)
        config_dir = config_path.parent
        loaded = yaml.safe_load(config_path.read_text(encoding="utf-8")) or {}
        config = loaded if isinstance(loaded, dict) else {}

    # Lexicon precedence: explicit --lexicon, else the config's `lexicon` key
    # (resolved relative to the config dir), else none.
    lexicon_path = args.lexicon
    if not lexicon_path and config.get("lexicon") and config_dir is not None:
        lexicon_path = config_dir / config["lexicon"]
    lexicon = Lexicon.load(Path(lexicon_path)) if lexicon_path else Lexicon({})
    ir, plan, warnings = compile_with_plan(
        text, lexicon=lexicon, config=config, voice_override=args.voice
    )

    out = Path(args.out) if args.out else Path(args.transcript).parent
    out.mkdir(parents=True, exist_ok=True)
    (out / "ir.json").write_text(ir.to_json(), encoding="utf-8")
    (out / "render_plan.json").write_text(plan.to_json(), encoding="utf-8")

    for w in warnings:
        print(f"warning: {w}", file=sys.stderr)
    print(f"compiled {len(ir.segments)} segments -> {out / 'ir.json'}")
    return 0


def _cmd_submit(args: argparse.Namespace) -> int:
    from prosodia.author.submit import package_job
    from prosodia.core.ir import EpisodeIR, RenderPlan

    ep = Path(args.episode)
    ir = EpisodeIR.from_json((ep / "ir.json").read_text(encoding="utf-8"))
    plan = RenderPlan.from_json((ep / "render_plan.json").read_text(encoding="utf-8"))
    job_id = args.job_id or (f"ep{ir.episode}" if ir.episode is not None else ep.name)

    # Per-project voice: bundle <project>/voices/<voice>.wav so the clip travels
    # with the job (the renderer prefers a bundled clip). --voice-ref overrides.
    voice_ref = args.voice_ref
    if not voice_ref and ir.voice and not ir.voice.startswith("preset:"):
        voices_dir = Path(args.voices) if args.voices else ep.parent.parent / "voices"
        cand = voices_dir / f"{ir.voice}.wav"
        if cand.exists():
            voice_ref = str(cand)

    dest = package_job(args.root, job_id, ir, plan, voice_ref=voice_ref)
    note = f" (voice: {Path(voice_ref).name})" if voice_ref else " (no voice clip; engine default)"
    print(f"submitted job '{job_id}' -> {dest}{note}")
    return 0


def _cmd_voice_prep(args: argparse.Namespace) -> int:
    try:
        from prosodia.author.voiceprep import prepare_clip
    except ImportError:
        print('voice-prep needs the audio extra: pip install "prosodia[audio]"', file=sys.stderr)
        return 1

    info = prepare_clip(args.source, args.start, args.out, target_s=args.duration)
    for w in info["warnings"]:
        print(f"warning: {w}", file=sys.stderr)
    print(f"wrote {args.out}  ({info['duration']:.1f}s @ {info['sr']} Hz, mono)")
    return 0


def _cmd_plan(args: argparse.Namespace) -> int:
    from prosodia.author.orchestrate import ClaudeRunner, plan_series
    from prosodia.core.trace import Trace

    proj = Path(args.project)
    cfg = _load_series(proj)
    prompt = (
        f"Series: {cfg.get('series', '')}\n"
        f"Goal: {cfg.get('description', '')}\n"
        f"Style: {cfg.get('style', '')}\n\n"
        "Produce the series outline and coverage map."
    )
    trace = Trace(proj / "plan" / "trace.jsonl")
    outline = plan_series(prompt, runner=ClaudeRunner(extra_dirs=(str(proj),)), trace=trace)
    out = proj / "plan" / "outline.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(outline, encoding="utf-8")
    print(f"wrote {out}")
    return 0


def _cmd_write(args: argparse.Namespace) -> int:
    from prosodia.author.orchestrate import ClaudeRunner, author_episode
    from prosodia.core.trace import Trace

    proj = Path(args.project)
    cfg = _load_series(proj)
    eps = {e.get("n"): e for e in cfg.get("episodes", [])}
    ep = eps.get(args.episode)
    if not ep:
        print(f"episode {args.episode} not found in {proj / 'series.yaml'}", file=sys.stderr)
        return 1
    target_minutes = ep.get("target_minutes", cfg.get("target_minutes", 30))
    brief = (
        f"Series: {cfg.get('series', '')}\n"
        f"Episode {ep['n']}: {ep.get('title', '')}\n"
        f"Scope: {ep.get('scope', '')}\n"
        f"Tension: {ep.get('tension', '')}\n"
        f"Target length: about {target_minutes} minutes of narration "
        "(long-form; write to that depth, not a summary).\n\n"
        "Write the full episode transcript in the Prosodia hybrid format."
    )
    epdir = proj / "episodes" / ep.get("slug", f"ep{ep['n']}")
    epdir.mkdir(parents=True, exist_ok=True)
    trace = Trace(epdir / "trace.jsonl")
    transcript = author_episode(
        brief, runner=ClaudeRunner(extra_dirs=(str(proj),)), trace=trace, max_rounds=args.max_rounds
    )
    out = epdir / "transcript.md"
    out.write_text(transcript, encoding="utf-8")
    print(f"wrote {out}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="prosodia",
        description="Author controllable narrated-audio transcripts (no GPU required).",
    )
    parser.add_argument("--version", action="store_true", help="print version and exit")
    sub = parser.add_subparsers(dest="command")

    p_plan = sub.add_parser("plan", help="plan a series outline + coverage map (Planner)")
    p_plan.add_argument("--project", required=True, help="project dir holding series.yaml")

    p_write = sub.add_parser("write", help="author an episode (Writer <-> Editor loop)")
    p_write.add_argument("--project", required=True, help="project dir holding series.yaml")
    p_write.add_argument("--episode", type=int, required=True, help="episode number")
    p_write.add_argument("--max-rounds", type=int, default=3, help="max editorial rounds")

    p_compile = sub.add_parser("compile", help="compile a transcript.md to IR + render plan")
    p_compile.add_argument("transcript", help="path to a transcript .md file")
    p_compile.add_argument("--out", help="output directory (default: alongside the transcript)")
    p_compile.add_argument("--lexicon", help="path to a pronunciation lexicon YAML")
    p_compile.add_argument("--config", help="project config YAML (provides default voice/seed)")
    p_compile.add_argument("--voice", help="voice override (highest precedence)")

    p_submit = sub.add_parser("submit", help="package a compiled episode into a render job")
    p_submit.add_argument("episode", help="directory holding ir.json + render_plan.json")
    p_submit.add_argument("--root", required=True, help="synced exchange root (holds inbox/ etc.)")
    p_submit.add_argument("--job-id", help="job id (default: ep<N> or the directory name)")
    p_submit.add_argument("--voice-ref", help="explicit voice .wav to bundle (overrides project voices/)")
    p_submit.add_argument("--voices", help="dir of voice clips (default: <project>/voices)")

    p_vp = sub.add_parser("voice-prep", help="cut a ~10s reference clip from a source .wav")
    p_vp.add_argument("source", help="source .wav file")
    p_vp.add_argument("--start", required=True, help="start timestamp: seconds (12.5) or M:SS")
    p_vp.add_argument("--out", required=True, help="output .wav (e.g. projects/<proj>/voices/narrator.wav)")
    p_vp.add_argument("--duration", type=float, default=10.0, help="target clip length seconds (default 10)")
    return parser


_DISPATCH = {
    "plan": _cmd_plan,
    "write": _cmd_write,
    "compile": _cmd_compile,
    "submit": _cmd_submit,
    "voice-prep": _cmd_voice_prep,
}


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if getattr(args, "version", False):
        from prosodia import __version__

        print(__version__)
        return 0
    if not args.command:
        parser.print_help()
        return 0
    handler = _DISPATCH.get(args.command)
    return handler(args) if handler else _todo(args.command)


if __name__ == "__main__":
    raise SystemExit(main())
