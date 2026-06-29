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
| `target_minutes` | long-form length the Writer aims for (per-episode `target_minutes` overrides) |
| `episodes` | list of `{ n, slug, title, scope, tension, target_minutes? }` — every topic assigned to exactly one episode |

`scope` defines an episode's boundaries (so later episodes don't re-explain earlier
material); `tension` is the dramatic hook the Writer emphasizes.

## Tone table

The **Tone specialist's** deterministic table (`src/prosodia/author/voice_profiles.yaml`)
and the **single source of truth** for the tone vocabulary and default pauses.
Maps each engine-neutral tone word to Chatterbox params:

```yaml
engine: chatterbox
pace: 0.9          # global speed dial: scales every cfg_weight (<1 = slower)
pauses:            # default silence durations (ms) — the one place these live
  paragraph_ms: 600
  beat_ms: 1200
default_tone: measured   # fallback for an unknown tone (the compiler warns)
tones:
  somber:   { exaggeration: 0.30, cfg_weight: 0.34, temperature: 0.70 }
  dramatic: { exaggeration: 0.78, cfg_weight: 0.30, temperature: 0.85 }
  # ... measured, neutral, warm, grave, wistful, reverent, tense, urgent, wry, matter-of-fact
```

These are **starting anchors** to tune per voice. Chatterbox coupling: higher
`exaggeration` speeds speech; lower `cfg_weight` makes delivery more deliberate —
the pairs already account for that interaction. Editing this file re-tunes the
whole show's delivery without touching any transcript.

**Pace levers, strongest first** (the show felt too fast → slow it here):
`pauses` (real silence between segments) → `pace` (one global dial) → a beat's
`rate: slow` (lowers its cfg via the backend) → individual `cfg_weight` values.

## Pronunciation lexicon

Per-project respellings, applied to `spoken_text` only (the transcript stays
readable). Longer keys win; matching is whole-word.

```yaml
lexicon:
  Monnet: "Mon-nay"
  Ruhr: "Roor"
  Maastricht: "Mahs-trikt"
```

Respellings are approximate and meant to be tuned against the chosen voice.

## Voices

Each project owns its narrator clips at `projects/<proj>/voices/<name>.wav` (10s+,
clean, single speaker, ≥24 kHz). Naming matches the `voice` id, so `voice:
narrator` → `voices/narrator.wav`.

`prosodia submit` **auto-bundles** the matching clip into the job, so the clip
travels with it and the render box needs no extra flags (a bundled clip is
preferred over the `--voices` dir; `submit --voice-ref <wav>` overrides). The same
reference is reused across every chunk and episode — the primary defense against
timbre drift.

Chatterbox clones zero-shot (no training) — just supply the clip. To cut one from
a longer recording, use [`prosodia voice-prep`](cli-reference.md#prosodia-voice-prep)
(needs the `audio` extra: `pip install "prosodia[audio]"`):

```bash
prosodia voice-prep narration.wav --start 1:30 \
  --out projects/eu_history/voices/narrator.wav
```

It cuts a ~10s clip from the given timestamp, ending at a natural pause, downmixed
to mono. Only clone voices you have the rights to; every render carries
Chatterbox's inaudible watermark.

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
