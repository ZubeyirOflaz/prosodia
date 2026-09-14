---
episode: 3
title: Under Whose Name
defaults:
  tone: measured
  rate: normal
---

## A sentence, read flat {tone: somber}

In November 2022, Jake Moffatt's grandmother died.

They needed a flight to the funeral. While they were booking it on Air Canada's website, they used the chatbot there, and asked about bereavement fares. A bereavement fare is the reduced price an airline offers someone travelling because a family member has died. The chatbot told them the discount could be applied for after the fact. Book now. Claim later.

It was wrong. Air Canada's actual policy allowed no retroactive claim, and when Moffatt asked for the difference back, the airline said no. So the matter went to the Civil Resolution Tribunal of British Columbia — a small-claims body, the sort of forum that handles a disputed deposit or a badly fitted roof. File number SC-2023-005609. Decided on 14 February 2024, by Tribunal Member Christopher C. Rivers.

And in that small room, Air Canada made an argument.

{pause: 1.4}

## What the tribunal said about it {tone: quoting, rate: slow}

The tribunal's own words now, from paragraph 27 of the decision. Quotation begins.

"Air Canada suggests the chatbot is a separate legal entity that is responsible for its own actions. This is a *remarkable* submission. While a chatbot has an interactive component, it is still just a part of Air Canada's website. It should be obvious to Air Canada that it is responsible for all the information on its website. It makes no difference whether the information comes from a static page or a chatbot."

End of quotation.

And a paragraph later, quotation: "I find Air Canada did not take reasonable care to ensure its chatbot was accurate." End of quotation.

The order came to 812 dollars and two cents, Canadian — of which 650 dollars and 88 cents was the money Moffatt had actually lost. Payable within fourteen days.

## Where we are, and what is being borrowed {tone: lucid}

One sentence of disclosure, because it matters and because you would be right to ask. That was Canada, a small-claims tribunal, deciding a case in contract and in negligent misrepresentation — which is the ordinary law's name for precisely what that second quotation describes: telling someone something untrue, carelessly, when they were entitled to rely on you. The European Union's Artificial Intelligence Act had nothing to do with it, and does not reach backwards to cases already decided.

But the counterfactual is narrower than it sounds. It is a counterfactual about the facts, not about the law. The same chatbot, offered on a website to travellers in the Union today, would be squarely inside the Act's scope — the Act reaches providers placing systems on the Union market wherever those providers sit. So the question is not "what if this were regulated". The question is: when the Act looks at this scene, who does it see?

This is The Instrument, a series that builds the European Union's AI Act one part at a time and asks what each part can and cannot see. So far we have the gate — what counts as an AI system at all — and the moment duties begin, when a system is placed on the market or put into service. Today we do the cast list: who everyone in that scene *is*, in the eyes of this law, before we go anywhere near what they owe.

And I will tell you now what the episode is for, because it is one idea and everything else hangs off it: the Act attaches its duties to roles, not to technologies, and most real fights under this law will be fights about which role somebody was in.

## The machine, and the honest limit {tone: precise}

Before the law touches it, the thing itself. And a warning about how far I can go.

The decision does not describe the chatbot's architecture. It says what the chatbot said. It does not say how it worked, and nobody should assume. What follows is my characterisation, not the tribunal's and not a cited source's, and I mark it as mine.

A customer-service chatbot of late 2022 was most likely built out of intent classification and retrieval. You type a sentence; the system matches it against a fixed set of things customers ask about — baggage, refunds, bereavement fares — picks the closest, and returns an answer that was already written down somewhere, in a help article, by a person. It does not compose the answer. It selects one.

A generative model does something different. It writes a new sentence, word by word, that is shaped like the right answer. And it fails differently too. The retrieval system serves you a stale document that a human wrote and nobody updated. The generative system invents a fluent sentence that was never true anywhere.

Note the date, incidentally. November 2022 is the month ChatGPT went public, right at the end of it — that is universally reported rather than checked here, and nothing today turns on the day. The point is only that this sits on the hinge between the two kinds of system.

