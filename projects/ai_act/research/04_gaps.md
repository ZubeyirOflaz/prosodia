# Docket 04 — Gap register  ·  updated after the deep research pass, 2026-09-12

The Planner uses web search **only** for a gap named here. Everything below is either **CLOSED**
(with where it was closed) or **OPEN** (with what is needed).

---

## CLOSED in the research pass

| # | Gap | Closed by |
|---|---|---|
| 1 | Operative text of the core articles | **`06_primary_text.md`** — Arts. 2, 3, 5, 43, 65–68, 99, 101, verbatim |
| 2 | Opening instances for four episodes | `05_foreign_instances.md` |
| 3 | Operational description of the systems in the cases | `03_cases_and_instances.md`, revised — both CAS and the Dutch risk model now have mechanism, inputs and measured performance |
| 4 | The fundamental-rights alternative in the drafting | **EDPB–EDPS Joint Opinion 5/2021** (18 June 2021): criticised the "positive list" approach to prohibitions, argued "risk to fundamental rights" should align with the GDPR, wanted societal risks to *groups* assessed, and **called for a general ban on biometric identification in publicly accessible spaces**. PDF: `edps.europa.eu/system/files/2021-06/EDPB-EDPS-2021-13-Artificial-Intelligence_EN.pdf` |
| 5 | The Omnibus's official number | **Regulation (EU) 2026/1744**, OJ **24 July 2026**, in force **27 July 2026**; also amends the EASA Regulation 2018/1139 and the Machinery Regulation 2023/1230 |
| 6 | The other penalty tiers | `06_primary_text.md` — €35m/7%, €15m/3%, €7.5m/1%, SME rule, and Art. 101 separately for GPAI |
| 7 | Governance bodies | `06_primary_text.md` — Arts. 65–68, including the permanent membership of the Advisory Forum |
| 9 | Whether the standards have arrived | **They have not.** See `02_critiques_and_contested.md`, revised: as of **June 2026 no JTC 21 deliverable grants presumption of conformity, because none has been cited in the Official Journal**. EN 18286 (AI quality management system) is the most advanced, at Approval |
| 10 | Budapest Bank | Case **NAIH-85-3/2022**; details in `03_cases_and_instances.md` |
| 11 | The Brussels effect, tested | Genuinely contested, with named positions on both sides — see below |
| 13 | The Garante decision date | **2 November 2024**, *provvedimento* n. 755 |
| 14 | Art. 2 extraterritorial scope | `06_primary_text.md` — limb (c) covers third-country providers and deployers where the **output** is used in the Union |
| 15 | Art. 43 allocation | `06_primary_text.md` — Annex III points 2–8 are **self-assessed**; only point 1 offers a notified-body route |
| 17 | CJEU defeat-device rulings | **C-128/20, C-134/20 and C-145/20, judgments 14 July 2022** (referrals from the Austrian Supreme Court and the regional courts of Eisenstadt and Klagenfurt). Earlier: **C-693/18**. Curia press release `cp220124en.pdf` |
| 18 | The DOT OIG report | **AV2021020**, *"Weaknesses in FAA's Certification and Delegation Processes Hindered Its Oversight of the 737 MAX 8"*, **23 February 2021**. Findings: no risk-based approach to ODA oversight; ODA personnel independence not ensured; FAA engineers at the Boeing office balancing certification against oversight duties; oversight insufficient to catch emerging high-risk concerns |

### On the Brussels effect (gap 11), because it is a lens episode

Not settled, and the disagreement is the content:
- **For:** "The Brussels Effect and Artificial Intelligence: How EU regulation will impact the
  global AI market" (GovAI, arXiv 2208.12645) — de facto and de jure effects likely for parts.
- **Against:** CEPA, *"Burying the Brussels Effect? AI Act Inspires Few Copycats"* — limited
  diffusion; Canada's AIDA and Brazil's risk-tiered bill are the main echoes, and Brazil's final
  shape is uncertain.
- **Inverted:** *"The Brussels Side-Effect: How the AI Act Can Reduce the Global Reach of EU
  Policy"* (German Law Journal, Cambridge).
- **Reframed:** *"Brussels effect or experimentalism? The EU AI Act and global standard-setting"*
  (Internet Policy Review).
- **Critique of the frame itself:** that it confuses compliance with legitimate authority and
  assumes the universality of European liberal values.

---

## OPEN — and the first one is a trap

### ⚠ 8. The "first AI Act fines" of €47 million — **UNVERIFIED, AND PROBABLY WRONG**

