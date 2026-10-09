---
episode: 2
title: A Reason to Touch It
defaults: { tone: measured, rate: normal }
---

## An urgent application {tone: measured}

On the eighth of August 2024, Ireland's Data Protection Commission went to the High Court in Dublin and asked for an order against a company.

The company was Twitter International Unlimited Company — the Irish-established arm of the platform. What the Commission wanted stopped was a training run. Public posts, written by users across the European Union and the wider European Economic Area, were being used to train a model called Grok.

The application was urgent. It was brought under section 134 of the Data Protection Act 2018, and it was the first time the Commission had used that power. On the Commission's own account, it was also the first time a lead supervisory authority in Europe had taken court proceedings of this kind.

Two weeks before that, users had noticed something in their account settings. Around the twenty-fifth and twenty-sixth of July, reporting described a new option on X — a setting that allowed a user's posts, and their interactions with Grok, to be used for training and fine-tuning, and to be shared with xAI. It was on by default. It had arrived on existing accounts without an announcement.

I should mark that carefully, because it is the only thing in this story that comes from the operator's own description of itself, and I have it through press reporting of an interface rather than from a document. So: reported. I will hold it at that, and no firmer.

The court case did not run. X agreed to suspend the processing. On the fourth of September 2024 the proceedings were struck out — the case ended with no judgment — on a permanent undertaking, the promise on which the Commission agreed to end the case. And the undertaking reached backwards, which is the part people get wrong. Posts made between the seventh of May and the first of August 2024. Where they had been used to develop, refine or train Grok, the data was to be deleted, and not processed further.

So the regulator got something real. The copy was to go.

{pause: 1.4}

Now the hinge, and it is one sentence long. The data was deleted. The model was not.

Nothing on the public record says the Commission asked about the model that had already been built. Hold that, because everything today walks towards it.

## Where we are {tone: lucid}

This is The Collisions, and this is the second episode.

The series takes one European instrument at a time and collides it with another, asking a single question each time: which rule actually bites, who it binds, and what falls through the seam.

Last time we established four things, and only two of them decide today. The first: almost anything you do to personal data counts as processing — and a training run is processing, like any other operation, with no special status at all. The second: the party who decides why and how is the controller, and the duties land on them. The other two — what makes information personal, and who counts as a processor — you can let go of for now.

That first one is the door into today. If training is processing, then somebody needs a reason to be allowed to do it.

That is what this episode is about: the reason. And the trouble waiting at the end of it is that this Regulation wants a purpose named in advance, while the thing being built is valuable precisely because nobody can say yet what it will be used for.

Not whether the data was personal — we settled that. Whether there was a lawful basis for touching it, and whether the thing it was touched *for* was a thing anyone had declared.

One warning before the apparatus, because you may well arrive carrying it, and it is wrong. It is the idea that data protection law is a bag of separate rules you can satisfy one at a time. It is not. The principles and the lawful bases interlock; you can pass one and fail because of the other, and the failure is the same failure looked at twice.

## The pipeline, described plainly {tone: precise}

Before any rule touches this, let me say what actually happens when a model is trained on a platform's posts. I'll describe it generically, because a generic description is all I can honestly give — I have nothing first-party about how this operator built anything.

Start with posts that are public by default. Public means readable without an account, indexed, quotable.

Then a pipeline. Something selects which posts to take, filters out what nobody wants, removes duplicates, and writes the survivors into a training set. That set is the corpus — the body of text a model learns from. Then a training run: the model's parameters are adjusted, repeatedly, against that corpus. When it finishes, the corpus and the model are two separate objects, and they can be in different hands.

And then there is a fourth thing, which is not part of any of that. At the moment you ask a question, a deployed system may go and fetch current posts to answer you. That is retrieval. It happens at inference time, on live data, for a different reason.

Keep those apart. Most public argument about this conflates them, and they raise different questions with different answers. Today is about training. Retrieval is a separate problem and I am not solving it.

What I cannot tell you: how many posts, which version of the model, or when the run happened. None of that is on the record I have, and a plausible-sounding number is still an invented one.

## The purpose rule {tone: precise}

Article 5 of the General Data Protection Regulation sets out the principles. Six of them in the first paragraph, and a seventh duty in the second, which I am saving for the end. One of the six is about security. It matters enormously and it is not this argument, so I am leaving it.

The first principle is lawfulness, fairness and transparency — and its lawfulness half is cashed out in a separate article, Article 6, which is where we go after this. So I'll hold it for a few minutes and give you the rest of Article 5 first.

The second principle is the spine of the episode. The Regulation's own words, and I'll say where they start and where they stop.

