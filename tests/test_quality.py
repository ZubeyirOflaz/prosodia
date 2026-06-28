"""Tests for the torch-free render helper ``quality.similarity`` (finding 27).

This module imports only difflib/re, so it stays on the authoring boundary and
runs without numpy/torch. The numpy audio helpers are covered in test_audio.py
(skipped when numpy is absent).
"""

from prosodia.render.quality import similarity


def test_similarity_normalizes_case_and_punct():
    assert similarity("Hello, World!", "hello world") == 1.0
    assert similarity("Hello world", "hello   world!") == 1.0


def test_similarity_identical_and_disjoint():
    assert similarity("the quick brown fox", "the quick brown fox") == 1.0
    # Fully disjoint word sets -> low score (char-normalized, not exactly 0).
    assert similarity("the quick brown fox", "zzz totally other phrase") < 0.3


def test_similarity_empty():
    assert similarity("", "") == 1.0
    assert similarity("abc", "") == 0.0
    assert similarity("", "abc") == 0.0


def test_similarity_partial():
    # One word differs -> strictly between 0 and 1.
    score = similarity("the quick brown fox", "the quick brown cat")
    assert 0.0 < score < 1.0
