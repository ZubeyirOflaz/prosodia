---
episode: 9
title: The General Case
defaults:
  tone: measured
  rate: normal
---

## A judge in Rome {tone: measured}

On the eighteenth of March, 2026, a judge in Rome set aside a fine of fifteen million euros.

Her name is Damiana Colla. The fine had been imposed on OpenAI by the Italian data protection authority — the Garante — in a decision numbered seven hundred and fifty-five, dated the second of November 2024. Judge Colla did not decide whether OpenAI had done the things the Garante said it had done. She did not decide whether fifteen million was too much, or too little.

She decided that the Garante had no business deciding at all.

At some point in 2024, OpenAI had established a subsidiary in Ireland.

{pause: 1.4}

European data protection law has a mechanism called the one-stop-shop. Where a company has its main establishment in one Member State, the supervisory authority of that State takes the lead, and the lead authority is the one entitled to take the decision. The court held that once the Irish company existed, Italy's authority was no longer that authority. On the reported account, the crossover happened months before the Garante's final decision. So the decision went out through a door that had already closed.

The court never reached the substance. Not one allegation was tested. A commentary on the judgment put it about as sharply as it can be put: the decision did not find OpenAI innocent. It found that Italy had no right to judge OpenAI.

It is worth remembering what the Garante had been doing, because it was not trivial. In late March 2023 Italy became the first country to block ChatGPT; access came back about a month later. The decision that followed found processing of personal data for training without an adequate legal basis, and inadequate information to users. There were further grounds, and I am not going to read them all. The authority also ordered something unusual — a six-month public awareness campaign across broadcast and print media, under a power in the Italian data protection code that it had never used before.

And this is the pivot, and it is the one thing from Rome worth carrying forward. Every word of that was data protection law. There was no AI-specific regime to reach for, so the Garante reached for the instrument that was on the shelf. It lost, and it lost on the question of who was entitled to decide rather than on whether it was right.

One disclosure before we leave Rome. I have not read the judgment. What I have just given you is reported — consistently, and from more than one direction — and it is still reported rather than read. Treat the reasoning as solid and the wording as second-hand.

## Where we are {tone: lucid}

This is The Instrument: a series that takes one European regulation and builds it, part by part, from its definitional gate to its last penalty.

You already have the gate — what has to be true of a thing before any of this law touches it. You already have the roles, provider and deployer, and the fact that duties attach to who you are rather than to what you built. And you have the conformity machinery: an assessment, a technical standard, and a presumption that falls out the far end.

In the chapter we are about to build, almost none of that machinery exists. No assessment. No notified body. No mark.

This chapter governs general-purpose AI models. It has its own definition of what it catches, its own way of sorting them, its own enforcer, and its own instrument standing in for a standard.

And there is a claim I am going to make three times in this episode, in different words each time, because it is the reason the episode exists. The first version is this. The rest of the Act is organised around a system's intended purpose. These models do not have one. This chapter is the Act saying so, in its own text.

## Two words that sound the same {tone: precise}

Start with a distinction that will otherwise wreck everything after it.

A general-purpose AI *model* is not a general-purpose AI *system*. The Regulation defines them separately, and they attract different duties, owed by different people.

The definition of the model — Article 3, point 63 — describes an AI model that, quote, displays significant generality and is capable of competently performing a wide range of distinct tasks, end quote, and that, quote, can be integrated into a variety of downstream systems or applications, end quote. Note the limit written into the same sentence: models used for research, development or prototyping, before they are placed on the market, are outside it.

The system gets its own definition a few points later — an AI system built on such a model, with, quote, the capability to serve a variety of purposes, end quote, whether used directly or built into something else.

Plainly: the model is the trained thing. The system is the product somebody wraps around it — the interface, the guardrails, the sales page.

The person who builds that product has a name in the Act. A *downstream provider*: the provider of a system that integrates a model, whoever supplied the model, including where a company supplied it to itself.

So. One model, many systems. The obligations we are about to walk through attach to the model itself, and they largely consist of passing information on to whoever builds on it.

## What the thing actually is {tone: curious}

Before any rule touches it, what is the thing?

