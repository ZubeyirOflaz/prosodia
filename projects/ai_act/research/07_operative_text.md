# Docket 07 — Operative text, verbatim from EUR-Lex

**This file supersedes every other file in this docket wherever they overlap.** The rest of
the docket was built from secondary sources — law-firm summaries, the Commission's own
explanatory pages, artificialintelligenceact.eu. This is the Regulation itself.

| | |
|---|---|
| Source | EUR-Lex consolidated text, CELEX **02024R1689-20260727** |
| URL | `https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02024R1689-20260727` |
| Version | `02024R1689 — EN — 27.07.2026 — 001.001` |
| Base act | Regulation (EU) 2024/1689 (OJ L, 12.7.2024) |
| Amended by | **Regulation (EU) 2026/1744 of 8 July 2026** (OJ L 1744, p. 1, 24.7.2026) — the only amendment to date |
| Retrieved | 2026-09-13 |
| Extracted text | sha256 `8e9a265395b0eb333bf2a2b813d688d566192266d05bc692deb56a52a739cf4d` |
| Tool | `experiments/eurlex/consolidate.py 02024R1689-20260727` |

**On provenance.** The served HTML carries a per-request analytics id, so its hash is not
stable and is not quoted here. Two independent fetches were converted and produced
byte-identical text; the hash above is of that text. The converter reports, for every
article and annex, whether it rendered all of the source's words — this extraction reported
no loss anywhere. That check is not decoration: an earlier pass silently dropped the
Annex III 1(a) carve-out and the whole of Article 26(5), and rendered the Article 51(2)
compute threshold as "1025" instead of 10^25.

**Consolidation markers.** `[▼M1]` marks text as amended by Regulation (EU) 2026/1744;
`[▼B]` marks a return to the original 2024 wording. They are left in place so an episode
can say which wording it is quoting. EUR-Lex's own caveat applies: a consolidated text is a
documentation tool with no legal effect, and the authentic text is the OJ.

**Recitals are not here.** A consolidated text omits the preamble. Where an episode needs a
recital, take it from the original OJ text of 2024/1689 and cite it as a recital, not as an
operative provision.

---

## What the 2026 amendment did — structurally

Entirely new provisions inserted by Regulation (EU) 2026/1744, present in the consolidated
text and absent from every other file in this docket:

- **Article 4a** — processing of special categories of personal data for bias detection and
  correction.
- **Article 60a** — real-world testing of high-risk systems covered by Annex I Section B
  legislation, outside sandboxes.
- **Articles 75a–75d** — the AI Office's own supervisory and enforcement powers:
  commitments (75b), non-compliance, fines and periodic penalty payments (75c), and
  safeguards (75d). **This is the provision base for any claim about who can fine whom**,
  and it did not exist when the enforcement material in `04_gaps.md` §8 was written.
- **Article 5(1)(ba) and (bb)** — two new prohibitions.
- **Annex XIV** — codes and categories for the notified-body designation procedure
  (Article 30).

Thirty-seven articles and annexes carry `[▼M1]` amended text. That list is derived from
marker positions and can be off by one article at a boundary, so treat it as a pointer, not
a citation: Articles 1, 2, 3, 5, 6, 10, 11, 17, 25, 27, 28, 29, 30, 40, 42, 43, 50, 56, 57,
58, 60, 63, 64, 69, 70, 72, 75, 76, 77, 95, 96, 97, 99, 111, 113, and Annexes I and VIII.

---

# The text

Each block below is verbatim. Paragraph numbers, point letters and nesting are the
Regulation's own, so anything here can be quoted with its citation.


## Article 3 — Definitions

> **Why it is here.** Gap 20. **Correction to the gap as written:** the training-compute criterion is NOT in the definition. Article 3(63) defines a general-purpose AI model by generality and task range only; the 10^25 floating-point-operation threshold lives in **Article 51(2)**, as a rebuttable presumption of high-impact capability, and is amendable by delegated act under Article 51(3). An episode that puts the number in the definition has the architecture wrong.

```text
(63) ‘general-purpose AI model’ means an AI model, including where such an AI model is trained with a large amount of data using self-supervision at scale, that displays significant generality and is capable of competently performing a wide range of distinct tasks regardless of the way the model is placed on the market and that can be integrated into a variety of downstream systems or applications, except AI models that are used for research, development or prototyping activities before they are placed on the market;
(64) ‘high-impact capabilities’ means capabilities that match or exceed the capabilities recorded in the most advanced general-purpose AI models;
(65) ‘systemic risk’ means a risk that is specific to the high-impact capabilities of general-purpose AI models, having a significant impact on the Union market due to their reach, or due to actual or reasonably foreseeable negative effects on public health, safety, public security, fundamental rights, or the society as a whole, that can be propagated at scale across the value chain;
(66) ‘general-purpose AI system’ means an AI system which is based on a general-purpose AI model and which has the capability to serve a variety of purposes, both for direct use as well as for integration in other AI systems;
(67) ‘floating-point operation’ means any mathematical operation or assignment involving floating-point numbers, which are a subset of the real numbers typically represented on computers by an integer of fixed precision scaled by an integer exponent of a fixed base;
```

### Article 51 — where the threshold actually is

```text
1. A general-purpose AI model shall be classified as a general-purpose AI model with systemic risk if it meets any of the following conditions:
    (a) it has high impact capabilities evaluated on the basis of appropriate technical tools and methodologies, including indicators and benchmarks;
    (b) based on a decision of the Commission, ex officio or following a qualified alert from the scientific panel, it has capabilities or an impact equivalent to those set out in point (a) having regard to the criteria set out in Annex XIII.
2. A general-purpose AI model shall be presumed to have high impact capabilities pursuant to paragraph 1, point (a), when the cumulative amount of computation used for its training measured in floating point operations is greater than 10^25.
3. The Commission shall adopt delegated acts in accordance with Article 97 to amend the thresholds listed in paragraphs 1 and 2 of this Article, as well as to supplement benchmarks and indicators in light of evolving technological developments, such as algorithmic improvements or increased hardware efficiency, when necessary, for these thresholds to reflect the state of the art.
```

## Article 5 — Prohibited AI practices

> **Why it is here.** Gap 23 — **Article 5(1)(g) is in here**, and the plan never taught it. Also carries the two new prohibitions, (ba) and (bb). The version in `06` is second-hand; this one is the text.

```text
1. The following AI practices shall be prohibited:
    (a) the placing on the market, the putting into service or the use of an AI system that deploys subliminal techniques beyond a person’s consciousness or purposefully manipulative or deceptive techniques, with the objective, or the effect of materially distorting the behaviour of a person or a group of persons by appreciably impairing their ability to make an informed decision, thereby causing them to take a decision that they would not have otherwise taken in a manner that causes or is reasonably likely to cause that person, another person or group of persons significant harm;
    (b) the placing on the market, the putting into service or the use of an AI system that exploits any of the vulnerabilities of a natural person or a specific group of persons due to their age, disability or a specific social or economic situation, with the objective, or the effect, of materially distorting the behaviour of that person or a person belonging to that group in a manner that causes or is reasonably likely to cause that person or another person significant harm;
[▼M1]
    (ba) the placing on the market, the putting into service or the use of an AI system that generates or manipulates realistic images, videos, audio or similar material of an identifiable natural person’s intimate parts, or of an identifiable natural person engaged in sexually explicit activities, without that person’s freely-given, specific, informed, unambiguous and explicit consent for that generation or manipulation;
    (bb) the placing on the market, the putting into service or the use of an AI system that generates or manipulates material or performance within the meaning of Article 2, points (c) and (e), of Directive 2011/93/EU, except where a ‘without right’ defence applies under national law;
[▼B]
    (c) the placing on the market, the putting into service or the use of AI systems for the evaluation or classification of natural persons or groups of persons over a certain period of time based on their social behaviour or known, inferred or predicted personal or personality characteristics, with the social score leading to either or both of the following:
        (i) detrimental or unfavourable treatment of certain natural persons or groups of persons in social contexts that are unrelated to the contexts in which the data was originally generated or collected;
        (ii) detrimental or unfavourable treatment of certain natural persons or groups of persons that is unjustified or disproportionate to their social behaviour or its gravity;
    (d) the placing on the market, the putting into service for this specific purpose, or the use of an AI system for making risk assessments of natural persons in order to assess or predict the risk of a natural person committing a criminal offence, based solely on the profiling of a natural person or on assessing their personality traits and characteristics; this prohibition shall not apply to AI systems used to support the human assessment of the involvement of a person in a criminal activity, which is already based on objective and verifiable facts directly linked to a criminal activity;
    (e) the placing on the market, the putting into service for this specific purpose, or the use of AI systems that create or expand facial recognition databases through the untargeted scraping of facial images from the internet or CCTV footage;
    (f) the placing on the market, the putting into service for this specific purpose, or the use of AI systems to infer emotions of a natural person in the areas of workplace and education institutions, except where the use of the AI system is intended to be put in place or into the market for medical or safety reasons;
    (g) the placing on the market, the putting into service for this specific purpose, or the use of biometric categorisation systems that categorise individually natural persons based on their biometric data to deduce or infer their race, political opinions, trade union membership, religious or philosophical beliefs, sex life or sexual orientation; this prohibition does not cover any labelling or filtering of lawfully acquired biometric datasets, such as images, based on biometric data or categorizing of biometric data in the area of law enforcement;
    (h) the use of ‘real-time’ remote biometric identification systems in publicly accessible spaces for the purposes of law enforcement, unless and in so far as such use is strictly necessary for one of the following objectives:
        (i) the targeted search for specific victims of abduction, trafficking in human beings or sexual exploitation of human beings, as well as the search for missing persons;
        (ii) the prevention of a specific, substantial and imminent threat to the life or physical safety of natural persons or a genuine and present or genuine and foreseeable threat of a terrorist attack;
        (iii) the localisation or identification of a person suspected of having committed a criminal offence, for the purpose of conducting a criminal investigation or prosecution or executing a criminal penalty for offences referred to in Annex II and punishable in the Member State concerned by a custodial sentence or a detention order for a maximum period of at least four years.
Point (h) of the first subparagraph is without prejudice to Article 9 of Regulation (EU) 2016/679 for the processing of biometric data for purposes other than law enforcement.
[▼M1]
1a. For the purposes of paragraph 1, first subparagraph, points (ba) and (bb):
    (a) the placing on the market or putting into service of an AI system that generates or manipulates the material or performance referred to in paragraph 1, first subparagraph, point (ba) or (bb) is only prohibited where:
        (i) that generation or manipulation is the intended purpose of the AI system; or
        (ii) the system’s design, training, architecture, capabilities or user-facing functionalities make that generation or manipulation a reasonably foreseeable and reproducible outcome, without requiring significant technical modification, and the system does not have reasonable and adequate technical safety measures and other safeguards to reliably prevent that generation or manipulation, taking into account reasonably foreseeable misuse, and to correct observed or reported misuse;
    (b) the use of an AI system that generates or manipulates the material or performance referred to in paragraph 1, first subparagraph, points (ba) and (bb) is only prohibited where the deployer uses the system for the purpose of generating or manipulating such material or performance.
1b. For the purposes of paragraph 1, first subparagraph, point (ba), an AI system that manipulates material in a way that does not increase the exposure of any depicted intimate parts or alter the nature of any depicted sexually explicit activities shall not constitute manipulation.
[▼B]
2. The use of ‘real-time’ remote biometric identification systems in publicly accessible spaces for the purposes of law enforcement for any of the objectives referred to in paragraph 1, first subparagraph, point (h), shall be deployed for the purposes set out in that point only to confirm the identity of the specifically targeted individual, and it shall take into account the following elements:
    (a) the nature of the situation giving rise to the possible use, in particular the seriousness, probability and scale of the harm that would be caused if the system were not used;
    (b) the consequences of the use of the system for the rights and freedoms of all persons concerned, in particular the seriousness, probability and scale of those consequences.
In addition, the use of ‘real-time’ remote biometric identification systems in publicly accessible spaces for the purposes of law enforcement for any of the objectives referred to in paragraph 1, first subparagraph, point (h), of this Article shall comply with necessary and proportionate safeguards and conditions in relation to the use in accordance with the national law authorising the use thereof, in particular as regards the temporal, geographic and personal limitations. The use of the ‘real-time’ remote biometric identification system in publicly accessible spaces shall be authorised only if the law enforcement authority has completed a fundamental rights impact assessment as provided for in Article 27 and has registered the system in the EU database according to Article 49. However, in duly justified cases of urgency, the use of such systems may be commenced without the registration in the EU database, provided that such registration is completed without undue delay.
3. For the purposes of paragraph 1, first subparagraph, point (h) and paragraph 2, each use for the purposes of law enforcement of a ‘real-time’ remote biometric identification system in publicly accessible spaces shall be subject to a prior authorisation granted by a judicial authority or an independent administrative authority whose decision is binding of the Member State in which the use is to take place, issued upon a reasoned request and in accordance with the detailed rules of national law referred to in paragraph 5. However, in a duly justified situation of urgency, the use of such system may be commenced without an authorisation provided that such authorisation is requested without undue delay, at the latest within 24 hours. If such authorisation is rejected, the use shall be stopped with immediate effect and all the data, as well as the results and outputs of that use shall be immediately discarded and deleted.
The competent judicial authority or an independent administrative authority whose decision is binding shall grant the authorisation only where it is satisfied, on the basis of objective evidence or clear indications presented to it, that the use of the ‘real-time’ remote biometric identification system concerned is necessary for, and proportionate to, achieving one of the objectives specified in paragraph 1, first subparagraph, point (h), as identified in the request and, in particular, remains limited to what is strictly necessary concerning the period of time as well as the geographic and personal scope. In deciding on the request, that authority shall take into account the elements referred to in paragraph 2. No decision that produces an adverse legal effect on a person may be taken based solely on the output of the ‘real-time’ remote biometric identification system.
4. Without prejudice to paragraph 3, each use of a ‘real-time’ remote biometric identification system in publicly accessible spaces for law enforcement purposes shall be notified to the relevant market surveillance authority and the national data protection authority in accordance with the national rules referred to in paragraph 5. The notification shall, as a minimum, contain the information specified under paragraph 6 and shall not include sensitive operational data.
5. A Member State may decide to provide for the possibility to fully or partially authorise the use of ‘real-time’ remote biometric identification systems in publicly accessible spaces for the purposes of law enforcement within the limits and under the conditions listed in paragraph 1, first subparagraph, point (h), and paragraphs 2 and 3. Member States concerned shall lay down in their national law the necessary detailed rules for the request, issuance and exercise of, as well as supervision and reporting relating to, the authorisations referred to in paragraph 3. Those rules shall also specify in respect of which of the objectives listed in paragraph 1, first subparagraph, point (h), including which of the criminal offences referred to in point (h)(iii) thereof, the competent authorities may be authorised to use those systems for the purposes of law enforcement. Member States shall notify those rules to the Commission at the latest 30 days following the adoption thereof. Member States may introduce, in accordance with Union law, more restrictive laws on the use of remote biometric identification systems.
6. National market surveillance authorities and the national data protection authorities of Member States that have been notified of the use of ‘real-time’ remote biometric identification systems in publicly accessible spaces for law enforcement purposes pursuant to paragraph 4 shall submit to the Commission annual reports on such use. For that purpose, the Commission shall provide Member States and national market surveillance and data protection authorities with a template, including information on the number of the decisions taken by competent judicial authorities or an independent administrative authority whose decision is binding upon requests for authorisations in accordance with paragraph 3 and their result.
7. The Commission shall publish annual reports on the use of real-time remote biometric identification systems in publicly accessible spaces for law enforcement purposes, based on aggregated data in Member States on the basis of the annual reports referred to in paragraph 6. Those annual reports shall not include sensitive operational data of the related law enforcement activities.
8. This Article shall not affect the prohibitions that apply where an AI practice infringes other Union law.
```

## Article 6 — Classification rules for high-risk AI systems

> **Why it is here.** Gap 22 — the classification rules, including the 6(3) derogation and its profiling carve-out.

