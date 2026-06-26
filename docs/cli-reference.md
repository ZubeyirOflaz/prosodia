# CLI reference

[← Docs index](README.md)

Two commands: **`prosodia`** (authoring, any machine) and **`prosodia-render`**
(GPU box, needs the `[render]` extra).

## `prosodia` (authoring)

```
prosodia [--version] {plan, write, compile, submit} ...
```

### `prosodia plan`

Run the Planner to produce a series outline + coverage map. Writes
`<project>/plan/outline.md` (and `plan/trace.jsonl`). Requires the `claude` CLI.

| Option | Req | Meaning |
|---|---|---|
| `--project DIR` | yes | project directory holding `series.yaml` |

### `prosodia write`

Run the Writer ⇄ Editor loop for one episode. Writes
`<project>/episodes/<slug>/transcript.md` (and `trace.jsonl`). Requires the `claude` CLI.

| Option | Req | Meaning |
|---|---|---|
| `--project DIR` | yes | project directory holding `series.yaml` |
| `--episode N` | yes | episode number (must exist in `series.yaml`) |
| `--max-rounds N` | no | max editorial rounds (default 3) |

### `prosodia compile`

Compile a transcript to `ir.json` + `render_plan.json`. Deterministic and offline.

| Argument / option | Req | Meaning |
|---|---|---|
| `transcript` | yes | path to a transcript `.md` file |
| `--out DIR` | no | output directory (default: alongside the transcript) |
| `--lexicon FILE` | no | pronunciation lexicon YAML |
| `--config FILE` | no | project config YAML (supplies the default `voice`/`seed`; if `--lexicon` is omitted, its `lexicon:` key is used, resolved relative to the config file) |
| `--voice NAME` | no | voice override (highest precedence) |

### `prosodia submit`

Package a compiled episode into a render job and publish it atomically to `inbox/`.

| Argument / option | Req | Meaning |
|---|---|---|
| `episode` | yes | directory holding `ir.json` + `render_plan.json` |
| `--root ROOT` | yes | synced exchange root (holds `inbox/` etc.) |
| `--job-id ID` | no | job id (default: `ep<N>` or the directory name) |
| `--voice-ref WAV` | no | a voice reference `.wav` to bundle with the job |

## `prosodia-render` (GPU box)

```
prosodia-render {doctor, render, watch} ...
```

Heavy imports are deferred; on a base install (no torch) it fails with a helpful
message instead of an ImportError. See [Renderer setup](../scripts/RENDERER_SETUP.md).

### `prosodia-render doctor`

Check the render environment (Python version, torch + CUDA, chatterbox, ffmpeg).
Exit 0 and "OK" when ready; otherwise lists exactly what's missing.

### `prosodia-render render`

Render a single job directory to `episode.wav`.

| Argument / option | Req | Meaning |
|---|---|---|
| `job` | yes | a job directory (holds `ir.json` + `render_plan.json`) |
| `--final` | no | final mode: N candidates + STT quality gate (default: fast preview) |
| `--voices DIR` | no | directory of voice reference `.wav` files |

### `prosodia-render watch`

Watch an exchange root and render jobs as they arrive (model kept warm).

| Argument / option | Req | Meaning |
|---|---|---|
| `root` | yes | synced exchange root (`inbox/ processing/ outbox/ failed/`) |
| `--final` | no | final mode (as above) |
| `--voices DIR` | no | directory of voice reference `.wav` files |
| `--interval SEC` | no | poll interval seconds (default 5.0) |
| `--once` | no | process the current inbox once and exit |

## See also

[Getting started](getting-started.md) · [Authoring guide](authoring-guide.md) ·
[Rendering](rendering.md) · [Handoff](HANDOFF.md)
