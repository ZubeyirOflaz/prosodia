---
episode: 4
title: The Ladder
defaults: { tone: measured, rate: normal }
---

## A car that can tell when it is being examined {tone: tense}

A test cell, somewhere in Europe. A car sits on a rolling road with its front wheels turning and its body going nowhere. There is a probe in the exhaust pipe. Nobody is driving it.

The test cycle is a fixed sequence — the same speeds, held for the same durations, in the same order, every time. That is what makes it a test rather than a drive. And a sequence that fixed has a signature: a narrow band of conditions, repeated exactly, that ordinary use on a road almost never reproduces.

The engine management software could tell the difference.

On the rig, it ran the emissions control system at full strength, everything the car had, working properly. Out on a road, with somebody actually steering, it backed that control off.

{pause: 1.4}

In 2015 this became public knowledge. Volkswagen. Roughly eight and a half million affected cars in Europe.

The thing to carry through the next half hour is duller than the deception, though — and far more useful than a scandal.

Nobody had to decide whether that car was inside the reach of the law.

It already was.

## Where this sits {tone: measured}

This is *The Instrument*, a series on the European Union's Artificial Intelligence Act — what it does, what it assumes, and whether any of it can be made to work. This is the fourth part.

You are carrying two things from earlier. The definitional gate — whether a piece of software infers at all, or only applies rules that a person wrote down. And the roles: provider and deployer, and the fact that duties attach when a system is placed on the market, not when it starts hurting somebody.

Today the system is through the gate and somebody owns it, so the Act has to sort it. It has to decide how much law this particular thing attracts.

That sorting is done by a single article and two annexes, and it is the most consequential piece of machinery in the whole Regulation. Get the sorting wrong and every obligation downstream lands on the wrong object.

What I will do today is take the sorting apart, and then show you the one thing it cannot see.

## What the software was doing, in its own terms {tone: precise}

Back to the car for a moment, because the mechanism matters before the law does.

The engineering term for that arrangement is a *defeat device*, and it is the field's own word rather than mine. It sits in European vehicle emissions law, in Article 5(2) of Regulation 715/2007, which is where such devices are prohibited. A defeat device is control software that detects the operating conditions characteristic of the approval test and changes the emissions strategy accordingly.

One version of it — the version that later reached the European courts — ran full exhaust-gas recirculation only between fifteen and thirty-three degrees Celsius, and only below a thousand metres. Outside that window, nitrogen oxides rose past the limits.

A disclosure now, because I would rather make it early than have you wondering. That software was not an AI system: it inferred nothing, and it was a set of conditions somebody had written down. The AI Act did not exist in 2015 either, so nothing I say today is a claim that the Act applied to Volkswagen.

What I am borrowing is the *route*, not the software — the road that car travelled to reach a market, because the AI Act now uses that same road, and almost nobody talks about it.

## The word the whole structure rests on {tone: measured}

Before the ladder, one word has to be nailed down.

When you hear *risk* in ordinary speech, you probably hear *danger*: a thing that might hurt you. That is not what the Regulation means, and the difference is load-bearing.

Article 3 carries sixty-eight definitions, and the second of them is this.

## Definition two {tone: quoting, rate: slow}

Quote. *Risk means the combination of the probability of an occurrence of harm and the severity of that harm.* End of quote.

## Two ingredients {tone: measured}

How likely, and how bad.

Set that out in ordinary language: risk here is not a property that a thing has. It is a product of two quantities, which is precisely what makes it something you can *rate* — something you can have more of and less of, along a scale.

You cannot build a ladder out of danger. You can build one out of a quantity.

## The first door {tone: measured}

Article 6 of Regulation (EU) 2024/1689 is headed *classification rules for high-risk AI systems*. I will give you its opening once, with the citation, and after that I will mostly call the thing it builds the ladder.

Paragraph 1 says that an AI system is high-risk where both of two conditions are fulfilled, and it labels those conditions (a) and (b). Here they are in the Act's own words.

## Conditions (a) and (b) {tone: quoting, rate: slow}

Condition (a): *the AI system is intended to be used as a safety component of a product, or the AI system is itself a product, covered by the Union harmonisation legislation listed in Annex I.*

Condition (b): *the product whose safety component pursuant to point (a) is the AI system, or the AI system itself as a product, is required to undergo a third-party conformity assessment.*

And the text then ties that assessment back to the same Annex I legislation.

## What those two conditions actually say {tone: measured}

{pause: 1.6}

