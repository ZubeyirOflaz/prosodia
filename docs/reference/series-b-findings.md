# Series B review — findings and decisions (October 2026)

A full review of *The Collisions* (casework Series B, ten episodes) against its persona, the
pipeline that produced it, and the renders of earlier series. Recorded **before** the changes it
proposes, so that each fix can be checked against the problem it was meant to solve.

| | |
|---|---|
| Reviewed | 2026-10-06 |
| Material | `projects/collisions` Eps 1–10 (transcripts, editor verdicts per round, compiled IR); 29 rendered episodes of `eu_history_v2` and `political_thinkers` for calibration |
| Method | full read of the scripts; editor records per round; measurements on the compiled IR and on real MP3 durations |

## Status at a glance

| # | Finding | Status |
|---|---|---|
| 1 | The engine speaks at **~170 wpm**; everything assumes 130 | **Fixed** 2026-10-09 — `atempo` 0.90 on the finished episode, chosen by ear |
| 2 | The tone specialist was never part of `write` | **Fixed** 2026-10-06 |
| 3 | Quotations delivered in the wrong voice, recurring | **Fixed** 2026-10-06 (blockquote = scoped quotation) |
| 4 | Mid-sentence pauses: are they used well? | **Yes — keep them** (user decision) |
| 5 | Every pause and paragraph splits the render | **Built** 2026-10-09 — inner pauses spliced into one generation (IR 0.2) |
| 6 | Background noise drops out between chunks | **Built** 2026-10-09; edges fixed 2026-10-14 — the loud part was the lead-in, raised ~33 dB by `loudnorm` |
| 7 | Renderer writes `episode.wav`; MP3s are made by hand | **Fixed** 2026-10-09 — titled, tagged MP3 |
| 8 | Editor improvements never reach the writer | **Fixed** 2026-10-09 — a ready verdict ends on a writer pass too; the editor's previous verdict is still not passed back |
| 9 | The same first-draft defects cost a round each episode | Proposed — not built |
| 10 | Prompt wording spoken as boilerplate across episodes | Proposed — not built |
| 11 | Long sentences | Proposed — not built |
| 12 | Smaller items, and accuracy defects shipped in Series B | Open |

---

## 1. Speech rate: 170 wpm, not 130

**Measured**, from the real duration of every rendered episode with a matching IR, minus authored
silence and the 8 s of lead/tail:

| | renders | median | range |
|---|---|---|---|
| `eu_history_v2` (hardcore-history) | 8 | **172 wpm** | 162–173 |
| `political_thinkers` (thinkers) | 21 | **170 wpm** | 166–176 |

**Everything is built on 130.** The casework persona's delivery target (`voice_profiles.yaml`,
from `casework-synthesis.md` §4.3 — the audio-native craft source sits at 127), the writer's
word-budget table (`writer.md` LENGTH), `scriptlint._WORDS_PER_MINUTE`, and every runtime
reported in review. So:

- **Episodes are ~20–25% shorter in audio than planned.** Collisions Ep 5 (brief 34 min) renders
  to about 29½ min; Ep 8 (brief 38) to about 36 — after the tone pass's added pauses.
- **The narration is faster than the persona was designed for.** The benchmarks (Harford 127,
  Fisher 137) were measured as **words ÷ total runtime, pauses included**; on that basis the toned
  Collisions Ep 8 projects to **~154 wpm overall** — about 15–20% too fast (an earlier "30%"
  compared the speaking rate with an overall rate). For dense legal material heard while
  travelling that is a comprehension problem, not a length problem. The user confirmed it:
  trouble keeping up while listening on the move, previously put down to the listening
  conditions.

**The `pace` dial does not control speed.** It scales `cfg_weight` (`render/pacing.py`), and the
persona with the *slower* settings renders *faster*: hardcore-history (pace 0.90, measured cfg
0.40) at 172 wpm, thinkers (0.95, 0.44) at 170. Casework (0.93, 0.44) sits between them and will
land at ~170 too. The roadmap already lists **"`rate` as true time-stretch"** as open.

