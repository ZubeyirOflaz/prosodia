# Open expressive-TTS landscape (2025–2026) — alternatives behind the pluggable backend

Research synthesis for the two standing audio problems, evaluated for a **local RTX 3080
(10 GB, Windows 11)** and Prosodia's **MIT / license-clear** rule. Chatterbox stays the
default; this is the shortlist if the prompt/table fixes + reference-clip work don't close
the gap.

## The single most important finding

**Almost no open model has a real pause-duration primitive or a numeric pitch/register
knob.** The field controls prosody three ways only: a **reference clip** (delivery transfer),
an **emotion vector**, or a **natural-language style prompt**. Chatterbox's two structural
gaps — no `<break>`, no register control — are shared by nearly the whole field. Two
late-2025/2026 releases are the exceptions and are the headline picks.

**Architectural corollary:** since almost nothing honors pause tags, **dramatic pauses are
compiled as inserted real silence in the renderer** (from `{pause: N}`) for every backend
*except* MOSS-TTS. Our renderer already does this — it's a strength, not a workaround.

## Comparison (condensed)

Legend: ✓ strong · ~ partial/indirect · ✗ none. "Style transfer" = transfers *delivery*,
not just timbre.

| Engine | Style xfer | Register/pitch | Timed pause | Fits 10 GB | License (commercial) | Long-form |
|---|---|---|---|---|---|---|
| **Chatterbox** (baseline) | ~ (`exaggeration` scalar) | ✗ | ✗ | ✓ | **MIT ✓** | good, ~40 s chunks |
| **MOSS-TTS** v1.5/Local | ~ (voice-design prompt) | ~ (qualitative) | **✓ `[pause X.Ys]`** | ✓ (1.7B/4B) | **Apache-2.0 ✓** | built for long-form |
| **IndexTTS2** | **✓ (emo-ref + 8-float vec + NL emotion)** | ~ (deep only via timbre ref) | ~ (inter-sentence only) | ✓ ~5.9 GB **FP16 only** | custom *bilibili* (not OSI) | auto-chunk, stable ID |
| **GPT-SoVITS** | ✓ (reference-driven) | ~ (via ref; real `speed_factor`) | ✗ | ✓ ~6–8 GB | **MIT code** (audit weights) | good; chunk+concat |
| **StyleTTS2** | ✓ (`alpha`/`beta` split) | ~ (`embedding_scale`) | ✗ | ✓ ~2 GB | **MIT** (weights: disclose clause) | human-level clarity; no long mode |
| **Step-Audio-EditX** | ✓ | **✓ tags: `deeply`,`authority`,`serious`** | ✗ | ⚠ wants 12–16 GB | **Apache-2.0 ✓** | <30 s/inf → heavy chunking |
| **Higgs Audio v2** | ✓ (auto adapt) | ~ (via ref) | ✗ | ⚠ cloning 18–20 GB (offload) | **Apache-2.0 ✓** | purpose-built long-form |
| **Parler-TTS** | ✗ (NL description) | **~ promptable "low-pitched"** | ✗ | ✓ ~5 GB | **Apache-2.0 ✓** | chunk per sentence |
| **XTTS-v2** / **F5-TTS** | ~ clone | ✗ | ✗ | ✓ | **non-commercial ✗** | drift/hallucination on long text |
| FastPitch / Mellotron | ✓ (GST) | **✓ (explicit F0 shift/contour)** | ~ (per-phoneme dur) | ✓ tiny | Apache/BSD/MIT ✓ | Tacotron-era, below SOTA |

Ruled out on license (conflict with MIT/commercial-clear): XTTS-v2, F5-TTS weights,
Fish/OpenAudio S1, Spark-TTS, Llasa, Higgs v3. Weak on control: Kokoro (fine no-GPU
fallback), Orpheus emotion tags, CosyVoice (no pitch/pause).

## Top picks to trial (alongside Chatterbox)