And the uncertainty costs us nothing. Under the Act's definition, both of those systems infer. Both are through the gate. And neither is, in law, anybody.

{pause: 1.4}

## The two words that split the world {tone: quoting}

The Act's cast list lives in its definitions article. Two of them carry this episode.

Article 3, point 3, of Regulation (EU) 2024/1689 defines a provider. Quotation: a person or body that develops an AI system, or has one developed, and places it on the market or puts it into service "under its own name or trademark, whether for payment or free of charge". End of quotation.

Article 3, point 4, defines a deployer. Quotation: a person or body "using an AI system under its authority except where the AI system is used in the course of a personal non-professional activity". End of quotation.

That is the last time I will say those numbers. From here they are the *name rule* and the *authority rule*, and together they are the split the whole Act rests on.

## What those words actually mean {tone: lucid}

Take the wrong answers first, because you are probably carrying one.

The wrong answer for "provider" is: the company that wrote the code. Writing the code does not make you a provider. *Shipping it under your name* does. A firm that builds a system and never puts it on the market is not a provider of anything. A firm that buys someone else's system, strips the branding off, puts its own on, and sells it — that firm is the provider, and it has never written a line of it. In a few minutes I will show you the exact sentence of the Act that does that to them.

The wrong answer for "deployer" is: the user — the person typing. Also wrong. A deployer is an organisation using the system under its own authority, in a professional context, and the Act says so in the same breath — personal, non-professional use is carved straight out. You, at home, asking a chatbot to plan a holiday, are not a deployer. You owe this Regulation nothing at all.

So: two roles. One is about whose name is on the thing. The other is about whose authority it runs under.

There is a third word, and it is a trap. *Operator*. The Act's enforcement provisions talk constantly about operators, and the natural reading — the person operating the machine, the one at the controls — will mislead you every time you meet it. An operator is an umbrella. It covers six roles, and the two you already have, provider and deployer, are both inside it. So when an enforcement provision says an operator must do something, hear it as the statute sweeping the entire cast into one bucket, rather than pointing at somebody sitting at a keyboard.

Two roles that matter, then, and an umbrella word covering six. That is the vocabulary.

## Why roles at all {tone: curious}

The Act could have done this differently, and it is worth saying what it declined.

It could have attached duties to the *system* — a register of certified models, obligations that travel with the artefact wherever it goes, the way a serial number travels with an engine. Somebody certifies the model; the certificate follows the model; whoever holds it holds the duties.

It did not. It attached duties to roles, and it did that for a plain historical reason: those roles were already there. Manufacturer, importer, distributor, and the chain running between them — that is the architecture of forty years of European product law, the machinery that governs lifts and toys and medical devices. The Act did not invent a cast. It reached for the one that already existed and pointed it at software.

What was traded for that? Fit. The roles map cleanly onto a thing that is manufactured once, boxed, shipped, sold and used. They map awkwardly onto software that is configured by the customer, fine-tuned on the customer's own data, and updated on a server on a Tuesday afternoon without anyone being told. One organisation can occupy several of these roles at the same time — and, this is the part that matters, an organisation can *change role* by changing the system.

So I will say again what I said at the start, because it is the whole episode: most of the real arguments under this Act will not be arguments about whether a system is dangerous. They will be arguments about who the provider is.

Two things in hand, then, before we test them on a real airline. Duties here attach to roles, and the roles were borrowed ready-made from product law. Whose name, and whose authority.

## Working it on these facts {tone: precise}

Back to Air Canada. Run the two rules, and answer each one yourself before I do.

Was Air Canada a deployer?

{pause: 1.4}

Almost certainly. It used an AI system under its own authority, in the course of its business, to talk to its customers. That is the authority rule, satisfied without difficulty.

Was Air Canada also the provider?

{pause: 1.4}