Quote: personal data shall be collected for specified, explicit and legitimate purposes, and not further processed in a manner that is incompatible with those purposes. End of quote.

Call that **the purpose rule**, and from now on that is what I'll call it.

Plainly: you say what you are collecting it for, at the time you collect it. You say it clearly enough that it means something. And later uses have to be compatible with what you said.

Now the misreading, which is the most common one in this field. People hear the purpose rule as *tell them what you'll use it for*, as though it were a disclosure obligation. It is a constraint on what you may do. "We later decided to train on it" is not a grey area under this rule. It is the textbook case of the thing the rule was written to stop.

One limit, in the same breath, because I'd be misleading you otherwise. The same provision says that further processing for archiving in the public interest, or for scientific or historical research, or for statistics, is not to be considered incompatible — in accordance with the research safeguards in Article 89. We will come back to what that carve-out does and does not do, and it does less than people hope.

## Four more principles, and they all hang on one hook {tone: precise}

The elegant thing about Article 5 — and this is the bit that turns a checklist into a machine — is that the other principles are all measured *against the purpose*.

Data minimisation. The wrong reading is "don't collect too much". The Regulation's own words are — adequate, relevant, and limited to what is necessary in relation to the purposes for which they are processed. End of quote.

Listen to the end of that again — *in relation to the purposes for which they are processed*. That is what carries it. There is no absolute amount that is too much. There is only too much *for what you said you were doing*, which means scale is not a defence — scale is the thing being tested.

Accuracy. The wrong reading is "the model should be accurate". That is not what the principle says.

Quote: accurate and, where necessary, kept up to date; every reasonable step must be taken to ensure that personal data that are inaccurate, having regard to the purposes for which they are processed, are erased or rectified without delay. End of quote.

There is the hook again, sitting in the middle of the sentence — inaccurate having regard to the purposes. So when a system states something false about a named person, that is not a product-quality complaint. It is an accuracy problem under a principle of the Regulation, and somebody owes a duty about it.

Storage limitation, and the phrase to listen for is — kept in a form which permits identification. That is a question you can ask about a model, not about a file server. The whole provision runs: quote, kept in a form which permits identification of data subjects for no longer than is necessary for the purposes for which the personal data are processed — and there the sentence stops.

{pause: 1.4}

And then the seventh, the one I said I was saving. Article 5, second paragraph, which is short and does more work than any of them. The controller shall be responsible for, and — quote — be able to demonstrate compliance with — end of quote — everything above. Accountability. Not "be responsible". Be able to *show* it, to someone who asks.

That converts every principle I just gave you into a documentary burden. Somebody has to have written it down, in advance, in a form that survives a regulator reading it.

So far we have two things. A purpose, declared at collection, which the other principles are measured against. And a duty to be able to demonstrate all of it.

## Six doors {tone: measured}

Principles are not permission. Article 6 supplies that separately, and it opens with a sentence worth hearing exactly. Quote: processing shall be lawful only if and to the extent that at least one of the following applies. End of quote.

Only if. At least one. Then six bases. Call them **the six doors**.

Consent is the first door, and it is the one everybody assumes is the main one. It is one of six, and the Regulation gives it no priority whatever over the other five.

Why six doors and not one? The alternative, argued over for years before this Regulation was written, was to require consent for everything. It was rejected for a reason you will recognise the moment I say it: if consent is the only door, then every ordinary, unobjectionable, necessary act of processing has to be preceded by a request, and people learn to click through requests without reading them. Consent for everything produces consent theatre, and consent theatre protects nobody.

So: six doors, most of them turning on necessity, and one of them — the last — on a balance.

What was traded away to get that? Three things, and they are the price of the design. The balancing door is the one almost everyone walks through. It is assessed in the first instance by the controller itself. And the assessment only ever surfaces when a regulator asks to see it.

Now the two doors that matter today.

**Consent**, defined in Article 4. Quote: any freely given, specific, informed and unambiguous indication of the data subject's wishes by which he or she, by a statement or by a clear affirmative action, signifies agreement to the processing. End of quote.

A question for you, and take a moment with it. A setting that was already switched on, that arrived on your account without an announcement, and that you never touched — is that a clear affirmative action by you?

{pause: 1.4}

Reading the words alone, I don't see how it can be. A default is not a statement, and not touching something is not an action. That is my reading of the text, and I mark it as mine.

**Legitimate interests** is the sixth door, and it is the one this whole story is really about. Quote: necessary for the purposes of the legitimate interests pursued by the controller or by a third party, except where such interests are overridden by the interests or fundamental rights and freedoms of the data subject which require protection of personal data, in particular where the data subject is a child. End of quote.

