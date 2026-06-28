"""Pluggable TTS backends.

Chatterbox is the first implementation; cloud engines (e.g. Gemini multi-speaker
TTS, ElevenLabs) and other local engines (Orpheus, Higgs Audio, Dia, Kokoro) can
be added later behind the same ``TTSBackend`` interface defined in ``base.py``.
"""