```text
1. Irrespective of whether an AI system is placed on the market or put into service independently of the products referred to in points (a) and (b), that AI system shall be considered to be high-risk where both of the following conditions are fulfilled:
    (a) the AI system is intended to be used as a safety component of a product, or the AI system is itself a product, covered by the Union harmonisation legislation listed in Annex I;
    (b) the product whose safety component pursuant to point (a) is the AI system, or the AI system itself as a product, is required to undergo a third-party conformity assessment, with a view to the placing on the market or the putting into service of that product pursuant to the Union harmonisation legislation listed in Annex I.
[▼M1]
1a. For the purposes of this Regulation, including paragraph 1 of this Article, AI systems that are solely used for non-safety related aspects of user assistance, performance optimisation, service efficiency, automation or convenience or quality control shall not qualify as safety components.
1b. Notwithstanding paragraph 1a, AI systems the failure or malfunctioning of which would endanger health and safety shall qualify as safety components.
1c. A product that is required to undergo a third-party conformity assessment solely due to risks other than risks to health and safety, in particular risks relating to the distribution of radio spectrum or electromagnetic interference that do not affect health and safety, shall not be considered as fulfilling the condition in paragraph 1, point (b).
[▼B]
2. In addition to the high-risk AI systems referred to in paragraph 1, AI systems referred to in Annex III shall be considered to be high-risk.
3. By derogation from paragraph 2, an AI system referred to in Annex III shall not be considered to be high-risk where it does not pose a significant risk of harm to the health, safety or fundamental rights of natural persons, including by not materially influencing the outcome of decision making.
The first subparagraph shall apply where any of the following conditions is fulfilled:
    (a) the AI system is intended to perform a narrow procedural task;
    (b) the AI system is intended to improve the result of a previously completed human activity;
    (c) the AI system is intended to detect decision-making patterns or deviations from prior decision-making patterns and is not meant to replace or influence the previously completed human assessment, without proper human review; or
    (d) the AI system is intended to perform a preparatory task to an assessment relevant for the purposes of the use cases listed in Annex III.
Notwithstanding the first subparagraph, an AI system referred to in Annex III shall always be considered to be high-risk where the AI system performs profiling of natural persons.
4. A provider who considers that an AI system referred to in Annex III is not high-risk shall document its assessment before that system is placed on the market or put into service. Such provider shall be subject to the registration obligation set out in Article 49(2). Upon request of national competent authorities, the provider shall provide the documentation of the assessment.
5. The Commission shall, after consulting the European Artificial Intelligence Board (the ‘Board’), and no later than 2 February 2026, provide guidelines specifying the practical implementation of this Article in line with Article 96 together with a comprehensive list of practical examples of use cases of AI systems that are high-risk and not high-risk.
6. The Commission is empowered to adopt delegated acts in accordance with Article 97 in order to amend paragraph 3, second subparagraph, of this Article by adding new conditions to those laid down therein, or by modifying them, where there is concrete and reliable evidence of the existence of AI systems that fall under the scope of Annex III, but do not pose a significant risk of harm to the health, safety or fundamental rights of natural persons.
7. The Commission shall adopt delegated acts in accordance with Article 97 in order to amend paragraph 3, second subparagraph, of this Article by deleting any of the conditions laid down therein, where there is concrete and reliable evidence that this is necessary to maintain the level of protection of health, safety and fundamental rights provided for by this Regulation.
8. Any amendment to the conditions laid down in paragraph 3, second subparagraph, adopted in accordance with paragraphs 6 and 7 of this Article shall not decrease the overall level of protection of health, safety and fundamental rights provided for by this Regulation and shall ensure consistency with the delegated acts adopted pursuant to Article 7(1), and take account of market and technological developments.
```

## ANNEX III — High-risk AI systems referred to in Article 6(2)

> **Why it is here.** Gap 24 — all eight points, enumerated, with their sub-points.

```text
High-risk AI systems pursuant to Article 6(2) are the AI systems listed in any of the following areas:
    1. Biometrics, in so far as their use is permitted under relevant Union or national law:
        (a) remote biometric identification systems.
        This shall not include AI systems intended to be used for biometric verification the sole purpose of which is to confirm that a specific natural person is the person he or she claims to be;
        (b) AI systems intended to be used for biometric categorisation, according to sensitive or protected attributes or characteristics based on the inference of those attributes or characteristics;
        (c) AI systems intended to be used for emotion recognition.
    2. Critical infrastructure: AI systems intended to be used as safety components in the management and operation of critical digital infrastructure, road traffic, or in the supply of water, gas, heating or electricity.
    3. Education and vocational training:
        (a) AI systems intended to be used to determine access or admission or to assign natural persons to educational and vocational training institutions at all levels;
        (b) AI systems intended to be used to evaluate learning outcomes, including when those outcomes are used to steer the learning process of natural persons in educational and vocational training institutions at all levels;
        (c) AI systems intended to be used for the purpose of assessing the appropriate level of education that an individual will receive or will be able to access, in the context of or within educational and vocational training institutions at all levels;
        (d) AI systems intended to be used for monitoring and detecting prohibited behaviour of students during tests in the context of or within educational and vocational training institutions at all levels.
    4. Employment, workers’ management and access to self-employment:
        (a) AI systems intended to be used for the recruitment or selection of natural persons, in particular to place targeted job advertisements, to analyse and filter job applications, and to evaluate candidates;
        (b) AI systems intended to be used to make decisions affecting terms of work-related relationships, the promotion or termination of work-related contractual relationships, to allocate tasks based on individual behaviour or personal traits or characteristics or to monitor and evaluate the performance and behaviour of persons in such relationships.
    5. Access to and enjoyment of essential private services and essential public services and benefits:
        (a) AI systems intended to be used by public authorities or on behalf of public authorities to evaluate the eligibility of natural persons for essential public assistance benefits and services, including healthcare services, as well as to grant, reduce, revoke, or reclaim such benefits and services;
        (b) AI systems intended to be used to evaluate the creditworthiness of natural persons or establish their credit score, with the exception of AI systems used for the purpose of detecting financial fraud;
        (c) AI systems intended to be used for risk assessment and pricing in relation to natural persons in the case of life and health insurance;
        (d) AI systems intended to evaluate and classify emergency calls by natural persons or to be used to dispatch, or to establish priority in the dispatching of, emergency first response services, including by police, firefighters and medical aid, as well as of emergency healthcare patient triage systems.
    6. Law enforcement, in so far as their use is permitted under relevant Union or national law:
        (a) AI systems intended to be used by or on behalf of law enforcement authorities, or by Union institutions, bodies, offices or agencies in support of law enforcement authorities or on their behalf to assess the risk of a natural person becoming the victim of criminal offences;
        (b) AI systems intended to be used by or on behalf of law enforcement authorities or by Union institutions, bodies, offices or agencies in support of law enforcement authorities as polygraphs or similar tools;
        (c) AI systems intended to be used by or on behalf of law enforcement authorities, or by Union institutions, bodies, offices or agencies, in support of law enforcement authorities to evaluate the reliability of evidence in the course of the investigation or prosecution of criminal offences;
        (d) AI systems intended to be used by law enforcement authorities or on their behalf or by Union institutions, bodies, offices or agencies in support of law enforcement authorities for assessing the risk of a natural person offending or re-offending not solely on the basis of the profiling of natural persons as referred to in Article 3(4) of Directive (EU) 2016/680, or to assess personality traits and characteristics or past criminal behaviour of natural persons or groups;
        (e) AI systems intended to be used by or on behalf of law enforcement authorities or by Union institutions, bodies, offices or agencies in support of law enforcement authorities for the profiling of natural persons as referred to in Article 3(4) of Directive (EU) 2016/680 in the course of the detection, investigation or prosecution of criminal offences.
    7. Migration, asylum and border control management, in so far as their use is permitted under relevant Union or national law:
        (a) AI systems intended to be used by or on behalf of competent public authorities or by Union institutions, bodies, offices or agencies as polygraphs or similar tools;
        (b) AI systems intended to be used by or on behalf of competent public authorities or by Union institutions, bodies, offices or agencies to assess a risk, including a security risk, a risk of irregular migration, or a health risk, posed by a natural person who intends to enter or who has entered into the territory of a Member State;
        (c) AI systems intended to be used by or on behalf of competent public authorities or by Union institutions, bodies, offices or agencies to assist competent public authorities for the examination of applications for asylum, visa or residence permits and for associated complaints with regard to the eligibility of the natural persons applying for a status, including related assessments of the reliability of evidence;
        (d) AI systems intended to be used by or on behalf of competent public authorities, or by Union institutions, bodies, offices or agencies, in the context of migration, asylum or border control management, for the purpose of detecting, recognising or identifying natural persons, with the exception of the verification of travel documents.
    8. Administration of justice and democratic processes:
        (a) AI systems intended to be used by a judicial authority or on their behalf to assist a judicial authority in researching and interpreting facts and the law and in applying the law to a concrete set of facts, or to be used in a similar way in alternative dispute resolution;
        (b) AI systems intended to be used for influencing the outcome of an election or referendum or the voting behaviour of natural persons in the exercise of their vote in elections or referenda. This does not include AI systems to the output of which natural persons are not directly exposed, such as tools used to organise, optimise or structure political campaigns from an administrative or logistical point of view.
```

## Article 9 — Risk management system

> **Why it is here.** Gap 21 — risk management.

```text
1. A risk management system shall be established, implemented, documented and maintained in relation to high-risk AI systems.
2. The risk management system shall be understood as a continuous iterative process planned and run throughout the entire lifecycle of a high-risk AI system, requiring regular systematic review and updating. It shall comprise the following steps:
    (a) the identification and analysis of the known and the reasonably foreseeable risks that the high-risk AI system can pose to health, safety or fundamental rights when the high-risk AI system is used in accordance with its intended purpose;
    (b) the estimation and evaluation of the risks that may emerge when the high-risk AI system is used in accordance with its intended purpose, and under conditions of reasonably foreseeable misuse;
    (c) the evaluation of other risks possibly arising, based on the analysis of data gathered from the post-market monitoring system referred to in Article 72;
    (d) the adoption of appropriate and targeted risk management measures designed to address the risks identified pursuant to point (a).
3. The risks referred to in this Article shall concern only those which may be reasonably mitigated or eliminated through the development or design of the high-risk AI system, or the provision of adequate technical information.
4. The risk management measures referred to in paragraph 2, point (d), shall give due consideration to the effects and possible interaction resulting from the combined application of the requirements set out in this Section, with a view to minimising risks more effectively while achieving an appropriate balance in implementing the measures to fulfil those requirements.
5. The risk management measures referred to in paragraph 2, point (d), shall be such that the relevant residual risk associated with each hazard, as well as the overall residual risk of the high-risk AI systems is judged to be acceptable.
In identifying the most appropriate risk management measures, the following shall be ensured:
    (a) elimination or reduction of risks identified and evaluated pursuant to paragraph 2 in as far as technically feasible through adequate design and development of the high-risk AI system;
    (b) where appropriate, implementation of adequate mitigation and control measures addressing risks that cannot be eliminated;
    (c) provision of information required pursuant to Article 13 and, where appropriate, training to deployers.
With a view to eliminating or reducing risks related to the use of the high-risk AI system, due consideration shall be given to the technical knowledge, experience, education, the training to be expected by the deployer, and the presumable context in which the system is intended to be used.
6. High-risk AI systems shall be tested for the purpose of identifying the most appropriate and targeted risk management measures. Testing shall ensure that high-risk AI systems perform consistently for their intended purpose and that they are in compliance with the requirements set out in this Section.
7. Testing procedures may include testing in real-world conditions in accordance with Article 60.
8. The testing of high-risk AI systems shall be performed, as appropriate, at any time throughout the development process, and, in any event, prior to their being placed on the market or put into service. Testing shall be carried out against prior defined metrics and probabilistic thresholds that are appropriate to the intended purpose of the high-risk AI system.
9. When implementing the risk management system as provided for in paragraphs 1 to 7, providers shall give consideration to whether in view of its intended purpose the high-risk AI system is likely to have an adverse impact on persons under the age of 18 and, as appropriate, other vulnerable groups.
10. For providers of high-risk AI systems that are subject to requirements regarding internal risk management processes under other relevant provisions of Union law, the aspects provided in paragraphs 1 to 9 may be part of, or combined with, the risk management procedures established pursuant to that law.
```

## Article 10 — Data and data governance

> **Why it is here.** Gap 21 — data and data governance.

```text
[▼M1]
1. High-risk AI systems which make use of techniques involving the training of AI models with data shall be developed on the basis of training, validation and testing data sets that meet the quality criteria referred to in paragraphs 2, 3 and 4 of this Article and in Article 4a(1) whenever such data sets are used.
[▼B]
2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular:
    (a) the relevant design choices;
    (b) data collection processes and the origin of data, and in the case of personal data, the original purpose of the data collection;
    (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment and aggregation;
    (d) the formulation of assumptions, in particular with respect to the information that the data are supposed to measure and represent;
    (e) an assessment of the availability, quantity and suitability of the data sets that are needed;
    (f) examination in view of possible biases that are likely to affect the health and safety of persons, have a negative impact on fundamental rights or lead to discrimination prohibited under Union law, especially where data outputs influence inputs for future operations;
    (g) appropriate measures to detect, prevent and mitigate possible biases identified according to point (f);
    (h) the identification of relevant data gaps or shortcomings that prevent compliance with this Regulation, and how those gaps and shortcomings can be addressed.
3. Training, validation and testing data sets shall be relevant, sufficiently representative, and to the best extent possible, free of errors and complete in view of the intended purpose. They shall have the appropriate statistical properties, including, where applicable, as regards the persons or groups of persons in relation to whom the high-risk AI system is intended to be used. Those characteristics of the data sets may be met at the level of individual data sets or at the level of a combination thereof.
4. Data sets shall take into account, to the extent required by the intended purpose, the characteristics or elements that are particular to the specific geographical, contextual, behavioural or functional setting within which the high-risk AI system is intended to be used.
[▼M1 —————]
[▼M1]
6. For the development of high-risk AI systems not using techniques involving the training of AI models, paragraphs 2, 3 and 4 of this Article and Article 4a(1) shall apply only to the testing data sets.
[▼B]
```

## Article 11 — Technical documentation

> **Why it is here.** Gap 21 — technical documentation.

```text
1. The technical documentation of a high-risk AI system shall be drawn up before that system is placed on the market or put into service and shall be kept up-to date.
[▼M1]
That technical documentation shall be drawn up in such a way as to demonstrate that the high-risk AI system complies with the requirements set out in this Section and to provide national competent authorities and notified bodies with the necessary information in a clear and comprehensive form to assess the compliance of the AI system with those requirements. It shall contain, at a minimum, the elements set out in Annex IV. SMEs, including start-ups, and SMCs, may provide the elements of the technical documentation specified in Annex IV in a simplified manner. To that end, the Commission shall establish a simplified technical documentation form targeted at the needs of SMEs, including start-ups, and SMCs. Where an SME, including a start-up, or an SMC, opts to provide the information required in Annex IV in a simplified manner, it shall use the form referred to in this paragraph. Notified bodies shall accept the form for the purposes of the conformity assessment.
[▼B]
2. Where a high-risk AI system related to a product covered by the Union harmonisation legislation listed in Section A of Annex I is placed on the market or put into service, a single set of technical documentation shall be drawn up containing all the information set out in paragraph 1, as well as the information required under those legal acts.
3. The Commission is empowered to adopt delegated acts in accordance with Article 97 in order to amend Annex IV, where necessary, to ensure that, in light of technical progress, the technical documentation provides all the information necessary to assess the compliance of the system with the requirements set out in this Section.
```

## Article 12 — Record-keeping

> **Why it is here.** Gap 21 — record-keeping.

```text
1. High-risk AI systems shall technically allow for the automatic recording of events (logs) over the lifetime of the system.
2. In order to ensure a level of traceability of the functioning of a high-risk AI system that is appropriate to the intended purpose of the system, logging capabilities shall enable the recording of events relevant for:
    (a) identifying situations that may result in the high-risk AI system presenting a risk within the meaning of Article 79(1) or in a substantial modification;
    (b) facilitating the post-market monitoring referred to in Article 72; and
    (c) monitoring the operation of high-risk AI systems referred to in Article 26(5).
3. For high-risk AI systems referred to in point 1 (a), of Annex III, the logging capabilities shall provide, at a minimum:
    (a) recording of the period of each use of the system (start date and time and end date and time of each use);
    (b) the reference database against which input data has been checked by the system;
    (c) the input data for which the search has led to a match;
    (d) the identification of the natural persons involved in the verification of the results, as referred to in Article 14(5).
```

## Article 13 — Transparency and provision of information to deployers

> **Why it is here.** Gap 21 — transparency to the deployer.

