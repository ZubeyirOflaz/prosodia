---
episode: 1
title: The Same File, Twice
defaults:
  tone: measured
  rate: normal
---

## The word, repeated {tone: tense}

They chose an ordinary word. And they asked a production chatbot to repeat it — not a hundred times, not until it got bored, but indefinitely.

For a while, it did what it was told.

Then it drifted. Then it stopped behaving like an assistant altogether, and began producing text nobody had asked for — stretches of the material it had been trained on. And among that material, the researchers reported, contact details belonging to real people. Not invented details that merely looked plausible. Theirs.

The people who did this were Milad Nasr, Nicholas Carlini and eight colleagues, and they published it as "Scalable Extraction of Training Data from Production Language Models" on the twenty-eighth of November, 2023. They call the technique a divergence attack: you push the model off the register it was trained to hold, and something else comes through. They disclosed it to the company first and waited ninety days before publishing. Their paper reports that the attack surfaced training data at roughly a hundred and fifty times the rate of ordinary use — one attack, on one model, in late 2023. I'll date that figure and leave it there.

Now hold on to the part that is easy to miss.

Somebody had to try.

It did not leak. It did not spill. A person sat down and did a specific, deliberate, slightly absurd thing for long enough, and then a stranger's details arrived. Whether the machine was holding those details *before* anybody tried turns out to be a legal question, and a hard one.

Because there is no filing cabinet inside the thing. There are no rows. There is no record in it that belongs to anybody.

And a stranger's contact details came out anyway.

## Where this is {tone: measured}

This is The Collisions.

The series before this one took a single instrument — the Artificial Intelligence Act — and read it end to end. This one is about what happens when that instrument is not the only one in the room. Every AI system operating in Europe answers to more than one body of law at once, and those bodies of law were drafted by different people, at different times, about different things. Nobody designed the overlap. It simply happened.

So the question, every episode: which rule actually bites, who does it bind, and what falls through the seam between them.

Today, the oldest and heaviest of them — the General Data Protection Regulation — and the one question that everything else waits on. Is the material these systems were built out of personal data at all? If it is, a very large body of obligation switches on. If it is not, almost none of it does.

Two ways of hearing this Regulation will send you wrong, and I want to refuse both before we start.

The first is that it's a bag of rules — a pile of separate obligations you work through one at a time. What it actually is, is a single definition with an enormous amount hanging off it. If the definition doesn't catch, nothing else in the instrument ever runs.

The second misreading is more tempting, and it usually catches people with technical training: that the thing is a decision tree. Almost every term that matters here is a standard rather than a switch — something a human being applies to facts, in a situation, and can get wrong. There is no flowchart underneath any of it.

One piece of honesty about scope. Large parts of this Regulation will never appear in this series: what happens when data leaves Europe, what happens when there's a breach, the whole architecture of fines. There are others. I'm not going to read you the list, and I'm not promising them later either. This is a series about collisions, not a course on the Regulation.

## What the machine actually does {tone: precise}

Before any rule touches this, I want to describe the thing being governed the way the people who build it would describe it.

You crawl. You gather text at scale from the open web and from whatever else you can reach. You filter and de-duplicate, because repeated material distorts what follows. You tokenise — cut the text into the small units the system actually operates on. Then you train: you run the material through a network and adjust its parameters, over and over, so that it gets better at one narrow task, which is predicting what comes next. When you're finished, you have a set of numbers. The weights. You ship those, and at inference time you serve outputs from them.

Notice what is absent from that description.

At no point does anyone build a table. There is no row for a person, no field called "name" that you could sort by or search or point at. The training material had rows in it, sometimes. What comes out the other end is a very large arrangement of numbers, and what any individual sentence contributed to those numbers is a matter of degree.

The field has a word for the recoverable end of that spectrum. Memorisation.

Carlini, Ippolito, Jagielski, Lee, Tramèr and Zhang set out the operational version of it in a paper called "Quantifying Memorization Across Neural Language Models", at the ICLR conference in 2023. A model has memorised a string from its training data when, prompted with the text that came just before it, the model emits that string word for word. Their point is that this is a quantity you can measure rather than a property a model either has or lacks. And it grows with three things. The size of the model. The number of times the example was duplicated in the training data. And the length of the prompt you use to go looking.

That third one is the one to keep.

It means the same model can look clean under a short prompt and give back training data under a longer one. So whether a model has memorised something is partly a fact about how hard you tried.

{pause: 1.4}

There is a second kind of disclosure here, quieter than the first, and it deserves a sentence of its own.

