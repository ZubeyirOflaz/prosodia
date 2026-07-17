"""Generate the lexicon-norm study inputs (lexicon.yaml + variants.yaml).

Goal: a broad, cross-cultural corpus of "second-tier" names — the kind an educated
listener recognizes but a layperson (and Chatterbox) tends to mangle — rendered in
three competing RESPELLING NOTATIONS so we can find which convention holds up.
Deliberately excludes the truly famous (Socrates/Plato/Aristotle/Confucius/…) since
Chatterbox already says those right and a respelling can only hurt.

Each name is one source, encoded as a compact pronunciation string:
  - words separated by SPACE, syllables by "-", the stressed syllable prefixed "*".
  e.g. "thoo-*sid-ih-deez"  ->  syllables thoo / sid(stressed) / ih / deez
       "ib-un khal-*doon"   ->  two words, stress on "doon"

From that single source of truth we emit three notations, so the audition renders
four columns per name (as-written + A + B + C):

  A  plain-hyphen : capitalized, hyphens, NO stress mark   -> Thoo-sid-ih-deez   (lexicon.yaml)
  B  stress-caps  : A but stressed syllable ALL-CAPS       -> Thoo-SID-ih-deez   (variants.yaml #1)
  C  spaced       : A but spaces instead of hyphens        -> Thoo sid ih deez   (variants.yaml #2)

Contrasts the audition then isolates:
  as-written -> A : does the name even need help?
  A -> B          : does marking stress (CAPS) help or hurt?
  A -> C          : hyphens vs. spaces as the syllable separator?

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


def notations(pron: str) -> tuple[str, str, str]:
    """(A plain-hyphen, B stress-caps, C spaced) from one pronunciation string."""
    words, (sw, ss) = _parse(pron)
    a_words, b_words, c_words = [], [], []
    for wi, sylls in enumerate(words):
        a_words.append(_cap("-".join(sylls)))
        c_words.append(_cap(" ".join(sylls)))
        b = [s.upper() if (wi == sw and si == ss) else s for si, s in enumerate(sylls)]
        b_words.append(_cap("-".join(b)))
    return " ".join(a_words), " ".join(b_words), " ".join(c_words)


def main() -> None:
    lex_lines = [
        "# Lexicon-norm study — Style A (plain-hyphen): capitalized, hyphen syllables, no stress mark.",
        "# Generated by build.py — edit the pronunciations there, not here.",
        "lexicon:",
    ]
    var_lines = [
        "# Candidate respellings A/B'd against Style A (lexicon.yaml) and the as-written baseline.",
        "#   - #1 = Style B (stress-caps)   - #2 = Style C (spaced)",
        "# Generated by build.py — edit the pronunciations there, not here.",
    ]
    total = 0
    for category, names in DATA:
        lex_lines.append(f"  # --- {category} ---")
        var_lines.append(f"# --- {category} ---")
        for src, pron in names:
            a, b, c = notations(pron)
            total += 1
            key = f'"{src}"' if (" " in src or "-" in src) else src
            lex_lines.append(f'  {key}: "{a}"')
            var_lines.append(f"{key}:")
            var_lines.append(f'  - "{b}"   # B stress-caps')
            var_lines.append(f'  - "{c}"   # C spaced')
        var_lines.append("")

    (HERE / "lexicon.yaml").write_text("\n".join(lex_lines) + "\n", encoding="utf-8")
    (HERE / "variants.yaml").write_text("\n".join(var_lines) + "\n", encoding="utf-8")
    print(f"wrote lexicon.yaml + variants.yaml — {total} names")
    print(f"render count = {total} names x 4 columns x N takes")


if __name__ == "__main__":
    main()
