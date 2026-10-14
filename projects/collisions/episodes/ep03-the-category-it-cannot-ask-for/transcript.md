---
episode: 3
title: The Category It Cannot Ask For
defaults: { tone: measured, rate: normal }
---

## A field that wanted a name {tone: measured, note: "a story told plainly; let the oddity of the field surface on its own, without signalling it"}

In Lithuania there is a law about people who run organisations that take public money. If you run one, you file a declaration of private interests.

One of the things that declaration wanted was the name of the declarant's spouse, cohabitee or partner.

A name. {pause: 0.5} Written in.

And the declarations were published. Put online, in public, {pause: 0.4} where anyone at all could read them.

The man at the centre of this did not file his. In the court papers he is called only OT — he heads a body that receives public funds, and he challenged the publication requirement rather than complying with it. On the other side was Lithuania's Chief Official Ethics Commission, the body that runs the register. The case travelled from a regional administrative court in Lithuania up to the Court of Justice of the European Union, and on the first of August 2022 the Grand Chamber gave judgment.

{pause: 1.0}

{tone: curious} Nowhere on that form was there a question about anybody's private life. There was no box asking about sexual orientation. There was a field, {pause: 0.4} and the field wanted a name.

{tone: precise} The Court held — and I am paraphrasing the judgment rather than reading it to you — that publishing personal data liable indirectly to disclose a person's sexual orientation is processing of a special category of personal data. Because from the name of a spouse, a cohabitee or a partner, information about the sex life or the sexual orientation of the declarant, and of that partner, may be {pause: 0.5} *deduced*. And a narrow reading — one that covered only data that is sensitive on its face — would undermine how well the protection actually works.

{pause: 1.4}

{tone: pointed} A form that never asked the question, {pause: 0.4} and answered it anyway. {tone: measured}

{pause: 1.2}

## Where we are {tone: neutral, note: "orientation, companionable; a quick map before the climb"}

This is The Collisions, and this is the third episode.

The series takes European instruments that arrived at different times, written by different people about different things, and puts them on the same machine — {pause: 0.4} then asks which rule actually bites, who it binds, and what falls through the seam.

You should be carrying two things from the last two episodes. First, what makes information personal data, and how slippery the answer gets when the thing holding it is a trained model. Second, that touching personal data at all requires a lawful basis, and that the word "necessary" does far more work in that test than it looks like it does.

{tone: warm} Today adds something narrower and much harder. There is a short list of categories that the Regulation does not merely regulate. {pause: 0.5} {tone: pointed} It forbids. {tone: neutral}

{pause: 1.2}

And there is one word sitting inside that prohibition {pause: 0.4} which decides whether the whole thing reaches modern systems or stops short of them.

{tone: wry} We will get to the word. First, the machine. {tone: neutral}

## What a classifier does that nobody asked it to do {tone: lucid, note: "working the mechanism out alongside the listener; plain and unhurried"}

Take a system that decides something about people. Whether to offer someone a policy, flag a claim, shortlist an application. It takes in features about a person and produces a number.

Now suppose the people who built it are careful and well-intentioned. They know the law. So they do the obvious thing: {pause: 0.4} they never collect ethnicity. There is no field for it. It is not in the training data, it is not in the input, nobody typed it anywhere.

{tone: curious} Has the system been kept ignorant of ethnicity? {tone: lucid}

{pause: 1.8}

No. And the reason is ordinary statistics, {pause: 0.3} doing their work whether or not anybody wanted them to.

Ethnicity correlates with other things the system does have. Postcode is the standard example. Where people live is not randomly distributed, and it has not been for a long time, so a postcode carries information about ethnicity {pause: 0.4} whether or not anybody intended that. The same structure shows up everywhere. The timing of certain purchases carries information about pregnancy. The rhythm and cadence of somebody's typing carries information about motor conditions. None of those were designed as proxies. {pause: 0.5} They just are.

{pause: 0.6}

{tone: pointed} Take out the field, {pause: 0.4} and the model reconstructs the field from what is left. {tone: lucid}

{pause: 1.4}

{tone: wry} The field of computer science has a name for the naive fix, and the name is a little unkind: {pause: 0.4} *fairness through unawareness*. {tone: lucid} It comes from a 2012 paper by Cynthia Dwork and four co-authors called "Fairness Through Awareness" — {pause: 0.3} the title is the argument. Being blind to a protected attribute does not make a system fair, because group membership shows up again in everything else you kept.

