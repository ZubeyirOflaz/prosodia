# Synthesis working document — the `casework` persona

Stage 4 (distil) and stage 6 (synthesise) of [`craft-sourcing.md`](craft-sourcing.md), for the
persona provisionally called **`casework`**. The five dossiers stay untouched and self-contained;
**every comparison between sources lives here and only here.**

---

## 1. The aim, written down

Synthesis rules resolve conflicts "against the persona's aim statement". It did not exist as a
document until now; this is it, and it is the tiebreaker for everything below.

> **`casework` exists to build a durable understanding of how a formal apparatus governs a
> technical reality — and to form a way of looking at any such question, including ones that do
> not exist yet.** The listener should finish an episode able to say what the rule does, what it
> assumes about the machine, where its boundary lies, where it is contested, and what they would
> now ask of a system they have never met.
>
> Passing an examination is a by-product, not a design target. No beat exists to produce recall.
> The subject is technical social science generally; law and the regulation of AI and data is the
> first and hardest instance.

Two consequences that decide real cases below: **comprehension outranks suspense**, and **a stated
understanding outranks an implied one**.

## 2. Roster and job precedence

Each source is authoritative **only** for its hired job. Outside it, the aim decides.

| Source | Job | Corpus strength |
|---|---|---|
| [Hildebrandt](hildebrandt-craft.md) | **the gaze** — what must be asked for an answer to count | 113k words of her own prose; the four-step spine has **two independent witnesses** |
| [Fisher](fisher-craft.md) | **architecture** — series order, episode structure, navigation | ≈17 h verified across 40 segments, plus his own pedagogy paper and exam |
| [Harford](harford-craft.md) | **cases and surface** — the opening, the ending, the sentence | 7 episodes, every claim counted |
| [Sapolsky](sapolsky-craft.md) | **one device** — levels of causation, and dissolving a category | the device appears in **25 of 25** lectures |

[Carlin](carlin-craft.md) is not in this roster: he is the soul of `hardcore-history`, a different
persona.

## 3. Stage 4 — the adversarial pass

54 candidate lines were nominated. The test: *would this be true of any competent teacher in this
field?* If yes, it costs prompt budget and discriminates nothing.

**Cut as generic (2).**
- *Sapolsky 7* — "frame a topic as a puzzle rather than a body to be covered." Advice, not
  technique; every good teacher does it.
- *Sapolsky 3* — "open on a concrete case before naming any framework." True, universal, and
  already stated more specifically by Harford 1. Redundant.

**Cut as already house policy (1).**
- *Fisher 5* — "never invent a controversy." Every Prosodia persona already forbids fabrication;
  spending a line restates an existing rule. The *real-not-hypothetical* distinction survives
  inside Harford 1 and the editor standards.

**Merged (3 → 1 or folded).**
- *Hildebrandt 14* folds into *Hildebrandt 9*: naming the intuitive misreading and earning the
  term in plain language are one move at one moment (first use).
- *Sapolsky 8* ("it depends") folds into an editor standard with Fisher's flat admission of
  indeterminacy — the same honesty, stated once.
- *Harford 6* (counterfactual) was already demoted at its own pass 2 from signature to available
  device; it survives inside Hildebrandt 6 (contestability) and Fisher's both-branches move, and
  does not need a line of its own.

**Reclassified — not prompt lines at all (5).** These are **defaults and tuning targets**, and
belong in `persona.yaml` and `voice_profiles.yaml` where they can be changed without editing a
prompt: Fisher 2 (unit length), Harford 8 (sentence rhythm), Harford 9 ("but" not "however" — a
watchlist entry), plus the speech-rate and address targets in §5.

**Surviving, prompt-eligible: 45**, of which ~33 are genuine writer/planner/editor instructions.
Against a working budget of ~40 lines across all role files, **volume is not the binding
constraint** — coherence is. Several survivors presuppose incompatible episode shapes, which §4
settles.

## 4. The conflicts that are real

### 4.1 The first ninety seconds — resolved, and both sources already agree

| Source | Practice |
|---|---|
| Fisher | Orientation: index, place in the arc, what you should already hold, what today adds (27 of 40 segments) |
| Harford | Cold open on a named person in a placed scene, **no** statement of the topic (6 of 7) |

