from prosodia.author.chunk import chunk_text, split_sentences
from prosodia.author.lexicon import Lexicon
from prosodia.author.normalize import int_to_words, normalize_text, year_to_words


def test_chunk_basic():
    assert chunk_text("Hello there.") == ["Hello there."]


def test_chunk_respects_max_and_preserves_words():
    text = " ".join(["word"] * 200)  # ~1000 chars, no sentence punctuation
    chunks = chunk_text(text, max_chars=100)
    assert chunks and all(len(c) <= 100 for c in chunks)
    assert " ".join(chunks).split() == text.split()  # no words lost or added


def test_chunk_packs_multiple_sentences():
    chunks = chunk_text("One. Two. Three. Four.", max_chars=12)
    assert all(len(c) <= 12 for c in chunks)
    assert len(chunks) >= 2


def test_split_sentences():
    assert split_sentences("A. B! C?") == ["A.", "B!", "C?"]


def test_int_and_year_words():
    assert int_to_words(399) == "three hundred ninety-nine"
    assert int_to_words(1_000_000) == "one million"
    assert year_to_words(1945) == "nineteen forty-five"
    assert year_to_words(1900) == "nineteen hundred"
    assert year_to_words(1905) == "nineteen oh five"
    assert year_to_words(2020) == "twenty twenty"


def test_normalize_text():
    assert "nineteen fourteen to nineteen forty-five" in normalize_text("from 1914-1945")
    assert "section forty-five a" in normalize_text("see §45a now")
    assert "twenty-seven" in normalize_text("27 states")
    assert "World War Two" in normalize_text("after WWII ended")
    assert "nineteen forty-five" in normalize_text("the spring of 1945")


def test_int_and_year_words_edge_cases():  # finding 15
    assert int_to_words(0) == "zero"
    assert int_to_words(-5) == "minus five"
    assert (
        int_to_words(1234567)
        == "one million two hundred thirty-four thousand five hundred sixty-seven"
    )


def test_normalize_decimals():  # finding 4
    assert normalize_text("Pi is 3.14") == "Pi is three point one four"
    assert "point five" in normalize_text("0.5 percent")


def test_normalize_year_boundaries():  # findings 5, 13
    assert normalize_text("1000") == "one thousand"
    assert normalize_text("1066") == "ten sixty-six"
    assert normalize_text("1100") == "eleven hundred"
    assert normalize_text("1905") == "nineteen oh five"
    assert normalize_text("2000") == "two thousand"
    assert normalize_text("2005") == "two thousand five"
    assert normalize_text("2099") == "twenty ninety-nine"
    # >= 2100 has no two-pair reading -> cardinal.
    assert normalize_text("2150") == "two thousand one hundred fifty"


def test_normalize_year_ranges():  # finding 14
    assert normalize_text("1990–2010") == "nineteen ninety to twenty ten"
    assert normalize_text("300-400") == "three hundred to four hundred"
    for dash in ("-", "–", "—"):  # hyphen, en-dash, em-dash
        assert (
            normalize_text(f"1914{dash}1945")
            == "nineteen fourteen to nineteen forty-five"
        )


def test_normalize_symbols_and_commas():  # finding 15
    assert normalize_text("1,000,000") == "one million"
    assert "fifty percent" in normalize_text("50%")
    assert "R and D" in normalize_text("R&D")


def test_era_markers_only_number_adjacent():  # findings 6, 16
    # Number-adjacent era markers expand (letter-by-letter), longest key first.
    assert normalize_text("in 200 BCE") == "in two hundred B C E"
    assert "ten sixty-six" in normalize_text("AD 1066")
    # Bare words are NOT corrupted.
    assert normalize_text("CE marked goods") == "CE marked goods"
    assert normalize_text("AD tests") == "AD tests"
    # Unambiguous abbreviations still expand unconditionally.
    out = normalize_text("the EEC and USSR")
    assert "E E C" in out and "U S S R" in out


def test_lexicon():
    lex = Lexicon({"Maastricht": "Mahs-trikt", "Monnet": "Moh-nay"})
    out = lex.apply("Monnet signed at Maastricht.")
    assert "Moh-nay" in out and "Mahs-trikt" in out
    assert Lexicon({}).apply("unchanged") == "unchanged"