Solon Barocas and Andrew Selbst named the mechanism at work, in a 2016 article in the California Law Review: {pause: 0.5} **redundant encoding**. Their point sharpens it. Removing the sensitive label does not remove the disadvantage, because the surviving features already carry the disadvantage. The data is a record of how advantage was distributed {pause: 0.3} before anyone built anything.

{pause: 0.6}

And there is a sting in it. You could go hunting proxies and strip them out one by one — {pause: 0.4} but the proxies carry task-relevant information too. Remove enough of them and the model gets worse at the job. There is no free version of the naive fix.

{pause: 1.0}

{tone: contemplative} Name the level we are on. That was a *technical* explanation: features, correlation, encoding. Now push back one step and ask what produced it. Nobody chose the proxy. {pause: 0.6} The proxy is what a society's history looks like {pause: 0.4} when you write it down as a table.

## The trap in the middle {tone: curious, note: "the trap closes slowly; let the listener see each step before it is named"}

{tone: wry} So the system may be acting on a protected attribute it was never given. Fine. You are a responsible organisation. You will check. {tone: curious}

How?

{pause: 1.4}

To find out whether a system treats one group differently from another, somebody has to be able to sort the outcomes by group. That means somebody has to *hold* the group membership. To measure discrimination on the basis of ethnicity, you need people's ethnicity — {pause: 0.4} the thing you carefully did not collect. And, as you'll hear in a moment, {pause: 0.3} the thing the law forbids you to hold.

{pause: 0.8}

{tone: measured} This is the reported working condition of the people whose job it is. In 2021 McKane Andrus and three colleagues published a study at the ACM conference on fairness, accountability and transparency, based on interviews with thirty-eight practitioners working in or next to algorithmic fairness. What they found was that fairness tooling almost invariably requires access to protected attributes, or to proxies for them — {pause: 0.4} and that practitioners routinely do not have that data.

The paper's title says it: {pause: 0.4} "What We Can't Measure, We Can't Understand."

{pause: 1.2}

{tone: lucid} Hold on to the shape of this, because we will come back to it twice more. {pause: 0.4} {tone: pointed} **You cannot decline to disclose what can be predicted. And to prove that a machine is not discriminating, you have to hold the very data you are forbidden to hold.** {tone: curious}

{pause: 1.6}

That is the *organisational* level of the problem — {pause: 0.3} the audit that cannot be run. Keep it. Now the law.

## The sentence that does the work {tone: measured, rate: normal, note: "set the reading up plainly; only the Regulation's own words go in the quoting voice"}

I am going to read you one sentence from Regulation 2016/679, the General Data Protection Regulation. These are the Regulation's words, not mine, and I will tell you where they stop.

{pause: 0.8}

Article 9, paragraph 1. Quote.

> "Processing of personal data revealing racial or ethnic origin, political opinions, religious or philosophical beliefs, or trade union membership, {pause: 0.4} and the processing of genetic data, biometric data for the purpose of uniquely identifying a natural person, data concerning health or data concerning a natural person's sex life or sexual orientation {pause: 0.6} shall be prohibited."

End of quotation.

{pause: 1.4}

{tone: precise}

Eight kinds of thing, {pause: 0.4} and two of them do the work today: what a system can work out about someone's ethnicity, and what it can work out about their health.

I will call that sentence **the prohibition** from now on, and I will not say the number again.

## What the prohibition actually is {tone: precise, note: "definitional and even; structure should read as structure"}

Strip that down to what it does.

It names a closed set of categories. And for everything inside that set, the starting position is: {pause: 0.4} no. Not "be careful". Not "document your reasoning". Prohibited.

{pause: 0.8}

{tone: lucid} That is the misreading to take off the table now, because almost everyone arrives with it. Most people hear "special categories" and translate it as *sensitive information, handle with care* — a flag on a file, a reason for stronger security, a thing you mention in a policy. That is wrong in a way that changes every conclusion you draw afterwards. The default for ordinary personal data is that you may process it if you have a lawful basis. {pause: 0.4} {tone: pointed} The default for these categories is that you may not process them at all, {pause: 0.3} and then a short list of exceptions is carved back in. {tone: precise}

{pause: 1.2}

Two different machines. One says find a reason. The other says the answer is no {pause: 0.3} unless one of a fixed number of doors opens.

{pause: 1.0}

And now the word. {pause: 0.6} **Revealing.**

{pause: 0.8}

