# Craft sourcing — how a persona's soul gets built from a real corpus

**Purpose.** Turn "we should write like X" into a **traceable, role-partitioned craft
reference** distilled from X's own words, so a persona's role prompts are grounded in
observed technique rather than in our impression of a reputation. The output of this
process is a `docs/reference/<slug>-craft.md` dossier per source; the first one written
by hand, before this process existed, is [`carlin-craft.md`](carlin-craft.md) — the shape
it settled on is what this document generalizes.

**Why it exists.** A persona is ~400 lines of prompt that will shape hundreds of hours of
audio. Getting the soul wrong is expensive and invisible: the prompts still *read* fine.
Two failure modes forced this process:

1. **The reputation trap.** We nearly adopted a teacher whose method was perfect on paper
   and whose long-form work turned out to be paywalled, panel-based, and impossible to
   attribute to one voice. A soul we cannot read is a style we would have invented and
   attached to a famous name.
2. **The generic trap.** "Uses concrete examples", "defines terms clearly", "builds from
   the familiar" are true of every good teacher. They cost prompt budget and discriminate
   nothing. A dossier must separate a source's **differentia** from generic good teaching.

---

## The three source roles, and what each one has to clear

A roster mixes sources doing different jobs, and **the bar depends on the job**. Decide the job
first; the gate follows from it. A source hired for one job is never "failing" the bar of a job
it was not hired for.

| Role | What it supplies | What its corpus has to support |
|---|---|---|
| **Soul** | The persona's overall voice and method — the thing everything else is fitted to | **Gate 0, all four tests.** A whole style is being reconstructed, so the corpus must be big enough to corroborate claims across it, attributable to one voice, and built to teach |
| **Content source** | Substance, framing, a way of looking at the subject | Enough primary text to evidence the frame accurately and quote it correctly. Delivery is irrelevant, so audio and caption quality do not apply |
| **Device source** | One or a few named techniques, borrowed and named | Enough corpus to evidence **that technique** and show its shape. Nothing more. It need not be designed for a remote audience, need not be a whole course, and need not clear Gate 0 |

A device source clearing only its own bar is the normal case, not a compromised one. What
matters is whether the borrowed technique is **in harmony with the soul's method** — a judgment
made at synthesis, against the persona's aim, not against the source's completeness.

## Gate 0 — soul eligibility

Run this **only** on a candidate for the soul role. It is not a quality score and it is not run
on content or device sources except to record, for the file, what their corpus would and would
not support if someone later proposed promoting them.

| Test | Bar | Why |
|---|---|---|
| **Obtainable** | ≥ 10 h or ≥ 100k words of primary corpus, downloadable without institutional access | Below that, claims cannot be corroborated across the corpus |
| **Single voice** | The corpus is dominated by one speaker; panels/interviews disqualify unless the target's turns can be cleanly separated | Otherwise style is unattributable |
| **Designed** | Built to teach an audience, not an artefact of circumstance (a course, a broadcast series, a written curriculum) | Incidental recordings encode room dynamics, not method |
| **Self-described** *(bonus, decisive when present)* | The source has published an account of their own pedagogy | Removes our inference from the loop |

Record the result in the dossier's §0 either way, for a candidate soul. It is how we avoid
re-litigating a rejected candidate three sessions later — and, for a device source, how a future
reader knows what the corpus could and could not be asked to do.

---

## Stages

**1 — Manifest & acquire.** Write `experiments/craft_sourcing/sources/<slug>.json`: the
person, the **one job they are hired for**, a permission note, and every corpus item typed
`youtube` / `pdf` / `html`. Then `fetch.py` pulls it into a gitignored staging area,
normalizes each item to plain text, and records sha256 + word count + duration per item, so
any later claim can be traced to a file. YouTube items fetch **subtitles only** — never
video — and keep both tracks: the *manual* track is punctuated (usable for prose metrics),
the *auto* track carries inline word timestamps (the only route to pause structure without
downloading audio).

**2 — Measure.** `profile.py <slug>` produces the numbers: prose shape (sentence length
distribution, question rate, address rates, hedging), delivery (see caveats below), and
**mined verbatim habits** — the most frequent sentence openers, repeated 4-grams, and
capitalised markers. The mining matters: it yields a source's actual transition vocabulary
rather than our paraphrase of it, and it has already contradicted an assumption we held.

