"""Rendering side — runs on the GPU box; requires the ``render`` extra.

Watches the synced inbox for jobs, atomically claims a job once its manifest
validates, and renders the IR to audio with a pluggable TTS backend (Chatterbox
first): sentence-aware chunking under the engine's per-generation cap, real
silence for authored pauses, click-free joins, an STT-based per-chunk quality
gate, and a single final loudness normalization.

Importing the render *submodules* (``render.py``, ``backends.chatterbox_backend``,
etc.) pulls in torch via the TTS backend, so those require the ``render`` extra.
Importing the package itself stays light: ``import prosodia.render`` works on a
base, torch-free install (``cli`` defers its heavy imports), which keeps the
authoring/render dependency boundary intact. The authoring side never imports the
render submodules.
"""