**Native levers, measured (2026-10-06).** The user asked for a native slowdown before any
artificial one. Three Political Thinkers renders whose exact IR and render plan survive in
`outbox/` were cut back into their 213 paused stretches (inserted silence is digital zero; a
monotonic alignment matched each authored pause in order), giving the speaking rate of each
stretch against the settings that produced it:

| tone | exaggeration | effective cfg | stretches | median wpm |
|---|---|---|---|---|
| grave | 0.50 | 0.285 | 40 | 170 |
| contemplative | 0.44 | 0.342 | 38 | 165 |
| tense | 0.64 | 0.380 | 14 | 162 |
| measured | 0.48 | 0.418 | 50 | 173 |
| curious | 0.58 | 0.437 | 19 | 163 |
| lucid | 0.50 | 0.456 | 31 | 176 |

- **`cfg_weight` barely moves the rate**: a weighted fit gives ~8 wpm across 0.285–0.456. Even
  extrapolated to the 0.20 floor (below which Chatterbox slurs, `pacing.py`) it does not approach
  130.
- **`exaggeration` shows no effect** across 0.44–0.64; lowering it further is what caused the
  flatness fixed in mid-2026.
- **The reference clip does not set the tempo either — tested 2026-10-09.** The casework clip is
  byte-identical to the Political Thinkers clip (so ~170 wpm is this voice). It was time-stretched with
  ffmpeg `rubberband` (pitch preserved) to 0.85× and 0.75×, i.e. a clip speaking at ~134 and ~119 wpm
  instead of ~158, and the same 161 words of Collisions Ep 8 were rendered with each — casework
  `measured` settings, two matched seeds, chunked as the renderer does, on the authoring laptop's CPU
  (`.venv-render`; the model is the same as on the render box, so tempo results transfer):

  | reference clip | output wpm (seed 101 · 102) | mean | intelligibility (faster-whisper) | voice similarity to original |
  |---|---|---|---|---|
  | original (~158 wpm) | 159.3 · 169.6 | **164** | 0.956 | 0.974 |
  | 0.85× (~134 wpm) | 167.5 · 163.7 | **166** | 0.956 | 0.959 |
  | 0.75× (~119 wpm) | 165.2 · 150.6 | **158** | 0.956 · 0.979 | 0.954 |

  A clip 15–25% slower moved the output by 0–4%, inside the ~10 wpm spread between two seeds of the
  *same* clip. Chatterbox clones the voice, not the pace. The earlier reading — clip ~159 → output ~170,
  other clip ~154 → ~170 — was in fact evidence of a model-default rate, over-read as clip transfer. A
  naturally slow read (with its own pauses and prosody) is not strictly ruled out, but the direct test of
  tempo transfer is negative. Outputs kept for listening in the session scratchpad
  (`clipslow/out_clip*.wav`); script `clipslow/run.py`.
- **Pauses help but cannot do it alone**: reaching ~130 overall from a 170 speaking rate would
  need about a third of the runtime to be silence.

**So there is no native speed lever in Chatterbox** — `cfg_weight` is weak, `exaggeration` and the
reference clip are inert, and it has no speed or duration parameter. **Native control means another
engine**, behind the pluggable backend (`tts-engine-landscape.md`): **MOSS-TTS** (token-count duration
control *and* authorable timed pauses inside one generation — which would also solve §5; Apache-2.0) or
**GPT-SoVITS** (a real `speed_factor`; MIT code, weights to audit). IndexTTS2's duration control is
disabled in its public release.

**A removed speed control, found 2026-10-09.** Chatterbox builds audio in stages: text → speech
tokens (T3) → mel spectrogram (S3Gen flow) → waveform (HiFT vocoder). Its S3Gen stage comes from
CosyVoice, whose speed control **interpolates the mel spectrogram in time before the vocoder** — and
Chatterbox's own code says it dropped it: `chatterbox/models/s3gen/s3gen.py:289`, *"TODO jrm: ignoring
the speed control (mel interpolation) and the HiFTGAN caching mechanisms for now."* Restoring it is a
small change in our backend (interpolate `output_mels` along time, then `hift_inference`). Because the
vocoder synthesises the waveform — and predicts pitch from the mel — afresh, it should avoid the
phase-vocoder artefact heard on the stretched reference clips (below). Unverified by ear. Caveat:
uniform interpolation lengthens consonants as much as vowels, where a naturally slower speaker mostly
lengthens vowels and pauses — mild at 0.85–0.9, to be judged.

