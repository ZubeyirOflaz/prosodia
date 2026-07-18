# Research: pronunciation control in Chatterbox TTS

Deep-research pass (18 sources, 76 claims, adversarially verified). Answers the question:
*is a respelling lexicon the right tool for Chatterbox, did we make a mistake, and is there
a better engine?* **Bottom line: no code bug; respelling is the only lever Chatterbox gives
you (and what the community uses) — our v1 format was wrong; switching engines does not buy
pronunciation control.**

## 1. Chatterbox has no pronunciation API — confirmed from the source code

- `generate()` runs exactly one preprocessing step, `punc_norm()`, then tokenizes raw
  graphemes via `EnTokenizer.text_to_tokens()`. **No phoneme/IPA input, no SSML, no
  pronunciation-override.** Pronunciation is fully learned from graphemes.
  [tts.py](https://github.com/resemble-ai/chatterbox/blob/master/src/chatterbox/tts.py)
- `punc_norm()` only: capitalizes the first letter, collapses whitespace runs to single
  spaces, swaps ~12 punctuation variants to ASCII, appends a period if none. **It does NOT
  special-case ALL-CAPS or hyphens** — single internal spaces are preserved and hyphens are
  kept (em/en-dashes are normalized *into* hyphens). So a hyphenated/spaced/CAPS respelling
  reaches the model **unmodified**. (tts.py)
- **Correction to our earlier hypothesis:** the "hyphens → separate words" and "CAPS →
  acronym" artifacts are *not* a normalization rule we can point at — they're **emergent
  model behavior**. The specific claim that space-separating letters is the model's intended
  initialism representation was **refuted 3–0** in verification. The practical upshot is
  unchanged (odd formatting confuses the model), but the mechanism is the learned model, not
  a text-frontend bug.
- The only generate-time knobs are `temperature` (0.8), `exaggeration` (0.5), `cfg_weight`
  (0.5) — **none target pronunciation**; they affect pacing/emotion.
  [HF model card](https://huggingface.co/ResembleAI/chatterbox)

## 2. What the community actually does

- There is **no built-in custom-pronunciation/lexicon feature**. The GitHub issue asking
  "does it support custom pronunciation?" got **no maintainer answer**; the only workaround
  offered is a **user-maintained respelling dictionary applied externally** — exactly our
  compile-time source→respelling map.
  [issue #115](https://github.com/resemble-ai/chatterbox/issues/115)
- The respelling style people use is **minimal grapheme edits to the real word** (e.g.
  `John → Jon` — drop/alter the letters that throw the model off), **not** syllable
  notation with hyphens and stress-caps. This is the key finding for us. (issue #115)
- Even the feature-rich wrapper (Chatterbox-TTS-Extended) exposes **no phoneme input, no
  SSML, no pronunciation lexicon** — only a filler-noise replace list (um/ahh→sigh), which
  is not a name-pronunciation map.
  [Chatterbox-TTS-Extended](https://github.com/petermg/Chatterbox-TTS-Extended)
- The **reference clip influences pronunciation/accent but unreliably** (non-UK samples
  frequently came out UK-accented; inconsistent, worse for female voices), and "all accents
  mispronounce certain words, which is why a custom pronunciation dictionary is needed rather
  than relying on the reference clip alone." (issue #115) — so the clip is not a control lever.

## 3. Verdict on the respelling lexicon

**It is the right *kind* of tool — the only one Chatterbox offers — but our v1 *format* was
wrong.** Syllable-hyphenation + ALL-CAPS stress + spacing all fight the model. The
community's minimal-real-word-edit style is what works. Our v2 (natural run-on, no
hyphens/caps) is the right direction; a *minimal-edit* variant (change as few letters as
possible from the true spelling) is likely even better and worth testing alongside it.
Academic G2P work confirms phoneme input beats graphemes in general, but **Chatterbox can't
accept phonemes**, so those gains are inaccessible without changing engines.

## 4. Alternatives — do they buy pronunciation control? No.

| Engine | Clones voice? | Phoneme/IPA/SSML control? | RTX 3080? | License |
|---|---|---|---|---|
| **Chatterbox** | yes (~5 s ref) | **no** (grapheme-only) | yes, 4–6 GB | **MIT** ✅ |
| XTTS-v2 (Coqui) | yes | no (grapheme; but accent stable vs speaker) | yes, 4–6 GB | CPML **non-commercial**, Coqui defunct/unmaintained |
| F5-TTS | yes (~3 s) | no (end-to-end, no phoneme stage) | yes, ~3–5 GB | code MIT, **weights CC-BY-NC** |
| Fish-Speech | yes | no | yes | **CC-BY-NC-SA** |
| Piper | **no** | **yes** (eSpeak-NG phonemes) | yes | MIT |
| Kokoro | no | — | yes | Apache-2.0 |

Sources: [localaimaster](https://localaimaster.com/blog/best-local-tts-models),
[promptquorum](https://www.promptquorum.com/power-local-llm/local-tts-voice-cloning-piper-coqui-xtts),
[F5-TTS](https://github.com/swivid/f5-tts), [phonemizer](https://github.com/bootphon/phonemizer).

**The fundamental tension:** the engines that accept phonemes (Piper, via eSpeak-NG) **don't
clone a voice**; the engines that clone (Chatterbox, XTTS, F5, Fish) are **grapheme-only with
no phoneme API**. There is **no engine that gives both voice cloning *and* phoneme-level
pronunciation control** on a single consumer GPU. On top of that, every cloning alternative
is **non-commercially licensed**, whereas Chatterbox is MIT. So switching engines trades away
license + our tuned pipeline **without** gaining real pronunciation control.

## Recommendation

1. **Keep Chatterbox and keep a respelling lexicon — but format entries the community way:**
   minimal, natural, real-word edits (no hyphens, no CAPS, no syllable spacing).
2. **Use it sparingly.** The scoresheet shows raw wins most of the time; lean on the
   unassisted-first fallback already built, and only add a lexicon entry where raw genuinely
   fails *and* a respelling clearly beats it.
3. **v2 experiment stands**, with an added arm worth testing: *minimal-edit* respellings
   (change the fewest letters) alongside the natural run-on, since community evidence favors
   staying close to the real word.
4. **Do not switch engines for pronunciation.** (If pronunciation ever becomes the top
   priority over cloning/license, the only real lever is a phoneme engine like Piper — losing
   the cloned narrator — so it's not a fit here.)
