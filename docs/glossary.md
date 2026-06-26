# Glossary

[← Docs index](README.md)

- **Transcript** — the human-editable source of truth, in the [hybrid format](../formats/SPEC.md);
  spoken verbatim.
- **Beat** — a `## title {directives}` section; the unit of delivery intent and a
  (future) chapter marker. The title is not spoken.
- **Segment** — a contiguous run of speech with one intent and no internal pause;
  one IR record. Pauses become the `pause_before_ms` of the next segment.
- **Intent** — engine-neutral delivery: `tone`, `rate`, and free-text `note`.
- **Tone / rate** — emotional delivery word (e.g. `somber`) / pace word (e.g. `slow`).
- **IR (intermediate representation)** — the compiled transcript
  (`prosodia.core.ir.EpisodeIR`): segments with `authored_text`, `spoken_text`,
  `pause_before_ms`, `emphasis`, and `chunks`.
- **Render plan** — the derived, engine-specific params per segment
  (`RenderPlan` / `SegmentParams`); produced by the Tone specialist, consumed by
  the renderer. Kept separate from the IR so the transcript stays engine-portable.
- **Tone specialist** — the mapping layer (intent → engine params); v0.1 is a
  deterministic [table](configuration.md#voice_profilesyaml-the-tone-table).
- **Chunk** — a ~300-char piece of `spoken_text` sized for the engine's
  per-generation cap.
- **Normalization** — compile-time conversion of numbers/dates/symbols to spoken form.
- **Lexicon** — per-project pronunciation respelling of proper nouns.
- **Voice reference** — a `.wav` clip the engine clones; reused across the series
  to prevent timbre drift.
- **Job** — a directory (`ir.json`, `render_plan.json`, optional voice clip,
  `manifest.json`) exchanged through the synced folder.
- **Manifest** — sha256 + size of every payload file; the **atomic claim** gate
  (the renderer claims a job only when it validates).
- **Exchange root** — the synced folder holding `inbox/ processing/ outbox/ failed/`.
- **Fast preview / final** — render modes: 1 candidate, no STT / N candidates + STT gate.
- **Quality gate** — STT validation + candidate selection that rejects bad chunks.
- **Trace** — the append-only per-stage provenance log (`trace.jsonl`).
- **Coverage map** — the assignment of every topic to exactly one episode (in
  `series.yaml`).

## See also

[Architecture](architecture.md) · [Transcript format](../formats/SPEC.md) ·
[Job protocol](../protocol/SPEC.md)