The prohibition does not say data *stating* racial or ethnic origin. It does not say data *recording* someone's religion. It says data *revealing* it.

{tone: lucid} That is a wider word, deliberately, and the Grand Chamber said so in the Lithuanian case: {pause: 0.4} data liable indirectly to reveal sensitive information is not excluded from this regime, because reading it narrowly would undermine the protection's effectiveness.

{pause: 0.6}

{tone: contemplative} A name in a field on a form was inside the prohibition. Not because the form asked. {pause: 0.5} Because the answer gave it away.

## Three of the categories come with their own definitions {tone: precise, note: "three definitions, each set against a common assumption; even and deliberate"}

Some of those categories are left to ordinary meaning. Three are not, and the definitions matter more than you would expect.

**Biometric data.** People assume this means any photograph of a face. It does not. The Regulation's definition is data resulting from specific technical processing relating to physical, physiological or behavioural characteristics, {pause: 0.3} which allow or confirm the unique identification of a person. {tone: pointed} Read that as: {pause: 0.3} the processing, not the picture, is what makes it biometric. {tone: precise}

{pause: 1.2}

{tone: lucid} So a photograph of your face in a family album is not biometric data. The identical file, fed into a pipeline that turns it into a template and matches it against others to work out who you are, {pause: 0.4} is. Same pixels. {pause: 0.4} Different legal object, because of what is being done to them and why. {tone: precise}

{pause: 0.6}

**Data concerning health** is broader than people expect in the other direction. The definition covers personal data related to physical or mental health which *reveals* information about a person's health status — {pause: 0.5} and there is that word again. {tone: lucid} Nothing in it requires a doctor, a diagnosis, or a medical record. An inference about somebody's health status, drawn from data that is not medical at all, {pause: 0.4} is pulled inside once it has been drawn and written down. {tone: precise}

And **genetic data**. Not "DNA on file somewhere" — the definition is data giving unique information about a person's physiology or health, resulting in particular from the analysis of a biological sample. Narrower, more technical, and the one that matters least for what follows.

{pause: 0.8}

{tone: lucid} So far we have two things. A prohibition whose trigger word is *revealing*, {pause: 0.4} and a set of categories where at least two of the definitions are about what the data lets you work out, not about where it came from.

## The doors {tone: lucid, note: "four doors opened one at a time from a closed list; let each ordinal land as a signpost"}

The prohibition has exceptions. There are ten of them, they are a closed list, and I am not going to read you ten of anything. I will open four, and then tell you honestly what I have left shut.

{pause: 0.6}

{tone: precise} The first is **explicit consent**. The person agrees to this processing, for specified purposes. That is a higher bar than ordinary consent, which the Regulation already defines as freely given and unambiguous — explicit consent asks for more than that again. {tone: lucid} And the door has a lock on the outside: {pause: 0.4} the same provision says that Union or Member State law may provide that the prohibition cannot be lifted by the data subject at all. In some places, for some processing, {pause: 0.3} you are not permitted to agree.

{pause: 0.8}

The second is the one that matters most for anything trained on the open internet. It covers processing that relates to personal data — and these are the Regulation's words — {pause: 0.4} "manifestly made public by the data subject".

{tone: warm} Take that slowly. It has two joints, and both of them bear weight. {tone: lucid}

{pause: 0.6}

{tone: pointed} *By the data subject.* Not by anybody. Not about them. {pause: 0.3} By them. {tone: lucid}

{pause: 1.4}

If a journalist writes that someone is a member of a party, that person has not made it public. If your cousin posts about your religion, you have not made it public. The door only opens for what the person themselves put out.

And then *manifestly*. Manifestly means somebody could look at that record and see that the person put it there on purpose — {pause: 0.3} obviously, evidently, unmistakably. Anyone building a training corpus by scraping and relying on this door has to be able to say that about every record inside it, {pause: 0.4} category by category, person by person.

{tone: wry} That is the weakest joint in the scraping defence, and it is weak at both ends. {tone: lucid}

{pause: 1.0}

The third door is **substantial public interest**. People hear that as "it's important, and we think it's worth it". It is much more demanding. {pause: 0.3} It requires a *law*. {tone: precise} And that law has to be proportionate to the aim, has to leave the essence of the right to data protection intact, and has to carry suitable and specific safeguards. {tone: lucid} A company deciding for itself that its purpose is substantial {pause: 0.3} does not get through.

{pause: 0.8}

