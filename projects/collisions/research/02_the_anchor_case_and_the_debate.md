# Docket 02 — The anchor case, and the argument it did not settle  ·  compiled 2026-09-16

The roadmap names three things Series B must have before planning: the Article 22 case law
including SCHUFA, the state of the explanation debate with who holds what, and the PLD's treatment
of software. The first two are here; the third is in `01_operative_text.md`.

**Provenance.** Located by web search on 2026-09-16 against CJEU, Oxford Academic and SSRN records.
Bibliographic details verified; interpretive summaries are the compiler's. Nothing read in full.

---

## The anchor case — SCHUFA

**Case C-634/21, *SCHUFA Holding (Scoring)*, Court of Justice of the European Union, Grand Chamber,
judgment of 7 December 2023.** *Verified: case number, party, court, date.*

**The facts.** OQ was refused a loan by a German bank. The bank relied on a credit-repayment
probability score produced by SCHUFA, a German credit reference agency. OQ went after SCHUFA, not
the bank.

**The holding, and it is the first time the Court interpreted Art. 22 at all.** Producing the
score is itself an automated individual decision within Art. 22(1), *where the third party draws
strongly on that score* to establish, implement or terminate a contract. So the Art. 22 obligations
fall on the **scoring agency**, not only on the lender who acted on it.

> **Why this is the right anchor for the series.** The whole episode of Series A about who counts
> as provider and who as deployer turns on a role allocation under one instrument. SCHUFA is the
> same question under a different instrument, and it comes out differently: the Court reached past
> the party that made the decision to the party that made the thing the decision was made with.
> That is a collision the series exists to show — and it can be worked as a fact pattern, because
> there is a named person, a named firm, a refused loan and a dated judgment.

**The load-bearing words are in the test, not the outcome.** "Draws strongly on" is doing the work,
and it is the hinge a later episode can change one fact against: what if the bank had a human
review the file, and followed the score anyway? ⚠ The exact formulation used in the operative part
should be taken from the judgment itself before it is quoted aloud — the summaries here paraphrase.

---

## The debate SCHUFA did not settle: is there a right to an explanation?

Both sides have names, both are in the same journal, and they are answering each other. Give them
as an exchange, the way Episode 2 of Series A gives Easterbrook and Lessig.

**Against — the foundational sceptical paper.** **Sandra Wachter, Brent Mittelstadt and Luciano
Floridi, "Why a Right to Explanation of Automated Decision-Making Does Not Exist in the General
Data Protection Regulation", *International Data Privacy Law* 7(2) (2017), p. 76.** *Verified:
authors, exact title, journal, volume, year, first page.*

Their argument: Arts. 13–15 give a **right to be informed** — meaningful but properly limited
information about the logic involved, the significance and the envisaged consequences — and that is
a different and much smaller thing than a right to an explanation of a *particular decision* after
it has been made. Their constructive proposal is **counterfactual explanation**: tell the person
what would have had to be different for the answer to change, which is useful to them and does not
require opening the model. (*Wachter, Mittelstadt and Russell, "Counterfactual Explanations Without
Opening the Black Box", Harvard Journal of Law & Technology 31 (2018).* ⚠ *Issue and pages not
established here.*)

**For — the direct reply, published in the same journal months later.** **Andrew D. Selbst and
Julia Powles, "Meaningful information and the right to explanation", *International Data Privacy
Law* 7(4) (November 2017), pp. 233–242, DOI `10.1093/idpl/ipx022`.** *Verified: authors, exact
title, journal, volume, issue, month, year, page range, DOI.*

Their argument turns on what "meaningful information about the logic involved" must mean if it is
to mean anything: information is not meaningful unless it lets the person do something — contest
the decision, or exercise the rights the Regulation gives them elsewhere. Read that way the
provisions already require explanation in the sense that matters, whatever the drafters called it.

> **This is the exchange the persona's sharpest beat was built for.** The synthesis names the
> distinction between a **justification** and an **explanation** — the latter earning its place
> only by making a decision contestable — as the single most useful idea in the roster for this
> material. Selbst and Powles are arguing exactly that; Wachter and colleagues are arguing that the
> text does not carry it. Do not resolve it by picking the nicer-sounding side.

---

## What this docket does NOT yet have

Stated plainly, because a plan built on it will otherwise reach for these and reconstruct them:

- **A documented controversy per episode where two instruments genuinely conflicted.** The roadmap
  asks for one each. There is exactly one here (SCHUFA), and it is a collision between roles rather
  than between instruments. **Episodes on the DSA, the DMA, the Data Act, copyright and
  text-and-data-mining have no instance at all**, and the planner must mark them as not yet
  plannable rather than inventing one.
- **The operative text of the DSA, DMA, Data Act, Data Governance Act and the copyright
  directive.** Only the GDPR and the PLD are in `01`. Each is fetchable in one command —
  `consolidate.py <CELEX> out.md --select "…"` — and should be fetched before the episode that
  teaches it, not before the plan.
- **The withdrawn AI Liability Directive** and what filled the gap: no source here.
- **Post-SCHUFA Art. 22 case law.** The Court has ruled more than once since; this docket has the
  first judgment only, and any claim about the line of authority needs a later case.
- **Nothing on anonymisation, DPIAs or purpose limitation as applied to training** beyond the
  operative text itself.

## The rule that produced this file

Series A's first plan reconstructed forty-nine article numbers and fifteen citations from memory,
because it was planned against a docket that did not hold them. The fix was not a better planner
prompt; it was writing down what the docket lacked so the plan could say so. This section is that,
written before the plan rather than after it.
