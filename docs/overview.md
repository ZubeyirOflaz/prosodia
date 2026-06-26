# Overview

[← Docs index](README.md)

**Prosodia** turns a transcript you fully control — annotated with performance
directions (tone, speed, pauses, emphasis) — into narrated audio, using a
decoupled, swappable text-to-speech engine that runs on your own GPU.

## Why it exists

Tools like **NotebookLM** generate audio that is only *indirectly* controllable.
For long-form, multi-episode narrative content (think Dan Carlin's *Hardcore
History*), that produces four recurring problems:

1. **Uncontrollable transcript** — wrong emphasis, narrative breaks, synthetic dialogue.
2. **Forced two-person format** — constant speaker-switching that breaks focus.
3. **Content ↔ speech disconnect** — delivery that misses the content's ideal emotion: absent pauses, near-interruptions, synthetic flow.
4. **Poor multi-episode coverage** — series that skip or repeat large sections.

See [Features](features.md) for how each is addressed, and [DESIGN.md §2](../DESIGN.md)
for the original framing.

## The thesis

**Decouple the script from the voice.** A human (with an LLM's help) writes a
transcript that is the *single source of truth* and carries explicit per-section
delivery intent; a separate, pluggable TTS engine voices **exactly** that —
nothing downstream re-interprets it.

The key difference from a NotebookLM "source": that is an *input an AI expands*
into the real audio. A Prosodia transcript **is** the final script — spoken
verbatim. See the [Transcript format](../formats/SPEC.md).

## Two sides, one synced folder

```
Author a transcript            →     Render to audio
(any machine, no GPU)                (Windows + NVIDIA GPU)
plan · write · compile · submit      watch · render → episode.wav
            └──────────  synced folder (inbox/ … outbox/)  ──────────┘
```

- **Authoring** runs anywhere — pure-Python, no torch.
- **Rendering** runs on a machine with an NVIDIA GPU (Chatterbox first).
- The two exchange jobs through a [cloud-synced folder](HANDOFF.md), so you can
  write remotely and render on the GPU box.

For how the pieces fit together, read [Architecture](architecture.md).

## Status

Pre-alpha PoC. The authoring side is built and tested end-to-end (a worked
example lives in `projects/eu_history/`); the renderer is built and awaits its
first audio run on the GPU machine. Details in [Roadmap & status](roadmap.md).

## See also

[Getting started](getting-started.md) · [Architecture](architecture.md) ·
[Features](features.md) · [DESIGN.md](../DESIGN.md)
