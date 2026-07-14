# Prosodia — Design & Build Context

> **Handoff note.** This file was written at standard effort to **preserve context before a max-effort design pass** (the user will switch effort to `max`, which resets the conversation). It records the **design goals** and the **decisions already locked in** (with rationale), and then explicitly hands the remaining, design-heavy choices to the higher-effort pass.
>
> **For the max-effort model picking this up:** treat §2 (Goals) and §3 (Locked decisions) as fixed inputs — don't re-litigate them. Your job is to design and build the items in **§7 (Open decisions)**, following the proposed architecture in §5 as a starting recommendation (refine it freely). Phases 0–1 of §6 are the immediate target.

---

## 1. What Prosodia is

**Prosodia** is a script-first, fully controllable narrated-audio generator. An LLM (Claude, via Claude Code) writes a transcript that carries explicit *performance directions* (tone, speed, pauses, emphasis); a **decoupled, pluggable text-to-speech engine** then renders that transcript to audio. The local TTS engine is **Chatterbox**, running on the user's RTX 3080 Windows machine.

It exists because **NotebookLM**'s "audio overview" feature, while convenient, indirectly controls the final output and produced four recurring problems (see §2) for long-form, multi-episode narrative content (e.g. "Hardcore History"–style deep dives). Prosodia's thesis: **decouple the script from the voice**, give the human direct control of the transcript, and feed the TTS explicit per-section delivery guidance.

Non-profit, open source, MIT-licensed. Repo: `github.com/ZubeyirOflaz/prosodia`.

---

## 2. Design goals (the "why" — fixed)

The four problems Prosodia must improve on, in the user's own framing:

1. **Directly controllable transcript.** NotebookLM's output is only *indirectly* guided, causing wrong emphasis on topics, narrative breaks, and synthetic-feeling dialogue. → The transcript must be the human-editable source of truth; nothing downstream may reinterpret it.
2. **No forced two-person format.** Constant speaker-switching makes listeners lose focus, and switches land at unnatural moments. → Single narrator by default; multi-speaker only when explicitly chosen.
3. **Content↔speech alignment.** NotebookLM's delivery diverges from the ideal emotion for the content: missing pauses at critical points, speakers nearly interrupting each other, overall synthetic flow. → The system must pass the TTS explicit **tone and speed guidance per section**, plus controlled pauses.
4. **Adequate multi-episode coverage.** A multi-episode series divides content poorly — skipping significant portions or repeating large sections across episodes. → The authoring side must plan coverage across the whole series and enforce non-overlap / no-gaps.

Meta-goals (also fixed):

5. **Decoupled transcript generation and speech output** — so different TTS engines/configs can be swapped and A/B-tested.
6. **Remote authoring without GPU access** — author transcripts from any machine; the GPU box only renders.
7. **Simple Windows 11 setup** — a couple of trigger scripts install all dependencies on the GPU PC.

---

## 3. Locked decisions (do not re-litigate)

