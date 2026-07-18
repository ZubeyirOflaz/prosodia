"""Generate the lexicon-norm study v2 (lexicon.yaml + scoresheet.md).

v1 result: syllable-notation respellings (hyphens / ALL-CAPS stress / spaces) LOSE to
the raw name — Chatterbox reads hyphens & spaces as separate words and ALL-CAPS as an
acronym. See archive/ for that run and its filled scoresheet.

v2 tests a single, cleaner idea: does a NATURAL, real-word respelling — the same
phonetic content written as a plausible run-on word with NO hyphens, NO CAPS, and spaces
ONLY between genuine words — beat the unassisted spelling? Just two columns per name:

  as-written : the raw name (unassisted)          -> Thucydides
  natural    : run-on real-word respelling         -> Thoosidihdeez

Respelling source: if ``natural_respellings.yaml`` is present (produced by wiki_pron.py +
the lexicographer agent from Wikipedia pronunciations) it is used verbatim — the strongest,
sourced version of the respelling. Otherwise the respellings are derived mechanically from
the syllable DATA below, encoded as a compact pronunciation string (unchanged from v1):
  - words separated by SPACE, syllables by "-", the stressed syllable prefixed "*".
  e.g. "thoo-*sid-ih-deez"  ->  syllables thoo / sid(stressed) / ih / deez  ->  "Thoosidihdeez"
       "ib-un khal-*doon"   ->  two words -> "Ibun Khaldoon" (space kept between real words)

Run:  python experiments/lexicon_norms/build.py
"""

from __future__ import annotations

from pathlib import Path

HERE = Path(__file__).resolve().parent

