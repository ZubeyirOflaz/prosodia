# Authoring guide

[← Docs index](README.md)

Authoring produces a **transcript** — the source of truth, spoken verbatim — and
packages it as a render job. You can author two ways:

- **Orchestrated**: let the headless Claude Code loop draft and edit it.
- **By hand**: write the transcript yourself (or edit an orchestrated draft).

Either way the transcript is the same [hybrid format](../formats/SPEC.md), and the
same `compile` → `submit` steps follow.

## Orchestrated authoring

Requires the `claude` CLI (it runs on your Claude subscription — no API key). The
[pipeline](pipeline-and-traces.md) is Planner → Writer ⇄ Editor → Tone specialist.

```bash
prosodia plan  --project projects/eu_history              # writes plan/outline.md
prosodia write --project projects/eu_history --episode 1  # writes episodes/ep1/transcript.md
```

`plan` builds the outline from any verified source material you place in
`projects/<proj>/research/*.md` (the [docket](configuration.md#research-docket)),
web-searching only to fill flagged gaps; a series-level `scope:` plans a subset now.

`write` runs the Writer ⇄ Editor loop until the Editor judges the draft ready (up
to `--max-rounds`, default 3). Every stage appends to `episodes/<slug>/trace.jsonl`
so you can see what happened and [route feedback to the right stage](pipeline-and-traces.md#troubleshooting).

## Writing by hand — format cheatsheet

The [transcript format spec](../formats/SPEC.md) is canonical; the essentials:

```markdown
---
voice: narrator                 # optional — omit to inherit the project default
episode: 1
title: "The Suicide of a Continent"
defaults: { tone: measured, rate: normal }
---

<!-- comments are never spoken -->

## Beat title {tone: somber, rate: slow}
Spoken verbatim. A blank line is a paragraph (a short pause).
A deliberate beat: {pause: 1.0}  Emphasis with *asterisks*.
A mid-beat shift: {tone: tense} now it is tense.

## Next beat {tone: grave}
...
```

- **Beat** = `## title {directives}` — the title is a chapter marker (not spoken)
  and the unit of delivery. One beat → one IR segment.
- **Directives** `{tone, rate, note}` set engine-neutral intent; `{pause: N}`
  inserts `N` seconds of real silence. **Mark only what the prose can't imply.**
- **Tone words**: `measured, neutral, warm, somber, grave, wistful, reverent,
  tense, urgent, dramatic, wry, matter-of-fact` (the [tone table](configuration.md#tone-table)
  is the source of truth; unknown tones warn and fall back).
- **Emphasis** `*word*` (use `\*` / `\{` for literals). **Two-host**: `@speaker`
  tags with a `speakers:` map in front-matter.

## House style

The target is immersive, single-narrator *Hardcore History*-style narration:
vivid scenes, real stakes, human focus, rhetorical questions, slow down on
pivotal moments, end on a hook. The active persona's Writer role prompt encodes this
(`src/prosodia/author/personas/<persona>/roles/writer.md`); the existing EU episode
is a worked example.

## Numbers, dates, and pronunciation

Write naturally — `1945`, `1914–1945`, `§45a`, `Maastricht`. Conversion to spoken
form happens at **compile time**: [normalization](configuration.md#lexicon--normalization)
spells out numbers/years; a per-project [lexicon](configuration.md#pronunciation-lexicon)
respells proper nouns. The IR keeps both the authored and spoken text.

## Compile and submit

```bash
prosodia compile projects/eu_history/episodes/ep1/transcript.md \
  --config projects/eu_history/series.yaml --lexicon projects/eu_history/lexicon.yaml
prosodia submit projects/eu_history/episodes/ep1 --root <synced_folder> --job-id eu-ep1
```

`compile` is deterministic and offline. Full flags: [CLI reference](cli-reference.md).

## See also

[Transcript format](../formats/SPEC.md) · [Configuration](configuration.md) ·
[Pipeline & traces](pipeline-and-traces.md) · [CLI reference](cli-reference.md)
