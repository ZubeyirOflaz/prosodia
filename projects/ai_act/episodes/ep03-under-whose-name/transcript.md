---
episode: 3
title: Under Whose Name
defaults:
  tone: measured
  rate: normal
---

## The chatbot said yes {tone: measured}

In November 2022, Jake Moffatt's grandmother died.

Moffatt went to Air Canada's website to book a flight, and used the chat window the airline had put there. The chatbot said bereavement fares could be applied for retroactively. Book the ticket now; claim the discount afterwards.

They could not. Air Canada refused the claim.

Fifteen months later, on 14 February 2024, the Civil Resolution Tribunal of British Columbia decided file SC-2023-005609. The decision is reported as *Moffatt v. Air Canada*, 2024 BCCRT 149, and the tribunal member was Christopher C. Rivers. Most of it is the ordinary business of a small-claims body. A few hundred dollars, a disputed fare, two parties and a rulebook.

One paragraph is not ordinary at all.

Quoting the tribunal, at paragraph 27. "Air Canada suggests the chatbot is a separate legal entity that is responsible for its own actions. This is a remarkable submission. While a chatbot has an interactive component, it is still just a part of Air Canada's website. It should be obvious to Air Canada that it is responsible for all the information on its website. It makes no difference whether the information comes from a static page or a chatbot." End of quotation.

Hear what the tribunal is comparing. A static page on one side. A chat window on the other. Same website, same company, same answer owed.

And at paragraph 28, still quoting: "I find Air Canada did not take reasonable care to ensure its chatbot was accurate."

The order came to $812.02, Canadian, of which $650.88 was damages — the remainder being pre-judgment interest under the Court Order Interest Act, and the tribunal fees. Payable within fourteen days.

Hold on to the airline's argument. It is the shape of the whole episode. A national carrier stood up in a tribunal and said: the machine is somebody else. Ask it.

## Where this sits {tone: lucid}

This is *The Instrument*, and this is the third episode.

You already have the gate: an artificial intelligence system, in this Act's sense, is a machine-based system that infers, and the Regulation only touches things that get through it. You have the pacing argument, and the reason this instrument was built with parts that can be moved without reopening the statute.

Today is the cast list — the parties standing around the machine, rather than the machine. What the Act calls each of them, and how you change what you are called.

It is the least glamorous material in the Regulation, and it is where real arguments end up. If you are ever in a room with lawyers about an AI system, the fight will probably not be about whether the model is any good. It will be about whose it is.

## What the thing actually was {tone: curious}

Before any rule touches it, the machine.

And straight away a difficulty, which I will state rather than paper over. The decision does not describe the architecture. It tells us there was a chatbot on a website and that the chatbot said something untrue. It does not say how that sentence was produced, and I am not going to assume — assuming is how a confident account of a system becomes a wrong one.

Two possibilities.

The first. A customer-service bot of that vintage — and this conversation happened weeks before ChatGPT was released to the public — was most likely a retrieval system with a classifier in front of it. You type a sentence. The system maps it onto one of a fixed set of intents, each intent standing for a job a customer might be trying to finish. Having picked the intent, it returns a stored answer: a template, or a passage pulled from help content the company itself wrote. Everything it says, somebody wrote in advance. Its only original act is the choice of which stored thing to reach for.

The field has names for that architecture. I am not going to give you one I cannot source.

If that is what happened, the failure is a filing failure. Somewhere in that corpus sat a page about bereavement fares, stale or badly worded, and the classifier reached for it.

The second possibility is a generative model, composing the answer as it goes. That fails somewhere else entirely. The sentence that reaches the customer may never have existed before it was said. Nobody wrote it, nobody approved it, and it arrives fluent enough that nobody queries it.

Two quite different machines. Same customer, same screen, same wrong answer.

To the Act, the difference is nothing. Both infer. Both are through the gate.

## The words that do the work {tone: quoting, rate: slow}

The Act answers "who is responsible" with a set of roles. One company can occupy several of them.

Two carry the whole regulation. Both sit in Article 3, the definitions, and I will read them once.