**What the stretched clips sounded like.** The user heard "a micro reverb in the voice" on the 0.85× and
0.75× reference clips. That is the classic **phasiness** of a phase-vocoder stretch: ffmpeg's `rubberband`
filter exposes only Rubber Band's older engine, run here on default settings. Any after-the-fact stretch
of finished audio carries some of it, scaled by the amount of stretch. The speaker-similarity score
(0.96 / 0.95) barely registered it — it measures identity, not artefacts.

**Decision and fix (2026-10-09).** Four post-hoc stretchers were compared by ear on the same take
(Rubber Band old engine, Rubber Band 4.0 R3 "finer", Praat PSOLA, ffmpeg `atempo`), each at 90% and
85%. **The user judged `atempo` "the best one by far", and 90% the right amount** — below it the
artefacts become clear "and the speech feels like it drags on without any reason". Built: every
persona's `voice_profiles.yaml` sets `tempo: 0.90`; the value travels in each job's `render_plan.json`
(`RenderPlan.tempo`, default 1.0 for plans written before it existed); the renderer applies `atempo`
in the same ffmpeg pass as loudness normalisation, so the whole episode — speech and authored pauses —
plays at 0.9×. `prosodia-render doctor` now fails if ffmpeg lacks `atempo` or `libmp3lame`, because
the fallback is a WAV with no tempo. The mel-interpolation route above stays untested.

**Options that were considered within Chatterbox:**
- **Slow the audio** — pitch-preserving time-stretch (WSOLA / phase vocoder) of each generation,
  or of the whole episode, toward the persona's target. Keeps the scripts as they are; quality
  cost of stretching ~0.75× to be judged by ear.
- **Write to the real rate** — re-base the word budgets on 170 wpm. Fixes length, not speed.
- **Both** — stretch to the comprehension target and budget words for it.

## 2. The tone specialist was never in the pipeline — fixed

`roles/tone.md` was written and tuned against measured narration, run **once by hand** for
`eu_history_v2`, and never called by `prosodia write`. `orchestrate.py` loaded only planner,
writer and editor. Both casework series (22 episodes) shipped with the writer's markup alone.
The compile step logged an event labelled `tone-specialist` that was in fact the deterministic
render plan, so traces showed a pass that never ran.

**What it cost, measured on Series B:**

| | |
|---|---|
| mid-sentence pauses | **0** in 22 casework episodes (235 pauses, all at line ends); `eu_history_v2`, toned by hand, had 153 — all mid-sentence |
| `pointed` (meant for one sentence) used as a whole-beat tone | 21 beats, **~57 min of a 375-min series**; the machine beat headed `pointed` in 8 of 10 |
| `quoting` on beat headers | 7 beats, ~17 min of the narrator's gloss in the statute's voice |
| `grave` on machinery | 3 beats |

**Built:** `write` runs the pass after the editor loop (`--no-tone` skips it); `prosodia tone`
applies it to existing transcripts. Every attempt is checked mechanically — a changed spoken word
or beat title rejects it, with the difference quoted back on the retry; delivery errors from
`scriptlint.lint_delivery` (sentence tones on headers, directive-set `quoting`, `pointed` spans
over 45 words, no mid-sentence pause) earn one retry. The render-plan event is relabelled
`render-plan`.

**First runs** (`prosodia tone` on Collisions Eps 5 and 8, both clean on the first attempt):

| | Ep 8 before → after | Ep 5 before → after |
|---|---|---|
| delivery errors | 5 → 0 | 3 → 0 |
| words in `pointed` | 1,298 → 281 | 577 → 187 |
| `pointed` followed by a pause | 4 → 20 of 21 | 4 → 14 of 14 |
| words in the quoting voice | 866 → 160 | 567 → 79 |
| quoting voice on non-instrument text | 22 segments → 0 | 12 → 0 |
| mid-sentence pauses | 0 → 107 | 0 → 51 |
| spoken words changed | none | none |

