---
episode: 5
title: The Red Lines
defaults: { tone: measured, rate: normal }
---

## A label attached to a phone call {tone: measured}

Somewhere inside a Hungarian bank's systems, in 2018, a recording of a telephone call is saved with a label attached to it.

The label is not the customer's name. It is not the account number, and it is not the reason they rang. The label is how the customer *sounded*.

For forty-five days, anyone with the right access can play that call back and read the label off it.

One thing before the facts. Everything I am about to describe was decided under the General Data Protection Regulation, in 2022 — three years before Article 5 of the AI Act applied to anything at all.

The bank is Budapest Bank. From May 2018 it ran artificial-intelligence speech processing across its customer-service call recordings. The software listened for keywords. It also formed a view about the emotional state of the person speaking, and it stored that view alongside the audio.

What was the view for? Several things. Two of them matter today. The results were used to rate the quality of the call-handling staff's work. And they were used to rank the calls, so that the software could recommend which customers somebody ought to ring back first.

Hold on to the first of those.

The emotions being inferred belonged to the customers. The rating that came out of them landed on the staff.

In September 2021 the Hungarian data protection authority — NAIH — opened an investigation. The case is NAIH-85-3/2022. It fined the bank two hundred and fifty million forints, about six hundred and sixty-five thousand euros, which at that point was the largest data protection fine Hungary had issued. It found automated decision-making and profiling with no valid legal basis. It found no proper balancing of interests, and safeguards it judged inadequate. It held that nothing short of freely given, informed consent could ground that kind of analysis of a person's voice.

And then it ordered the bank to stop analysing emotions.

{pause: 1.0}

## Where we are {tone: lucid}

This is The Instrument, a series about how Europe decided to regulate artificial intelligence as a product placed on a market. This is its fifth episode.

Today is about the part of that structure that is not a rung. Article 5. Ten prohibited practices. Not managed. Not audited. Forbidden.

What today gives you is the sharpest instance in the whole Act of a question this series keeps returning to: what does a rule assume about the machine it is aimed at?

## Two things this article is not {tone: precise}

Before the text, two misreadings. Both of them are what a technically-minded listener reaches for, and both will cost you the episode.

The first is that Article 5 is a bag of ten independent rules, like ten items on a banned-substances schedule, each one self-contained. It is not. Several of them are built out of definitions that live somewhere else entirely, in Article 3, and two of them — as you will hear — share an entire separate paragraph deciding how far they reach.

The second misreading is that it is a decision tree. That you can take a system, run it down the ten branches, and fall out of the bottom with an answer. You cannot, and the reason is worth holding: most of these prohibitions turn on *purpose* and on *context*, not on capability. The same piece of software can sit on either side of the line depending on what it is sold for and where it is switched on.

So: not a list of things, and not a flowchart. A set of conditions about use.

## What is actually prohibited {tone: precise}

The first word this episode has to earn decides everything that comes after it.

**Prohibited practice.**

The meaning you are probably bringing is "an illegal system" — a piece of software that is unlawful the way a weapon is unlawful, unlawful in itself, wherever it is and whoever holds it.

That is not what the Regulation says. What each limb of Article 5 forbids is an *act*: the placing on the market, the putting into service, or the use. And in several of the limbs — the emotion one included — the middle act is narrowed further, to putting into service **for this specific purpose**.

Strip that back and it comes to this. Every one of these prohibitions is aimed at something a person or a company *does* with a capability — sells it, switches it on, points it at somebody.

There is a sharper version still. The last of the ten limbs, the one about police using live face recognition in public, does not prohibit placing anything on a market at all. It prohibits only the *use*. You may build it and sell it in Europe. It lands in the high-risk tier, with everything that tier will demand of it. What Article 5 forbids is a police force switching it on.

So, a question, and take your time with it.

Was the software Budapest Bank bought an illegal product?

{pause: 1.4}

No. On these facts nothing tells you the vendor did anything prohibited. The Regulation splits those two apart — the one who builds and sells, and the one who switches it on — and here it is the configuration that the rule reaches, not the product. That distinction is going to do a great deal of work today.

## What the software was doing {tone: curious}

Now the machine, in the language of the people who build it.

Speech emotion recognition works on four properties of the sound itself, and two of them will do. Pitch — how high or low the voice is. And speaking rate — how fast the words come. The other two are loudness, and the quality that makes a voice bright or muffled.

Those properties are extracted from short stretches of audio, usually utterance by utterance. They are then fed to a classifier, which maps them onto a small set of labels — a handful of named emotional states — and typically the system also produces one aggregate figure for the call as a whole.

