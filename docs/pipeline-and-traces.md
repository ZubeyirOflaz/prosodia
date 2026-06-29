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

Each stage appends one JSON line to the episode's `trace.jsonl` (and writes its
artifact). The trace records the sequence (plan → write → edit → …) so a complaint
about the output can be reconstructed end-to-end.

## Troubleshooting

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
