#!/usr/bin/env bash
# Launch the Prosodia renderer watcher, or install it as a systemd --user service.
#
# The Windows counterpart is start_renderer.ps1 (which uses a logon Scheduled
# Task for the same reason this uses a --user unit: the renderer wants a real
# user session, not a system service). Run scripts/setup.sh first.
#
# Usage:
#   scripts/start_renderer.sh --root /home/you/Sync/prosodia
#   scripts/start_renderer.sh --root /home/you/Sync/prosodia --final --voices ./voices
#   scripts/start_renderer.sh --root /home/you/Sync/prosodia --device cpu --install
set -euo pipefail

ROOT=""
VENV_DIR=".venv-render"
VOICES=""
DEVICE=""
FINAL=0
INSTALL=0
repo="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --root)    ROOT="$2"; shift 2 ;;
    --venv)    VENV_DIR="$2"; shift 2 ;;
    --voices)  VOICES="$2"; shift 2 ;;
    --device)  DEVICE="$2"; shift 2 ;;
    --final)   FINAL=1; shift ;;
    --install) INSTALL=1; shift ;;
    -h|--help) sed -n '2,15p' "${BASH_SOURCE[0]}"; exit 0 ;;
    *) echo "unknown argument: $1" >&2; exit 2 ;;
  esac
done

if [[ -z "$ROOT" ]]; then echo "--root <synced_exchange_root> is required" >&2; exit 2; fi
ROOT="$(cd "$ROOT" && pwd)"   # absolute: a systemd unit has no useful cwd

render="$repo/$VENV_DIR/bin/prosodia-render"
if [[ ! -x "$render" ]]; then
  echo "Renderer not found at $render - run scripts/setup.sh first." >&2
  exit 1
fi

args=(watch "$ROOT")
(( FINAL )) && args+=(--final)
[[ -n "$VOICES" ]] && args+=(--voices "$VOICES")
[[ -n "$DEVICE" ]] && args+=(--device "$DEVICE")

if (( INSTALL )); then
  unit_dir="${XDG_CONFIG_HOME:-$HOME/.config}/systemd/user"
  mkdir -p "$unit_dir"
  # Quote each argument for the unit's ExecStart line.
  quoted=""
  for a in "${args[@]}"; do quoted+=" \"$a\""; done
  cat > "$unit_dir/prosodia-renderer.service" <<UNIT
[Unit]
Description=Prosodia renderer watcher
After=default.target

[Service]
Type=simple
ExecStart=$render$quoted
WorkingDirectory=$repo
Restart=on-failure
RestartSec=60
# No timeout: an episode render legitimately takes hours.
TimeoutStopSec=30

[Install]
WantedBy=default.target
UNIT
  systemctl --user daemon-reload
  systemctl --user enable --now prosodia-renderer.service
  printf '\033[32m%s\033[0m\n' "Installed and started the 'prosodia-renderer' user service."
  echo "  status:  systemctl --user status prosodia-renderer"
  echo "  logs:    journalctl --user -u prosodia-renderer -f"
  echo "  stop:    systemctl --user disable --now prosodia-renderer"
  # Without this the unit dies at logout; it is what makes the service survive
  # the way the Windows logon task does.
  if ! loginctl show-user "$USER" -p Linger 2>/dev/null | grep -q 'Linger=yes'; then
    printf '\033[33m%s\033[0m\n' "To keep it running when you are logged out, enable lingering:"
    echo "  sudo loginctl enable-linger $USER"
  fi
else
  printf '\033[36m%s\033[0m\n' "Starting renderer watch on $ROOT ..."
  exec "$render" "${args[@]}"
fi
