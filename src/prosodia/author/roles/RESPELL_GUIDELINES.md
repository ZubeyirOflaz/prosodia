# Respelling guidelines — natural, Chatterbox-friendly pronunciations

How to turn a Wikipedia pronunciation (IPA and/or its hyphen-and-CAPS respelling) into a
**natural, real-word respelling** that the Chatterbox TTS reads correctly.

## Why respelling at all

Chatterbox has **no phoneme/IPA/SSML input** — it reads raw letters and pronounces them
with a learned English model. You cannot feed it IPA. The only lever is to **spell the name
the way it sounds, as an ordinary English-looking word**, so the model's own reading lands
on the right pronunciation.

## The hard rule: what NOT to produce

Chatterbox mis-reads exactly the format Wikipedia respelling uses. **Never** emit:
- **Hyphens** between syllables (`thew-SID-ih-deez`) → read as separate words.
- **ALL-CAPS** stressed syllables (`NEE-chuh`, `ə-KWY-nəs`) → read as an acronym, spelled
  out letter by letter.
- **Spaces between syllables** of one word → read as separate words.

## What TO produce

A single **run-on, lower-case-after-initial, real-word-looking spelling**, using ordinary
English letter patterns:
- **No hyphens, no ALL-CAPS.** Capitalise only the first letter.
- **Spaces only between genuinely separate words** (`Ibn Khaldun` → `Ibun Khaldoon`, not
  `Ibunkhaldoon`).
- Prefer common English graphemes: `ee`=/iː/, `oo`=/uː/, `oh`=/oʊ/, `ay`=/eɪ/, `eye`/`y`=/aɪ/,
  `ow`=/aʊ/, `uh`=schwa /ə/, `k`=/k/, `s`=/s/, `sh`=/ʃ/, `ch`=/tʃ/, `j`=/dʒ/, `zh`=/ʒ/.
- **Change as few letters from the real name as you can** while fixing the error. Minimal
  edits read most naturally (e.g. `Nietzsche → Neecha`, not a wholesale invention). Only
  fully respell when the name is far from how it looks (`Thucydides → Thoosidadeez`).
- Convey stress with **natural spelling, not caps** — usually the vowel spelling already
  implies it (`Neecha`, `Uhkwynus`); if needed, double a consonant or use a clearer vowel.
- **Sanity check:** read your spelling aloud as if it were an English word. Does a narrator
  land on the right pronunciation? If not, adjust.

## Which input to trust, in order

1. **Wikipedia respelling** (`thew-SID-ih-deez`) — best starting point; just strip the
   hyphens/CAPS and naturalise (`Thewsidadeez` / `Thoosidadeez`).
2. **IPA** (`/θjuːˈsɪdɪˌdiːz/`) — use when there's no respelling; convert IPA → English
   graphemes with the table above.
3. **Neither** (the tool flagged a gap) — use your own knowledge of the accepted English
   pronunciation. If you are unsure, **leave the name out** rather than guess wildly.
4. If Wikipedia gives **two variants** (`NEE-chuh, NEE-chee`), pick the **more common
   English** one.

## When to emit NO entry

Most names don't need one. **Omit a name entirely if Chatterbox is likely to say it correctly
from the raw spelling** — regular English-looking names (Weber, Bentham, Hayek, Hobbes,
Locke), and anything whose spelling already matches its sound. A respelling can only *hurt*
those. Prefer a small lexicon of genuinely-hard names over a big one.

## Worked examples

| name | wiki respell / IPA | → natural entry |
|---|---|---|
| Thucydides | `thew-SID-ih-deez` | `Thoosidadeez` |
| Nietzsche | `NEE-chuh` `/ˈniːtʃə/` | `Neecha` |
| Aquinas | `ə-KWY-nəs` | `Uhkwynus` |
| Ibn Khaldun | `IB-ən hal-DOON` | `Ibun Khaldoon` |
| Foucault | `/fuːˈkoʊ/` | `Fookoh` |
| Xenophon | `/ˈzɛnəfən/` | `Zenuhfun` |
| Weber | (regular-looking) | *(omit — say it raw)* |

## Output format

Emit YAML under a `lexicon:` map, source spelling → natural respelling, one per line, and
nothing for names you omit:

```yaml
lexicon:
  Thucydides: "Thoosidadeez"
  Nietzsche: "Neecha"
  "Ibn Khaldun": "Ibun Khaldoon"
```

Quote keys that contain a space or hyphen. Keep entries only for names that genuinely need
help.