It's called membership inference, and it was set out by Reza Shokri, Marco Stronati, Congzheng Song and Vitaly Shmatikov at the IEEE Symposium on Security and Privacy in 2017. You take a record. You have nothing but ordinary outside access to the model — what the field calls black-box access, meaning you can put questions in and read answers out and see nothing whatever of the machinery. And from that you try to establish whether that record was in the training set at all. Nothing the person wrote ever comes back. You learn only that they were in there. For some sets of people — a clinical study, everyone who contacted a helpline — that on its own is the disclosure.

Two different questions, then. Can the content be got out. And: can it be shown that this particular person was in there. Keep them apart. They do different legal work later.

One more piece of engineering, because a lawyer always asks for it. Machine unlearning — removing one training example's influence after the fact, without retraining from scratch — is an active research area. There is no accepted guarantee, and no agreed way to verify that it worked.

Does the system behave as I've described it? It does, and that's why this episode opens on an experiment rather than an argument. Extraction has been demonstrated against deployed commercial models by named researchers who published their method. Separately, in November 2025, a German regional court — the Landgericht München I, in a case brought by the collecting society GEMA — found that song lyrics could be got out of a production model, and held that the memorised work in the model was itself an act of reproduction. That's copyright, not data protection; a regional court, not the Court of Justice; and reported as under appeal. One sentence of corroboration about the mechanism, and I'm building nothing on it.

## The words that do the work {tone: precise}

The sentence all of this depends on sits in Article 4 of the Regulation — the definitions article. A definitions article is a dictionary rather than a rule, which is exactly why it can quietly decide more than most rules do.

{tone: quoting, rate: slow}

Quote. Personal data means "any information relating to an identified or identifiable natural person". And an identifiable natural person is one "who can be identified, directly or indirectly, in particular by reference to an identifier such as a name, an identification number, location data, an online identifier". End quote.

{tone: precise, rate: normal}

That's the citation, once. From here on I'll call it the subject test.

You were probably expecting a different example from me. A customer record — a row with a name, an email address and a date of birth in it. I'm not going to use one, because that example teaches the wrong lesson. It leaves you thinking personal data means data with your name on it, or data you handed over.

Listen to the words again. *Any information relating to* a person who can be identified. Directly or indirectly.

The load sits on that one word, identifiable, and it's where a technically trained listener goes wrong first. Identifiable does not mean somebody identified them. It means they can be.

Try the error on something harmless before we put it near the Regulation. Nobody has ever picked the lock on my front door. It does not follow that the lock cannot be picked. Whether it can is a question about the lock, about who's holding what tools, about how long they have — and not in any way a question about what has happened so far.

Now put the lock down. Identifiable is a test about capability, not about history.

{pause: 1.2}

And its limit, in the same breath: a natural person. A living individual. A company's own commercial information is not personal data merely because it is sensitive, and this Regulation also has limits on its own scope that I'm not covering today. They exist. Don't leave here applying the definition wider than it goes.

Second definition, and it's shorter. Processing.

{tone: quoting, rate: slow}

Quote: "any operation or set of operations which is performed on personal data or on sets of personal data, whether or not by automated means, such as collection, recording, organisation" —

{tone: precise, rate: normal}

end quote, and the list carries on well past where I stopped.

You don't need the list. You need two things from it. The first is the phrase the drafters put in early: on personal data, *or on sets of personal data*. A record, or a collection. The definition was built to reach both.

The second is how little it takes to be inside. Almost anything you can do to data is processing. Collecting it is processing. Training on it is processing. Deleting it is processing — erasure is on the list too.

So the sentence "we didn't use anybody's data, we only trained on it" describes a kind of processing. It does not describe a way out of the Regulation.

{pause: 1.4}

A question for you, and take a moment with it. A corpus of web text, with every obvious name stripped out of it. On the subject test — personal data, or not?

{pause: 1.4}

## Why an open definition {tone: lucid}

Before I answer that, why is the definition shaped like this at all?

The road not taken was a schedule. Several national laws and most sectoral rules do it that way: list the protected fields — name, address, identification number — and regulate those. It's administrable. You can tell, from a column heading, whether you're inside the rules.

Europe went the other way, in a text written in 2016, and chose an open functional definition: anything relating to somebody you can pick out. The reason is that a schedule can be evaded by inventing a new kind of identifier. A device fingerprint is not a name. A session token is not an address. Under a schedule they're outside; under the subject test they're squarely in — and the Regulation's own wording names an online identifier for precisely that reason.

What was traded away was boundaries. A definition that wide puts very nearly everything in scope, and moves the whole argument to one place. Identifiability — which is exactly where the argument sits now, and where the rest of this episode happens.

## Working it {tone: measured}

So. Is a scraped web corpus personal data?

