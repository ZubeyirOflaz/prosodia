# Docket 01 — The instrument  ·  compiled 2026-09-12

Architecture of Regulation (EU) 2024/1689 as amended. **Article numbers here are pointers for
navigation, not quotations** — see the provenance warning in `00_status_and_dates.md`. Anything the
writer speaks as the text's own words must come from the consolidated version on EUR-Lex.

---

## What counts as an AI system at all — Art. 3(1)

The definitional gate, and the natural first episode: everything else in the Act only matters if
your thing is through it.

> A **machine-based system** designed to operate with **varying levels of autonomy**, that **may
> exhibit adaptiveness** after deployment, and that, for **explicit or implicit objectives**,
> **infers** from the input it receives how to generate outputs such as predictions, content,
> recommendations or decisions that can **influence physical or virtual environments**.
>
> *(Paraphrase from secondary summaries — verify verbatim before quoting.)*

**Commission Guidelines on the definition**, published **February 2025**, alongside the tranche of
obligations that began applying on 2 February 2025 (definitions, AI literacy, prohibitions). The
clarification that matters most for teaching: **adaptiveness after deployment is NOT a necessary
condition**, because the Act says "may". A system that never learns anything after shipping is
still an AI system.

**Where the boundary bites** — the episode's "change one fact" material: the elements are
machine-based, autonomy, inference, objectives, output, influence. Vary one and the system falls
out of scope. A deterministic rule engine with no inference is the obvious test case.

## The actors

Provider · deployer · importer · distributor · authorised representative. **Duties attach to roles,
not to technologies**, and a single organisation can occupy several at once or change role by
modifying a system. This is where most real disputes live and it is badly under-taught elsewhere.
*(Definitions in Art. 3; confirm the numbering.)*

## The risk tiers

1. **Prohibited** (Art. 5) — applies from 2 Feb 2025; penalties from 2 Aug 2025.
2. **High-risk** — Annex III (stand-alone use cases) and Annex I (embedded in already-regulated
   products). The heavy regime: risk management, data governance, technical documentation, logging,
   human oversight, accuracy/robustness/cybersecurity, conformity assessment, CE marking,
   post-market monitoring.
3. **Limited risk** — transparency duties (Art. 50), from 2 Aug 2026.
4. **Minimal risk** — nothing.

**The structural point for a lens episode:** the tier is fixed by *intended purpose at design
time*, while harm is contextual and shows up in deployment. That gap is the Act's central design
bet, and it is what the risk-based versus rights-based argument is actually about.

## Prohibited practices — Art. 5

The original list covers: manipulative or deceptive techniques; exploitation of vulnerability;
social scoring; untargeted scraping of facial images; **emotion inference in the workplace and in
education institutions**; biometric categorisation; predictive criminal-risk assessment of
individuals; and real-time remote biometric identification in public for law enforcement, with
exceptions.

**Art. 5(1)(f) — emotion recognition** is the best-documented prohibition for an episode: it bans
inferring emotions of a natural person in **workplace and education** settings, **except for
medical or safety reasons**. The Commission's stated rationale is worth quoting: these are
**asymmetric environments with a fundamental power imbalance** — a worker or a student cannot
meaningfully decline.

**Added by the 2026 Omnibus, in force 2 December 2026:** AI-generated non-consensual intimate
imagery, and AI-generated CSAM. See `00_status_and_dates.md`.

**Commission Guidelines on prohibited practices**, 4 February 2025, **non-binding**, with worked
examples. That they are non-binding is itself teachable: the interpretation that will actually bind
comes later, from courts.

## The high-risk regime

Two routes in — Annex III use cases, and Annex I product-safety legislation — and one regime out.
The obligations listed above are the ones a deployer or provider actually feels. **Conformity
assessment against harmonised standards produces a presumption of conformity**, which is the hinge
the whole standardisation critique turns on (see `02_critiques_and_contested.md`).

**Now deferred: Annex III to 2 December 2027, Annex I to 2 August 2028.**

## General-purpose AI

Obligations from 2 Aug 2025. Code of Practice (10 July 2025; adequate 1 Aug 2025) with chapters on
**Transparency, Copyright, and Safety and Security** — the last binding only systemic-risk
providers. **Systemic risk threshold: 10^25 FLOP**, reported as capturing 5–15 companies. Providers
of such models must notify the AI Office. AI Office enforcement powers live from 2 Aug 2026.

**The teachable oddity:** a compute threshold is a proxy for a capability question, and it is the
kind of bright line that is administrable precisely because it does not measure what anyone
actually cares about.

## Governance and enforcement

- **AI Office** — inside the Commission; supervises GPAI models centrally; steers uniform
  implementation.
- **AI Board**, **Scientific Panel**, **Advisory Forum** — *composition and powers not yet
  established in this docket; see gaps.*
- **National competent authorities** — each Member State designates a **notifying authority** and a
  **market-surveillance authority** (Art. 70). Market surveillance does post-market work (Art. 74):
  investigate complaints, demand documentation, require corrective measures, fine, withdraw from
  the market. Live from 2 Aug 2026.
- **Notified bodies** — third-party conformity assessment where required.
- **Penalties** — up to **€35 million or 7% of worldwide annual turnover** for prohibited
  practices; other tiers not yet established here.

## Suggested episode order for the apparatus arc

Each is one apparatus, ~27 minutes. Lens episodes interleave at roughly one in four.

1. What counts as an AI system — Art. 3(1), the definitional gate
2. **[LENS] Why regulate a technology at all** — the pacing problem, regulation by architecture
3. Who you are in the picture — provider, deployer, and duties that follow roles
4. The ladder of risk — how the tiers are built and what the design bet is
5. The red lines — prohibited practices, and why these
6. **[LENS] Risk-based against rights-based** — the road not taken
7. The weight of high risk — what the regime actually demands
8. Standards, and who really writes the law — conformity, presumption, CEN-CENELEC
9. The general-purpose problem — GPAI, systemic risk, a compute threshold
10. **[LENS] The Brussels effect** — does any of this travel?
11. Who enforces this — AI Office, market surveillance, penalties, and the collection problem
12. **[VERDICT] Was a product the right thing to regulate?**
