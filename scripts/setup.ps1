#requires -Version 5.1
<#
.SYNOPSIS
  One-time setup for the Prosodia renderer on Windows 11 + NVIDIA GPU (e.g. RTX 3080).
.DESCRIPTION
  Installs ffmpeg, creates a Python 3.11 venv, installs a CUDA PyTorch wheel FIRST
  (so chatterbox-tts does not pull a CPU/wrong build - repair B1), then installs
  prosodia[render], and finally runs `prosodia-render doctor`.
  Verify the CUDA tag (cu126/cu128) against your driver at pytorch.org/get-started.
#>
[CmdletBinding()]
param(
  [string]$CudaIndex = "https://download.pytorch.org/whl/cu126",
  [string]$VenvDir = ".venv-render"
)
$ErrorActionPreference = "Stop"
$repo = Split-Path $PSScriptRoot -Parent
Write-Host "== Prosodia renderer setup (repo: $repo) ==" -ForegroundColor Cyan

# 1. ffmpeg - a system dependency, not a pip package (repair B1)
if (-not (Get-Command ffmpeg -ErrorAction SilentlyContinue)) {
  Write-Host "Installing ffmpeg via winget ..."
  winget install -e --id Gyan.FFmpeg --accept-source-agreements --accept-package-agreements
  Write-Host "If ffmpeg is still not found, open a NEW shell (PATH refresh) and re-run." -ForegroundColor Yellow
}

# 2. venv on Python 3.11/3.12 - torch/Chatterbox wheels lag newer Pythons (repair B2)
function Test-PyVersion($ver) {
  try { $null = & py "-$ver" --version 2>&1; return ($LASTEXITCODE -eq 0) } catch { return $false }
}
$pyVer = $null
foreach ($v in @("3.11", "3.12")) { if (Test-PyVersion $v) { $pyVer = $v; break } }
if (-not $pyVer) {
  Write-Host "No suitable Python found. The renderer needs Python 3.11 or 3.12" -ForegroundColor Red
  Write-Host "(torch/Chatterbox wheels lag newer versions; 3.13+ is not supported)." -ForegroundColor Red
  Write-Host "Install it, then re-run this script:" -ForegroundColor Yellow
  Write-Host "  winget install -e --id Python.Python.3.11" -ForegroundColor Yellow
  throw "Python 3.11/3.12 not found by the 'py' launcher (see 'py --list')."
}
$venvPath = Join-Path $repo $VenvDir
Write-Host "Creating venv at $venvPath on Python $pyVer ..."
& py "-$pyVer" -m venv $venvPath
$py = Join-Path $venvPath "Scripts\python.exe"
& $py -m pip install --quiet --upgrade pip

# 3. CUDA PyTorch FIRST, before the render extra (repair B1)
Write-Host "Installing CUDA PyTorch from $CudaIndex ..."
& $py -m pip install torch torchaudio --index-url $CudaIndex

# 4. prosodia + the render extra (chatterbox-tts, faster-whisper, soundfile)
Write-Host "Installing prosodia[render] ..."
& $py -m pip install -e "$repo[render]"

# 4b. Guard: the [render] extra can pull a CPU torch over the CUDA wheel (repair B1).
$cudaTag = ""
try { $cudaTag = (& $py -c "import torch,sys; sys.stdout.write(str(torch.version.cuda))") } catch { $cudaTag = "" }
if ([string]::IsNullOrWhiteSpace($cudaTag) -or $cudaTag -eq "None") {
  Write-Host "torch has no CUDA (a CPU build slipped in) - reinstalling the CUDA wheel ..." -ForegroundColor Yellow
  & $py -m pip install --force-reinstall torch torchaudio --index-url $CudaIndex
}

# 5. sanity check the environment
Write-Host "Running doctor ..."
& (Join-Path $venvPath "Scripts\prosodia-render.exe") doctor

Write-Host "Done. Launch the watcher with:" -ForegroundColor Green
Write-Host "  scripts\start_renderer.ps1 -Root <synced_exchange_root>" -ForegroundColor Green