That depends on a fact the decision does not give us, and I am not going to pretend otherwise. If the airline bought a chatbot from a vendor and ran it as the vendor shipped it, the vendor is the provider. If the airline commissioned the thing, or took a product and put it into service under its own name, the answer changes. And putting into service, in this Act, has a defined meaning: supplying a system for first use, including for your own use. On that branch Air Canada is the provider *and* the deployer, both, simultaneously, and the entire provider stack lands on an airline.

And what about the chatbot?

{pause: 1.4}

Nothing. The Act has no role for it. There is no category into which a system itself can be placed as a bearer of duties, and that absence is not an oversight — it is the design. Air Canada's submission in that tribunal was an attempt to put something in a box the law does not have. The tribunal called it remarkable, which, from a tribunal member, means absurd.

## Change one fact {tone: pointed}

The way to feel the edge of a rule is to move one thing and watch the answer move. Before I do it, one boundary, said once and then assumed.

The article I am about to use — Article 25 of the Regulation, responsibilities along the AI value chain, and this is its one citation — is written for *high-risk* systems, and so are the documentation duties that hang off it. Whether a customer-service chatbot is high-risk is a question about the Act's tiers, and we have not built the tiers yet. So everything in the next few minutes is machinery you now understand, running inside that boundary. You do not need to settle when it fires. Let it sit.

First. Air Canada licenses the chatbot from a vendor, runs it exactly as delivered, changes nothing. The vendor is the provider. The airline is the deployer. The heavy documentation duties — the technical file, the record of how the thing was built and tested — sit with the vendor, in the vendor's office, in a country the airline may never have visited.

Now change one fact. Air Canada puts its own name on it. The name only; nobody touches the code. A distributor, an importer, a deployer or a third party who puts their name or trademark on a system already on the market is thereafter considered the provider of it, and carries the provider's obligations. Nothing technical has changed. Nobody has retrained anything. A logo moved, and with it, in law, the authorship of the system.

{pause: 1.4}

## The clause underneath that {tone: measured}

That same sentence of the Act carries a rider worth hearing, because it sharpens the claim I keep making. It applies, quotation, "without prejudice to contractual arrangements stipulating that the obligations are otherwise allocated". End of quotation. The parties may divide the work between themselves by contract, and commercial parties absolutely will. That does not take the role away — the regulator still knows whose name is on the box — but it means the fight over who bears the cost of being the provider starts in a negotiation, long before it ever reaches an authority. Arguments about who the provider is, again.

Change a different fact instead. Air Canada leaves the badge alone but fine-tunes the model on its own fare rules, or points it at a task it was never sold for. Now two other limbs of the same article are live: a substantial modification, or a change of the intended purpose. And *substantial modification* is the next term you should not guess at. The wrong reading is "any change" — every patch, every update, re-triggering everything. The Act is narrower. It means a change that was not foreseen or planned in the original conformity assessment — the check the provider ran before the system was allowed onto the market — and that either affects the system's compliance or alters what the system is for. A bug fix the provider anticipated is not one. A new capability nobody assessed might be.

And when the flip happens, the first provider drops out. Article 25's second paragraph — rewritten by the 2026 amendment, and what I am giving you is the wording as it now stands — says the provider that initially placed the system on the market is no longer considered the provider of that specific system. Not shares the role. Stops.

In exchange it picks up a duty: three things to hand across. The documentation, enough for the new provider to assess compliance. Information about the system's known limitations and failure modes — which is the most interesting of the three, because it is an admission in writing that the thing has some. And targeted technical access, so the new provider can test what it has just become responsible for. With one escape hatch: an initial provider who has clearly specified that its system is not to be turned into a high-risk system owes none of it.

Say that plainly. Putting your name on somebody else's system makes you its author in law, and the person who actually built it walks away — owing you the file.

{pause: 1.4}

## One more fact, and this one I cannot answer {tone: contemplative}

Change the last fact, and watch me run out of road.

Keep everything Canadian. A Canadian vendor, a Canadian airline, a website written for Canadian customers. Nothing about the system was ever aimed at Europe. But a traveller in Munich opens that website, asks the same question about bereavement fares, reads the same wrong answer, and books on the strength of it.

