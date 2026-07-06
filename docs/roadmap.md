# Roadmap & status

[← Docs index](README.md)

Pre-alpha PoC. The full phase plan is [DESIGN.md §6](../DESIGN.md); resolved
decisions are [DESIGN.md §11](../DESIGN.md); tracked fixes are
[REPAIR_PLAN.md](../REPAIR_PLAN.md).

## Done (built and tested)

- **Authoring pipeline** end-to-end: Planner / Writer ⇄ Editor / Tone specialist
  ([pipeline](pipeline-and-traces.md)), plus `compile` and `submit`.
- **Contracts**: IR, render plan, intent vocabulary, [job protocol](../protocol/SPEC.md)
  with manifest-based atomic claim, and the trace log.
- **Tone table**, **normalization**, **pronunciation lexicon**, sentence-aware **chunking**.
- **Renderer** (code): Chatterbox backend, pause/trim/crossfade assembly, STT
  quality gate, loudness normalization, the inbox **watcher**, and Windows
  **setup scripts**.
- **Worked example**: `projects/eu_history/` — episode 1 authored, compiled (33
  segments), and packaged into a job that validates.
- **Delivery-quality pass**: an LLM **tone specialist** ([`roles/tone.md`](../src/prosodia/author/roles/tone.md))
  run with a word-invariance check, plus a retuned `voice_profiles.yaml` — raised
  `exaggeration` to cure flatness, mid-clause digest pauses — applied to
  `projects/eu_history_v2/` (5 episodes).
- A test suite ([evaluation](evaluation.md)) and this documentation set.

## Open — needs the GPU box

- **First end-to-end audio run** on the RTX 3080 (the render path is unit-tested
  but unproven on hardware).
- **B1 / B2** ([REPAIR_PLAN](../REPAIR_PLAN.md)): the `[render]` extra / CUDA torch
  ordering and the Python-version pin — validated by `prosodia-render doctor` on
  the box.
- **A/B vs NotebookLM** on EU ep1–3 ([evaluation](evaluation.md), [A/B sheet](AB_TESTING.md)).

## Open — features

- **Two-host rendering**: `@speaker` tags are parsed and validated into the IR, but
  the renderer voices the whole episode with one voice — per-speaker voice
  resolution and turn-taking gaps are not yet wired.
- **Chapter metadata & per-episode output filenames** (today: a flat `episode.wav`).
- **`rate` as true time-stretch** (today: coupled onto `cfg_weight`).
- **Coverage lint** (today: the Planner produces the map; no automated checker).

## Later (behind the pluggable interface)

- **Phase 4** delivery tuning (calibrate `voice_profiles.yaml` against the chosen
  voice); cloud backends (Gemini multi-speaker, ElevenLabs) for a GPU-off path;
  multilingual narration. See [DESIGN.md §10/§6](../DESIGN.md).

## Delivery quality — deferred improvement ladder

Two known gaps vs the real narrator: **flatness / underuse of the low register**, and **too
little pause** at digest / "imagine the scene" moments. The shipped tone-specialist retune
(above) is step 0; the rest is a cheapest-first ladder — stop as soon as it's good by ear.

1. **🔜 Reference-clip engineering** — a neutral, calm clip already carries the low register
   at its natural baseline; if the clone still sits too high, a formant-preserving pitch-down
   of ~2–3 semitones. The clip sets register *center*; `exaggeration` sets *movement* —
   separate knobs, so no low-vs-full-range trade-off. Cost: a few renders.
2. **⏸ Prosody-profiling harness** — reference-vs-generated diff → a **Flatness score** and a
   **Pause-deficit score** that name the exact knob; a stopping condition for tuning.
   Eval-only, ~1 day on the render box. → [`reference/prosody-profiling.md`](reference/prosody-profiling.md)
3. **⏸ Alternative TTS engines** — if Chatterbox can't reach the target: MOSS-TTS (native
   timed pauses), IndexTTS2 (emotion control), GPT-SoVITS (MIT drop-in, register via a deeper
   reference). A/B one episode vs Chatterbox. → [`reference/tts-engine-landscape.md`](reference/tts-engine-landscape.md)
4. **🧊 LoRA fine-tune of Chatterbox** — the strongest register lever but the highest
   commitment (rent a ≥16 GB GPU to train, serve on the 3080). Last resort.

## See also

[Repair plan](../REPAIR_PLAN.md) · [DESIGN.md](../DESIGN.md) ·
[Evaluation & testing](evaluation.md) · [Features](features.md)
