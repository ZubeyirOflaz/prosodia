"""Command-line entry point for the authoring side (``prosodia``).

Pure-Python, no torch. ``plan`` and ``write`` drive the headless Claude Code
orchestrator (they require the ``claude`` CLI). ``compile`` and ``submit`` are
fully offline. Handlers import lazily so ``--help`` stays fast.
"""

from __future__ import annotations

import argparse
import re
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

    from prosodia.author.compile import compile_text
    from prosodia.author.lexicon import Lexicon
    from prosodia.author.persona import Persona
    from prosodia.author.tone import VoiceProfiles, build_render_plan
    from prosodia.core.lineage import build_lineage
    from prosodia.core.trace import Run

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

    # Run compile and tone as separate steps so their warnings can be attributed
    # to the right stage in the trace (bad directives -> compile; tone fallbacks
    # -> tone specialist). Share one VoiceProfiles instance across both.
    persona = Persona.resolve(args.persona or config.get("persona"), project=config_dir)
    profiles = VoiceProfiles.load(persona.voice_profiles_path())
    ir, compile_warnings = compile_text(
        text, lexicon=lexicon, config=config, voice_override=args.voice, profiles=profiles
    )
    plan, tone_warnings = build_render_plan(ir, profiles)

    out = Path(args.out) if args.out else Path(args.transcript).parent
    out.mkdir(parents=True, exist_ok=True)
    (out / "ir.json").write_text(ir.to_json(), encoding="utf-8")
    (out / "render_plan.json").write_text(plan.to_json(), encoding="utf-8")

    # Provenance: record compile + tone into the episode's run/, persisting each
    # stage's warnings as first-class diagnosis signals (not just stderr).
    run = Run(out / "run")
    ir_art = run.write_artifact("stages/compile/ir.json", ir.to_json(), label="ir")
    run.event("compile", "compile", outputs=[ir_art], warnings=compile_warnings, segments=len(ir.segments))
    plan_art = run.write_artifact("stages/tone/render_plan.json", plan.to_json(), label="render_plan")
    run.event("tone", "tone-specialist", inputs=[ir_art], outputs=[plan_art], warnings=tone_warnings)
    lineage = build_lineage(ir, plan, run.events())
    run.write_artifact("lineage.json", lineage.to_json(), label="lineage")
    run.write_index(episode=ir.episode, title=ir.title)

    for w in compile_warnings + tone_warnings:
        print(f"warning: {w}", file=sys.stderr)
    print(f"compiled {len(ir.segments)} segments (persona: {persona.name}) -> {out / 'ir.json'}")
    print(f"trace: {run.dir}")
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

    # Record the handoff in the episode's run/ so the trace spans authoring -> submit.
    from prosodia.core.trace import Run

    run = Run(ep / "run")
    run.event(
        "submit", "submit", job=job_id, dest=str(dest),
        voice=Path(voice_ref).name if voice_ref else None, segments=len(ir.segments),
    )
    run.write_index(episode=ir.episode, title=ir.title)

    note = f" (voice: {Path(voice_ref).name})" if voice_ref else " (no voice clip; engine default)"
    print(f"submitted job '{job_id}' -> {dest}{note}")
    return 0


def _cmd_voice_prep(args: argparse.Namespace) -> int:
    try:
        from prosodia.author.voiceprep import prepare_clip
    except ImportError:
        print('voice-prep needs the audio extra: pip install "prosodia[audio]"', file=sys.stderr)
        return 1

    info = prepare_clip(
        args.source, args.start, args.out,
        target_s=args.duration, min_s=args.min_s, max_s=args.max_s,
    )
    for w in info["warnings"]:
        print(f"warning: {w}", file=sys.stderr)
    print(f"wrote {args.out}  ({info['duration']:.1f}s @ {info['sr']} Hz, mono)")
    return 0


