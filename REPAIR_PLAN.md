# Repair Plan

Issues found in the Phase-0 self-audit and the hardening pass. **Resolved** items
landed *with a test*. Only the renderer-environment rows remain open, and those
can only be validated on the actual Windows + RTX 3080 box.

## Resolved (with tests)

| ID | Issue | Resolution / test |
|----|-------|-------------------|
| **A1** | Dangling console-script entry points | `author/cli.py` + `render/cli.py`; render CLI defers heavy imports and adds `doctor`. (`tests/test_boundary.py`) |
| **E1** | `render/__init__` overstated the boundary | Reworded; `import prosodia.render` works torch-free. (`tests/test_boundary.py`) |
| **C1** | Voice double-sourced | Optional in front-matter; precedence instruction → front-matter → config. (`tests/test_compile.py::test_voice_precedence`) |
| **C2** | Tone vocabulary duplicated | `voice_profiles.yaml` is the single source; SPEC references it; compiler warns + falls back. (`tests/test_tone.py`) |
| **C3** | Pause defaults stated twice | Defaults centralized; front-matter can override. (`tests/test_compile.py::test_front_matter_pauses_override`) |
| **D1** | Directive parsing must be quote-aware | Quote-aware tokenizer. (`tests/test_compile.py::test_parse_directives_quote_aware`) |
| **D2** | Front-matter `---` vs body thematic break | Leading-fence-only front-matter. (`tests/test_compile.py::test_body_thematic_break_not_front_matter`) |
| **D3** | `format_version` float + title brace | Quoted version; trailing-brace beat directives. (`tests/test_compile.py::test_beat_title_trailing_brace`) |

## Open — validate on the GPU box

| ID | Issue | Fix in place | How to verify |
|----|-------|--------------|---------------|
| **B1** | `[render]` extra can pull a CPU/wrong torch; ffmpeg is a system dep | `setup.ps1` installs CUDA torch → `prosodia[render]` → ffmpeg, in that order; `prosodia-render doctor` asserts `torch.cuda` + ffmpeg | `prosodia-render doctor` returns OK on the 3080 box |
| **B2** | Render box needs Python 3.11/3.12 (not 3.13+) | `setup.ps1` pins `py -3.11`; render CLI errors on ≥3.13 | `doctor` reports a version problem on 3.13+ |

## Known scope limits (documented, not bugs)

- **Two-host rendering** is not yet wired: `@speaker` tags are parsed and validated
  into the IR, but the renderer voices the whole episode with one voice (no
  per-speaker voice or turn-taking gaps). See `DESIGN.md` §11 row 16 and the README.
- **Renderer unproven on hardware**: the render path is unit-tested but has not had
  an end-to-end audio run on the RTX 3080 yet — the first A/B target
  (`docs/AB_TESTING.md`).