I'm going to say the moves out loud, because the method is half of what I want you to take away. State the issue. Name the instrument. Apply it to these facts, not to facts in general. Take the best argument against your answer. Then conclude.

The issue: whether a corpus assembled by crawling the open web is personal data within the subject test.

The instrument: the subject test. Any information relating to an identified or identifiable natural person.

The application: the open web is largely made of people writing about themselves and each other. Forum posts with signatures. Staff pages. A message board thread from 2009 where somebody's full name sits three lines above their phone number. Strip the obvious identifiers and the relation survives, because the surrounding text still relates to that person and still lets them be picked out indirectly.

The counter-argument, and you will hear it every single time: it was public. They put it on the internet themselves.

Take it seriously, then answer it. There's nothing in the subject test about whether information was public. Public and personal are two different axes. A phone number in a printed directory is published, and it relates to an identifiable person, and both of those are true at the same time. Publication may matter a great deal to a later question — whether there was a lawful reason to process it — but it does not lift the material out of the definition.

The conclusion, plainly. In the ordinary case, a general web corpus is personal data. That is not a close call.

Now the escape hatch people reach for next, and it's where the most-misused word in this field lives.

Pseudonymisation. Quote: processing personal data "in such a manner that the personal data can no longer be attributed to a specific data subject without the use of additional information, provided that such additional information is kept separately". End quote.

Picture a drawer. You take the names out of the file, you put them in a drawer in another room, and you lock it. The file is now pseudonymised — and the Regulation's own answer, written into the definition itself, is that the file is *still personal data*, because the key exists. Somebody can walk to the other room.

That's the drawer. Keep it in view. We come back to it twice, and the second time it decides a case.

## Who decided {tone: precise}

Next: who owes the duties?

Controller. Quote: the person or body "which, alone or jointly with others, determines the purposes and means of the processing". End quote. I'll call that the purposes-and-means test.

The wrong instinct is that the controller is whoever's holding the data — which would make the company renting out the hard disks responsible and the company that decided to crawl the web innocent. The test asks something else entirely. Who chose why. And who chose how. Note the phrase "alone or jointly with others": there can be more than one controller for the same processing, and how that's divided up is a machinery I'm not opening today.

Processor. Quote: one who "processes personal data on behalf of the controller". End quote. *On behalf of.* That's the whole weight of it. And the consequence people miss is this: if you decide a purpose of your own — you were handed data to host, and you start training on it — you have stopped being a processor, whatever your contract calls you. The contract is evidence of what was agreed, and not an answer to what was done.

And that gives us the first collision of this series, in two sentences. The other instrument in the room allocates responsibility by who developed a system and placed it on the market as against who uses it — provider and deployer, with duties attaching at the moment the thing is placed on the market or put into service — where this one allocates by who chose the purposes and who chose the means, from the first moment data is touched. Same company, same afternoon, two tests that can pick out different people.

Two more definitions, quickly, because the case that follows turns on them. A recipient is anyone the data is disclosed to — and the definition carries its own carve-out, because a public authority that receives data in the course of a particular inquiry is not a recipient. A third party is anyone standing outside a particular circle: outside the controller, outside the processor, outside the people working under their authority, and outside the person the data is about.

They sound interchangeable. They aren't, and here is one place the difference bites. Among the reasons this Regulation gives for processing lawfully at all, one of them is an interest pursued not by the controller but by a third party. Which of the two words fits you decides whether that door is even open.

So. A file that moved.

## The regulator, then the Court {tone: measured}

Our question — is the corpus personal data at all — has two answers, nine months apart, from two institutions, and they do not reason the same way.

The regulator first. The European Data Protection Board adopted Opinion 28/2024 on the seventeenth of December, 2024, at the request of the Irish supervisory authority — which matters, because Ireland supervises most of the large model providers established in the Union. The Board was asked four questions. Take the first: when can an AI model be considered anonymous?

The answer. A model trained on personal data cannot in all cases be considered anonymous. Anonymity is assessed case by case. And a model may be anonymous where the probability of extracting personal data from it — directly, or by putting queries to it — is negligible for each data subject.

Said plainly: there is no such thing as an anonymous model in general. There is only this model, assessed on what someone could actually get out of it.

Now look at what kind of test that is. It is a claim about what an adversary can obtain, which makes it falsifiable — by experiment. And you have already heard the experiment. Somebody had to try, and the whole test is about whether trying works. The lawyers and the security researchers arrived at the same shape of question from opposite ends of the building, without coordinating.

And say what the Opinion is, because the word is doing real work. It is the Board's view, dated December 2024. It binds nobody the way a judgment binds.

