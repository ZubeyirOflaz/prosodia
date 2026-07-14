# Authoring UI (planned)

[← Docs index](README.md)

> **Status: built (Phases 1–4).** `prosodia ui` serves the dashboard, the live job
> console, the transcript editor, repetition lint, and diagnosis. This document
> records the architecture and rationale; the decision is also summarized in
> [DESIGN.md §12](../DESIGN.md).

## Goal

One barebones **local** interface that unifies the authoring commands — `plan`,
`write`, `compile`, `trace-report`, `diagnose`, `personas`, and transcript/config
editing — so the pipeline isn't driven by remembering CLI flags. Not a product
surface; a single-user cockpit for the workflow this repo already implements.

## Constraints that decide the shape

These are not preferences — they are the load-bearing inputs:

- **Torch-free, tiny install.** The authoring base is only `pydantic + pyyaml`
  (see [DESIGN §3](../DESIGN.md)). Anything the UI adds lands in *that* install, so
  "avoid expensive dependencies" is the first-order metric.
- **Single user, localhost.** No auth, no sessions, no scale, no CDN — the
  requirements that justify a heavy web framework don't exist here.
- **Files are the source of truth.** `transcript.md`, `series.yaml`,
  `plan/outline.md`. The UI is a thin layer over the filesystem, the
  [trace store](pipeline-and-traces.md#traces), and subprocess triggers.
- **Two things already exist that the UI should lean on:** the `Run` trace store is
  a ready-made status substrate, and `author/trace_view.py` / `plan-view` already
  emit **self-contained HTML with only the standard library**.

## The decision

**Backend — Python standard-library `http.server`.** A `ThreadingHTTPServer` bound
to `127.0.0.1`, with route handlers that call the existing orchestrate/CLI functions
and return HTML built the same way `trace_view.py` already builds it. **Zero new
dependencies** — the install stays `pydantic + pyyaml`.

**Frontend — a tiny in-house interactivity layer (htmx-style).** Rather than vendor
the real ~14 KB `htmx.min.js`, the UI ships a ~60-line dependency-free JS shim
(`web/assets.py`, served at `/assets/app.js`) using the same attribute-driven model:
`data-get`/`data-post` fetch and swap an HTML **fragment** into a target, with
`data-trigger="load"` and interval `data-poll`. No JSON API, no JS framework, no build
step — and no external file to fetch, so it stays fully self-contained. It is a
deliberate **drop-in stand-in for htmx** (swap in the real library and rename the
attributes to `hx-*` later if richer behavior is ever wanted). Live job progress —
the reason a frontend layer earns its place at all — works the same way.

**Sanctioned upgrade — Flask.** Identical architecture; adopt *only* if hand-rolled
routing/templating outgrows a comfortable dispatch table. htmx multiplies the number
of small endpoints, so that endpoint sprawl is the likely, concrete trigger — but it
is not required for the MVP, and the htmx frontend is unchanged by the swap.

**Rejected / situational.** FastAPI + Uvicorn solves multi-client API concurrency we
don't have, at the cost of an async model and a frontend split. Textual (a terminal
UI) is lightweight but throws away the self-contained HTML we already generate.
**Streamlit / Gradio are rejected** — they pull pandas/tornado/uvicorn/huggingface
trees that directly violate the dependency budget. The full options comparison lived
in the review artifact that seeded this plan.

## What htmx buys (and where it doesn't)

htmx provides four things: **live partial refresh** (poll/SSE), **inline actions
without navigation**, **lazy panels**, and **forms that swap results in place**.
Mapped to the feature surface:

| Feature | htmx capability | Benefit |
|---|---|---|
| **Live job console** for `plan`/`write` — Writer↔Editor rounds appear as they complete, from the trace store, with a stdout tail | live refresh | **Flagship** |
| Inline pipeline triggers — run compile/lint/write from the dashboard; the status badge flips in place | inline action | Strong |
| Transcript editor — save → recompile → errors shown | full-page POST | Strong |
| Episode table with status badges (*drafted / compiled / traced*) | static per load | Strong |
| Per-job panel — status + stdout tail, self-refreshing (no cancel yet) | live refresh | Good |
| Artifact drill-down (view any round's `transcript.vN`, verdicts, brief) | lazy panel | Moderate |
| Diagnosis flow — "report a problem" form → ranked-sources page | full-page POST | Moderate |
| Tone/delivery tuner *(not built)* — nudge a `voice_profiles.yaml` value, re-render params | form-swap | future |
| Serving existing trace/diagnosis/outline HTML; static config viewing | — | **None** (full page is fine) |

The decisive one is the first row: long `claude -p` jobs whose status must update
live. Plain full-page reloads (`<meta refresh>`) are the weak point; htmx turns the
multi-minute `write` from a black box into a panel you can watch. **Caveat:** this is
*round-level* liveness out of the box (the worker writes each round's artifact; htmx
polls and swaps it in). Token-level streaming would mean capturing
`claude -p --output-format stream-json` into an SSE endpoint — a clean later upgrade,
not needed for the MVP.

## Future: trace & diagnosis as live, integrated views

Today `trace-report` and `diagnose` emit a **single self-contained HTML file**
(`author/trace_view.py`). That file is genuinely valuable — shareable, offline,
archival — and **stays**. But as the *working* surface it has three limits: it is a
**static snapshot** (regenerate to see a re-run), it **inlines everything** (a large
trace with many rounds/artifacts becomes a heavy file), and it is **disconnected**
from the running app (read-only; you can't act from it).

Integrating it via htmx removes all three and turns the trace viewer into the UI's
**live job console**:

- **Live** — while a `plan`/`write` job runs, the trace panel polls `run.json` and
  swaps in new stages and Writer↔Editor rounds as they land, instead of a manual
  regenerate-and-reopen.
- **Lazy** — heavy artifacts (full drafts, round diffs) load on demand via `hx-get`
  rather than being inlined up front, so a big trace stays fast.
- **Actionable & navigable** — trigger *re-run this stage with notes*, *diagnose
  this*, or *open the transcript at this segment* inline; click a lineage segment to
  jump to the round that produced it, or a diagnosis candidate to the implicated
  stage.
- **Unified** — it renders inside the dashboard shell (theme, nav, project context)
  rather than as an orphan file.

The clean way to get both is **one rendering core, two delivery modes** (matching the
"one store, two readers" philosophy): refactor `trace_view.py` from one monolithic
page-builder into composable **fragment builders** (timeline, per-stage panel,
segment-lineage row, diff). The standalone `trace-report` file composes the fragments
into a self-contained page (unchanged for users); the web server serves the same
fragments to htmx. Diagnosis follows the same split.

This lands across the phases: the fragment refactor + live trace is part of **Phase
2** (job console); the actionable/navigable trace is **Phase 3**. The exportable
self-contained file is kept throughout. *(Shipped: the `render_trace_fragment` refactor,
the live trace embedded in the running `write` job panel, and the fully interactive
trace page — lazy artifact drill-down, segment→producing-round links, and
re-run-a-stage buttons — via an optional `TraceLinks` hook the UI passes and the
standalone file omits.)*

## Architecture

A new torch-free package `prosodia.author.web`, launched by a
`prosodia ui --root <projects-dir> --port 8765` subcommand (defaults to `projects/`).
It adds a layer; it changes nothing beneath it.

```
  Browser (127.0.0.1)              server-rendered HTML + in-house app.js (htmx-style)
        │  app.js swaps HTML fragments; data-poll self-refresh on job panels
        ▼
  web/server.py        ThreadingHTTPServer · GET/POST routes · shared _layout()
        │              (+ trace_view's CSS on the trace page) · inlined CSS
        ├──────────────────────────────┬───────────────────────────────────────
        ▼                               ▼
  web/jobs.py                     web/views.py
  in-memory registry +            render dashboards; serve existing HTML verbatim
  ONE serialized worker for       (trace-report / diagnose / plan-view); transcript
  plan|write (they contend);      editor (textarea → save → recompile)
  fast ops (compile|lint) inline
        │                               │
        ▼                               ▼
  Existing core — UNCHANGED
  orchestrate (plan_series, author_episode) · compile · diagnosis ·
  the Run trace store (run.json, artifacts) · project files
```

**Route sketch**

- `/` — projects · `/p/<proj>` — dashboard: series config, personas, episode table
  with status badges.
- `POST /p/<proj>/plan`, `…/write?ep=N`, `…/compile?ep=N`, `…/diagnose` — enqueue a
  job, swap in its status panel.
- `/jobs/<id>` — live status + stdout tail (htmx-polled) · `/ep/<proj>/<n>` —
  view/edit transcript, then recompile.
- `/trace/<proj>/<n>`, `/diagnosis/<id>`, `/outline/<proj>` — serve the existing
  self-contained HTML.

**Guardrails**

- **Serialize LLM jobs** — one `claude -p` at a time (concurrent sessions have been
  observed to fail); fast/deterministic ops stay inline.
- **Bind `127.0.0.1` only** — no external exposure, no auth needed, no secrets
  rendered.
- **Guard the torch boundary** — `web` imports only authoring code; a test asserts no
  torch import path (keeps [DESIGN §3](../DESIGN.md)'s boundary intact).
- **Invoke via `python -m`** — matches the known console-script-shim issue on the
  authoring box.

## Phased build

Each phase is independently useful and shippable, front-loading value. **All four are
now implemented** (`prosodia ui`):

1. **Read-only dashboard.** Browse projects, personas, and the episode table with
   computed status; serve the existing trace / diagnosis / outline HTML. No job
   execution — near-zero risk. (htmx used only for lazy-loading those panels.)
2. **Trigger jobs.** Inline `compile` / `lint-repetition`; the serialized worker for
   `plan` / `write`, with an htmx-polled live status panel reading the trace.
3. **In-browser editing.** Transcript textarea → save → recompile, with compile
   errors surfaced inline; repetition-lint results alongside.
4. **Diagnosis & handoff.** A "report a problem" form driving `diagnose` into the
   ranked-sources HTML, and a `submit` button to package a compiled episode into a
   render job.

## Risks & open questions

- **Live output vs. simplicity.** Polling is trivial but coarse; SSE gives live
  streaming with a little stdlib work and no deps. Start with polling; add SSE only
  if the wait feels opaque.
- **Job durability.** An in-memory registry loses state on restart — acceptable, since
  the `Run` trace persists the real record on disk. Reconstructing job history from
  traces is a later nicety.
- **The Flask line.** Pick a concrete trigger (e.g. "handler boilerplate exceeds the
  app logic") so adopting B is a deliberate call, not drift.
- **Concurrency policy.** One serialized LLM worker is safe; whether a fast op may run
  *during* a long `write` is a quick decision (probably yes — they don't contend).

## See also

[DESIGN.md §12](../DESIGN.md) · [Pipeline & traces](pipeline-and-traces.md) ·
[CLI reference](cli-reference.md) · [Architecture](architecture.md) ·
[Roadmap & status](roadmap.md)