# (category, [(source_name, pronunciation), ...]). Stress marked with a leading "*".
DATA: list[tuple[str, list[tuple[str, str]]]] = [
    ("Ancient Greek", [
        ("Thucydides", "thoo-*sid-ih-deez"),
        ("Polybius", "puh-*lib-ee-us"),
        ("Thrasymachus", "thruh-*sim-uh-kus"),
        ("Xenophon", "*zen-uh-fon"),
        ("Anaximander", "uh-*nak-suh-man-der"),
        ("Anaxagoras", "an-ak-*sag-er-us"),
        ("Parmenides", "par-*men-ih-deez"),
        ("Empedocles", "em-*ped-uh-kleez"),
        ("Heraclitus", "hair-uh-*kly-tus"),
        ("Epictetus", "ep-ik-*tee-tus"),
        ("Alcibiades", "al-suh-*by-uh-deez"),
        ("Isocrates", "eye-*sok-ruh-teez"),
        ("Antisthenes", "an-*tis-thuh-neez"),
        ("Protagoras", "proh-*tag-er-us"),
        ("Diogenes", "dy-*oj-uh-neez"),
    ]),
    ("Roman / Latin", [
        ("Lucretius", "loo-*kree-shus"),
        ("Tacitus", "*tass-ih-tus"),
        ("Quintilian", "kwin-*til-ee-un"),
        ("Boethius", "boh-*ee-thee-us"),
        ("Diocletian", "dy-uh-*klee-shun"),
        ("Scipio", "*sip-ee-oh"),
        ("Sallust", "*sal-ust"),
        ("Gracchus", "*grak-us"),
        ("Catullus", "kuh-*tul-us"),
        ("Juvenal", "*joo-vuh-nul"),
    ]),
    ("Medieval / Islamic Golden Age", [
        ("Aquinas", "uh-*kwy-nus"),
        ("Marsilius", "mar-*sil-ee-us"),
        ("Averroes", "uh-*ver-oh-eez"),
        ("Avicenna", "av-ih-*sen-uh"),
        ("Al-Farabi", "al fah-*rah-bee"),
        ("Al-Ghazali", "al guh-*zah-lee"),
        ("Ibn Khaldun", "ib-un khal-*doon"),
        ("Maimonides", "my-*mon-ih-deez"),
        ("Duns Scotus", "dunz *skoh-tus"),
        ("Ockham", "*ok-um"),
        ("Abelard", "*ab-uh-lard"),
        ("Anselm", "*an-selm"),
    ]),
    ("Continental Europe", [
        ("Montesquieu", "mon-tuh-*skyoo"),
        ("Rousseau", "roo-*soh"),
        ("Machiavelli", "mah-kee-uh-*vel-ee"),
        ("Grotius", "*groh-shus"),
        ("Nietzsche", "*nee-chuh"),
        ("Tocqueville", "*tohk-vil"),
        ("Foucault", "foo-*koh"),
        ("Habermas", "*hah-ber-mahs"),
        ("Weber", "*vay-ber"),
        ("Proudhon", "proo-*dohn"),
        ("Gramsci", "*gram-shee"),
        ("Hegel", "*hay-gul"),
        ("Goethe", "*gur-tuh"),
        ("Kierkegaard", "*keer-kuh-gard"),
        ("Spinoza", "spih-*noh-zuh"),
        ("Leibniz", "*lybe-nits"),
        ("Schopenhauer", "*shoh-pen-how-er"),
        ("Diderot", "dee-duh-*roh"),
        ("Durkheim", "*dur-kime"),
        ("Vico", "*vee-koh"),
        ("Pareto", "puh-*ray-toh"),
        ("Voltaire", "vol-*tair"),
        ("Adorno", "uh-*dor-noh"),
        ("Marcuse", "mar-*koo-zuh"),
        ("Althusser", "al-too-*sair"),
        ("Derrida", "dair-ee-*dah"),
        ("Deleuze", "duh-*looz"),
        ("Bourdieu", "boor-*dyuh"),
        ("Beauvoir", "boh-*vwar"),
        ("Condorcet", "kon-dor-*say"),
    ]),
    ("Russian / Slavic", [
        ("Bakunin", "buh-*koo-nin"),
        ("Kropotkin", "kruh-*pot-kin"),
        ("Herzen", "*hair-tsen"),
        ("Plekhanov", "plih-*khah-nof"),
        ("Berdyaev", "ber-*dyah-yef"),
        ("Solzhenitsyn", "sohl-zhuh-*neet-sin"),
        ("Luxemburg", "*look-sem-boork"),
    ]),
    ("Non-Western (China / India)", [
        ("Mencius", "*men-shee-us"),
        ("Xunzi", "*shoon-dzuh"),
        ("Mozi", "*maw-dzuh"),
        ("Laozi", "*low-dzuh"),
        ("Zhuangzi", "*jwahng-dzuh"),
        ("Han Feizi", "*hahn fay-dzuh"),
        ("Sun Tzu", "*soon dzoo"),
        ("Kautilya", "kow-*til-yuh"),
        ("Nagarjuna", "nah-gar-*joo-nuh"),
        ("Ashoka", "uh-*shoh-kuh"),
        ("Ambedkar", "ahm-*bayd-kar"),
    ]),
    ("Modern / English-tricky", [
        ("Wollstonecraft", "*wool-stun-kraft"),
        ("Oakeshott", "*ohk-shot"),
        ("Hayek", "*hy-ek"),
        ("Arendt", "*air-unt"),
        ("Fanon", "fah-*nohn"),
        ("Bentham", "*ben-thum"),
    ]),
]


def _parse(pron: str) -> tuple[list[list[str]], tuple[int, int]]:
    """Return (words as syllable-lists, (word_idx, syll_idx) of the stress)."""
    words: list[list[str]] = []
    stress = (0, 0)
    for wi, word in enumerate(pron.split(" ")):
        sylls = []
        for si, syl in enumerate(word.split("-")):
            if syl.startswith("*"):
                stress = (wi, si)
                syl = syl[1:]
            sylls.append(syl)
        words.append(sylls)
    return words, stress


def _cap(word: str) -> str:
    return word[:1].upper() + word[1:] if word else word


def natural(pron: str) -> str:
    """A run-on, real-word respelling: syllables concatenated with NO hyphens and NO
    stress CAPS (only an initial capital), spaces kept ONLY between genuine words. Same
    phonetic content as v1's hyphenated notation, minus the formatting Chatterbox
    mis-reads as separate words / an acronym.
      "thoo-*sid-ih-deez" -> "Thoosidihdeez"   |   "ib-un khal-*doon" -> "Ibun Khaldoon"
    """
    words, _ = _parse(pron)
    return " ".join(_cap("".join(sylls)) for sylls in words)


