"""Voice-audition pure helpers (clip discovery + the A/B index page)."""

from prosodia.render.audition import _index_html, discover_clips


def test_discover_clips_dir_only_wavs_sorted(tmp_path):
    (tmp_path / "b.wav").write_bytes(b"x")
    (tmp_path / "a.wav").write_bytes(b"x")
    (tmp_path / "notes.txt").write_text("x", encoding="utf-8")
    got = discover_clips(tmp_path)
    assert [p.name for p in got] == ["a.wav", "b.wav"]  # only .wav, sorted


def test_discover_clips_list_dedupes(tmp_path):
    (tmp_path / "a.wav").write_bytes(b"x")
    (tmp_path / "b.wav").write_bytes(b"x")
    got = discover_clips([tmp_path / "a.wav", tmp_path])  # file + dir overlap
    assert [p.name for p in got] == ["a.wav", "b.wav"]  # a.wav not duplicated


def test_index_html_players_and_text():
    h = _index_html("Hello world.", [("narrator.wav", ["narrator__seed1.wav", "narrator__seed2.wav"])])
    assert "Hello world." in h
    assert h.count("<audio") == 2
    assert "narrator__seed1.wav" in h and "narrator__seed2.wav" in h