The fourth is the research door — archiving in the public interest, scientific or historical research, statistics. It is frequently misread as a general licence for people building models. It carries the same structure of requirements as the one before it, including a legal basis and specific safeguards, and it is anchored to a further provision about safeguards for research processing.

{pause: 0.8}

Six doors I have not opened. Two of them do most of the work in ordinary life — one for employment and social-security obligations, one for medical care. None of the six is the one an AI developer is looking for.

{pause: 1.0}

One more piece, and it is the one people forget the Regulation contains at all. On genetic data, biometric data and data concerning health, Member States may maintain or introduce {pause: 0.3} *further conditions, including limitations*. National law can make it *harder*. {pause: 0.3} Not easier.

{pause: 0.8}

Twenty-seven.

{pause: 0.8}

{tone: wry} That is how many answers there can be to the same question about the same system, {pause: 0.4} inside a single Regulation that people describe as uniform.

## Why a prohibition, and why on inputs {tone: contemplative, note: "history thought through, not recited; the stakes are real but stay under the surface"}

There was another way to build this, and Europe knew about it.

The other way is a rule about outcomes. Do not discriminate. If your process produces worse results for a protected group and you cannot justify it, you are liable — {pause: 0.3} and the question of what data you held is beside the point. That is broadly the shape anti-discrimination law takes.

Data protection went the other way. It built a prohibition on *holding and using* the categories {pause: 0.3} in the first place.

{pause: 0.6}

And there is a reason, which is worth dating rather than treating as timeless. The harms this list was written against {pause: 0.4} were harms of the file. {tone: somber} Somebody writing down who belonged to which group, {pause: 0.4} and then acting on the list. Europe in the twentieth century did not have to look far for examples. {tone: contemplative}

{pause: 1.2}

If the danger is that the category gets recorded and then used, the intervention that makes sense is to stop the recording. {pause: 0.4} Cut it off at the input.

{pause: 0.6}

{tone: measured} That is the *rights-based* level of the explanation, and this is where this episode stops on it. The categories on that list are protected because of what has been done with them before. What a fundamental right actually is, and how a court tests whether a limit on one is permissible — {pause: 0.3} that is a whole apparatus of its own, and it belongs to a later series in this programme. You do not need it today. Everything in this episode works without it. {tone: contemplative}

{pause: 1.0}

Now the trade. {pause: 0.4} {tone: pointed} An input rule is an excellent answer to a clerk with a ledger. It has very little to say {pause: 0.3} to a system that manufactures the input itself. {tone: contemplative}

{pause: 1.4}

## Working the Lithuanian case {tone: measured, note: "a worked method — issue, instrument, test, counter, answer, conclusion; each label is a signpost, give it a beat"}

Let me do the case properly, as a piece of reasoning, because the moves are half of what is worth learning.

The issue. {pause: 0.4} A statute requires a form, the form requires the name of a spouse, cohabitee or partner, and the form gets published. Is publishing it processing of a special category?

{pause: 1.4}

The instrument. {pause: 0.4} The prohibition, and specifically its trigger word: *revealing*.

The test. {pause: 0.4} {tone: precise} Does this data reveal one of the listed categories — {pause: 0.3} and does "revealing" reach data that reveals only indirectly? {tone: measured}

{pause: 1.4}

{tone: curious} Now the counter-argument, and it is not a silly one. A name is a name. It states nothing whatsoever about anyone's sexual orientation. On its face the field contains a string of letters and nothing else. Read the prohibition as covering data that is sensitive in itself, and a name falls outside it. That reading is textually available, and if you were arguing for the Chief Official Ethics Commission {pause: 0.3} you would make it. {tone: measured}

{pause: 0.8}

The Court's answer, paraphrased. {pause: 0.4} {tone: precise} From the name of a spouse, cohabitee or partner, information about the sex life or sexual orientation of the declarant and of that partner may be deduced. Data liable indirectly to disclose such information is not excluded from the regime. And the narrow reading would undermine the effectiveness of the protection, which is a reason to reject it. {tone: measured}

Conclusion: {pause: 0.3} publishing those declarations was processing of special-category data, so the prohibition applied and a door had to be found.

{pause: 1.2}

Now the limit, because you should not leave with a wider rule than the one that exists.

That judgment is about **publication**. It is about a disclosure that puts information in front of ordinary readers who then draw an ordinary inference. It moved the boundary from *stating* {pause: 0.3} to *revealing*.