The keyword spotting that ran alongside is a different animal, and it is worth keeping separate. Matching spoken words against a list is a task with a right answer. Someone said the word or they did not.

The emotion part has no such anchor. A classifier learns by being shown examples that a human being has already labelled. Someone sat with a recording and decided that this one is anger and that one is frustration. The model is learning to reproduce those judgements. Whatever was in those labels is what comes out the other end.

Keep that in your pocket. We will need it.

And it is worth naming, plainly, the level at which a bank decides to buy a thing like this. It is economic. A call centre is a throughput business — calls per hour, complaints avoided, staff ranked against each other. Software that scores every call without a supervisor listening to any of them is, in that frame, a productivity purchase. Nobody in the procurement meeting had to be interested in the psychology of emotion.

## The shape of the article {tone: lucid}

Ten limbs. I am not going to read them to you, because a list of ten read aloud is ten things you will not have by the end of the sentence. I am going to give you the shape instead.

Three families, and then two arrivals that fit none of them.

The first family is about **what is done to a person's will**. Systems using subliminal, purposefully manipulative or deceptive techniques, and systems exploiting a person's vulnerabilities — their age, disability, or a specific social or economic situation. Both of those limbs carry the same demanding condition: the technique must have the objective or the effect of *materially distorting* behaviour, in a way that causes or is likely to cause significant harm. That is a high bar, and I will come back to whether anyone can clear it.

The second family is about **being sorted**. Social scoring. Predicting who will commit a crime. And assigning people to categories on the basis of their bodies.

The third family is about **being looked at**. Building face databases by scraping. Inferring emotions at work and at school. And live face-matching in public places by the police.

Then the two arrivals, added in 2026: systems that generate non-consensual intimate imagery of an identifiable person, and systems that generate child sexual abuse material. Those two sit oddly in the architecture, and the oddness is instructive. The other eight are about something being done to a person who is present — classified, watched, manipulated. These two are about an *output*. Nobody need be in the room.

{pause: 1.0}

Now, social scoring, because the phrase is wider in ordinary speech than it is in this statute, and the gap between the two is where listeners get lost.

What the ban says is narrow. Evaluation or classification of people **over a certain period of time**, based on their social behaviour or on personal characteristics — known, inferred, or predicted. And then the score has to lead somewhere: to detrimental treatment in a context *unrelated* to where the data came from, or to treatment that is unjustified or disproportionate to the behaviour itself.

A listener who takes "social scoring" at face value walks away believing credit scoring is banned in Europe. It is not. Evaluating someone's creditworthiness is named in Annex III as high-risk — the tier this series has already built: heavily regulated, and permitted. With its own carve-out, incidentally: systems used to detect financial fraud are excluded from that heading.

## The provision itself {tone: measured}

The provision the Budapest case sits on is Article 5, paragraph 1, point (f). I will read it once, and you will hear where it opens and where it closes.

## The text {tone: quoting, rate: slow}

Quote. *The placing on the market, the putting into service for this specific purpose, or the use of AI systems to infer emotions of a natural person in the areas of workplace and education institutions, except where the use of the AI system is intended to be put in place or into the market for medical or safety reasons.* End quote.

{pause: 1.4}

## In ordinary words {tone: lucid}

You may not sell, switch on, or use a system that works out how people are feeling, if you are doing it in a workplace or an educational institution — unless the reason it is there is medical or safety.

And there is a definition underneath it that decides how wide it goes. An **emotion recognition system**, in Article 3, is a system for the purpose of identifying or inferring emotions *or intentions* of natural persons on the basis of their biometric data.

Two things in that. It is not only about faces — and it reaches intentions, not just feelings. Biometric data, in this Act, means personal data from technical processing of a person's physical, physiological or *behavioural* characteristics. A voice sits inside that description. So a bank listening to how a caller sounds is in the frame. A system guessing at your mood from how fast you type may well not be, because typing speed is not obviously the processing of a bodily characteristic at all.

From here on I will call Article 5 what everyone in the field calls it. The red lines.

## Why this rule, and not another {tone: contemplative}

A legal order whose whole instinct is to manage rather than to forbid drew a small number of absolute lines. Why these?

For the emotion limb, the Commission's stated reason is about consent, and it is not about accuracy. A workplace and a school are asymmetric environments with a fundamental power imbalance. A worker cannot meaningfully decline the microphone. A fifteen-year-old cannot meaningfully decline the camera in the exam hall. Where refusal is not really available, consent cannot do the work it does elsewhere.

