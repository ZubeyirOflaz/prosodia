# Docket 02 — The mass-surveillance cases  ·  compiled 2026-10-09

The five judgments the roadmap names — *Digital Rights Ireland*, *Schrems* I and II, *La Quadrature du
Net*, *Big Brother Watch* — plus the two that sit between them (*Tele2 Sverige/Watson*, *Centrum för
rättvisa*) and the one that continues *Schrems* (*Latombe*). For each: the people, the facts, the holding,
and **the proportionality reasoning, extracted step by step**, because the roadmap's condition for this
series is that proportionality is *taught*, not invoked.

**Provenance.**
- **Luxembourg cases:** the Court of Justice's own **press releases**, downloaded from `curia.europa.eu`
  on 2026-10-09 (PDFs under `experiments/eurlex/cache/curia/`, gitignored). Text in quotation marks below is
  **press-release wording — the Court's official summary, not the judgment**. ⚠ Before any of it is read
  aloud as *the Court's words*, take the passage from the judgment itself (EUR-Lex is behind a browser
  challenge since 2026-10; CELLAR content negotiation serves judgments — `publications.europa.eu/resource/celex/6YYYYCJNNNN`).
- **Strasbourg cases:** HUDOC refuses non-browser requests (HTTP 403), so *Big Brother Watch* and *Centrum
  för rättvisa* rest on **secondary sources** (Inforrm/Voorhoof, EU Law Analysis, Strasbourg Observers, EJIL:
  Talk!, European Law Blog), consistent with one another. ⚠ Read the judgment before quoting it.
- **Latombe:** practitioner and academic reports, mutually consistent; ⚠ not read in the original.
- Interpretive notes marked **›** are the compiler's.

---

## How the test runs — read this first

