# Prosodia

**Script-first, controllable narrated audio.** Prosodia turns a transcript you fully control — annotated with performance directions like tone, speed, and pauses — into narrated audio using a decoupled, swappable text-to-speech engine running on your own GPU.

> ⚠️ **Pre-alpha.** Design in [`DESIGN.md`](DESIGN.md). The authoring pipeline (`plan → write → compile → submit`), the per-episode run trace, and the trace-viewer + diagnosis tooling are **built and tested**; the renderer is built and awaits its first end-to-end audio run on a GPU box.

## Why

Tools like NotebookLM generate audio that is only *indirectly* controllable. For long-form, multi-episode narrative content that causes recurring problems:

1. **Uncontrollable transcript** — wrong emphasis, narrative breaks, synthetic-feeling dialogue.
2. **Forced two-person format** — constant speaker-switching that breaks listener focus.
3. **Content↔speech disconnect** — delivery that doesn't match the content's ideal emotion; missing pauses, near-interruptions, synthetic flow.
4. **Poor multi-episode coverage** — series that skip or repeat large sections across episodes.

Prosodia's approach: **decouple the script from the voice.** A human (with an LLM's help) writes a transcript that is the single source of truth and carries explicit per-section delivery guidance; a separate, pluggable TTS engine voices exactly that.

## How it works

```
Author a transcript          →   Render to audio
(human-edited, with tone/         (decoupled, pluggable TTS;
 speed/pause directions)          Chatterbox on a local GPU)
```

- **Authoring** runs anywhere (no GPU required).
- **Rendering** runs on a machine with an NVIDIA GPU.
- The two sides exchange jobs through a synced folder, so you can write remotely and render on the GPU box.

The default is a **single narrator** (multi-speaker `@tags` are parsed and validated today, but per-speaker voice rendering is not yet wired — see [`DESIGN.md`](DESIGN.md) §11), the TTS engine is **pluggable** (local [Chatterbox](https://github.com/resemble-ai/chatterbox) first; cloud engines later), and voices can be **preset or cloned**.

See [`DESIGN.md`](DESIGN.md) for the full architecture, decisions, and build plan.

## Status

Pre-alpha PoC. The **authoring side is built and tested** (`plan → write → compile → submit`), with a worked example in `projects/eu_history/`. The **renderer is built** for a Windows + NVIDIA box (`prosodia-render`; see [`scripts/RENDERER_SETUP.md`](scripts/RENDERER_SETUP.md)) and awaits its first end-to-end audio run on the GPU machine.

## Quickstart

Authoring (any machine, no GPU — pure-Python, no torch):

```bash
pip install -e .
prosodia compile projects/eu_history/episodes/ep1/transcript.md \
  --config projects/eu_history/series.yaml --lexicon projects/eu_history/lexicon.yaml
prosodia submit projects/eu_history/episodes/ep1 --root <synced_folder> --job-id eu-ep1
```

`compile` writes `ir.json` + `render_plan.json` next to the transcript by default; pass `--out <dir>` to write them elsewhere. If `--lexicon` is omitted, a `lexicon:` key in the `--config` file (resolved relative to that file) is used.

`prosodia plan --project <dir>` and `prosodia write --project <dir> --episode N` drive the headless Claude Code authoring loop (Planner → Writer ⇄ Editor). Rendering runs on a GPU box — see [`scripts/RENDERER_SETUP.md`](scripts/RENDERER_SETUP.md) and [`docs/HANDOFF.md`](docs/HANDOFF.md).

## Documentation

Full documentation is in [`docs/`](docs/README.md):
[Overview](docs/overview.md) · [Getting started](docs/getting-started.md) ·
[Architecture](docs/architecture.md) · [Authoring guide](docs/authoring-guide.md) ·
[Configuration](docs/configuration.md) · [CLI reference](docs/cli-reference.md) ·
[Rendering](docs/rendering.md) · [Pipeline & traces](docs/pipeline-and-traces.md) ·
[Roadmap & status](docs/roadmap.md).

## License

MIT — see [`LICENSE`](LICENSE).
