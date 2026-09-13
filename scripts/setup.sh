#!/usr/bin/env bash
# One-time setup for the Prosodia renderer on Linux/macOS.
#
# The Windows counterpart is setup.ps1. Same shape, same ordering rule: install
# the right PyTorch wheel FIRST, so `chatterbox-tts` cannot drag a different
# build in over the top of it (repair B1).
#
# Unlike setup.ps1 this does not assume NVIDIA. It picks a torch flavour from
# what it actually finds:
#     nvidia-smi present            -> CUDA wheel
#     AMD GPU present (no NVIDIA)   -> ROCm wheel, but see the warning below
#     neither                       -> CPU wheel (the small, lean install)
#
# ROCm warning: on an *integrated* AMD GPU (Ryzen AI / APU), CPU rendering
# measured ~3x FASTER than the iGPU on this project, because Chatterbox's
# autoregressive stage is bound by memory bandwidth the iGPU already shares with
# the CPU. Pass --flavor cpu on an APU unless you have measured otherwise.
#
# Usage:
#   scripts/setup.sh                          # auto-detect
#   scripts/setup.sh --flavor cpu             # force the lean CPU install
#   scripts/setup.sh --flavor cu128           # force a CUDA tag
#   scripts/setup.sh --flavor rocm6.4
#   scripts/setup.sh --venv .venv-render --python 3.12
set -euo pipefail

FLAVOR=""
VENV_DIR=".venv-render"
PYTHON_REQ=""
repo="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --flavor) FLAVOR="$2"; shift 2 ;;
    --venv)   VENV_DIR="$2"; shift 2 ;;
    --python) PYTHON_REQ="$2"; shift 2 ;;
    -h|--help) sed -n '2,30p' "${BASH_SOURCE[0]}"; exit 0 ;;
    *) echo "unknown argument: $1" >&2; exit 2 ;;
  esac
done

cyan() { printf '\033[36m%s\033[0m\n' "$*"; }
green() { printf '\033[32m%s\033[0m\n' "$*"; }
yellow() { printf '\033[33m%s\033[0m\n' "$*"; }
red() { printf '\033[31m%s\033[0m\n' "$*"; }

cyan "== Prosodia renderer setup (repo: $repo) =="

# ── 1. ffmpeg — a system dependency, not a pip package (repair B1) ────────────
if ! command -v ffmpeg >/dev/null 2>&1; then
  red "ffmpeg is not on PATH. Install it, then re-run this script:"
  if command -v dnf >/dev/null 2>&1;      then yellow "  sudo dnf install ffmpeg"
  elif command -v apt >/dev/null 2>&1;    then yellow "  sudo apt install ffmpeg"
  elif command -v pacman >/dev/null 2>&1; then yellow "  sudo pacman -S ffmpeg"
  elif command -v brew >/dev/null 2>&1;   then yellow "  brew install ffmpeg"
  else yellow "  (use your package manager)"; fi
  exit 1
fi

# ── 2. venv on a Python the TTS wheels build for (3.11–3.14) ─────────────────
# chatterbox-tts >= 0.1.7 declares torch >= 2.9 for Python 3.14, so 3.14 is fine
# and is preferred here: on <= 3.13 chatterbox pins torch==2.6.0 exactly, which
# fights any non-default wheel (that is the repair-B1 conflict).
find_python() {
  local want=("$@")
  for v in "${want[@]}"; do
    if command -v "python$v" >/dev/null 2>&1; then echo "python$v"; return 0; fi
  done
  return 1
}
if [[ -n "$PYTHON_REQ" ]]; then
  PY_CMD="$(find_python "$PYTHON_REQ")" || { red "python$PYTHON_REQ not found."; exit 1; }
else
  PY_CMD="$(find_python 3.14 3.13 3.12 3.11)" || true
fi

venv="$repo/$VENV_DIR"
if command -v uv >/dev/null 2>&1; then
  cyan "Creating venv at $venv with uv (${PY_CMD:-3.14}) ..."
  uv venv --python "${PYTHON_REQ:-3.14}" "$venv"
  PIP=(uv pip install)
  export VIRTUAL_ENV="$venv"
else
  if [[ -z "${PY_CMD:-}" ]]; then
    red "No suitable Python found. The renderer needs Python 3.11-3.14."
    yellow "Install one (e.g. 'sudo dnf install python3.12') or install uv, then re-run."
    exit 1
  fi
  cyan "Creating venv at $venv on $PY_CMD ..."
  "$PY_CMD" -m venv "$venv"
  "$venv/bin/python" -m pip install --quiet --upgrade pip
  PIP=("$venv/bin/python" -m pip install)
fi
py="$venv/bin/python"

# ── 3. pick a torch flavour ──────────────────────────────────────────────────
if [[ -z "$FLAVOR" ]]; then
  if command -v nvidia-smi >/dev/null 2>&1 && nvidia-smi -L >/dev/null 2>&1; then
    FLAVOR="cu126"
    cyan "Detected an NVIDIA GPU -> CUDA wheel ($FLAVOR)."
    yellow "Verify the tag against your driver at https://pytorch.org/get-started/locally/"
  elif command -v rocm-smi >/dev/null 2>&1 || [[ -e /dev/kfd ]]; then
    FLAVOR="cpu"
    yellow "Detected an AMD GPU but defaulting to the CPU wheel."
    yellow "On an integrated AMD GPU (Ryzen AI / APU) the CPU is typically FASTER:"
    yellow "Chatterbox's autoregressive stage is memory-bandwidth-bound and the"
    yellow "iGPU shares that bandwidth with the CPU. For a discrete Radeon, re-run"
    yellow "with: scripts/setup.sh --flavor rocm6.4"
  else
    FLAVOR="cpu"
    cyan "No GPU detected -> CPU wheel."
  fi
fi
INDEX="https://download.pytorch.org/whl/$FLAVOR"

# ── 4. torch FIRST, before the render extra (repair B1) ──────────────────────
cyan "Installing PyTorch ($FLAVOR) from $INDEX ..."
"${PIP[@]}" torch torchaudio --index-url "$INDEX"

before="$("$py" -c 'import torch; print(torch.__version__)')"

# ── 5. prosodia + the render extra ───────────────────────────────────────────
cyan "Installing prosodia[render] ..."
# --index-strategy is a uv flag; harmless to omit for plain pip.
if command -v uv >/dev/null 2>&1; then
  "${PIP[@]}" -e "$repo[render]" --index-strategy unsafe-best-match
else
  "${PIP[@]}" -e "$repo[render]"
fi

# ── 5b. Guard: the [render] extra can replace the wheel we just chose ────────
after="$("$py" -c 'import torch; print(torch.__version__)')"
if [[ "$before" != "$after" ]]; then
  yellow "The render extra changed torch ($before -> $after) - restoring the $FLAVOR wheel ..."
  "${PIP[@]}" --reinstall torch torchaudio --index-url "$INDEX" 2>/dev/null \
    || "${PIP[@]}" --force-reinstall torch torchaudio --index-url "$INDEX"
fi

# ── 6. sanity check ──────────────────────────────────────────────────────────
cyan "Running doctor ..."
"$venv/bin/prosodia-render" doctor

green "Done. Launch the watcher with:"
green "  scripts/start_renderer.sh --root <synced_exchange_root>"