Unpack it slowly, because it is written in the language of a field most listeners have never been inside.

Annex I is a list of existing European product laws. Not AI laws — product laws, several of them decades old, and it comes in two sections. I am not going to read it to you, because a list of directives and regulations by number turns to noise in the ear within about four seconds. What matters is the kind of thing on it. The first section gathers the general regimes that govern manufactured goods sold across the Union; the second holds the heavier sectoral regimes, and one of those is the approval of motor vehicles. Which is why we opened on a car.

So, in plainer words than the Act uses: if your AI system is a safety component of one of those products, or is one of those products, and that product already has to be checked by somebody other than its manufacturer before it can be sold, then your AI system is high-risk. Automatically. No further question gets asked.

And the term doing the work in that sentence is *safety component*.

Wrong reading: an important part, or a part that is itself safe. The Act's reading, from Article 3: a component that fulfils a safety function for the product, or whose failure or malfunctioning endangers the health and safety of persons or property.

The 2026 amendment then sharpened that, and this is a limit you need to hold alongside the rule. Systems used *solely* — and the word solely is the hinge — for non-safety-related aspects of user assistance, or for convenience and efficiency, expressly do not qualify as safety components. Unless, and the very next paragraph says this, unless their failure or malfunctioning would endanger health and safety, in which case they qualify after all. There is a further carve-out for products that need third-party assessment only for reasons unrelated to health and safety, and radio spectrum is the example the text itself gives.

So the first door is narrow and its frame is made of qualifiers. But it is a real door, and it stands open for anything embedded in a machine that Europe already regulates.

## The second door {tone: measured}

Paragraph 2 of the same article is one sentence long. In addition to the systems caught by paragraph 1 — and these are the Act's own words — *AI systems referred to in Annex III shall be considered to be high-risk.* The quotation closes there.

Annex III is a different kind of list altogether. Not products: *use cases*. Eight areas, each with sub-points beneath it. Two of those areas are the ones this episode needs — access to essential public benefits, and employment. The other six run from biometrics at one end to the administration of justice at the other, and you do not need to hold them today.

Two doors.

Most people who have heard of this Act have only ever heard of the second one. They think high-risk means *named in Annex III*. It does not. There is a whole parallel route in through the product legislation, and a car is on that route.

So if that emissions strategy were an AI system today, the question of whether it was high-risk would never go near Annex III. Nobody would open the list. It would turn instead on whether an emissions-control strategy counts as a safety component — genuinely arguable, and I am not going to pretend to you that it is settled — and the answer would arrive out of the car law, not out of the AI law.

## The ladder itself {tone: measured}

{pause: 1.2}

Now the structure, which is better built in front of you than recited.

The top rung forbids. Article 5 lists practices that may not be placed on the market, put into service or used at all, and it has been live since 2 February 2025.

Below it sits the high-risk rung, which is everything we are doing today. A heavy regime — documentation and oversight and assessment. Not yet in force: Annex III systems become high-risk on 2 December 2027, and Annex I systems on 2 August 2028.

Below that, a much lighter rung. Article 50 imposes specific transparency duties on certain systems — telling you that you are speaking to a machine, marking synthetic content — and those have been live since 2 August 2026.

And below that, nothing. No rung at all. Most software in Europe sits there, and the Act has no opinion about it.

Three rungs impose duties and one forbids. That is the structure.

## What high-risk does not mean {tone: pointed}

Two corrections before we go further, because a technically-trained listener arrives holding both mistakes.

The first is the four tiers. You will have seen a four-level pyramid, and two of its levels are not in the Regulation at all. Take the refutation first: the operative text prohibits some things, classifies others as high-risk, and imposes transparency duties on a further set. About everything else it simply says nothing. Go looking in the provisions for a category called *limited risk* and you will not find one. The pyramid is a summary somebody made afterwards. It is not wrong as a picture; it is wrong as a place to look things up.

The second mistake is bigger, and it is the single most consequential wrong reading in the Act.

*High-risk* does not mean dangerous.

It is a legal classification, triggered by an Annex III listing or by the Annex I product route, and it says nothing whatsoever about how harmful this particular deployment is to these particular people. A high-risk system can be harmless in practice. A system on no list at all can wreck a life.

The label tells you which body of law applies. It does not tell you how worried to be.

## A model that sorted a queue {tone: measured}

The second instance is European, and it is not counterfactual about the harm.