| Decision | Choice | Rationale |
|---|---|---|
| **Name** | `prosodia` | Chosen over bare `prosody` (which collides with the Wikipedia-notable Prosody IM XMPP server *and* the generic linguistics term → heavy SEO dilution). `prosodia` is rarer/more ownable; only real collision is `prosodia.io` (a niche dev-metrics SaaS, no Wikipedia article) + `prosodia.de` (a German publisher). PyPI `prosodia` is free; the GitHub user `prosodia` is a dormant 1-repo account (so the project lives at `ZubeyirOflaz/prosodia`). |
| **License** | MIT | Already in repo; aligns with Chatterbox (MIT). |
| **Primary TTS engine** | **Chatterbox** (Resemble AI) | Best open-source naturalness (beat ElevenLabs ~63–65% in blind tests); single consistent voice; **per-chunk emotion (`exaggeration`) and pacing (`cfg_weight`) dials** that map directly onto goal #3; mature long-form/audiobook tooling; `pip install chatterbox-tts`. |
| **Hardware fit** | Verified on RTX 3080 (10 GB) | Original 0.5B model ≈ 5–7 GB VRAM; Turbo 350M ≈ 4.5 GB. Comfortable with headroom. |
| **Transcript authoring** | Claude (Claude Code) writes it; **human edits it directly** | Serves goal #1 — transcript is the source of truth. |
| **Decoupling** | Transcript generation and speech rendering are **separate stages** with a defined interchange artifact | Serves goals #5/#6; lets us swap TTS engines. |
| **Handoff mechanism** | **Cloud-synced folder** (Syncthing recommended; Dropbox/Drive acceptable) | User's choice. No open ports, no public endpoint; author drops a job, GPU PC watches & renders, audio syncs back. Needs an atomicity marker so the watcher never grabs a half-synced job. |
| **Voice source** | **Support both** preset voices and cloned voices (Chatterbox does ~5 s zero-shot cloning); configurable per job | User's choice ("decide later / support both"). |
| **Narrator format** | **Single narrator by default; optional two-host** via explicit speaker tags per segment | User's choice; directly serves goal #2. |
| **TTS backend architecture** | **Pluggable interface; implement Chatterbox first** | User's choice ("Chatterbox now, pluggable later"). Cloud backends (Google Gemini multi-speaker TTS, ElevenLabs) and other local engines (Orpheus, Higgs Audio v2) added later behind the same interface. |
| **Tone / delivery control** | **Two layers:** engine-neutral *delivery intent* baked into the transcript + a **separate, instructable mapping layer** (a mapping agent guided by user-authored instructions/anchors) that compiles intent → engine-specific params | User-confirmed. Cleanly decouples the TTS layer (goal #5); gives a single place to tune delivery and encode Phase-4 calibration without editing transcripts; keeps the transcript human-editable (#1). The engine-native alternative (bake Chatterbox knobs into the transcript directly) was considered and **declined** in favor of portability. See §10-F. |
| **Authoring location** | Any machine, no GPU; pure-Python (no torch) | Serves goal #6. |
| **Render location** | The user's separate **Windows 11 PC with RTX 3080** | Fixed hardware. |

---

## 4. Verified facts & external references (don't re-research these)

**Chatterbox**
- VRAM: original/multilingual 0.5B ≈ 5–7 GB; Turbo 350M ≈ 4.5 GB → fits the 3080's 10 GB. ([install/VRAM](https://dev.to/nodeshiftcloud/how-to-install-and-run-chatterbox-locally-5fd2))
- Controls: `exaggeration` (0=flat → 0.5 default → 1+=theatrical, **emotion intensity, per generation/chunk**); `cfg_weight` (lower ≈ slower/more deliberate pacing; ~0.3 for fast reference voices); plus `temperature`, `top_p`, `min_p`, `repetition_penalty`. ([params](https://www.segmind.com/models/chatterbox-tts))
- **~40 s per generation** for best quality → long-form needs **sentence-aware chunking + concatenation**. Audiobook forks already do this.
- Tooling: `pip install chatterbox-tts`; **devnen/Chatterbox-TTS-Server** exposes an **OpenAI-compatible HTTP API** + voice cloning + audiobook-scale chunking ([repo](https://github.com/devnen/Chatterbox-TTS-Server)); psdwizzard/chatterbox-Audiobook and petermg/Chatterbox-TTS-Extended are audiobook-oriented forks.
- **Nuance / limitation:** emotion is a **per-chunk scalar**, not inline SSML/emotion tags, and there's **no SSML `<break>`** — pauses must be inserted as real silence at marked beats, and tone shifts happen at chunk boundaries. This actually fits goal #3's "per-section guidance" model well.

**Alternatives kept behind the pluggable interface (for later)**
- **Orpheus** (Llama-based): 8 inline emotion tags (`<laugh>`, `<sigh>`, etc.), zero-shot cloning — more granular per-moment emotion, slightly lower naturalness.
- **Higgs Audio v2**: very expressive, heavier.
- **Dia** (Nari Labs, 1.6B): purpose-built for **scripted multi-speaker dialogue** with nonverbal cues (laughs, sighs) — the strongest candidate if/when the optional two-host mode matters.
- **Kokoro** (82M): runs on **CPU**, 54 preset voices — the no-GPU fallback / lowest-resource option.
- **Cloud**: **Google Gemini multi-speaker TTS** (label speakers in the transcript → distinct consistent voices; free tier w/ rate limits — closest to "NotebookLM engine, your script") and **ElevenLabs** (top fidelity + cloning). Useful as a **GPU-off fallback** for fully remote rendering.

**Claude API reality (why TTS is a separate stage):** the Claude API is text-only output (no audio/TTS endpoint); Claude's app "voice mode" is app-level (ElevenLabs subcontractor), not an exportable audio API. So Claude writes; a separate engine voices.

**Handoff:** Syncthing (LAN-direct, private, no size caps) is the recommended sync layer; any synced folder works.

---

## 5. Proposed architecture (a recommendation — refine in the design pass)

> This is the shape sketched during the design dialogue. The max-effort pass should treat it as a strong starting point and finalize the details flagged in §7.

```
┌───────────────────────────┐        synced folder         ┌────────────────────────────┐
│  AUTHORING (any machine)   │      (Syncthing/Dropbox)     │   RENDER (Win11 + RTX 3080) │
│  Claude writes & human     │   inbox/<job>/  ──────────▶  │  watcher claims job (atomic) │
│  edits:                    │     transcript.md (edit!)    │  compile → IR → chunk        │
│   • series + coverage map  │     transcript.json (IR)     │  map tone/speed → Chatterbox │
│   • transcript.md          │     job.yaml, voice_ref.wav  │  insert pauses → render      │
│   • compile + submit tools │     job.ready (atomic flag)  │  concat → mp3 + chapters     │
│                            │   outbox/<job>/ ◀──────────  │  write status.json + audio   │
└───────────────────────────┘     episode.mp3, status.json └────────────────────────────┘
```

> **Superseded by §11.** The `mp3` / `mp3 + chapters` wording in this sketch and in
> the §6 phase table is out of date: the renderer as built writes a flat
> `episode.wav` (WAV, loudness-normalized) with **no chapter markers**. Read §11
> for the as-built behavior.

**Proposed repo layout** (note: the authoring/renderer split and single-vs-two-package question is itself an OPEN decision — see §7):

```
prosodia/
  authoring/                 # no GPU, pure-Python, runs remotely
    series/                  # series.yaml, coverage_map, episodes/*.md
    formats/SPEC.md          # transcript markup spec
    voice_profiles.yaml      # tone/rate words → TTS params (tunable)
    compile_transcript.py    # transcript.md → transcript.json (IR) + validate
    submit.py                # package a job → synced inbox/ (+ job.ready)
    lint_coverage.py         # multi-episode overlap/gap check
  renderer/                  # Win11 + 3080
    setup.ps1                # one-shot deps: venv, CUDA torch, chatterbox, ffmpeg, weights
    start_renderer.ps1       # launch watcher (optionally a Scheduled Task)
    watch_and_render.py      # polls inbox/, atomic-claims via job.ready
    render.py                # IR → chunk → params → pauses → concat → mp3
    backends/base.py         # TTSBackend interface
    backends/chatterbox_backend.py
  protocol/SPEC.md           # job-folder contract (inbox/processing/outbox/failed)
  DESIGN.md                  # this file
  CLAUDE.md
```

**How each goal maps to a component:**
- #1 (control) → `transcript.md` is source of truth; renderer voices exactly the compiled IR.
- #2 (single narrator) → format defaults to one speaker; `@speaker` tags opt-in to two-host.
- #3 (content↔speech) → inline tone/speed/pause directives + `voice_profiles.yaml` mapping words→Chatterbox params + programmatic silence insertion.
- #4 (coverage) → authoring-side `coverage_map` (every topic assigned to exactly one episode) + `lint_coverage.py`.

---

## 6. Build plan (phases)

| Phase | Deliverable | Side | Notes |
|---|---|---|---|
| **0. Contracts** | Transcript-format SPEC, IR JSON schema, job-protocol SPEC, `voice_profiles.yaml` mapping | authoring | **Immediate target.** Design-heavy → max-effort pass. |
| **1. Authoring pipeline** | `compile_transcript.py` (+ validation), `submit.py`, one sample episode | authoring | **Immediate target.** Testable with no GPU. |
| **2. Renderer core** | `setup.ps1`, Chatterbox backend, `render.py` (chunk/pause/concat); CLI render of a local IR → mp3 | GPU PC | User runs `setup.ps1`. |
| **3. Decoupled handoff** | Syncthing config, `watch_and_render.py`; end-to-end drop→mp3 | both | Joint test. |
| **4. Tone/pacing tuning** | Calibrate `voice_profiles.yaml`, pauses, emphasis; A/B naturalness | both | Serves #3. |
| **5. Coverage tooling** | `coverage_map` planner + `lint_coverage.py`; validate on a real series | authoring | Serves #4. |
| **6. Pluggable + polish** | Add a cloud backend behind the interface; autostart service; docs | both | |

---

## 7. OPEN design decisions — for the max-effort pass

These were deliberately **not** decided yet, so the higher-effort model can design them well. Each should be resolved in Phase 0/1:

1. **Transcript markup grammar.** Exact syntax for directives (tone, rate, pause, emphasis) and `@speaker` tags. Inline tags vs front-matter blocks vs both. Must stay hand-editable (goal #1) and unambiguous to parse. *(Sketch shown during dialogue used `[[tone: somber, rate: slow]]`, `[[pause: 1.2s]]`, `[[emphasis]]…[[/emphasis]]`, `@narrator` — illustrative only.)*
2. **IR (intermediate representation) schema.** The `transcript.json` the renderer consumes. Proposed per-segment fields: `{speaker, text, tone, rate, exaggeration, cfg_weight, temperature, pre_pause_ms, post_pause_ms}`. Finalize fields, types, validation, versioning.
3. **`voice_profiles.yaml` vocabulary + mapping.** The set of tone words (somber/neutral/dramatic/…) and rate words (slow/normal/fast) and their numeric Chatterbox param values. Keep it tunable without re-authoring transcripts.
4. **Chunking & joins.** Sentence-aware splitting strategy under the ~40 s cap; concatenation with click-free joins (tiny crossfade?); chapter markers.
5. **Pause insertion.** How marked pauses become silence (durations, placement, leading/trailing trim of generated chunks).
6. **Job-folder protocol.** Exact folder names (`inbox/processing/outbox/failed`), file set per job, `status.json` schema, error handling, and the **atomic-claim mechanism** (e.g. a `job.ready` marker written last + atomic move) that survives a cloud-sync race.
7. **Chatterbox integration mode.** Direct `chatterbox-tts` Python lib vs the devnen OpenAI-compatible HTTP server. Pick during renderer build (the HTTP server may simplify the decoupled/remote model).
8. **Repo packaging.** One package or two (authoring = pure-Python no-torch; renderer = torch/CUDA). Affects `setup.ps1` and pip metadata. Authoring must install with **no torch** to stay light on the remote machine.
9. **Coverage planner + lint.** `series.yaml` schema; how Claude generates the `coverage_map` (assign each topic to exactly one episode, with covered/referenced/out-of-scope flags + per-episode boundary notes); whether `lint_coverage.py` is heuristic or LLM-assisted.
10. **Windows setup specifics.** Python version (3.11 suggested); the **correct CUDA PyTorch wheel for the 3080**; ffmpeg install (winget?); model-weight download on first run; Syncthing install/config; autostart (Scheduled Task / NSSM). Goal: **two scripts** — `setup.ps1` (once) + `start_renderer.ps1`.
11. **CLI/config ergonomics, determinism (seed handling), and a testing strategy.**
12. **Mapping-layer design.** *(Architecture now LOCKED — two layers, see §3 "Tone / delivery control" and §10-F. What remains open is the mapping layer's design.)* Decide: the **instruction/profile format** the mapping agent consumes; whether it's a **hybrid** of a numeric anchor table (for determinism/reproducibility) + natural-language guidance (for nuance) — recommended — vs pure-table or pure-agent; how **per-engine and per-voice profiles** are structured; and the engine-neutral *intent* vocabulary itself (rich/descriptive, not a coarse enum, so rich engines like Gemini aren't starved). The IR sits between the two layers — confirm it carries intent, with the engine-specific render-plan as a derived artifact.
13. **Text normalization for narration.** How the IR/renderer converts numbers, dates, symbols, and abbreviations ("1957", "§45a", "27", "EEC") to spoken form — Chatterbox has no SSML to lean on. See §10-D.
14. **Pronunciation overrides.** A per-project lexicon for proper nouns / non-English names (Schuman, Montesquieu, Ibn Khaldun, Maastricht), since there's no SSML phoneme support. See §10-E.
15. **Pause authoring policy.** Whether pauses are author-marked vs renderer-inferred, their durations, and how "critical-point" pauses (goal #3) are decided and placed.
16. **Two-host turn-taking & timing** (optional multi-speaker mode): inter-speaker gaps/ordering to avoid NotebookLM's "near-interruption" artifact. See §10-I.

---

## 8. Constraints & gotchas to remember

- **Torch + CUDA on Windows** — must match a CUDA wheel to the 3080; the #1 setup friction point.
- **ffmpeg** required for audio concat/export.
- **~40 s Chatterbox chunk cap** → mandatory chunking; watch for artifacts at joins.
- **Sync atomicity** — a cloud-synced folder can deliver a job half-written; gate the watcher on a last-written `job.ready` marker.
- **Model-weight download** size on first render-side run.
- **Determinism** — seed the generation for reproducible renders.
- **License cleanliness (OSS)** — preset voices and any reference clip used for cloning must be license-clear; document this. Chatterbox itself is MIT.
- **Authoring must not require a GPU or torch** — keep that dependency boundary strict.

---

## 9. Provenance

This document distills a multi-turn design dialogue (held in a different repo's Claude Code session) covering: NotebookLM's limitations, Claude's lack of an audio-output API, a survey of cloud + local TTS engines, verification that Chatterbox runs on the RTX 3080, and a naming exercise that landed on `prosodia`. The four numbered problems in §2 are the user's original requirements verbatim in intent. Everything in §3 is settled; everything in §7 is open.

---

## 10. Homework — deeper design questions to study & refine

Beyond the must-resolve build decisions in §7, these cross-cutting questions deserve dedicated study. Each notes the goal(s) and phase(s) it most affects. They surfaced from re-reading the full design dialogue and from the nature of the target content (long-form historical narration).

**A. Leverage the existing test corpus (don't start from a blank page).** Two hand-written, NotebookLM-targeted narrative series already exist and are ideal migration + validation content. They also already encode tone/pacing/structure *intent* in each file's `CUSTOMIZE PROMPT` + `EPISODE-SPECIFIC TENSION` headers and a shared style prompt — i.e. a working prototype of what Prosodia's format must capture:
  - `C:\Users\zuebe\Documents\Repos\tum_ai_in_society\aptitude_test_prep\exam_preparation_dashboard\audio_sources\eu_history_series\` (6 episodes + README)
  - `…\audio_sources\political_thinkers_series\` (10 episodes + README)
  Use them to (a) reverse-engineer how expressive the transcript format must be, and (b) act as the Phase 5 coverage-validation corpus. *[Goals #1,#3,#4; Phases 0,5]*

**B. Authoring "house style" / narrative-craft layer.** The target is Dan-Carlin-style immersion (stakes, vivid scene-setting, rhetorical questions, cliffhangers) — and Carlin is a *solo* narrator, which is *why* single-narrator is the default, not merely a preference. Define a series-level style spec + per-episode intent notes that guide **what Claude writes** (distinct from the mechanical markup that guides **how the TTS speaks**). The existing series READMEs are a working prototype. *[Goals #1,#2,#3]*

**C. Naturalness evaluation method.** Phase 4 tuning needs a bar. Define an A/B protocol (Prosodia vs NotebookLM on the *same* script) and a rubric (emphasis correctness, pause placement, flow, absence of synthetic artifacts). Use professional narration as the reference bar — e.g. Hardcore History, History of Philosophy Without Any Gaps. *[Goal #3; Phase 4]*

**D. Text normalization for narration.** History content is dense with numbers, dates, symbols, abbreviations ("1957", "§45a", "27 states", "EEC", "WWII"). With no SSML, decide where/how these become correct spoken forms before synthesis. *[Goal #3; Phases 0,2]*

**E. Pronunciation control.** Proper nouns and non-English names (Schuman, Montesquieu, Rousseau, Bakunin, Ibn Khaldun, Gramsci, Maastricht) are a recurring narration-quality killer and easy to overlook. With no SSML phonemes in Chatterbox, design a per-project pronunciation lexicon (respelling/phonetic hints, or curated reference pronunciations). *[Goal #3; Phases 0,2]*

**F. Where engine-specific tone control lives (two-layer design).** (Also §7-12.) This was explicitly questioned: *shouldn't Claude just set the tone in the target engine's own configuration method?* **DECIDED (user-confirmed) — separate intent from engine config across two layers, with Claude driving both:**
  - **Transcript (source of truth):** Claude writes words + *delivery intent* as rich, human-editable descriptive notes ("hushed, almost reverent, long beat before the last line") — **not** engine knobs. Stays portable and durable.
  - **Engine-aware adapter (compile step):** translates intent → the target engine's actual config (Chatterbox `exaggeration`/`cfg_weight`, Gemini free-text style prompt, Orpheus emotion tags). **This adapter can itself be a Claude pass** ("you're targeting Chatterbox; here are its knobs + Phase-4 calibration; emit the render plan"), so no loss of Claude's per-segment intelligence — the engine-specific output is a *derived render-plan*, not the hand-authored transcript.

  Why not bake engine config into the transcript directly: it breaks the swap-engines goal (#5), pollutes the human-editable source (#1), and is brittle across model upgrades; also, the correct scalar for a given tone is *empirical* (Phase 4), so Claude shouldn't hardcode numbers a priori. Keep the intent vocabulary **rich/descriptive, not a coarse enum**, or rich engines like Gemini lose capability.

  **The instructable mapping layer is a feature, not just glue:** because it's separately instructable, it becomes the single place to (a) tune the whole show's delivery feel without touching transcripts, (b) store Phase-4 calibration as instructions/anchors, and (c) hold per-engine **and** per-voice profiles. Recommended shape: a **hybrid** — numeric anchor table (determinism/reproducibility) + natural-language guidance for the mapping agent (nuance) — not pure-table or pure-agent.

  **Override considered and declined:** authoring engine-native directives directly into the transcript (simpler, Chatterbox-only) was weighed and rejected in favor of portability/goal #5. *[Goals #1,#5; Phases 0,4,6]*

**G. Tone↔pace coupling in Chatterbox.** `exaggeration` and `cfg_weight` are *not* independent (higher exaggeration speeds speech; lower cfg_weight slows it). The tone/rate→param mapping (`voice_profiles.yaml`) must model the interaction, not set the two dials separately. *[Goal #3; Phase 4]*

**H. Voice consistency across chunks and episodes.** With ~40 s chunking and multi-episode series, guard against timbre/pacing drift between chunks and across episodes (fixed seed, identical reference clip/conditioning, loudness normalization). *[Goal #2; Phases 2,4]*

**I. Two-host timing & turn-taking (optional mode).** (Also §7-16.) When multi-speaker is used, design inter-speaker gaps/ordering (per-turn lead-in/trail silence?) to avoid the "near-interruption" artifact that made NotebookLM's dialogue feel synthetic. *[Goal #3; Phase 2]*

**J. Cross-episode continuity.** Beyond non-overlap (goal #4): a recap/callback policy — brief "previously / coming up" boundaries and intentional callbacks — plus a check that later episodes don't *re-explain* already-covered material. *[Goal #4; Phase 5]*

**K. Audio post-processing & delivery.** Loudness normalization (podcast standard ≈ −16 LUFS), optional intro/outro or music bed, output container/bitrate, and embedded chapter metadata. *[Phases 2,6]*

**L. Render throughput & completion signal.** Estimate render time on the 3080 (~10-min episodes synthesized in ~40 s chunks) to set expectations and decide on batching; and how the authoring side learns a job finished (poll `outbox/` vs a push notification). A side benefit of local rendering worth noting: it removes NotebookLM's hard per-day generation quota entirely. *[Phases 2,3]*

**M. Future / secondary.** Multilingual narration (Chatterbox has a multilingual 0.5B); and a cloud-backend GPU-off path (Gemini/ElevenLabs) for rendering when the 3080 box is unavailable — both fit naturally behind the pluggable interface. *[Phase 6]*

---

## 11. Implementation status & resolved decisions (PoC)

What the PoC build settled for the §7 open decisions, and where each lives. Known
follow-ups are tracked in `REPAIR_PLAN.md`.

**Architecture as built** (supersedes the §5 sketch's single "authoring" box):

- **Authoring** is a role-separated, traced, looped multi-agent process driven by
  **headless Claude Code** (`claude -p`, subscription auth, no API key):
  **Planner → (plan critic) → Writer ⇄ Editor loop → Tone specialist**. Every stage
  writes into a per-episode `run/` folder — id-linked, status-bearing events
  (`events.jsonl` + `run.json`), content-hashed artifacts, **versioned Writer/Editor
  rounds** (no overwrite), and a `lineage.json` mapping each final segment back
  through its stages. `prosodia.author.orchestrate` + the active persona's
  `personas/<persona>/roles/*.md` (the shared `diagnostician` stays at
  `author/roles/`), and the Planner also reads the project's `research/` docket;
  loop logic unit-tested with an injectable runner.
- **Observability & diagnosis** read that one store two ways: `prosodia trace-report`
  renders the run to a self-contained HTML viewer, and `prosodia diagnose "<complaint>"`
  ranks the probable stage(s) behind a reported problem — a deterministic signal pass
  (tone fallbacks, warn/error events, an unresolved editorial loop, compile warnings),
  optionally refined by a Claude agent (`roles/diagnostician.md`) — into an HTML report.
  `core/trace.py` (`Run`), `core/lineage.py`, `core/diagnosis.py`, `author/trace_view.py`.
- **Personas** make the authoring voice switchable: each persona is a self-contained
  set of role prompts + tone table + defaults in a reusable library
  (`author/personas/<name>/`), chosen per project via `series.yaml` `persona:`
  (default `hardcore-history`). Built-ins: `hardcore-history` (the original dramatic
  voice) and `thinkers` (ideas-in-their-time — Carlin × Sandel). `author/persona.py`;
  `prosodia personas` / `persona-new`; the `diagnostician` role stays shared.
- **Two-layer tone** (§7-12/§10-F): the transcript carries engine-neutral intent;
  the **Tone specialist** compiles intent → engine params. Stage 1 is the
  deterministic table `author/personas/<persona>/voice_profiles.yaml`
  (`author/tone.py`); an
  LLM-driven version is an optional later upgrade. `render_plan.json` is derived.
- **Renderer** is a deterministic, LLM-free function of (IR + render_plan + voice +
  seed) on the GPU box: chunk → generate → pause silence → trim → 20 ms crossfade →
  concat → STT quality gate (faster-whisper) → loudness-normalize once, bookended by 4 s lead/tail silence and (by default) a spoken title;
  fast-preview vs final modes. `prosodia.render.*`.

**Resolved §7 decisions:**

| §7 | Decision / location |
|---|---|
| 1 Transcript grammar | Hybrid: front-matter + `## beat {tone, rate}` + `{pause}` + `*emphasis*` — `formats/SPEC.md`. |
| 2 IR schema | `prosodia.core.ir` (pydantic); Segment carries intent, authored_text, spoken_text, pause_before_ms, emphasis, chunks. |
| 3 voice_profiles | `author/personas/<persona>/voice_profiles.yaml` — each persona's source of truth for tone words + pause defaults. |
| 4 Chunking | sentence-aware pack to ~300 chars with split cascade (`author/chunk.py`). |
| 5 Pauses | real silence at segment boundaries; explicit `{pause}` + paragraph/beat defaults. |
| 6 Job protocol | `protocol/SPEC.md` — manifest (sha256+size) atomic claim + building→inbox rename. |
| 7 Integration | in-process library behind a `TTSBackend` interface, model kept warm. |
| 8 Packaging | one package `prosodia`; base = pure-Python authoring, `[render]` extra = torch/Chatterbox. |
| 9 Coverage | `series.yaml` coverage map + series-level `scope` + Planner role (builds from a per-project `research/` docket); a lint pass is future. |
| 10 Windows setup | `scripts/setup.ps1` + `start_renderer.ps1` (CUDA torch first, Py 3.11, ffmpeg, logon task). |
| 11 Determinism/CLI | derived per-chunk seeds; `prosodia` / `prosodia-render` CLIs; pytest suite. |
| 12 Mapping layer | table-first deterministic; LLM optional. |
| 13 Normalization | `author/normalize.py` (years, ranges, §, era abbreviations). |
| 14 Pronunciation | per-project `lexicon.yaml` (`author/lexicon.py`), applied to spoken_text only. |
| 15 Pause policy | author-marked + paragraph/beat defaults (configurable). |
| 16 Two-host | `@speaker` tags + front-matter `speakers` map are **parsed into the IR and validated** (unknown `@tag` warns); single-narrator is the default/tested path. **Not yet wired in the renderer:** per-speaker voice resolution and turn-taking gaps — the renderer currently voices the whole episode with one resolved voice. |

**Voice resolution (§3 / repair C1):** instruction-time override → front-matter
`voice` → project-config default.

**First validation target:** `projects/eu_history/` (ep1 authored, compiled,
packaged). A/B vs NotebookLM on EU ep1–3 per `docs/AB_TESTING.md`. The first
`thinkers`-persona series is `projects/political_thinkers/` ("The Long Argument" —
a 20-episode outline built from a verified docket, with episodes 1–2 authored and
compiled).

---

## 12. Authoring UI (planned)

A single, barebones **local** interface unifying the authoring commands (plan,
write, compile, trace, diagnose, persona/transcript management) so the pipeline
isn't driven by CLI flags alone. **Built** as `prosodia ui` (Phases 1–4). Decision
recorded here; full rationale and the options comparison in
[`docs/authoring-ui.md`](docs/authoring-ui.md):

- **Backend: Python standard-library `http.server`** (a `ThreadingHTTPServer` bound
  to `127.0.0.1`) — **zero new dependencies**, so the torch-free authoring install
  stays `pydantic + pyyaml`. It reuses the self-contained HTML the project already
  emits (`author/trace_view.py`, `plan-view`) and reads status straight from the
  existing `Run` trace store. A small thread-based job runner **serializes** the
  long `claude -p` jobs (concurrent sessions contend) and runs fast ops inline.
- **Frontend: a tiny in-house interactivity layer** — htmx-style `data-*` attributes,
  ~60 lines served at `/assets/app.js` (not a Python dependency, no build step, no
  external file) — for live job progress and inline actions via partial HTML swaps. A
  deliberate drop-in stand-in for htmx.
- **Sanctioned upgrade: Flask** — identical architecture; adopt only if hand-rolled
  routing/templating outgrows a comfortable dispatch table (htmx's many small
  endpoints are the likely trigger). FastAPI/Textual are situational;
  Streamlit/Gradio are rejected (they violate the dependency budget).
- **Phased**: (1) read-only dashboard → (2) trigger jobs with live status → (3)
  in-browser transcript editing + recompile → (4) diagnosis flow + render-job submit.
