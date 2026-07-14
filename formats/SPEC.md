# Prosodia Transcript Format — SPEC v0.1

The transcript is the **source of truth**. It is written and edited by hand (with
an LLM's help), it is spoken **verbatim** — nothing downstream rephrases,
expands, or summarizes it — and it carries **engine-neutral delivery intent**
(tone, rate, pause, emphasis) that a later mapping layer compiles into a specific
TTS engine's settings. (Contrast with a NotebookLM "source": that is an *input*
an AI expands into the real audio. A Prosodia transcript *is* the script.)

This document defines the format precisely enough to parse unambiguously while
staying comfortable to read and edit.

---

## 1. Design principles

1. **Verbatim.** Every spoken word appears in the body, in order. The renderer
   speaks exactly the compiled text. Write at final length.
2. **Engine-neutral intent.** You describe *delivery* (somber, slow, a long
   beat) — never engine knobs (Chatterbox `exaggeration`, etc.). A separate,
   tunable mapping layer turns intent into engine settings, so transcripts stay
   portable across engines and durable across model upgrades.
3. **Mark only what the writing can't already imply.** Good prose carries most
   of its own prosody through word choice, sentence length, em-dashes, and
   rhetorical questions. Reach for an explicit directive only when the delivery
   you want would *not* be obvious from the words — a deliberate long pause, a
   tone the sentence alone wouldn't telegraph.
4. **The beat is the unit of tone.** Real TTS engines set emotional tone per
   *chunk*, not per word; tone shifts land cleanly at boundaries. So the format's
   primary structural unit — the **beat** — is also the unit of delivery intent.
   One beat = one consistent delivery, compiled to one IR segment.

---

## 2. File shape

A transcript is a UTF-8 Markdown file: a **YAML front-matter block** delimited by
`---`, followed by a **body** that is a sequence of **beats**.

```
---
format_version: "0.1"
voice: narrator
style: hardcore-history
episode: 1
title: "The Suicide of a Continent"
defaults: { tone: measured, rate: normal }
---

<!-- EPISODE TENSION: rock-bottom chapter; do not rush to the happy ending. -->

## The smell of the ruin   {tone: somber, rate: slow}
Picture the continent in the spring of 1945.
Not a map — a smell. {pause: 1.2}
Brick dust and cordite, and something worse underneath it.

## They thought it would happen again   {tone: tense}
And here is the thing they actually believed: they did not believe it was over.
They believed it might happen *again*.
```

---

## 3. Front-matter

YAML between the opening and closing `---`. Metadata only — **never spoken**.

