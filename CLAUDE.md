# CLAUDE.md — working in the Prosodia repo

**Read [`DESIGN.md`](DESIGN.md) first — it is the source of truth for this project.** It records the design goals, the decisions already locked in, and the open design decisions still to be made.

## Orientation (one paragraph)

Prosodia turns an LLM-authored, human-editable **transcript with performance directions** (tone/speed/pause/emphasis) into narrated audio via a **decoupled, pluggable TTS engine** (Chatterbox on a local RTX 3080). It exists to beat NotebookLM on transcript control, narration coherence, content↔speech alignment, and multi-episode coverage. Two sides — **authoring** (any machine, no GPU) and **renderer** (Windows 11 + RTX 3080) — exchange jobs through a **cloud-synced folder**.

## Hard rules

- **Don't re-litigate the locked decisions** in `DESIGN.md` §3 (name, Chatterbox-first, synced-folder handoff, single-narrator default + optional two-host, pluggable backend, both preset & cloned voices).
- **The authoring side must not depend on a GPU or on PyTorch.** Keep that dependency boundary strict — it must `pip install` and run on a laptop with no CUDA.
- **The transcript is the source of truth.** Nothing downstream may silently reinterpret it (goal #1).
- The current target is **Phases 0–1** (`DESIGN.md` §6) and resolving the **open decisions** (`DESIGN.md` §7).

## Conventions

- License: MIT (open source). Keep dependencies and any bundled/preset voices license-clear.
- Don't commit audio outputs, model weights, venvs, or synced job folders (see `.gitignore`).
- Don't `git commit`/`push` unless the user asks.