def respellings() -> dict[str, str]:
    """Name -> natural respelling. Prefer the Wikipedia+agent-sourced file
    (``natural_respellings.yaml``, produced via wiki_pron.py + the lexicographer) if it
    exists; otherwise derive them mechanically from the syllable DATA."""
    src = HERE / "natural_respellings.yaml"
    if src.exists():
        import yaml

        loaded = yaml.safe_load(src.read_text(encoding="utf-8")) or {}
        if isinstance(loaded, dict):
            return {str(k): str(v) for k, v in loaded.items()}
    return {name: natural(pron) for _, names in DATA for name, pron in names}


METHODS = [
    ("as-written", "the raw name, no lexicon (unassisted)"),
    ("natural", "run-on real-word respelling: no hyphens, no CAPS, spaces only between real words"),
]


def _scoresheet() -> str:
    """A scoring sheet as GitHub task-list checkboxes: one `###` heading per name (so
    Ctrl+Shift+O / the Outline panel jump straight to it) and one checkbox per render
    method (toggle `[ ]`->`[x]` from the keyboard, or click it in the VSCode/Cursor
    preview). Mark every method that sounded correct AND stable across the seeds."""
    n = sum(len(names) for _, names in DATA)
    out = [
        "# Lexicon-norm scoresheet",
        "",
        f"_{n} names. Listen to each name's takes in `out/index.html`, then tick the "
        "method(s) that came out **correct AND stable across the seeds**._",
        "",
        "**Navigate:** `Ctrl+Shift+O` (Go to Symbol) then type a name to jump; or use the "
        "Outline panel. **Mark:** toggle `[ ]`→`[x]` (keyboard), `Alt+C` with the "
        "*Markdown All in One* extension, or click the box in the Markdown preview.",
        "",
        "Rules:",
        "- Tick **as-written** ⇒ the name needs **no lexicon entry** (Chatterbox nails it unaided).",
        "- Tick **natural** ⇒ the run-on respelling was clearly more accurate/reliable than raw.",
        "- Tick **both** if they're equally good; leave **both blank** + add a note if neither works.",
        "",
        "Method legend — " + "; ".join(f"**{m}** = {d}" for m, d in METHODS) + ".",
        "",
        "> Generated by `build.py`; it will NOT overwrite this file once it exists, so your",
        "> marks are safe across regenerations. Delete it to regenerate a blank sheet.",
        "",
    ]
    resp = respellings()
    for category, names in DATA:
        out.append(f"## {category}")
        out.append("")
        for src, pron in names:
            spellings = [src, resp.get(src) or natural(pron)]
            out.append(f"### {src}")
            for (label, _desc), spelling in zip(METHODS, spellings):
                out.append(f"- [ ] {label} · `{spelling}`")
            out.append("- notes: ")
            out.append("")
    return "\n".join(out) + "\n"


def main() -> None:
    lex_lines = [
        "# Lexicon-norm study v2 — NATURAL run-on respellings (no hyphens, no CAPS,",
        "# spaces only between real words). Auditioned against the as-written baseline.",
        "# Generated by build.py — edit the pronunciations there, not here.",
        "lexicon:",
    ]
    resp = respellings()
    total = 0
    for category, names in DATA:
        lex_lines.append(f"  # --- {category} ---")
        for src, pron in names:
            total += 1
            key = f'"{src}"' if (" " in src or "-" in src) else src
            lex_lines.append(f'  {key}: "{resp.get(src) or natural(pron)}"')

    (HERE / "lexicon.yaml").write_text("\n".join(lex_lines) + "\n", encoding="utf-8")
    # v2 is a two-way test (raw vs natural) — no A/B/C variants file. Remove any stale one.
    (HERE / "variants.yaml").unlink(missing_ok=True)
    print(f"wrote lexicon.yaml — {total} natural respellings (removed stale variants.yaml)")
    print(f"render count = {total} names x 2 columns (as-written + natural) x N takes")

    sheet = HERE / "scoresheet.md"
    if sheet.exists():
        print("scoresheet.md exists — leaving your marks untouched (delete it to regenerate)")
    else:
        sheet.write_text(_scoresheet(), encoding="utf-8")
        print("wrote scoresheet.md (blank — tick as-written / natural per name)")


if __name__ == "__main__":
    main()