Notice something about that reason, though: it is nowhere in the operative text. The provision says where the ban applies and what the exception is. It does not say why. The reasoning lives in the material around the Regulation, and the words that bind are the ones I read you.

And there was a road not taken, which is the more interesting half.

On the eighteenth of June 2021, the European Data Protection Board and the European Data Protection Supervisor published a joint opinion on the draft. They attacked the method itself — the idea of a "positive list", a fixed enumeration of banned practices, on the ground that the harms would not politely stay inside it. And on biometrics they asked for something much larger than what exists: a general ban on biometric identification in publicly accessible spaces.

They did not get it. What the red lines contain instead is one limb, aimed only at police, only in real time, with three permitted objectives, a judicial authorisation regime and an annual reporting duty bolted on.

That is the trade. A general prohibition was on the table, and a narrow one with exceptions is what was built.

## Does the banned thing exist {tone: curious}

Now the question this series asks about every rule, and it is the one that makes today worth forty minutes. Before you reason about what a rule should do with a machine, ask whether the machine does what the rule thinks it does.

Let me demonstrate the shape of the problem on something with nothing at stake.

Suppose a thermometer reads two degrees high, every time, in every room. It is wrong, but it is *reliable*, and reliability is repairable — you subtract two. Now suppose instead somebody hands you a ruler and asks you to measure the length of a Tuesday. There is no correction to apply. The instrument is not miscalibrated. The thing it claims to measure is not the kind of thing the instrument measures.

Emotion inference has been challenged at that second level, and the challenge is serious.

A body of review literature in psychology argues that expressive configurations — what a face does, what a voice does — do not map reliably onto emotion categories across different people and different contexts. The same inner state produces different outward signals in different people; the same outward signal means different things in different situations. The challenge goes deeper than badly trained classifiers. It asks whether the target is stable enough to be classified at all.

I want to be straight with you about the standing of that. I have not been able to pin the argument to a single paper I can name to the standard this series holds itself to, so I am giving you the literature and not a citation, and no figures at all. Take it as that.

## What the ban assumes {tone: pointed}

So set the two things side by side.

Point (f) presumes emotion inference works well enough to be dangerous. The research suggests the inference is not reliable.

Both of those can be true at once, and the resolution matters. An unreliable system that has authority over a worker's performance evaluation is *more* harmful than a reliable one, not less. Noise in a measurement that decides your appraisal is not a comfort.

But look precisely at what has happened. If the capability is not really there, then the thing the red lines have forbidden is a **claim**. What they stop, on that reading, is the use of a vendor's assertion — this software can tell you how your staff are feeling — as grounds for treating a person a particular way.

{pause: 1.4}

That is the move this whole series exists to make audible, and this is its clearest case. A rule aimed at a machine turns out to be a rule about what an organisation is permitted to *act as though* it knows.

And here is where I come down, for what one judgement is worth. Between a prohibition grounded in accuracy and a prohibition grounded in power, the power reading is both the stronger one and the one the text supports — because point (f) says not one word about whether the inference is any good. It does not require the system to work. It does not require it to fail. It asks only where you are standing and what you are pointing it at.

## Change one fact {tone: precise}

Two things are established, and one is still open. Established: the red lines forbid acts, not artefacts. Established: point (f) does not care whether the machine works. Open: what exactly point (f) attaches to. That last one is what the next few minutes are for, and the way to hear it is to change the facts one at a time.

We have the case as it stands: customers' emotions inferred, the output used to evaluate employees.

**One.** Take away the employee evaluation. Same software, same calls, same inference. But the output goes only to the marketing department — nobody is rated by it. The subjects are still customers. The place is still, for the staff standing in it, a workplace.

Does point (f) still bite?

{pause: 1.4}

Notice what turns on your answer. If it does not bite, the prohibition is about *whose* emotions are being read. If it does, the prohibition is about *where the system is running*. The text says "in the areas of workplace and education institutions" — which describes a place, not a person. The Budapest facts sit precisely on that seam, and I am not going to pretend it has been resolved. It has not. There is no enforcement decision under this Act to point at, and this case is the cleanest illustration Europe has of the question being open.

**Two.** Move the same system into the interview room. Emotion inferred from job candidates, and whether they are hired turns partly on the output. That is squarely a workplace and squarely a person whose treatment depends on the reading. This one is easy — which is exactly why it is useful. It shows you that Budapest is a hard case, not a typical one.

**Three.** Now sell the identical capability as a driver drowsiness detector. Same acoustic features, same classifier. The prohibition carries an exception for systems intended to be put into service for medical or safety reasons, and drowsiness detection is a safety case if anything is.