From 2013 the Dutch Tax Administration — the Belastingdienst — ran a risk-classification model in its childcare-benefits division. Operationally it was unremarkable: supervised learning on applications that had previously been judged correct or incorrect, producing a risk score. The score was used as a first filter, so that officials scrutinised the highest-scoring claims first.

A triage tool. A way of ordering a queue.

Its inputs included dual nationality. They included low income. They included whether the applicant's name read as non-Dutch.

## What that queue did {tone: grave}

Between 2005 and 2019, roughly twenty-six thousand families — some estimates say thirty-five thousand — were wrongly accused of childcare-benefit fraud and required to repay in full, commonly twenty to sixty thousand euros each. More than eleven hundred children were placed in foster care.

{pause: 2.0}

The third Rutte cabinet resigned in January 2021. On 25 May 2022 the Dutch government admitted that institutional racism, in part of the Tax Administration, had been a root cause. Amnesty International's report on the affair is called *Xenophobic machines*.

## Keeping two systems apart {tone: precise}

One thing to keep straight, because secondary accounts blur it constantly. This is *not* SyRI. SyRI was a separate Dutch welfare-fraud system, struck down by the District Court of The Hague in February 2020 — different system, different case. The benefits scandal is the Tax Administration's risk-classification model, and that model is what we are discussing.

So we now have two systems in play. A car that recognised its examiner, which came in through the product door. And a scoring model in a tax office, which comes in through the other one.

## Area five, point (a) {tone: quoting}

The benefits model is the cleanest match in the entire annex. Annex III, area five, point (a). The Act's words are: *AI systems intended to be used by public authorities or on behalf of public authorities to evaluate the eligibility of natural persons for essential public assistance benefits and services, including healthcare services, as well as to grant, reduce, revoke, or reclaim such benefits and services.* End of quote.

## Whose purpose {tone: precise}

Evaluate eligibility for a benefit — and then grant it, or take it back. A benefits risk model sits inside those words without any strain at all.

Notice the phrase that opens the point, though: *intended to be used*.

That is the second load-bearing term of the day, and the Act defines it. *Intended purpose* means, quote, *the use for which an AI system is intended by the provider*, end of quote — and the Act then spells out where you go to find that purpose. In the information the provider supplies: the instructions for use, the promotional and sales material, the technical documentation.

Said flatly, then. The intended purpose is not what the thing gets used for. It is what the provider *says* it is for.

Its companion term is *reasonably foreseeable misuse*, and the wrong reading of that one is "anything a user might get up to". The Act is narrower. Misuse is use that is not in accordance with the intended purpose, but which may result from reasonably foreseeable human behaviour, or from interaction with other systems. Foreseeable, not merely imaginable.

Which leaves one question standing.

Who gets to say what a system is for?

{pause: 1.6}

The person who wrote the documentation. Nobody else.

## The way off the list {tone: precise}

Being named in Annex III is not quite the end of it, and here the architecture gets interesting.

Paragraph 3 of Article 6 is a derogation. Wrong reading: an exemption you apply for, from somebody who grants it. There is no application and there is no somebody. It is a self-assessment, done by the provider, before the system goes on the market.

The test is written negatively, and that matters enough that I will give it as it stands.

## The negative test {tone: quoting, rate: slow}

By derogation, an Annex III system shall not be considered high-risk where — quote — *it does not pose a significant risk of harm to the health, safety or fundamental rights of natural persons, including by not materially influencing the outcome of decision making.* End of quote.

## Reading it the right way round {tone: pointed}

Not *does it influence the outcome*. Does it *not* influence. The system has to fail to matter.

That applies where one of four conditions is met, and two of them will do for today: the system performs a narrow procedural task, or it does preparatory work towards an assessment that somebody else makes. There are two more, and I am leaving them.

Then comes a carve-back, in a sentence of its own, and it is the most important clause in the paragraph. Notwithstanding all of that — the Act's words — *an AI system referred to in Annex III shall always be considered to be high-risk where the AI system performs profiling of natural persons.*

Always. No derogation.

*Profiling* is the third term to earn. Wrong reading: building up a customer profile, the marketing sense of the word. That is not it. The Act does not define profiling for itself — it imports the definition whole from data-protection law — and here the term does one very specific job: it is the trigger that closes the escape hatch.

Stripped of the cross-reference, and this next sentence is my gloss rather than the statute, it means using personal data automatically to evaluate things about a person.

A benefits risk model evaluates things about people, automatically, from their data. It profiles. The hatch is shut before it opens.