A provider — and I am leaving out the words "or a general-purpose AI model", which is a separate track we reach in episode nine — a provider is "a natural or legal person, public authority, agency or other body that develops an AI system, or that has an AI system developed, and places it on the market or puts the AI system into service under its own name or trademark, whether for payment or free of charge." End of quotation.

A deployer is "a natural or legal person, public authority, agency or other body using an AI system under its authority except where the AI system is used in the course of a personal non-professional activity." End of quotation.

One more, doing quiet work beneath both. Putting into service means "the supply of an AI system for first use directly to the deployer or for own use in the Union for its intended purpose." Which is to say: handing it to whoever will actually use it, or switching it on for yourself.

Now strip the other two to the studs.

A provider is whoever the thing goes out under the name of. Not whoever wrote the code — the text says develops, *or has developed*. You can commission the entire system from somebody else and still be its provider, if the words "under its own name or trademark" fit you.

A deployer is whoever is using it, under their authority, for something other than their private life.

From now on I will call the first of those *the name rule*, and I will not say the number again.

Four parties stood around that chat window. The airline. Whoever built the bot. Jake Moffatt. And the bot. On those two definitions, how many of the four can you already name?

{pause: 1.4}

## Two ways to read a cast list, both wrong {tone: pointed}

Two misreadings arrive with this material. Refuse both now.

The first: that these are boxes, one per company, ticked once. One organisation can be a provider and a deployer at the same time, of the same system — which happens whenever a firm builds a tool and also uses it.

The second is the one an engineer reaches for: that there must be a decision procedure, facts in, branches followed, role out. No. The role turns on things partly contractual, partly commercial and partly a matter of conduct — whose name is on the launcher, what the agreement allocates, what somebody did to the system last Tuesday. Those move. The role moves with them.

## Why roles, and not a registry of machines {tone: lucid}

There was an obvious alternative and Europe did not take it. The duties could have been attached to the system: a registry of certified models, each with an identity and a file, obligations travelling with the artefact — the way a registration follows a vehicle rather than a driver. Coherent design. Nobody built it.

What was built instead is about forty years old and was not designed for software at all. Manufacturer, importer, distributor, authorised representative: the vocabulary of European product safety, the machinery that decides who answers for a lift, a toy, a pressure vessel. Michael Veale and Frederik Zuiderveen Borgesius, writing on the draft in 2021, put it sharply — what the Act leans on is, in their words, "1980s product safety regulation".

You already hold the intuition, and it comes from a supermarket shelf. A tin of own-brand tomatoes. The chain did not grow the tomatoes and did not can them; some cannery did, and that cannery probably fills tins for four rivals under four labels. The name on the tin is the chain's, so the chain is who you go to. That is the name rule, several decades early, in a tin.

What was traded for it? Determinacy. A tin has one author and does not change on the shelf. A deployed AI system is configured by the customer, tuned on the customer's data, updated by the vendor on a Tuesday afternoon without anyone being told, and resold by two intermediaries in between. The cannery model creaks, and it creaks in one place above all: when does configuring something make you its author?

## Working it {tone: precise}

Now put the case through the instrument.

First, a disclosure. What follows is a counterfactual. The Act did not apply to Moffatt: this was Canada, a provincial small-claims tribunal, deciding a claim in contract and in negligent misrepresentation — carelessly telling somebody something untrue that they then act on. Paragraph 28 is that test in plain words: the airline did not take reasonable care to ensure its chatbot was accurate. The Regulation was not in force there, is not in force there, and does not reach backwards anywhere. It is worth asking what it would have demanded. It is not worth pretending it demanded anything.

But the counterfactual is about the facts, not about the law. The Act reaches providers placing systems on the market in the Union — these are its words — "irrespective of whether those providers are established or located within the Union or in a third country". The same chatbot, offered to passengers in the Union today, is squarely inside the Regulation. That part is not hypothetical.

So. Air Canada, the vendor, Moffatt, and the chatbot.

Air Canada is a deployer. Not close. The system was used under the airline's authority, on the airline's website, in the course of its business, and no exception touches it.