| Field | Req? | Meaning |
|---|---|---|
| `format_version` | no | Format version this file targets (quote it — a bare `0.1` parses as a YAML float). Defaults to the current SPEC version. *In v0.1 it is advisory: the compiler neither records nor validates it.* |
| `voice` | no | Narrator voice id (a reference clip in the project's `voices/` folder, or `preset:<name>`). **Optional override** — if omitted, the voice is resolved from the project-config default. The renderer uses the *same* resolved reference for every chunk and episode (the primary defense against timbre drift). |
| `style` | no | Series house-style id. Guides **what the Writer writes**; ignored by the renderer. |
| `episode`, `title` | no | Episode number and title. *(v0.1: recorded in the IR for provenance; the renderer does not yet use them for chapter metadata or output filenames — the output is a flat `episode.wav`.)* |
| `defaults` | no | Default delivery intent for beats that don't override it (`tone`, `rate`). |
| `speakers` | no | For two-host mode only: maps `@speaker` names to voice ids, e.g. `{ narrator: anna, guest: ben }`. Omit for single-narrator (the default). |
| `pauses` | no | Override default pause durations (see §7), e.g. `{ paragraph: 0.4, beat: 0.8 }` (seconds). |
| `seed` | no | Integer seed for reproducible-ish renders. Omit to let the renderer pick and record one. |

**Voice resolution.** The narrator voice is resolved with this precedence:
(1) an explicit voice given at generation time (the instruction step) →
(2) front-matter `voice` → (3) the project config's default voice. The resolved
voice is recorded in the job, so a render is never ambiguous. Normally you set
the voice once in the project config and omit it from transcripts.

---

## 4. Beats and the body

- A **beat** begins with a level-2 heading: `## <beat title>  {<directives>}`.
  - The **title** is for you (navigation). It is **not spoken**. *(v0.1: it is
    stored in the IR but not yet emitted as a chapter marker — see §13.)*
  - The optional trailing `{...}` sets the beat's delivery intent (§5).
- A single optional level-1 heading (`# <episode title>`) may precede the first
  beat; it is not spoken (it duplicates front-matter `title`). Other heading
  levels are reserved and treated as non-spoken structural notes in v0.1.
- The **body** of a beat is everything until the next `##` (or end of file).
  It is **spoken verbatim**, in order.
- A **blank line** separates paragraphs. A paragraph break is a natural short
  pause (§7). Single newlines within a paragraph are treated as spaces.

---

## 5. Directives — `{ ... }`

A directive block is `{ key: value, key: value, ... }`: comma-separated
`key: value` pairs. Values are bare words, quoted strings, or numbers.

**Delivery intent keys** (engine-neutral):

| Key | Value | Effect |
|---|---|---|
| `tone` | a tone word (see §5.1) or quoted phrase | Emotional delivery for the span. |
| `rate` | `very-slow` \| `slow` \| `normal` \| `fast` \| `very-fast`, or a number (speed multiplier, `1.0` = normal) | Pace for the span. *(v0.1 Chatterbox: realized indirectly by coupling `rate` onto `cfg_weight` — slower rate = more deliberate delivery — not as exact time-scaling.)* |
| `note` | quoted free-text | Rich, descriptive nuance for the mapping layer / a richer engine, e.g. `note: "hushed, almost reverent; let the last line land"`. Never starves an expressive engine. |

**Point-event key:**

| Key | Value | Effect |
|---|---|---|
| `pause` | number (seconds) | Inserts exactly that much **real silence** at this point. Not a tone shift. |

**Where directives may appear:**

- **In a beat header** — applies to the whole beat: `## Title {tone: somber, rate: slow}`.
- **Inline in the body** — applies from that point until the next inline
  directive or the next beat. This is the escape hatch for a mid-beat shift
  without starting a new chapter: `... and then, quietly, {tone: hushed} everything changed.`
- `{pause: N}` may appear anywhere in the body (it is a point event, so it does
  not "carry" forward); it is conventionally placed at a sentence boundary.

Each `tone`/`rate`/`note` directive (header or inline) starts a **new IR
segment**. Keep them sparse (principle #3): most transcripts will set tone at the
beat header and rarely inline.

### 5.1 Tone vocabulary

The tone words are an **open, descriptive set** — not a rigid enum. The starter
vocabulary (mapped to engine settings in `voice_profiles.yaml`) includes:
`measured`, `neutral`, `warm`, `somber`, `grave`, `tense`, `urgent`, `dramatic`,
`wry`, `wistful`, `reverent`, `matter-of-fact`. You may use a word not yet in the
table; the compiler will **warn** and fall back to `defaults.tone` until you add
it (with a tuned mapping) — so unknown tones never silently change delivery. Use
`note:` for nuance beyond a single word.

---

## 6. Emphasis — `*italics*`

Wrap a word or phrase in single asterisks to mark **emphasis**: `it might happen *again*`.

> **Engine honesty (Chatterbox, v0.1).** Chatterbox has no per-word stress
> control (its only levers are per-chunk scalars). So in the Chatterbox backend,
> emphasis is **preserved as intent** in the IR (it pays off on engines that *do*
> support per-word emphasis, e.g. Gemini) and may be realized as a subtle
> micro-pause around the phrase — but it is **not** a guarantee of vocal stress.
> Carry real emphasis in the *prose* (the surrounding words and rhythm); use
> `*...*` to record intent, not to demand acoustics the engine can't deliver.

Use `\*` for a literal asterisk.

---

## 7. Pauses

Three sources of silence, longest-lived first:

1. **Explicit** — `{pause: N}` inserts exactly `N` seconds of real silence.
   Use this for "critical-point" beats (design goal #3).
2. **Beat boundary** — the gap between beats. Default ≈ `0.8 s`.
3. **Paragraph break** — a blank line. Default ≈ `0.4 s`.

Defaults are configurable via front-matter `pauses:` or the project config; they
are realized by the renderer as real silence segments spliced between rendered
audio (never as engine "breaks," which Chatterbox lacks). Sentence-internal
pacing is governed by `rate`, not by pauses.

---

## 8. Speakers — single by default, `@tag` to opt in

The default is a **single narrator** (front-matter `voice`); no tags needed —
this is the intended common case (goal #2).

For optional two-host mode, begin a line with `@<name>` to set the speaker for
the following paragraph(s) until the next `@<name>` or the next beat:

```
@narrator
So the question on the table in Paris was colder than we'd ask today.

@guest
Colder how?
```

Each `@name` should appear in front-matter `speakers:`; the compiler **warns** on
an `@name` that is not declared there (it is accepted, not rejected, in v0.1).

> **Renderer status (v0.1).** Speaker tags are parsed into the IR, but the
> renderer does not yet resolve them to distinct per-speaker voices: it renders
> the whole episode with one resolved voice. Multi-voice two-host rendering and
> renderer-applied turn-taking gaps are not yet wired (see DESIGN §11).

---

## 9. Comments and non-spoken content

- `<!-- ... -->` HTML comments are **never spoken**. Use them for author notes,
  the episode tension brief, and diagnostics (this matches the convention in the
  existing hand-written corpus).
- Front-matter, beat titles, directives, and `@speaker` tags are never spoken.
- **Everything else in a beat body is spoken**, verbatim.

---

## 10. Numbers, dates, symbols, and pronunciation

Write the body in **natural, readable form** — `1945`, `1914–1945`, `§45a`,
`EEC`, `Maastricht`. Do **not** hand-spell things phonetically in the transcript;
that would pollute the source of truth.

Conversion to spoken form happens at **compile time**, not here:
- **Normalization** turns `1945` → "nineteen forty-five", `1914–1945` → "nineteen
  fourteen to nineteen forty-five", `§45a` → "section forty-five a", etc.
- A per-project **pronunciation lexicon** respells proper nouns the engine would
  otherwise mangle (`Maastricht`, `Montesquieu`, `Ibn Khaldun`).

The compiler records both the **authored text** (what you wrote) and the
**spoken text** (what the engine receives) in the IR, so the transcript stays
human-readable while the renderer gets a pronounceable form. See the IR schema
and `lexicon`/`normalize` docs.

---

## 11. What gets spoken — the precise rule

Spoken = the concatenation, in document order, of all **beat-body text**, with:
- comments removed,
- directive blocks removed (their effect applied),
- `@speaker` tags removed (their effect applied),
- emphasis markers removed (their effect recorded),
- front-matter and headings excluded,
- the resulting runs normalized + lexicon-applied at compile time.

If it isn't beat-body text, it isn't spoken.

---

## 12. Worked example

```
---
format_version: "0.1"
voice: narrator
style: hardcore-history
episode: 1
title: "The Suicide of a Continent"
defaults: { tone: measured, rate: normal }
pauses: { paragraph: 0.4, beat: 0.9 }
seed: 70814
---

<!-- EPISODE TENSION: the rock-bottom chapter. End in the dark, with one
     strange idea forming — do not rush to the happy ending. -->

## The smell of the ruin   {tone: somber, rate: slow}
Picture the continent in the spring of 1945. Not a map — a smell.
Brick dust and cordite, and something worse underneath it. {pause: 1.0}
Tens of millions were dead. Whole cities were gone.

And here is the thing the people standing in that rubble actually believed,
the thing that is almost impossible to feel from where we sit now: they did
not believe it was over. {pause: 0.8} They believed it might happen *again*.

## Three times in one lifetime   {tone: grave}
Because it had a pattern. Think like a Frenchman born in 1900. By the time you
are forty-five, Germany has invaded your country three times — 1870, 1914,
1940. {pause: 0.6} Three times in a single human lifetime.

## The strange, indispensable man   {tone: measured, note: "a turn toward intrigue; lean in"}
Which brings us to the man at the center of this story. His name is Jean Monnet,
and he is almost a joke as a candidate for "father of a continent."
```

Compiles to: 4 beats → segments carrying `{tone, rate, note}` + emphasis spans +
explicit/auto pauses; each segment's spoken text normalized (`1945` →
"nineteen forty-five", `1870, 1914, 1940` spelled out) and any lexicon respelling
applied (`Monnet`); then chunked to the engine's per-generation cap for rendering.

---

## 13. From transcript to audio (pipeline context)

```
transcript.md ──compile──▶ IR (segments: intent + authored_text + spoken_text + chunk plan)
                              │
                              ├─ Tone specialist ─▶ render_plan.json (engine params per segment)
                              │
                              └──────────────▶ renderer: chunk → generate (+STT quality-gate,
                                               final mode) → trim → splice pauses / crossfade →
                                               concat → loudness-normalize → episode.wav
```

> **v0.1 output.** A single flat `episode.wav` (loudness-normalized). Chapter
> markers/metadata and per-episode output filenames are not yet produced.

The transcript never contains engine settings; the render plan is a **derived**
artifact. See `protocol/SPEC.md` for the job/handoff contract and the IR schema
in `prosodia.core` for field-level detail.
```