So it is out of the ban. It is not out of the Act. Annex III names emotion recognition under its biometrics heading, which is the high-risk rung — and whether a drowsiness detector is inferring an *emotion* at all is a question somebody is eventually going to have to answer. Note what did the work, though. The capability never changed. The stated purpose did, and the system moved down a tier.

**Four.** The live edge, and this one is newer than the rest of the Act.

A general-purpose image generator. Built for design work. Never intended for anything sexual. But look at its architecture, and at what its interface lets a user do. Producing intimate imagery of an identifiable person is a reasonably foreseeable and reproducible outcome. No significant technical modification required. And it ships with no meaningful safeguards against that, and no way to correct misuse once somebody reports it.

Under paragraph 1a of Article 5, that is enough. Placing it on the market is prohibited. What triggers the prohibition is what the system will predictably do.

{pause: 1.0}

There are limits on that, and they matter. The same paragraph says that for *use*, as opposed to sale, the prohibition bites only where the deployer is actually using the system to generate such material. And a further paragraph carves out manipulation that does not increase the exposure of anything depicted or alter the nature of what is depicted.

But the direction of travel is unmistakable, and it is the sharpest live question in the Regulation: whether "reasonably foreseeable and reproducible" makes the providers of general-purpose tools answerable for what their users do. That is still moving. Nobody knows yet how far it reaches.

## Find the word {tone: wry}

A different exercise now, and I want to be clear before I start that I am not describing an amendment. Nothing here has changed. I am deleting words from the statute out loud so you can hear what they were holding up.

Take the limb about predicting crime. It forbids systems that assess or predict the risk of a person committing a criminal offence — **based solely on the profiling** of that person, or on assessing their personality traits. And it says expressly that it does not apply to systems supporting a *human* assessment that is already grounded in objective and verifiable facts linked to a criminal activity.

Now delete the word *solely*.

Every human-in-the-loop policing tool in Europe changes category overnight. One officer in the chain no longer saves you. That single adverb is carrying the entire predictive-policing prohibition, and it is carrying it in the direction of permission.

One more. The scraping limb forbids creating or expanding facial recognition databases through the **untargeted** scraping of facial images from the internet or from CCTV footage.

Delete *untargeted*.

{pause: 1.0}

Now an investigator collecting photographs of one named suspect is doing a prohibited thing. That word is the whole difference between a dragnet and a case file.

There is a general question hiding in that exercise, and it is the one I most want you to keep. In any rule you are handed: which single word is load-bearing, and what moves if you move it?

## Three operations, three fates {tone: precise}

Where we are. We have the emotion limb worked through, and we have two words pulled out of two other limbs to show what qualifiers hold up. What is left is the family about bodies — being sorted by them, and being found by them. It needs three terms first.

Three words that sound like one word. Almost everyone says "facial recognition" for all three. The Act keeps them apart and gives them different fates.

**Biometric identification** is one-to-many. It takes your biometric data and compares it against a database to establish who you are.

**Biometric verification** is one-to-one. It compares you against something you supplied earlier, to confirm you are who you claim. And Annex III carves it out explicitly — a system whose sole purpose is confirming a person is who they say they are does not land on the high-risk rung.

**Biometric categorisation** is neither. It assigns you to a *class* on the basis of your body. It answers a different question: what sort of person the system has decided you are.

So — which of the three is your phone doing when it unlocks?

{pause: 1.4}

Verification. One-to-one, against a template you handed it yourself, answering a question you asked. That is the operation the Act was least worried about, and the carve-out says so.

The third one has its own prohibition, which people routinely miss. The red lines forbid biometric categorisation systems that sort people individually, from their biometric data, into a short list of protected categories. Two of them tell you the shape of it: political opinions, and religious or philosophical beliefs. The rest are of the same kind, and I am not going to read them.

With a limit written into the same sentence, and these are the Act's words. Quote. *This prohibition does not cover any labelling or filtering of lawfully acquired biometric datasets, such as images, based on biometric data or categorizing of biometric data in the area of law enforcement.* End quote. And the definition itself carries an escape hatch: a categorisation system does not count where the categorisation is ancillary to another commercial service and strictly necessary for objective technical reasons.

Say that back plainly. Sorting faces in a lawfully held collection is not the banned thing. Using a face to guess at someone's religion is.

## Live, in public, by the police {tone: measured}

Two more definitions, and then the last limb.

A **publicly accessible space**, in this Act, is any physical place accessible to an undetermined number of people — publicly *or privately* owned, regardless of whether conditions for access apply, and regardless of capacity limits. A shopping centre is one. A stadium is one. Private ownership does not take you out.

