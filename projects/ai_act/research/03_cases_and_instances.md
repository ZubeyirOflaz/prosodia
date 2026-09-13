# Docket 03 — Documented cases and opening instances  ·  compiled 2026-09-12

The persona **forbids invented controversies**. An episode without a real, documented instance
cannot be written as designed, which makes this the binding constraint on the whole series. Each
case below is given with what it can carry.

**All of these come from secondary sources.** Before an episode uses names, figures or dates aloud,
they need a primary check. Where a figure is contested, that is noted.

---

## 1. The Dutch childcare benefits scandal (*toeslagenaffaire*)

**Carries:** the definitional gate; risk scoring; what a rule assumes about a machine; the human
stakes that earn the `dramatic` tone.

**How the model worked.** From **2013** the Tax Administration ran a **risk-classification model**
in its childcare-benefits division, trained on examples of correct and incorrect applications, as a
**first filter**: officials then scrutinised the claims it labelled highest-risk. Its variables
included **dual nationality, low income, and whether the applicant's name read as non-Dutch**. What
turned a flawed model into a catastrophe was what surrounded it: civil servants treated a risk score
as grounds for **full suspension of benefits and aggressive clawback of years of past payments,
often with no explanation, no appeal pathway, and no evidence beyond the score itself**. Amnesty
International's report on it is titled *Xenophobic machines* (EUR 35/4686/2021).

Between **2005 and 2019** the Dutch Tax and Customs Administration wrongly accused roughly
**26,000 families** (some estimates say 35,000) of childcare-benefit fraud and demanded full
repayment — commonly **€20,000 to €60,000** per family. The risk-classification model treated
**dual nationality** and **foreign-sounding names** as fraud indicators; the families hit were
disproportionately of Moroccan, Turkish, Surinamese and Caribbean descent. **More than 1,100
children were placed in foster care** as a consequence. The **third Rutte cabinet resigned in
January 2021**. On **25 May 2022** the Dutch government admitted for the first time that
**institutional racism** in part of the Tax Administration was a root cause.

> **TRAP — do not conflate two different systems.** The benefits scandal involved the Tax
> Administration's **risk-classification model**. **SyRI** (*Systeem Risico Indicatie*) was a
> **separate** welfare-fraud system, struck down by **the District Court of The Hague in February
> 2020** as incompatible with Article 8 ECHR. Secondary sources blur them constantly. An episode
> that merges them is wrong, and a listener who knows the material will hear it. **Verify which
> system is being described before writing a word.**

## 2. Clearview AI

**Carries:** untargeted facial-image scraping; the as-written-against-as-enforced beat, better than
anything else in the docket.

A US company that scraped the open web for faces — it has claimed **more than 60 billion images** —
and sold facial recognition to law enforcement. **Five European authorities have fined it roughly
€105 million in total**: the Dutch AP **€30.5m** (2024), the Italian Garante **€20m** (Feb 2022),
the French CNIL **€20m** (Oct 2022, plus **€5.2m** in overdue-penalty payments), the Greek HDPA
**€20m** (July 2022), and the UK ICO **£7.5m** (2022). The Dutch authority found processing without
a legal basis under Arts. 5(1) and 6(1) GDPR and unlawful processing of biometric special-category
data under Art. 9(1).

**The reason this case is worth an episode: Clearview disputes EU jurisdiction and has not paid.**
Collection of every one of those fines remains contested. A hundred million euros of enforcement
that produced no money is the cleanest available illustration of the difference between a rule and
its enforcement.

## 3. The Dutch Crime Anticipation System (CAS)

**Carries:** predictive policing; and the persona's signature beat — what the rule assumes the
machine can do, against what it does.

The Netherlands was the **first country to deploy predictive policing nationally**. CAS was
**piloted from 2015, rolled out nationwide in 2017, and used until mid-December 2025**; the
discontinuation was reported in **February 2026**. *(An earlier version of this docket said 2019 —
wrong.)*

