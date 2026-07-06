# Delivery-profile process — feed a clip in, get numbers out

**Purpose.** Turn a subjective note ("it sounds flat," "it doesn't pause enough to let
a scene land") into a **measured diff** between a real narrator and our generated audio,
so we know *which knob to turn and by how much*. It converts the two standing complaints
into two scores:

- **Flatness score** — how much less pitch/energy variation our audio has vs the reference.
- **Pause-deficit score** — how much less (and less *well-placed*) silence our audio has.

This is an **evaluation/tuning harness**, not part of the shipped pipeline. It runs on the
**render box** (needs audio libraries + optionally the GPU) and is **eval-only**: a couple
of the best analysis models are CC-BY-NC / research-licensed, so this code stays out of the
MIT `prosodia` package (keep it under `experiments/` or a separate `prosodia-eval` extra).

---

## The prosody profile (~20 numbers per clip)

Each clip is reduced to one vector. The metrics that matter for our two problems:

### Register / pitch  → the *flatness* complaint
| metric | meaning | tool |
|---|---|---|
| `f0_median_hz` / `f0_median_st` | overall pitch height (semitones = comparable across voices) | Parselmouth |
| **`f0_sd_st`** | **pitch variation in semitones — the core flatness number** (low = monotone) | Parselmouth |
| `low_register_frac` | fraction of voiced time spent below the speaker's own median | Parselmouth |
| `register_offset_st` | how much lower the reference sits than us (the "uses his low end" gap) | Parselmouth |
| `f0_cv` | pitch coefficient of variation (dynamics, normalized) | Parselmouth |

### Pacing / pause  → the *digest-pause* complaint
| metric | meaning | tool |
|---|---|---|
| `speech_rate_wpm` | words per minute (excludes silence) | WhisperX |
| `long_pause_per_min` | count of pauses ≥ ~600 ms per minute | silero-VAD + WhisperX |
| `pause_ratio` | total silence ÷ total duration | silero-VAD |
| **`long_pause_midsentence_frac`** | **fraction of long pauses that fall MID-CLAUSE, not at punctuation** | WhisperX word timings |
| `interword_gap_cv` | how variable the gaps between words are (robotic = low) | WhisperX |

### Energy / emotion  → corroborates flatness
| metric | meaning | tool |
|---|---|---|
| `rms_dyn_range_db` | loudness dynamic range (quiet↔loud spread) | librosa |
| `arousal_mean` / **`arousal_std`** | activation level and its **variation over time** (expressiveness) | openSMILE eGeMAPS + audeering SER* |
| `loudness_cv` | loudness variation | openSMILE eGeMAPS |

\* audeering's SER model is **CC-BY-NC-SA — evaluation only**, do not ship. openSMILE
eGeMAPS + librosa alone already give a usable energy read if we want a clean-license subset.

**The standout metric is `long_pause_midsentence_frac`.** A real narrator drops long beats
*mid-clause* — right after the image lands — to let you picture it; flat TTS only pauses at
commas and periods. That single number is exactly the "not enough time to imagine the
scenario" complaint, it's measurable, and it maps straight to a tone-specialist action
(add mid-sentence `{pause}`), which is why we already wrote that rule into `tone.md`.

---

## Toolchain (all pip-installable, Windows + CUDA ok)

| layer | library | gives us |
|---|---|---|
| pitch / register | **Parselmouth** (Praat) | F0 track → median, SD, low-register fraction, all in semitones |
| words + timing | **WhisperX** | word-level timestamps → rate + *where* each pause falls |
| pauses | **silero-VAD** | speech/silence segmentation → pause counts, durations, ratio |
| energy / emotion | **openSMILE** (eGeMAPS) + **librosa**; optional **audeering** SER | loudness dynamics, arousal + its variance |
| parallel-clip metrics (optional) | **TTS-Objective-Metrics** | F0-RMSE / MCD when comparing the *same* script |

Two comparison modes:
- **Distributional** (our case): reference and generated say *different words* (a Carlin
  clip vs one of our episodes) → compare the summary vectors + distances. This is the mode
  the harness defaults to.
- **Parallel** (optional, sharper): make the reference narrator's *exact* words our
  transcript, render it, and compare frame-aligned (DTW + F0-RMSE/MCD). Best for A/B-ing a
  parameter change against a ground-truth reading of the same text.

---

## The process (what you actually do)

1. **Reference clip.** Cut 30–120 s of the target narrator at his characteristic delivery
   (mono, ≥16 kHz, clean). For our two problems, pick a passage where he uses his low
   register *and* a scene-setting beat with real pauses — those are the stress tests.
2. **Generated clip.** Render a comparable passage (similar tone/length) with the current
   `voice_profiles.yaml` + reference voice clip.
3. **Extract.** Run the harness on both → two profile vectors (JSON).
4. **Diff → scores.** The harness prints the per-metric deltas plus the two headline
   scores (Flatness, Pause-deficit) and flags the biggest contributors.
5. **Read the deltas → act on the right lever:**
   - `f0_sd_st` / `arousal_std` / `rms_dyn_range_db` low → **flatness**: raise `exaggeration`
     for the tones in play (we just did this globally); if still flat, it's model-level
     (reference clip / engine — see `tts-engine-landscape.md`).
   - `register_offset_st` / `low_register_frac` low → **register**: not a tone-table knob —
     use a **lower reference clip**, a formant-preserving pitch-down of the clip, or a
     fine-tune. Chatterbox takes register only from the reference.
   - `long_pause_per_min` / `long_pause_midsentence_frac` low → **pacing**: tell the tone
     specialist to add longer, mid-clause `{pause}` at digest beats (rule now in `tone.md`),
     or raise the default `beat_ms`.
6. **Re-render, re-measure, iterate** until the deltas close. The scores give you a stopping
   condition instead of guessing by ear.

---

## Status & effort

- **Not built yet.** ~1 day to stand up on the render box (deps + a `profile.py` extractor
  and a `diff.py` reporter). Deferred by choice — we're doing the cheap prompt/table fixes
  first and will build this if they don't fully close the gap, or when we want a hard
  stopping condition for tuning.
- Maps to `DESIGN.md` naturalness-eval / Phase-4 tuning.
- Fits the project's rule that **the transcript stays the source of truth**: this only
  *measures* output and *advises* the (deterministic) tone table + the tone specialist —
  it never rewrites the transcript.
