# A/B naturalness test — Prosodia vs NotebookLM

Goal: decide whether controlled, single-narrator Chatterbox beats NotebookLM on
the four problems Prosodia targets. First corpus: **EU history ep1–3**.

For each episode, listen to both and score 1–5 (5 = better) on:

| Dimension (→ goal) | NotebookLM | Prosodia | Notes / timestamps |
|---|---|---|---|
| Emphasis on the right ideas (#1, #3) | | | |
| Pause placement at critical moments (#3) | | | |
| Narrative coherence / no jarring breaks (#1) | | | |
| Absence of synthetic flow / near-interruptions (#2, #3) | | | |
| Coverage: nothing skipped or repeated (#4) | | | |
| Overall immersion (Hardcore-History feel) | | | |

Note specific timestamps where Prosodia is worse, then route each issue to the
stage that caused it using the episode trace
(`projects/eu_history/episodes/<ep>/trace.jsonl`):

| You hear… | Stage | Fix |
|---|---|---|
| wrong topic / repeats across episodes | Planner | re-plan boundaries in `series.yaml` |
| flat or wrong delivery *in the writing* | Writer/Editor | re-run the editorial loop with notes |
| right words, wrong tone/pace | Tone intent / `voice_profiles.yaml` | adjust the beat's intent or the mapping |
| mispronounced name / digits read wrong | lexicon / normalize | add a `lexicon.yaml` entry / rule |
| stutter, repeated/garbled word in audio | renderer | re-render in `--final` (STT gate) |
