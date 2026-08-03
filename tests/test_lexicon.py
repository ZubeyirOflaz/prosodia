"""Lexicon apply + reverse (the reverse map feeds the render STT gate)."""

from prosodia.author.lexicon import Lexicon


def test_apply_whole_word_longest_first():
    lex = Lexicon({"Ibn": "Ib-un", "Ibn Khaldun": "Ib-un Khal-doon"})
    # longer key wins; whole-word only
    assert lex.apply("Ibn Khaldun wrote") == "Ib-un Khal-doon wrote"
    assert lex.apply("Ibnx") == "Ibnx"  # not a whole word


def test_reverse_roundtrip():
    lex = Lexicon({"Thucydides": "Thoo-sid-ih-deez", "Ibn Khaldun": "Ib-un Khal-doon"})
    original = "His name was Thucydides, and Ibn Khaldun came later."
    assert lex.reverse(lex.apply(original)) == original


def test_reverse_maps_respellings_back():
    lex = Lexicon({"Thucydides": "Thoo-sid-ih-deez"})
    assert lex.reverse("So Thoo-sid-ih-deez tells us.") == "So Thucydides tells us."


def test_reverse_longest_respelling_first():
    # respellings, not sources, are matched here; the longer respelling must win so a
    # shorter one that is a prefix can't grab part of it.
    lex = Lexicon({"A": "Ib-un", "B": "Ib-un Khal-doon"})
    assert lex.reverse("Ib-un Khal-doon") == "B"


def test_reverse_empty_lexicon_is_identity():
    assert Lexicon({}).reverse("untouched Thoo-sid-ih-deez") == "untouched Thoo-sid-ih-deez"


def test_load_bare_lexicon_key_is_empty(tmp_path):
    # A `lexicon:` key with no children parses to None — must load as empty, not crash.
    p = tmp_path / "lex.yaml"
    p.write_text("# header\nlexicon:\n", encoding="utf-8")
    lex = Lexicon.load(p)
    assert lex.entries == {}
    assert lex.apply("Thucydides stays") == "Thucydides stays"