```text
1. High-risk AI systems shall be designed and developed in such a way as to ensure that their operation is sufficiently transparent to enable deployers to interpret a system’s output and use it appropriately. An appropriate type and degree of transparency shall be ensured with a view to achieving compliance with the relevant obligations of the provider and deployer set out in Section 3.
2. High-risk AI systems shall be accompanied by instructions for use in an appropriate digital format or otherwise that include concise, complete, correct and clear information that is relevant, accessible and comprehensible to deployers.
3. The instructions for use shall contain at least the following information:
    (a) the identity and the contact details of the provider and, where applicable, of its authorised representative;
    (b) the characteristics, capabilities and limitations of performance of the high-risk AI system, including:
        (i) its intended purpose;
        (ii) the level of accuracy, including its metrics, robustness and cybersecurity referred to in Article 15 against which the high-risk AI system has been tested and validated and which can be expected, and any known and foreseeable circumstances that may have an impact on that expected level of accuracy, robustness and cybersecurity;
        (iii) any known or foreseeable circumstance, related to the use of the high-risk AI system in accordance with its intended purpose or under conditions of reasonably foreseeable misuse, which may lead to risks to the health and safety or fundamental rights referred to in Article 9(2);
        (iv) where applicable, the technical capabilities and characteristics of the high-risk AI system to provide information that is relevant to explain its output;
        (v) when appropriate, its performance regarding specific persons or groups of persons on which the system is intended to be used;
        (vi) when appropriate, specifications for the input data, or any other relevant information in terms of the training, validation and testing data sets used, taking into account the intended purpose of the high-risk AI system;
        (vii) where applicable, information to enable deployers to interpret the output of the high-risk AI system and use it appropriately;
    (c) the changes to the high-risk AI system and its performance which have been pre-determined by the provider at the moment of the initial conformity assessment, if any;
    (d) the human oversight measures referred to in Article 14, including the technical measures put in place to facilitate the interpretation of the outputs of the high-risk AI systems by the deployers;
    (e) the computational and hardware resources needed, the expected lifetime of the high-risk AI system and any necessary maintenance and care measures, including their frequency, to ensure the proper functioning of that AI system, including as regards software updates;
    (f) where relevant, a description of the mechanisms included within the high-risk AI system that allows deployers to properly collect, store and interpret the logs in accordance with Article 12.
```

## Article 14 — Human oversight

> **Why it is here.** Gap 21 — human oversight. **The phrase the plan attributed to Article 26 is not in this article**; see the note under Article 26.

```text
1. High-risk AI systems shall be designed and developed in such a way, including with appropriate human-machine interface tools, that they can be effectively overseen by natural persons during the period in which they are in use.
2. Human oversight shall aim to prevent or minimise the risks to health, safety or fundamental rights that may emerge when a high-risk AI system is used in accordance with its intended purpose or under conditions of reasonably foreseeable misuse, in particular where such risks persist despite the application of other requirements set out in this Section.
3. The oversight measures shall be commensurate with the risks, level of autonomy and context of use of the high-risk AI system, and shall be ensured through either one or both of the following types of measures:
    (a) measures identified and built, when technically feasible, into the high-risk AI system by the provider before it is placed on the market or put into service;
    (b) measures identified by the provider before placing the high-risk AI system on the market or putting it into service and that are appropriate to be implemented by the deployer.
4. For the purpose of implementing paragraphs 1, 2 and 3, the high-risk AI system shall be provided to the deployer in such a way that natural persons to whom human oversight is assigned are enabled, as appropriate and proportionate:
    (a) to properly understand the relevant capacities and limitations of the high-risk AI system and be able to duly monitor its operation, including in view of detecting and addressing anomalies, dysfunctions and unexpected performance;
    (b) to remain aware of the possible tendency of automatically relying or over-relying on the output produced by a high-risk AI system (automation bias), in particular for high-risk AI systems used to provide information or recommendations for decisions to be taken by natural persons;
    (c) to correctly interpret the high-risk AI system’s output, taking into account, for example, the interpretation tools and methods available;
    (d) to decide, in any particular situation, not to use the high-risk AI system or to otherwise disregard, override or reverse the output of the high-risk AI system;
    (e) to intervene in the operation of the high-risk AI system or interrupt the system through a ‘stop’ button or a similar procedure that allows the system to come to a halt in a safe state.
5. For high-risk AI systems referred to in point 1(a) of Annex III, the measures referred to in paragraph 3 of this Article shall be such as to ensure that, in addition, no action or decision is taken by the deployer on the basis of the identification resulting from the system unless that identification has been separately verified and confirmed by at least two natural persons with the necessary competence, training and authority.
The requirement for a separate verification by at least two natural persons shall not apply to high-risk AI systems used for the purposes of law enforcement, migration, border control or asylum, where Union or national law considers the application of this requirement to be disproportionate.
```

## Article 15 — Accuracy, robustness and cybersecurity

> **Why it is here.** Gap 21 — accuracy, robustness, cybersecurity.

```text
1. High-risk AI systems shall be designed and developed in such a way that they achieve an appropriate level of accuracy, robustness, and cybersecurity, and that they perform consistently in those respects throughout their lifecycle.
2. To address the technical aspects of how to measure the appropriate levels of accuracy and robustness set out in paragraph 1 and any other relevant performance metrics, the Commission shall, in cooperation with relevant stakeholders and organisations such as metrology and benchmarking authorities, encourage, as appropriate, the development of benchmarks and measurement methodologies.
3. The levels of accuracy and the relevant accuracy metrics of high-risk AI systems shall be declared in the accompanying instructions of use.
4. High-risk AI systems shall be as resilient as possible regarding errors, faults or inconsistencies that may occur within the system or the environment in which the system operates, in particular due to their interaction with natural persons or other systems. Technical and organisational measures shall be taken in this regard.
The robustness of high-risk AI systems may be achieved through technical redundancy solutions, which may include backup or fail-safe plans.
High-risk AI systems that continue to learn after being placed on the market or put into service shall be developed in such a way as to eliminate or reduce as far as possible the risk of possibly biased outputs influencing input for future operations (feedback loops), and as to ensure that any such feedback loops are duly addressed with appropriate mitigation measures.
5. High-risk AI systems shall be resilient against attempts by unauthorised third parties to alter their use, outputs or performance by exploiting system vulnerabilities.
The technical solutions aiming to ensure the cybersecurity of high-risk AI systems shall be appropriate to the relevant circumstances and the risks.
The technical solutions to address AI specific vulnerabilities shall include, where appropriate, measures to prevent, detect, respond to, resolve and control for attacks trying to manipulate the training data set (data poisoning), or pre-trained components used in training (model poisoning), inputs designed to cause the AI model to make a mistake (adversarial examples or model evasion), confidentiality attacks or model flaws.
```

## Article 26 — Obligations of deployers of high-risk AI systems

> **Why it is here.** The disputed quotation, resolved. The plan quoted *"the necessary competence, training and authority"* and cited Article 26. **The attribution is correct** — it is Article 26(2), and the full sentence continues "as well as the necessary support". The defect was never that the plan was wrong; it was that nothing in the docket could have told anyone either way, and the plan told the writer the quotation came from the docket. It now does.

```text
1. Deployers of high-risk AI systems shall take appropriate technical and organisational measures to ensure they use such systems in accordance with the instructions for use accompanying the systems, pursuant to paragraphs 3 and 6.
2. Deployers shall assign human oversight to natural persons who have the necessary competence, training and authority, as well as the necessary support.
3. The obligations set out in paragraphs 1 and 2, are without prejudice to other deployer obligations under Union or national law and to the deployer’s freedom to organise its own resources and activities for the purpose of implementing the human oversight measures indicated by the provider.
4. Without prejudice to paragraphs 1 and 2, to the extent the deployer exercises control over the input data, that deployer shall ensure that input data is relevant and sufficiently representative in view of the intended purpose of the high-risk AI system.
5. Deployers shall monitor the operation of the high-risk AI system on the basis of the instructions for use and, where relevant, inform providers in accordance with Article 72. Where deployers have reason to consider that the use of the high-risk AI system in accordance with the instructions may result in that AI system presenting a risk within the meaning of Article 79(1), they shall, without undue delay, inform the provider or distributor and the relevant market surveillance authority, and shall suspend the use of that system. Where deployers have identified a serious incident, they shall also immediately inform first the provider, and then the importer or distributor and the relevant market surveillance authorities of that incident. If the deployer is not able to reach the provider, Article 73 shall apply mutatis mutandis. This obligation shall not cover sensitive operational data of deployers of AI systems which are law enforcement authorities.
For deployers that are financial institutions subject to requirements regarding their internal governance, arrangements or processes under Union financial services law, the monitoring obligation set out in the first subparagraph shall be deemed to be fulfilled by complying with the rules on internal governance arrangements, processes and mechanisms pursuant to the relevant financial service law.
6. Deployers of high-risk AI systems shall keep the logs automatically generated by that high-risk AI system to the extent such logs are under their control, for a period appropriate to the intended purpose of the high-risk AI system, of at least six months, unless provided otherwise in applicable Union or national law, in particular in Union law on the protection of personal data.
Deployers that are financial institutions subject to requirements regarding their internal governance, arrangements or processes under Union financial services law shall maintain the logs as part of the documentation kept pursuant to the relevant Union financial service law.
7. Before putting into service or using a high-risk AI system at the workplace, deployers who are employers shall inform workers’ representatives and the affected workers that they will be subject to the use of the high-risk AI system. This information shall be provided, where applicable, in accordance with the rules and procedures laid down in Union and national law and practice on information of workers and their representatives.
8. Deployers of high-risk AI systems that are public authorities, or Union institutions, bodies, offices or agencies shall comply with the registration obligations referred to in Article 49. When such deployers find that the high-risk AI system that they envisage using has not been registered in the EU database referred to in Article 71, they shall not use that system and shall inform the provider or the distributor.
9. Where applicable, deployers of high-risk AI systems shall use the information provided under Article 13 of this Regulation to comply with their obligation to carry out a data protection impact assessment under Article 35 of Regulation (EU) 2016/679 or Article 27 of Directive (EU) 2016/680.
10. Without prejudice to Directive (EU) 2016/680, in the framework of an investigation for the targeted search of a person suspected or convicted of having committed a criminal offence, the deployer of a high-risk AI system for post-remote biometric identification shall request an authorisation, ex ante, or without undue delay and no later than 48 hours, by a judicial authority or an administrative authority whose decision is binding and subject to judicial review, for the use of that system, except when it is used for the initial identification of a potential suspect based on objective and verifiable facts directly linked to the offence. Each use shall be limited to what is strictly necessary for the investigation of a specific criminal offence.
If the authorisation requested pursuant to the first subparagraph is rejected, the use of the post-remote biometric identification system linked to that requested authorisation shall be stopped with immediate effect and the personal data linked to the use of the high-risk AI system for which the authorisation was requested shall be deleted.
In no case shall such high-risk AI system for post-remote biometric identification be used for law enforcement purposes in an untargeted way, without any link to a criminal offence, a criminal proceeding, a genuine and present or genuine and foreseeable threat of a criminal offence, or the search for a specific missing person. It shall be ensured that no decision that produces an adverse legal effect on a person may be taken by the law enforcement authorities based solely on the output of such post-remote biometric identification systems.
This paragraph is without prejudice to Article 9 of Regulation (EU) 2016/679 and Article 10 of Directive (EU) 2016/680 for the processing of biometric data.
Regardless of the purpose or deployer, each use of such high-risk AI systems shall be documented in the relevant police file and shall be made available to the relevant market surveillance authority and the national data protection authority upon request, excluding the disclosure of sensitive operational data related to law enforcement. This subparagraph shall be without prejudice to the powers conferred by Directive (EU) 2016/680 on supervisory authorities.
Deployers shall submit annual reports to the relevant market surveillance and national data protection authorities on their use of post-remote biometric identification systems, excluding the disclosure of sensitive operational data related to law enforcement. The reports may be aggregated to cover more than one deployment.
Member States may introduce, in accordance with Union law, more restrictive laws on the use of post-remote biometric identification systems.
11. Without prejudice to Article 50 of this Regulation, deployers of high-risk AI systems referred to in Annex III that make decisions or assist in making decisions related to natural persons shall inform the natural persons that they are subject to the use of the high-risk AI system. For high-risk AI systems used for law enforcement purposes Article 13 of Directive (EU) 2016/680 shall apply.
12. Deployers shall cooperate with the relevant competent authorities in any action those authorities take in relation to the high-risk AI system in order to implement this Regulation.
```

## Article 75a — Supervisory and enforcement powers of the AI Office

> **Why it is here.** New. The AI Office's supervisory and enforcement powers.

```text
1. When exercising its tasks of supervision and enforcement laid down in Article 75(1) of this Regulation, the AI Office shall have all the powers of a market surveillance authority provided for in this Section and in Article 14(4) and Article 16(3) of Regulation (EU) 2019/1020. The AI Office shall be authorised to fully reclaim from the relevant operator the totality of the costs of its supervision and enforcement activities with respect to instances of non-compliance, including costs for human and technical resources, in accordance with Article 15 of Regulation (EU) 2019/1020. Article 17 of Regulation (EU) 2019/1020 shall apply mutatis mutandis.
2. Where the AI Office has reasonable grounds to suspect non-compliance with this Regulation by a provider or a deployer of an AI system referred to in Article 75(1) of this Regulation, it may adopt a decision to start an investigation into that non-compliance in accordance with Article 14(4), point (f) of Regulation (EU) 2019/1020. Upon starting such an investigation, the AI Office shall notify the operator of the AI system concerned. The AI Office may exercise the powers referred to in paragraph 1 of this Article on its own initiative or following a complaint received pursuant to Article 85 of this Regulation, even before starting an investigation pursuant to Article 14(4), point (f) of Regulation (EU) 2019/1020.
Where a market surveillance authority has reason to suspect non-compliance with this Regulation by a provider or a deployer of an AI system referred to in Article 75(1), it may send a request to the AI Office to assess the matter.
3. The AI Office may exercise the powers listed in Article 14(4), points (a), (b) and (c) of Regulation (EU) 2019/1020 and Article 74(12) and (13) of this Regulation by simple request or by decision.
When requesting information, the AI Office shall state the legal basis and the purpose of the request, specify what information is required, and set the period within which the information is to be provided. Where the request is a simple request, the AI Office shall additionally indicate that although there is no obligation to provide the information requested, in the case of a voluntary reply, the information must be correct and not misleading, and indicate the potential fines provided for in Article 99(5) for supplying incorrect or misleading information. Where the request is made by decision, the AI Office shall additionally indicate the fines provided for in Article 99(5) for supplying incorrect, incomplete or misleading information and indicate the right to have the decision reviewed by the Court of Justice of the European Union. The AI Office shall send a copy of the request to the market surveillance authority of the Member State in the territory of which the operator or its legal representative is situated.
4. In order to carry out the tasks assigned to it under this Section, the AI Office may conduct all necessary remote or on-site inspections pursuant to the powers laid down in Article 14(4), points (d) and (e) of Regulation (EU) 2019/1020 and Article 74(5) of this Regulation. When conducting an inspection, the AI Office shall inform the provider concerned of the subject matter and purpose of the investigation, the relevant fines referred to in Article 99(5) of this Regulation, and the right to have the decision reviewed by the Court of Justice of the European Union. Prior to conducting an inspection, the AI Office shall inform the market surveillance authority of the Member State in the territory of which the operator or its legal representative is situated.
During such an inspection, the officials of the AI Office shall be empowered to:
    (a) enter any of the business premises, land or property located in the Union of the operator concerned;
    (b) examine the books, data and other material relevant to the execution of their tasks, irrespective of the medium on which they are stored;
    (c) take or obtain in any form copies of or extracts from books, data and other records;
    (d) ask any of the persons subject to the inspection, or their representatives, or staff, for oral or written explanations on factors or documents relating to the subject matter and purpose of the inspection, and to record the answers;
    (e) seal any business premises and books or records for the duration of, and to the extent necessary for, the inspection.
Where the AI Office finds that a natural or legal person opposes or obstructs an inspection, the national competent authority of the Member State concerned shall afford it the necessary assistance, requesting, where appropriate, the assistance of the police or an equivalent enforcement authority, to enable it to conduct its on-site inspection.
Where an on-site inspection of business premises, land or property requires authorisation by a judicial authority in accordance with national law, the AI Office shall apply for such an authorisation. The AI Office may also apply for such authorisation as a precautionary measure. Where such an authorisation is applied for, the national judicial authority shall promptly verify that the coercive measures envisaged are neither arbitrary nor excessive having regard to the subject matter of the investigation or inspection and the documents provided by the AI Office with the decision. In its verification of the proportionality of coercive measures, the national judicial authority may ask the AI Office for detailed explanations, in particular relating to the grounds the AI Office has for suspecting that an infringement of this Regulation has taken place and the seriousness of the suspected infringement and, where relevant, the nature of the involvement of the person subject to the coercive measures. The national judicial authority shall not review the necessity of the investigation or inspection nor demand information from the case file of the AI Office. In accordance with the Treaties, the legality of the decision of the AI Office is subject to review only by the Court of Justice of the European Union.
5. At the request of the AI Office, the competent market surveillance authority of a Member State may in its own territory carry out any investigation, inspection or other fact-finding measure on behalf and for the account of the AI Office in order to establish whether there has been an infringement of this Regulation. The officials of the competent authorities of the Member States who are responsible for conducting such investigations, inspections, or fact-finding measures, as well as those authorised or appointed by them, shall exercise their powers in accordance with their national law.
6. In addition to the powers set out in paragraph 1 of this Article, the AI Office, in the exercise of its competences referred to in Article 75(1), may:
    (a) order operators to provide access to, and explanations relating to, their AI systems;
    (b) impose an obligation on an operator to retain all data and documents deemed to be necessary to assess the implementation of and compliance with the obligations under this Regulation.
7. To assist it in monitoring the effective implementation and compliance with the relevant provisions of this Regulation and to provide it with specific expertise or knowledge in the exercise of its competences under Article 75(1), the AI Office may appoint independent external experts and auditors, as well as experts, investigative teams and auditors from the Member State’s competent authorities with the agreement of the authority concerned. Information obtained as a result of such monitoring actions shall be shared with the relevant competent authorities of the Member States.
8. Information collected pursuant to this Article shall be used only for the purpose of this Regulation.
```

