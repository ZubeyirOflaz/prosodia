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
- [Job protocol](../protocol/SPEC.md) — the synced job-folder contract (canonical)
- [Glossary](glossary.md) — terms used across the docs

## Project

- [Evaluation & testing](evaluation.md) — the automated suite and the A/B method
- [A/B scoring sheet](AB_TESTING.md) — Prosodia vs NotebookLM
- [Roadmap & status](roadmap.md) — what's done, what's open
- [Repair plan](../REPAIR_PLAN.md) — tracked fixes and remaining items