Is Air Canada also the provider? Put the test to it. Did the airline put this system into service under its own name or trademark?

{pause: 1.4}

Answering needs a fact the decision does not give us: what the customer saw. If the chat window carried a vendor's brand, and that vendor sold the same product to five other airlines, Air Canada is a deployer and nothing more. If the window was simply part of the Air Canada website, answering as Air Canada, the airline is both at once.

The counter-argument is contractual. Somewhere there is a services agreement allocating responsibility between the airline and whoever built the thing. In a commercial dispute that document may decide everything. Against this Regulation it does less than a lawyer might hope, because what you *are* is settled by facts — whose name went on it, who used it under their authority — and a document cannot make those facts different. Whether a document can move the duties that follow is a separate question, and the Act answers it in a way you may not expect. Hold that.

Then the party Air Canada nominated. The chatbot. The Act contains no such role. No category for the system as a responsible party, no column for the machine, not even an empty one. Every duty runs to somebody the law already recognises: a person, an authority, a body. The absence is total, and it is deliberate.

The tribunal called the submission remarkable. That is a judge's word for absurd.

## Change one fact {tone: precise}

A boundary stays invisible until you move something across it.

Start clean. Air Canada licenses a chatbot and runs it exactly as the vendor shipped it, under the vendor's brand. The vendor is the provider. If a system like this lands on the high-risk rung — and we do not yet know that it does — the technical documentation and the instructions for use are the vendor's to produce. Air Canada is a deployer, with a deployer's own obligations, which belong to episode seven.

Change one fact. The airline puts its own name on it, and it answers as Air Canada. Two roads lead there and they are not the same road. If the airline commissioned the thing — had it developed — the name rule alone makes the airline its provider. If the airline simply badged a product somebody else had already placed on the market, the route is the flip, and the flip runs only on the high-risk rung.

Change a different fact. The vendor ships a general customer-service bot, and the airline tunes it on its own fare rules — or points it at a job the vendor never intended.

That is the flip.

Quoting Article 25, on responsibilities along the AI value chain: "Any distributor, importer, deployer or other third-party shall be considered to be a provider of a high-risk AI system for the purposes of this Regulation and shall be subject to the obligations of the provider under Article 16, in any of the following circumstances." End of quotation.

Three circumstances. The first, quoting: "they put their name or trademark on a high-risk AI system already placed on the market or put into service, without prejudice to contractual arrangements stipulating that the obligations are otherwise allocated." End of quotation.

The second, quoting: "they make a substantial modification to a high-risk AI system that has already been placed on the market or has already been put into service in such a way that it remains a high-risk AI system pursuant to Article 6." End of quotation.

The third I will summarise rather than read. Change what a system is for, and thereby turn something that was not high-risk into something that is, and you become its provider too.

Plainly: touch it hard enough and you become its author.

Now hear the tail of that first limb again. *Without prejudice to contractual arrangements stipulating that the obligations are otherwise allocated.* Two questions, then, not one. What you are is fixed by what you did — put your badge on it and you are the provider of it, and no drafting undoes that. What you must then *do* is another matter, and in the badge-it case the Act leaves the door open for a contract to send those duties elsewhere. Being it and carrying it come apart. Only the second is negotiable.

The Act follows the flip through. Where it happens, the original provider stops being the provider of that system, and is left owing the new one documentation, information about known limitations and failure modes, and technical access. Unless the original provider had clearly specified that its system was not to be turned into a high-risk one. Then that duty to cooperate falls away — and that is a clause somebody is drafting into a contract this week.

Notice how often the words "high-risk" appeared. They are load-bearing. The flip operates on one rung of a ladder, and whether an airline's chatbot is near that rung we cannot say yet, because we have not built the ladder.

One last change. Move nothing about the system. Move the passengers. The airline is Canadian, the bot is Canadian, the servers are Canadian — and somebody in Munich reads the website and acts on what it says. The Act reaches "providers and deployers of AI systems that have their place of establishment or are located in a third country, where the output produced by the AI system is used in the Union."