### 1. MOSS-TTS — for problem (ii), dramatic pauses
The **only open model with an authorable, timed pause** (`…名字是[pause 3.2s]静夜思！`,
verified on the official repo) plus token-count duration control. A near-exact match for a
`{pause: N}` transcript directive — controllable beats *from the model* instead of stitched
silence. **Apache-2.0**, 1.7B/4B fit 10 GB, built for long-form. Caveat: register control is
only qualitative; "beats all open models" is a vendor claim — verify by ear.
Repo: `github.com/OpenMOSS/MOSS-TTS`.

### 2. IndexTTS2 — for problem (i), expressive / not-flat + cross-episode consistency
**Strongest expressiveness controls in the field**, mapping cleanly to a two-layer
"intent → params" design: a **separate emotion reference** (disentangled from timbre), an
**8-float emotion vector** `[happy, angry, sad, afraid, disgusted, melancholic, surprised,
calm]`, *and* a **natural-language emotion prompt**. Auto-chunking re-anchors timbre per
chunk → **stable narrator identity across episodes** (serves the multi-episode goal).
~5.9 GB, **must run FP16** (`--cuda_kernel --fp16`; FP32 is unusably slow). **Caveats:**
license is a custom *bilibili Model Use License* (royalty-free < 100 M MAU but **not
OSI/MIT** — flag before adopting); deeper register still needs a deep timbre reference (no
pitch knob); paper's precise duration control is disabled in the public release.
Repo: `github.com/index-tts/index-tts`.

### 3. GPT-SoVITS — cleanest MIT drop-in (honorable mention)
The closest "like Chatterbox but reference-driven, MIT code" option: verified
reference-*style* transfer (swap a deep/whispered/angry reference and delivery follows;
pitch-shifting the reference yields a faithfully deeper read → a practical **register**
lever), a real `speed_factor`, fits ~6–8 GB. Its weaknesses (no native pause, long-form
drift) are exactly what our renderer already absorbs. Audit bundled weights (HuBERT,
BigVGAN) per-component before shipping. Repo: `github.com/RVC-Boss/GPT-SoVITS`.

## How the field maps to our two problems

- **(i) Lower register / not-flat:** explicit numeric pitch only in the old family
  (FastPitch F0-shift, Mellotron F0 contour). Tag-based register in Step-Audio-EditX
  (`deeply`/`authority`). Best expressive-but-implicit (deep = deep reference clip):
  IndexTTS2, GPT-SoVITS, StyleTTS2, Higgs v2. Only Parler-TTS makes "low-pitched" directly
  *promptable* (imperfect obedience).
- **(ii) Dramatic pauses:** native timed pause only in **MOSS-TTS**; per-phoneme duration in
  FastSpeech2; everything else → **insert silence in the renderer** (what we do).

## Caveats on the evidence
- **No primary-source RTX-3080 speed numbers** exist for any model — all RTF extrapolated.
- **No independent blind long-form benchmarks** — vendor MOS + community anecdote only.
- Confidence highest on **licenses + control mechanisms** (from GitHub LICENSE files, model
  cards, source), lowest on **quantified long-form stability + peak VRAM**.
- Objective pre-commit check available: **EmergentTTS-Eval** (scores emotion/emphasis/pause).

## Recommendation
Keep **Chatterbox (MIT)** as the default. Do the cheap fixes first (done: tone-table
retune + digest-pause rule; next: reference-clip engineering — a lower/expressive clip).
**Only if those don't close the gap**, A/B one representative episode across
**Chatterbox + GPT-SoVITS (register) + MOSS-TTS (pauses)** on pause-heavy and
register-shifting passages, scored with the delivery-profile harness
(`prosody-profiling.md`). **LoRA fine-tuning is deferred** (highest commitment; needs a
rented ≥16 GB GPU to train, then serve on the 3080) — revisit only if a reference clip +
an alternative engine still can't hit the register target.
