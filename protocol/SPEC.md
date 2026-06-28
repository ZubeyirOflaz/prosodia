# Prosodia Job Protocol — SPEC v0.1

The authoring and rendering sides exchange work through a cloud-synced folder (the
**exchange root**). This document is the contract; it is implemented in
`prosodia.core.protocol`.

## Folders (under the exchange root)

| Folder | Purpose | Writer |
|---|---|---|
| `inbox/` | jobs ready to render | author |
| `processing/` | a claimed job, mid-render | renderer |
| `outbox/` | finished jobs (audio + status) | renderer |
| `failed/` | jobs that errored (see status.json) | renderer |
| `building/` | author's local staging (pre-publish) | author |

**Single-writer zones** (so sync conflicts can't arise): the author writes only
`inbox/` (and its own `building/`); the renderer writes only `processing/`,
`outbox/`, `failed/`.

## A job

A directory named by job id, holding immutable inputs:

- `ir.json` — the compiled IR (`prosodia.core.ir.EpisodeIR`)
- `render_plan.json` — derived engine params (`prosodia.core.ir.RenderPlan`)
- `<voice>.wav` — optional bundled voice reference
- `manifest.json` — sha256 + size of every payload file above (excludes itself and status.json)

The renderer adds after claiming: `status.json` (mutable control state) and, in
`outbox/`, `episode.wav`.

## Atomic claim — the core safety property

A cloud-synced folder can present a half-synced job. The guard (repair A2/B1):

1. The author writes all payload files into `building/<job_id>/`, computes
   `manifest.json` **last**, then renames the folder into `inbox/<job_id>/`
   (same-filesystem atomic rename). The manifest's presence is the trigger; its
   **content (hashes) is the actual gate**.
2. The renderer claims a job only when `validate_job()` returns no problems —
   every file in the manifest exists and its size + sha256 match. A job that does
   not yet validate is skipped and retried (still syncing). This is immune to
   per-file sync reordering, partial sync, and interrupted transfers.
3. On claim, the renderer atomically moves `inbox/<job_id>` → `processing/<job_id>`.

## status.json

`{job_id, state, message, progress}` where `state` is
`queued` (optional) → `rendering` → `done` | `failed`. `message` holds the audio
filename (done) or the error (failed); `progress` is 0..1.

## Sync-layer notes

- **Syncthing** (recommended): LAN-direct, private. Its temp files
  (`~syncthing~*.tmp` on Windows) are auto-ignored. You may drive the trigger off
  its REST event stream (`ItemFinished`) instead of polling — but keep the
  manifest check as the gate regardless.
- **Dropbox / Google Drive**: also work. Neither exposes a reliable local
  "fully synced" signal, so the manifest+hash check is what makes the design
  portable.
- Watch for `*.sync-conflict-*` files — with single-writer zones they should never
  appear; treat any as an operational alert.
