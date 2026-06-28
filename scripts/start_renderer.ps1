#requires -Version 5.1
<#
.SYNOPSIS
  Launch the Prosodia renderer watcher, or register it as a logon Scheduled Task.
.DESCRIPTION
  Runs `prosodia-render watch <Root>`. With -Install, registers a Scheduled Task
  that runs AT LOGON in the interactive user session - which sidesteps the
  Session-0 / WDDM GPU-access problem on a consumer GPU (repair B2). Run setup.ps1
  first.
.EXAMPLE
  scripts\start_renderer.ps1 -Root D:\Sync\prosodia
.EXAMPLE
  scripts\start_renderer.ps1 -Root D:\Sync\prosodia -Final -Voices .\voices -Install
#>
[CmdletBinding()]
param(
  [Parameter(Mandatory = $true)][string]$Root,   # synced exchange root (holds inbox/)
  [string]$VenvDir = ".venv-render",
  [string]$Voices = "",
  [switch]$Final,                                 # final mode (candidates + STT gate)
  [switch]$Install                                # register a logon Scheduled Task instead of running now
)
$ErrorActionPreference = "Stop"
$repo = Split-Path $PSScriptRoot -Parent
$render = Join-Path $repo "$VenvDir\Scripts\prosodia-render.exe"
if (-not (Test-Path $render)) { throw "Renderer not found at $render - run scripts\setup.ps1 first." }

$watchArgs = @("watch", $Root)
if ($Final) { $watchArgs += "--final" }
if ($Voices) { $watchArgs += @("--voices", $Voices) }

if ($Install) {
  $action = New-ScheduledTaskAction -Execute $render -Argument ($watchArgs -join " ")
  $trigger = New-ScheduledTaskTrigger -AtLogOn
  $settings = New-ScheduledTaskSettingsSet -RestartCount 3 -RestartInterval (New-TimeSpan -Minutes 1) -ExecutionTimeLimit ([TimeSpan]::Zero)
  Register-ScheduledTask -TaskName "ProsodiaRenderer" -Action $action -Trigger $trigger -Settings $settings -RunLevel Limited -Force | Out-Null
  Write-Host "Registered Scheduled Task 'ProsodiaRenderer' (runs at logon in your session)." -ForegroundColor Green
} else {
  Write-Host "Starting renderer watch on $Root ..." -ForegroundColor Cyan
  & $render @watchArgs
}
