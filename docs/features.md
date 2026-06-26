# Features

[← Docs index](README.md)

What Prosodia does, mapped to the four problems it targets (the [Overview](overview.md)
explains the problems) and the meta-goals.

## Against the four problems

| # | Problem | Feature |
|---|---------|---------|
| 1 | Uncontrollable transcript | The [transcript](../formats/SPEC.md) is the **source of truth**, spoken **verbatim**. The compiler records both `authored_text` and `spoken_text`; nothing downstream rephrases it. |
| 2 | Forced two-person format | **Single narrator by default**; optional two-host via `@speaker` tags (parsed today; per-speaker voicing is on the [roadmap](roadmap.md)). |
| 3 | Content ↔ speech disconnect | **Per-section delivery intent** (`tone`, `rate`, `note`) compiled to engine params, plus **real silence** for paragraph/beat/explicit pauses. |
| 4 | Poor multi-episode coverage | A series **coverage map** in [`series.yaml`](configuration.md) assigns every topic to exactly one episode; the [Planner](pipeline-and-traces.md) enforces no-gaps/no-overlap. |

## Meta-goals

- **Decoupled, pluggable engine** (#5) — engine-neutral intent + a derived render
  plan; Chatterbox first, behind a `TTSBackend` interface. See [Architecture](architecture.md).
- **Remote authoring, no GPU** (#6) — the authoring side is pure-Python; the
  packaging enforces a torch-free base install.
- **Simple GPU setup** (#7) — two scripts ([Renderer setup](../scripts/RENDERER_SETUP.md)).

## Authoring features

- **Headless multi-agent loop** — Planner → Writer ⇄ Editor → Tone specialist,
  driven by Claude Code on your subscription (no API key). [Pipeline & traces](pipeline-and-traces.md).
- **Hybrid transcript format** — prose-first, with beat-level `{tone, rate}`
  directives, `{pause: N}`, and `*emphasis*`. [Format spec](../formats/SPEC.md).
- **Text normalization** — numbers, years, ranges, `§`, era abbreviations → spoken form.
- **Pronunciation lexicon** — per-project respelling of proper nouns.
- **Provenance traces** — every stage writes a versioned artifact + a trace line,
  so feedback routes to the stage that caused an issue.

## Rendering features

- **Sentence-aware chunking** under the engine's per-generation cap.
- **Quality gate** — STT-validated candidate selection catches hallucinated/garbled
  chunks (final mode); a fast-preview mode for quick iteration. [Rendering](rendering.md).
- **Click-free joins** — lead/trail trim + short crossfade; pauses as real silence.
- **Loudness normalization** — one EBU R128 pass over the final audio.
- **Atomic handoff** — the renderer claims a job only when its manifest validates
  (sha256 + size), so a half-synced job is never grabbed. [Job protocol](../protocol/SPEC.md).
- **Warm model + watcher** — the model loads once; the watcher renders jobs as they arrive.

## See also

[Overview](overview.md) · [Architecture](architecture.md) ·
[Getting started](getting-started.md) · [Roadmap & status](roadmap.md)
