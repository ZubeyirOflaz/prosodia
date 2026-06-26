# Rendering

[← Docs index](README.md)

The renderer runs on the GPU box and turns a job (`ir.json` + `render_plan.json`
+ optional voice clip) into `episode.wav`. It is a deterministic, LLM-free
function of `(IR + render plan + voice + seed)`.

## Setup

One-time, on a Windows + NVIDIA machine: [Renderer setup](../scripts/RENDERER_SETUP.md).
It installs a CUDA torch wheel first, then `prosodia[render]`, then ffmpeg, and
runs `prosodia-render doctor` to confirm the environment. The authoring side never
needs any of this.

## How a job renders

For each [segment](glossary.md) in the IR, in order:

1. Emit `pause_before_ms` of **real silence** (paragraph / beat / explicit `{pause}`).
2. Render each ~300-char **chunk** with the segment's Chatterbox params from the
   render plan (`exaggeration`, `cfg_weight`, `temperature`), reusing one voice
   reference for timbre consistency.
3. **Quality-gate** the chunk (see below).
4. Trim lead/trail silence and **crossfade-join** (20 ms) to avoid clicks.

Then the whole episode is **loudness-normalized once** (EBU R128 via ffmpeg) to
`episode.wav`. Per-chunk normalization is deliberately avoided (it amplifies
volume drift).

## Modes

| Mode | Flag | Behavior |
|---|---|---|
| Fast preview (default) | — | 1 candidate per chunk, no STT — fast, for finding gross failures |
| Final | `--final` | N candidates per chunk + STT validation, keep the best |

Start in fast preview to shake out problems, then re-render `--final` for quality.

## Quality gate

In final mode, each chunk is transcribed with **faster-whisper** and compared to
the intended text; the renderer generates several candidates (with derived seeds)
and keeps the closest match. This catches Chatterbox's hallucinations, repeats,
and off-prompt continuation that crossfading cannot fix.

## Voices

The voice is resolved to a reference clip: a clip **bundled with the job** wins;
otherwise `--voices <dir>/<voice>.wav`; otherwise the engine default. See
[Configuration → voices](configuration.md#voices).

## Running

```powershell
# one job:
prosodia-render render <synced_folder>\inbox\eu-ep1 --final --voices .\voices

# or watch the exchange root and render jobs as they arrive (model stays warm):
prosodia-render watch <synced_folder> --voices .\voices
```

`scripts\start_renderer.ps1` wraps `watch` and can register a logon Scheduled Task.

## Job lifecycle

The watcher claims a job only when its **manifest validates** (sha256 + size of
every payload file), then moves it `inbox/ → processing/`, renders, and moves it
`→ outbox/` with a `done` status — or `→ failed/` with the error in `status.json`.
A half-synced job never validates and is retried. Full contract:
[Job protocol](../protocol/SPEC.md).

## See also

[Renderer setup](../scripts/RENDERER_SETUP.md) · [Handoff](HANDOFF.md) ·
[Job protocol](../protocol/SPEC.md) · [CLI reference](cli-reference.md) ·
[Architecture](architecture.md)