One more piece and then we can move. A provider who *does* conclude that their system is not high-risk has to document that assessment before placing it on the market, and register the system anyway, under Article 49(2). You do not walk away quietly. You file.

## Change one fact {tone: curious}

The boundary of a rule only becomes audible when you move something, so let us move things.

First. Take that same model, lift it out of the tax office, and sell it to a bank to triage loan applications. Still high-risk? Yes — Annex III, area five, point (b), which covers evaluating the creditworthiness of natural persons or establishing their credit score. Same area, next letter. And that point carries its own limit, which you should hear in the same breath: systems used for the purpose of detecting financial fraud are excepted from it.

Now change one fact. The bank points the model at its own *internal audit* workload instead, ranking which of the bank's files get reviewed this quarter. It touches no applicant, and no applicant's outcome.

Is that still high-risk?

{pause: 1.4}

Possibly not. That looks like a narrow procedural task which does not materially influence the outcome of decision-making about anybody, and the derogation may take it off the ladder entirely. The software is identical. The classification moved because what the thing is pointed at moved.

Second, and this one lives at the other door. I am going to build an example rather than report one, so hear it as a construction. Put an AI system in a car that tunes the cabin climate for comfort and nothing else — purely a convenience. Under the 2026 wording that is not a safety component, so the first door does not open; and nobody consults Annex III either, because cabin comfort is not a listed use case. Now change one fact. The same system also manages the cooling of the battery pack, and its failure could start a fire. The next paragraph catches it, because failure would endanger health and safety, so it is a safety component after all. Same box, same code, and now high-risk — through a door that Annex III never touches.

Third. Back to the benefits model, and take the number away. The system now outputs no score at all, just a ranked queue of case files with no figures attached to them.

The design document says that is a preparatory task. Triage. Ordering work.

The behaviour of the officials says something else, because the ones the model ranked highest got treated as suspects. So does the system materially influence the outcome of decision-making? The answer depends on which evidence you read, and the Act's test is applied by the provider, reading its own documentation.

Fourth, and this is the one that should stay with you. Remove nationality as a variable — take it out completely — and keep postcode.

Postcode, in a segregated housing market, carries a great deal of the same information, and the discriminatory effect may barely move.

Does the classification under Article 6 move?

{pause: 1.4}

Not a millimetre. It was high-risk before, because of what it is for and who uses it, and it is high-risk afterwards for exactly the same reason.

Blind.

The tier is not tracking the change that matters most, and it was never built to.

## Why this shape and not another {tone: contemplative}

So why a ladder at all?

Other shapes were available, and they were not fringe ideas. One was a rights-based instrument, keyed not to what a product is but to how severely it interferes with a protected interest — whoever caused the interference, and whatever technology they used. European data protection authorities pushed hard in that direction during the drafting, and I am leaving that argument alone today, because it is a whole episode of its own and it deserves the room.

The other was sectoral. Rules for medical devices written by the people who already regulate medical devices; rules for policing written by the people who already regulate policing. The Commission's own impact assessment, published in April 2021, set out a sectoral, ad-hoc approach as one of the options on the table, considered it, and did not take it.

The tier model won for two reasons that are worth saying out loud, because they are good reasons.

First, it is the shape European product law already had. Conformity assessment and market surveillance: that apparatus exists, it has staff, and it reaches every unit placed on the market before anybody has been hurt.

Second, it gives industry an answer in advance. Read the list, find yourself on it or fail to, and know your obligations before you build. That is worth a great deal to somebody trying to ship something.

And what was traded away is this. The tier is fixed by intended purpose, at design time, by the provider — while harm is contextual, and turns up in deployment.

## What the rule assumes about the machine {tone: pointed}

That trade is the heart of the episode, so let me put it as directly as I can.

Article 6 presumes a system with a stable intended purpose, declared by the person who built it. It presumes that you can read risk off what a thing was built for.

The benefits model was built to sort a queue. That is a true and accurate description of it, and any technical file would have said so honestly.

It was *used* as proof of fraud.

The tier tracked the design document. The harm tracked the organisation. And nothing in Article 6 can see the gap between those two, because Article 6 only ever reads one of them.

## Pushing down through the levels {tone: measured}

Now push down through that, because "the model was biased" is where most accounts stop, and it is the least interesting layer of the thing.

Take the technical level first. This was a classifier whose training labels came out of prior investigations, so it did not learn which applications were wrong. It learned which applications had previously been *found* wrong, which is a record of where officials had already been looking.

