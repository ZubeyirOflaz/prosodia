# Renderer setup

The renderer runs on the render box. The authoring side never needs any of this.

A GPU is **preferred, not required**: with no usable GPU the renderer falls back
to CPU and produces identical output, just slower (see *Performance* below).

## Prerequisite: Python 3.11–3.14

Python **3.14 is now supported and preferred**: `chatterbox-tts` >= 0.1.7
declares `torch>=2.9` for 3.14, whereas on 3.11–3.13 it pins `torch==2.6.0`
*exactly* — which fights any non-default wheel and is the root of the repair-B1
conflict below. Prefer 3.14 unless something else forces an older one.

```powershell
# Windows, if the py launcher has nothing suitable:
winget install -e --id Python.Python.3.14
py --list
```

## One-time setup

**Linux / macOS:**

```bash
# from the repo root, on the render machine:
scripts/setup.sh                   # ffmpeg check + venv + torch + prosodia[render]
scripts/setup.sh --flavor cpu      # force the lean CPU install (~1.9 GB)
scripts/setup.sh --flavor cu128    # force a CUDA tag
```

`setup.sh` picks the torch flavour from what it finds: CUDA if `nvidia-smi`
works, otherwise CPU. It does **not** default to ROCm even when it sees an AMD
GPU — see *AMD GPUs* below.

**Windows:**

```powershell
# from the repo root, on the GPU machine:
scripts\setup.ps1            # ffmpeg + venv + CUDA torch + prosodia[render]
```

Both scripts install, in order (this order matters — repair B1):
1. **ffmpeg** (a system dependency; not a pip package) — `winget install Gyan.FFmpeg` on Windows, your package manager on Linux (`sudo dnf install ffmpeg`).
2. A venv (`.venv-render`) on the newest suitable Python it can find (repair B2).
3. A **CUDA PyTorch** wheel from `--index-url .../whl/cu126` **before** the render extra, so `chatterbox-tts` doesn't pull a CPU build. Verify the CUDA tag (cu126/cu128) for your driver at <https://pytorch.org/get-started/locally/>.
4. `pip install -e .[render]` (chatterbox-tts, faster-whisper, soundfile).

Then it runs the environment check:

```powershell
.venv-render\Scripts\prosodia-render.exe doctor     # Windows
.venv-render/bin/prosodia-render doctor              # Linux/macOS
```

`doctor` must print **"Render environment OK"** before you render. If not, it lists exactly what's missing (Python version, torch, chatterbox, ffmpeg). It then reports which **device** it will use and why, e.g.:

```
Render environment OK (Python, torch, chatterbox, ffmpeg).
  device: cpu (auto)
  GPU unusable: no GPU visible to torch (CPU-only build, or no driver)
  CPU rendering works but is far slower than a discrete GPU - expect roughly 3x realtime ...
```

Force a device with `--device cpu|cuda` on any subcommand, or by exporting
`PROSODIA_DEVICE`.

## Performance: what to expect

Chatterbox splits into an autoregressive token stage (**~62%** of the time) and a
vocoder stage (~37%). The autoregressive stage is **memory-bandwidth-bound**,
which is what makes device choice matter so much.

Measured on an 8-core Ryzen AI 7 350 laptop (no discrete GPU), rendering as
compute-seconds per second of audio:

| Device | Realtime factor | 36-minute episode, fast preview |
| --- | --- | --- |
| CPU (16 threads) | ~3.0–3.4x | ~2 hours |
| Radeon 860M iGPU (ROCm) | ~9.2x | ~5.5 hours |

`--final` mode multiplies generation by `DEFAULT_CANDIDATES` (2). The STT gate
itself is nearly free even on CPU (~0.07x realtime).

So a CPU-only box is a viable *overnight* renderer, not an interactive one.

## AMD GPUs

A ROCm/HIP build of torch reports AMD hardware through the **same
`torch.cuda` API** — there is no `torch.rocm` — so `torch.cuda.is_available()`
is True on an AMD GPU. Two traps follow:

1. **Missing kernels.** A HIP wheel carries kernels only for the gfx targets it
   was built for. On anything else, every kernel launch dies with
   `HIP error: invalid device function` at the first matmul, long after model
   load. `prosodia.render.device` checks `torch.cuda.get_arch_list()` up front
   and falls back to CPU with a readable reason instead. As of ROCm 7.0 the
   wheels ship gfx1150/gfx1151 but **not gfx1152** (Krackan Point / Radeon
   860M); `HSA_OVERRIDE_GFX_VERSION=11.0.0` makes it run anyway.
2. **An integrated GPU is often slower than the CPU.** It shares one memory
   controller with the CPU, so it has no bandwidth advantage on the
   bandwidth-bound autoregressive stage, and few CUs to help on the rest.
   Measured here: the iGPU was **3x slower** than the CPU. Native kernels would
   not change that much — forcing the architecturally-native gfx1151 kernels was
   *slower* than the gfx1100 ones (3.27 vs 3.61 TFLOPS fp16), so kernel
   selection is not the bottleneck; bandwidth and 8 CUs are.