Two aggregator blogs report that within days of 2 August 2026 the **EU AI Office** issued three
fines totalling **€47m**: €18m against a pan-European HR technology company for hiring AI without
conformity-assessment documentation or human oversight; €14m against a credit-scoring provider for
Annex III documentation failures; €15m against a retail chain for real-time emotion recognition
across four Member States.

**Three reasons to distrust it**, all established in this pass:

1. **No authoritative source.** A search restricted to `europa.eu` domains returns the enforcement
   framework pages and the 2 August announcement, and **no press release announcing any fine**.
2. **The Commission's own press release says otherwise.** IP/26/1714, **31 July 2026**,
   *"Commission starts enforcing AI Act rules and new transparency requirements on 2 August"*,
   describes the machinery being switched on — the Scientific Panel, complaints tools, whistleblower
   channels — and **names no company and no penalty**.
3. **It does not fit the architecture.** Under Art. 101 the **Commission** may fine providers of
   **general-purpose AI models**. Penalties under Art. 99 are laid down and applied by **Member
   States** through national market surveillance authorities. A hiring platform, a credit scorer and
   a retail chain are high-risk providers and deployers — **not the AI Office's to fine**.

**UPDATE 2026-09-13 — the Commission press release was retrieved and read in full.** It confirms
the negative: IP/26/1714 announces enforcement beginning and **names no company and no penalty**. It
also supplies the three-way enforcement split (`06_primary_text.md`), which makes the reported fines
*less* plausible, not more: a hiring platform, a credit scorer and a retail chain fall to **national
competent authorities**, not to the AI Office that the reports credit.

**UPDATE 2026-09-13 (second) — reason 3 was RIGHT but stated too crudely; here it is corrected
against the text.** The 2026 amendment inserted Arts. 75a–75d, which the docket did not know
about. Under **Art. 75(1) as amended, the AI Office is *exclusively competent*** for supervision
and enforcement in relation to two classes of AI **system** — not merely GPAI models:

- **(a)** AI systems based on a general-purpose AI model **where the model and the system come
  from the same provider, or from the same undertaking** — excluding Annex I product systems,
  Annex III point 2 systems, law-enforcement/border/financial systems under Art. 74(6), and
  Annex III point 8 systems in the administration of justice; and
- **(b)** AI systems that constitute, or are integrated into, a **VLOP or VLOSE** designated under
  the DSA (Regulation (EU) 2022/2065).

That competence runs to **providers** of those systems, and to deployers only where the deployer
is the provider or part of the same undertaking. **Art. 75c(4)** then lets the AI Office impose
penalties under Art. 99(3)–(7) *mutatis mutandis*, and Art. 75(1e) shows the class expressly
includes **high-risk** systems.

So the old formulation — "the Commission fines GPAI model providers under Art. 101, everything
else is the Member States'" — **is now incomplete**: the AI Office can fine the provider of a
high-risk *system* when that system falls inside Art. 75(1).

**The objection to the €47m story survives, and is sharper for it.** A pan-European HR platform, a
credit-scoring provider and a retail chain running emotion recognition are none of them a
same-undertaking GPAI system or a VLOP. They fall to **national competent authorities** under
Art. 99. The reports credit the AI Office with fines that, on the amended text, are still not the
AI Office's to impose — and now the reason is a specific competence rule that can be quoted, rather
than a general impression of the architecture.

**Verdict for the writer: do not use this.** If an episode wants to say what AI Act enforcement has
actually produced, the honest answer as of this compilation is: the powers went live on 2 August
2026, the AI Office reportedly sent its first **requests for information** to frontier GPAI
providers around **29 August 2026** *(also secondary, also unconfirmed)*, and **no confirmed
penalty has been established**. That is a more interesting fact than the fines would have been.

### 12. The Court of Rome annulment — confirmed in substance, worth a primary check

Now multi-sourced and the reasoning is clear (see `05_foreign_instances.md`): annulled on
**jurisdiction**, not merits. Judge **Damiana Colla**, **18 March 2026**. Still worth reading the
judgment itself if it can be obtained, because an episode turns on the distinction.

### ~~16. *Moffatt v Air Canada*~~ — **CLOSED 2026-09-13**, retrieved manually

Decision read. Citation, tribunal member, date, the "remarkable submission" passage and the full
order are now verbatim in `05_foreign_instances.md`.

### ~~19. EUR-Lex consolidated text~~ — **CLOSED 2026-09-13**

Fetched, converted and installed as `07_operative_text.md`. `06_primary_text.md` remains one
remove from the source and is now marked superseded wherever the two overlap.

---

