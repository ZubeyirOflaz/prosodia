"""Shared contracts for both the authoring and rendering sides.

This subpackage is the dependency boundary: it is pure-Python (no torch, no
GPU) and is imported by both ``prosodia.author`` and ``prosodia.render``. It
defines the artifacts the two sides exchange — the intermediate representation
(IR), the engine-neutral intent vocabulary, the synced job-folder protocol, and
the append-only process trace — so neither side can silently reinterpret the
other's output (design goal #1: the transcript is the source of truth).
"""