Hence `setup.sh` defaults an AMD box to the CPU wheel. Use
`--flavor rocm6.4` only for a discrete Radeon, and measure both.

### `doctor` says the GPU is unusable (CPU torch slipped in)

This is only a problem on a box that *has* a usable GPU — on a CPU-only machine
it is the expected, working state.

If `doctor` reports no GPU on a machine that has an NVIDIA GPU and
current drivers, the installed torch is almost certainly a **CPU-only build** (the
`[render]` extra reinstalled torch from PyPI over the CUDA wheel — repair B1).
Both setup scripts detect and re-fix this automatically (step 4b/5b); to repair
an existing venv by hand:

```powershell
.venv-render\Scripts\python.exe -c "import torch; print(torch.__version__, torch.version.cuda)"
# +cpu / None == CPU build -> force the CUDA wheel back in:
.venv-render\Scripts\python.exe -m pip install --force-reinstall torch torchaudio --index-url https://download.pytorch.org/whl/cu126
```

If it then reports a CUDA version but is still False, your driver may be too old
for that runtime — try the `.../whl/cu121` index instead.

## Running

Point the renderer at the **synced exchange root** (the folder Syncthing/Dropbox keeps in sync; it will contain `inbox/ processing/ outbox/ failed/`):

**Linux / macOS:**

```bash
# run in the foreground (fast-preview mode by default):
scripts/start_renderer.sh --root ~/Sync/prosodia

# final quality, with a voices folder:
scripts/start_renderer.sh --root ~/Sync/prosodia --final --voices ./voices

# or install a systemd --user service that restarts on failure:
scripts/start_renderer.sh --root ~/Sync/prosodia --install
#   status: systemctl --user status prosodia-renderer
#   logs:   journalctl --user -u prosodia-renderer -f
# to keep it running while logged out: sudo loginctl enable-linger $USER
```

**Windows:**

```powershell
# run in the foreground (fast-preview mode by default):
scripts\start_renderer.ps1 -Root D:\Sync\prosodia

# final quality (N candidates + Whisper validation), with a voices folder:
scripts\start_renderer.ps1 -Root D:\Sync\prosodia -Final -Voices .\voices

# or auto-start at logon (Scheduled Task in your user session — repair B2):
scripts\start_renderer.ps1 -Root D:\Sync\prosodia -Install
```

The watcher claims a job only when its manifest validates (sha256 + size of every
payload file), renders it, and moves it to `outbox/` (or `failed/` with an error
in `status.json`). The model is loaded once and kept warm across jobs.

## Render a single job manually

```powershell
.venv-render\Scripts\prosodia-render.exe render D:\Sync\prosodia\inbox\eu-ep1 --final --voices .\voices
```

## Voices

Put narrator reference clips in a `voices/` folder as `<name>.wav`. A transcript/job
whose `voice` is `narrator` resolves to `voices\narrator.wav`; a job may also bundle its
own clip, which wins.

**Choosing a clip matters — it's a real lever.** Chatterbox clones zero-shot, so the
reference's *style and emotion leak into the output*, and stability/artifacts vary by clip:

- **Match the delivery you want:** a calm, measured, audiobook-style clip for narration —
  not conversational, dramatic, whispery, or fast (a breathy clip can add hissy noise).
- **Meet the spec:** WAV, ≥24 kHz, single speaker, no background music/noise, one
  continuous take, ~10–20 s (≈5 s for Turbo). Cleanliness matters more than length.
- **Instability is partly random per generation**, so judge a clip on its *best of N*
  takes, not one. Once you pick a clip, reuse that *same* clip (and seed) across every
  chunk and episode — the main defense against timbre drift.
- **Accent is Chatterbox's weak spot** and a clip swap won't reliably fix it. If your
  narrator isn't General-American, test the accent early; a known workaround is to
  generate a clean sample in the target accent and then use *that* as the reference.

### Audition candidate voices

By default this renders each clip across the **full delivery range** — a built-in suite of
short passages spanning the tonal registers (measured → warm → wry → tense → urgent →
dramatic → reverent → somber → grave) and cadences (fast enumerations, long flowing
sentences, slow deliberate lines, a posed question). Each passage uses the **real
parameters the pipeline would apply** for its tone and rate, so a clip that sounds perfect
grave-and-slow but falls apart wry-and-fast is caught here, not in a finished episode:

```powershell
.venv-render\Scripts\prosodia-render.exe audition --voices .\voices --out .\voice_audition
# single-passage mode with your own line (optionally a tone/rate to speak it with):
.venv-render\Scripts\prosodia-render.exe audition --voices a.wav b.wav --text "Your test line." --tone grave --rate slow
# audition against a specific persona's tone table (name, or a path to a voice_profiles.yaml):
.venv-render\Scripts\prosodia-render.exe audition --voices .\voices --persona thinkers
```

It writes one `.wav` per passage×clip×take plus an `index.html` (grouped by passage, showing
the resolved parameters) with audio players — open it in a browser to compare. Add `--takes N`
for seed-to-seed variance, or force a single setting across every passage with
`--exaggeration` / `--cfg` / `--temperature`.