`grave`/`somber` moved onto human stakes only (Elaine Herzberg; the man refused a loan) and off
the machinery. One instrument passage is still in the narrator's voice (Ep 8's damage-list
categories).

## 3. Quotations — fixed for good

**Why it kept coming back.** Every fix went into `tone.md`, which nothing read, while
`writer.md` — which is read — taught the defect in its own FORMAT example
(`## What the text actually says {tone: quoting, rate: slow}`). And every approach relied on a
writer remembering to switch off a tone that stays on until told otherwise (SPEC §5).

**Now:** a blockquote **is** the quotation (SPEC §5.2). The compiler reads `> ` lines as
`{tone: quoting, rate: slow}` and restores whatever delivery was in force when the blockquote
ends — the scope is the syntax, so it cannot leak. Only personas with a `quoting` tone are
affected. Both prompts say: quote in a blockquote, never set `quoting` with a directive.
`lint_delivery` makes a directive-set or header `quoting` an error the tone pass is retried on.

## 4. Mid-sentence pauses — used well; keep them

All 157 in toned Eps 5 and 8 were read: 66 after a comma, 56 after a dash, 2 after a semicolon,
33 with no punctuation. Nearly all do one of five jobs for an ear-only listener:

- **a term lands before its definition** — "The first is the controller — ‖ the organisation that determines…"
- **a hold before the payoff** — "a perfectly respectable way out ‖ when it is true"; "Not a mortgage — ‖ a phone."
- **the end of a long subject, before its verb** — "A firm that builds a driving system and drives it itself ‖ is the manufacturer of that system."
- **the two halves of a contrast** — "answering properly is a cost ‖ and answering thinly is free"
- **the rhythm of a sequence** — "long enough to brake, ‖ long enough to steer, ‖ long enough to do both"

About a dozen are neutral ("On the twenty-seventh of February 2025, ‖"); none works against
meaning. **Decision: do not reduce the count.** An earlier suggestion to cut the 300 ms ones was
wrong — it rested on the weakest example. Density: Ep 8 now has 41.6 pause directives per 1,000
words; `eu_history_v2` Ep 8 (already rendered) has 38.4.

Every one of these jobs depends on the voice signalling *the sentence is not finished*. That is
exactly what §5 threatens.

## 5. Every pause and paragraph splits the render

**Mechanism.** The IR can only express a pause as `pause_before_ms` on a segment, so the compiler
ends the segment at every `{pause}`, every paragraph break and every tone directive
(`compile.py`). The renderer makes one independent `ChatterboxTTS.generate()` call per chunk,
conditioned only on the reference clip — no knowledge of the words on either side — trims it,
inserts the pause as silence, and joins (`render.py`). Chatterbox has no pause token.

**So chunks are short, and it is not the 300-character cap doing it:**

| | median chunk | ≈ speech | under 100 chars | ended by a segment boundary (not the cap) |
|---|---|---|---|---|
| `political_thinkers` (rendered) | 207 chars | 12.6 s | 16% | 50% |
| `eu_history_v2` (rendered, toned) | 122 | 7.4 s | 43% | 82% |
| Collisions, writer markup | 174 | 10.6 s | 24% | 76% |
| Collisions Eps 5+8 after tone pass | **83** | **5.1 s** | **59%** | **98%** |

Ep 8 went from 152 segments to 349, 43 of them four words or fewer.

**Consequences:**
- A mid-sentence cut is rendered as if it were a complete utterance, so the half before the pause
  tends to end like a full stop — turning a hold before a payoff into two sentences (§4).
- Very short inputs are where Chatterbox is least stable and the faster-whisper gate least reliable.
- Every join is a background-noise discontinuity (§6).

**Proposed (approved in principle, not built):**
1. **Split only where generation parameters change** (tone, rate, speaker) or at the cap. Pauses
   and paragraph breaks become **inner pauses**: a position in the spoken text and a duration,
   carried in the IR. Text is packed across them up to the cap.
2. **Give the engine a natural boundary.** 124 of the 157 mid-sentence pauses already follow a
   comma or dash; for the rest, the compiler adds a comma to the *spoken* text only (the
   transcript is untouched, as with number normalisation). Paragraph pauses already fall at
   sentence ends.