## Links for manual retrieval

The two items a person can get in a browser in a minute, and automated retrieval cannot:

1. **Moffatt v Air Canada, 2024 BCCRT 149** —
   `https://www.canlii.org/en/bc/bccrt/doc/2024/2024bccrt149/2024bccrt149.html`
   *(CanLII blocks scripted requests.)* What is needed: the tribunal member's exact words on the
   "separate legal entity" submission, and confirmation of the damages figure.

2. **Any authoritative source for AI Act enforcement actions to date** — the Commission press
   corner filtered for the AI Act, or the AI Act Service Desk:
   `https://ec.europa.eu/commission/presscorner/` and
   `https://ai-act-service-desk.ec.europa.eu/`
   What is needed: whether **any** fine or formal proceeding under the AI Act has actually been
   opened, and by whom. This decides the enforcement episode.

Lower priority, obtainable but not yet read in full (the consolidated AI Act is no longer
on this list — it is in `07_operative_text.md`):
- The Omnibus: `https://eur-lex.europa.eu/eli/reg/2026/1744/oj/eng`
- EDPB–EDPS Joint Opinion 5/2021:
  `https://www.edps.europa.eu/system/files/2021-06/EDPB-EDPS-2021-13-Artificial-Intelligence_EN.pdf`
- DOT OIG AV2021020:
  `https://www.oig.dot.gov/sites/default/files/FAA%20Certification%20of%20737%20MAX%20Boeing%20II%20Final%20Report%5E2-23-2021.pdf`
- Amnesty, *Xenophobic machines* (EUR 35/4686/2021):
  `https://www.amnesty.org/en/documents/eur35/4686/2021/en/`
- NAIH decision NAIH-85-3/2022 via GDPRhub:
  `https://gdprhub.eu/NAIH_(Hungary)_-_NAIH-85-3/2022`
- Dutch government Algorithm Register entry for CAS:
  `https://algoritmes.overheid.nl/en/algoritme/81228922`

---

## OPENED BY THE SERIES PLAN, 2026-09-13

The first `prosodia plan` run against this docket was reviewed independently. It produced a usable
twelve-episode plan, but **49 of its 63 article numbers and roughly fifteen scholarly citations are
not in any file in `research/`** — the planner reconstructed them from model memory and, in one
episode, told the writer they came from the docket. That is a docket problem before it is a planner
problem: the material below is what an episode plan legitimately needs and this docket does not
hold. Until each is closed, anything the plan says about it is unverified.

### ~~Priority A~~ — **CLOSED 2026-09-13** by `07_operative_text.md`

The EUR-Lex consolidated text (CELEX **02024R1689-20260727**) was fetched, converted with a
per-article completeness check, and installed as `07_operative_text.md`. Gaps 20–27 are closed:
every article below is now in the docket verbatim, with its paragraph numbers and point letters,
and can be quoted with its citation.

| Gap | Material | Status |
|---|---|---|
| 20 | Art. 3(63) and the GPAI definitions | closed — **with a correction, below** |
| 21 | Arts. 9–15, the high-risk requirements | closed, all seven verbatim |
| 22 | Art. 6(1)–(4), classification and the 6(3) derogation | closed |
| 23 | Art. 5(1)(g) | closed — the whole of Art. 5, including the new (ba), (bb), (1a), (1b) |
| 24 | Annex III points 1–8, enumerated | closed, with all sub-points |
| 25 | Arts. 85–87, complaint and remedy | closed |
| 26 | Arts. 95–96, codes of conduct and guidelines | closed |
| 27 | Art. 112, evaluation and review | closed |

**Gap 20 was wrong as written, and the correction matters.** The gap asked for Art. 3(63)
"including the training-compute criterion". There is no compute criterion in the definition.
Art. 3(63) defines a general-purpose AI model by generality and task range alone; the **10^25
floating-point-operation** figure is **Art. 51(2)**, where it is a *rebuttable presumption* of
high-impact capability, and Art. 51(3) lets the Commission move it by delegated act. A definition
and a rebuttable presumption amendable by delegated act are different kinds of thing, and an
episode that puts the number in the definition has the architecture of the GPAI tier wrong. Art. 51
is in `07` alongside the definitions for exactly this reason.

**The Article 26 dispute is resolved, in the plan's favour.** The plan quoted *"the necessary
competence, training and authority"* and cited Article 26. That attribution is **correct** — it is
Art. 26(2), and the sentence continues "as well as the necessary support". The defect was never
that the plan was wrong; it was that the docket held no Art. 26 text, so nothing could have told
anyone either way, and the plan told the writer the quotation came from the docket. It does now.

