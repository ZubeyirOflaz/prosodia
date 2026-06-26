# Configuration

[← Docs index](README.md)

A **project** is a directory of one series. The EU example is the reference:

```
projects/eu_history/
  series.yaml            # series config + coverage map
  lexicon.yaml           # pronunciation respellings
  voices/                # narrator reference clips: <name>.wav  (you add these)
  plan/                  # Planner output: outline.md, trace.jsonl  (generated)
  episodes/
    ep1/
      transcript.md      # the source of truth (authored)
      ir.json            # compiled IR              (generated)
      render_plan.json   # derived engine params    (generated)
      trace.jsonl        # authoring provenance     (generated)
```

## `series.yaml`

Series-level config and the coverage map (goal #4). Fields:

| Field | Meaning |
|---|---|
| `series`, `description` | series name and one-line goal |
| `style` | house-style id, passed to the Writer |
| `engine` | target TTS engine (`chatterbox`) |
| `voice` | **default voice** for the series (a transcript may omit `voice` and inherit this) |
| `lexicon` | path to the pronunciation lexicon, relative to this file |
| `episodes` | list of `{ n, slug, title, scope, tension }` — every topic assigned to exactly one episode |

`scope` defines an episode's boundaries (so later episodes don't re-explain earlier
material); `tension` is the dramatic hook the Writer emphasizes.

## `voice_profiles.yaml` — the tone table

The **Tone specialist's** deterministic table (`src/prosodia/author/voice_profiles.yaml`)
and the **single source of truth** for the tone vocabulary and default pauses.
Maps each engine-neutral tone word to Chatterbox params:

```yaml
engine: chatterbox
pauses:            # default silence durations (ms) — the one place these live
  paragraph_ms: 400
  beat_ms: 800
default_tone: measured   # fallback for an unknown tone (the compiler warns)
tones:
  somber:   { exaggeration: 0.30, cfg_weight: 0.35, temperature: 0.70 }
  dramatic: { exaggeration: 0.80, cfg_weight: 0.30, temperature: 0.85 }
  # ... measured, neutral, warm, grave, wistful, reverent, tense, urgent, wry, matter-of-fact
```

These are **starting anchors** to tune per voice. Chatterbox coupling: higher
`exaggeration` speeds speech; lower `cfg_weight` makes delivery more deliberate —
the pairs already account for that interaction. Editing this file re-tunes the
whole show's delivery without touching any transcript.

## `lexicon.yaml` — pronunciation

Per-project respellings, applied to `spoken_text` only (the transcript stays
readable). Longer keys win; matching is whole-word.

```yaml
lexicon:
  Monnet: "Mon-nay"
  Ruhr: "Roor"
  Maastricht: "Mahs-trikt"
```

Respellings are approximate and meant to be tuned against the chosen voice.

## `voices/`

Narrator reference clips as `voices/<name>.wav` (10s+, clean, single speaker). A
job whose resolved `voice` is `narrator` renders against `voices/narrator.wav`. A
job may also bundle its own clip (via `prosodia submit --voice-ref`), which wins.
The same reference is reused across every chunk and episode — the primary defense
against timbre drift.

## Lexicon & normalization

- **Normalization** (`author/normalize.py`) converts numbers, 4-digit years,
  year ranges, `§` sections, and era abbreviations (WWII, BCE, …) to spoken form
  at compile time.
- The **lexicon** (`author/lexicon.py`) respells proper nouns.

Both run during `compile`, producing each segment's `spoken_text` alongside the
`authored_text`.

## Transcript front-matter

Per-episode settings live in the transcript's YAML front-matter (`voice`,
`episode`, `title`, `defaults`, `pauses`, `speakers`, `seed`). These are documented
in the [transcript format spec §3](../formats/SPEC.md). Precedence for `voice`:
instruction-time override → front-matter → `series.yaml` default.

## See also

[Authoring guide](authoring-guide.md) · [Transcript format](../formats/SPEC.md) ·
[CLI reference](cli-reference.md) · [Rendering](rendering.md)