A large language model of the kind this chapter is aimed at is trained in two stages. In the first, a network with a very large number of parameters is shown an enormous quantity of text and asked, over and over, to predict the next fragment. Nobody labels anything. The supervision comes from the text itself — the answer to each prediction is the next word, already sitting there. Do that at sufficient scale and the parameters settle into something that can continue almost any passage plausibly.

Then a second stage, far smaller: tuning on curated examples, and on human judgements about which of two answers is better. That is where a text-continuation engine becomes something that answers questions and refuses requests.

None of that is in the Regulation.

{pause: 1.2}

What the Regulation reaches for instead is a number: how much arithmetic the first stage consumed. The unit is the floating-point operation, and the Act defines it — quote, any mathematical operation or assignment involving floating-point numbers, end quote. What is being counted is arithmetic. A count of operations performed, added up across the whole of training — not a speed, and not a piece of hardware.

Think of it as a receipt. Carry that image with you, because it earns its keep in about a minute. Compute is a receipt for how much went in. It is not a description of what came out.

Why would anyone regulate on a receipt? Because around 2022 and 2023, when this chapter was being drafted, compute was the best publicly checkable predictor available. Spend more computation. Use more data. Build a bigger model. The result gets better — and it gets better predictably enough that firms committed very large training budgets on the strength of the relationship. I am not going to name you a paper for that, because I have not been able to confirm one to the standard this series uses. Take it as what it is: an empirical regularity, widely relied upon, and argued about.

The receipt has a second virtue, and it is the practical one. You can estimate it from outside. Parameter count, token count, a small constant, and you are within range — no access to the model required. A regulator can work it out from a press release.

## What the text actually says {tone: quoting, rate: slow}

Article 51 is where the sorting happens, and it offers two ways in.

The first: a model has high impact capabilities, evaluated on appropriate technical tools and methodologies, including indicators and benchmarks. The second: the Commission decides, on its own initiative or after a qualified alert from the scientific panel — that is, after a formal warning from the Act's standing panel of independent experts, people chosen for their expertise and for having no tie to any provider — that a model has an equivalent impact, judged against criteria set out in Annex thirteen.

Two ways in. Almost every account of this chapter you will ever hear mentions only the number.

The number is in the next paragraph, and this is the Regulation's own sentence.

Quote. A general-purpose AI model shall be presumed to have high impact capabilities pursuant to paragraph 1, point (a), when the cumulative amount of computation used for its training measured in floating point operations is greater than ten to the twenty-fifth. End quote.

{pause: 1.4}

Read the verb. *Presumed.* Not defined as. Not deemed to be for all purposes. Presumed — which, in the law of any European state you care to name, means a starting point that somebody is entitled to argue against.

And the paragraph after it lets the Commission move the figure by delegated act — a Commission instrument that changes the law's own text without going back to Parliament — in light of algorithmic improvements or increased hardware efficiency, so that the threshold reflects the state of the art.

So the number is not the definition. One question, and take a moment with it. If a model comes in below ten to the twenty-fifth, is it outside this regime?

{pause: 2.0}

No. It is outside the *presumption*. It can still be classified on evaluation, and it can still be designated by the Commission. The number is a fast lane into the class, not a fence around it.

From now on I will call the whole apparatus *the model regime*, and that figure *the threshold*, and I will not read you the article number again.

Two more terms, because the chapter is unparseable without them.

High impact capabilities. The Act's words: quote, capabilities that match or exceed the capabilities recorded in the most advanced general-purpose AI models, end quote. Listen to what that does. It is a relative definition with no fixed contents. Whatever the frontier is, this class is the frontier — which means the class redefines itself every time somebody releases something better, and nobody has to amend anything.

And systemic risk, which is a term of art and does not mean what it means in banking. The Regulation calls it, quote, a risk that is specific to the high-impact capabilities of general-purpose AI models, end quote — significant for the Union market by reason of reach or of foreseeable negative effects, and, quote, propagated at scale across the value chain, end quote. Said more simply: a harm that arrives everywhere at once, because thousands of products were built on the same thing.

What happens once a model is in the class sits in the following article, and it is short. The provider notifies the Commission, within two weeks of meeting the condition or of learning that it will. With that notification the provider may argue that the model, exceptionally, presents no systemic risk. If the Commission rejects the argument, the model is in. A provider designated by the Commission may ask for reassessment — but not sooner than six months after the decision.

