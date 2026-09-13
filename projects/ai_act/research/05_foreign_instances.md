# Docket 05 — Instances from outside the EU, read through the Act  ·  compiled 2026-09-12

`03_cases_and_instances.md` left four episodes with no usable opening instance. This file fills
three of them from cases outside the EU's AI Act — and the exercise turned out to be worth more
than a gap-filler, because two of these cases are *inside the very machinery the Act borrowed*.

---

## THE DISCLOSURE RULE — read before using any of these

The persona forbids inventing controversies; it does not forbid analysing a real one under a law
that did not govern it. But the listener must never be left thinking the Act applied when it did
not. Two requirements:

1. **The case is stated as what it was** — the jurisdiction, the law actually applied, the actual
   outcome. No blurring.
2. **The AI Act reading is announced as counterfactual**, in the episode, at the point it starts:
   *"The Act did not apply here. It is worth asking what it would have demanded."*

**But check first whether it is counterfactual at all.** Article 2 gives the Act extraterritorial
reach — it bites on providers placing systems on the EU market wherever they are established, on
deployers located in the Union, and reportedly where a system's **output is used** in the Union.
Several of the cases below would be squarely in scope if the same system were offered to EU users
today. That question — "would this actually be covered?" — is itself a first-rate opening for the
scope episode. *(Art. 2's exact wording needs the EUR-Lex check; treat this as a pointer.)*

---

## 1. Moffatt v Air Canada — fills **"who you are in the picture"**

**Canada, Civil Resolution Tribunal of British Columbia. *Moffatt v. Air Canada*, 2024 BCCRT 149,
file SC-2023-005609, issued 14 February 2024, Tribunal Member Christopher C. Rivers.
VERIFIED AGAINST THE DECISION ITSELF.**

In November 2022, after the death of their grandmother, Jake Moffatt booked a flight with Air
Canada, having used the chatbot on Air Canada's website while researching. **The chatbot said
bereavement fares could be applied for retroactively.** They could not be. Moffatt claimed the
difference in fare.

The passage the episode turns on, verbatim from paragraph 27:

> "…Air Canada suggests the chatbot is a separate legal entity that is responsible for its own
> actions. **This is a remarkable submission.** While a chatbot has an interactive component, it is
> still just a part of Air Canada's website. It should be obvious to Air Canada that it is
> responsible for all the information on its website. **It makes no difference whether the
> information comes from a static page or a chatbot.**"

And at paragraph 28: *"I find Air Canada did not take reasonable care to ensure its chatbot was
accurate."*

**The order (paragraph 44): $812.02 in total** — **$650.88 in damages**, $36.14 pre-judgment
interest under the Court Order Interest Act, and $125 in tribunal fees, payable within 14 days.
*(An earlier version of this docket gave only the damages figure.)*

**Through the Act.** Air Canada is a **deployer** — it used an AI system under its own authority;
someone else provided it. The Act's entire architecture rests on that provider/deployer split, and
what Air Canada attempted was to invoke a **third category the Act does not contain**: the system
as its own responsible party. There is no such role, and the reason there is no such role is worth
a whole episode.

Two further readings, both teachable:
- **Art. 50 transparency** (live 2 August 2026) would require the chatbot to disclose that a person
  is interacting with an AI system. That duty addresses the *disclosure*, not the misinformation.
- **The Act would not have got Moffatt his C$650.88.** It is a market-surveillance regime, not a
  private right of action. His remedy came from ordinary contract and tort law. **The gap between
  regulatory compliance and individual redress is one of the most useful things this series can
  teach**, and this case shows it in miniature.

## 2. Volkswagen and the defeat device — fills **"standards and conformity assessment"**

**EU, 2015 onwards. Not counterfactual: this happened inside EU product-safety law.**

VW fitted software that recognised the conditions of the **type-approval test** and ran full
emissions control only during it, then reduced that control in ordinary driving — roughly **8.5
million affected cars in Europe**. The CJEU later held such devices unlawful under Art. 5(2)(a) of
Regulation 715/2007, rejecting the engine-protection exception — see **C-128/20, C-134/20 and
C-145/20, judgments of 14 July 2022**, on the "thermal window" that ran full exhaust-gas
recirculation only between **15°C and 33°C and below 1,000 metres**, letting NOx rise past the
limits outside it; and the earlier **C-693/18**. The European Parliament ran an
inquiry (EMIS, report A8-0049/2017). Afterwards, **Member States applied neither financial nor
legal penalties to manufacturers**; there were no mandatory recalls or retrofits and no withdrawal
of type approvals, and VW maintained it had never breached EU rules. The type-approval framework
was subsequently revised to require Member States to run a minimum number of independent tests each
year.

**Through the Act — and this is why the case matters more than any other in the docket.** The AI
Act's high-risk regime runs on the same machinery: **conformity assessment against harmonised
standards, producing a presumption of conformity, marked with a CE mark.** Dieselgate is that
machinery's most famous failure, and it failed in the specific way that should worry anyone
regulating AI: **the product was built to pass the assessment rather than to meet the standard.**
An AI system tuned to perform on the benchmark used for its conformity assessment, and differently
in deployment, is the identical failure with different physics.

It also answers Veale and Zuiderveen Borgesius empirically. They objected that the Act inherits
four decades of product-safety machinery. Here is what that machinery did when someone had a strong
incentive to game it — followed by an enforcement aftermath that produced almost nothing.

## 3. Boeing 737 MAX and the FAA's ODA — the same episode, from the other side

**United States, certification of the 737 MAX. DOT Office of Inspector General report AV2021020,
23 February 2021: *"Weaknesses in FAA's Certification and Delegation Processes Hindered Its
Oversight of the 737 MAX 8"*.** The report also found no risk-based approach to ODA oversight, that
ODA personnel independence from company influence was not ensured, and that FAA engineers stationed
at Boeing were balancing certification work against their oversight duties.

The FAA's **Organization Designation Authorization** programme lets a manufacturer perform
certification functions on the regulator's behalf. The OIG found that management and oversight
weaknesses limited the FAA's ability to assess risk in the Boeing ODA, and that **the FAA did not
have a complete understanding of Boeing's safety assessments of MCAS until after the first
accident**. An internal FAA survey found **56% of aircraft-certification staff felt there was too
much external influence on the agency, affecting safety**. Fourteen recommendations followed; the
FAA restored limited certification delegation to Boeing in September 2025.

**Through the Act.** Where Dieselgate shows a standard being gamed, Boeing shows **assessment
delegated to the party being assessed**. That is not a hypothetical worry for the AI Act: for most
stand-alone high-risk systems the default route is **the provider's own internal conformity
assessment**, with third-party notified bodies required only in limited cases. *(Verify the exact
allocation in Art. 43 before stating it.)* The question the episode can then put honestly is the
one the Boeing report answers: what does a regulator need in order to check work it has delegated,
and does any AI market-surveillance authority currently have it?

## 4. The Italian Garante and OpenAI — fills **general-purpose AI**

**Italy. A GDPR action, not an AI Act one — and it has a twist.**

Italy was the first country to **temporarily ban ChatGPT**, in late March 2023; access was restored
about a month later. The Garante then fined OpenAI **€15 million** (decision reported 2 November
2024, widely reported in December 2024) for processing personal data to train ChatGPT **without an
adequate legal basis**, inadequate transparency to users, inadequate age verification, and failure
to notify the March 2023 breach within 72 hours. It also used, for the first time, its power under
Art. 166(7) of the Italian Data Protection Code to order a **six-month public awareness campaign**
across radio, television, print and online media.

**The twist, and it is sharper than "the fine was overturned".** On **18 March 2026** the Court of
Rome, **Judge Damiana Colla**, annulled *provvedimento* **n. 755** of 2 November 2024 — **on
jurisdiction, not on the merits.** The court held the Garante had no competence once OpenAI
established its **Irish subsidiary in 2024**, so the GDPR's one-stop-shop mechanism sent the case to
the Irish authority. **The court never reached the substantive allegations at all.** As one
commentary put it: the decision did not find OpenAI innocent; it found that Italy had no right to
judge OpenAI. The European Law Blog analysis is titled *"Establish, Then Escape? How the Court of
Rome, the One-Stop-Shop and a Single Word Opened an AI Enforcement Gap"*.

**Through the Act.** This is what regulating a general-purpose model looked like **before there was
a regime for it**: a national data-protection authority reaching for GDPR because it was the only
instrument available — and then losing the case not on whether it was right, but on **whether it was
allowed to decide at all**, because the company had incorporated in another Member State. The AI
Act's answer is structural — GPAI obligations from August 2025, a Code
of Practice covering transparency, copyright and safety, a systemic-risk tier above 10^25 FLOP, and
**supervision centralised in the AI Office rather than left to twenty-seven national regulators**.
The Garante episode is the argument for that centralisation, made by events.

And the annulment is the "as written, as enforced" beat at its sharpest: **Europe's most famous
enforcement action against a general-purpose model was overturned by a court.** An episode that
told only the fine and not the annulment would be telling the comfortable half.

---

## What this does to the coverage table

| Episode | Instance |
|---|---|
| Who you are in the picture | ✅ **Moffatt v Air Canada** |
| Standards and who writes the law | ✅ **Dieselgate** (primary) + **Boeing ODA** (delegation) |
| The weight of high risk | ✅ **Boeing ODA** carries the self-assessment question |
| General-purpose AI | ✅ **Garante v OpenAI**, including the annulment |

**All four gaps are now filled.** Two of the instances — Dieselgate and Boeing — are stronger than
the European AI-specific cases they replace, because they show the Act's own borrowed machinery
under load, with decades of aftermath to examine.

## New verification items for `04_gaps.md`

- Court of Rome annulment, 18 March 2026 — **single source, and an episode turns on it**.
- Garante decision date: 2 November 2024 versus December 2024 reporting.
- Art. 2 extraterritorial scope — exact wording.
- Art. 43 — which high-risk systems need a notified body and which are self-assessed.
- Moffatt citation 2024 BCCRT 149 and the damages figure.
- CJEU defeat-device rulings — case numbers and dates, not yet collected.