def _cmd_plan_view(args: argparse.Namespace) -> int:
    from prosodia.author.plan_view import render_file

    out = render_file(args.plan, args.out, args.title)
    print(f"wrote {out} — open it in a browser to review the plan")
    return 0


def _cmd_lint_repetition(args: argparse.Namespace) -> int:
    from prosodia.author.repetition import analyze, format_report, load_episode_transcripts

    if args.project:
        episodes = load_episode_transcripts(Path(args.project))
    else:
        episodes = {
            (Path(p).parent.name or Path(p).stem): Path(p).read_text(encoding="utf-8")
            for p in args.transcripts
        }
    if not episodes:
        print("no transcripts found (pass files or --project)", file=sys.stderr)
        return 1
    print(format_report(analyze(episodes)))
    return 0


def _cmd_trace_report(args: argparse.Namespace) -> int:
    from prosodia.author.trace_view import render_trace_html
    from prosodia.core.lineage import Lineage
    from prosodia.core.trace import RunIndex

    run_dir = Path(args.episode) / "run"
    index_path = run_dir / "run.json"
    if not index_path.exists():
        print(f"no run trace at {index_path} (run plan/write/compile first)", file=sys.stderr)
        return 1
    index = RunIndex.model_validate_json(index_path.read_text(encoding="utf-8"))
    lin_path = run_dir / "lineage.json"
    lineage = Lineage.from_json(lin_path.read_text(encoding="utf-8")) if lin_path.exists() else None
    out = Path(args.out) if args.out else run_dir / "trace.html"
    out.write_text(render_trace_html(index, lineage), encoding="utf-8")
    print(f"wrote {out} — open it in a browser")
    return 0


def _cmd_diagnose(args: argparse.Namespace) -> int:
    from datetime import datetime, timezone

    from prosodia.author.trace_view import render_diagnosis_html
    from prosodia.core.diagnosis import (
        DIAGNOSIS_SCHEMA, apply_agent_result, build_agent_context, build_diagnosis,
    )
    from prosodia.core.ir import EpisodeIR, RenderPlan
    from prosodia.core.lineage import Lineage, build_lineage
    from prosodia.core.trace import Run

    ep = Path(args.episode)
    ir = EpisodeIR.from_json((ep / "ir.json").read_text(encoding="utf-8"))
    plan = RenderPlan.from_json((ep / "render_plan.json").read_text(encoding="utf-8"))
    run = Run(ep / "run")
    events = run.events()
    lin_path = run.dir / "lineage.json"
    lineage = (
        Lineage.from_json(lin_path.read_text(encoding="utf-8"))
        if lin_path.exists()
        else build_lineage(ir, plan, events)
    )

    diags_dir = run.dir / "diagnoses"
    diags_dir.mkdir(parents=True, exist_ok=True)
    diag_id = f"diag-{len(list(diags_dir.glob('diag-*.json'))) + 1:03d}"
    diag = build_diagnosis(
        args.complaint, lineage, events,
        episode=ir.episode, beat=args.beat, diag_id=diag_id,
        created=datetime.now(timezone.utc).isoformat(),
    )

    # Hand the deterministic ranking to the Claude agent to refine, unless --no-agent.
    if not args.no_agent:
        try:
            from prosodia.author.orchestrate import ClaudeRunner, _load_role

            _, structured = ClaudeRunner().run(
                build_agent_context(diag, lineage, events),
                system=_load_role("diagnostician"),
                schema=DIAGNOSIS_SCHEMA,
            )
            diag = apply_agent_result(diag, structured)
        except Exception as exc:  # noqa: BLE001 - agent is best-effort; fall back deterministically
            print(f"note: agent refinement skipped ({exc}); using deterministic diagnosis", file=sys.stderr)

    (diags_dir / f"{diag_id}.json").write_text(diag.to_json(), encoding="utf-8")
    html_path = diags_dir / f"{diag_id}.html"
    html_path.write_text(render_diagnosis_html(diag), encoding="utf-8")

    if diag.most_likely:
        top = diag.most_likely
        print(f"{diag_id}: most likely -> {top.stage} ({int(round(top.confidence * 100))}%) [{diag.method}]")
    print(f"  {diag.summary}")
    print(f"report: {html_path}")
    return 0