Notice what is missing from that entire procedure. No notified body. No harmonised standard. No certificate at the end. After a whole episode spent on the machinery of third-party assessment, this regime has none of it. The regulator decides directly, and the provider's remedy is to argue.

## Why a number, and not something better {tone: measured}

Every rule is a choice against other rules. This one was made under pressure, and the roads not taken are worth saying aloud.

The Commission's original proposal, in April 2021, contains no chapter on general-purpose models. Not a thin one. None. The architecture was built for systems with a stated purpose, sold for a stated job. Then a general-purpose product reached the public, and the proposal became a description of a world that had moved.

So: do nothing about models, and regulate only the systems built from them. There is a real argument there. Duties would land on whoever deploys a thing into a context, which is where harm actually happens. What it gives up is everything upstream. If a defect sits in the model, every product built on it inherits the defect, and you would be correcting them one at a time, forever.

{pause: 1.2}

Or: put these models into the high-risk regime the Act already had. Conformity assessment, technical documentation, a presumption flowing from standards. It does not work, for a reason that is almost funny. That regime assesses a system against its intended purpose. These models are defined by *not having* one. You would be certifying a thing as fit for a use nobody has specified.

What everyone actually wanted was the third thing: regulate on capability. Name the dangerous things a model can do, test for them, catch whatever can do them, regardless of how it was built. Nobody could operationalise it. There is no agreed test, and no agreed level of performance on any test that corresponds to a level of danger.

What got built instead was a proxy plus a promise. The proxy is the threshold, administrable precisely because it does not measure what anyone cares about — you can check it, and checking it tells you something adjacent to the point. The promise is a code of practice, which can be written in months, where a standard takes years.

That is the technical level of explanation, and it is worth pushing one level back. A threshold set at ten to the twenty-fifth catches, on reported estimates, somewhere between five and fifteen companies worldwide. Say that differently and it stops being a technical parameter. It becomes a description of an industry — a statement that frontier model training is, today, something a handful of very large firms do. And the instrument chosen to govern those firms was drawn up with their participation. Neither of those is a scandal. Both follow from the shape of the market rather than from the drafting, because a rule written for a concentrated industry has nobody else in the room.

## What a provider actually owes {tone: lucid}

So: a chapter with its own definition, its own way of sorting, and a number that starts an argument rather than ending one. What remains is what the sorting gets you — what a provider owes, and to whom.

{pause: 1.2}

So what does the model regime demand?

Every provider of a general-purpose model — above the threshold or below it — owes four things. Three of them are documents. The fourth is a policy.

The first document is the technical documentation of the model, its minimum contents laid down in Annex eleven, and among much else it must record the computational resources used to train the model — floating-point operations being the Annex's own example. It has to exist, be kept current, and be handed over when the AI Office or a national authority asks for it. Nobody files it anywhere. It sits with the provider until someone requests it. The receipt, kept.

The AI Office, incidentally, is not an agency. The Act's definitions say plainly that it is a function inside the Commission, and that references to the Office are references to the Commission.

The second set of documents goes downstream, to the people building products on the model, with minimum contents in Annex twelve. That is the one with practical bite — capabilities, limitations, what the thing can and cannot be relied on to do.

The third is the one that drew the attention: the provider must draw up and make publicly available, quote, a sufficiently detailed summary about the content used for training, end quote — following a template the AI Office provides. And the fourth, the policy, is a copyright policy, including identifying and complying with a reservation of rights.

I am naming one thing this episode does not cover, and it is that policy's neighbour. Whether training a model on copyrighted work is lawful in the first place is live, unsettled, and decided nowhere in this Regulation. What the Act does is require a policy and a summary. It neither blesses the practice nor condemns it.

If a model is in the systemic-risk class, four further obligations attach. The two that matter most: the provider must evaluate the model against state-of-the-art protocols, including conducting and documenting adversarial testing — red-teaming, written down — and must report serious incidents to the AI Office without undue delay. The other two concern risk mitigation, and the cybersecurity of the model and the physical infrastructure under it.

Now the instrument.

{pause: 1.2}

