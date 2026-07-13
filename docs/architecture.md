# Architecture

[← Docs index](README.md)

Prosodia has two sides that never share a process and exchange work through a
synced folder. The **authoring** side is pure-Python (no GPU); the **render**
side needs an NVIDIA GPU. The boundary is enforced in packaging: the base install
has no torch, and the render dependencies live in a `[render]` extra.

## Data flow

```
                AUTHORING (any machine, no torch)                       RENDER (GPU box)
 series.yaml ─▶ Planner ─▶ outline ─▶ Writer ⇄ Editor ─▶ transcript.md
                                          (loop)              │
                                                              ▼ compile
                                   IR (ir.json) ◀── normalize + lexicon + chunk
                                          │
                                  Tone specialist
                                          │
                                          ▼
                              render_plan.json  ──┐
                                                  │ submit (manifest, atomic)
                              voice_ref.wav ──────┤
                                                  ▼
                                          inbox/<job>/  ───── synced ─────▶  watch + claim
                                                                                  │
                                                                                  ▼ render
                                                            chunk → generate → pause silence →
                                                            trim → crossfade → STT gate →
                                                            concat → loudness-normalize
                                                                                  │
                                          outbox/<job>/episode.wav  ◀── synced ───┘
```

## Components

### Authoring (`prosodia.author`)

A role-separated, traced pipeline driven by **headless Claude Code** (`claude -p`,
on your subscription — no API key):

- **Planner** → a series outline + coverage map (`series.yaml` is the seed).
- **Writer ⇄ Editor loop** → the episode transcript, revised until the Editor's
  structured `{ready, notes}` verdict passes.
- **Tone specialist** → compiles engine-neutral intent into engine parameters.

Then two deterministic, offline steps:

- **compile** (`author/compile.py`) → parses the transcript into the IR, applying
  [normalization](configuration.md#lexicon--normalization) and the pronunciation
  lexicon and chunking each segment.
- **submit** (`author/submit.py`) → packages a render job and publishes it
  atomically to the synced `inbox/`.

Full detail: [Pipeline & traces](pipeline-and-traces.md). Roles, loop, and CLI:
[Authoring guide](authoring-guide.md).

### The two-layer tone model

The transcript carries **engine-neutral delivery intent** (`tone`, `rate`,
`note`) — never engine knobs. The **Tone specialist** (`author/tone.py` + each
persona's `personas/<persona>/voice_profiles.yaml`) maps intent → Chatterbox params.
In v0.1 this is a
deterministic table; an optional LLM-driven Tone specialist can replace it behind
the same interface. The `render_plan.json` is a **derived** artifact, so the
transcript stays portable across engines (design goal #5).

### Render (`prosodia.render`)

A deterministic, LLM-free function of `(IR + render_plan + voice + seed)`:

- **backends** — a `TTSBackend` interface (`backends/base.py`) with a Chatterbox
  implementation (`backends/chatterbox_backend.py`), model loaded once and kept warm.
- **render loop** (`render.py`) — per segment: emit `pause_before_ms` of silence,
  render each chunk, [quality-gate](rendering.md#quality-gate) it, trim, crossfade-join.
- **quality** (`quality.py`) — faster-whisper STT validation + candidate selection.
- **audio** (`audio.py`) — silence, trim, crossfade, and a single final loudness
  normalization (ffmpeg).
- **watcher** (`watch_and_render.py`) — claims jobs whose manifest validates.

Details: [Rendering](rendering.md).

## Contracts (`prosodia.core`)

The shared, dependency-light artifacts both sides agree on, so neither can
silently reinterpret the other's output (goal #1):

| Contract | Where | What |
|---|---|---|
| **IR** | `core/ir.py` (`EpisodeIR`, `Segment`) | the compiled transcript: per-segment `intent`, `authored_text`, `spoken_text`, `pause_before_ms`, `emphasis`, `chunks` |
| **Render plan** | `core/ir.py` (`RenderPlan`, `SegmentParams`) | derived per-segment engine params |
| **Intent** | `core/intents.py` | engine-neutral `tone` / `rate` / `note` vocabulary |
| **Job protocol** | `core/protocol.py` → [`protocol/SPEC.md`](../protocol/SPEC.md) | folders, manifest, atomic claim |
| **Trace** | `core/trace.py` | append-only per-stage provenance log |

## Package layout

```
src/prosodia/
  core/     # shared contracts — pure-Python, no torch (imported by both sides)
  author/   # authoring — pure-Python, no torch; CLI: `prosodia`
  render/   # rendering — needs the [render] extra; CLI: `prosodia-render`
```

`pip install prosodia` gives the authoring side with **no torch**;
`pip install prosodia[render]` adds torch + Chatterbox + faster-whisper on the GPU
box. The boundary is regression-tested (`tests/test_boundary.py`).

## See also

[Pipeline & traces](pipeline-and-traces.md) · [Transcript format](../formats/SPEC.md) ·
[Job protocol](../protocol/SPEC.md) · [Configuration](configuration.md) ·
[DESIGN.md §11](../DESIGN.md) (resolved decisions)
