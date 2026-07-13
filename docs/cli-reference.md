# CLI reference

[← Docs index](README.md)

Two commands: **`prosodia`** (authoring, any machine) and **`prosodia-render`**
(GPU box, needs the `[render]` extra).

## `prosodia` (authoring)

```
prosodia [--version] {plan, write, compile, submit, voice-prep, plan-view, trace-report, diagnose, personas, persona-new} ...
```

### `prosodia plan`

Run the Planner to produce a series outline + coverage map. Writes
`<project>/plan/outline.md` (and `plan/trace.jsonl`). Requires the `claude` CLI.

| Option | Req | Meaning |
|---|---|---|
| `--project DIR` | yes | project directory holding `series.yaml` |
| `--persona NAME` | no | persona to author with (default: `series.yaml` `persona:` or `hardcore-history`) |

### `prosodia write`

Run the Writer ⇄ Editor loop for one episode. Writes
`<project>/episodes/<slug>/transcript.md` (and `trace.jsonl`). Requires the `claude` CLI.

| Option | Req | Meaning |
|---|---|---|
| `--project DIR` | yes | project directory holding `series.yaml` |
| `--episode N` | yes | episode number (must exist in `series.yaml`) |
| `--max-rounds N` | no | max editorial rounds (default 3) |
| `--persona NAME` | no | persona to author with (default: `series.yaml` `persona:` or `hardcore-history`) |

### `prosodia compile`

Compile a transcript to `ir.json` + `render_plan.json` (and a per-episode `run/`
trace + `lineage.json`). Deterministic and offline.

| Argument / option | Req | Meaning |
|---|---|---|
| `transcript` | yes | path to a transcript `.md` file |
| `--out DIR` | no | output directory (default: alongside the transcript) |
| `--lexicon FILE` | no | pronunciation lexicon YAML |
| `--config FILE` | no | project config YAML (supplies the default `voice`/`seed`; if `--lexicon` is omitted, its `lexicon:` key is used, resolved relative to the config file) |
| `--voice NAME` | no | voice override (highest precedence) |
| `--persona NAME` | no | persona for the tone table (default: `--config` `persona:` or `hardcore-history`) |

### `prosodia submit`

Package a compiled episode into a render job and publish it atomically to `inbox/`.

| Argument / option | Req | Meaning |
|---|---|---|
| `episode` | yes | directory holding `ir.json` + `render_plan.json` |
| `--root ROOT` | yes | synced exchange root (holds `inbox/` etc.) |
| `--job-id ID` | no | job id (default: `ep<N>` or the directory name) |
| `--voices DIR` | no | dir of voice clips to bundle from (default: `<project>/voices`) |
| `--voice-ref WAV` | no | explicit voice `.wav` to bundle (overrides `--voices`) |

By default `submit` bundles `<project>/voices/<voice>.wav` (the per-project clip
matching the resolved `voice`) into the job, so it travels with it.

### `prosodia voice-prep`

Cut a ~10s narration reference clip from a longer source `.wav`, ending at a
natural pause and downmixed to mono. Needs the `audio` extra
(`pip install "prosodia[audio]"`); no GPU.

| Argument / option | Req | Meaning |
|---|---|---|
| `source` | yes | source `.wav` file |
| `--start TS` | yes | start timestamp: seconds (`12.5`) or `M:SS` (`1:30`) |
| `--out WAV` | yes | output path (e.g. `projects/<proj>/voices/narrator.wav`) |
| `--duration S` | no | target clip length in seconds (default 10) |

### `prosodia plan-view`

Render a plan outline (the Planner's Markdown) into a self-contained HTML **review
page** — the highest-value point for a quick human check, before any episode is
written. Pure standard-library; no GPU, no extra deps; open the file in a browser.

| Argument / option | Req | Meaning |
|---|---|---|
| `plan` | yes | path to a plan `.md` (the Planner's outline) |
| `--out HTML` | no | output path (default: alongside the plan) |
| `--title T` | no | page title (default: the plan's H1 or the filename) |

### `prosodia trace-report`

Render an episode's run trace into a self-contained HTML **trace viewer** (pipeline
timeline, per-stage inputs/outputs/warnings, and the segment lineage table). Pure
standard-library; open the file in a browser.

| Argument / option | Req | Meaning |
|---|---|---|
| `episode` | yes | episode dir holding `run/` (`run.json`) |
| `--out HTML` | no | output path (default: `<episode>/run/trace.html`) |

### `prosodia diagnose`

Turn a reported problem into a ranked list of probable sources across the pipeline —
each with evidence and a recommended fix — written to an HTML report in
`run/diagnoses/`. A deterministic signal pass reads the trace and ranks candidates;
unless `--no-agent`, a Claude agent then re-ranks and enriches them.

| Argument / option | Req | Meaning |
|---|---|---|
| `episode` | yes | episode dir holding `ir.json` + `render_plan.json` + `run/` |
| `complaint` | yes | the problem in plain words (e.g. `"the opening feels flat"`) |
| `--beat N` | no | focus on a specific beat index |
| `--no-agent` | no | deterministic signals only (skip the Claude agent) |

### `prosodia personas`

List available personas (the built-in library plus a project's local `personas/`).

| Option | Req | Meaning |
|---|---|---|
| `--project DIR` | no | also include this project's local `personas/` |

### `prosodia persona-new`

Scaffold a new persona by copying an existing one (ownership is complete, so you start
from a full role set + tone table to edit).

| Argument / option | Req | Meaning |
|---|---|---|
| `name` | yes | new persona name |
| `--from NAME` | no | persona to copy from (default: `hardcore-history`) |
| `--into DIR` | no | library dir to create it in (default: the built-in library) |
| `--project DIR` | no | resolve `--from` against a project's `personas/` too |

## `prosodia-render` (GPU box)

```
prosodia-render {doctor, render, watch, audition} ...
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

### `prosodia-render audition`

Render the **same text** with several reference clips side by side (content held
constant, so the clip is the only variable) to A/B candidate voices. Writes one `.wav`
per clip×take plus an `index.html` player. See [Renderer setup → Voices](../scripts/RENDERER_SETUP.md).

| Argument / option | Req | Meaning |
|---|---|---|
| `--voices ...` | yes | a `voices/` dir and/or `.wav` files to compare |
| `--out DIR` | no | output directory (default: `./voice_audition`) |
| `--text STR` / `--text-file F` | no | text to speak (default: a built-in narration sample) |
| `--takes N` | no | takes per clip, seeds matched across clips (default 2) |
| `--exaggeration` / `--cfg` / `--temperature` | no | delivery overrides |

## See also

[Getting started](getting-started.md) · [Authoring guide](authoring-guide.md) ·
[Rendering](rendering.md) · [Handoff](HANDOFF.md)
