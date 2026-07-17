# Lexicon-norm study

**Goal.** Find out *which respelling notation Chatterbox honors best*, so we can write
lexicon norms instead of guessing per name. We render a broad, cross-cultural corpus of
**second-tier names** — recognizable to an educated listener but routinely mangled by a
layperson and by the TTS (the *Thucydides* tier) — in three competing notations, and
listen for which one comes out right *and stable across seeds*.

Deliberately **excluded**: the truly famous (Socrates, Plato, Aristotle, Confucius,
Caesar, …). Chatterbox already pronounces those correctly, and a respelling can only
introduce drift. If a name in this list turns out to render fine "as written," that's a
result too — it means it never needed a lexicon entry.

## The experiment

One pronunciation per name is the source of truth (in `build.py`); from it we emit three
notations, so each name is auditioned in **four columns**:

| column | example (`Thucydides`) | what it is |
|---|---|---|
| as-written | `Thucydides` | baseline — does it even need help? |
| **A** plain-hyphen | `Thoo-sid-ih-deez` | capitalized, hyphens, **no** stress mark |
| **B** stress-caps | `Thoo-SID-ih-deez` | A **+ stressed syllable in ALL-CAPS** |
| **C** spaced | `Thoo sid ih deez` | A but **spaces** instead of hyphens |

The contrasts are designed to isolate one variable each:

- **as-written → A** — is a respelling needed at all?
- **A → B** — does marking stress (CAPS) help, hurt, or do nothing?
- **A → C** — hyphen vs. space as the syllable separator?

(For names whose words are all single-syllable — e.g. *Sun Tzu* — A and C collapse to the
same string; that's expected, just fewer distinct columns for that name.)

## Corpus

91 names across seven groups: Ancient Greek · Roman/Latin · Medieval & Islamic Golden Age
· Continental Europe · Russian/Slavic · Non-Western (China/India) · Modern English-tricky.
The grouping lets you look for **per-culture patterns** (e.g. "German -sche endings need
X", "Chinese pinyin needs Y") rather than only per-name results.

## Files

- `build.py` — the source of truth. Edit a pronunciation here (`"thoo-*sid-ih-deez"`,
  `*` marks the stressed syllable) and re-run to regenerate both YAMLs consistently.
- `lexicon.yaml` — Style **A** (the "lexicon" column).
- `variants.yaml` — Styles **B** and **C** (variant 1 / variant 2).
- `out/` — render output + `index.html` (created by the run; git-ignored).

Regenerate the inputs after editing `build.py`:

```
python experiments/lexicon_norms/build.py
```

## Running the audition (GPU box)

Runs on the renderer (needs the render extra + Chatterbox). Point `--voices` at the
narrator clip you're actually shipping — pronunciation stability is voice-dependent, so
audition against the real reference, not a placeholder.

```
python -m prosodia.render.cli lexicon-audition \
  --voices <path-to-narrator.wav-or-voices-dir> \
  --lexicon  experiments/lexicon_norms/lexicon.yaml \
  --variants experiments/lexicon_norms/variants.yaml \
  --out      experiments/lexicon_norms/out \
  --takes 3
```

Then open `experiments/lexicon_norms/out/index.html` and A/B the columns by ear.

**Render count** = 91 names × 4 columns × `takes`. At `--takes 3` that's ~1092 clips —
a long batch. To triage first, cut with `--takes 2`, or scope to one group with
`--names Thucydides Polybius …` (space-separated source names). A first pass at `--takes 2`
on one or two groups is enough to sanity-check the notations before the full run.

## Reading the results → norms

For each name, note per column: **correct?** and **stable across the seeds?** (an unstable
respelling drifts seed-to-seed even when one take sounds right — that's a reject). Then
roll up across the corpus:

- Does **A** beat as-written often enough to justify respelling at all, or only for
  certain phonetic shapes?
- Does **B** (stress caps) actually move stress, or does Chatterbox ignore case?
- Do **hyphens or spaces** read more reliably as syllable breaks?
- Any **per-culture** rule (French nasal endings, German *ei/eu*, pinyin *zi/zhi*, Greek
  *-ides/-oras*)?

The winning conventions become the lexicon-authoring norms; feed them back into the
per-project `lexicon.yaml` files and the writer/compile guidance.

> This directory lives under `/experiments/` which is git-ignored — it's a research
> workspace, not shipped source.