**Luxembourg (Charter Art. 52(1), docket `01`).** A limitation must (1) be **provided for by law**; (2)
**respect the essence** of the right — a floor, not a weight: if the essence is touched, the measure fails
without any balancing; (3) pursue an **objective of general interest** recognised by the Union (or protect
others' rights); (4) be **appropriate** to that objective; (5) be **necessary** — in this case law, *strictly*
necessary; and (6) not be disproportionate to the objective. **Where the interference is serious, the
legislature's discretion shrinks and the Court's review becomes strict** — that sentence in *Digital Rights
Ireland* is what turns the test from a formula into a constraint.

**Strasbourg (ECHR Arts. 8(2), 10(2), 11(2), docket `01`).** The interference must be **in accordance with
the law** — which includes the *quality* of the law: accessible, foreseeable, with safeguards against
arbitrariness — pursue a **listed legitimate aim**, and be **necessary in a democratic society**, with the
state allowed a **margin of appreciation**. For secret surveillance, most of the work happens at the first
step: the Court asks whether the law contains enough **safeguards**, not whether this particular
surveillance was justified.

› **The two courts ask different first questions.** Luxembourg tends to decide on *necessity*; Strasbourg
tends to decide on the *quality of the law*. A listener who knows that can predict how each case below will
come out — which is the transfer the persona wants.

---

## 1 · Digital Rights Ireland (2014) — the template

**Joined Cases C-293/12 and C-594/12, *Digital Rights Ireland Ltd* and *Kärntner Landesregierung and
Others*, Court of Justice (Grand Chamber), judgment of 8 April 2014.** Press release No 54/14.
*Verified: case numbers, parties, formation, date.*

**The people.** In Ireland, **Digital Rights Ireland**, an Irish company, against the Irish authorities. In
Austria, constitutional actions brought by the **Government of the Province of Carinthia** and by
*"Mr Seitlinger, Mr Tschohl and 11 128 other applicants"*.
› *Eleven thousand one hundred and thirty people sued over one directive* — a rare case where the applicants
are literally a crowd, and the episode can say so.

**The measure.** **Directive 2006/24/EC** required providers to retain **traffic and location data** —
who communicated with whom, by what means, when, from where, how often — for between **six and twenty-four
months**, for possible access by national authorities fighting serious crime. **Not content.**

**What the data reveals.** In the press release's words, the data "taken as a whole, may provide very
precise information on the private lives of the persons whose data are retained, such as the habits of
everyday life, permanent or temporary places of residence, daily or other movements, activities carried
out, social relationships and the social environments frequented" — and retention without the person
being told "is likely to generate in the persons concerned a feeling that their private lives are the
subject of constant surveillance."

**The proportionality reasoning, step by step.**

| step | answer | why |
|---|---|---|
| interference | **particularly serious** | retention plus authority access, across the whole population |
| essence | **not affected** | no knowledge of *content*; providers bound by data-security principles |
| objective | **legitimate** | fighting serious crime, "ultimately, public security" |
| scrutiny | **strict** | the seriousness of the interference reduces the legislature's discretion |
| appropriate | **yes** | retention may help attain the objective |
| strictly necessary | **no** | see below |

**Why it failed necessity** — four defects, each one a reusable test:
1. **Undifferentiated:** it covered "all individuals, all means of electronic communication and all traffic
   data without any differentiation, limitation or exception".
2. **No access criterion:** no objective criterion confining access to sufficiently serious crime — it
   deferred to "serious crime" as each Member State defined it — and **no prior review by a court or
   independent body**.
3. **Retention period:** 6–24 months with no distinction between categories of data or persons and no
   objective criteria for setting it.
4. **Safeguards:** security levels could be set with regard to **cost**; no irreversible destruction at
   the end of the period; and **no requirement to keep the data within the EU**, so independent oversight
   was not assured.

**Effect.** The directive was declared invalid **from the date it entered into force** — the Court did not
limit the temporal effect.

› **The template:** almost every later case is a variation on these four defects. Teach them once, here,
and the rest of the episode — and the rest of the series — becomes a matter of checking which one a new
measure repeats.

---

## 2 · Tele2 Sverige and Watson (2016) — the bridge

**Joined Cases C-203/15 and C-698/15, *Tele2 Sverige AB v Post- och telestyrelsen* and *Secretary of State
for the Home Department v Tom Watson and Others*, Court of Justice (Grand Chamber), 21 December 2016.**
Press release No 145/16. *Verified: case numbers, parties, date.*

After the directive fell, Member States kept their **national** retention laws. *Tele2* held that EU
law — the e-Privacy Directive, Art. 15(1), read with the Charter — **precludes national laws requiring
general and indiscriminate retention** of traffic and location data. ⚠ *The UK party, Tom Watson, was a
serving Labour MP; confirm the co-applicants before naming them.*

› **Use it in one sentence**: the Court said the same thing twice, once to the Union legislature and once
to the Member States — which is what made *La Quadrature du Net* necessary.

---

## 3 · La Quadrature du Net (2020) — the graduated answer, and the algorithms

**Joined Cases C-511/18, *La Quadrature du Net and Others*, C-512/18, *French Data Network and Others*, and
C-520/18, *Ordre des barreaux francophones et germanophone and Others*, Court of Justice (Grand Chamber),
6 October 2020** — delivered the same day as **C-623/17, *Privacy International*** (UK Investigatory Powers
Tribunal). Press release No 123/20. *Verified: all four case numbers, parties, date.*

**The people.** French digital-rights association **La Quadrature du Net** and others before the
**Conseil d'État**; the association of French- and German-speaking **Belgian bar associations** before the
**Belgian Constitutional Court**; **Privacy International** before the UK's **Investigatory Powers
Tribunal**.

**Why it came back.** After *Tele2*, in the press release's words, "certain States" feared they had "been
deprived of an instrument which they consider necessary to safeguard national security and to combat
crime." Several argued that **national security is outside EU law** (Art. 4(2) TEU). **The Court
disagreed:** laws obliging providers to retain or forward data for national-security purposes **fall within
the e-Privacy Directive**.

**The holding — not a ban but a ladder:**

| purpose | what is allowed |
|---|---|
| any purpose | **not** general and indiscriminate retention as a *preventive* measure — confirmed |
| a **serious threat to national security**, "genuine and present or foreseeable" | **general and indiscriminate retention**, for a period "limited in time to what is strictly necessary", renewable while the threat persists, **subject to effective review by a court or an independent administrative body whose decision is binding** |
| serious crime, serious threats to public security | **targeted retention**, limited by "objective and non-discriminatory factors" — categories of persons or **a geographical criterion** |
| any of the above | general retention of **IP addresses** (time-limited) and of **civil-identity data** (not time-limited); **expedited retention** ("quick freeze") once an offence is established or reasonably suspected |
| terrorism | **real-time collection** limited to persons with "a valid reason to suspect" involvement, with prior review |

**The machine, in the judgment.** Under the national-security condition, the directive "also does not
preclude **the automated analysis of the data**, inter alia traffic and location data, **of all users** of
means of electronic communication." That is France's 2015 intelligence-law **algorithmic analysis** —
the so-called *boîtes noires* (black boxes).
› **This is the series' hinge between surveillance law and AI**, and it is in a Grand Chamber judgment:
a court accepting automated screening of an entire population's metadata, conditionally.
⚠ **The conditions the judgment attaches to automated analysis** — widely reported as pre-established,
specific, reliable and non-discriminatory models and criteria, and individual non-automated re-examination
of any positive result — **are not in the press release and are not held here.** Read the judgment before
stating them. ⚠ The French intelligence law's provision and its year should be taken from the judgment's
recital of national law.

**Proportionality, extracted.** Same structure as *Digital Rights Ireland*, but the Court let the
**objective** set the **ceiling of permissible intrusion**: the graver the objective, the broader the
retention it can justify — national security above serious crime, serious crime above crime in general.
The ladder is proportionality turned into a table.

**Evidence obtained unlawfully.** Admissibility is for national law, but criminal courts must
**disregard** evidence from unlawful general retention where the accused "are not in a position to comment
effectively" on it.

› **For the held verdict:** this is the strongest evidence that proportionality *bends* when states push
back. The same Court that struck down general retention in 2014 and 2016 wrote, in 2020, the conditions
under which general retention — and population-wide automated analysis — is lawful. Constraint or
ratification? Both readings are available, and that is the point.

---

## 4 · Schrems I (2015) — the essence, as a floor

**Case C-362/14, *Maximillian Schrems v Data Protection Commissioner*, Court of Justice (Grand Chamber),
6 October 2015.** Press release No 117/15. *Verified.*

**The person.** **Maximillian Schrems**, "an Austrian citizen", a Facebook user **since 2008**. His data,
like that of other EU users, went from **Facebook's Irish subsidiary** to servers in the **United States**.
After **Edward Snowden's 2013 revelations** about the **NSA**, he complained to the **Irish Data Protection
Commissioner** that US law did not protect his data against public-authority surveillance. The
Commissioner rejected it: the Commission's **Safe Harbour Decision (2000/520/EC, 26 July 2000)** had already
found US protection adequate.

**The holding.** (a) A Commission adequacy decision **cannot remove or reduce** national supervisory
authorities' powers to examine a complaint; only the Court can declare the decision invalid, so authorities
and complainants must be able to get the question to it. (b) **The Safe Harbour Decision is invalid.**

**Proportionality — but the case turns on the step before it.**
- The Commission never found that the US ensured protection "**essentially equivalent**" to the EU's — it
  examined only the scheme, which bound **companies** and not **US public authorities**, and which yielded
  to US national security "without limitation".
- Legislation authorising "storage of all the personal data of all the persons whose data is transferred …
  without any differentiation, limitation or exception" is **not limited to what is strictly necessary** —
  the *Digital Rights Ireland* language, transported abroad.
- **The essence:** legislation permitting authorities "to have access on a generalised basis to the
  **content** of electronic communications must be regarded as **compromising the essence** of the
  fundamental right to respect for private life." And legislation giving the individual **no legal remedy**
  to access, rectify or erase their data "compromises the essence of the fundamental right to effective
  judicial protection."

› **The contrast to teach:** in *Digital Rights Ireland* the essence was *not* touched — no content — so
the Court had to weigh, and the measure failed necessity. In *Schrems I* the essence *was* touched —
content — so **no weighing was needed at all**. The essence is the one place in the test where nothing
is balanced. Episode-ready, and a direct answer to "is proportionality just a form?": not at the essence.

---

## 5 · Schrems II (2020) — the replacement falls too

**Case C-311/18, *Data Protection Commissioner v Facebook Ireland Ltd and Maximillian Schrems*, Court of
Justice (Grand Chamber), 16 July 2020.** Press release No 91/20. *Verified.*

**What happened in between.** After *Schrems I*, Mr Schrems **reformulated his complaint**: Facebook
Ireland now transferred data under **standard contractual clauses** (Commission Decision 2010/87). The
Irish authority took the question to the High Court, which referred it; meanwhile the Commission adopted the
**Privacy Shield** decision (**2016/1250**).

**The holding.** **Standard contractual clauses: valid** — because they oblige exporter and recipient to
**verify, before any transfer**, that the destination's protection is respected, and to **suspend** the
transfer when it is not. **Privacy Shield: invalid.**

**Proportionality, extracted.** Privacy Shield, "as did Decision 2000/520", gave US national security,
public interest and law enforcement **primacy**. The US limitations on access "are not circumscribed in a
way that satisfies requirements that are essentially equivalent to those required under EU law, by the
principle of proportionality, in so far as the surveillance programmes based on those provisions are **not
limited to what is strictly necessary**": for "certain surveillance programmes" the provisions "do not
indicate any limitations on the power they confer", nor guarantees for targeted **non-US persons**, and
they grant **no actionable rights before the courts**. **Article 47 (remedy):** the **Ombudsperson** was not
an independent body able to bind the intelligence services.
⚠ The press release does not name the programmes; reporting names **Section 702 FISA** and **Executive Order
12333**. Take the names from the judgment before saying them.

**What came next — still moving.** US **Executive Order 14086** (October 2022) and a third adequacy decision,
the **EU-US Data Privacy Framework** (Commission Implementing Decision (EU) **2023/1795**, July 2023).
Challenged by **Philippe Latombe**, a French member of parliament: **Case T-553/23, *Latombe v Commission*,
General Court, 3 September 2025 — action dismissed**, the framework upheld. ⚠ *Reported; the decision
number, the EO date and whether an appeal to the Court of Justice is pending as at the week of recording
must be checked — this is the moving part of the episode.*

› **For the held verdict:** two invalidations, then a validation by the lower court. Either the third
framework finally met the test — or the test has been made to fit. Lay out the sequence; let the listener
hold both.

---

## 6 · Big Brother Watch v the United Kingdom (2021) — Strasbourg's version

**Big Brother Watch and Others v. the United Kingdom, European Court of Human Rights (Grand Chamber),
applications nos. 58170/13, 62322/14 and 24960/15, judgment of 25 May 2021.** *Verified: name, formation,
application numbers, date.*

**The people.** Three joined applications brought by civil-liberties organisations, journalists and
human-rights groups — **Big Brother Watch** among them, and the **Bureau of Investigative Journalism**.
⚠ *Name individual applicants only after checking the judgment's list.*

**The measure.** The UK's historic **bulk interception** regime under **section 8(4) of the Regulation of
Investigatory Powers Act 2000**, revealed by the Snowden disclosures; the acquisition of communications
data from providers; and the **receipt of intelligence from foreign services**.

**The holding.** Bulk interception is **not in itself** incompatible with the Convention. But the regime
lacked **"end-to-end safeguards"** — necessity and proportionality assessed **at each stage**; **independent
authorisation at the outset**, when the operation's object and scope are defined; and **supervision and
independent ex post facto review**.
- **Violation of Article 8** (bulk interception): authorised by the **Secretary of State, not an independent
  body**; insufficient oversight of the **categories of selectors and search terms**; no prior internal
  authorisation for **selectors linked to an identifiable individual**. Also a violation for the
  acquisition of communications data from providers.
- **Violation of Article 10**: insufficient protection of **confidential journalistic material**.
- **No violation** for the receipt of intelligence from foreign partners.

**Same day: *Centrum för rättvisa v. Sweden* (Grand Chamber, application no. 35252/08).** A Swedish
public-interest law firm challenged Sweden's signals-intelligence regime. **Violation of Article 8 on three
specific gaps:** no clear rule on destroying intercepted material containing no personal data; no
requirement to weigh individuals' privacy before sharing material with foreign partners; no effective
ex post facto review. ⚠ *Application number from reporting; confirm.*

**Proportionality, extracted.** Strasbourg did **not** ask whether bulk interception was necessary — it
accepted that states may need it, within their **margin of appreciation**. It asked whether the **law around
it** was good enough. That is the "quality of the law" step doing the work Luxembourg does at "strictly
necessary".
› Critics read the pair as **normalising** mass surveillance — "The Grand Normalization of Mass Surveillance"
(EJIL: Talk!); "Opens the Gates of an Electronic 'Big Brother' in Europe" (Strasbourg Observers, quoting a
separate opinion ⚠). **Name those holders when the critique is voiced; check whose separate opinion the
quotation comes from.**

---

## For the planner — the series' evidence on the held verdict

› Compiler's reading, offered as material, not as the verdict:

| | what proportionality did |
|---|---|
| *Digital Rights Ireland* 2014 | struck down an EU directive outright, retroactively |
| *Schrems I* 2015 | found the **essence** violated — no balancing needed |
| *Tele2* 2016 | extended the prohibition to national law |
| *Schrems II* 2020 | struck down the replacement framework |
| *La Quadrature du Net* 2020 | **wrote the conditions** for general retention and population-wide automated analysis |
| *Big Brother Watch* 2021 | accepted bulk interception in principle; found the safeguards wanting |
| *Latombe* 2025 | the lower court upheld the third transatlantic framework |

The line bends **after states push back**, and it bends **toward procedure** — independent authorisation,
review, time limits — rather than toward prohibition. Whether that is proportionality working or
proportionality yielding is the verdict's question, and this table is its evidence.

---

## Still to research for this series

- **Predictive policing and biometric identification, with documented deployments** (which force, which
  system, which years, what happened): *Glukhin v. Russia* (ECtHR 2023, facial recognition and a lone
  protester); *R (Bridges) v Chief Constable of South Wales Police* (Court of Appeal, 2020); the German
  Federal Constitutional Court on automated data analysis in Hesse and Hamburg (February 2023);
  the Dutch *SyRI* welfare-fraud judgment (District Court of The Hague, February 2020); *Ligue des droits
  humains* (C-817/19, 2022, passenger-data risk profiling); Clearview AI enforcement.
- **Democracy and elections**: the Romanian Constitutional Court's annulment of the 2024 presidential first
  round; deepfakes in the 2023 Slovak election; Cambridge Analytica enforcement.
- **Emergency powers and derogation**: Art. 15 ECHR derogations (France 2015, Turkey 2016, the 2020
  pandemic notifications); France's algorithmic video surveillance law for the 2024 Olympics and what
  happened to its "experimental" end date.
- **The proportionality debate itself, with named holders** — the defenders (e.g. Aharon Barak, Robert
  Alexy) and the critics (e.g. Stavros Tsakyrakis) — for the lens episode.
- **Charter Arts. 11, 12, 21, 47, 48, 54** verbatim (docket `01`); **Protocol 15**'s preamble recital.