{pause: 1.4}

Before I tell you what the Court did — think about the drawer, and the key in the other room. Does it matter *who* is holding the file?

{pause: 1.4}

Case C-413/23 P, European Data Protection Supervisor against the Single Resolution Board, judgment of the fourth of September, 2025.

The facts are concrete. After the resolution of Banco Popular Español on the seventh of June, 2017, the Single Resolution Board ran a procedure letting former shareholders and creditors comment on a preliminary decision about compensation. It passed some of those comments on, in pseudonymised form, to Deloitte, which was valuing the effects of the resolution. The comments had been detached from the names. The Board kept the key.

I haven't read the Court's own words, so I'll paraphrase and attribute rather than pretend to quote. As reported, what it held is this. Pseudonymised data is not automatically personal data for every party that touches it. Whether it counts as personal data in a given pair of hands depends on whether that recipient can reasonably re-identify, judged on the technical, the organisational and the legal circumstances. The Court set aside the judgment below.

Which means the same file can be personal data in the hands of the sender, and not personal data in the hands of the receiver.

The same file. Twice.

That is the first time the Court has said so explicitly, and it departs from where the supervisory authorities had sat for years — which was that pseudonymised data is personal data always and everywhere. Those two positions no longer sit comfortably together, and nobody has reconciled them.

And now the limit, which I want heard as loudly as the holding. That case was about a set of written comments sent to an auditor. No model weights came anywhere near it. Whether the Court's relative approach reaches a trained model at all is precisely the open question. The Board reasons from what can be extracted. The Court reasons from who is holding it. Both are live, the Court is later, and the Court binds — and the argument where those two meet on a model has not yet been run by anybody.

## Change one fact {tone: curious}

The way to hear where a rule actually stops is to change one detail and watch the answer move. Three times.

One. Everything the same, except that before the file is sent, the key is destroyed. The names are gone and nobody can put them back. Notice what shifts: not only the recipient's position, but the sender's. If the link is genuinely unrecoverable by anyone, the argument that this file relates to identifiable people gets much harder for everybody in the chain. The drawer isn't locked now. There is no drawer.

Two. Everything the same, except the recipient is the firm that crawled the web in the first place, and it's holding the corpus those pseudonyms were drawn from. It can re-link, with what it actually has, on a Tuesday afternoon. Back inside the Regulation — for the recipient, and for the sender who chose to send it there. Relativity cuts both ways. It can put you outside. It can just as easily put you in.

Three, and this is the one that matters for machines. Change the facts so that the model can be prompted into emitting a training string that identifies a particular person. Now the claim isn't only that the model was *derived from* personal data. The argument becomes available that the artefact itself contains it — and everything follows from that. The business that took a general model and fine-tuned it on its own support tickets is now a controller of personal data it never collected, about people it has never dealt with, sitting inside a file of numbers it cannot read.

## Which level you are standing on {tone: contemplative}

When someone explains to you why this is hard, listen for which level the explanation is sitting on. The level is usually a convenient stopping place rather than a cause.

The technical answer: there are parameters, not records, so there's nothing to delete. True as description. But it explains nothing — it restates the situation in the vocabulary of the people who built it.

Push back one. The organisational answer: nobody owns the corpus. It was assembled by a team that has moved on, from sources partly logged and partly not, at a company that has reorganised twice since. The reason nobody can tell you whether a person is in the training set is very often that nobody kept the kind of record that would let them.

Push back again. The economic answer, which is the honest one: deletion costs a retraining run. That is why "can we delete it" is almost never asked as a purely legal question inside a firm. It's asked as a budget question wearing a legal question's clothes.

And underneath all three, the thing that actually generated the problem. A person who never transacted with any of these companies, never agreed to anything, has no way of knowing they're in the set, and no practical way of finding out. Every level above that is a description of the machinery that arrived at it.

## What the Regulation thinks a machine is {tone: pointed}

Now the beat this whole series exists for. What does the rule assume about the thing it governs?

There's a definition in Article 4 I've kept back, and it gives the game away. A filing system. Quote: "any structured set of personal data which are accessible according to specific criteria". End quote.

If you heard that and thought "a database", you are wrong in both directions. A drawer of paper cards filed by surname is a filing system, and there's no electricity anywhere near it. A shoebox of unsorted receipts is not one, however much personal data is in the box. The definition isn't asking about the technology. It's asking whether you can go in by a criterion and come back out holding a thing — and having got it, read it, correct it, or destroy it.

That is a picture of the world, and the picture came from a medium: the register, the card index, and then the database, which is the card index with electricity. Every remedy in the instrument is cut to that shape. Access means show me my record. Rectification means correct my record. Erasure means take my record out. All three need something you can point at.

