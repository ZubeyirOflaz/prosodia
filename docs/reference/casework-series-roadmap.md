# `casework` — series roadmap

Series A is scaffolded at `projects/ai_act/`. This document holds the other three so they can be
picked up cold, months later, without re-deriving the reasoning. The shape comes from
[`casework-synthesis.md`](casework-synthesis.md) §6; the boundaries come from one test.

## The test that draws the boundaries

**Can a listener start here?** Not "is this a different topic" — dependency. Running it over the
source material gives a lopsided graph:

- **Entered cold:** the AI Act itself · fundamental rights and surveillance · governance inside
  organisations
- **Dependent:** the GDPR/liability/DSA material (it is *about* instruments colliding, so it
  presupposes them) · comparative governance (presupposes the model being compared)
- **Presupposed by everything:** the conceptual apparatus — the pacing problem, risk-based against
  rights-based regulation, regulation by architecture, the Brussels effect

That last line is the counterintuitive result and the reason there is no "Series 0". **The material
that looks most like a natural first season is precisely the material that must never be one**: if
the conceptual groundwork becomes its own series, every later series silently depends on it and
nothing is standalone. It is distributed instead as the **lens layer** — roughly one episode in
four, inside every series, with the switch announced in both directions.

---

## Series A — The Instrument · `projects/ai_act/` · **scaffolded**

**Covers:** the AI Act end to end, with lens episodes woven through. Scope and the definition of an
AI system; the actors it names; the risk tiers; prohibited practices; the high-risk regime; GPAI
and systemic risk; governance and standardisation; enforcement, penalties and the timeline; the
standing critiques of the product-safety framing.
**Held verdict:** was regulating artificial intelligence as a *product* the right choice?
**Size:** 10–12 episodes. **Depends on:** nothing.
**Reserves:** everything in B, C and D, named aloud when an episode reaches for it.

---

## Series B — The Collisions

**The question:** what happens when one instrument meets another, and when a rule meets a machine
that does not behave the way the rule assumes?

**Covers:** the GDPR interface — lawful bases and purpose limitation as constraints on training;
Article 22 and automated decision-making; the information duties; special-category data and the
inference problem; DPIAs; anonymisation and why it usually fails; the overlapping and conflicting
obligations where the AI Act and the GDPR meet. Then liability: the revised Product Liability
Directive and software as a product; fault-based liability and the burden of proof; the withdrawn
AI Liability Directive and what filled the gap. Then the rest of the acquis as it bites on AI: the
DSA's risk assessments, recommender transparency and researcher access; the DMA and gatekeepers;
the Data Act and Data Governance Act; copyright, text-and-data-mining exceptions, training-data
legality and output protectability.

**Held verdict:** does layered protection actually protect, or does it multiply duties while
leaving the same gap? **Size:** 8–10 episodes. **Depends on:** Series A — this series is *about*
collisions, so the instruments must already be known. It must state its prerequisites in episode 1
and re-earn any term it leans on.

**The signature beat lands hardest here.** "What the rule assumes about the machine" is at its
sharpest on Article 22 and the explanation debate: the distinction between a **justification** and
an **explanation** — where the latter earns its place only by making a decision contestable — is
the single most useful idea in the whole roster for this material.

**Before planning:** a docket on the Art. 22 case law including SCHUFA (C-634/21); the state of the
explanation debate with who holds what; the PLD's treatment of software; and at least one
documented controversy per episode where two instruments genuinely conflicted.

---

## Series C — The Constitutional Layer

**The question:** what survives when the rules meet real power?

**Covers:** the Charter and ECHR rights AI engages — privacy, data protection, non-discrimination,
fair trial, expression and assembly; **proportionality as the standard tool**, taught properly
rather than invoked; the mass-surveillance jurisprudence (*Digital Rights Ireland*, *Schrems I* and
*II*, *La Quadrature du Net*, *Big Brother Watch*); predictive policing, biometric identification
and the rule of law; democracy and elections — microtargeting, synthetic media, the Political
Advertising Regulation; emergency powers, derogation and the erosion of safeguards.

**Held verdict:** is proportionality a real constraint on state power over data, or a form that
ratifies whatever was going to happen?
**Size:** ~8 episodes. **Depends on:** nothing — **the most genuinely standalone of the four**, and
a listener could start here cold.

**This is the strongest candidate for the best episodes in the production.** It has what the
persona is built for and what the others have less of: real people with names, real judgments with
consequences, and the one place the rarely-used `dramatic` tone is actually earned — the moment a
right is lost or a power upheld. If the pilot arc in Series A shows the spine works, C is where it
will pay best.

**Before planning:** judgment summaries rather than full texts, with the proportionality reasoning
extracted; the factual background of each case as a narrative with named applicants; and the
documented deployments (which force, which system, which years, what happened).

---

## Series D — Elsewhere and Inside

**The question:** who else tried, and what does any of this look like from inside an organisation?

**Covers, in two halves.** *Elsewhere:* the Council of Europe Framework Convention as the first
binding international AI treaty; the OECD principles, the UNESCO recommendation and the G7 process;
the UN's Global Digital Compact; the United States as a sectoral and state-level patchwork with
executive-order volatility; China's algorithmic-recommendation, deep-synthesis and generative-AI
measures with their registration regime; standards bodies as governance (ISO/IEC 42001, IEEE);
fragmentation and geopolitical competition. *Inside:* governance frameworks, model cards,
datasheets and system cards; auditing and assurance, internal against third-party, and the access
problem; impact assessments — DPIA, FRIA, algorithmic; procurement as a regulatory instrument;
accountability for agentic systems, with human-in-the-loop as a legal construct.

**Held verdict:** does any of this machinery produce trustworthiness, or only its documentation?
**Size:** ~8 episodes, and it splits cleanly into two four-episode arcs if that reads better.
**Depends on:** Series A for the comparative half (you need the EU model to compare against); the
organisational half is close to standalone.

**Note the verdict is the accountability paradox** — that the audit apparatus can hollow out the
quality it measures. It is the sharpest question in the roster and it belongs last, because it
judges everything the three earlier series described.

---

## Practical notes for whoever picks this up

- **One project directory per series**, each with its own `series.yaml`, `research/`,
  `lexicon.yaml` and `voices/`, all carrying `persona: casework`. Follow `projects/ai_act/`.
- **Use the same narrator clip across every series.** It is the primary defence against timbre
  drift, and four series is a long time for a voice to wander.
- **Keep lexicons empty until something is heard wrong.** Raw spelling generally beats a respelling
  on this engine; add an entry only after hearing a specific name mangled.
- **Cross-series deferral is a planner instruction**, already in the prompt: reserved material is
  named aloud with the series that takes it, never silently covered.
- **The order is not fixed.** A depends on nothing; C depends on nothing. If the pilot arc suggests
  the case-led material works better than the instrument-led material, C can run second or even
  first. B and D need A.