As of June 2026 there is no harmonised standard for any of this. There may be one day. Until then the Act offers a substitute, and the substitute is a *code of practice*.

A code of practice, under Article 56, is drawn up at Union level, and the AI Office runs the process. Providers are invited to take part. Civil society, academia and the people building on these models may support the work. A provider may then rely on the code to demonstrate compliance — and the text is precise about for how long: until a harmonised standard is published. After that, the standard carries the presumption.

Which raises an obvious question, and this one is worth answering in your own head first. What happens to a provider who declines to sign?

{pause: 2.0}

Nothing automatic. Such a provider must demonstrate alternative adequate means of compliance, for assessment by the Commission. Declining is permitted. Declining quietly is not.

The Act set a deadline for the code — ready, in its words, at the latest by 2 May 2025 — and it said what would happen if nothing adequate arrived: the Commission may lay down common rules by implementing act, which is the Commission writing binding rules under a power the statute already handed it. If the voluntary instrument fails, a compulsory one replaces it.

The code was published on 10 July 2025 and declared adequate on 1 August 2025. Three chapters. Transparency, copyright, and safety and security — and the last of those binds only providers of systemic-risk models. By August 2026, more than twenty providers had signed.

Set that beside the other thing this series has been watching. The harmonised standards the high-risk regime depends on are not there; as of June 2026 not one of them had been cited in the Official Journal. The code, for all its softness, exists. That is the defenders' strongest point, and it deserves to be stated in their voice rather than mine.

And now a term to keep well apart from that one, because in the ear they are nearly identical. A code of *practice* is what we have just described: general-purpose models, a way of showing you complied with duties that are mandatory. A code of *conduct*, under Article 95, is something else entirely — an encouragement to apply high-risk-style requirements, voluntarily, to systems that are *not* high risk.

One word apart, and that word is carrying more weight than it can hold. Practice: how you show you complied. Conduct: doing more than you had to.

## Change one fact {tone: pointed}

If you have been holding this chapter as a decision tree — something you run once, after which you know your answer — the next few minutes will break that. The way to find the edge of a rule is to move a single detail and watch the answer flip.

Take a model trained deliberately just under the threshold — a run sized to come in below it — and then post-trained hard. Distilled from something larger, tuned extensively, and given a long chain of reasoning at the point of use, so that it spends far more computation answering your question than it ever spent learning to answer questions at all.

What class is it in?

{pause: 2.0}

Below the line. The presumption never fires, because the presumption looks only at training compute. The routes back in are the two we noted: an evaluation-based classification, or a Commission designation on those criteria. Both need somebody to notice and act. Neither happens by itself.

That is the receipt problem at its sharpest. Compute spent at training time is a receipt for the first stage only. A model that does its thinking when you ask it something is buying capability the threshold cannot see, and buying it after the receipt was printed. That gap has widened every year since the number went into the text, and it is the strongest argument anyone has that the threshold measures the wrong quantity.

Change a different fact. Release the model under a free and open-source licence — genuinely open, with weights and architecture made public. Two of the four duties fall away. The technical documentation and the downstream information package are no longer required.

But the relief has a relief of its own, and it is the important half. The copyright policy stays. The training-content summary stays. And the relief does not apply at all to a model with systemic risk. So move one more fact — push that same open model over the threshold — and the relief vanishes outright. An open frontier model carries the full weight, with the systemic-risk obligations on top of it.

Third. A provider above the threshold notifies, as it must, and argues in the same breath that its model presents no systemic risk. The Commission weighs the argument and rejects it in a reasoned decision. That is the whole process. No third party assessed anything, and nothing is issued at the end, because nothing in this chapter issues anything.

Compare that with what an ordinary high-risk system gets — an assessment, a declaration, a mark on the product. A model gets a letter from the Commission.

And a fourth, which carries us somewhere else. Remember the airline chatbot, whose operator argued to a tribunal that the chatbot was a separate legal entity, responsible for its own actions. Rebuild it today on a general-purpose model, and put it in front of European customers.

## Telling people {tone: measured}

Article 50, live since 2 August 2026, is the Act's transparency rung, and it is a great deal smaller than its name suggests.