{pause: 0.6}

{tone: pointed} It is not a holding that a statistical prediction of a protected attribute {pause: 0.3} is processing of special-category data. {tone: measured}

{pause: 1.2}

No decision I have been able to find has said that — and I will come back to how sure I can be about that. The gap between revealing and predicting {pause: 0.4} is exactly where this episode lives, and I need it to stay audible.

## Change one fact {tone: curious, note: "a variation game; alter one thing and watch the classification move"}

So let us change facts and watch the classification move.

**First.** Take the model from earlier. Never given ethnicity. And it predicts ethnicity correctly four times in five — {pause: 0.4} not because anyone asked it to.

Is the system processing special-category data?

{pause: 1.8}

{tone: warm} I do not know, and neither does anybody else with authority to say. That is the honest state of the question. {tone: lucid} The instrument's word is *revealing*, and its whole apparatus assumes data that exists {pause: 0.3} and can be pointed at. A capacity to produce the category on demand {pause: 0.3} is a different object. {tone: curious}

{pause: 1.0}

Genuinely unresolved.

{pause: 1.0}

**Second.** Change the source. Now the training data was scraped from public profiles where people stated their own religion, in their own words, on their own pages.

The manifest-publication door is at least in play — {pause: 0.4} and everything now rests on two words. Was it *manifestly* public, for each record? And was it public by the data subject, rather than about them? The people who posted their own religion may clear it. {pause: 0.3} The people they mentioned do not. {tone: wry} One corpus, and the door opens for some rows and not others, which is not a state most systems are built to be in. {tone: curious}

{pause: 1.0}

**Third.** Change the use. The output is not research now — {pause: 0.3} it goes into deciding whether someone gets credit.

{tone: measured} A second rule bites at that point, and it is a different rule from this one. It is about what may be *decided* automatically, and about decisions taken on the basis of these categories. That is a whole apparatus with a Grand Chamber judgment behind it, and it is not this episode's.

## The collision {tone: measured, note: "the sharpest collision in the series; dated and exact, the force carried by precision rather than volume"}

{tone: lucid} Take stock before the hardest part. We have a prohibition, not a caution; {pause: 0.3} we have the word *revealing*, which reaches data that gives the category away rather than states it; {pause: 0.3} and we have a machine that can produce the category from material nobody thought to protect, while nobody can check whether it does so without holding that category themselves. {tone: measured}

{pause: 1.0}

{tone: warm} Now two instruments meet on the same machine, and this is the sharpest collision in the series. {tone: measured}

{tone: precise} Everything in this beat carries a date, because most of it is still moving. {tone: measured}

{pause: 0.6}

The AI Act has always had a provision permitting the processing of special categories specifically to detect and correct bias. Series A taught that provision. {pause: 0.5} It no longer exists.

{pause: 0.8}

In July 2026 the AI Act was amended. The amendment came out of the Digital Omnibus — the European Commission's package reopening the digital rulebook, {pause: 0.3} law rewriting law it had just written.

{pause: 1.0}

It deleted that provision and put a new, freestanding one in its place. {tone: precise} Article 4a, in force since the end of July 2026. I will call it **the bias-detection permission**, and that is the last time I will say its number. {tone: measured}

{pause: 0.6}

And the replacement is {pause: 0.3} *broader* than what it replaced. The old provision reached providers — the parties that build systems and put them on the market — and only in relation to high-risk systems, the AI Act's tier for things it treats as carrying serious risk to people. The new one reaches deployers, {pause: 0.3} the parties that merely use a system. And it reaches providers and deployers of systems and models {pause: 0.3} that are not high-risk at all.

{pause: 1.0}

{tone: precise} Three phrases in that text, and I will bracket each as the Regulation's own.

The first is three words. Quote, "may exceptionally process", end quote. The drafters wrote the exception's character into the verb. {pause: 0.4} Exceptionally.

{pause: 0.8}

{tone: lucid} The second is a condition, and it is our trap written into law. Remember the trap: {pause: 0.3} you cannot decline to disclose what a machine can predict, and to prove the machine is not discriminating you must hold the very data you are forbidden to hold. Here is the second half of that, {pause: 0.4} legislated. The forbidden data may be held only where the bias detection and correction, quote, {pause: 0.3} "cannot be effectively fulfilled by processing other data, including synthetic or anonymised data", end quote. In plain terms: {pause: 0.3} you may hold it only if the job genuinely cannot be done without it. {pause: 0.6} The interview study we heard earlier is the evidence about whether it can.