## Article 75b — Commitments

> **Why it is here.** New. Commitments.

```text
If, during proceedings under Article 75a(2), the operator concerned offers commitments to ensure compliance with the relevant provisions of this Regulation, the AI Office may, by decision, make those commitments binding on the operator concerned and declare that there are no further grounds for action. The AI Office may, upon request or on its own initiative, reopen the proceedings where:
    (a) there has been a material change in any of the facts on which the decision was based;
    (b) the operator acts contrary to its commitments; or
    (c) the decision was based on incomplete, incorrect or misleading information provided by the operator concerned.
Where the AI Office considers that the commitments offered by the operator concerned are unable to ensure effective compliance with the relevant provisions of this Regulation, it shall reject those commitments in a reasoned decision when concluding the proceedings.
```

## Article 75c — Non-compliance, fines and periodic penalty payments

> **Why it is here.** New. Non-compliance, fines and periodic penalty payments.

```text
1. Where the AI Office finds that an operator falling within the scope of Article 75(1) does not comply with the relevant provisions of this Regulation or with commitments made binding pursuant to Article 75b, it shall adopt a decision establishing such non-compliance.
2. Before adopting a decision pursuant to paragraph 1, the AI Office shall communicate its preliminary findings to the operator concerned. In the preliminary findings, the AI Office shall explain the measures that it is considering taking, or that it considers that the operator concerned should take, in order to effectively address the preliminary findings.
3. In the decision pursuant to paragraph 1 of this Article, the AI Office shall, where relevant, order the operator concerned to take the necessary measures to ensure compliance with the relevant provisions of this Regulation within a reasonable period specified therein and to provide information on the measures that that operator intends to take to comply with the decision. The operator concerned shall provide the AI Office with a description of the measures it has taken to ensure compliance with the decision upon their implementation. Prior to requesting any measure, the AI Office may engage in a structured dialogue with the operator of the AI system in question. During this dialogue, the operator may propose commitments in accordance with Article 75b.
4. A decision adopted pursuant to paragraph 1 of this Article may be accompanied by the imposition of penalties in accordance with Article 99(3) to (7), which provisions shall apply mutatis mutandis to the AI Office in the execution of its supervision and enforcement tasks referred to in Article 75(1).
In particular, the following shall be subject to administrative fines as referred to in Article 99(4):
    (a) infringement of any applicable provision of this Regulation, including those not listed in Article 99(4);
    (b) failure to comply with decisions or measures adopted pursuant to the powers listed in Article 14(4) or Article 16(3) of Regulation (EU) 2019/1020, as well as those specified in Article 75a of this Regulation;
    (c) failure to comply with a commitment made binding by a decision pursuant to Article 75b.
The supply of incorrect, incomplete or misleading information to the AI Office in reply to a request shall be subject to administrative fines as referred to in Article 99(5).
5. The AI Office may adopt a decision imposing periodic penalty payments to compel the operators subject to its competence pursuant to Article 75(1) to the following:
    (a) to submit to an investigation;
    (b) to comply with an information request ordered by a decision adopted under Article 75a(3);
    (c) to submit to an inspection ordered by a decision pursuant to Article 75a(4);
    (d) to provide correct or complete answers or explanations in the context of an inspection ordered by a decision pursuant to Article 75a(4);
    (e) to comply with corrective actions ordered pursuant to the power listed in Article 16 of Regulation (EU) 2019/1020;
    (f) to comply with commitments made legally binding by a decision pursuant to Article 75b; or
    (g) to comply with a decision pursuant to the paragraph (1) of this Article.
Those penalty payments shall be effective and proportionate, and, where applicable, shall not exceed 5 % of the average daily income or worldwide annual turnover in the preceding financial year per day, calculated from the date appointed by the decision.
6. The Court of Justice of the European Union shall have unlimited jurisdiction to review decisions of the AI Office fixing a fine or periodic penalty payment pursuant to this Article. It may cancel, reduce or increase the fine or periodic penalty payment imposed.
7. Funds collected through the imposition of fines or periodic penalty payments pursuant to this Article shall contribute to the general budget of the Union.
8. The powers conferred on the AI Office by this Article shall be subject to a limitation period of five years. The limitation period shall begin to run on the day on which the infringement is committed. However, in the case of continuing or repeated infringements, the limitation period shall begin to run on the day on which the infringement ceases.
The power of the AI Office to enforce decisions taken pursuant to this Article shall be subject to a limitation period of five years. The limitation period shall begin to run on the day on which the decision becomes final.
The implementing act referred to in Article 75d(3) shall specify the first and second subparagraphs of this paragraph, including the circumstances in which the limitation periods shall be interrupted.
9. Where the AI Office determines that there are no grounds to adopt a decision of non-compliance, it shall close the proceeding by a decision. That decision shall apply with immediate effect.
```

## Article 75d — Safeguards and further specification

> **Why it is here.** New. Safeguards.

```text
1. Article 18 of Regulation (EU) 2019/1020 shall apply mutatis mutandis to operators subject to the AI Office’s competence pursuant to Article 75(1) of this Regulation, without prejudice to more specific procedural rights provided for in this Regulation.
2. The rights of defence and of access to the file of operators falling within the scope of Article 75(1) shall be fully respected in proceedings. In view of the possible adoption of decisions on the basis of Article 75c(1), those operators shall be entitled to have access to the AI Office file under the terms of a negotiated disclosure, subject to the legitimate interest of the operator or other person concerned in the protection of their business secrets. The AI Office shall have the power to adopt decisions setting out such terms of disclosure in the case of disagreement between the parties. The right of access to the file shall not extend to confidential information and internal documents of the AI Office, the Board, competent market surveillance authorities or other public authorities of the Member States. In particular, the right of access shall not extend to correspondence between the AI Office and those authorities. Nothing in this paragraph shall prevent the AI Office from disclosing and using information necessary to prove an infringement.
3. The Commission may adopt implementing acts concerning the practical arrangements for access to the file and the negotiated disclosure of information provided for in paragraph 2.
4. The AI Office shall publish the decisions it adopts pursuant to Articles 75b and 75c. Such publication shall state the names of the parties and the main content of the decision, including any penalties imposed. The publication shall have regard to the rights and legitimate interests of any person concerned in the protection of their confidential information.
```

## Article 85 — Right to lodge a complaint with a market surveillance authority

> **Why it is here.** Gap 25 — the right to complain to a market surveillance authority.

```text
Without prejudice to other administrative or judicial remedies, any natural or legal person having grounds to consider that there has been an infringement of the provisions of this Regulation may submit complaints to the relevant market surveillance authority.
In accordance with Regulation (EU) 2019/1020, such complaints shall be taken into account for the purpose of conducting market surveillance activities, and shall be handled in line with the dedicated procedures established therefor by the market surveillance authorities.
```

## Article 86 — Right to explanation of individual decision-making

> **Why it is here.** Gap 25 — the right to an explanation of individual decision-making.

```text
1. Any affected person subject to a decision which is taken by the deployer on the basis of the output from a high-risk AI system listed in Annex III, with the exception of systems listed under point 2 thereof, and which produces legal effects or similarly significantly affects that person in a way that they consider to have an adverse impact on their health, safety or fundamental rights shall have the right to obtain from the deployer clear and meaningful explanations of the role of the AI system in the decision-making procedure and the main elements of the decision taken.
2. Paragraph 1 shall not apply to the use of AI systems for which exceptions from, or restrictions to, the obligation under that paragraph follow from Union or national law in compliance with Union law.
3. This Article shall apply only to the extent that the right referred to in paragraph 1 is not otherwise provided for under Union law.
```

## Article 87 — Reporting of infringements and protection of reporting persons

> **Why it is here.** Gap 25 — reporting infringements.

```text
Directive (EU) 2019/1937 shall apply to the reporting of infringements of this Regulation and the protection of persons reporting such infringements.
```

## Article 95 — Codes of conduct for voluntary application of specific requirements

> **Why it is here.** Gap 26 — codes of conduct.

```text
1. The AI Office and the Member States shall encourage and facilitate the drawing up of codes of conduct, including related governance mechanisms, intended to foster the voluntary application to AI systems, other than high-risk AI systems, of some or all of the requirements set out in Chapter III, Section 2 taking into account the available technical solutions and industry best practices allowing for the application of such requirements.
2. The AI Office and the Member States shall facilitate the drawing up of codes of conduct concerning the voluntary application, including by deployers, of specific requirements to all AI systems, on the basis of clear objectives and key performance indicators to measure the achievement of those objectives, including elements such as, but not limited to:
    (a) applicable elements provided for in Union ethical guidelines for trustworthy AI;
    (b) assessing and minimising the impact of AI systems on environmental sustainability, including as regards energy-efficient programming and techniques for the efficient design, training and use of AI;
    (c) promoting AI literacy, in particular that of persons dealing with the development, operation and use of AI;
    (d) facilitating an inclusive and diverse design of AI systems, including through the establishment of inclusive and diverse development teams and the promotion of stakeholders’ participation in that process;
    (e) assessing and preventing the negative impact of AI systems on vulnerable persons or groups of vulnerable persons, including as regards accessibility for persons with a disability, as well as on gender equality.
3. Codes of conduct may be drawn up by individual providers or deployers of AI systems or by organisations representing them or by both, including with the involvement of any interested stakeholders and their representative organisations, including civil society organisations and academia. Codes of conduct may cover one or more AI systems taking into account the similarity of the intended purpose of the relevant systems.
[▼M1]
4. The AI Office and the Member States shall take into account the specific interests and needs of SMEs, including start-ups, and SMCs, when encouraging and facilitating the drawing up of codes of conduct.
[▼B]
```

## Article 96 — Guidelines from the Commission on the implementation of this Regulation

> **Why it is here.** Gap 26 — Commission guidelines.

```text
1. The Commission shall develop guidelines on the practical implementation of this Regulation, and in particular on:
[▼M1]
    (a) the application of the requirements and obligations referred to in Articles 8 to 15 and in Articles 25 and 26;
[▼B]
    (b) the prohibited practices referred to in Article 5;
    (c) the practical implementation of the provisions related to substantial modification;
    (d) the practical implementation of transparency obligations laid down in Article 50;
    (e) detailed information on the relationship of this Regulation with the Union harmonisation legislation listed in Annex I, as well as with other relevant Union law, including as regards consistency in their enforcement;
    (f) the application of the definition of an AI system as set out in Article 3, point (1);
[▼M1]
    (g) the practical implementation of Article 8(2), Article 9(10) and Article 17(3) in accordance with the principle of complementarity and proportionality, with a view to ensuring consistency, avoiding duplication and minimising additional burdens when complying with the requirements of this Regulation and the requirements of the Union harmonisation legislation listed in Section A of Annex I; such guidelines shall be published by 1 August 2027.
[▼M1]
When issuing such guidelines, the Commission shall involve the Board and pay particular attention to the needs of SMEs, including start-ups, and SMCs, of local public authorities and of the sectors most likely to be affected by this Regulation.
[▼B]
The guidelines referred to in the first subparagraph of this paragraph shall take due account of the generally acknowledged state of the art on AI, as well as of relevant harmonised standards and common specifications that are referred to in Articles 40 and 41, or of those harmonised standards or technical specifications that are set out pursuant to Union harmonisation law.
2. At the request of the Member States or the AI Office, or on its own initiative, the Commission shall update guidelines previously adopted when deemed necessary.
```

## Article 112 — Evaluation and review

> **Why it is here.** Gap 27 — evaluation and review: the Act's own capacity to be revised, which the verdict episode leans on.

```text
1. The Commission shall assess the need for amendment of the list set out in Annex III and of the list of prohibited AI practices laid down in Article 5, once a year following the entry into force of this Regulation, and until the end of the period of the delegation of power laid down in Article 97. The Commission shall submit the findings of that assessment to the European Parliament and the Council.
2. By 2 August 2028 and every four years thereafter, the Commission shall evaluate and report to the European Parliament and to the Council on the following:
    (a) the need for amendments extending existing area headings or adding new area headings in Annex III;
    (b) amendments to the list of AI systems requiring additional transparency measures in Article 50;
    (c) amendments enhancing the effectiveness of the supervision and governance system.
3. By 2 August 2029 and every four years thereafter, the Commission shall submit a report on the evaluation and review of this Regulation to the European Parliament and to the Council. The report shall include an assessment with regard to the structure of enforcement and the possible need for a Union agency to resolve any identified shortcomings. On the basis of the findings, that report shall, where appropriate, be accompanied by a proposal for amendment of this Regulation. The reports shall be made public.
4. The reports referred to in paragraph 2 shall pay specific attention to the following:
    (a) the status of the financial, technical and human resources of the national competent authorities in order to effectively perform the tasks assigned to them under this Regulation;
    (b) the state of penalties, in particular administrative fines as referred to in Article 99(1), applied by Member States for infringements of this Regulation;
    (c) adopted harmonised standards and common specifications developed to support this Regulation;
    (d) the number of undertakings that enter the market after the entry into application of this Regulation, and how many of them are SMEs.
5. By 2 August 2028, the Commission shall evaluate the functioning of the AI Office, whether the AI Office has been given sufficient powers and competences to fulfil its tasks, and whether it would be relevant and needed for the proper implementation and enforcement of this Regulation to upgrade the AI Office and its enforcement competences and to increase its resources. The Commission shall submit a report on its evaluation to the European Parliament and to the Council.
6. By 2 August 2028 and every four years thereafter, the Commission shall submit a report on the review of the progress on the development of standardisation deliverables on the energy-efficient development of general-purpose AI models, and asses the need for further measures or actions, including binding measures or actions. The report shall be submitted to the European Parliament and to the Council, and it shall be made public.
7. By 2 August 2028 and every three years thereafter, the Commission shall evaluate the impact and effectiveness of voluntary codes of conduct to foster the application of the requirements set out in Chapter III, Section 2 for AI systems other than high-risk AI systems and possibly other additional requirements for AI systems other than high-risk AI systems, including as regards environmental sustainability.
8. For the purposes of paragraphs 1 to 7, the Board, the Member States and national competent authorities shall provide the Commission with information upon its request and without undue delay.
9. In carrying out the evaluations and reviews referred to in paragraphs 1 to 7, the Commission shall take into account the positions and findings of the Board, of the European Parliament, of the Council, and of other relevant bodies or sources.
10. The Commission shall, if necessary, submit appropriate proposals to amend this Regulation, in particular taking into account developments in technology, the effect of AI systems on health and safety, and on fundamental rights, and in light of the state of progress in the information society.
11. To guide the evaluations and reviews referred to in paragraphs 1 to 7 of this Article, the AI Office shall undertake to develop an objective and participative methodology for the evaluation of risk levels based on the criteria outlined in the relevant Articles and the inclusion of new systems in:
    (a) the list set out in Annex III, including the extension of existing area headings or the addition of new area headings in that Annex;
    (b) the list of prohibited practices set out in Article 5; and
    (c) the list of AI systems requiring additional transparency measures pursuant to Article 50.
12. Any amendment to this Regulation pursuant to paragraph 10, or relevant delegated or implementing acts, which concerns sectoral Union harmonisation legislation listed in Section B of Annex I shall take into account the regulatory specificities of each sector, and the existing governance, conformity assessment and enforcement mechanisms and authorities established therein.
13. By 2 August 2031, the Commission shall carry out an assessment of the enforcement of this Regulation and shall report on it to the European Parliament, the Council and the European Economic and Social Committee, taking into account the first years of application of this Regulation. On the basis of the findings, that report shall, where appropriate, be accompanied by a proposal for amendment of this Regulation with regard to the structure of enforcement and the need for a Union agency to resolve any identified shortcomings.
```

