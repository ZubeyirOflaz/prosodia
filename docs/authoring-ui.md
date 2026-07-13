# Authoring UI (planned)

[← Docs index](README.md)

> **Status: planned, not built.** This records the agreed architecture and phased
> plan for a local authoring interface. Design decision is also summarized in
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

**Frontend — vendored htmx.** htmx is a ~14 KB JavaScript file (served *locally* from
the repo, so it is **not** a Python dependency and needs **no build step**). It is a
frontend technique, not a backend: the server returns small **HTML fragments** and
htmx swaps them into the page — no JSON API, no JS framework. It earns its place
because the app is job-centric, and live job progress is exactly its sweet spot.

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
| Live transcript editor — save → recompile → segment count + format errors swap in | form-swap | Strong |
| Episode table with live status (*planned → drafted → approved → compiled*) | live refresh | Strong |
| Job queue panel (queued/running, cancel) | live refresh | Good |
| Draft-round diff (`transcript.v1` vs `v2`, already persisted) | lazy panel | Moderate |
| Diagnosis flow — "report a problem" form swaps in the ranked-sources panel | form-swap | Moderate |
| Tone/delivery tuner — nudge a `voice_profiles.yaml` value, re-render a segment's params | form-swap | Nice |
| Serving existing trace/diagnosis/outline HTML; static config viewing | — | **None** (full page is fine) |

The decisive one is the first row: long `claude -p` jobs whose status must update
live. Plain full-page reloads (`<meta refresh>`) are the weak point; htmx turns the
multi-minute `write` from a black box into a panel you can watch. **Caveat:** this is
*round-level* liveness out of the box (the worker writes each round's artifact; htmx
polls and swaps it in). Token-level streaming would mean capturing
`claude -p --output-format stream-json` into an SSE endpoint — a clean later upgrade,
not needed for the MVP.

## Architecture

A new torch-free package `prosodia.author.web`, launched by a
`prosodia ui --project <dir> --port 8765` subcommand. It adds a layer; it changes
nothing beneath it.

```
  Browser (127.0.0.1)                     server-rendered HTML + vendored htmx.js
        │  htmx swaps HTML fragments; <meta refresh> or SSE on job panels
        ▼
  web/server.py        ThreadingHTTPServer · ~10 routes · shared _page() layout
        │              (extended from author/trace_view.py) · inlined CSS
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

Each phase is independently useful and shippable, front-loading value:

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