A direct collision at the same moment — but each source already resolves it internally.
**Harford defers his framing rather than omitting it**: the show identification lands at **7–11%**
in, never at the top. **Fisher's orientation is a lecture-boundary device** (12 of 12 lecture
openers); his interior segments open cold on material instead (13 of 40).

**Resolution: hook, then orient.** Open on the instance with Harford's specificity; make
orientation the second beat, inside the first two or three minutes. Neither source is compromised
and both are followed.

### 4.2 Where the verdict goes — three verdicts, three sites

| Source | Practice |
|---|---|
| Fisher | Withholds his own perspective until the **10th of 12 lectures**, and says he is withholding it |
| Hildebrandt | Marks judgments as hers, inline, wherever they arise |
| Harford | The ending carries the lesson; explicit statement is rare (2 of 7) |

These look contradictory because "verdict" names three different things.

1. **What follows from this rule** — per episode, carried by the ending as a consequence rather
   than a summary (Harford, 0 of 7 summary closes).
2. **A local judgment on a specific test or argument** — marked as the narrator's own, used
   sparingly; Fisher does this in only **6 of 40** segments.
3. **The series' normative question** — is the risk-based frame right? — **held until late and
   announced as held** (Fisher).

No conflict once separated. The aim requires (1) and (2): a stated understanding outranks an
implied one, so Harford's "let the ending carry it" is accepted for the *lesson* and rejected as a
general policy on judgment.

### 4.3 The measurable disagreements

| metric | Fisher | Harford | Sapolsky | Hildebrandt |
|---|---|---|---|---|
| unit length | **27 min** | 37 min | 97 min¹ | — |
| speech rate | 137 wpm | **127 wpm** | 160 wpm | — |
| sentence median | 17 | **12** | 13 | 20² |
| short (≤8 words) | 16% | **33%** | 35% | 24%² |
| second person /1k | **6.3** | **6.7** | 26.4³ | 0.56² |

¹ a university timetable, not a design choice · ² written prose, explicitly excluded from delivery
· ³ live-room address ("you guys"), an artefact of teaching to a room

**Resolution by medium, not by vote.** Rank the sources by how close their corpus is to
single-narrator audio with no visual aid:

- **Sentence rhythm → 12–13 words median, a third under eight.** The two sources whose listeners
  had *nothing in their hands* (Harford, Sapolsky) land at 12 and 13 independently. Fisher's 17 is
  lecture prose delivered alongside slides and two mindmaps — the medium that his own §G says
  cannot come with us.
- **Speech rate → ~130 wpm.** Harford 127 is audio-native and produced; Fisher 137 is slide-aided;
  Sapolsky 160 is a live room. Dense material, no picture, slower end.
- **Unit length → 25–30 min.** The unit is *one apparatus*, which is Fisher's unit, so his figure
  governs. Harford's 37 is one *case*.
- **Second person → ≈6.5 per 1,000 words.** The strongest quantitative result in the whole
  exercise: **Fisher 6.3 and Harford 6.7**, two sources in different genres, converging within
  0.4. Sapolsky and Hildebrandt are excluded for the reasons above.

### 4.4 A conflict with no source-based answer

Both spoken sources identify themselves **by name** — "I'm Terry Fisher", "I'm Tim Harford" — and
both use it as the frame that follows the hook. A synthesised narrator has no name and cannot
honestly claim one. What occupies that slot is a genuine open question, not something the corpora
can settle. Options: a series name without a person ("This is *Casework*, episode four"); a pure
position statement with no identification at all; or an explicit statement that the narration is
synthetic. **This needs a decision before the writer prompt is written.**

## 5. Targets for `persona.yaml` and `voice_profiles.yaml`

Derived above; kept out of the prompts so they can be retuned without rewriting a role.

```yaml
defaults:
  target_minutes: 27        # one apparatus; 15-45 real range (Fisher, measured)
  host_mode: single
# rhythm and delivery targets for the writer prompt and the tone table
sentence_median_words: 12   # Harford 12, Sapolsky 13 — the two unaided-audio sources
short_sentence_frac: 0.33   # a third at eight words or fewer
speech_rate_wpm: 130        # Harford 127 (audio-native) over Fisher 137 (slide-aided)
second_person_per_1k: 6.5   # Fisher 6.3, Harford 6.7 — independent convergence
```