That is not the question I asked earlier. Earlier, the airline was offering its service into the Union. Now it offers the service nowhere near the Union, and a person in the Union reaches it anyway. On those facts the answer is genuinely arguable, and I will not pretend otherwise. But you can see what the argument would be about, which is the point of moving one fact at a time.

## Which level you are standing on {tone: contemplative}

Why did the chatbot say the wrong thing? Several answers are true and they are not competing.

Technically: a retrieval system returned a stale document. That is what an engineer would say, and it is correct.

But push on it. Why was the document stale? Because nobody owned the help content. That is an organisational answer — and notice what just happened. The technical explanation turned out to be a tidy summary of the organisational one. The machine did exactly what an unowned corpus makes machines do.

I will stop pushing there, because this can be done forever, and an episode that does it forever never lands. Two further levels are worth naming without excavating. Institutional: a tribunal with no reason to invent a new kind of legal person, which declined to. And rights-based: a customer with no way of knowing what they were talking to, how confident it was, or where its answer had come from.

That last one has a rule now — a transparency duty, live since August 2026, that an interactive system must tell you it is one. It belongs to episode nine, and I will say only what it does not do. It addresses the disclosure. It does not address the sentence being wrong.

## What the rule assumes about the machine {tone: pointed}

Every rule carries a picture of the thing it governs, and this one's picture is unusually clear.

The provider–deployer split assumes a stable artefact with a determinate author. Somebody made a thing. The thing has edges. Somebody else uses it, and at any moment you can say which is which.

Hold that against a modern deployed system. It is updated on the vendor's servers continuously, without the customer being told. It is retrained on new data. Its behaviour is reshaped by the customer with a paragraph of English in a text box — no code, no release, no version number. Under some contracts the customer's own traffic feeds the next version.

Where is the artefact in that? Which version was placed on the market? Who authored the sentence that reached the passenger: the people who trained the base model, the people who wrote the retrieval corpus, or whoever typed the paragraph of instructions that morning?

The Act's answer is not a bad one. It makes modification a role-changing act. Alter the thing enough and you inherit the duties of whoever made it. The flip is what stops the picture collapsing.

But it buys that coherence with a single word. Substantial. The Act's definition turns on whether the change was one the provider had already foreseen and planned for in the check it ran before the system shipped — that check is the conformity assessment, and how it works is episode eight — and on whether the change affects compliance, or alters what the system is for. Everything depends on where that line falls. Whether it can be administered at scale is, honestly, unknown. Nobody has run this instrument long enough to know.

## Where it is contested {tone: measured}

Three joints, in three conditions.

The first is settled in practice and still alive in the literature: whether any legal system should recognise an artificial agent as a responsible party. Practice has answered. As this is written, in September 2026, no court has been shown to have accepted the argument, this tribunal called the attempt remarkable, and the Act does not contain the category. The scholarly argument continues, and it is serious. But nobody should plan around winning it.

The second is genuinely contested. Whether "under its own name or trademark" can work for foundation models re-served through a dozen intermediaries: a model trained by one company, hosted by a second, wrapped by a third, resold by a fourth, and configured by the firm that actually faces the public. The tin of tomatoes had one cannery. This has six, and each can say with a straight face that the name on the tin is not theirs. The value-chain rules are the least tested part of the Act.

The third is still moving, and as this is written there is no authority on it at all. Whether a deployer who writes a system prompt — a paragraph of plain English that changes what the system does — has substantially modified anything. That is not a marginal question. It is what an enormous number of organisations are doing right now, and if the answer is yes, a great many companies that believe themselves deployers are providers.

I cannot tell you how it resolves. Nobody can, today. More than that may be unavailable until somebody litigates it.

## As written, as enforced {tone: somber}

Now the part that matters most.

Suppose all of this had applied. Air Canada established in the Union, the chatbot in scope, every duty live. What would Moffatt have got?

A complaint right. Any person with grounds to think the Regulation has been infringed may complain to the relevant market-surveillance authority, and that authority takes it into its market-surveillance work. What follows is episode eleven's: investigations, documents demanded, corrective measures, fines.

