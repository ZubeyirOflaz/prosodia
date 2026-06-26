# End-to-end handoff (authoring ↔ renderer)

```
author (any machine)                 synced folder              renderer (GPU box)
  prosodia plan / write          +------------------+        prosodia-render watch
  prosodia compile     ------->  | inbox/  building/|  ----->  claim (manifest ok)
  prosodia submit --root <sync>  | outbox/ failed/  |  <-----  episode.wav + status
                                 +------------------+
```

## Steps

1. Pick an exchange folder, e.g. `D:\Sync\prosodia`, and share it with Syncthing
   between the authoring machine and the GPU box (Dropbox/Drive also work).
2. **Author** (any machine, no GPU):
   ```bash
   prosodia compile projects/eu_history/episodes/ep1/transcript.md \
     --config projects/eu_history/series.yaml --lexicon projects/eu_history/lexicon.yaml
   prosodia submit projects/eu_history/episodes/ep1 --root D:/Sync/prosodia --job-id eu-ep1
   ```
3. **Render** (GPU box): once (`scripts\setup.ps1`), then
   ```powershell
   scripts\start_renderer.ps1 -Root D:\Sync\prosodia
   ```
4. The audio appears in `outbox\eu-ep1\episode.wav` and syncs back.

The renderer claims a job only when its `manifest.json` validates, so a
half-synced job is never grabbed. Full contract: [`protocol/SPEC.md`](../protocol/SPEC.md).

## Synced-folder hygiene (`.stignore`)

A clean setup uses a **dedicated** exchange folder holding only the job lifecycle
(`inbox/ processing/ outbox/ failed/`). If instead you sync the **whole repo**
(convenient, since the render box can then `pip install -e .[render]` from it),
exclude the noise — version control, virtualenvs, caches, model weights, and local
job staging — so they don't sync between machines. The repo ships a `.stignore`
at its root for exactly this. **Never ignore `inbox/ outbox/ processing/ failed/`** —
those are the handoff.

`.stignore` is **per-machine** (Syncthing does not sync it). Two options to apply
it on both sides:

- **Copy** the repo's `.stignore` to the synced-folder root on the render box too, or
- **Auto-sync the list**: keep the patterns in a synced file (e.g. `.stignore.shared`)
  and make each machine's local `.stignore` a single line — `#include .stignore.shared`.
  The shared file then syncs to both sides; only the one-line `.stignore` is set per machine.

Adding `.stignore` is non-destructive: it stops *future* syncing of matched paths
but does not delete files already present. If a virtualenv or `.git` synced over
before you added it, delete that copy on the render box by hand.