## Article 113 — Entry into force and application

> **Why it is here.** Not a listed gap, but the dates in `00_status_and_dates.md` are checkable only against this, as amended.

```text
This Regulation shall enter into force on the twentieth day following that of its publication in the Official Journal of the European Union.
It shall apply from 2 August 2026.
However:
[▼M1]
    (a) Chapters I and II shall apply from 2 February 2025, with the exception of Article 5(1), first subparagraph, points (ba) and (bb), and Article 5(1a) and (1b) which shall apply from 2 December 2026;
[▼B]
    (b) Chapter III Section 4, Chapter V, Chapter VII and Chapter XII and Article 78 shall apply from 2 August 2025, with the exception of Article 101;
[▼M1]
    (c) Chapter III, Sections 1, 2, and 3, with the exception of Article 6(5), shall apply from:
        (i) 2 December 2027 as regards AI systems classified as high-risk pursuant to Article 6(2) and Annex III; and
        (ii) 2 August 2028 as regards AI systems classified as high-risk pursuant to Article 6(1) and Annex I;
[▼M1]
    (d) Articles 102 to 110 shall apply from 27 July 2026.
[▼B]
```

---

# Part two — the provisions the first plan reached for and this docket had not supplied

`prosodia plan-lint` compared every citation in `plan/outline.md` against this directory and found
twenty provisions the plan asserts that no file here contained. They are below, verbatim, from the
same consolidated text and the same extraction as Part one.

Regenerate with:

```bash
python experiments/eurlex/consolidate.py 02024R1689-20260727 out.md \
  --select "Article 21,Article 22,Article 25,Article 28,Article 40,Article 41,Article 44,Article 47,Article 48,Article 52,Article 53,Article 54,Article 55,Article 56,Article 57,Article 64,Article 88,Article 100,ANNEX XI,ANNEX XII"
```

## Article 21 — Cooperation with competent authorities

```text
1. Providers of high-risk AI systems shall, upon a reasoned request by a competent authority, provide that authority all the information and documentation necessary to demonstrate the conformity of the high-risk AI system with the requirements set out in Section 2, in a language which can be easily understood by the authority in one of the official languages of the institutions of the Union as indicated by the Member State concerned.
2. Upon a reasoned request by a competent authority, providers shall also give the requesting competent authority, as applicable, access to the automatically generated logs of the high-risk AI system referred to in Article 12(1), to the extent such logs are under their control.
3. Any information obtained by a competent authority pursuant to this Article shall be treated in accordance with the confidentiality obligations set out in Article 78.
```

## Article 22 — Authorised representatives of providers of high-risk AI systems

```text
1. Prior to making their high-risk AI systems available on the Union market, providers established in third countries shall, by written mandate, appoint an authorised representative which is established in the Union.
2. The provider shall enable its authorised representative to perform the tasks specified in the mandate received from the provider.
3. The authorised representative shall perform the tasks specified in the mandate received from the provider. It shall provide a copy of the mandate to the market surveillance authorities upon request, in one of the official languages of the institutions of the Union, as indicated by the competent authority. For the purposes of this Regulation, the mandate shall empower the authorised representative to carry out the following tasks:
    (a) verify that the EU declaration of conformity referred to in Article 47 and the technical documentation referred to in Article 11 have been drawn up and that an appropriate conformity assessment procedure has been carried out by the provider;
    (b) keep at the disposal of the competent authorities and national authorities or bodies referred to in Article 74(10), for a period of 10 years after the high-risk AI system has been placed on the market or put into service, the contact details of the provider that appointed the authorised representative, a copy of the EU declaration of conformity referred to in Article 47, the technical documentation and, if applicable, the certificate issued by the notified body;
    (c) provide a competent authority, upon a reasoned request, with all the information and documentation, including that referred to in point (b) of this subparagraph, necessary to demonstrate the conformity of a high-risk AI system with the requirements set out in Section 2, including access to the logs, as referred to in Article 12(1), automatically generated by the high-risk AI system, to the extent such logs are under the control of the provider;
    (d) cooperate with competent authorities, upon a reasoned request, in any action the latter take in relation to the high-risk AI system, in particular to reduce and mitigate the risks posed by the high-risk AI system;
    (e) where applicable, comply with the registration obligations referred to in Article 49(1), or, if the registration is carried out by the provider itself, ensure that the information referred to in point 3 of Section A of Annex VIII is correct.
The mandate shall empower the authorised representative to be addressed, in addition to or instead of the provider, by the competent authorities, on all issues related to ensuring compliance with this Regulation.
4. The authorised representative shall terminate the mandate if it considers or has reason to consider the provider to be acting contrary to its obligations pursuant to this Regulation. In such a case, it shall immediately inform the relevant market surveillance authority, as well as, where applicable, the relevant notified body, about the termination of the mandate and the reasons therefor.
```

## Article 25 — Responsibilities along the AI value chain

```text
1. Any distributor, importer, deployer or other third-party shall be considered to be a provider of a high-risk AI system for the purposes of this Regulation and shall be subject to the obligations of the provider under Article 16, in any of the following circumstances:
    (a) they put their name or trademark on a high-risk AI system already placed on the market or put into service, without prejudice to contractual arrangements stipulating that the obligations are otherwise allocated;
    (b) they make a substantial modification to a high-risk AI system that has already been placed on the market or has already been put into service in such a way that it remains a high-risk AI system pursuant to Article 6;
    (c) they modify the intended purpose of an AI system, including a general-purpose AI system, which has not been classified as high-risk and has already been placed on the market or put into service in such a way that the AI system concerned becomes a high-risk AI system in accordance with Article 6.
[▼M1]
2. Where the circumstances referred to in paragraph 1 occur, the provider that initially placed the AI system on the market or put it into service shall no longer be considered to be a provider of that specific AI system for the purposes of this Regulation.
That initial provider shall closely cooperate with new providers and shall make available the necessary information and provide the reasonably expected technical access and other assistance that are required for the fulfilment of the obligations set out in this Regulation, in particular with regard to compliance with the conformity assessment of high-risk AI systems.
In particular, the obligation laid down in the second subparagraph shall include, where relevant for the purposes specified therein, the following:
    (a) making available of technical documentation sufficient to assess compliance with the requirements laid down in Article 16;
    (b) informing the new providers about known limitations and failure modes; and
    (c) providing the new providers with targeted technical access, including for testing and validation.
This paragraph shall not apply in cases where the initial provider has clearly specified that its AI system is not to be changed into a high-risk AI system and therefore does not fall under the obligation to cooperate with the new providers and hand over the documentation.
[▼B]
3. In the case of high-risk AI systems that are safety components of products covered by the Union harmonisation legislation listed in Section A of Annex I, the product manufacturer shall be considered to be the provider of the high-risk AI system, and shall be subject to the obligations under Article 16 under either of the following circumstances:
    (a) the high-risk AI system is placed on the market together with the product under the name or trademark of the product manufacturer;
    (b) the high-risk AI system is put into service under the name or trademark of the product manufacturer after the product has been placed on the market.
[▼M1]
4. The provider of a high-risk AI system and the third party that supplies an AI system, AI model, tools, services, components, or processes that are used or integrated in a high-risk AI system shall, by written agreement, specify the necessary information, capabilities, technical access and other assistance based on the generally acknowledged state of the art, in order to enable the provider of the high-risk AI system to fully comply with the obligations set out in this Regulation. This paragraph shall not apply to third parties making accessible to the public tools, services, processes, or components, other than general-purpose AI models, under a free and open-source licence.
[▼B]
The AI Office may develop and recommend voluntary model terms for contracts between providers of high-risk AI systems and third parties that supply tools, services, components or processes that are used for or integrated into high-risk AI systems. When developing those voluntary model terms, the AI Office shall take into account possible contractual requirements applicable in specific sectors or business cases. The voluntary model terms shall be published and be available free of charge in an easily usable electronic format.
5. Paragraphs 2 and 3 are without prejudice to the need to observe and protect intellectual property rights, confidential business information and trade secrets in accordance with Union and national law.
```

## Article 28 — Notifying authorities

```text
1. Each Member State shall designate or establish at least one notifying authority responsible for setting up and carrying out the necessary procedures for the assessment, designation and notification of conformity assessment bodies and for their monitoring. Those procedures shall be developed in cooperation between the notifying authorities of all Member States.
2. Member States may decide that the assessment and monitoring referred to in paragraph 1 is to be carried out by a national accreditation body within the meaning of, and in accordance with, Regulation (EC) No 765/2008.
3. Notifying authorities shall be established, organised and operated in such a way that no conflict of interest arises with conformity assessment bodies, and that the objectivity and impartiality of their activities are safeguarded.
4. Notifying authorities shall be organised in such a way that decisions relating to the notification of conformity assessment bodies are taken by competent persons different from those who carried out the assessment of those bodies.
5. Notifying authorities shall offer or provide neither any activities that conformity assessment bodies perform, nor any consultancy services on a commercial or competitive basis.
6. Notifying authorities shall safeguard the confidentiality of the information that they obtain, in accordance with Article 78.
7. Notifying authorities shall have an adequate number of competent personnel at their disposal for the proper performance of their tasks. Competent personnel shall have the necessary expertise, where applicable, for their function, in fields such as information technologies, AI and law, including the supervision of fundamental rights.
[▼M1]
8. Notifying authorities designated pursuant to this Regulation that are responsible for AI systems covered by the Union harmonisation legislation listed in Section A of Annex I shall ensure that the conformity assessment body that applies for designation both pursuant to this Regulation and the Union harmonisation legislation listed in Section A of Annex I is provided with the possibility to submit a single application and undergoes a unified assessment procedure to be designated pursuant to this Regulation and Union harmonisation legislation listed in Section A of Annex I, where the relevant Union harmonisation legislation provides for such single application and unified assessment procedure. To that end, notifying authorities designated pursuant to this Regulation and those designated pursuant to the Union harmonisation legislation listed in Section A of Annex I shall cooperate in their assessments.
The single application and the unified assessment procedure referred to in this paragraph shall also be made available to notified bodies already designated pursuant to the Union harmonisation legislation listed in Section A of Annex I, when those notified bodies apply for designation pursuant to this Regulation, provided that the relevant Union harmonisation legislation provides for such a procedure.
A conformity assessment body that is designated pursuant to more than one piece of Union harmonisation legislation listed in Section A of Annex I shall have to apply only once to be designated pursuant to this Regulation. A designation pursuant to this Regulation shall be applicable for all Union harmonisation legislation listed in Section A of Annex I for which the conformity assessment body is designated.
The single application and the unified assessment procedure shall avoid any unnecessary duplications, build on the existing procedures for designation in accordance with the Union harmonisation legislation listed in Section A of Annex I and ensure compliance with the requirements relating to notified bodies both in accordance with this Regulation and the relevant Union harmonisation legislation.
9. A notifying authority that has been designated pursuant to the Union harmonisation legislation listed in Section A of Annex I is also the notifying authority for the application of the single application and unified assessment procedure referred to in paragraph 8, unless the Member State designates another notifying authority for this Regulation.
[▼B]
```

## Article 40 — Harmonised standards and standardisation deliverables

```text
1. High-risk AI systems or general-purpose AI models which are in conformity with harmonised standards or parts thereof the references of which have been published in the Official Journal of the European Union in accordance with Regulation (EU) No 1025/2012 shall be presumed to be in conformity with the requirements set out in Section 2 of this Chapter or, as applicable, with the obligations set out in of Chapter V, Sections 2 and 3, of this Regulation, to the extent that those standards cover those requirements or obligations.
2. In accordance with Article 10 of Regulation (EU) No 1025/2012, the Commission shall issue, without undue delay, standardisation requests covering all requirements set out in Section 2 of this Chapter and, as applicable, standardisation requests covering obligations set out in Chapter V, Sections 2 and 3, of this Regulation. The standardisation request shall also ask for deliverables on reporting and documentation processes to improve AI systems’ resource performance, such as reducing the high-risk AI system’s consumption of energy and of other resources during its lifecycle, and on the energy-efficient development of general-purpose AI models. When preparing a standardisation request, the Commission shall consult the Board and relevant stakeholders, including the advisory forum.
When issuing a standardisation request to European standardisation organisations, the Commission shall specify that standards have to be clear, consistent, including with the standards developed in the various sectors for products covered by the existing Union harmonisation legislation listed in Annex I, and aiming to ensure that high-risk AI systems or general-purpose AI models placed on the market or put into service in the Union meet the relevant requirements or obligations laid down in this Regulation.
The Commission shall request the European standardisation organisations to provide evidence of their best efforts to fulfil the objectives referred to in the first and the second subparagraph of this paragraph in accordance with Article 24 of Regulation (EU) No 1025/2012.
[▼M1]
The Commission shall request, in accordance with Regulation (EU) No 1025/2012 of the European Parliament and of the Council ( ^1 ) and without undue delay, the European standardisation organisations to develop standardisation deliverables, including, as appropriate, harmonised standards, to facilitate the joint compliance and presumption of conformity with the requirements or obligations set out in Chapter III, Sections 2 and 3 of this Regulation, and the relevant requirements and obligations laid down in the Union harmonisation legislation listed in Annex I to this Regulation.
[▼B]
3. The participants in the standardisation process shall seek to promote investment and innovation in AI, including through increasing legal certainty, as well as the competitiveness and growth of the Union market, to contribute to strengthening global cooperation on standardisation and taking into account existing international standards in the field of AI that are consistent with Union values, fundamental rights and interests, and to enhance multi-stakeholder governance ensuring a balanced representation of interests and the effective participation of all relevant stakeholders in accordance with Articles 5, 6, and 7 of Regulation (EU) No 1025/2012.
```

## Article 41 — Common specifications

```text
1. The Commission may adopt, implementing acts establishing common specifications for the requirements set out in Section 2 of this Chapter or, as applicable, for the obligations set out in Sections 2 and 3 of Chapter V where the following conditions have been fulfilled:
    (a) the Commission has requested, pursuant to Article 10(1) of Regulation (EU) No 1025/2012, one or more European standardisation organisations to draft a harmonised standard for the requirements set out in Section 2 of this Chapter, or, as applicable, for the obligations set out in Sections 2 and 3 of Chapter V, and:
        (i) the request has not been accepted by any of the European standardisation organisations; or
        (ii) the harmonised standards addressing that request are not delivered within the deadline set in accordance with Article 10(1) of Regulation (EU) No 1025/2012; or
        (iii) the relevant harmonised standards insufficiently address fundamental rights concerns; or
        (iv) the harmonised standards do not comply with the request; and
    (b) no reference to harmonised standards covering the requirements referred to in Section 2 of this Chapter or, as applicable, the obligations referred to in Sections 2 and 3 of Chapter V has been published in the Official Journal of the European Union in accordance with Regulation (EU) No 1025/2012, and no such reference is expected to be published within a reasonable period.
When drafting the common specifications, the Commission shall consult the advisory forum referred to in Article 67.
The implementing acts referred to in the first subparagraph of this paragraph shall be adopted in accordance with the examination procedure referred to in Article 98(2).
2. Before preparing a draft implementing act, the Commission shall inform the committee referred to in Article 22 of Regulation (EU) No 1025/2012 that it considers the conditions laid down in paragraph 1 of this Article to be fulfilled.
3. High-risk AI systems or general-purpose AI models which are in conformity with the common specifications referred to in paragraph 1, or parts of those specifications, shall be presumed to be in conformity with the requirements set out in Section 2 of this Chapter or, as applicable, to comply with the obligations referred to in Sections 2 and 3 of Chapter V, to the extent those common specifications cover those requirements or those obligations.
4. Where a harmonised standard is adopted by a European standardisation organisation and proposed to the Commission for the publication of its reference in the Official Journal of the European Union, the Commission shall assess the harmonised standard in accordance with Regulation (EU) No 1025/2012. When reference to a harmonised standard is published in the Official Journal of the European Union, the Commission shall repeal the implementing acts referred to in paragraph 1, or parts thereof which cover the same requirements set out in Section 2 of this Chapter or, as applicable, the same obligations set out in Sections 2 and 3 of Chapter V.
5. Where providers of high-risk AI systems or general-purpose AI models do not comply with the common specifications referred to in paragraph 1, they shall duly justify that they have adopted technical solutions that meet the requirements referred to in Section 2 of this Chapter or, as applicable, comply with the obligations set out in Sections 2 and 3 of Chapter V to a level at least equivalent thereto.
6. Where a Member State considers that a common specification does not entirely meet the requirements set out in Section 2 or, as applicable, comply with obligations set out in Sections 2 and 3 of Chapter V, it shall inform the Commission thereof with a detailed explanation. The Commission shall assess that information and, if appropriate, amend the implementing act establishing the common specification concerned.
```