The Act's scope provision has a limb for exactly this shape of fact. It reaches providers and deployers established in a third country, quotation, "where the output produced by the AI system is used in the Union". End of quotation.

So. Was the output used in the Union?

{pause: 1.4}

I do not know. The passenger was in Munich. They read it in Munich, and acted on it in Munich, with a card, and the ticket they ended up holding was wrong for them by the price of a bereavement discount. That sounds like use. But four words there are carrying an enormous amount of weight — *used in the Union* — and they do not say whether that means *somebody in Europe saw it* or *this business went looking for European customers*. Those are very different rules. On the first, a great deal of the world's customer-service software is inside a European statute without anyone having decided to put it there. On the second, almost none of it is.

I am not aware of a court that has construed those words, and I am not going to pretend to more certainty than that. The variant earns its place through the question rather than the answer: the hardest thing about this whole scene turns out to be where an output was *used* — and that is a question about the cast list too, because until you know whether the Act reaches them, nobody in the chain is anybody at all.

## The rest of the cast, compressed on purpose {tone: measured}

Take stock. We have two rules — the name rule, which asks whose name is on the system, and the authority rule, which asks under whose authority it runs. And we have watched a name move the provider role from one company to another with no line of code changing.

Now three more roles. I am going to name them and move on, rather than walk through their duties, and you should know I am making that compression on purpose.

An *authorised representative* is not a lawyer and not a sales agent. When the provider of a high-risk system sits outside the Union, it must appoint someone inside it, by written mandate, who holds the paperwork — the declaration of conformity, the technical documentation — for ten years. The authorities can then address the representative in addition to the provider, or instead of it. It is a letterbox with legal weight. And if that representative comes to believe the provider is breaking the rules, it does not get a choice: it must terminate the mandate, and immediately tell the market-surveillance authority why.

An *importer* and a *distributor* are not the same thing and are constantly treated as if they were. An importer is inside the Union and places on the market a system bearing the name of a firm established outside it. A distributor is anyone else in the supply chain who makes a system available, being neither the provider nor the importer. Different position in the chain, different duties, and — this is the point of naming them at all — either of them can become a provider by doing the thing we just watched: putting a name on it.

## Five ways to explain this, and only one of them is a cause {tone: contemplative}

Step back from the law for a moment, because there are several true stories about what went wrong at that airline and they are not competitors.

The technical story: a system returned a stale answer about a policy that had changed.

The organisational story: nobody owned the help content. The chatbot was as accurate as the corpus behind it, and the corpus had an owner in the way a shared kitchen has a cleaner.

The economic story: 650 dollars, against the recurring cost of keeping a help corpus correct in every channel it feeds.

And the story from where Moffatt was standing: a grieving passenger who had no way of knowing what they were talking to, or how much of it to believe.

Now, each of those feels like an explanation, and each of them is really a *summary* of everything upstream of it. "Nobody owned the help content" is not a cause. It is a compact way of describing a set of budget decisions, reporting lines and hiring choices that were made over years by people with names. Push one level back and it dissolves into those. Push again and it dissolves into the economics of running a customer-service function at the lowest cost per contact.

Do that too often and you never land anywhere. So I will do it once more and stop. The institutional story is the one the Act cares about, and it is this: somebody had to be the party responsible, and the airline proposed that nobody was. A tribunal refused. The Act refuses in advance, structurally, by making the entire question "under whose name".

## What the rule assumes about the machine {tone: pointed}

This is the beat that this series exists for, so let me be careful.

The provider–deployer split assumes a stable artefact with a determinate author. Somebody made this thing. Somebody else uses it. You can tell which is which, and the boundary between making and using is visible from outside.

Consider what strains that. A system updated on the provider's servers every week, so that the thing a deployer used on Monday is not the thing they use on Friday, and nobody notified anyone. A system retrained continuously on the deployer's own traffic, so that the deployer's customers are shaping it. A system whose behaviour is reconfigured by the customer writing a paragraph of ordinary English into a settings box — a change to what the system does, made by someone who never touched the model, costing nothing and leaving no record.