And **"real-time"** does not mean what you would guess. It is not live-versus-recorded. A real-time remote biometric identification system is one where the capture, the comparison and the identification all happen without significant delay — and the definition expressly includes limited short delays, in order to stop anyone engineering their way around the rule by adding a pause. The other kind, post-remote, is not in Article 5 at all. It is high-risk, with its own authorisation regime attached.

{pause: 1.0}

So the last of the red lines: the use of real-time remote biometric identification in publicly accessible spaces, for law enforcement — and here the Act's own words — quote, *unless and in so far as such use is strictly necessary* for one of the following objectives, end quote.

Two of those words are where all the limiting happens. They set the bar above importance, and above justification. Strictly necessary — and only for objectives the statute itself lists. I will give you two of the three: searching for specific victims of abduction, trafficking or sexual exploitation, and missing persons; and preventing a specific, substantial and imminent threat to life, or a terrorist attack. The third points outward, to a list of serious offences in Annex II, which I am naming and not reading.

Around that limb sits paragraphs 2 through 7 of Article 5, and I am describing that machinery in outline rather than walking you through it, because it is six paragraphs of procedure and you would not keep them.

In structure, four things, and two of them decide it. A Member State has to legislate before any of it is available at all — no national law, no power. And each use needs prior authorisation from a judicial or independent authority, with a twenty-four-hour window in genuine urgency and immediate deletion if it is refused. Notification and annual reporting sit on top of those two.

One sentence out of that machinery is worth hearing in the Act's own words, because it rhymes with the word we deleted earlier. Quote. *No decision that produces an adverse legal effect on a person may be taken based solely on the output of the real-time remote biometric identification system.* End quote.

There is that adverb again, doing the same job in the opposite direction.

## As written, as enforced {tone: somber}

Now the part of the episode where the question stops being what the rule says.

The prohibitions became applicable on the second of February 2025. The penalties for breaching them did not arrive until the second of August that year. For six months, Europe had a ban with no sanction attached to it.

The national market surveillance authorities — the bodies that actually investigate, demand documents and impose fines — got their powers on the second of August 2026. The two new limbs, the ones about generated intimate imagery and abuse material, bite on the second of December 2026. As I speak, they are not yet in force. And the high-risk tier I have been sending systems down into all episode — the drowsiness detector, the face-matching system lawfully sold — does not itself begin to apply to Annex III systems until the second of December 2027.

So, as of September 2026, no confirmed penalty under Article 5 has been established. Not one. The red lines are the oldest part of this Regulation in operation and they have produced no enforcement anyone can point at.

That high bar I set aside earlier — materially distorting someone's behaviour, in a way that causes significant harm — nobody has yet had to clear it in a case, and whether it can be cleared at all is genuinely disputed.

Which is why this episode opened where it did. The only emotion-recognition enforcement in Europe that exists is Hungarian, from 2022, under a different statute. Name the level that decision belongs to and it is institutional: a data protection regulator reaching a use case years before an AI law existed, because it was the only instrument in the building. And that is not an accident of Hungary. It is what happens everywhere in the gap between a rule becoming applicable and a body becoming able to act on it.

That data protection law runs underneath almost every case in this series, and it gets a series of its own, called The Data Subject. You do not need to carry it today.

One last piece of honesty about interpretation. The Commission published guidelines on prohibited practices on the fourth of February 2025, with worked examples. They are useful. They do not bind. What will eventually bind is a court, and no court has spoken.

## What you now ask {tone: measured}

Three questions to take out of this, and they are not about the red lines.

First: in the rule in front of you, which single word is load-bearing — and what moves if you move it? *Solely*. *Untargeted*. *Strictly*. The word that reads like emphasis is usually the word doing the work.

Second: is this rule premised on the system working, or on somebody acting as though it does? That is not a philosophical question. It changes what evidence would count against the rule, and it changes who you would have to sue.

And third, the one Budapest leaves open: is the prohibited thing defined by the setting, by the person, or by the purpose? Because a rule that follows the room and a rule that follows the subject go to different places the moment the facts shift, and the drafters do not always seem to have noticed which one they wrote.

{pause: 1.0}

The Act forbids a short list and regulates everything else. That is a choice, and it was made against a live alternative. There were people in the room in 2021 arguing that the instrument should have been built the other way round — starting from the rights at stake rather than from the risk profile of a product.

That argument deserves more than a sentence, and it is getting a whole episode.

We are stepping away from the text next time.