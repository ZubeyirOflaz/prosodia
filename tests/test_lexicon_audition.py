"""Lexicon-audition helpers (entry expansion + page) and a fake-backend smoke test."""

import pytest

from prosodia.render.lexicon_audition import _index_html, _Section, expand_entries


def test_expand_entries_raw_then_lexicon():
    plan = expand_entries({"Thucydides": "Thoo-sid-ih-deez", "Grotius": "Gro-shus"})
    assert [src for src, _ in plan] == ["Thucydides", "Grotius"]  # lexicon order preserved
    labels = [v.label for v in plan[0][1]]
    tokens = [v.token for v in plan[0][1]]
    assert labels == ["as written", "lexicon"]
    assert tokens == ["Thucydides", "Thoo-sid-ih-deez"]


def test_expand_entries_no_raw():
    plan = expand_entries({"Grotius": "Gro-shus"}, include_raw=False)
    assert [v.label for v in plan[0][1]] == ["lexicon"]


def test_expand_entries_names_filter():
    plan = expand_entries({"A": "a", "B": "b"}, names=["B"])
    assert [src for src, _ in plan] == ["B"]


def test_expand_entries_variants_and_unlisted_name():
    plan = expand_entries(
        {"Thucydides": "Thoo-sid-ih-deez"},
        variants={"Thucydides": ["thoo SIH dih deez"], "Xenophon": ["ZEN-uh-fon"]},
    )
    d = dict(plan)
    # existing name gets raw + lexicon + variant 1
    assert [v.label for v in d["Thucydides"]] == ["as written", "lexicon", "variant 1"]
    assert d["Thucydides"][2].token == "thoo SIH dih deez"
    # a name only present in variants is still auditionable (raw + its variant)
    assert "Xenophon" in d
    assert [v.token for v in d["Xenophon"]] == ["Xenophon", "ZEN-uh-fon"]


def test_index_html_escapes_and_lists_players():
    s = _Section(source="Grotius", caption="lexicon: Gro-shus",
                 players=[("lexicon · seed 7", "00_Grotius__1_lexicon__00_narrator__seed7.wav")])
    h = _index_html([s], "start with {} now")
    assert "Grotius" in h and "Gro-shus" in h
    assert h.count("<audio") == 1
    assert "start with {} now" in h  # carrier frame shown


def test_frame_without_placeholder_rejected():
    from prosodia.render.lexicon_audition import lexicon_audition
    with pytest.raises(ValueError, match="placeholder"):
        lexicon_audition(["v"], "out", lexicon={"A": "a"}, frame="no placeholder here")


# --- fake-backend smoke test (needs the audio deps) ---
np = pytest.importorskip("numpy")
pytest.importorskip("soundfile")


class _FakeBackend:
    sample_rate = 16000

    def __init__(self):
        self.calls = []

    def load(self):
        pass

    def generate(self, text, **kw):
        self.calls.append((text, kw))
        return np.ones(2000, dtype=np.float32) * 0.4


def test_lexicon_audition_end_to_end(tmp_path):
    from prosodia.render.lexicon_audition import lexicon_audition

    (vd := tmp_path / "voices").mkdir()
    (vd / "narrator.wav").write_bytes(b"RIFFfake")
    out = tmp_path / "lex_aud"
    backend = _FakeBackend()
    written = lexicon_audition(
        vd, out, lexicon={"Thucydides": "Thoo-sid-ih-deez"},
        backend=backend, takes=2,
    )
    # 1 name x (raw + lexicon) x 1 clip x 2 takes = 4 renders
    assert len(written) == 4
    assert len(backend.calls) == 4
    # the respelling is what gets spoken in the "lexicon" variant
    assert any("Thoo-sid-ih-deez" in c[0] for c in backend.calls)
    assert any("Thucydides" in c[0] and "Thoo-sid-ih-deez" not in c[0] for c in backend.calls)
    html = (out / "index.html").read_text(encoding="utf-8")
    assert html.count("<audio") == 4