Three limbs, and they are cumulative. There must be an interest, and it must be legitimate. The processing must be necessary for it. And the balance must not come out against you.

The limit, in the same breath: the very next sentence of the Regulation says this door does not apply to public authorities performing their tasks. A ministry cannot reach for it. A company can.

And I have to stop on that middle limb, because one word decides more cases in this Regulation than any other.

## Necessary {tone: pointed}

The word "necessary" appears in five of the six doors.

The wrong reading is "useful". The second wrong reading, which is more insidious because it sounds modest, is "this is how we do it".

Take it away from machines for a moment. A gym asks for your date of birth, and says it needs it for the contract.

Does it?

{pause: 1.4}

Their honest answer is that it is convenient. Convenient is not the test. The test is whether the purpose can be achieved another way that intrudes less. If a tick-box saying "I am over eighteen" would do, the date of birth is not necessary, for all its usefulness.

Now bring it back. Necessary does not mean the model would be better. It means there is no less intrusive way to get where you are going.

## Working it {tone: measured}

Let me do the analysis properly, saying the moves as moves, because the method is half the lesson.

**The issue.** Two issues, actually, and they get collapsed constantly. First: is there a door for this processing at all? Second: is training a *further* purpose, incompatible with the one the data was collected for? A controller can walk through a door and still fail the purpose rule. Both have to come out right.

**The instrument.** For the first question, the six doors. Consent is not available, on the reading I gave you, if the setting was a default. So the answer, if there is one, is legitimate interests.

**The test, applied to these facts.** Limb one: is there an interest, and is it legitimate? Building and improving a conversational model is a commercial interest. And the words you heard a moment ago were — quote — the legitimate interests pursued by the controller or by a third party — end of quote. They do not say those interests have to be anything other than commercial. Limb one is not where this fails.

Limb two, necessity. Could the model have been built without these particular people's posts? The honest answer from any lab is that it would have been a worse model. Notice what that answer is doing. It is answering "would it be better with" — and the test asks "could it be done without".

Limb three, the balance. The people who wrote those posts wrote them to be read. They were public to readers. Whether being public to readers means being available to a training corpus is the entire question. And the Regulation frames it as a collision: the controller's interest on one side, and on the other the interests and fundamental rights and freedoms of the person who wrote it. My own instinct is that it turns on what the person typing could have expected — but the words of the balance do not put it that way, and this programme has found no court that has put it that way either. So take the expectation as mine, and the collision as the Regulation's.

**The counter-argument, at its strongest**, because it deserves one. The material was already public, and the author chose to publish it. Adding a sentence anyone can already read to a corpus does very little extra to that person. And asking each of them is not a real alternative at this scale; it is a way of saying no while sounding procedural. There is force in that, and it is the argument that will eventually be made in a courtroom.

**The conclusion.** On the public record I have, nobody decided. The proceedings were struck out on that undertaking, so there is no judgment, no finding, and no precedent. The question of whether legitimate interests can carry a training run on public posts is open in September 2026, and anyone who tells you it is settled in either direction is telling you what they hope.

## The compatibility test {tone: precise}

Now the second issue, which is the one the purpose rule generates.

A post written years before any of this was collected for something. Running a social platform — showing that post to other people, and keeping it there.

Training a model is a different purpose. So the Regulation asks whether the new purpose is compatible with the old one, and Article 6, fourth paragraph, tells you how to work that out. Call it **the compatibility test**.

The misreading is that it is a general balancing exercise where you weigh the good against the bad. It is more structured than that. Five factors are named, and I am going to walk two of them. The other three are real and I am leaving them.

Factor one that I'll take: the context in which the data was collected, and in particular the relationship between the data subject and the controller. That factor asks what the relationship actually was, when you typed it. The policy's wording is evidence of that, at best.

Factor two that I'll take: the possible consequences of the intended further processing for the person. Not the intent behind it. The consequences.

And the limit, said out loud: this test only runs where the further processing is not based on the person's consent, and not based on a Union or Member State law that meets a particular standard. If either of those is in play, you are somewhere else in the Regulation.

That brings me back to the research carve-out, because this is where people reach for it. Further processing for scientific research is not to be treated as incompatible. And the words that follow are what make it a carve-out rather than a licence: it runs only subject to the research safeguards I mentioned. Two things it does not do. It does not supply a lawful basis — you still need a door. And it does not turn an organisation into a research institution because it has researchers in it.

