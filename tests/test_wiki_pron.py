"""wiki_pron: wikitext template parsing + fetch orchestration (no network — a fake fetcher)."""

from prosodia.author.wiki_pron import (
    _respell_from_args, _resolve_chain, fetch_pronunciations, parse_wikitext,
)


def test_respell_from_args_basic():
    assert _respell_from_args("thew|SID|ih|deez") == "thew-SID-ih-deez"


def test_respell_from_args_wordspace_and_variant():
    # "_" is a word-space; ",_" separates alternate pronunciations
    assert _respell_from_args("IB|ən|_|hal|DOON") == "IB-ən hal-DOON"
    assert _respell_from_args("NEE|chuh|,_|NEE|chee") == "NEE-chuh, NEE-chee"


def test_parse_wikitext_picks_first_templates():
    wt = ("'''Thucydides''' ({{IPAc-en|θj|uː|ˈ|s|ɪ|d|ɪ|ˌ|d|iː|z}} {{respell|thew|SID|ih|deez}}; "
          "{{lang-grc|Θουκυδίδης}} {{IPA|grc|tʰuːkydǐdɛːs|}}) was an Athenian historian.")
    ipa, respell = parse_wikitext(wt)
    assert respell == "thew-SID-ih-deez"
    assert ipa == "/θjuːˈsɪdɪˌdiːz/"   # English IPAc-en, not the Greek {{IPA|grc}}


def test_parse_wikitext_none_when_absent():
    assert parse_wikitext("'''Hobbes''' (1588–1679) was an English philosopher.") == (None, None)


def _fake_fetch(titles):
    pages = {
        "Thucydides": "'''Thucydides''' ({{respell|thew|SID|ih|deez}}) was Athenian.",
        "Han Fei": "'''Han Fei''' ({{IPAc-en|h|ɑː|n|_|f|eɪ}}) was a philosopher.",  # no respell
    }
    normalized = {"han feizi": "Han Feizi"}
    redirects = {"Han Feizi": "Han Fei"}
    return pages, normalized, redirects


def test_fetch_pronunciations_maps_and_flags():
    prons = fetch_pronunciations(["Thucydides", "han feizi", "Nonexistentname"], opener=_fake_fetch)
    by = {p.name: p for p in prons}
    assert by["Thucydides"].respell == "thew-SID-ih-deez" and by["Thucydides"].found
    # redirect chain resolved; IPA present, respell absent
    assert by["han feizi"].title == "Han Fei" and by["han feizi"].respell is None
    assert by["han feizi"].ipa == "/hɑːn feɪ/" and by["han feizi"].found
    # missing article flagged, not dropped
    assert not by["Nonexistentname"].found and "no Wikipedia article" in by["Nonexistentname"].note


def test_fetch_batch_error_is_isolated():
    def boom(titles):
        raise RuntimeError("network down")
    prons = fetch_pronunciations(["A", "B"], opener=boom)
    assert len(prons) == 2 and all(not p.found and "fetch error" in p.note for p in prons)
