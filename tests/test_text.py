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


def test_normalize_decades():
    # "1820s" matched neither _YEAR (trailing \b fails before the 's') nor _INT, so it
    # reached the engine as raw digits. Decades now spell out.
    assert normalize_text("the late 1820s") == "the late eighteen twenties"
    assert normalize_text("the 1890s") == "the eighteen nineties"
    assert normalize_text("the 1900s") == "the nineteen hundreds"
    assert normalize_text("the 1860s were loud") == "the eighteen sixties were loud"
    assert "1820" not in normalize_text("1820s")  # no raw digits leak through


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


def test_space_grouped_thousands_are_one_number():
    """EU legal texts group thousands with spaces, not commas.

    `_INT` understood only the comma form, so "EUR 35 000 000" was read as three
    separate numbers and spoken as "thirty-five zero zero" — a different figure,
    from a transcript that looked correct. The Act's own penalty amounts are
    written this way, so the docket supplies them in exactly this shape.
    """
    assert normalize_text("EUR 35 000 000") == "EUR thirty-five million"
    assert normalize_text("EUR 7 500 000") == "EUR seven million five hundred thousand"
    assert "1 000" not in normalize_text("1 000 words")


def test_exponents_are_spoken_as_powers():
    # "10^25" was read as "ten caret twenty-five"; it is the GPAI systemic-risk threshold.
    assert "ten to the twenty-fifth" in normalize_text("greater than 10^25 operations")


def test_article_citations_are_spoken_as_citations():
    assert normalize_text("Art. 6(3)") == "Article six, paragraph three"
    assert normalize_text("Art. 5(1)(g)") == "Article five, paragraph one, point g"
    assert normalize_text("Arts. 51-56") == "Articles fifty-one to fifty-six"
    # a bare hyphenated pair outside a citation context is left alone (it may be a dash)
    assert "to" not in normalize_text("51-56")


def test_day_month_dates_take_an_ordinal():
    # "2 August 2026" was spoken as "two August"; a regulatory series says dates constantly.
    assert normalize_text("on 2 August 2026") == "on the second of August twenty twenty-six"
    assert normalize_text("the 31 July 2026") == "the thirty-first of July twenty twenty-six"