## Article 44 — Certificates

```text
1. Certificates issued by notified bodies in accordance with Annex VII shall be drawn-up in a language which can be easily understood by the relevant authorities in the Member State in which the notified body is established.
2. Certificates shall be valid for the period they indicate, which shall not exceed five years for AI systems covered by Annex I, and four years for AI systems covered by Annex III. At the request of the provider, the validity of a certificate may be extended for further periods, each not exceeding five years for AI systems covered by Annex I, and four years for AI systems covered by Annex III, based on a re-assessment in accordance with the applicable conformity assessment procedures. Any supplement to a certificate shall remain valid, provided that the certificate which it supplements is valid.
3. Where a notified body finds that an AI system no longer meets the requirements set out in Section 2, it shall, taking account of the principle of proportionality, suspend or withdraw the certificate issued or impose restrictions on it, unless compliance with those requirements is ensured by appropriate corrective action taken by the provider of the system within an appropriate deadline set by the notified body. The notified body shall give reasons for its decision.
An appeal procedure against decisions of the notified bodies, including on conformity certificates issued, shall be available.
```

## Article 47 — EU declaration of conformity

```text
1. The provider shall draw up a written machine readable, physical or electronically signed EU declaration of conformity for each high-risk AI system, and keep it at the disposal of the national competent authorities for 10 years after the high-risk AI system has been placed on the market or put into service. The EU declaration of conformity shall identify the high-risk AI system for which it has been drawn up. A copy of the EU declaration of conformity shall be submitted to the relevant national competent authorities upon request.
2. The EU declaration of conformity shall state that the high-risk AI system concerned meets the requirements set out in Section 2. The EU declaration of conformity shall contain the information set out in Annex V, and shall be translated into a language that can be easily understood by the national competent authorities of the Member States in which the high-risk AI system is placed on the market or made available.
3. Where high-risk AI systems are subject to other Union harmonisation legislation which also requires an EU declaration of conformity, a single EU declaration of conformity shall be drawn up in respect of all Union law applicable to the high-risk AI system. The declaration shall contain all the information required to identify the Union harmonisation legislation to which the declaration relates.
4. By drawing up the EU declaration of conformity, the provider shall assume responsibility for compliance with the requirements set out in Section 2. The provider shall keep the EU declaration of conformity up-to-date as appropriate.
5. The Commission is empowered to adopt delegated acts in accordance with Article 97 in order to amend Annex V by updating the content of the EU declaration of conformity set out in that Annex, in order to introduce elements that become necessary in light of technical progress.
```

## Article 48 — CE marking

```text
1. The CE marking shall be subject to the general principles set out in Article 30 of Regulation (EC) No 765/2008.
2. For high-risk AI systems provided digitally, a digital CE marking shall be used, only if it can easily be accessed via the interface from which that system is accessed or via an easily accessible machine-readable code or other electronic means.
3. The CE marking shall be affixed visibly, legibly and indelibly for high-risk AI systems. Where that is not possible or not warranted on account of the nature of the high-risk AI system, it shall be affixed to the packaging or to the accompanying documentation, as appropriate.
4. Where applicable, the CE marking shall be followed by the identification number of the notified body responsible for the conformity assessment procedures set out in Article 43. The identification number of the notified body shall be affixed by the body itself or, under its instructions, by the provider or by the provider’s authorised representative. The identification number shall also be indicated in any promotional material which mentions that the high-risk AI system fulfils the requirements for CE marking.
5. Where high-risk AI systems are subject to other Union law which also provides for the affixing of the CE marking, the CE marking shall indicate that the high-risk AI system also fulfil the requirements of that other law.
```

## Article 52 — Procedure

```text
1. Where a general-purpose AI model meets the condition referred to in Article 51(1), point (a), the relevant provider shall notify the Commission without delay and in any event within two weeks after that requirement is met or it becomes known that it will be met. That notification shall include the information necessary to demonstrate that the relevant requirement has been met. If the Commission becomes aware of a general-purpose AI model presenting systemic risks of which it has not been notified, it may decide to designate it as a model with systemic risk.
2. The provider of a general-purpose AI model that meets the condition referred to in Article 51(1), point (a), may present, with its notification, sufficiently substantiated arguments to demonstrate that, exceptionally, although it meets that requirement, the general-purpose AI model does not present, due to its specific characteristics, systemic risks and therefore should not be classified as a general-purpose AI model with systemic risk.
3. Where the Commission concludes that the arguments submitted pursuant to paragraph 2 are not sufficiently substantiated and the relevant provider was not able to demonstrate that the general-purpose AI model does not present, due to its specific characteristics, systemic risks, it shall reject those arguments, and the general-purpose AI model shall be considered to be a general-purpose AI model with systemic risk.
4. The Commission may designate a general-purpose AI model as presenting systemic risks, ex officio or following a qualified alert from the scientific panel pursuant to Article 90(1), point (a), on the basis of criteria set out in Annex XIII.
The Commission is empowered to adopt delegated acts in accordance with Article 97 in order to amend Annex XIII by specifying and updating the criteria set out in that Annex.
5. Upon a reasoned request of a provider whose model has been designated as a general-purpose AI model with systemic risk pursuant to paragraph 4, the Commission shall take the request into account and may decide to reassess whether the general-purpose AI model can still be considered to present systemic risks on the basis of the criteria set out in Annex XIII. Such a request shall contain objective, detailed and new reasons that have arisen since the designation decision. Providers may request reassessment at the earliest six months after the designation decision. Where the Commission, following its reassessment, decides to maintain the designation as a general-purpose AI model with systemic risk, providers may request reassessment at the earliest six months after that decision.
6. The Commission shall ensure that a list of general-purpose AI models with systemic risk is published and shall keep that list up to date, without prejudice to the need to observe and protect intellectual property rights and confidential business information or trade secrets in accordance with Union and national law.
```

## Article 53 — Obligations for providers of general-purpose AI models

```text
1. Providers of general-purpose AI models shall:
    (a) draw up and keep up-to-date the technical documentation of the model, including its training and testing process and the results of its evaluation, which shall contain, at a minimum, the information set out in Annex XI for the purpose of providing it, upon request, to the AI Office and the national competent authorities;
    (b) draw up, keep up-to-date and make available information and documentation to providers of AI systems who intend to integrate the general-purpose AI model into their AI systems. Without prejudice to the need to observe and protect intellectual property rights and confidential business information or trade secrets in accordance with Union and national law, the information and documentation shall:
        (i) enable providers of AI systems to have a good understanding of the capabilities and limitations of the general-purpose AI model and to comply with their obligations pursuant to this Regulation; and
        (ii) contain, at a minimum, the elements set out in Annex XII;
    (c) put in place a policy to comply with Union law on copyright and related rights, and in particular to identify and comply with, including through state-of-the-art technologies, a reservation of rights expressed pursuant to Article 4(3) of Directive (EU) 2019/790;
    (d) draw up and make publicly available a sufficiently detailed summary about the content used for training of the general-purpose AI model, according to a template provided by the AI Office.
2. The obligations set out in paragraph 1, points (a) and (b), shall not apply to providers of AI models that are released under a free and open-source licence that allows for the access, usage, modification, and distribution of the model, and whose parameters, including the weights, the information on the model architecture, and the information on model usage, are made publicly available. This exception shall not apply to general-purpose AI models with systemic risks.
3. Providers of general-purpose AI models shall cooperate as necessary with the Commission and the national competent authorities in the exercise of their competences and powers pursuant to this Regulation.
4. Providers of general-purpose AI models may rely on codes of practice within the meaning of Article 56 to demonstrate compliance with the obligations set out in paragraph 1 of this Article, until a harmonised standard is published. Compliance with European harmonised standards grants providers the presumption of conformity to the extent that those standards cover those obligations. Providers of general-purpose AI models who do not adhere to an approved code of practice or do not comply with a European harmonised standard shall demonstrate alternative adequate means of compliance for assessment by the Commission.
5. For the purpose of facilitating compliance with Annex XI, in particular points 2 (d) and (e) thereof, the Commission is empowered to adopt delegated acts in accordance with Article 97 to detail measurement and calculation methodologies with a view to allowing for comparable and verifiable documentation.
6. The Commission is empowered to adopt delegated acts in accordance with Article 97(2) to amend Annexes XI and XII in light of evolving technological developments.
7. Any information or documentation obtained pursuant to this Article, including trade secrets, shall be treated in accordance with the confidentiality obligations set out in Article 78.
```

## Article 54 — Authorised representatives of providers of general-purpose AI models

```text
1. Prior to placing a general-purpose AI model on the Union market, providers established in third countries shall, by written mandate, appoint an authorised representative which is established in the Union.
2. The provider shall enable its authorised representative to perform the tasks specified in the mandate received from the provider.
3. The authorised representative shall perform the tasks specified in the mandate received from the provider. It shall provide a copy of the mandate to the AI Office upon request, in one of the official languages of the institutions of the Union. For the purposes of this Regulation, the mandate shall empower the authorised representative to carry out the following tasks:
    (a) verify that the technical documentation specified in Annex XI has been drawn up and all obligations referred to in Article 53 and, where applicable, Article 55 have been fulfilled by the provider;
    (b) keep a copy of the technical documentation specified in Annex XI at the disposal of the AI Office and national competent authorities, for a period of 10 years after the general-purpose AI model has been placed on the market, and the contact details of the provider that appointed the authorised representative;
    (c) provide the AI Office, upon a reasoned request, with all the information and documentation, including that referred to in point (b), necessary to demonstrate compliance with the obligations in this Chapter;
    (d) cooperate with the AI Office and competent authorities, upon a reasoned request, in any action they take in relation to the general-purpose AI model, including when the model is integrated into AI systems placed on the market or put into service in the Union.
4. The mandate shall empower the authorised representative to be addressed, in addition to or instead of the provider, by the AI Office or the competent authorities, on all issues related to ensuring compliance with this Regulation.
5. The authorised representative shall terminate the mandate if it considers or has reason to consider the provider to be acting contrary to its obligations pursuant to this Regulation. In such a case, it shall also immediately inform the AI Office about the termination of the mandate and the reasons therefor.
6. The obligation set out in this Article shall not apply to providers of general-purpose AI models that are released under a free and open-source licence that allows for the access, usage, modification, and distribution of the model, and whose parameters, including the weights, the information on the model architecture, and the information on model usage, are made publicly available, unless the general-purpose AI models present systemic risks.
```

## Article 55 — Obligations of providers of general-purpose AI models with systemic risk

```text
1. In addition to the obligations listed in Articles 53 and 54, providers of general-purpose AI models with systemic risk shall:
    (a) perform model evaluation in accordance with standardised protocols and tools reflecting the state of the art, including conducting and documenting adversarial testing of the model with a view to identifying and mitigating systemic risks;
    (b) assess and mitigate possible systemic risks at Union level, including their sources, that may stem from the development, the placing on the market, or the use of general-purpose AI models with systemic risk;
    (c) keep track of, document, and report, without undue delay, to the AI Office and, as appropriate, to national competent authorities, relevant information about serious incidents and possible corrective measures to address them;
    (d) ensure an adequate level of cybersecurity protection for the general-purpose AI model with systemic risk and the physical infrastructure of the model.
2. Providers of general-purpose AI models with systemic risk may rely on codes of practice within the meaning of Article 56 to demonstrate compliance with the obligations set out in paragraph 1 of this Article, until a harmonised standard is published. Compliance with European harmonised standards grants providers the presumption of conformity to the extent that those standards cover those obligations. Providers of general-purpose AI models with systemic risks who do not adhere to an approved code of practice or do not comply with a European harmonised standard shall demonstrate alternative adequate means of compliance for assessment by the Commission.
3. Any information or documentation obtained pursuant to this Article, including trade secrets, shall be treated in accordance with the confidentiality obligations set out in Article 78.
```

## Article 56 — Codes of practice

```text
1. The AI Office shall encourage and facilitate the drawing up of codes of practice at Union level in order to contribute to the proper application of this Regulation, taking into account international approaches.
2. The AI Office and the Board shall aim to ensure that the codes of practice cover at least the obligations provided for in Articles 53 and 55, including the following issues:
    (a) the means to ensure that the information referred to in Article 53(1), points (a) and (b), is kept up to date in light of market and technological developments;
    (b) the adequate level of detail for the summary about the content used for training;
    (c) the identification of the type and nature of the systemic risks at Union level, including their sources, where appropriate;
    (d) the measures, procedures and modalities for the assessment and management of the systemic risks at Union level, including the documentation thereof, which shall be proportionate to the risks, take into consideration their severity and probability and take into account the specific challenges of tackling those risks in light of the possible ways in which such risks may emerge and materialise along the AI value chain.
3. The AI Office may invite all providers of general-purpose AI models, as well as relevant national competent authorities, to participate in the drawing-up of codes of practice. Civil society organisations, industry, academia and other relevant stakeholders, such as downstream providers and independent experts, may support the process.
4. The AI Office and the Board shall aim to ensure that the codes of practice clearly set out their specific objectives and contain commitments or measures, including key performance indicators as appropriate, to ensure the achievement of those objectives, and that they take due account of the needs and interests of all interested parties, including affected persons, at Union level.
5. The AI Office shall aim to ensure that participants to the codes of practice report regularly to the AI Office on the implementation of the commitments and the measures taken and their outcomes, including as measured against the key performance indicators as appropriate. Key performance indicators and reporting commitments shall reflect differences in size and capacity between various participants.
[▼M1]
6. The Commission and the Board shall regularly monitor and evaluate the achievement of the objectives of the codes of practice by the participants and their contribution to the proper application of this Regulation. The Commission, taking utmost account of the opinion of the Board, shall assess whether the codes of practice cover the obligations provided for in Articles 53 and 55, and shall regularly monitor and evaluate the achievement of their objectives. The Commission shall publish its assessment of the adequacy of the codes of practice.
[▼B]
7. The AI Office may invite all providers of general-purpose AI models to adhere to the codes of practice. For providers of general-purpose AI models not presenting systemic risks this adherence may be limited to the obligations provided for in Article 53, unless they declare explicitly their interest to join the full code.
8. The AI Office shall, as appropriate, also encourage and facilitate the review and adaptation of the codes of practice, in particular in light of emerging standards. The AI Office shall assist in the assessment of available standards.
9. Codes of practice shall be ready at the latest by 2 May 2025. The AI Office shall take the necessary steps, including inviting providers pursuant to paragraph 7.
If, by 2 August 2025, a code of practice cannot be finalised, or if the AI Office deems it is not adequate following its assessment under paragraph 6 of this Article, the Commission may provide, by means of implementing acts, common rules for the implementation of the obligations provided for in Articles 53 and 55, including the issues set out in paragraph 2 of this Article. Those implementing acts shall be adopted in accordance with the examination procedure referred to in Article 98(2).
```

## Article 57 — AI regulatory sandboxes