Ask what produced that, and you are at the organisational level. A score read as evidence, by people who had not been trained to read it, with no explanation attached to it and no path of appeal away from it.

Ask what produced *that*, and you reach the institution. A tax authority with a fraud mandate and no mechanism for discovering that it had been wrong about somebody. Plenty inside it was built to find money owed; nothing inside it was built to run the correction in the other direction.

Underneath the institution sits the economics. Money recovered was a measure of success, and an organisation measured on recovery will find things to recover. The model did not invent that incentive. It served it faster than people could.

And then the rights level, which is where the affair is usually described, and where it took longest to arrive. Discrimination on nationality, running for years, and more than a decade before anyone in government said the words institutional racism out loud.

Each of those levels is a way of describing everything upstream of it. Not one of them is the cause on its own.

The ladder reaches the first. It touches the second, because the deployer carries real duties of its own. It does not reach the rest at all.

I am not going to tell you today whether that is a fatal objection to the design. I am telling you where the instrument stops.

## Where this is contested {tone: measured}

Three joints, and they are in three different conditions.

Is a tiered risk model the right shape in the first place? Contested — and I have no consensus to report to you, because informed opinion genuinely has not converged. Martin Ebers, who teaches information technology law at Tartu, argues in a paper called *Truly Risk-Based Regulation of Artificial Intelligence* that the Act is not truly risk-based at all: that it claims proportionality and then departs from it by fixing closed categories in advance, and that assessment ought to be sector-specific instead. That is, near enough, the option the Commission itself assessed and declined. On the other side, Ronit Justo-Hanani has written in defence of the co-regulation design the Act actually adopted, while naming the precondition it depends on — that public authorities get access to the data they would need in order to supervise it. The weight does not lean here. What I can give you are the two rival shapes, and I have.

Does paragraph 3 open an escape hatch that providers will self-certify their way through? Also contested, and the profiling carve-back is both the limit on that worry and the test of it. Anything that profiles cannot use the hatch. Whether providers will agree with regulators about what profiling covers is a question nobody can answer yet, because nobody has litigated it.

And is Annex III a list that can be kept current, or one that will always be a scandal behind? Still moving. The Commission can amend that annex by delegated act, without reopening the statute, and the power sits in Article 7. It can also add to the derogation conditions, modify them, or delete them where deletion is what is needed to keep protection up — subject to an express floor, because no such amendment may decrease the overall level of protection the Regulation provides.

Contrast that with Annex I. It was amended in 2026 as well, but by Parliament and Council, in an act of legislation, not by the Commission on its own.

One annex bends. The other has to be legislated.

## As written, as enforced {tone: somber}

Now the uncomfortable arithmetic.

None of this applied to the Dutch Tax Administration. Not one word of it, because the Act did not exist. And the parts that would apply to its successors — the ones that make a benefits risk model high-risk and load it with duties — do not apply until 2 December 2027.

What actually ended that affair was a parliamentary inquiry, sustained journalism, and a cabinet that resigned. No market-surveillance authority. No conformity assessment. No classification of anything.

I said I would name what I am leaving out, so here it is: the entire machinery behind the first door. Annex I's two sections, and the reason the split between them matters — because for products in the second section, most of the AI Act's own requirements do not apply directly at all. The duties get threaded into the existing sectoral law instead, by Articles 102 to 110, which have been in application since 27 July 2026, and which are plumbing.

I have just summarised a whole parallel route into the high-risk regime in about ninety seconds. That is a compression, and I would rather admit to it than disguise it. The machinery gets taken apart properly later in the series.

## What you now ask {tone: measured}

So what do you take away, other than article numbers you will not remember and should not try to?

Three questions, and they work on any system, in any jurisdiction, under any regime.

The first. Which rung is this thing on — and was that decided by what it is *for*, or by what it *does* to somebody? Almost every classification scheme you will ever meet answers the first of those and then quietly claims to have answered the second.

The second. Who declared the purpose, and would the people actually using the system recognise the description? Read the technical file, then go and watch the room where it runs. If those two accounts have drifted apart, ask whether anything in the rule is capable of noticing that they have.

And the third, which is the benefits model in a single line. Does this system decide, or does it produce a queue that somebody else treats as a decision? The law will look at the first. The harm will come from the second.

{pause: 1.2}

We have a ladder now. Three rungs that impose duties, and one that forbids.

Next time, the top rung — and why a legal order whose whole instinct is to regulate rather than ban decided that a small number of things may not be built at all.