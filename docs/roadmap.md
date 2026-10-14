# Roadmap & status

[← Docs index](README.md)

Pre-alpha PoC. The full phase plan is [DESIGN.md §6](../DESIGN.md); resolved
decisions are [DESIGN.md §11](../DESIGN.md); tracked fixes are
[REPAIR_PLAN.md](../REPAIR_PLAN.md).

## Done (built and tested)

- **Authoring pipeline** end-to-end: Planner / Writer ⇄ Editor / Tone specialist
  ([pipeline](pipeline-and-traces.md)), plus `compile` and `submit`. *The tone specialist was
  listed here but only became part of `write` on 2026-10-06; before that it had been run once by
  hand — see [Series B findings §2](reference/series-b-findings.md).*
- **Contracts**: IR, render plan, intent vocabulary, [job protocol](../protocol/SPEC.md)
  with manifest-based atomic claim, and the trace log.
- **Tone table**, **normalization**, **pronunciation lexicon**, sentence-aware **chunking**.
- **Renderer** (code): Chatterbox backend, pause/trim/crossfade assembly, STT
  quality gate, loudness normalization, the inbox **watcher**, and Windows
  **setup scripts**.
- **Worked example**: `projects/eu_history/` — episode 1 authored, compiled (33
  segments), and packaged into a job that validates.
- **Personas + docket-driven planning**: switchable authoring personas
  (`hardcore-history`, `thinkers`); the Planner builds from a per-project
  [research docket](configuration.md#research-docket) and honors a series-level
  `scope:`. First `thinkers` series `projects/political_thinkers/` ("The Long
  Argument") — a 20-episode outline plus episodes 1–2 authored and compiled.
- **Authoring UI** (`prosodia ui`): a dependency-free local dashboard — browse
  projects/episodes with status, run planner/writer as live serialized jobs, compile,
  edit transcripts (save + recompile), repetition-lint, and run deterministic
  diagnosis; reuses the existing trace/outline HTML, and the trace view is
  **interactive** (lazy artifact drill-down, segment→round links, re-run a stage).
  Std-lib server + a ~60-line in-house htmx-style JS layer, no new deps. See
  [Authoring UI](authoring-ui.md).
- **Delivery-quality pass**: an LLM **tone specialist** ([`roles/tone.md`](../src/prosodia/author/personas/hardcore-history/roles/tone.md))
  run with a word-invariance check, plus a retuned `voice_profiles.yaml` — raised
  `exaggeration` to cure flatness, mid-clause digest pauses — applied to
  `projects/eu_history_v2/` (5 episodes). Applied by hand at the time; now run by `write` and
  by `prosodia tone`, with a word-invariance check and `scriptlint.lint_delivery`.
- A test suite ([evaluation](evaluation.md)) and this documentation set.

## Agreed or proposed, not yet built — audit of 2026-10-09

An audit of the whole casework session (10 Sept – 9 Oct) found agreed work that had quietly not
happened: the final writer pass on a `ready` verdict (agreed 14 Sept in its reason, built only for
the round-limit case), pauses inside one generation and room tone (agreed 6 Oct, skipped when the
tempo/MP3 change went first), and a half-applied HTML-comment fix in script-lint. All four were
built on 2026-10-09. What remains, kept apart so "proposed" is not read as "decided":

**Agreed, not yet done**
- **Visual-study handoff log** — the 10 Sept instruction to append useful material to
  `~/Documents/tum_ais_studies/06_visual_study_material/HANDOFF.md` lapsed after day one. Candidates
  since: the load-bearing terms with their likely wrong readings (flashcards), Hildebrandt's
  four-step spine, the series question ledgers, `references.md`, the four *Digital Rights Ireland*
  defects.

**Proposed on 6 Oct ([Series B findings §8–11](reference/series-b-findings.md)), never decided**
- Hand the editor its previous verdict.
- One line each in `writer.md`: check announced counts; describe a system in at most three stages;
  keep a rule's qualifier when recalling it; caveats after the hook; a listening frame before a
  long quotation; retrieval beats in lens episodes.
- A prompt-echo check (phrases a script shares with its own persona prompt) — Series C Ep 1 had one.
- The recurring prompt phrases on the watchlist; an enumeration check for fragment lists.
- A check that sends narrator sentences over ~40 words back to the editor.
- Restage Series B at 0.9× tempo (the toned Eps 5 and 8 were held for the pause splice, now built).

**Raised 13 Sept, never decided**
- An unreadable editor verdict counts as `ready` with a green trace (a test certifies it).
- Re-running `write` reuses the run folder and overwrites the earlier run's drafts.
- `test_boundary.py`'s torch test can never fail.

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
- **Chapter metadata** — per-beat chapter marks in the MP3. *(Per-episode output filenames are
  done: the renderer writes "N. Title.mp3", [Series B findings §7](reference/series-b-findings.md).)*
- **`rate` as true time-stretch** — the per-beat `rate` is still coupled onto `cfg_weight`, which
  barely changes speed. The *episode* tempo is fixed (`atempo` 0.90 at render,
  [Series B findings §1](reference/series-b-findings.md)); a per-beat equivalent would need
  mel interpolation inside the backend, which Chatterbox's authors left out.
- *(Done 2026-10-09: pauses inside one generation, and room tone in the silences inside an episode;
  its loud lead-in fixed 2026-10-14 — [Series B findings §5–6](reference/series-b-findings.md).)*
- **Room tone that follows the pause** — today the fill plays 10 dB under the background everywhere,
  a stopgap: at full level a long pause was exposed hiss. Better: background level at a pause's seams,
  fading to silence in its middle; or a cleaner reference clip, which fixes it at the source
  ([Series B findings §6](reference/series-b-findings.md)).
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

[Series B findings](reference/series-b-findings.md) · [Repair plan](../REPAIR_PLAN.md) · [DESIGN.md](../DESIGN.md) ·
[Evaluation & testing](evaluation.md) · [Features](features.md)
