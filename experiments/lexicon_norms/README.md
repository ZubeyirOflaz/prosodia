# Lexicon-norm study

**Goal.** Find a respelling notation Chatterbox actually honors — or confirm that none
does and the raw spelling should win. Second-tier names (recognized but easily mangled,
the *Thucydides* tier), across cultures. The truly famous (Socrates, Plato, Confucius…)
are excluded — Chatterbox already says those right.

## v1 (archived) — syllable notations lost

v1 auditioned three syllable notations against the raw name:
`Thoo-sid-ih-deez` (hyphens) · `Thoo-SID-ih-deez` (stress CAPS) · `Thoo sid ih deez` (spaces).

**Result: the raw name almost always won.** Chatterbox is a grapheme-input model with a
learned pronunciation and no phoneme API, so the formatting backfired: **hyphens and
spaces are read as word breaks** (the name comes out as separate words) and **ALL-CAPS is
read as an acronym** (spelled out letter by letter). The stress-caps notation was the
worst. The v1 inputs and the filled scoresheet are in [`archive/`](archive/).

## v2 (current) — does a *natural* run-on respelling help?

v2 keeps only the idea that might survive the above: the same phonetic content written as
a **natural, real-word run-on** — **no hyphens, no CAPS**, spaces only between genuine
words — so there's nothing for the model to mis-segment. Two columns per name:

| column | example (`Thucydides`) | what it is |
|---|---|---|
| as-written | `Thucydides` | the raw name (unassisted) |
| **natural** | `Thoosidihdeez` | run-on real-word respelling |

Other examples: `Xenophon`→`Zenuhfon`, `Nietzsche`→`Neechuh`, `Foucault`→`Fookoh`,
`Ibn Khaldun`→`Ibun Khaldoon`, `Machiavelli`→`Mahkeeuhvelee`.

The one question: **does the natural respelling read more accurately/reliably than the raw
name, or does the run-on itself confuse the model too?** If natural wins on a meaningful
share of names, respelling is viable (just in this format) and worth per-name hand-tuning;
if it doesn't beat raw, respelling is the wrong tool for Chatterbox and we drop the lexicon.

> The natural spellings are **Wikipedia-sourced**: `wiki_pron.py` pulls each name's IPA +
> respelling from Wikipedia, and the lexicographer agent converts them to natural run-ons per
> `src/prosodia/author/roles/RESPELL_GUIDELINES.md` (see `natural_respellings.yaml` +
> `wiki_prons.json`). This gives the respelling idea its *strongest* form — so if natural
> still loses to raw, respelling is genuinely the wrong tool, not just badly spelled.
> (`build.py` falls back to mechanically stripping v1's syllable DATA if that file is absent.)

## Files

- `build.py` — source of truth. Edit a pronunciation (`"thoo-*sid-ih-deez"`, `*` marks
  stress) and re-run to regenerate `lexicon.yaml` + `scoresheet.md`.
- `lexicon.yaml` — the natural respellings (the `natural` column).
- `scoresheet.md` — GitHub-checkbox sheet; won't overwrite once you start marking.
- `out/` — render output + `index.html` (created by the run; git/sync-ignored).
- `archive/` — the v1 inputs and the filled v1 scoresheet.

Regenerate inputs after editing `build.py`:

```
python experiments/lexicon_norms/build.py
```

## Running the audition (GPU box)

Runs on the renderer. Point `--voices` at the real narrator clip. **No `--variants` now**
— the raw baseline (`as written`) plus the `lexicon` (natural) column give the two takes.

```
python -m prosodia.render.cli lexicon-audition \
  --voices <narrator.wav-or-dir> \
  --lexicon experiments/lexicon_norms/lexicon.yaml \
  --out     experiments/lexicon_norms/out \
  --takes 3
```

**Render count** = 91 names × 2 columns × `takes` (≈ 546 at `--takes 3`). Scope a first
pass with `--names Thucydides Nietzsche Ibn\ Khaldun Xunzi …`.

Then open `out/index.html`, A/B each pair, and tick in `scoresheet.md`:
- **as-written** ⇒ raw wins (no entry needed).
- **natural** ⇒ the run-on respelling is clearly more accurate/reliable.
- **both** ⇒ a tie; **neither** + a note ⇒ neither is acceptable.

> This directory lives under `/experiments/`, carved out of `.gitignore`/`.stignore` so the
> study source is tracked and syncs to the render box; `out/` stays local.