3. **Splice the silence into the one generation.** Find the gap Chatterbox left at that
   boundary — nearest low-energy gap to the expected time, or faster-whisper word timestamps
   where the gate already runs — and stretch it to the authored duration. If no gap is close
   enough, that one pause falls back to a split, and is logged.
4. **Engine-neutral:** the IR says "N ms after this word"; an engine with native timed pauses
   (MOSS-TTS, `tts-engine-landscape.md`) uses them directly.

**Validation:** splice logic unit-tested on synthetic audio here; then an A/B render on the
render box (Chatterbox is not installed on the authoring laptop, and must not be — CLAUDE.md):
the same paragraphs rendered split and spliced.

**Built 2026-10-09** (agreed 6 October, then skipped when the tempo/MP3 change was done ahead of
it — see the audit note in `docs/roadmap.md`):
- **Compiler** (`compile.py`): a segment ends only where the delivery changes (a directive that
  *changes* tone/rate/note, a speaker tag, a quotation's edges) or at a beat. `{pause}` and
  paragraph breaks inside it become `Segment.chunk_pauses` — "N ms after the k-th word of this
  chunk" (IR 0.2). The spoken text before a mid-sentence pause gains a comma if it has no
  punctuation. Series C Ep 1: **286 segments → 113; ~290 generations → 171** (median 188 chars);
  generations of four words or fewer **21 → 2**; 161 pauses, 139 inside a generation.
- **Renderer** (`render.py`, `splice.py`): generate every chunk first, then measure room tone,
  splice, assemble. A pause's gap is found by aligning the text's punctuation with the audio's
  gaps in order (long gaps preferred — on real narration punctuation gaps ran 200–750 ms, gaps
  inside a sentence under ~150 ms) and lengthened to the authored duration. **Fallback differs from
  the design above:** a pause whose gap cannot be found keeps the engine's own pause and is
  logged, rather than re-rendering the chunk split — a split is the very cut this removes, and the
  comma already gives a short pause. Word timestamps from the faster-whisper gate are not used.
- Old (IR 0.1) jobs still render: their pauses are room-tone gaps between generations.

## 6. Background noise drops out between chunks

**Observed by the user:** each generation carries background noise inherited from the reference
clip; the joins between chunks have none, and that is audible. More splits (§5) would make it
worse.

**Mechanism** (`render/audio.py`):
- every inserted silence — paragraph (550 ms), beat (1,100 ms), each `{pause}`, the title gap and
  the 4 s lead/tail — is **digital zero** (`silence()` is `np.zeros`);
- each chunk is trimmed below −40 dBFS (keeping 50 ms), so its own noise tail is cut;
- each generation's noise differs a little in level and colour;
- loudness normalisation (EBU R128, −16 LUFS) runs on the whole episode and raises the noise
  floor under speech while the zeros stay zero — widening the contrast.

**User's proposal:** estimate the background noise from Chatterbox's own output and add it under
the whole episode as a final pass. Options, as analysed:

- **(a) Fill the gaps with matched room tone** — estimate the noise spectrum from the quiet
  stretches inside the generated chunks; synthesise noise with that spectrum (or overlap-add real
  noise excerpts); put it in every inserted silence instead of zeros, crossfaded at the edges.
  Leaves the speech untouched; removes the holes directly. **Recommended first.**
- **(b) Denoise every chunk, then lay one continuous bed** under the whole episode. Gives a
  perfectly uniform floor; risks denoising artefacts on the voice.
- **(c) Add a bed over everything without removing anything.** Under speech the noise roughly
  doubles in power (uncorrelated) while gaps get the bed alone — a ~3 dB step remains where today
  there is a drop to zero. Better than now; not seamless on its own.
- **(d) Upstream:** a cleaner reference clip (`prosodia voice-prep`) gives the generations less
  noise to begin with. Risk: a denoised reference can make the clone sound processed.

§5 reduces the number of joins, but splicing still inserts silence, so (a) is needed either way.

**Built 2026-10-09 as option (a); the cause of "far too strong" found and fixed 2026-10-14.**
`audio.RoomTone` estimates a spectrum and level from the quietest frames inside the generated chunks
and fills the silences with matching noise. The user's verdict on the first real render (Series B
Ep 1): "way too strong and … much worse than the silence we had". Measured on that render:

