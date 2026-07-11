# Pipeline & traces

[← Docs index](README.md)

Authoring is a role-separated, traced, looping process. Each role is a headless
Claude Code call (`claude -p`, on your subscription); each stage writes a
versioned artifact and a trace line, so when you dislike something in the output
you can find — and fix — the stage that caused it.

## The pipeline

```
                          series.yaml
                              │
                          [Planner] ── outline + coverage map
                              │ (per-episode brief: scope, tension)
                              ▼
          ┌────────────▶ [Writer] ── transcript draft (+ first-layer intent)
          │                   │
   editorial notes            ▼
          │              [Editor] ── {ready, notes}?
          └──── no ───────────┤
                          yes  ▼
                       [Tone specialist] ── render_plan.json (engine params)
                              │
                              ▼
                     compile → submit → job
```

## Roles

- **Planner** — from the series goal, produces the outline and a **coverage map**
  that assigns every topic to exactly one episode (no gaps/overlap, goal #4), with
  per-episode scope, handover/recap, and tension. (`author/roles/planner.md`)
- **Writer** — writes the **verbatim** transcript for one episode in the house
  style + first-layer engine-neutral delivery intent. (`author/roles/writer.md`)
- **Editor** — judges the draft against the brief and house style and returns a
  structured `{ready, notes}` verdict; if not ready, the notes go back to the
  Writer. (`author/roles/editor.md`)
- **Tone specialist** — compiles the engine-neutral intent into engine params. In
  v0.1 this is the deterministic [tone table](configuration.md#tone-table);
  an LLM-driven version is an optional later upgrade.

Implementation: `author/orchestrate.py` (the loop is unit-tested with an injectable
runner, so no quota is needed to test it). See [Architecture](architecture.md).

## Checkpoints

Human approval is configurable. While calibrating, the natural gates are: approve
the **plan**, then approve each **transcript** before rendering. Because authoring
and rendering are decoupled, you can also just review the final audio and fix
afterward via the traces.

## Traces

Every stage writes into the episode's `run/` folder — the single provenance store
that both you and the agent read:

- `events.jsonl` / `run.json` — an id-linked, status-bearing event per stage
  (`ok`/`warn`/`error`), with content-hashed inputs/outputs so each stage links to
  the next, and warnings (a tone fallback, a malformed directive) recorded as
  first-class signals.
- `stages/` — the persisted artifacts, including **every Writer/Editor round**
  (`write.rN/transcript.vN.md`, `edit.rN/verdict.json`) — no silent overwrite, so
  the diff between rounds is inspectable.
- `lineage.json` — each final segment mapped back to its beat, intent, resolved
  tone params, and any tone fallback.

`prosodia trace-report <episode>` renders all of this into a self-contained
`trace.html` (pipeline timeline, per-stage detail, segment lineage table) you open
in a browser.

## Diagnosis

`prosodia diagnose <episode> "<complaint>" [--beat N]` turns a plain-words problem
into a ranked list of probable sources across the whole process — each with its
evidence and a concrete fix — written to an HTML report in `run/diagnoses/`. A
deterministic signal pass reads the trace and ranks candidates; unless
`--no-agent`, a Claude agent (`roles/diagnostician.md`) then re-ranks and enriches
them. Example: "the opening feels flat" on an episode whose first beat asked for an
unmapped tone → **tone stage, 85%** → "add the tone to `voice_profiles.yaml`."

## Troubleshooting

`prosodia diagnose` automates the routing below; this table is the manual reference
for which stage owns which kind of problem:

| You notice… | Stage at fault | Where / fix |
|---|---|---|
| an episode repeats or skips a topic | **Planner** | `series.yaml` coverage map → re-plan boundaries |
| a passage is flat / wrong stress *in the writing* | **Writer / Editor** | re-run `write` with notes |
| right words, wrong tone or pace | **Tone intent** or the table | adjust the beat's `{tone}` / edit [`voice_profiles.yaml`](configuration.md#tone-table) |
| a name is mispronounced / digits read wrong | **compile** (normalize/lexicon) | add a [`lexicon.yaml`](configuration.md#pronunciation-lexicon) entry |
| a stutter / garbled word in the audio | **renderer** | re-render `--final` (STT gate) |

This same routing underlies the [A/B evaluation](evaluation.md).

## See also

[Architecture](architecture.md) · [Authoring guide](authoring-guide.md) ·
[Configuration](configuration.md) · [Evaluation & testing](evaluation.md)
