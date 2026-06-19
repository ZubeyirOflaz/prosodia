# Prosodia

**Script-first, controllable narrated audio.** Prosodia turns a transcript you fully control — annotated with performance directions like tone, speed, and pauses — into narrated audio using a decoupled, swappable text-to-speech engine running on your own GPU.

> ⚠️ **Early / work in progress.** The design is settled and documented in [`DESIGN.md`](DESIGN.md); implementation is just beginning.

## Why

Tools like NotebookLM generate audio that is only *indirectly* controllable. For long-form, multi-episode narrative content that causes recurring problems:

1. **Uncontrollable transcript** — wrong emphasis, narrative breaks, synthetic-feeling dialogue.
2. **Forced two-person format** — constant speaker-switching that breaks listener focus.
3. **Content↔speech disconnect** — delivery that doesn't match the content's ideal emotion; missing pauses, near-interruptions, synthetic flow.
4. **Poor multi-episode coverage** — series that skip or repeat large sections across episodes.

Prosodia's approach: **decouple the script from the voice.** A human (with an LLM's help) writes a transcript that is the single source of truth and carries explicit per-section delivery guidance; a separate, pluggable TTS engine voices exactly that.

## How it works

```
Author a transcript          →   Render to audio
(human-edited, with tone/         (decoupled, pluggable TTS;
 speed/pause directions)          Chatterbox on a local GPU)
```

- **Authoring** runs anywhere (no GPU required).
- **Rendering** runs on a machine with an NVIDIA GPU.
- The two sides exchange jobs through a synced folder, so you can write remotely and render on the GPU box.

The default is a **single narrator** (optional multi-speaker), the TTS engine is **pluggable** (local [Chatterbox](https://github.com/resemble-ai/chatterbox) first; cloud engines later), and voices can be **preset or cloned**.

See [`DESIGN.md`](DESIGN.md) for the full architecture, decisions, and build plan.

## Status

Pre-alpha. Architecture and decisions are documented; the authoring and rendering pipelines are being built. Not yet usable end-to-end.

## License

MIT — see [`LICENSE`](LICENSE).