Freshness watchlist, split as the Fisher dossier requires — **devices to keep, varying the
wording** (the restatement, backward reference, the deferral, the concession) against **filler to
ban** ("however", spatial deixis of every kind, summary openers at a close).

## 6. Four ways to combine them

### Option A — Layered *(recommended)*

Each source owns a layer; §4 shows the conflicts are conflicts of scale, not of substance.

| Layer | Owner | What it fixes |
|---|---|---|
| The question-set an answer must satisfy | Hildebrandt | what the episode is *for* |
| Series and episode architecture | Fisher | order, oscillation, deferral, position |
| First three minutes, last two, and the sentence | Harford | whether anyone keeps listening |
| One recurring interior beat | Sapolsky | how a single explanation is opened up |

**Episode spine:** cold open on the instance → orientation → the system described operationally,
on its own terms → the text, quoted once, then named → work it → the levels beat → what the rule
assumes about the machine → where it is contested → as written against as enforced → what you now
ask → sources read aloud.

*For:* uses every source where its evidence is strongest; every element counted or quoted.
*Against:* eleven beats in 27 minutes is dense, and a spine this explicit can read as a checklist
if the writer prompt does not also say when to skip a beat.

### Option B — Course companion (Fisher-dominant)

Fisher's architecture governs everything, including the opening: orientation first, hook second or
not at all. Harford contributes only rhythm, endings, and the spoken sources. Built to be worked
through unit by unit alongside a syllabus.

*For:* maximal navigability; simplest to write; closest to the study use.
*Against:* discards the strongest listenability evidence in the roster. A dense episode that opens
on orientation has to survive its first minute on the listener's discipline alone, and Fisher's
own Principle 1 says listening alone is where learning fails.

### Option C — Case-led (Harford-dominant)

Every episode is a real, documented controversy; the apparatus is what you need in order to
understand it. Fisher supplies deferral, the spiral promise and the restatement; Hildebrandt the
questions the case must answer; Sapolsky the levels.

*For:* most listenable; the case supplies the reason to care; consistent with Fisher's own
practice of building case studies from real controversies.
*Against:* coverage becomes hostage to which cases exist — an apparatus with no good controversy
attached gets under-taught — and it leans on Harford's "let the ending carry the lesson", which
§4.2 rejects against the aim.

### Option D — Oscillating types (Fisher's own solution, generalised)

Alternate **episode types** rather than blending them: a case episode (Harford-shaped) then an
apparatus episode (Fisher-shaped), with the switch announced in both directions and the episode
number attached. This is exactly what Fisher does with nine doctrinal and three theory lectures.

*For:* no compromise between the two strongest structural sources — each episode type stays pure;
the alternation is the single best-evidenced series-level practice in the roster.
*Against:* doubles the episode count or halves coverage per unit; pairs must be planned together;
a listener dipping in can land on the wrong type.

### The recommendation

**A, with D's oscillation reserved for material that has no case.** Layered episodes are the
default. The conceptual apparatus that has no controversy attached — risk-based against
rights-based regulation, the pacing problem, Lessig's modalities, the Brussels effect — becomes its
own **lens episode**, placed between doctrinal ones and announced in both directions.

That is Fisher's nine-and-three, rebuilt from evidence rather than borrowed: the material that
*has* a case gets Option A; the material that has only arguments gets its own type. It also gives
the series its shape for free — roughly two lens episodes for every five or six doctrinal ones.

## 7. What synthesis cannot settle

1. **Course companion or standalone series?** Decides how much orientation each episode carries,
   and whether Option B's case gets stronger.
2. **The narrator's identity in the frame slot** (§4.4).
3. **Coverage ambition** — seven units at one apparatus per episode is not seven episodes.
4. **Fisher's sixth pass** remains unmet: an independent reader. Everything in his dossier is one
   analyst's work, verified mechanically and extended by held-out reading.