```text
[▼M1]
1. Member States shall ensure that their competent authorities establish at least one AI regulatory sandbox at national level, which shall be operational by 2 August 2027. That sandbox may also be established jointly with the competent authorities of other Member States. The Commission may provide technical support, advice and tools for the establishment and operation of AI regulatory sandboxes.
[▼B]
The obligation under the first subparagraph may also be fulfilled by participating in an existing sandbox in so far as that participation provides an equivalent level of national coverage for the participating Member States.
2. Additional AI regulatory sandboxes at regional or local level, or established jointly with the competent authorities of other Member States may also be established.
[▼M1]
3. The European Data Protection Supervisor may establish an AI regulatory sandbox for Union institutions, bodies, offices and agencies. For this purpose, references to national competent authorities in this Chapter shall be construed as references to the European Data Protection Supervisor.
[▼M1]
3a. The AI Office may establish an AI regulatory sandbox at Union level for AI systems covered by Article 75(1). For this purpose, references to national competent authorities in this Chapter shall be construed, where relevant, as references to the AI Office. That AI regulatory sandbox shall be implemented in close cooperation with relevant competent authorities, in particular where compliance with Union legislation other than this Regulation is supervised in the AI regulatory sandbox, and shall provide priority access to SMEs, including start-ups, and SMCs.
The establishment of a Union level AI regulatory sandbox by the AI Office shall be without prejudice to the competences of Member States to establish and supervise AI regulatory sandboxes for AI systems under their supervision.
[▼B]
4. Member States shall ensure that the competent authorities referred to in paragraphs 1 and 2 allocate sufficient resources to comply with this Article effectively and in a timely manner. Where appropriate, national competent authorities shall cooperate with other relevant authorities, and may allow for the involvement of other actors within the AI ecosystem. This Article shall not affect other regulatory sandboxes established under Union or national law. Member States shall ensure an appropriate level of cooperation between the authorities supervising those other sandboxes and the national competent authorities.
[▼M1]
5. AI regulatory sandboxes established under this Article shall provide for a controlled environment that fosters innovation and facilitates the development, training, testing and validation of innovative AI systems for a limited time before their being placed on the market or put into service pursuant to a specific sandbox plan agreed between the providers or prospective providers and the competent authorities, ensuring that appropriate safeguards are in place. Such sandboxes may include testing in real world conditions supervised therein. Where applicable, the sandbox plan shall incorporate the real-world testing plan referred to in Articles 60 and 60a.
[▼B]
6. Competent authorities shall provide, as appropriate, guidance, supervision and support within the AI regulatory sandbox with a view to identifying risks, in particular to fundamental rights, health and safety, testing, mitigation measures, and their effectiveness in relation to the obligations and requirements of this Regulation and, where relevant, other Union and national law supervised within the sandbox.
7. Competent authorities shall provide providers and prospective providers participating in the AI regulatory sandbox with guidance on regulatory expectations and how to fulfil the requirements and obligations set out in this Regulation.
Upon request of the provider or prospective provider of the AI system, the competent authority shall provide a written proof of the activities successfully carried out in the sandbox. The competent authority shall also provide an exit report detailing the activities carried out in the sandbox and the related results and learning outcomes. Providers may use such documentation to demonstrate their compliance with this Regulation through the conformity assessment process or relevant market surveillance activities. In this regard, the exit reports and the written proof provided by the national competent authority shall be taken positively into account by market surveillance authorities and notified bodies, with a view to accelerating conformity assessment procedures to a reasonable extent.
8. Subject to the confidentiality provisions in Article 78, and with the agreement of the provider or prospective provider, the Commission and the Board shall be authorised to access the exit reports and shall take them into account, as appropriate, when exercising their tasks under this Regulation. If both the provider or prospective provider and the national competent authority explicitly agree, the exit report may be made publicly available through the single information platform referred to in this Article.
9. The establishment of AI regulatory sandboxes shall aim to contribute to the following objectives:
    (a) improving legal certainty to achieve regulatory compliance with this Regulation or, where relevant, other applicable Union and national law;
    (b) supporting the sharing of best practices through cooperation with the authorities involved in the AI regulatory sandbox;
    (c) fostering innovation and competitiveness and facilitating the development of an AI ecosystem;
    (d) contributing to evidence-based regulatory learning;
[▼M1]
    (e) facilitating and accelerating access to the Union market for AI systems, in particular when provided by SMEs, including start-ups, and SMCs.
10. National competent authorities shall ensure that, to the extent the innovative AI systems involve the processing of personal data or otherwise fall under the supervisory remit of other national authorities or competent authorities providing or supporting access to data, the competent data protection authorities and those other national or competent authorities are associated with the operation of the AI regulatory sandbox and involved in the supervision of those aspects to the extent of their respective tasks and powers.
[▼B]
11. The AI regulatory sandboxes shall not affect the supervisory or corrective powers of the competent authorities supervising the sandboxes, including at regional or local level. Any significant risks to health and safety and fundamental rights identified during the development and testing of such AI systems shall result in an adequate mitigation. National competent authorities shall have the power to temporarily or permanently suspend the testing process, or the participation in the sandbox if no effective mitigation is possible, and shall inform the AI Office of such decision. National competent authorities shall exercise their supervisory powers within the limits of the relevant law, using their discretionary powers when implementing legal provisions in respect of a specific AI regulatory sandbox project, with the objective of supporting innovation in AI in the Union.
12. Providers and prospective providers participating in the AI regulatory sandbox shall remain liable under applicable Union and national liability law for any damage inflicted on third parties as a result of the experimentation taking place in the sandbox. However, provided that the prospective providers observe the specific plan and the terms and conditions for their participation and follow in good faith the guidance given by the national competent authority, no administrative fines shall be imposed by the authorities for infringements of this Regulation. Where other competent authorities responsible for other Union and national law were actively involved in the supervision of the AI system in the sandbox and provided guidance for compliance, no administrative fines shall be imposed regarding that law.
13. The AI regulatory sandboxes shall be designed and implemented in such a way that, where relevant, they facilitate cross-border cooperation between national competent authorities.
[▼M1]
14. National competent authorities, the European Data Protection Supervisor and the AI Office, shall, as appropriate and within their respective competences, coordinate their activities and cooperate within the framework of the Board. They may support the joint establishment and operation of AI regulatory sandboxes, including in different sectors, and exchange best practices on related matters.
[▼B]
15. National competent authorities shall inform the AI Office and the Board of the establishment of a sandbox, and may ask them for support and guidance. The AI Office shall make publicly available a list of planned and existing sandboxes and keep it up to date in order to encourage more interaction in the AI regulatory sandboxes and cross-border cooperation.
16. National competent authorities shall submit annual reports to the AI Office and to the Board, from one year after the establishment of the AI regulatory sandbox and every year thereafter until its termination, and a final report. Those reports shall provide information on the progress and results of the implementation of those sandboxes, including best practices, incidents, lessons learnt and recommendations on their setup and, where relevant, on the application and possible revision of this Regulation, including its delegated and implementing acts, and on the application of other Union law supervised by the competent authorities within the sandbox. The national competent authorities shall make those annual reports or abstracts thereof available to the public, online. The Commission shall, where appropriate, take the annual reports into account when exercising its tasks under this Regulation.
17. The Commission shall develop a single and dedicated interface containing all relevant information related to AI regulatory sandboxes to allow stakeholders to interact with AI regulatory sandboxes and to raise enquiries with competent authorities, and to seek non-binding guidance on the conformity of innovative products, services, business models embedding AI technologies, in accordance with Article 62(1), point (c). The Commission shall proactively coordinate with national competent authorities, where relevant.
```

## Article 64 — AI Office

```text
1. The Commission shall develop Union expertise and capabilities in the field of AI through the AI Office.
2. Member States shall facilitate the tasks entrusted to the AI Office, as reflected in this Regulation.
[▼M1]
3. Without prejudice to the budgetary procedure, the AI Office shall be allocated adequate resources to effectively perform its duties and exercise its powers in relation to the enforcement of this Regulation.
[▼B]
```

## Article 88 — Enforcement of the obligations of providers of general-purpose AI models

```text
1. The Commission shall have exclusive powers to supervise and enforce Chapter V, taking into account the procedural guarantees under Article 94. The Commission shall entrust the implementation of these tasks to the AI Office, without prejudice to the powers of organisation of the Commission and the division of competences between Member States and the Union based on the Treaties.
2. Without prejudice to Article 75(3), market surveillance authorities may request the Commission to exercise the powers laid down in this Section, where that is necessary and proportionate to assist with the fulfilment of their tasks under this Regulation.
```

## Article 100 — Administrative fines on Union institutions, bodies, offices and agencies

```text
1. The European Data Protection Supervisor may impose administrative fines on Union institutions, bodies, offices and agencies falling within the scope of this Regulation. When deciding whether to impose an administrative fine and when deciding on the amount of the administrative fine in each individual case, all relevant circumstances of the specific situation shall be taken into account and due regard shall be given to the following:
    (a) the nature, gravity and duration of the infringement and of its consequences, taking into account the purpose of the AI system concerned, as well as, where appropriate, the number of affected persons and the level of damage suffered by them;
    (b) the degree of responsibility of the Union institution, body, office or agency, taking into account technical and organisational measures implemented by them;
    (c) any action taken by the Union institution, body, office or agency to mitigate the damage suffered by affected persons;
    (d) the degree of cooperation with the European Data Protection Supervisor in order to remedy the infringement and mitigate the possible adverse effects of the infringement, including compliance with any of the measures previously ordered by the European Data Protection Supervisor against the Union institution, body, office or agency concerned with regard to the same subject matter;
    (e) any similar previous infringements by the Union institution, body, office or agency;
    (f) the manner in which the infringement became known to the European Data Protection Supervisor, in particular whether, and if so to what extent, the Union institution, body, office or agency notified the infringement;
    (g) the annual budget of the Union institution, body, office or agency.
2. Non-compliance with the prohibition of the AI practices referred to in Article 5 shall be subject to administrative fines of up to EUR 1 500 000 .
3. The non-compliance of the AI system with any requirements or obligations under this Regulation, other than those laid down in Article 5, shall be subject to administrative fines of up to EUR 750 000 .
4. Before taking decisions pursuant to this Article, the European Data Protection Supervisor shall give the Union institution, body, office or agency which is the subject of the proceedings conducted by the European Data Protection Supervisor the opportunity of being heard on the matter regarding the possible infringement. The European Data Protection Supervisor shall base his or her decisions only on elements and circumstances on which the parties concerned have been able to comment. Complainants, if any, shall be associated closely with the proceedings.
5. The rights of defence of the parties concerned shall be fully respected in the proceedings. They shall be entitled to have access to the European Data Protection Supervisor’s file, subject to the legitimate interest of individuals or undertakings in the protection of their personal data or business secrets.
6. Funds collected by imposition of fines in this Article shall contribute to the general budget of the Union. The fines shall not affect the effective operation of the Union institution, body, office or agency fined.
7. The European Data Protection Supervisor shall, on an annual basis, notify the Commission of the administrative fines it has imposed pursuant to this Article and of any litigation or judicial proceedings it has initiated.
```

## ANNEX XI — Technical documentation referred to in Article 53(1), point (a) — technical documentation for providers of general-purpose AI models

```text
Section 1
Information to be provided by all providers of general-purpose AI models
The technical documentation referred to in Article 53(1), point (a) shall contain at least the following information as appropriate to the size and risk profile of the model:
    1. A general description of the general-purpose AI model including:
        (a) the tasks that the model is intended to perform and the type and nature of AI systems in which it can be integrated;
        (b) the acceptable use policies applicable;
        (c) the date of release and methods of distribution;
        (d) the architecture and number of parameters;
        (e) the modality (e.g. text, image) and format of inputs and outputs;
        (f) the licence.
    2. A detailed description of the elements of the model referred to in point 1, and relevant information of the process for the development, including the following elements:
        (a) the technical means (e.g. instructions of use, infrastructure, tools) required for the general-purpose AI model to be integrated in AI systems;
        (b) the design specifications of the model and training process, including training methodologies and techniques, the key design choices including the rationale and assumptions made; what the model is designed to optimise for and the relevance of the different parameters, as applicable;
        (c) information on the data used for training, testing and validation, where applicable, including the type and provenance of data and curation methodologies (e.g. cleaning, filtering, etc.), the number of data points, their scope and main characteristics; how the data was obtained and selected as well as all other measures to detect the unsuitability of data sources and methods to detect identifiable biases, where applicable;
        (d) the computational resources used to train the model (e.g. number of floating point operations), training time, and other relevant details related to the training;
        (e) known or estimated energy consumption of the model.
    With regard to point (e), where the energy consumption of the model is unknown, the energy consumption may be based on information about computational resources used.
Section 2
Additional information to be provided by providers of general-purpose AI models with systemic risk
1. A detailed description of the evaluation strategies, including evaluation results, on the basis of available public evaluation protocols and tools or otherwise of other evaluation methodologies. Evaluation strategies shall include evaluation criteria, metrics and the methodology on the identification of limitations.
2. Where applicable, a detailed description of the measures put in place for the purpose of conducting internal and/or external adversarial testing (e.g. red teaming), model adaptations, including alignment and fine-tuning.
3. Where applicable, a detailed description of the system architecture explaining how software components build or feed into each other and integrate into the overall processing.
```

## ANNEX XII — Transparency information referred to in Article 53(1), point (b) — technical documentation for providers of general-purpose AI models to downstream providers that integrate the model into their AI system

```text
The information referred to in Article 53(1), point (b) shall contain at least the following:
    1. A general description of the general-purpose AI model including:
        (a) the tasks that the model is intended to perform and the type and nature of AI systems into which it can be integrated;
        (b) the acceptable use policies applicable;
        (c) the date of release and methods of distribution;
        (d) how the model interacts, or can be used to interact, with hardware or software that is not part of the model itself, where applicable;
        (e) the versions of relevant software related to the use of the general-purpose AI model, where applicable;
        (f) the architecture and number of parameters;
        (g) the modality (e.g. text, image) and format of inputs and outputs;
        (h) the licence for the model.
    2. A description of the elements of the model and of the process for its development, including:
        (a) the technical means (e.g. instructions for use, infrastructure, tools) required for the general-purpose AI model to be integrated into AI systems;
        (b) the modality (e.g. text, image, etc.) and format of the inputs and outputs and their maximum size (e.g. context window length, etc.);
        (c) information on the data used for training, testing and validation, where applicable, including the type and provenance of data and curation methodologies.
```

## Article 3 in full — every definition, because the series runs on them

Part one carried only 3(63)–(67). The first plan reached for **3(9) 'placing on the market'** and
**3(10) 'making available on the market'** — the concept its own through-line rests on — and this
docket did not contain either. Add `--select "Article 3"` to the command above to regenerate.