def _cmd_personas(args: argparse.Namespace) -> int:
    from prosodia.author.persona import Persona

    project = Path(args.project) if args.project else None
    names = Persona.available(project)
    if not names:
        print("no personas found", file=sys.stderr)
        return 1
    for name in names:
        p = Persona.resolve(name, project=project)
        desc = " ".join(p.description.split())
        print(f"{name:20} {desc[:96]}")
    return 0


def _cmd_persona_new(args: argparse.Namespace) -> int:
    import shutil

    from prosodia.author.persona import Persona

    project = Path(args.project) if args.project else None
    src = Persona.resolve(args.from_persona, project=project)
    dest_root = Path(args.into) if args.into else Persona._builtin_library()
    dest = dest_root / args.name
    if dest.exists():
        print(f"persona '{args.name}' already exists at {dest}", file=sys.stderr)
        return 1
    shutil.copytree(src.root, dest)
    print(f"created persona '{args.name}' at {dest}  (copied from '{src.name}')")
    print("  edit roles/*.md, voice_profiles.yaml, and persona.yaml to shape the new voice")
    return 0


def _cmd_plan(args: argparse.Namespace) -> int:
    from prosodia.author.orchestrate import ClaudeRunner, plan_series
    from prosodia.author.persona import Persona
    from prosodia.core.trace import Trace

    proj = Path(args.project)
    cfg = _load_series(proj)
    persona = Persona.resolve(args.persona or cfg.get("persona"), project=proj)
    prompt = (
        f"Series: {cfg.get('series', '')}\n"
        f"Goal: {cfg.get('description', '')}\n"
        f"Style: {cfg.get('style', '')}\n"
        f"Organizing angle: {cfg.get('angle') or '(none given — propose one that fits the material)'}\n"
    )
    if cfg.get("scope"):
        prompt += f"Scope for THIS plan (cover only this; reserve the rest for a later expansion): {cfg['scope']}\n"
    # Feed the verified research docket STRAIGHT into the prompt so the planner builds from our
    # material instead of re-researching every thinker from the open web (which timed out).
    research_dir = proj / "research"
    docket = (
        [
            f"===== research/{f.name} =====\n{f.read_text(encoding='utf-8')}"
            for f in sorted(research_dir.glob("*.md"))
        ]
        if research_dir.is_dir()
        else []
    )
    if docket:
        prompt += (
            "\n\nRESEARCH DOCKET — verified, cited source material. BUILD THE OUTLINE FROM THIS; do "
            "NOT re-research thinkers it already covers. Use web search ONLY to fill a gap the docket "
            "explicitly flags (e.g. Ibn Khaldun) or to check a single doubtful anecdote:\n\n"
            + "\n\n".join(docket)
        )
    prompt += "\n\nProduce the series outline and coverage map."
    trace = Trace(proj / "plan" / "trace.jsonl")
    # Web tools stay on for the few flagged gaps; longer timeout — a full-series outline is a big
    # single generation.
    runner = ClaudeRunner(
        extra_dirs=(str(proj),), allowed_tools=("WebSearch", "WebFetch"), timeout=1800
    )
    outline = plan_series(prompt, runner=runner, persona=persona, trace=trace)
    out = proj / "plan" / "outline.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(outline, encoding="utf-8")
    print(f"wrote {out}  (persona: {persona.name})")
    return 0