It does three things. A system that interacts with people must make clear the person is dealing with an AI. Deep fakes must be labelled. And synthetic or manipulated content must carry marks a machine can detect.

Deep fake is a defined term, not a figure of speech. The Act's words: quote, AI-generated or manipulated image, audio or video content that resembles existing persons, objects, places, entities or events and would falsely appear to a person to be authentic or truthful, end quote.

Note what the duty is. It is a labelling duty and nothing more. The transparency rung does not forbid making the thing; it requires that the thing be marked.

So the rebuilt chatbot must now say it is not a person.

{pause: 1.4}

And that is all it must do. If it tells a grieving customer that a bereavement fare can be claimed retroactively, and no such policy exists, the transparency duty is satisfied. The disclosure was made. The statement was false. Transparency in this provision means telling you what you are talking to. It says nothing whatever about whether what it says is true.

Hold that, because it is the shape of a great deal of AI regulation and it is easy to mistake for more than it is.

One more instrument to name, and then I will stop naming instruments. On 31 July 2026 the Commission published a first list of organisations signing a code of practice on transparency of AI-generated content — more than a hundred and eighty of them. A second code, on a different subject, under a different part of the Act, from the one we spent five minutes on. If you are keeping count: one code of practice for general-purpose models, one code of practice for marking synthetic content, and one code of conduct for voluntary good behaviour. Three documents with nearly interchangeable names and no overlap in subject.

## What the rule assumes about the machine {tone: contemplative}

Now the question this series keeps returning to. What does the rule assume the machine is, and is it right?

Chapter Five assumes that a model's risk can be estimated from how it was made, rather than from what it does.

That is an extraordinary thing for a product-safety instrument to concede, and it is worth being fair about why it conceded. At the moment a model is placed on the market, nobody knows what it does — not the regulator, and not the company that trained it. Capabilities in these systems get discovered after the fact, by users, by researchers, by people trying things, sometimes long after release. A regime that waited for a settled account of what a model can do would never act at all. So the Act reached for the one quantity that exists before anyone has used the thing: the size of the bill.

That is an honest answer to a genuine problem of knowledge. It is also a confession, and the confession is the second version of my claim.

Go back to the definition of a general-purpose model. Significant generality. A wide range of distinct tasks. Integrable into a variety of downstream systems. That is a definition built entirely out of the *absence* of a purpose.

And intended purpose is the organising concept of the whole rest of this Regulation. It decides whether a system is high risk. It fixes what the risk management system must consider. It is the thing the instructions for use are required to state. Every mechanism the Act has runs off it.

So when the Act met a technology with no intended purpose, it could not extend the machinery. It had to build a second one alongside the first — different trigger, different enforcer, different instrument, and nothing at the end that certifies anything.

Say it plainly. Chapter Five is the Act admitting, in its own text, that its organising concept does not apply to the most consequential technology it governs.

One further thing, briefly, because you may have been waiting for it. Nothing in this chapter runs to a person. There is a complaint right in this part of the Act — and it belongs to downstream providers. It is a right for one company to complain about another. Individuals are not in this chapter at all. Where the rest of the Act at least gestures at an affected person, the model regime is a conversation between the Commission and a handful of firms.

## Where it is contested {tone: measured}

Three arguments are live, and they sit at different stages.

Whether the threshold tracks anything real about risk: contested, and moving against the number. The case for it is that it is checkable, uniform and hard to evade by accident. The case against grows every time capability arrives from somewhere the receipt does not record — from post-training, from distillation, from computation spent at the moment of use. I cannot give you a name on either side of this one, and I would rather tell you that than dress my own view up as somebody else's.

Whether a code of practice co-written with the industry it governs can be adequate for a risk the Act itself calls systemic: contested, and the defence is stronger than it sounds. It exists. The alternative mechanism — a harmonised standard — does not, and has not, and the regime depending on it had its dates moved to wait for it. An instrument that exists and binds imperfectly is being compared against an instrument that does not exist. Again, I have no named holder for either side, and you should weigh the argument accordingly.

Whether supervision should have been centralised in the Commission rather than spread across twenty-seven national authorities: this one the events answered. Rome is the argument. A national regulator brought the most prominent action in Europe against a general-purpose model and lost it because the company had incorporated somewhere else. Centralising supervision makes that failure impossible. What stays contested is whether the centre has the competence and the headcount, which is a different question and an open one. The 2026 amendment added a line about giving the AI Office adequate resources to do its job — the kind of line a legislature writes when it suspects the answer is no.