```text
For the purposes of this Regulation, the following definitions apply:
    (1) ‘AI system’ means a machine-based system that is designed to operate with varying levels of autonomy and that may exhibit adaptiveness after deployment, and that, for explicit or implicit objectives, infers, from the input it receives, how to generate outputs such as predictions, content, recommendations, or decisions that can influence physical or virtual environments;
    (2) ‘risk’ means the combination of the probability of an occurrence of harm and the severity of that harm;
    (3) ‘provider’ means a natural or legal person, public authority, agency or other body that develops an AI system or a general-purpose AI model or that has an AI system or a general-purpose AI model developed and places it on the market or puts the AI system into service under its own name or trademark, whether for payment or free of charge;
    (4) ‘deployer’ means a natural or legal person, public authority, agency or other body using an AI system under its authority except where the AI system is used in the course of a personal non-professional activity;
    (5) ‘authorised representative’ means a natural or legal person located or established in the Union who has received and accepted a written mandate from a provider of an AI system or a general-purpose AI model to, respectively, perform and carry out on its behalf the obligations and procedures established by this Regulation;
    (6) ‘importer’ means a natural or legal person located or established in the Union that places on the market an AI system that bears the name or trademark of a natural or legal person established in a third country;
    (7) ‘distributor’ means a natural or legal person in the supply chain, other than the provider or the importer, that makes an AI system available on the Union market;
    (8) ‘operator’ means a provider, product manufacturer, deployer, authorised representative, importer or distributor;
    (9) ‘placing on the market’ means the first making available of an AI system or a general-purpose AI model on the Union market;
    (10) ‘making available on the market’ means the supply of an AI system or a general-purpose AI model for distribution or use on the Union market in the course of a commercial activity, whether in return for payment or free of charge;
    (11) ‘putting into service’ means the supply of an AI system for first use directly to the deployer or for own use in the Union for its intended purpose;
    (12) ‘intended purpose’ means the use for which an AI system is intended by the provider, including the specific context and conditions of use, as specified in the information supplied by the provider in the instructions for use, promotional or sales materials and statements, as well as in the technical documentation;
    (13) ‘reasonably foreseeable misuse’ means the use of an AI system in a way that is not in accordance with its intended purpose, but which may result from reasonably foreseeable human behaviour or interaction with other systems, including other AI systems;
[▼M1]
    (14) ‘safety component’ means a component of a product or of an AI system which fulfils a safety function for that product or AI system, or the failure or malfunctioning of which endangers the health and safety of persons or property; for the purposes of this definition, a component fulfils a safety function where its intended purpose is to prevent or mitigate risks to health and safety of persons or property;
[▼M1]
    (14a) ‘micro, small and medium-sized enterprise’ or ‘SME’ means a micro, small or medium-sized enterprise as defined in Article 2 of the Annex to Recommendation 2003/361/EC;
    (14b) ‘small mid-cap enterprise’ or ‘SMC’ means a small mid-cap enterprise as defined in point (2) of the Annex to Recommendation (EU) 2025/1099;
[▼B]
    (15) ‘instructions for use’ means the information provided by the provider to inform the deployer of, in particular, an AI system’s intended purpose and proper use;
    (16) ‘recall of an AI system’ means any measure aiming to achieve the return to the provider or taking out of service or disabling the use of an AI system made available to deployers;
    (17) ‘withdrawal of an AI system’ means any measure aiming to prevent an AI system in the supply chain being made available on the market;
    (18) ‘performance of an AI system’ means the ability of an AI system to achieve its intended purpose;
    (19) ‘notifying authority’ means the national authority responsible for setting up and carrying out the necessary procedures for the assessment, designation and notification of conformity assessment bodies and for their monitoring;
    (20) ‘conformity assessment’ means the process of demonstrating whether the requirements set out in Chapter III, Section 2 relating to a high-risk AI system have been fulfilled;
    (21) ‘conformity assessment body’ means a body that performs third-party conformity assessment activities, including testing, certification and inspection;
    (22) ‘notified body’ means a conformity assessment body notified in accordance with this Regulation and other relevant Union harmonisation legislation;
    (23) ‘substantial modification’ means a change to an AI system after its placing on the market or putting into service which is not foreseen or planned in the initial conformity assessment carried out by the provider and as a result of which the compliance of the AI system with the requirements set out in Chapter III, Section 2 is affected or results in a modification to the intended purpose for which the AI system has been assessed;
    (24) ‘CE marking’ means a marking by which a provider indicates that an AI system is in conformity with the requirements set out in Chapter III, Section 2 and other applicable Union harmonisation legislation providing for its affixing;
    (25) ‘post-market monitoring system’ means all activities carried out by providers of AI systems to collect and review experience gained from the use of AI systems they place on the market or put into service for the purpose of identifying any need to immediately apply any necessary corrective or preventive actions;
    (26) ‘market surveillance authority’ means the national authority carrying out the activities and taking the measures pursuant to Regulation (EU) 2019/1020;
    (27) ‘harmonised standard’ means a harmonised standard as defined in Article 2(1), point (c), of Regulation (EU) No 1025/2012;
    (28) ‘common specification’ means a set of technical specifications as defined in Article 2, point (4) of Regulation (EU) No 1025/2012, providing means to comply with certain requirements established under this Regulation;
    (29) ‘training data’ means data used for training an AI system through fitting its learnable parameters;
    (30) ‘validation data’ means data used for providing an evaluation of the trained AI system and for tuning its non-learnable parameters and its learning process in order, inter alia, to prevent underfitting or overfitting;
    (31) ‘validation data set’ means a separate data set or part of the training data set, either as a fixed or variable split;
    (32) ‘testing data’ means data used for providing an independent evaluation of the AI system in order to confirm the expected performance of that system before its placing on the market or putting into service;
    (33) ‘input data’ means data provided to or directly acquired by an AI system on the basis of which the system produces an output;
    (34) ‘biometric data’ means personal data resulting from specific technical processing relating to the physical, physiological or behavioural characteristics of a natural person, such as facial images or dactyloscopic data;
    (35) ‘biometric identification’ means the automated recognition of physical, physiological, behavioural, or psychological human features for the purpose of establishing the identity of a natural person by comparing biometric data of that individual to biometric data of individuals stored in a database;
    (36) ‘biometric verification’ means the automated, one-to-one verification, including authentication, of the identity of natural persons by comparing their biometric data to previously provided biometric data;
    (37) ‘special categories of personal data’ means the categories of personal data referred to in Article 9(1) of Regulation (EU) 2016/679, Article 10 of Directive (EU) 2016/680 and Article 10(1) of Regulation (EU) 2018/1725;
    (38) ‘sensitive operational data’ means operational data related to activities of prevention, detection, investigation or prosecution of criminal offences, the disclosure of which could jeopardise the integrity of criminal proceedings;
    (39) ‘emotion recognition system’ means an AI system for the purpose of identifying or inferring emotions or intentions of natural persons on the basis of their biometric data;
    (40) ‘biometric categorisation system’ means an AI system for the purpose of assigning natural persons to specific categories on the basis of their biometric data, unless it is ancillary to another commercial service and strictly necessary for objective technical reasons;
    (41) ‘remote biometric identification system’ means an AI system for the purpose of identifying natural persons, without their active involvement, typically at a distance through the comparison of a person’s biometric data with the biometric data contained in a reference database;
    (42) ‘real-time remote biometric identification system’ means a remote biometric identification system, whereby the capturing of biometric data, the comparison and the identification all occur without a significant delay, comprising not only instant identification, but also limited short delays in order to avoid circumvention;
    (43) ‘post-remote biometric identification system’ means a remote biometric identification system other than a real-time remote biometric identification system;
    (44) ‘publicly accessible space’ means any publicly or privately owned physical place accessible to an undetermined number of natural persons, regardless of whether certain conditions for access may apply, and regardless of the potential capacity restrictions;
    (45) ‘law enforcement authority’ means:
        (a) any public authority competent for the prevention, investigation, detection or prosecution of criminal offences or the execution of criminal penalties, including the safeguarding against and the prevention of threats to public security; or
        (b) any other body or entity entrusted by Member State law to exercise public authority and public powers for the purposes of the prevention, investigation, detection or prosecution of criminal offences or the execution of criminal penalties, including the safeguarding against and the prevention of threats to public security;
    (46) ‘law enforcement’ means activities carried out by law enforcement authorities or on their behalf for the prevention, investigation, detection or prosecution of criminal offences or the execution of criminal penalties, including safeguarding against and preventing threats to public security;
    (47) ‘AI Office’ means the Commission’s function of contributing to the implementation, monitoring and supervision of AI systems and general-purpose AI models, and AI governance, provided for in Commission Decision of 24 January 2024; references in this Regulation to the AI Office shall be construed as references to the Commission;
    (48) ‘national competent authority’ means a notifying authority or a market surveillance authority; as regards AI systems put into service or used by Union institutions, agencies, offices and bodies, references to national competent authorities or market surveillance authorities in this Regulation shall be construed as references to the European Data Protection Supervisor;
    (49) ‘serious incident’ means an incident or malfunctioning of an AI system that directly or indirectly leads to any of the following:
        (a) the death of a person, or serious harm to a person’s health;
        (b) a serious and irreversible disruption of the management or operation of critical infrastructure;
        (c) the infringement of obligations under Union law intended to protect fundamental rights;
        (d) serious harm to property or the environment;
    (50) ‘personal data’ means personal data as defined in Article 4, point (1), of Regulation (EU) 2016/679;
    (51) ‘non-personal data’ means data other than personal data as defined in Article 4, point (1), of Regulation (EU) 2016/679;
    (52) ‘profiling’ means profiling as defined in Article 4, point (4), of Regulation (EU) 2016/679;
    (53) ‘real-world testing plan’ means a document that describes the objectives, methodology, geographical, population and temporal scope, monitoring, organisation and conduct of testing in real-world conditions;
    (54) ‘sandbox plan’ means a document agreed between the participating provider and the competent authority describing the objectives, conditions, timeframe, methodology and requirements for the activities carried out within the sandbox;
    (55) ‘AI regulatory sandbox’ means a controlled framework set up by a competent authority which offers providers or prospective providers of AI systems the possibility to develop, train, validate and test, where appropriate in real-world conditions, an innovative AI system, pursuant to a sandbox plan for a limited time under regulatory supervision;
    (56) ‘AI literacy’ means skills, knowledge and understanding that allow providers, deployers and affected persons, taking into account their respective rights and obligations in the context of this Regulation, to make an informed deployment of AI systems, as well as to gain awareness about the opportunities and risks of AI and possible harm it can cause;
    (57) ‘testing in real-world conditions’ means the temporary testing of an AI system for its intended purpose in real-world conditions outside a laboratory or otherwise simulated environment, with a view to gathering reliable and robust data and to assessing and verifying the conformity of the AI system with the requirements of this Regulation and it does not qualify as placing the AI system on the market or putting it into service within the meaning of this Regulation, provided that all the conditions laid down in Article 57 or 60 are fulfilled;
    (58) ‘subject’, for the purpose of real-world testing, means a natural person who participates in testing in real-world conditions;
    (59) ‘informed consent’ means a subject’s freely given, specific, unambiguous and voluntary expression of his or her willingness to participate in a particular testing in real-world conditions, after having been informed of all aspects of the testing that are relevant to the subject’s decision to participate;
    (60) ‘deep fake’ means AI-generated or manipulated image, audio or video content that resembles existing persons, objects, places, entities or events and would falsely appear to a person to be authentic or truthful;
    (61) ‘widespread infringement’ means any act or omission contrary to Union law protecting the interest of individuals, which:
        (a) has harmed or is likely to harm the collective interests of individuals residing in at least two Member States other than the Member State in which:
            (i) the act or omission originated or took place;
            (ii) the provider concerned, or, where applicable, its authorised representative is located or established; or
            (iii) the deployer is established, when the infringement is committed by the deployer;
        (b) has caused, causes or is likely to cause harm to the collective interests of individuals and has common features, including the same unlawful practice or the same interest being infringed, and is occurring concurrently, committed by the same operator, in at least three Member States;
    (62) ‘critical infrastructure’ means critical infrastructure as defined in Article 2, point (4), of Directive (EU) 2022/2557;
    (63) ‘general-purpose AI model’ means an AI model, including where such an AI model is trained with a large amount of data using self-supervision at scale, that displays significant generality and is capable of competently performing a wide range of distinct tasks regardless of the way the model is placed on the market and that can be integrated into a variety of downstream systems or applications, except AI models that are used for research, development or prototyping activities before they are placed on the market;
    (64) ‘high-impact capabilities’ means capabilities that match or exceed the capabilities recorded in the most advanced general-purpose AI models;
    (65) ‘systemic risk’ means a risk that is specific to the high-impact capabilities of general-purpose AI models, having a significant impact on the Union market due to their reach, or due to actual or reasonably foreseeable negative effects on public health, safety, public security, fundamental rights, or the society as a whole, that can be propagated at scale across the value chain;
    (66) ‘general-purpose AI system’ means an AI system which is based on a general-purpose AI model and which has the capability to serve a variety of purposes, both for direct use as well as for integration in other AI systems;
    (67) ‘floating-point operation’ means any mathematical operation or assignment involving floating-point numbers, which are a subset of the real numbers typically represented on computers by an integer of fixed precision scaled by an integer exponent of a fixed base;
    (68) ‘downstream provider’ means a provider of an AI system, including a general-purpose AI system, which integrates an AI model, regardless of whether the AI model is provided by themselves and vertically integrated or provided by another entity based on contractual relations.
```

## Articles 1 and 2 — subject matter and scope

Episode 1 teaches these and the docket did not contain them, so its writer quoted Art. 2(1)(c)
out of `06_primary_text.md` — the file headed SUPERSEDED and explicitly marked not quotable. The
editor caught it. This closes the hole. Note the exclusion paragraphs in Art. 2(3)–(12): Episode 1
names several aloud, and only these are the Act's own words.

```text
1. The purpose of this Regulation is to improve the functioning of the internal market and promote the uptake of human-centric and trustworthy artificial intelligence (AI), while ensuring a high level of protection of health, safety, fundamental rights enshrined in the Charter, including democracy, the rule of law and environmental protection, against the harmful effects of AI systems in the Union and supporting innovation.
2. This Regulation lays down:
    (a) harmonised rules for the placing on the market, the putting into service, and the use of AI systems in the Union;
    (b) prohibitions of certain AI practices;
    (c) specific requirements for high-risk AI systems and obligations for operators of such systems;
    (d) harmonised transparency rules for certain AI systems;
    (e) harmonised rules for the placing on the market of general-purpose AI models;
    (f) rules on market monitoring, market surveillance, governance and enforcement;
[▼M1]
    (g) measures to support innovation, with a particular focus on small mid-cap enterprises (SMCs) and small and medium-sized enterprises (SMEs), including start-ups.
[▼B]
```

## Article 2 — Scope

```text
1. This Regulation applies to:
    (a) providers placing on the market or putting into service AI systems or placing on the market general-purpose AI models in the Union, irrespective of whether those providers are established or located within the Union or in a third country;
    (b) deployers of AI systems that have their place of establishment or are located within the Union;
    (c) providers and deployers of AI systems that have their place of establishment or are located in a third country, where the output produced by the AI system is used in the Union;
    (d) importers and distributors of AI systems;
    (e) product manufacturers placing on the market or putting into service an AI system together with their product and under their own name or trademark;
    (f) authorised representatives of providers, which are not established in the Union;
    (g) affected persons that are located in the Union.
[▼M1]
2. For AI systems classified as high-risk AI systems in accordance with Article 6(1) related to products covered by the Union harmonisation legislation listed in Section B of Annex I, only Article 6(1), Article 60a and Articles 102 to 112 shall apply. Articles 57, 58 and 59 shall apply only in so far as the requirements for high-risk AI systems under this Regulation have been integrated in that Union harmonisation legislation.
[▼B]
3. This Regulation does not apply to areas outside the scope of Union law, and shall not, in any event, affect the competences of the Member States concerning national security, regardless of the type of entity entrusted by the Member States with carrying out tasks in relation to those competences.
This Regulation does not apply to AI systems where and in so far they are placed on the market, put into service, or used with or without modification exclusively for military, defence or national security purposes, regardless of the type of entity carrying out those activities.
This Regulation does not apply to AI systems which are not placed on the market or put into service in the Union, where the output is used in the Union exclusively for military, defence or national security purposes, regardless of the type of entity carrying out those activities.
4. This Regulation applies neither to public authorities in a third country nor to international organisations falling within the scope of this Regulation pursuant to paragraph 1, where those authorities or organisations use AI systems in the framework of international cooperation or agreements for law enforcement and judicial cooperation with the Union or with one or more Member States, provided that such a third country or international organisation provides adequate safeguards with respect to the protection of fundamental rights and freedoms of individuals.
5. This Regulation shall not affect the application of the provisions on the liability of providers of intermediary services as set out in Chapter II of Regulation (EU) 2022/2065.
6. This Regulation does not apply to AI systems or AI models, including their output, specifically developed and put into service for the sole purpose of scientific research and development.
[▼M1]
7. Union law on the protection of personal data, privacy and the confidentiality of communications applies to personal data processed in connection with the rights and obligations laid down in this Regulation. Without prejudice to Articles 4a and 59 of this Regulation, this Regulation shall not affect Regulation (EU) 2016/679 or (EU) 2018/1725, or Directive 2002/58/EC or (EU) 2016/680.
[▼B]
8. This Regulation does not apply to any research, testing or development activity regarding AI systems or AI models prior to their being placed on the market or put into service. Such activities shall be conducted in accordance with applicable Union law. Testing in real world conditions shall not be covered by that exclusion.
9. This Regulation is without prejudice to the rules laid down by other Union legal acts related to consumer protection and product safety.
10. This Regulation does not apply to obligations of deployers who are natural persons using AI systems in the course of a purely personal non-professional activity.
11. This Regulation does not preclude the Union or Member States from maintaining or introducing laws, regulations or administrative provisions which are more favourable to workers in terms of protecting their rights in respect of the use of AI systems by employers, or from encouraging or allowing the application of collective agreements which are more favourable to workers.
12. This Regulation does not apply to AI systems released under free and open-source licences, unless they are placed on the market or put into service as high-risk AI systems or as an AI system that falls under Article 5 or 50.
[▼M1]
13. For high-risk AI systems referred to in Article 6(1), the application of specific requirements or obligations laid down in Articles 9 to 15 and 17 to 25 may be limited, where and to the extent that:
    (a) Union harmonisation legislation listed in Section A of Annex I lays down requirements or obligations providing an equivalent or higher level of protection of health, safety or fundamental rights as the requirement or obligation concerned; and
    (b) such limitation does not reduce the overall level of protection provided for by this Regulation.
By 2 August 2027, the Commission shall adopt delegated acts in accordance with Article 97 in order to supplement this Regulation by specifying the high-risk AI systems concerned, the requirements or obligations that may be limited, the conditions under which such limitation applies, and the scope of the limitation.
[▼B]
```
