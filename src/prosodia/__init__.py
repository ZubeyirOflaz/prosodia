"""Prosodia — script-first, controllable narrated audio.

An LLM-authored, human-editable transcript carrying explicit performance
directions (tone, rate, pause, emphasis) is rendered to narrated audio by a
decoupled, pluggable TTS engine.

Two sides, exchanged through a cloud-synced job folder:

* ``prosodia.author`` — runs anywhere, pure-Python, NO torch/GPU. Plans a
  series, writes & edits transcripts (via headless Claude Code), compiles them
  to an intermediate representation (IR), and packages render jobs.
* ``prosodia.render`` — runs on a machine with an NVIDIA GPU. Watches for jobs
  and renders the IR to audio with a TTS backend (Chatterbox first). Requires
  the ``render`` extra (``pip install prosodia[render]``).
* ``prosodia.core`` — the shared, dependency-light contracts (IR, intent
  vocabulary, job protocol, trace log) that both sides agree on.

See ``DESIGN.md`` for the architecture and decisions.
"""

__version__ = "0.0.1"
