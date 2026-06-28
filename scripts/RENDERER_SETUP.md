# Renderer setup (Windows 11 + NVIDIA GPU)

The renderer runs on the GPU box. The authoring side never needs any of this.

## Prerequisite: Python 3.11 or 3.12

The TTS stack needs **Python 3.11 or 3.12** (torch/Chatterbox wheels lag newer
versions; 3.13+ is not supported). If `setup.ps1` reports *"No suitable Python
found"* / *"no suitable runtime found"*, install it and re-run:

```powershell
winget install -e --id Python.Python.3.11
# open a NEW terminal, then confirm:
py --list          # should list 3.11 (or 3.12)
```

## One-time setup

```powershell
# from the repo root, on the GPU machine:
scripts\setup.ps1            # ffmpeg + Python 3.11 venv + CUDA torch + prosodia[render]
```

`setup.ps1` installs, in order (this order matters — repair B1):
1. **ffmpeg** via `winget install Gyan.FFmpeg` (a system dependency; not a pip package).
2. A **Python 3.11/3.12** venv (`.venv-render`) — it auto-detects whichever the `py` launcher has (repair B2).
3. A **CUDA PyTorch** wheel from `--index-url .../whl/cu126` **before** the render extra, so `chatterbox-tts` doesn't pull a CPU build. Verify the CUDA tag (cu126/cu128) for your driver at <https://pytorch.org/get-started/locally/>.
4. `pip install -e .[render]` (chatterbox-tts, faster-whisper, soundfile).

Then it runs the environment check:

```powershell
.venv-render\Scripts\prosodia-render.exe doctor
```

`doctor` must print **"Render environment OK"** before you render. If not, it lists exactly what's missing (Python version, torch/CUDA, chatterbox, ffmpeg).

### `torch.cuda.is_available()` is False (CPU torch slipped in)

If `doctor` says CUDA is unavailable on a machine that has an NVIDIA GPU and
current drivers, the installed torch is almost certainly a **CPU-only build** (the
`[render]` extra reinstalled torch from PyPI over the CUDA wheel — repair B1).
`setup.ps1` now detects and re-fixes this automatically (step 4b); to repair an
existing venv by hand:

```powershell
.venv-render\Scripts\python.exe -c "import torch; print(torch.__version__, torch.version.cuda)"
# +cpu / None == CPU build -> force the CUDA wheel back in:
.venv-render\Scripts\python.exe -m pip install --force-reinstall torch torchaudio --index-url https://download.pytorch.org/whl/cu126
```

If it then reports a CUDA version but is still False, your driver may be too old
for that runtime — try the `.../whl/cu121` index instead.

## Running

Point the renderer at the **synced exchange root** (the folder Syncthing/Dropbox keeps in sync; it will contain `inbox/ processing/ outbox/ failed/`):

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

Put narrator reference clips in a `voices/` folder as `<name>.wav` (10s+, clean,
single speaker). A transcript/job whose `voice` is `narrator` resolves to
`voices\narrator.wav`. A job may also bundle its own voice clip, which wins.