**How it actually worked**, which the signature beat needs: it produced **weekly** analyses on a
grid of small city areas, assigning each a risk score for the coming period, and its outputs were
"hot times" and "hotspots". It drew on **three data sources** — **BVI** (the central police crime
database), **GBA** (municipal administration) and **CBS** (Statistics Netherlands demographics) —
depersonalised and anonymised. It covered burglaries, car and bicycle theft, and nuisance. And
critically: **CAS was a closed system — officers could not see what data the model had used for any
particular prediction.**

**Why it was stopped.** The police concluded its operational value was unclear because **there were
no clear goals and no measurable success criteria**, and that in Amsterdam **only one incident in
fifty was correctly predicted**.

> Grid size: sources give both "125 square metres" and "125 by 125 metres". **Check the Dutch
> government Algorithm Register entry before stating a figure** —
> `algoritmes.overheid.nl/en/algoritme/81228922`, which is the official register and also a
> first-rate artefact for an episode in its own right.

**A decade of operational policing built on a system that could not do the thing it was named
after.** For an episode about a legal regime that classifies systems by their intended purpose,
this is the sharpest possible instance: the law asks what a system is *for*, and here the answer
turned out to be nothing.

## 4. Budapest Bank (Hungary, 2022)

**Carries:** the emotion-recognition prohibition, with a real deployment predating the ban.

**Case NAIH-85-3/2022** (antecedent NAIH-7350/2021). From **May 2018**, Budapest Bank ran
AI speech-signal processing over **customer service call recordings**, analysing keywords **and the
emotional state of the speaker**. The results were stored with the call, replayable for **45 days**,
and used to monitor call quality, pre-empt complaints, **rate the quality of the call-handling
staff's work**, and rank calls so the software could recommend which callers to contact first. The
Hungarian DPA opened an investigation in September 2021 and fined the bank **HUF 250 million —
about €665,000**, then the largest data-protection fine in Hungary. It found automated
decision-making and profiling with **no valid legal basis**, no proper balancing of interests and
inadequate safeguards, held that **only freely given informed consent** could ground emotion-based
voice analysis, and **ordered the bank to cease analysing emotions**.

> **The detail that makes this a "change one fact" case.** The people whose emotions were inferred
> were **customers**; the purpose included **evaluating employees**. Art. 5(1)(f) prohibits
> inferring emotions "in the areas of workplace and education institutions". Whose workplace, and
> does the prohibition follow the data subject or the setting? That is a genuinely hard question and
> this case sits exactly on it. *(An earlier version of this docket said "employees and customers" —
> imprecise.)* Decision on GDPRhub: `gdprhub.eu/NAIH_(Hungary)_-_NAIH-85-3/2022`.

## 5. Lighthouse Reports' welfare-scoring investigations

**Carries:** comparative material, and a supply of further instances.

An investigative series on predictive risk assessment in European welfare systems, reporting from
**the Netherlands, Spain, Denmark and Serbia**, finding discrimination, privacy intrusion and
design flaws. Useful as a source of additional documented cases — **each one needs verifying
individually**; the series is a lead, not a citation.

---

## Coverage against the planned episodes

| Episode | Instance available? |
|---|---|
| What counts as an AI system | ✅ CAS, or the benefits model — both test inference and autonomy |
| The red lines | ✅ Budapest Bank (emotion), Clearview (scraping) |
| Who you are in the picture | ⚠️ **no strong case yet** — a role-dispute instance is needed |
| The ladder of risk | ✅ the benefits scandal |
| The weight of high risk | ⚠️ **weak** — needs a documented conformity-assessment story |
| Standards | ⚠️ the CEN-CENELEC crisis is the instance, but it is institutional, not human |
| GPAI | ❌ **nothing documented yet** — the biggest hole in the docket |
| Enforcement | ✅ Clearview, outstandingly |

**Four of twelve episodes had no usable opening instance.** All four are now filled from outside
the EU's AI Act — see `05_foreign_instances.md`, which also carries the disclosure rule for
analysing a real case under a law that did not govern it.
