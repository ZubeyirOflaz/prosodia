# CLI reference

[← Docs index](README.md)

Two commands: **`prosodia`** (authoring, any machine) and **`prosodia-render`**
(GPU box, needs the `[render]` extra).

## `prosodia` (authoring)

```
prosodia [--version] {plan, write, compile, submit, voice-prep, plan-view, lint-repetition, trace-report, diagnose, personas, persona-new, ui} ...
```

### `prosodia plan`

Run the Planner to produce a series outline + coverage map. Writes
`<project>/plan/outline.md` (and `plan/trace.jsonl`). Requires the `claude` CLI.

Feeds the project's `research/*.md` [docket](configuration.md#research-docket) into
the Planner so it builds from your verified material rather than researching from
scratch, and enables web search/fetch for gaps the docket flags. Honors a
series-level `scope:` to plan a subset now and expand later.

| Option | Req | Meaning |
|---|---|---|
| `--project DIR` | yes | project directory holding `series.yaml` |
| `--persona NAME` | no | persona to author with (default: `series.yaml` `persona:` or `hardcore-history`) |

### `prosodia write`

Run the Writer ⇄ Editor loop for one episode. Writes
`<project>/episodes/<slug>/transcript.md` (and a `run/` trace). Requires the `claude` CLI.

| Option | Req | Meaning |
|---|---|---|
| `--project DIR` | yes | project directory holding `series.yaml` |
| `--episode N` | yes | episode number (must exist in `series.yaml`) |
| `--max-rounds N` | no | max editorial rounds (default 3) |
| `--prior-episodes N` | no | how many of the most recent earlier episodes feed the writer's "avoid repetition" context (default 3; `0` disables) — capped so accumulating constraints don't make later episodes sound synthetic |
| `--persona NAME` | no | persona to author with (default: `series.yaml` `persona:` or `hardcore-history`) |

### `prosodia lexicon`

Build a pronunciation lexicon for a series and write `<project>/lexicon.yaml`. Delegates to
the **lexicographer agent**: for each name it fetches the Wikipedia pronunciation
(`wiki_pron.py`, author-side, no GPU) and converts it to a natural, Chatterbox-friendly
respelling per `roles/RESPELL_GUIDELINES.md` (no hyphens/CAPS — those are read as separate
words / acronyms). Only genuinely-hard names get an entry; easy names are left raw. The
**Planner emits the name list** (a `## Names for the lexicon` section in `plan/outline.md`) so
this pronunciation work never bloats the planner's own context. Requires the `claude` CLI.

| Option | Req | Meaning |
|---|---|---|
| `--project DIR` | yes | project dir (writes `<project>/lexicon.yaml`; preserves existing entries) |
| `--names ...` | no | names to include (default: the `Names for the lexicon` list in `plan/outline.md`) |
| `--names-file FILE` | no | read names from a file, one per line |
| `--out PATH` | no | output path (default: `<project>/lexicon.yaml`) |
| `--dry-run` | no | print the lexicon YAML instead of writing it |

> Standalone, no agent: `python -m prosodia.author.wiki_pron NAME ...` prints the raw
> Wikipedia IPA + respelling (JSON/TSV) for a name list.

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

### `prosodia lint-repetition`

Report repeated openings and phrases across a series' episodes — a cross-episode
freshness check. Pure standard-library; no GPU.

| Argument / option | Req | Meaning |
|---|---|---|
| `transcripts` | no | transcript `.md` files to compare (omit when using `--project`) |
| `--project DIR` | no | scan `episodes/*/transcript.md` under this project |

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

### `prosodia ui`

Serve the local authoring **dashboard** — a web view over the projects workspace:
browse projects and episodes (with drafted/compiled/traced status); run the planner
and writer as **live background jobs**; compile, edit transcripts (save + recompile),
repetition-lint, run deterministic diagnosis, and package render jobs; and open the
plan outline and each episode's run trace. Standard-library server plus a tiny
in-house JS layer (no GPU, no extra deps); binds to loopback. See the
[Authoring UI](authoring-ui.md) plan. `Ctrl-C` stops it.

| Option | Req | Meaning |
|---|---|---|
| `--root DIR` | no | projects root directory (default: `projects`) |
| `--host H` | no | bind host (default: `127.0.0.1`) |
| `--port N` | no | port (default: `8765`) |
| `--no-browser` | no | don't open a browser window on start |

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

Render a single job directory to `episode.wav`. The episode is bookended with 4 s of
lead/tail silence, and (unless `--no-title`) opens with the spoken episode title.