{pause: 0.8}

{tone: precise} The third is the important one for the seam. The bias-detection permission says its conditions apply, quote, "in addition to", end quote, the provisions of the data protection Regulation, {pause: 0.3} which reads as not displacing them. {tone: measured}

{pause: 1.4}

{tone: curious} So consider the deployer of an ordinary, non-high-risk system in September 2026. {tone: measured}

{pause: 0.6}

One Regulation, in force, tells that deployer it may exceptionally process special categories to check its system for bias. {pause: 0.6} {tone: pointed} The Regulation that actually governs that processing says such processing shall be prohibited — {pause: 0.4} with a closed list of doors, and this is not one of them. {tone: measured}

{pause: 1.4}

Nothing on the Regulation's own list is a bias-detection door. Whether a permission written into a different instrument can act as one {pause: 0.3} is the part nobody has answered.

{pause: 0.8}

{tone: precise} The amendment that would make the two agree has not passed. The data protection half of the Omnibus was split from the AI half and is still in negotiation {pause: 0.3} as at the week this was recorded. The prohibition is unamended. A proposed new route for AI development, and a proposed exemption for residual special-category data that ends up in a training set, {pause: 0.3} are proposals and nothing more. {tone: measured}

{pause: 0.8}

And the European Data Protection Board and the European Data Protection Supervisor, in two joint opinions issued in February 2026, objected to precisely this widening — {pause: 0.3} that it now extends past high-risk systems to all systems and models, and to deployers. They recalled that processing special categories is in principle prohibited, and that exceptions must stay narrow.

{tone: precise} The easy version of what happened next is wrong, so here is the exact one. The strict-necessity standard the authorities pressed for did survive into the adopted text; the words "strictly necessary" are in both paragraphs. So the objection was not simply ignored. {pause: 0.4} What happened is that the instrument was widened {pause: 0.3} over the stated objection of both those regulators. {tone: measured}

{pause: 1.0}

And that open question — whether a permission written into one instrument can act as a door in another — {pause: 0.3} is unsettled rather than contested. There are not two camps I could name for you. There is nobody with authority who has answered it, {pause: 0.3} as at the twentieth of September 2026.

{pause: 0.8}

{tone: contemplative} That is the *institutional* level. Two instruments legislating about the same prohibition from opposite directions, {pause: 0.3} three months apart, and neither one resolving the other.

## The sentence I keep coming back to {tone: contemplative, note: "institutional honesty, quietly noticed; no alarm, the sentence is plain and so is the reaction"}

There is one more line in the bias-detection permission, and it is the last sentence of its second paragraph. It is one sentence of institutional honesty. Hear it exactly as it is written.

{pause: 0.6}

Quote.

> "This paragraph does not create any obligation to conduct such bias detection and correction."

End of quotation.

{pause: 1.4}

{tone: pointed} A permission to look. {pause: 0.5} And no duty to look. {tone: contemplative}

{pause: 1.4}

{tone: lucid} Now the *economic* level, which that sentence states more plainly than I could. Checking for bias means obtaining and holding data that is prohibited by default. Holding it puts you in front of your regulator. And nobody is obliged to hold it at all. So the cheapest compliant posture available to any organisation is to know nothing — {pause: 0.5} and to be able to prove it knew nothing. {tone: contemplative}

{pause: 1.0}

The structure pays for that. {pause: 0.4} Nobody's ethics had to fail.

## What the prohibition assumes about the machine {tone: precise, note: "said as flatly as promised; even and deliberate, the weight saved for the third statement of the trap"}

This is why this series exists, so let me say it as flatly as I can.

The prohibition assumes that sensitivity is a property of **data**. It assumes a controller — the organisation that decides what happens to the data — can look at a field, know whether that field is inside the list, and decide accordingly. And it assumes, this is the load-bearing one, {pause: 0.4} that declining to collect is a way of declining to process. That not asking is a way of not knowing.

{pause: 1.0}

For a clerk with a ledger, every one of those assumptions holds.

{pause: 0.6}

{tone: lucid} For a model, the first one buckles {pause: 0.3} and the third one collapses. A model makes sensitivity a property of {pause: 0.4} **inference**. The category is not in the file; {pause: 0.3} the category is a thing the system can produce, at any time, from material nobody thought to protect.

{pause: 1.0}