| | level |
|---|---|
| speech (95th percentile) | −11 dB |
| the engine's own background between words | −48.5 dB |
| all 629 pauses inside the episode (room tone) | −48 to −50 dB median, none 10 dB above background |
| **the 4 s lead-in** | **−17 dB** |
| the tail | −49 rising to −45 dB |

So the fill was right everywhere except the edges. The finishing pass is single-pass `loudnorm`,
which sets its gain over a few seconds at a time: a lead-in of pure noise has no speech in that
window, and it was raised ~33 dB, to nearly the level of the speech; the tail was starting to rise
the same way. Digital zero cannot be raised, which is why the edges were silent before.
**Fix:** the lead-in and tail are digital silence again; room tone fills only the silences inside the
episode. On real Chatterbox chunks the estimate lands within 1 dB of the background between words.
A test renders through the real `loudnorm` and fails if either edge is not silent or a pause comes
out louder than the background. For listening, the user's Ep 1 with only its edges silenced was
written to `~/Downloads/1. The Same File, Twice - edges silenced.mp3`.

Kept from the same change: a pause inside a generation keeps the engine's own short gap and its
background — no trim to −40 dB and hard cut at each pause, as when every pause split the render.

## 7. Output format

The renderer writes `episode.wav` (`render/cli.py`, `watch_and_render.py`). The MP3s in
`outbox/` — 24 kHz mono, ~70 kbps, named like `7. The Science of Rise and Fall.mp3` — were made
by hand. **Fixed 2026-10-09:** given the job folder, the renderer writes `"N. Title.mp3"` itself —
LAME VBR mono at 24 kHz (~72 kbps on real narration, matching the hand-made files), ID3 title and
track, characters Windows refuses removed. An explicit `.wav` path still writes a WAV. The roadmap's open
item **"Chapter metadata & per-episode output filenames"** covers it; chapter marks per beat would
let a travelling listener skip back to the start of a passage.

## 8. Editor improvements never reach the writer

- When the editor returns `ready`, the loop **breaks**: that verdict's IMPROVEMENTS go to no one.
  About ninety shipped this way across Series B.
- `editor-notes.md` is written only when an episode ends **not** ready; a ready episode's notes
  live only under the gitignored `run/`.
- `editor.md` tells the editor IMPROVEMENTS "go to a human". No such step exists.
- Where improvements *were* passed back (non-final rounds), about three quarters of the sentences
  the editor quoted had changed by the next draft. **The writer does not ignore them; the
  pipeline never delivers the last ones.**

**Accuracy defects were filed as improvements.** Ep 9: two retrieval answers teach the
Product Liability Directive without its conditions — a defendant who "flatly refuses to hand over
its logs" gets "a presumed defect" (Art. 10(2)(a) bites only on a failure to disclose under
Art. 9(1), which requires court proceedings and a plausible claim); "the maker escapes **only** by
proving the defect came from complying" (Art. 11(1) has seven exemptions; Art. 10(5) lets any
presumption be rebutted). Those sentences were in all three drafts; rounds 1–2 did not flag them;
round 3 did, as IMPROVEMENTS, and returned `ready`.

**Why:** each editor round reads from scratch — brief and current draft only, not its own earlier
notes — so each round finds a different partial set (Eps 2 and 10 found a new real defect every
round); and `editor.md` pushes hard toward `ready` while promising a human will handle the rest.

**Proposed:** a writer pass on accuracy items even when the verdict is `ready`; tell the editor
what actually happens to each section; make a retrieval or change-one-fact answer that drops a
rule's condition BLOCKING; give the editor its previous verdict; always write `editor-notes.md`.