| Argument / option | Req | Meaning |
|---|---|---|
| `job` | yes | a job directory (holds `ir.json` + `render_plan.json`) |
| `--final` | no | final mode: N candidates + STT quality gate (default: fast preview) |
| `--voices DIR` | no | directory of voice reference `.wav` files |
| `--no-title` | no | don't speak the episode title at the start |
| `--no-lexicon-fallback` | no | **on by default (final mode):** normally each respelled name is spoken **unassisted first**, falling back to the lexicon respelling only if the plain name fails the STT gate. Pass `--no-lexicon-fallback` to always speak the respelling instead. |

### `prosodia-render watch`

Watch an exchange root and render jobs as they arrive (model kept warm).

| Argument / option | Req | Meaning |
|---|---|---|
| `root` | yes | synced exchange root (`inbox/ processing/ outbox/ failed/`) |
| `--final` | no | final mode (as above) |
| `--voices DIR` | no | directory of voice reference `.wav` files |
| `--interval SEC` | no | poll interval seconds (default 5.0) |
| `--once` | no | process the current inbox once and exit |
| `--no-title` | no | don't speak the episode title at the start |
| `--no-lexicon-fallback` | no | opt out of the default unassisted-first pronunciation (see `render` above); always speak the respelling |

### `prosodia-render audition`

A/B candidate voices across the **full delivery range**. By default it renders a built-in
*suite* of short passages spanning the tonal registers (measured → warm → wry → tense →
urgent → dramatic → reverent → somber → grave) and cadences (brisk enumerations, long
flowing sentences, a posed question with a beat, slow deliberate lines) — so you hear each
clip everywhere it will have to work, not just in calm narration. Each passage is spoken
with the **real engine parameters the pipeline would use** for that tone and rate (from the
persona's `voice_profiles.yaml` tone table + `pace` dial), so the audition matches
production. Content is held constant per row, so the reference clip is the only variable.
Writes one `.wav` per passage×clip×take plus an `index.html` player grouped by passage. See
[Renderer setup → Voices](../scripts/RENDERER_SETUP.md).

| Argument / option | Req | Meaning |
|---|---|---|
| `--voices ...` | yes | a `voices/` dir and/or `.wav` files to compare |
| `--out DIR` | no | output directory (default: `./voice_audition`) |
| `--text STR` / `--text-file F` | no | single-passage mode: speak this one text instead of the range suite |
| `--tone` / `--rate` | no | delivery intent for `--text` mode (default: `measured` / `normal`) |
| `--voice-profiles X` (alias `--persona`) | no | persona **name** (e.g. `thinkers`) or path to a `voice_profiles.yaml` whose tone table drives the params (default: the built-in persona's) |
| `--takes N` | no | takes per cell, seeds matched across clips (default 1) |
| `--exaggeration` / `--cfg` / `--temperature` | no | override that param for **every** passage (default: from the tone table) |

### `prosodia-render lexicon-audition`

Hear each lexicon respelling in the chosen voice **across N seeds**, to pick forms that
render *stably*. A respelling is only a hint to a neural TTS (no phoneme API) and every
occurrence in an episode is an independent generation, so an unstable respelling comes out
differently seed to seed — this surfaces that so you can replace it. Renders each entry
inside a carrier sentence and A/Bs it against the raw name and any candidate variants;
writes an `index.html` grouped by name. Workflow: audition → keep the stable respellings →
edit `lexicon.yaml` → recompile.

| Argument / option | Req | Meaning |
|---|---|---|
| `--voices ...` | yes | a `voices/` dir and/or `.wav` files |
| `--lexicon F` | yes | path to a project `lexicon.yaml` |
| `--out DIR` | no | output directory (default: `./lexicon_audition`) |
| `--names ...` | no | only audition these source names (default: all) |
| `--variants F` | no | YAML `{name: [respelling, …]}` of candidate respellings to A/B |
| `--frame STR` | no | carrier sentence with a `{}` placeholder for the name |
| `--takes N` | no | seeds per variant (default 3) |
| `--no-raw` | no | skip the raw-name baseline take |

> **Note (`--final` STT gate):** the render quality gate scores against a *de-respelled*
> reference (respellings mapped back to source spellings), so a correctly-pronounced take
> is rewarded, not the spelled-out one. This takes effect once an episode is **recompiled**
> (the de-respelled reference is embedded in `ir.json`). By default (unassisted-first) the
> renderer reuses that same de-respelled text as the *unassisted* spelling to try first,
> respelling only on a gate miss; the run logs how many respelled chunks actually needed the
> respelling. `--no-lexicon-fallback` turns that off and always speaks the respelling.

## See also

[Getting started](getting-started.md) · [Authoring guide](authoring-guide.md) ·
[Rendering](rendering.md) · [Handoff](HANDOFF.md)