One more thing about the compatibility test, and it is the thing the rest of the episode turns on. The test only exists at all where data is being processed *for a purpose other than the one it was collected for*. Those are the opening words of the provision. So the test cannot even start until somebody can say what the new purpose *is*. Remember that, because in a few minutes I am going to show you a kind of system that cannot supply it.

## One thing today is not about {tone: neutral}

There is a question sitting underneath all of this that I am not going to answer, and I'd rather say so than let you wonder whether I forgot.

Was it lawful to *copy* the material in the first place? Not to process it as personal data — to reproduce it, as text that somebody wrote. That is a different instrument, with a different set of exceptions, and a different set of courts arguing about it. It belongs to copyright, and to the platform rules, and to a handful of other instruments that are not this series' business.

You do not need it today. Let it go.

## Change one fact {tone: curious}

The way to hear where a rule stops is to move one detail and watch the answer move.

**One.** The posts were public. Does being public change which door you walk through?

For ordinary personal data — barely. Publicity is a factor in the balance, and it is a real one, but it is not a door. There is no basis in Article 6 that reads "the person had already published it".

Change it again, though, and a door does appear. If the data falls into the protected categories, publicity is one of the ways the prohibition lifts, and the Regulation's phrase for it is — manifestly made public by the data subject. End of quote. Different rule, different structure, and that is the next episode.

**Two.** The opt-out is offered before the training run rather than after.

The balance shifts, and it shifts noticeably. A person who could have said no and did not is in a different position from a person who found out afterwards. But now you have the harder question underneath it, and it is genuinely contested: can an opt-out carry a balance at all? An opt-out is not consent. It is a fact about the person's conduct that sits inside the weighing — and how much weight it deserves, when most people never open their settings, is exactly the argument nobody has won.

**Three**, and this is the one with money on it. The corpus is not scraped. It is bought.

Now a buyer has a model, or a dataset, whose history it did not witness. And it has inherited a question it cannot answer.

The European Data Protection Board took this up directly. In Opinion twenty-eight of 2024, adopted on the seventeenth of December 2024 at the request of the Irish supervisory authority, it was asked four questions about AI models, and the fourth was this: what follows, for the later phases, if the development processing was unlawful?

Say what that document is, before I say what it holds. It is an opinion. It is the view of a body of regulators, dated, reasoned, influential — and it binds nobody the way a judgment binds.

The Board takes three scenarios, and they are worth having in order.

In the first, the personal data is retained in the model and the same controller carries on processing it. Then the supervisory authority's corrective powers are in play, including an order to delete — which may limit or halt the model's use, with everything that follows commercially. And there is a second consequence in that scenario, quieter and sharper. The failure to justify the *first* processing may affect the balancing exercise for the *second*. A controller cannot walk into the deployment balance with clean hands it does not have.

In the second, the data is retained in the model and a *different* controller deploys it. The Board's position is that the second controller must satisfy itself that the development processing was not unlawful — including by looking at where the data came from, and by checking for prior decisions of authorities or courts. A duty of inquiry, sitting on the buyer.

In the third, the model has been anonymised before any further processing of personal data occurs. Then the original unlawfulness should not affect the model's later operation — because that operation no longer involves personal data at all.

That third one is the escape hatch. And you already know how narrow it is, because we spent the last episode walking up to it: on this same Opinion, a model trained on personal data cannot in all cases be considered anonymous, anonymity is assessed case by case, and the test turns on whether extraction is negligible for each person. The way out of an unlawful training run is to prove the model is anonymous. Proving that is the hardest thing in this series.

## Which level is doing the work {tone: contemplative}

Let me name the level we have been on, and then push off it once.

The obvious level is technical. Somewhere in that pipeline is a filter, and that filter decides what "public" meant — whether protected accounts were excluded, whether deleted posts were dropped, whether a name in someone else's post counts.

But the filter is not the cause of anything. It is a convenient place to point. The filter does what the organisation asked, and the organisation's answer to the legal question was written as an internal assessment of its own legitimate interests. A document. Written by the party it exonerates.

Push once more, and you are at the institutional level, and this is where it stops being anyone's fault. The design puts the balance in the controller's hands on purpose, because the alternative is a permission system for every act of processing in Europe. Self-assessment is the price of a workable regime. And it surfaces only when someone with a statutory power asks to see it — one national authority, for a platform whose users are spread across the Union and the wider European Economic Area.

Underneath all of that sits an economic fact so simple it is almost rude. The cost of asking is the loss of the data. Nobody who has done the arithmetic wants a real answer.

## What the rule assumes about the machine {tone: pointed}