The Act's answer to all of that is genuinely clever, and I will say so: it makes modification a role-changing act. Change the thing enough and you become responsible for it. That converts a technical question into a legal status, which is exactly what a statute is good for.

Whether it can be administered is a different question, and the honest answer is that nobody knows yet. It has not been tested. There is no authority to point you at.

## Where people disagree {tone: neutral}

Three joints, and they are in different states — as at September 2026, which is when I am describing the state of play. Two of the three could move.

Whether "under its own name or trademark" is workable when a general-purpose model is served through a dozen intermediaries, each adding a layer, each adding a name — that is contested. The value-chain rules are the least-tested part of this Act, and my own read, offered as mine, is that this is where the litigation will eventually land.

Whether a deployer who writes a system prompt — that paragraph of ordinary English in the settings box I described a few minutes ago — has thereby substantially modified anything: that is still moving. There is no authority. There is no guidance that settles it. If you want a confident answer to that question, there isn't one, and the confident answers you will hear are people's instincts wearing a suit.

And whether any legal system should recognise an artificial agent as a party that answers for itself — that one is settled in practice and unsettled in the academic literature. In practice, nobody has built such a category, and the tribunal in British Columbia is a small demonstration of how the argument fares when somebody tries. In the literature it stays open. And rather than wave at a body of work, I will say it plainly: this series has not found a scholar worth naming for it. What we have is the tribunal's one word for the submission, and the word was "remarkable".

## As written, as enforced {tone: grave}

Now the part that should unsettle you, and it is about Moffatt, not about Air Canada.

There is a role in the Act called the *affected person* — the person a system is used on. Go looking for it beside the other two, in the definitions article, and you will not find it. It is not defined there at all. It appears in the scope provision, which puts affected persons located in the Union inside the Act's reach, and again in a narrow right to an explanation. That absence is a clue, because the natural inference from "in scope" is completely wrong, so let me kill it now: being in scope is not the same as having rights you can enforce for yourself.

This is a market-surveillance regime. Its mechanism is a public authority that investigates, demands documents, and can push a product off the market. Not a court that awards you your money. Under this Act, Moffatt could have complained to a market-surveillance authority. They could have asked for an explanation of a decision, in the narrow circumstances where that right exists. What they could not have done is recover 650 dollars and 88 cents.

The regulator gets the instrument. The person gets a form.

And this is the disclosure I made when we started, coming back in a different shape: this case was decided under some other law, and that is precisely why Moffatt was paid. Ordinary contract. Ordinary negligent misrepresentation — carelessly telling someone something untrue when they were entitled to rely on you. Forty-year-old doctrine in a small-claims tribunal, which looked at a chatbot and shrugged and said: it is part of your website.

What you can actually recover when a system harms you — liability, who pays, and under which law — is a separate series, and it is called Who Pays. You do not need it today. Let it go.

{pause: 1.4}

## Where I come down {tone: pointed}

A local judgement, and only local. On the record we have, the name rule is the right hinge. It is administrable, it is checkable from outside, and it puts the duty on the party that captured the commercial benefit of putting its brand on a system. That is a defensible choice and I would defend it.

But it does one thing and not another. It tells you who the regulator may pursue. It does not tell the person on the other end of the chatbot anything at all.

## What you now ask {tone: lucid}

So. Five questions you can carry to any system you meet, starting tomorrow, whether or not it is in Europe.

Whose name is on this — and did they write it, buy it, or rebadge it?

If I changed the configuration, would I become its provider?

When this goes wrong, which of these parties can the affected person actually sue — and is that the same list the regulator can fine? Sit with that one. The two lists are rarely the same, and the gap between them is where people fall.

Who holds the documentation, and are they the same people who hold the risk?

And the last one, which you now know how to hear: is anyone in this chain suggesting that the system is responsible for itself?

{pause: 1.4}

Roles tell you who owes something. They do not tell you how much. For that, the Act sorts systems onto rungs — and a chatbot that misstates a bereavement policy lands on a rung we have not built yet. That is next.