def _cmd_write(args: argparse.Namespace) -> int:
    from prosodia.author.orchestrate import ClaudeRunner, author_episode
    from prosodia.author.persona import Persona
    from prosodia.core.trace import Run

    proj = Path(args.project)
    cfg = _load_series(proj)
    eps = {e.get("n"): e for e in cfg.get("episodes", [])}
    ep = eps.get(args.episode)
    if not ep:
        print(f"episode {args.episode} not found in {proj / 'series.yaml'}", file=sys.stderr)
        return 1
    persona = Persona.resolve(args.persona or cfg.get("persona"), project=proj)
    target_minutes = ep.get("target_minutes", cfg.get("target_minutes", persona.defaults.target_minutes))
    brief = (
        f"Series: {cfg.get('series', '')}\n"
        f"Episode {ep['n']}: {ep.get('title', '')}\n"
        f"Scope: {ep.get('scope', '')}\n"
        f"Tension: {ep.get('tension', '')}\n"
        f"Target length: about {target_minutes} minutes of narration "
        "(long-form; write to that depth, not a summary).\n"
    )
    # If the Planner has produced an outline, feed THIS episode's plan (its sourced
    # anecdotes, human anchor, and contested points) to the writer so it places rather
    # than invents. Falls back to the coarse brief above if there's no outline yet.
    outline_path = proj / "plan" / "outline.md"
    if outline_path.exists():
        from prosodia.author.planparse import extract_episode_section

        section = extract_episode_section(outline_path.read_text(encoding="utf-8"), ep["n"])
        if section:
            brief += (
                "\n--- PLAN FOR THIS EPISODE (from the Planner — follow it) ---\n"
                "Use the human anchor, the sourced anecdotes, and the contested points below as\n"
                "raw material: choose which to use, decide where each lands, word it, and tie it to\n"
                "the narrative. Do NOT invent anecdotes or state facts the plan did not give you.\n\n"
                f"{section}\n"
            )
    # Feed-forward: warn the writer off openings/phrases already used in earlier
    # episodes (a fresh writer is otherwise blind to the rest of the series).
    from prosodia.author.repetition import feedforward_context, load_episode_transcripts

    prior: dict[str, str] = {}
    for name, md in load_episode_transcripts(proj).items():
        m = re.search(r"(\d+)", name)
        if m and int(m.group(1)) < ep["n"]:
            prior[name] = md
    ff = feedforward_context(prior)
    if ff:
        brief += "\n\n" + ff + "\n"

    brief += "\nWrite the full episode transcript in the Prosodia hybrid format."
    epdir = proj / "episodes" / ep.get("slug", f"ep{ep['n']}")
    epdir.mkdir(parents=True, exist_ok=True)
    run = Run(epdir / "run")
    transcript = author_episode(
        brief, runner=ClaudeRunner(extra_dirs=(str(proj),)), persona=persona,
        run=run, max_rounds=args.max_rounds,
    )
    out = epdir / "transcript.md"
    out.write_text(transcript, encoding="utf-8")
    run.write_index(episode=ep["n"], title=ep.get("title"))
    print(f"wrote {out}  (persona: {persona.name})")
    print(f"trace: {run.dir}")
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
    p_plan.add_argument("--persona", help="persona name (default: series.yaml persona: or hardcore-history)")

    p_write = sub.add_parser("write", help="author an episode (Writer <-> Editor loop)")
    p_write.add_argument("--project", required=True, help="project dir holding series.yaml")
    p_write.add_argument("--episode", type=int, required=True, help="episode number")
    p_write.add_argument("--max-rounds", type=int, default=3, help="max editorial rounds")
    p_write.add_argument("--persona", help="persona name (default: series.yaml persona: or hardcore-history)")

    p_compile = sub.add_parser("compile", help="compile a transcript.md to IR + render plan")
    p_compile.add_argument("transcript", help="path to a transcript .md file")
    p_compile.add_argument("--out", help="output directory (default: alongside the transcript)")
    p_compile.add_argument("--lexicon", help="path to a pronunciation lexicon YAML")
    p_compile.add_argument("--config", help="project config YAML (provides default voice/seed)")
    p_compile.add_argument("--voice", help="voice override (highest precedence)")
    p_compile.add_argument("--persona", help="persona name (default: --config persona: or hardcore-history)")

    p_submit = sub.add_parser("submit", help="package a compiled episode into a render job")
    p_submit.add_argument("episode", help="directory holding ir.json + render_plan.json")
    p_submit.add_argument("--root", required=True, help="synced exchange root (holds inbox/ etc.)")
    p_submit.add_argument("--job-id", help="job id (default: ep<N> or the directory name)")
    p_submit.add_argument("--voice-ref", help="explicit voice .wav to bundle (overrides project voices/)")
    p_submit.add_argument("--voices", help="dir of voice clips (default: <project>/voices)")

    p_vp = sub.add_parser("voice-prep", help="cut a reference clip from a source .wav")
    p_vp.add_argument("source", help="source .wav file")
    p_vp.add_argument("--start", required=True, help="start timestamp: seconds (12.5) or M:SS")
    p_vp.add_argument("--out", required=True, help="output .wav (e.g. projects/<proj>/voices/narrator.wav)")
    p_vp.add_argument("--duration", type=float, default=10.0,
                      help="target clip length seconds (default 10; endpoint snaps to a natural pause near it)")
    p_vp.add_argument("--min-s", type=float, help="min clip length for the pause search (default: 0.8x duration)")
    p_vp.add_argument("--max-s", type=float, help="max clip length for the pause search (default: 1.35x duration)")

    p_pv = sub.add_parser("plan-view", help="render a plan outline to a lightweight HTML review page")
    p_pv.add_argument("plan", help="path to a plan .md (the Planner's outline)")
    p_pv.add_argument("--out", help="output .html (default: alongside the plan)")
    p_pv.add_argument("--title", help="page title (default: the plan's H1 or the filename)")

    p_lint = sub.add_parser("lint-repetition", help="report repeated openings/phrases across a series")
    p_lint.add_argument("transcripts", nargs="*", help="transcript .md files (or use --project)")
    p_lint.add_argument("--project", help="project dir; scans episodes/*/transcript.md")

    p_trace = sub.add_parser("trace-report", help="render an episode's run trace to a self-contained HTML page")
    p_trace.add_argument("episode", help="episode dir holding run/ (run.json)")
    p_trace.add_argument("--out", help="output .html (default: <episode>/run/trace.html)")

    p_diag = sub.add_parser("diagnose", help="diagnose a reported problem into ranked sources + an HTML report")
    p_diag.add_argument("episode", help="episode dir holding ir.json + render_plan.json + run/")
    p_diag.add_argument("complaint", help='the problem in plain words (e.g. "the opening feels flat")')
    p_diag.add_argument("--beat", type=int, help="focus on a specific beat index")
    p_diag.add_argument("--no-agent", action="store_true", help="deterministic signals only (skip the Claude agent)")

    p_personas = sub.add_parser("personas", help="list available personas")
    p_personas.add_argument("--project", help="include a project's local personas/ too")

    p_pnew = sub.add_parser("persona-new", help="scaffold a new persona by copying an existing one")
    p_pnew.add_argument("name", help="new persona name")
    p_pnew.add_argument("--from", dest="from_persona", default="hardcore-history",
                        help="persona to copy from (default: hardcore-history)")
    p_pnew.add_argument("--into", help="library dir to create it in (default: the built-in library)")
    p_pnew.add_argument("--project", help="also resolve --from against this project's personas/")
    return parser


_DISPATCH = {
    "plan": _cmd_plan,
    "write": _cmd_write,
    "compile": _cmd_compile,
    "submit": _cmd_submit,
    "voice-prep": _cmd_voice_prep,
    "plan-view": _cmd_plan_view,
    "lint-repetition": _cmd_lint_repetition,
    "trace-report": _cmd_trace_report,
    "diagnose": _cmd_diagnose,
    "personas": _cmd_personas,
    "persona-new": _cmd_persona_new,
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