Notice who is missing from that list.

{pause: 1.4}

Moffatt. The Act is a market-surveillance regime and not a private right of action. It tells a regulator what to inspect and a company what to document. The affected person — that is the Act's own term, and affected persons located in the Union are expressly within its scope — gets a channel for complaining, not a claim for money. Fines are paid to public authorities, not to passengers.

Moffatt got $650.88, and every cent came from ordinary contract and negligent misrepresentation, awarded by a small-claims tribunal applying law far older than any of this. The AI Act would have added obligations. It would not have added a dollar.

That gap — between regulatory compliance and individual redress — is one of the most useful things this series can give you, and I will keep pointing at it. Who pays, and under what law, is a different instrument: the revised product-liability regime, and the AI liability directive that was withdrawn before it arrived. That is series three, *Who Pays*. Not this one.

## The parts I am compressing {tone: neutral}

Three more roles, named and not walked through, because I would rather say so than leave you thinking the cast list is two people long.

An authorised representative. Where a provider sits outside the Union and wants to make a high-risk system available on the Union market, it must first appoint one inside, by written mandate. That representative holds the documentation, answers the authorities, and — the interesting part — must terminate the mandate if it comes to believe the provider is acting contrary to the Regulation. A compliance function with a duty to resign. General-purpose models have their own version of the arrangement, and that is episode nine.

An importer is whoever, inside the Union, places on the market a system bearing the name of somebody established outside it. A distributor is anyone else in the supply chain who makes a system available. Their obligations are checking obligations, and they are why a supply chain has friction in it at all. I am not walking through them today.

One further provision, discharged rather than handed on: the 2026 amendment added an article on processing special categories of personal data to detect and correct bias. It governs what data may be handled, not who is who. That sentence is the whole of what this episode needs from it.

## Where I come down {tone: pointed}

A judgement of my own, and a local one. The series' verdict is held for episode twelve, as episode one promised.

Attaching duties to names rather than to machines was right. It is administrable, it matches what customers already believe, and it closes the escape hatch Air Canada reached for. Somebody must be answerable, and the name on the tin is a better rule than any registry of models, because a name is the thing the public can actually see.

The flip is right too, in principle. Alter it enough and you own it.

But "enough" is carrying weight that nobody has yet defined, and that is where I expect this to break first. Not on foundation models, and not on the exotic cases. On some mid-sized company that typed four sentences into a configuration box and has no idea it just became a manufacturer.

## What you now ask {tone: measured}

Four questions to carry into a room you have never been in.

Whose name is on this system — and did they write it, buy it, or put their label on somebody else's?

If I changed the configuration, not the code, would that make me its provider?

When this goes wrong, which of these parties can the affected person actually sue?

{pause: 1.4}

And is that the same list as the one the regulator can fine? Very often it is not.

The fourth the tribunal handed us. Is anyone in this chain claiming the system is responsible for itself? That claim has never worked. The fact that a national airline made it, to a tribunal, in 2024, tells you how badly somebody wanted it to.

Next time, the question this episode cannot answer. Roles tell you who owes something. They do not tell you how much — and for that the Act sorts systems onto rungs, by what they can do to a person. The airline's chatbot lands somewhere on that ladder. We have not built it yet.

## Sources {tone: neutral}

Four things, if you want to go to them yourself.

The decision is *Moffatt v. Air Canada*, Civil Resolution Tribunal of British Columbia, decided by Tribunal Member Christopher C. Rivers in February 2024. The passages I read are paragraphs 27, 28 and 44.

The Act's own words came from the consolidated text of Regulation 2024/1689, as amended in 2026, published on EUR-Lex: the definitions article, the scope article, and Article 25 on responsibilities along the value chain.

The product-safety critique is Michael Veale and Frederik Zuiderveen Borgesius, *Demystifying the Draft EU Artificial Intelligence Act*, in Computer Law Review International, 2021.

And what I could not source, I told you about: the architecture of this chatbot is not in the decision, and nobody outside Air Canada knows what it was.