**3 — Independent reads.** *k* analysts run [`roles/craft_analyst.md`](../src/prosodia/author/roles/craft_analyst.md)
over **disjoint slices** of the corpus, blind to each other: k = 6 for a soul, 3 for a
support source. Disjoint and blind is the point — it is what makes step 4 meaningful.
(`carlin-craft.md` was distilled from six such reads.)

**3b — Verify, when you cannot be several people.** Independent reads need readers blind to one
another. Where only one analyst is available, run a **verification pass** instead and label it as
such: take every structural claim already written and test it by mechanical count against the
**whole** corpus rather than the slices that produced it. It addresses the same risk from the
other side — a claim generalised from a handful of sampled items must survive a count over all of
them — and it is cheap, repeatable and honest about what it is. On its first run it falsified one
claim and softened another out of ten tested.

It does **not** substitute for independent discovery: a count can only test claims someone
already thought to write down. Record the distinction rather than blurring it.

**3c — Discover on held-out material.** Verification and discovery are different jobs needing
different passes. A count tests claims that already exist; it can never find a technique nobody
thought to look for. So reserve part of every corpus and, late in the process, read it **cold,
with one instruction: find what the dossier does not contain.**

This is not optional polish. On its first two runs it found **eight** new techniques in one source
and **five** in another — after four and two passes respectively had already been run on them — and
in one case it overturned the picture, revealing a narrative habit that sampled openings and
closings had made invisible. Verification had turned up nothing new in either, because that is not
what verification is for.

Practical rule: sample openings and endings for structure, count across everything for frequency,
and read **whole items you have never opened** for discovery. The three passes see different things.

**4 — Distil.** Keep a claim only if **≥ 2 analysts found it independently**; demote
singletons to `[Inferred]`; drop anything neither can evidence. Then run the **adversarial
pass**: for every surviving claim, ask *would this be true of any competent teacher in this
field?* If yes, it is generic — cut it, however true. What remains is the differentia.

**5 — Write the dossier.** One tracked file, `docs/reference/<slug>-craft.md`, in the
schema the analyst role defines (§0–§I). Sections are named for the persona file they
feed, so synthesis is a merge rather than a fresh interpretation.

**6 — Synthesize** (once per persona, not per source). Merge the dossiers into role
prompts under three rules:

- **Job precedence.** Each source is authoritative *only* for the job it was hired for.
  Where two collide outside their assigned jobs, the persona's aim statement decides;
  inside an overlap, `[Observed]` beats `[Inferred]`.
- **Budget.** The writer prompt has a working ceiling around 170 lines (`thinkers` is 166).
  Each dossier may nominate at most ~12 candidate lines in §H; synthesis keeps roughly 40
  across all roles. Prompts degrade as they grow — cutting is part of the method.
- **No inheritance by default.** Do not carry another persona's tone vocabulary, defaults or
  freshness watchlist across. Fisher's most frequent sentence opener is `"in other words,"`
  — which is on the `thinkers` off-limits list. In a narrative-idea persona it is a lazy
  tic; in a doctrinal-teaching persona it is the load-bearing restatement move. Same words,
  opposite verdict, decided by the persona's job.

---

## Dossiers are self-contained — a hard rule

**A dossier describes one person and nobody else.** It may not compare its source to another
source, may not cite another dossier, and may not decide what the persona will do with what it
finds. Its §G may record what a technique would *cost* to convert to single-narrator audio,
because that is a property of the source and the medium; it may not record a preference between
sources.

The reason is practical. Stage 6 is where sources get mixed, and mixing is the step most likely
to change: a source gets dropped, a job gets reassigned, a fifth source arrives. If comparison
lives inside the dossiers, every one of those changes invalidates several dossiers at once and
the corpus has to be re-read. Keep the per-source records independent and any of them can be
revised, re-run, or discarded alone.

So: comparisons, precedence, conflict resolution and mix-and-match all live **here**, in the
synthesis rules above, or in the synthesis output — never in a `*-craft.md`. A dossier that
starts arguing for its own source has stopped being evidence.

---

## Confidence labels