**Three things the docket did not know about at all**, all inserted by Regulation (EU) 2026/1744
and all now in `07`:

- **Arts. 75a–75d** — the AI Office's own supervisory and enforcement powers, commitments, and
  **fines and periodic penalty payments**. This bears directly on gap 8 below: any account of "who
  can fine whom" written before this was read is incomplete, and the three-way enforcement split
  recorded there needs re-checking against 75a–75d.
- **Art. 4a** (special-category data for bias detection) and **Art. 60a** (real-world testing
  outside sandboxes).
- **Annex XIV** — notified-body designation codes, under Art. 30.

Thirty-seven articles and annexes carry amended text. `07` lists them, with the caveat that the
list is marker-derived and can be off by one article at a boundary.

**Two gaps this opened.** Both are follow-on work, not blockers:

30. **Recitals.** A consolidated text omits the preamble, so `07` has no recitals. The "why this
    rule and not another" beat leans on them. They must come from the original OJ text of
    2024/1689 and be cited as recitals, never as operative provisions.
31. ~~**Re-check gap 8 against Arts. 75a–75d.**~~ **Done, same day** — see the second update
    under gap 8. The conclusion held; the reasoning was replaced with the competence rule in
    Art. 75(1) as amended. `06_primary_text.md`'s "three bodies, not one" section still carries the
    older, cruder split and should be read together with that update.

**Priority B — no source base behind two planned episodes.**

28. **Ep 2 and Ep 10 (lens episodes)** have no docket material behind them at all. Every position
    in both was supplied from memory, and several positions are attributed to no one. Needed: for
    each position the episodes put in play, **one named holder and one locatable place they said
    it** — a paper, a book, an opinion, a speech. A position without a holder is cut.

**Priority C — a claim the plan makes that nothing supports.**

29. **"Four mutually incompatible versions" of the €47m story** (plan line 3). Gap 8 above says
    correctly that the figure is unverified and must not be used; the plan uses it anyway, as a
    thing to debunk, and escalates it with a count of variants that no source in this docket
    establishes. Either produce the four variants with their sources, or the claim goes and the
    debunking is rebuilt on what gap 8 actually establishes: a press release naming no company and
    no penalty, against an enforcement architecture split three ways.

---

## APPLIED TO THE PLAN, 2026-09-13 (second review)

A second review, run with the operative text in hand, checked every citation and quotation in
`plan/outline.md` mechanically against `07_operative_text.md`. Five point corrections were made to
the plan; each is recorded here because each was *plausible on the page* and none would have been
caught by reading.

1. **Annex X does not govern the database.** The plan had it governing the law-enforcement and
   migration entries of the EU database. Annex X is the list of Union acts establishing the
   large-scale IT systems, reached through **Art. 111(1)**. Restricted registration is **Art.
   49(4)** — Annex III points 1, 6 and 7 go into a secure non-public section open only to the
   Commission and the authorities in Art. 74(8).
2. **Common specifications take the examination procedure of Art. 98(2)**, not "the comitology
   procedure of Arts. 97–98". Art. 97 is the delegation power, for delegated acts.
3. **Art. 6(3) was quoted in an inverted form.** The plan asked whether a system does "materially
   influence the outcome of decision-making"; the Act's test is negative — a system escapes where
   it does not pose a significant risk, "including by **not materially influencing** the outcome of
   decision making". Quotation marks are inaudible, so an inverted paraphrase inside them is spoken
   as the statute.
4. **Art. 43's fifth subparagraph was quoted with its middle silently removed.** The full text is
   "the market surveillance authority **referred to in Article 74(8) or (9), as applicable**, shall
   act as a notified body" — and the elided clause is the point, because Art. 74(8) makes that
   authority the **data protection authority** for a law-enforcement system.
5. **Two invented sentences sat in quotation marks** next to a real citation ("your system shall not
   discriminate"). Marked as illustrations the script must disclose before speaking.

**Plus one rebuild, not a correction:** Ep 11's debunking of the €47m story rested on the
pre-amendment split. It now runs on Art. 75(1) as amended, Art. 75c(4) and Art. 75(1e) — see the
second update under gap 8. Arts. 75 and 75a–75d were added to the coverage map, which had reached
them only inside the range "Arts. 74–87".

**What produced most of this:** the map assigned **77 of 110 articles only inside a range**. A range
covers whatever is in it, including six articles inserted by Regulation (EU) 2026/1744 that the
planner never read and never named. The persona's planner now forbids assigning by bare range.