**Built 2026-10-09**, after Series C Ep 1 was approved in round 2 with seven improvements unapplied
(among them a prompt echo and a claim the plan does not make). The 14 September change had added a
final writer pass only for a loop that runs out of rounds — the literal request — although the
reason given for it ("if the process ends with editors but no changes are made, the last editor
round will always be a very expensive but low return review session") covers a ready verdict
just as well.
- A `ready` verdict whose `IMPROVEMENTS` section has content now gets one final writer pass with
  that section only (not BLOCKING or CLEARED), told to skip items meant for the producer.
- Nobody reviews that pass, so if it adds script-lint errors the approved draft is kept and the run
  is marked `warn`.
- `editor.md` now says what happens to each section: IMPROVEMENTS are applied on trust, so anything
  that must be fixed *and checked* — including a retrieval or change-one-fact answer that drops a
  rule's condition — is BLOCKING.
- `editor-notes.md` is written for every episode, and says whether the final pass applied the notes.
- Not built: handing the editor its previous verdict.

## 9. The same first-draft defects, every episode

Flagged as BLOCKING and fixed the next round each time — they cost rounds, not quality:
spoken lists over three (round 1 of five episodes, two in the "describe the system step by step"
beat); **announced counts that were wrong** (four episodes — "eleven words" that were eight,
"three terms" followed by four, a recap with the wrong number of presumptions); holdings restated
without their qualifier (stopped after the `writer.md` fix, Eps 4–9 clean; returned in the verdict,
which compresses earlier episodes from memory). Not recurring: forward references and the
"not X, Y" tic — Series A's main problems — produced no blocks.

**Proposed** one line each in `writer.md`: check every announced count; describe the system in at
most three stages; carry an earlier episode's qualifier when recalling it.

## 10. Prompt wording spoken as boilerplate

Phrases from the persona's own prompts, recurring across episodes: "before any rule touches"
(6/10, `writer.md` spine beat 3), "in the same breath" (6/10, the limit rule), "you do not need
[that today]" (6/10, the deferral example), "which rule actually bites, who it binds, and what
falls through" (6/10, `series.yaml` angle), "I'm not going to read you" (5/10).

**It can be caught from episode 1** — the source is known before any episode exists. A
"prompt-echo" check (word sequences a script shares with its persona prompts and `series.yaml`,
minus anything in the docket) flagged every recurring phrase except one paraphrase, each on its
first appearance (by Eps 1–4). It would feed the editor like the banned-phrase list.
`lint-repetition` covers phrases the writer invents, after the fact.

## 11. Long sentences — general, not legal

| | median | ≥30 words | ≥45 words |
|---|---|---|---|
| `political_thinkers` | 14 | 15.7% | 3.5% (374 narrator sentences) |
| `eu_history_v2` | 11 | 10.8% | 1.8% |
| casework Series A | 12 | 7.5% | 1.0% |
| casework Series B | 12 | 6.1% | 0.6% |

Casework is the tightest of the four. The legal material adds one specific cause — long verbatim
quotations (now set apart by a blockquote, with a pause each side). **Proposed:** a check that
quotes any narrator sentence over ~40 words back to the editor; it would serve every persona.

## 12. Smaller items, and what shipped in Series B

- Ep 9 opens on a jurisdiction caveat and Ep 5 spends its second paragraph on a sourcing caveat —
  both before the hook.
- The lens spine has no retrieval beats; Ep 6 has none.
- Lists written as fragments ("Vehicle. Bicycle. Unknown object.") pass the comma-based
  enumeration check.
- `writer.md`'s pre-flight says "Four counts" and lists five.
- Shipped accuracy defects: Ep 9's two retrieval answers (§8); Ep 1 "nine months apart" (eight);
  Ep 6 "a judgment from last February — from 2025".
- **Instrument numbers are read inconsistently** (`normalize.py`). The number after the slash is
  sometimes read as a pair and sometimes in full: `2024/1689` → "twenty twenty-four slash sixteen
  eighty-nine", but `2024/2853` → "…slash two thousand eight hundred fifty-three" and `2016/679` →
  "…slash six hundred seventy-nine". `COM(2022) 496` keeps its brackets and reads "COM" as a
  word. Found 2026-10-07 in the clip-tempo test passage (Collisions Ep 8).

## Corrections to what was reported during the work

- The line added to `tone.md` "so writers stop" putting `quoting` on beat headers had **no
  effect** — nothing read that file. Eps 4, 5, 8 and 9 were written after it and all did it again.
- Runtimes reported for Series B used 130 wpm and were ~20–25% too long (§1).
- The suggestion to reduce short mid-sentence pauses was wrong (§4).