Every non-obvious claim in a dossier carries one, matching the convention already used in
the study-materials project:

- **`[Observed]`** — verbatim evidence quoted in §I, with a locator.
- **`[Inferred]`** — a pattern across the corpus that no single quote proves.
- **`[Unverified]`** — from secondary description (a review, a summary, a search result).
  **Must be resolved or deleted before synthesis.** Unverified claims are how a reputation
  becomes a prompt.

---

## Delivery numbers, and what they are worth

Metric names deliberately match [`prosody-profiling.md`](prosody-profiling.md), so a
source's profile can serve as the **target vector** when tuning a persona's
`voice_profiles.yaml` against real narration — the calibration that doc calls for.

Caption-derived measurement is cheap and repeatable but is a **proxy**, valid for ranking
sources measured the same way, *not* directly comparable to the VAD-based numbers the
render-box harness produces. Known biases, all currently live:

- `speech_rate_wpm` from the manual track (words ÷ runtime) is the trustworthy figure. The
  word-timing rate under-counts, because the first word of each auto-caption cue sits
  outside the timestamp tags.
- `pause_ratio` and `long_pause_per_min` use a threshold relative to the corpus-median word
  interval, so they are internally consistent and absolutely uncalibrated.
- `long_pause_midsentence_frac` aligns the five words before each gap against the punctuated
  track; it reports `null` below 20 successful alignments.
- **Caption quality varies enormously by source and gates which metrics mean anything.** The
  profiler measures `punctuation_density` (sentence terminators per 100 words) and suppresses
  every sentence-level figure below 1.5. One source so far has professional human captions at
  ~5.2 marks per 100 words; another has auto-captions only, at a median of **0.04** — no
  punctuation at all. For an unpunctuated corpus, ratios per 1,000 words still hold (numerator
  and denominator are affected equally), and sentence length, question rate and
  `long_pause_midsentence_frac` are **unavailable, not approximate**. That last one silently
  reads `1.0` on unpunctuated text, because with no terminators to align against, every gap
  classifies as mid-sentence. Check the density before believing any figure.
- **Auto-caption text needs line-level dedup, not cue-level.** YouTube's rolling display repeats
  each line across consecutive cues, so joining cue bodies roughly **doubles** the text and
  inflates every count. `fetch.py` dedupes lines against a lookback window; a corpus extracted
  before that fix will read about twice its true length.
- Excerpts from an auto-captioned corpus are usable as evidence of **phrasing patterns**, never
  as exact wording — the transcription mangles technical terms and proper nouns. Say so in the
  dossier, at the top, where a reader cannot miss it.

Audio is only needed for pitch and energy — `f0_sd_st`, `arousal_std`, register — which
captions cannot see at all. Leave those cells empty rather than guessing.

---

## Hygiene

- **Never commit a raw corpus.** Third-party transcripts, captions and PDFs stay in
  `experiments/craft_sourcing/corpus/` (gitignored), as the research docket does for a
  project. The distilled dossier is our own work and is tracked — the same split that keeps
  `research/` out and `plan/outline.md` in.
- Acquire only what a person could obtain themselves, and record how, in §0.
- The dossier is for **style**, which is not ownable; it must never become a channel for
  reproducing a source's content. If a dossier starts quoting paragraphs rather than
  characterising moves, it has drifted.

---

## Roster status — all five dossiers

| source | role | passes | state |
|---|---|---|---|
| [`carlin`](carlin-craft.md) | soul (an earlier persona) | 6 independent analyses | complete, and the pattern this process generalises |
| [`fisher`](fisher-craft.md) | architecture | **5 of 6** | verification (§J) and held-out discovery (§K) done; the sixth pass needs a reader who has not seen the file |
| [`hildebrandt`](hildebrandt-craft.md) | content — the gaze | **3 of 3** | complete |
| [`harford`](harford-craft.md) | cases | **3 of 3** | complete |
| [`sapolsky`](sapolsky-craft.md) | device — levels of causation | **3 of 3** | complete |

Every dossier is self-contained: no cross-references between them, and no decisions about which
persona uses what. **Stages 4 and 6 now have an output** —
[`casework-synthesis.md`](casework-synthesis.md) — which is where every comparison between sources
lives, along with the persona's written aim statement (the tiebreaker the synthesis rules assume
and which did not exist until then), the adversarial pass results, the resolved conflicts, and four
costed ways of combining the four sources.