And if you are carrying the word *inference* from the earlier series — the machine producing a fact about a person that nobody handed it — then hear this. {pause: 0.4} *Revealing* is that same event, named from the other side. One word belongs to the engineers. The other belongs to the Regulation. They describe one thing, and a listener who holds them apart will miss {pause: 0.3} that the law is already halfway to the machine. {tone: precise}

{pause: 1.0}

So, for the third and last time, the claim of this episode: {pause: 0.6} {tone: pointed} you cannot decline to disclose what can be predicted. And to demonstrate that your machine is not discriminating, {pause: 0.3} you must hold the data you are forbidden to hold. {tone: precise}

{pause: 1.6}

{tone: contemplative} Two halves of one trap, and the instrument that built the trap and the instrument that noticed it {pause: 0.3} are different instruments.

## As written, as enforced {tone: measured, note: "a plain account of the record, and an honest one about where it runs out"}

As written, this prohibition is among the strongest things in the Regulation. Breaches of it sit in the Regulation's higher penalty tier — {pause: 0.3} that much is on the face of the text — and authorities have used it.

My impression of what has actually been enforced under it, offered as an impression rather than as a count I can give you, {pause: 0.3} is that it has mostly concerned data that was sensitive when it arrived. Obviously and undeniably inside the list from the start.

{pause: 0.8}

{tone: warm} The inference case is different, and here I have to give you an absence rather than a finding. {tone: measured}

{pause: 0.6}

{tone: precise} This programme searched on the twentieth of September 2026 and did not find any decision, anywhere, holding that predicting a protected attribute is itself processing of special-category data. {pause: 0.6} I am not telling you none exists. I am telling you that none was found, and giving you the date {pause: 0.3} so you can check whether that is still true when you hear this. {tone: measured}

{pause: 1.0}

{tone: wry} An absence with a date on it is the honest version of "nobody has run this yet".

## Where I come down {tone: contemplative, note: "a judgment of my own, owned and plain; thought through aloud, not pronounced"}

A judgment of my own, marked as mine, and it is local rather than the verdict this series is building toward.

{pause: 0.6}

I do not think an input-based prohibition can reach an inference {pause: 0.3} without somebody reinterpreting it. The word *revealing* is a genuinely wide word, and the Grand Chamber stretched it from stating to disclosing-indirectly. But every stretch so far has been applied to data that existed and was handed over. Getting from there to a machine that manufactures the category on request {pause: 0.4} is a different reading of what processing even is.

{pause: 1.0}

Somebody may do it. A court that took the effectiveness argument seriously enough could get there, and the effectiveness argument is already in the case law. {pause: 0.6} {tone: pointed} Until then, the most protective prohibition in the Regulation is pointed at the one place {pause: 0.4} the modern problem is not. {tone: contemplative}

{pause: 1.4}

## What you now ask {tone: precise, note: "the closing question-set; even and deliberate, and the silence after each question is the listener's turn"}

You will meet a system soon enough. Here are the questions this apparatus has just taught you to put to it — {pause: 0.3} and they work whether or not anybody involved has heard of the Regulation.

{pause: 0.8}

Which of the protected categories could this system predict, {pause: 0.3} whether or not anyone asked it to?

{pause: 1.8}

When someone tells you no sensitive data is processed here — {pause: 0.3} is that a claim about the inputs, or about the outputs? {pause: 1.6} Those are different claims, and only one of them is usually being made.

{pause: 1.2}

If somebody wanted to audit this thing for bias, what exactly would they have to be allowed to hold? {pause: 1.6} And has anyone actually asked that question out loud?

{pause: 1.6}

And when a permission appears — {pause: 0.3} which instrument is supplying it, and does that instrument own the prohibition it is carving into?

{pause: 2.0}

That last one is the general lesson of today. {pause: 0.4} {tone: pointed} A permission granted by one instrument over a prohibition owned by another {pause: 0.4} is not a permission. It is a disagreement, and somebody will eventually have to resolve it. {tone: precise}

{pause: 1.4}

{tone: curious} So the machine can work out the category. Which leaves one more question, and it is the obvious one.

{pause: 0.6}

Is it allowed to *decide* anything with it?

{pause: 1.6}

There is a single article about that. It runs to four short paragraphs, and it has one Grand Chamber judgment standing behind it — {pause: 0.4} about a man who was refused a loan, {pause: 0.3} and who sued the company that did not make the decision.

{pause: 0.8}

{tone: warm} Next time.