## As written, as enforced {tone: somber}

The model regime became applicable on 2 August 2025.

With one exception, written into the Act's own applicability article. Chapter Five applied from that date — except for Article 101, the provision letting the Commission fine providers of general-purpose models. Reported ceilings are three per cent of worldwide annual turnover, or fifteen million euros. That provision waited a further year.

So for twelve months there were duties, and no penalty attached to them. The AI Office's enforcement powers went live on 2 August 2026.

What has happened since? The AI Office is reported to have sent first requests for information to frontier providers around the end of August 2026. A caution on that: it is a secondary report and I have not been able to confirm it. And under this chapter, no penalty has been confirmed at all. Not one.

That is not a scandal either. A regime a month into its enforcement powers has not had time to produce a decision. But it does mean that every confident claim you have heard about what this chapter does in practice is a claim about text, not about outcomes.

The escalation available to the AI Office is better known by shape than by article number. It can request documentation. It can evaluate a model itself. It can require measures. And running alongside all of it is a set of procedural rights for the provider, written into the same section — the Act points at them in the very sentence that grants the powers.

Third-country providers must appoint an authorised representative established in the Union. I mention it and move on.

Over the whole of it sits one sentence. Quote. The Commission shall have exclusive powers to supervise and enforce Chapter Five. End quote — taking into account, the text adds immediately, the procedural guarantees in Article 94, and subject to market surveillance authorities being able to ask the Commission to act.

*Exclusive.* That is the Act's answer to the courtroom in Rome. No question of which Member State is entitled to decide, because no Member State is. The forum problem that ended the Garante's case cannot arise, because there is only one forum.

And mind the limit, because it is the one people drop. Exclusive for Chapter Five — for *models*. Who supervises the systems built on those models is a separate architecture with a separate answer, and this episode is not where it lives.

Europe's most famous enforcement action against a general-purpose model was annulled. Not because the regulator was wrong about the company. Because the regulator was the wrong regulator.

## What you now ask {tone: lucid}

My own view, marked as mine, and it is narrower than you might expect.

The threshold does not trouble me the way it troubles most of its critics. It never claimed to measure capability. The drafters wrote the word *presumed* into the sentence, and a power to move the figure into the paragraph after it, and that is what honest proxying looks like. What troubles me is the other end. This chapter's compliance instrument is a document its subjects helped write, assessed by an office inside the institution that drafted the law, with no third party at any point, and nothing issued at the end to say a model was examined and found to be as described. Everywhere else in this Act, somebody signs something. In this chapter, nobody does.

That is a local judgement about one chapter. I am not going to stretch it into a judgement about the Act. That one is being held.

What you should be able to do now is carry three questions to a system you have never met.

First. What is the threshold measuring — and what is it a proxy *for*? Every bright line in technology regulation stands in for something it cannot observe. Find the thing it cannot observe, and you will know what the rule is actually worried about.

{pause: 1.4}

Second. Could a system acquire the capability the rule fears without crossing the number the rule uses? If the answer is yes — and it usually is — then the line will have to be redrawn, and you can start asking who holds the power to redraw it, and how quickly they can move.

Third, and this one is a habit rather than a question. When somebody tells you a regulator lost a case, ask what it lost on. A ruling on jurisdiction decides who may judge. It decides nothing at all about whether the thing complained of ever happened. Those two get reported in the same sentence, and they are not the same finding.

The third version of my claim, and then we are finished with it. A statute built around what a product is for met a product that is not for anything — and rather than pretend otherwise, it wrote a separate chapter with a separate logic and a separate enforcer. That is either the Act's most candid moment or its largest admission of defeat, and it is probably both.

One last thing, and it is a question this chapter cannot answer from inside itself. A regime reaching somewhere between five and fifteen companies, nearly all of them established outside the Union, is making a very large assumption about its own reach. Does any of this travel? Does a European rule change what a company does in California, or does it only change what that company ships to Europe?

We step away from the text to find out. One episode. Then we come back to the instrument.