**What no single analyst can finish.** The `≥2 independent analysts` rule is unmet everywhere. It
is substituted for by two things that do work alone — full-corpus verification and held-out
discovery — and the dossiers say so in their own §J and §K sections rather than claiming
corroboration they do not have.

## Detail

- Process and tooling built. `fetch.py` and `profile.py` are stdlib + `curl`/`yt-dlp`/
  `pdftotext`, standalone under `experiments/` by the same rule that keeps the prosody
  harness out of the MIT package.
- **Run for:** `fisher` — 40 lecture segments (≈17 h, 150k caption words) plus his own
  pedagogy paper, exam and maps → [`fisher-craft.md`](fisher-craft.md), **pass 5 of 6** — a
  full-corpus verification pass (§J) and a held-out discovery pass (§K). The sixth is a read by
  someone who has not seen the file, which one analyst cannot supply.
  Pass 2 read his written account of the course design in full and it earned its keep: it
  corrected a pass-1 conclusion drawn from a metric (a 3% question rate read as temperament,
  where he states it is a deliberate channel split), fixed a miscount, and supplied §E almost
  entirely from his own stated principles. **Read a source's self-description before trusting
  any inference from their corpus** — it is the cheapest pass and the one that overturns things.
- **Run for:** `sapolsky` — 25 Stanford lectures (36.7 h, 355k words of auto-captions) →
  [`sapolsky-craft.md`](sapolsky-craft.md), **complete at pass 3 of 3** — a **device source**,
  hired for one technique. Per-lecture counting showed most of his apparent habits were localised
  and that pass 1's "method lexicon" was measuring his syllabus; the single device he was hired
  for is also the only one present in all 25 lectures. His corpus is an unedited residential lecture course, which is all a device source
  needs. Running him also exposed the two caption-quality problems
  now documented above — worth knowing that the second source, not the first, is what stresses
  the tooling.
- **Run for:** `hildebrandt` — the complete open-access book (11 chapters, 113k words of her own
  prose) plus her master-course syllabus → [`hildebrandt-craft.md`](hildebrandt-craft.md), **complete at
  pass 3 of 3**, a **content source**. The first **written** corpus, which forced three tooling fixes:
  browser headers (several academic hosts refuse a bare curl but serve an ordinary browser — a
  fetch-mechanics problem, not a licence one), support for corpora with no captions at all, and
  truncation of publisher **open peer-review threads**, which are other people's words on the
  author's own URL and the clearest route to a misattributed quotation this process has met.
- **Run for:** `harford` — 3 episodes transcribed locally and analysed →
  [`harford-craft.md`](harford-craft.md), **complete at pass 3 of 3** over 7 episodes. Extending the corpus
  from three episodes to seven **falsified three claims**, every one of them a generalisation
  from the episode that had been read most closely — the sharpest evidence yet for why single-item
  close reading needs a count behind it. No transcripts of his work exist — verified, not assumed:
  neither the real Cautionary Tales feed (265 episodes, found via the Apple lookup API) nor the
  BBC feed for *50 Things* carries `podcast:transcript` tags, and the YouTube uploads offer
  auto-captions only, at **0.17** marks per 100 words. The fix is `transcribe.py`, which reuses
  the `faster-whisper` this project already ships for the render-side quality gate and produces
  **8.04** marks per 100 words with proper nouns intact. **Local transcription is now the
  documented fallback for any source without human captions**, and it retroactively unblocks
  every auto-caption-only corpus. Transcription turned out far cheaper than expected — roughly
  two minutes per 37-minute episode with `small`/int8 on CPU — so a thin corpus is no longer a
  reason to accept auto-captions anywhere.
- **Dropped from the roster:** `oneill` and `ian-shapiro`. Both were queued as device sources and
  neither was started; the roster is the five dossiers above. Either can be revived cheaply — the
  tooling handles both, BBC answers `curl`, and Open Yale needs only the browser headers now built
  into `fetch.py`.
  Acquisition notes for each are in §0 of their dossiers as they land.
