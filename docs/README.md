# Prosodia Documentation

Script-first, controllable narrated audio — an LLM-authored, human-editable
transcript with explicit performance directions, rendered by a decoupled,
pluggable TTS engine. Project root: [README](../README.md). Full design rationale
and decisions: [DESIGN.md](../DESIGN.md).

## Start here

- [Overview](overview.md) — what Prosodia is and the problems it solves
- [Getting started](getting-started.md) — install and run the worked example
- [Features](features.md) — what it does, mapped to the design goals

## Using it

- [Authoring guide](authoring-guide.md) — write transcripts (orchestrated or by hand)
- [Transcript format](../formats/SPEC.md) — the hybrid format specification (canonical)
- [Configuration](configuration.md) — projects, `series.yaml`, voices, tone table, lexicon
- [CLI reference](cli-reference.md) — `prosodia` and `prosodia-render`
- [Rendering](rendering.md) — running the GPU renderer
- [Renderer setup](../scripts/RENDERER_SETUP.md) — one-time Windows + NVIDIA setup
- [Handoff](HANDOFF.md) — the authoring ↔ renderer sync flow

## Understanding it

- [Architecture](architecture.md) — components, contracts, and data flow
- [Pipeline & traces](pipeline-and-traces.md) — the multi-agent authoring loop and troubleshooting
- [Authoring UI](authoring-ui.md) — the planned local dashboard (stdlib + vendored htmx)
- [Job protocol](../protocol/SPEC.md) — the synced job-folder contract (canonical)
- [Glossary](glossary.md) — terms used across the docs

## Project

- [Evaluation & testing](evaluation.md) — the automated suite and the A/B method
- [A/B scoring sheet](AB_TESTING.md) — Prosodia vs NotebookLM
- [Roadmap & status](roadmap.md) — what's done, what's open
- [Repair plan](../REPAIR_PLAN.md) — tracked fixes and remaining items

## Reference

- [Carlin craft](reference/carlin-craft.md) — the Hardcore-History gold standard (plan- & prose-level)
- [Optimization lessons](reference/optimization-lessons.md) — what the prompt-refinement loops taught + the (do-not-run-yet) next-research proposal
- [Craft sourcing](reference/craft-sourcing.md) — the repeatable process for analysing a teacher's corpus into a dossier
- [Casework synthesis](reference/casework-synthesis.md) — how four dossiers were merged into the `casework` persona, and what was rejected
- [Casework series roadmap](reference/casework-series-roadmap.md) — Series B, C and D, scoped but not planned
- [Plan review](reference/plan-review.md) — how a Planner outline gets checked: `plan-lint` for the counting, an independent read for the judgement, and the standing ledger for Series A
- Craft dossiers: [Fisher](reference/fisher-craft.md) · [Hildebrandt](reference/hildebrandt-craft.md) · [Harford](reference/harford-craft.md) · [Sapolsky](reference/sapolsky-craft.md)