This is the beat the whole series exists for, so let me slow down.

The purpose rule assumes two things about the world it governs. That there is a purpose, knowable at the moment of collection. And that the set of downstream uses is bounded — that you could, in principle, write them down.

The Regulation is not naive about change. It anticipated that purposes drift, which is precisely why the compatibility test exists. But I told you what that test needs in order to run. It needs a new purpose, named, so that it can be held up against the old one.

Now hold that against a foundation model. A general-purpose model is built so that its uses are not specified in advance. That is what "general-purpose" means, and it is the property the thing is valuable for. Nobody training one can list what it will be used for, because if they could, they would have built something narrower and cheaper.

So here is the claim to carry out of this. This Regulation asks what the data is for. And the answer that makes the model valuable is: we don't know yet.

Those two sentences cannot both be satisfied by being more careful. This is a genuine contradiction between a rule that assumes purposes are declarable and a technology whose worth is that they are not, and no better lawyer closes it. That is my judgment, and I mark it as mine, and it is local — it is about this rule and this kind of system, not about whether the Regulation was a good idea.

## As written, as enforced {tone: measured}

Two things are in different states, and you should be able to hear which is which.

Settled: training on personal data is processing, and it needs a basis. Nobody serious disputes that.

Contested — and both sides have names. The same Board, in the same Opinion, was asked how a controller demonstrates legitimate interest for the development phase, and answered the question rather than closing the door. And when a provision was proposed to say so expressly, the Board and the European Data Protection Supervisor said it was not needed, because legitimate interests may already serve. So: conditionally available on the regulator's own view, untested by any court this programme has found. That proposal is still in negotiation as this is recorded, in September 2026, and everything about it will have moved by the time you hear it.

Now the enforcement pattern, which is the difference between the rule as written and the rule as it lands. What this area has produced is undertakings, pauses and switched defaults. As at September 2026, this programme has found no decision on the merits — no ruling saying yes, this basis works, or no, it does not.

Ask what that pattern actually produces. Accountability said: be able to demonstrate compliance. What gets produced is the demonstration. An assessment, filed, available if requested. Whether the assessment was any good is a question that has an answer only in the rare case where someone with power reads it. In this story, nobody ever did. The case ended before anybody had to.

## The model, still standing {tone: grave}

Back to Dublin, and to the sentence I planted at the beginning.

The undertaking deleted the corpus. Posts made in a defined window, used to develop, refine or train Grok — gone, and not to be processed further. That is a genuine result. A regulator moved fast, used a power it had never used, and got an outcome within four weeks.

And the model trained on that corpus was not mentioned.

Put the Board's framework next to that, and here is what follows. On that framework there are two ways the model is dealt with: either it turns out to be anonymous, in which case there is nothing left to reach — or an order reaches it. Neither happened. That is my inference from two sourced facts placed side by side — nobody has held it, and it may be wrong about what the undertaking's words actually covered.

There is a second gap I cannot close. Whether that undertaking bound xAI, as a separate legal person, or only the platform company that gave it — I do not know, and this programme has not established it. And that gap is itself the shape of the problem: the corpus and the model can end up in different hands inside the same corporate group. In October 2024 — again on reporting rather than a document I hold — the platform's privacy policy was changed to permit third parties to train on users' posts as well. The corpus travels, and it travels faster than any undertaking about it.

One question to sit with. When a regulator deletes the training data and leaves the trained system running — what exactly has been protected?

{pause: 2.2}

## What you now ask {tone: lucid}

Three questions to carry out of this, for any system you meet.

The first. What purpose was stated when this data was collected, and by whom? Not what the company says it does now. What was declared, at the moment of collection, to the person who typed it. Ask that of a general-purpose model and the honest answer is a shrug — and the shrug is the whole problem. This Regulation asks what the data is for. The answer that makes the model worth building is that nobody knows yet.

The second, and this is the one that does the most work. When someone says the processing is necessary — ask which sense they mean. Necessary as in there is no less intrusive way to do this. Or necessary as in this is how we do it. Those are different claims and the word hides the difference.

And the third, which is really a wager. If the answer is legitimate interests, ask who wrote the assessment that says so, and ask them what losing the balance would look like. If nobody in the organisation can describe what losing looks like, then no balance was performed. Something else was performed, and it was written down.

{pause: 1.4}

Next time, the rule changes shape. There is material in a corpus like that one which may not be processed at all — not on consent, not on legitimate interests, not by anybody, unless a specific door opens. A prohibition rather than a permission.

And the thing that makes it hard is this. Nobody has to write down the forbidden category for a machine to work it out.