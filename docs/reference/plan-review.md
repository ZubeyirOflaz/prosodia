# Reviewing a plan

A plan sits upstream of every episode in a series, so one bad decision in it is multiplied
by the episode count. The writer has an editor; the plan had nothing. This is how a plan
gets reviewed, and why it is split the way it is.

## The split, and the evidence for it

Reviewing the first `ai_act` plan by hand produced two very different kinds of finding.

**Things settled by counting.** 77 of 110 articles covered only inside ranges. 22 of 63
citations resolving to nothing in the docket. 7 of 22 quotations not verbatim. 17 proper
nouns absent from the docket. A planned runtime 11% over target. Every one of these came
from a script, and **no LLM reviewer can do any of them reliably** — it cannot hold 110
article numbers, and it will tell you with confidence that a quotation is verbatim.

**Things settled by judgement.** That Ep 7 teaches twenty-five provisions from a case that
reaches one. That Ep 9's opening instance is entirely GDPR, a statute the series has
reserved. That the "levels" beat had become a five-slot recitation delivered eight times.
These came from reading, and specifically from an **independent** read given an explicit
list of what had already been found.

So: **the counting is automated, the judgement is not.** A planner/reviewer loop would
automate the half that worked least well, cannot do the half that worked best, and would
inherit the failure mode the writer/editor loop already has — an unparseable verdict
defaulting to `ready` with a green trace — on the artifact where it costs the most.

## The automated half: `prosodia plan-lint`

`src/prosodia/author/planlint.py`. Runs at the end of `prosodia plan` (reporting only) and
on demand, where it exits non-zero on errors. No model call; runs in under a second.

| Check | The defect it stands for |
|---|---|
| `cite-not-in-docket` | the planner reconstructing article numbers from memory |
| `quote-not-verbatim` | an inverted or silently elided quotation, spoken as the instrument's own words |
| `bare-range` | "Arts. 74–87" covering provisions nobody read, including ones a later amendment inserted |
| `forward-prereq` | an episode depending on a later episode |
| `applied-coverage` | provisions assigned vs provisions actually worked outside an enumeration |
| `unsayable` | a table, or a run of article numbers, handed to one voice with no picture |
| `verify-budget` | more items to check at write time than the writer's budget of one |
| `outside-docket` | more than three `[OUTSIDE DOCKET: …]` items in an episode |
| `docket-veto` | a figure the docket marks unverified, used anyway |
| `opening-repeat` | two episodes declaring the same opening type |
| `runtime` | summed length against `target_minutes` × episode count |

**An error usually means the docket is short, not the plan.** On the first `ai_act` run,
20 of the 24 errors were closed by extending `research/` with provisions the plan was
right to reach for; the other two were an ellipsis inside quotation marks.

Checks needing a docket skip, with a note, when `research/` is absent, so this runs against
any project.

### Two bugs found in the checks themselves

Both are the errors the module exists to catch, which is worth remembering when extending it.

- Comparing citations against raw docket text reported Article 14 missing while the docket
  said "Arts. 8–21". The linter was **covering by range** — the very thing it flags. Docket
  ranges are now expanded before anything is called missing.
- A `"([^"]+)"` regex pairs from one quotation's *closing* mark to the next one's *opening*
  mark as soon as a short quotation appears, inventing a span out of ordinary prose. Pair
  sequentially by splitting on the quote character instead.

## The human half

Once per series, after the lint is clean. Give the reviewer:

1. **The plan, the synthesis doc, and the planner prompt** — it must judge against the
   method, not against taste.
2. **An explicit exclusion list** of what is already known. Without it, most of the report
   is a rediscovery of the last report.
3. **A question set aimed at teaching, not at structure.** Does each episode build an
   apparatus from one instance and stress-test it, or front-load exposition and attach a
   case as decoration? Is the difficulty curve real — what does each episode assume the
   listener holds, against what earlier episodes actually taught? Are the variants decidable
   from what the episode taught? Would a listener finish able to interrogate a system the
   series never mentioned? Is anything at stake for every five minutes of planned audio?

Ask it to say what is **good**, too. The `ai_act` review's most useful line was that the
"what the rule assumes about the machine" beat was excellent in all eight apparatus
episodes — which is the thing to protect when something has to be cut.

## A hazard while a run is in flight

`Persona.role()` (`persona.py:45`) **re-reads the prompt file on every call**, and
`author_episode` calls it once per writer round and once per editor round. So editing
`writer.md` or `editor.md` while an episode is being written silently changes the contract
between rounds: round 2 is judged against a prompt round 1 never saw. Nothing in the run
trace records which text was used, so the change leaves no evidence.

Do not touch a persona's role prompts while a `write` is running. Python files are safe —
the running process has already imported them — and so is the research docket, which is
read once when the brief is assembled.

Worth fixing properly: archive each role prompt into the run alongside `brief.md`, so a
draft can be read against the instructions that actually produced it.

## What only a person can decide

Whether the series is standalone enough; whether the verdict is right; whether a case is
worth its minutes. Neither half of this touches those.

## Standing ledger — Series A ("The Instrument")

Fixed: the coverage map's bare ranges and the chapter mislabel that had swallowed Chapter X;
`placing on the market` now taught in Ep 1; Ep 1's held-verdict promise; Ep 12's contradictory
close; Ep 5's variants; Ep 11's penalty table; the Annex X, Arts. 97–98, Art. 6(3) and Art. 43
citation defects; Ep 11's enforcement beat rebuilt on Arts. 75a–75d.

Open, and each needs material rather than editing:

- **Ep 7 needs a second instance** — a documented deployment where a data-governance or
  record-keeping duty is the hinge, decidable under Arts. 10 and 12. The docket records this
  as a known hole.
- **Ep 9 needs a GPAI instance**, or must be rebuilt on the Art. 51(2) compute threshold with
  the Garante case demoted to ninety seconds of pre-history.
- **Eps 2 and 10** (lens) have no docket behind them: every position needs a named holder and
  a locatable place they said it.
- **Recitals** are absent from the docket — a consolidated text omits the preamble, and the
  "why this rule and not another" beat leans on them.
- The **levels beat** is identical in all eight apparatus episodes, and five of the eight do
  no work with the list afterwards.

## See also

[craft-sourcing.md](craft-sourcing.md) · [casework-synthesis.md](casework-synthesis.md) ·
[casework-series-roadmap.md](casework-series-roadmap.md) ·
[CLI reference](../cli-reference.md#prosodia-plan-lint)