A trained model has parameters. Nothing in it is accessible according to specific criteria — you cannot go in by a name and come out with a person. Whatever is in there is smeared across an enormous quantity of numbers, in a form where the same numbers that encode somebody's phone number also encode grammar, and arithmetic, and the plot of Hamlet.

So here's the claim I want to land, and I'll say it more than once, because it is the episode.

The remedies in this Regulation were built for a filing cabinet, and a trained model is not one. That is why the argument in Europe moved away from "delete my record" and back to something much more basic — is this personal data at all?

## Contested, and unbuilt {tone: neutral}

Three states of a question, and I want you to be able to hear which is which.

Settled: the subject test catches indirect identification. That isn't in dispute anywhere.

Contested, and recently moved: whether identifiability is absolute or relative. Absolute means a file either relates to identifiable people or it doesn't, full stop, for everyone. Relative means you ask the question separately for each party holding it. The supervisory authorities were, for years, effectively in the first camp. The Court's 2025 judgment reasons in the second. That's a live disagreement between two institutions that are supposed to be applying the same words.

Contested, and here's where I'll ask you to commit, because you will meet this argument. Two positions. The first: a trained model is a derived artefact — statistical regularities lifted out of data — and the personal data stayed behind in the corpus, so the model itself is outside the Regulation. The second: the weights contain personal data, because under the right prompt they'll give it back.

My answer, and it's mine rather than anybody's holding. Neither survives as a general claim. The first is the weaker of the two, and the extraction literature is why — you cannot assert categorical anonymity for an artefact whose anonymity is *defined* by what can be got out of it, while people keep getting things out of it. But the second doesn't generalise either. A small model, trained on well de-duplicated data, queried by someone without the original corpus, may genuinely have nothing recoverable in it. That leaves us with the answer the Board gave: case by case, on evidence, about this model. Less satisfying than a rule. Also, I think, the only thing the facts will carry.

Still moving: whether unlearning can be verified. No standard, no accepted test, an open research question as at September 2026.

And then the gap between the text and the world. What has actually happened, on the public record, is undertakings, pauses, and settings changed after the fact. As at September 2026, this programme knows of no order anywhere in the Union requiring a trained model to be deleted on data protection grounds. That is a checkable claim with a date on it — and if it's wrong by the time you hear this, it's wrong in an interesting direction.

## The question this series holds {tone: contemplative}

One more thing before the close, and it's a promise.

This series has a question it is deliberately not answering today. Europe's response to these systems has been to layer instruments — a data protection regulation, a product statute, an AI Act — each written for something slightly different, all of them landing on the same machine. The question is whether layering actually protects anybody. Or whether it multiplies duties for the organisations that already had lawyers, while leaving the same person exposed in the same place. It matters that the Act, for instance, is enforced by market surveillance authorities and gives the person harmed no right to sue under it at all.

I can't answer that until the layers are on the table. So it is held, on purpose, until Episode 10 — and I'm telling you now so that you can hold me to it.

What I'll say today is only this. Be suspicious of both easy answers. This instrument is not idle here: it reached a general-purpose model on a question of first principle, before any AI-specific law had said a word about it. And it is not sufficient either, because every mechanism in it presumes that somebody can find the data.

## What you now ask {tone: warm}

Not a summary. The point of an episode like this one is the questions you carry to the next system you meet, and there are three I'd want you to have.

First. Who could re-identify this, with what they actually hold? Not "could anyone, anywhere, with unlimited resources" — the question is about a specific party and the tools genuinely available to them. That's what the Court made central in 2025, and it's the question most confident claims about privacy are silently assuming an answer to.

Second. Is the claim of anonymity about the file, or about the situation? Somebody will tell you a dataset has been anonymised. Ask who's holding the key, where it is, and what happens if one organisation ends up with both halves. Anonymity that depends on two parties staying separate is a fact about an arrangement — and arrangements change.

Third, and this is the one that catches people out. If a person asked tomorrow for their data to be deleted, what exactly would be deleted? And could anyone verify it?

{pause: 1.4}

If the answer is "we'd remove it from the corpus", ask what happens to the model that was trained on the corpus. If the answer is "we'd retrain", ask who is paying. And if the answer is "the model doesn't contain it" — you now know exactly what that claim costs to prove.

{pause: 1.6}

So. If a scraped corpus is personal data, and in the ordinary case it is, then somebody needed a reason in law to touch it. The Regulation supplies six reasons, and only six. Nothing outside that list makes processing lawful.

Six.

And very nearly the whole argument about how these systems were built has come down to one of them.

That's next time.