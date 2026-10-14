# Editor's notes on episode 1 — marked ready

The last verdict (edit.r2). A final writer pass applied them on 2026-10-09 (replayed through the new ready-verdict pass, then the tone pass re-run), and **nobody reviewed that pass** — check them against `transcript.md`.

BLOCKING

None. I checked every case name, date, figure and quotation against dockets 01–03 and none is wrong. A listener can follow and apply the test, and none of this persona's hard rules is broken.

IMPROVEMENTS

1. Method narration, an echo of the prompt (in "What the network already knows"). Quote: "Before reasoning about rules for any system, I ask whether the system exists as described. This one plainly does." This belongs to the family of the banned "before any rule touches": the narrator is reciting its instructions. Cut both sentences. The next line ("The directive laid a legal duty on records the operators already held") already does the work.

2. The strongest case for the directive can be held by a named body, and the docket names one ("The other side, at its best"). Quote: "Now the strongest case for the directive, in the best form I can give it. The framing is mine." Docket 03 [43] records the Justice and Home Affairs Council of 19 December 2002. It concluded that these data are "particularly important and therefore a valuable tool in the prevention of offences and the fight against crime". Open on that, with audible brackets, then extend it in the narrator's voice ("Put at its strongest, in my words: next year's suspect is, today, an ordinary subscriber..."). This meets the persona's "who holds it".

3. Quote: "No regulator could test the law itself against the Charter. Only a court could." The plan says "No regulator does". "Could" will clash with Episode 2: Schrems I (docket 02 §4) teaches that supervisory authorities must be able to examine such a complaint and get it to the Court. Replace with: "No regulator tested the law against the Charter. People who could sue brought it to a court."

4. A contradiction the listener may hear (docket 03 §2, compiler's note). The essence of data protection survives because the directive "at least imposed certain principles of data security" ([40]). Defect four then finds that same security too weak ([66]–[67]). Add one clause at the end of defect four, for example: "These are the same security rules that kept the core of data protection intact. The gate asks whether any protection exists. The test of need asks whether it is enough." This is optional, but it closes a "wait, what?" moment.

5. Quote: "That will matter before the end." This is a debt of about 25 minutes. The payoff ("Remember the challengers, who had a law and had read it") already supplies its own reminder, so the early promise only adds load. Cut it.

6. Quote: "Two misreadings need refusing early, because a technically trained ear reaches for them." This presumes too much about the listener. Use "...because both are tempting."

7. "Why one clause" is accurate, but the trade it describes is slightly too clean for Article 7 specifically. The Explanation to Art. 7 says its limitations "are the same as those allowed by Article 8 of the ECHR". Consider: "...one of which ties certain Charter rights, private life among them, to the Convention's standards. You can set that aside." It stays one clause, and the flexibility claim is no longer heard as covering Art. 7 without exception.

8. Length: 5,413 spoken words, about 42 minutes against 40. That is fine as a guide and the material justifies it. Do not cut to hit the number.

9. For the human, a lint artefact rather than a script defect. The `no-breath` warning quotes the WRITER NOTES comment. scriptlint.py:266 measures the raw transcript without stripping `<!-- -->`, unlike lines 113 and 356, so the comment's 500 words were counted as a stretch with no pause. compile.py:33 strips comments, so nothing in the notes is spoken. In the spoken text, every beat has a heading, a pause or a question well inside 450 words. The fix is one `re.sub` at line 266.

10. Tone: no `dramatic` is set. The plan earns it for the directive "treated as never having been valid". Leave it to the tone pass, at "The answer was that, as a matter of Union law, it never had been."

CLEARED

- Source fidelity. Checked: the 11 August 2006 action and the June registration ([17]); Seitlinger, Tschohl, 11,128 others and Carinthia ([3], [19]); both references in 2012 (docket 03 header); March 2006 (the operative part); six to twenty-four months ([64]); "practically the entire European population" ([56]); the Portuguese government ([50]); six examples in [27]; [27] and [39] twelve paragraphs apart, with no excerpted paragraph missing between them.
- Verbatim quotations, checked word for word: [20], Art. 7, Art. 8(1), [33], [37], both sentences of Art. 52(1) (the truncation is declared), [48], [52], [57], the "economic considerations" phrase from [67], "is invalid", the press release on temporal effect, and [27]. Judgment wording is used throughout where docket 03 §1 lists a difference from the press release.
- Attribution:
  - the temporal effect goes to the press release, with the judgment "silent" and "sets no limit", never "declined";
  - the constant-surveillance line goes to the Court, following its Advocate General;
  - "map of a life" is marked as the narrator's;
  - the content-line tension is marked as the series' reading;
  - "the weighing never gets a paragraph of its own" matches docket 03 §3.
- The essence: each right gets its own reason ([39] content, [40] data security), as the plan required.
- Apparatus fidelity: the two gates, the four questions (each named as the Court reaches it), the scrutiny dial ([47]–[48]) and the test's two limbs ([46]). The loss on necessity and not on balancing lands four times. The four defects come in the Court's order, in two pairs, and are turned into a design brief that recurs four times, including at the held verdict.
- All ten load-bearing terms are earned, each with its misreading named and corrected.
- Machine beat: the core of private life is drawn by kind of data, while the Court's own [27] says the records map a life. A second assumption, that the test reads design and not use, is paid off against the challengers. Both are present and real.
- Levels: economic, then rights, then organisational (the state ordering firms that already hold the records). It terminates: "One step back is enough."
- Boundary: changing one fact flips defects one and two, and the content variant flips the category to failing at the gate. The dial also flips with seriousness. The content variant is unnumbered, makes no prediction and has no pointer.
- Settled, contested and still moving are all distinguished. "Asked again" carries no date, as the plan asks.
- Comprehension:
  - three rejoin points tested ("Now the four questions", "The first pair is about who gets caught", "This one carries two") all signpost;
  - two mid-episode recaps;
  - three retrieval questions, each followed by a 2.5-second pause;
  - forward references within budget (Episode 9, the deferral to other series, the handover), none in the first five minutes, the deferral framed as permission to forget;
  - no spoken run of more than three items (the field definitions are chunked into three sentences);
  - every quotation is followed by a plain restatement, each worded differently.
- Hard rules:
  - no spatial deixis;
  - no banned phrase;
  - no spoken bibliography;
  - no case or instrument numbers spoken;
  - "however" absent;
  - the other European rights court is not mentioned and the Court is not said to have reasoned alone;
  - only one numbered pointer (Episode 9);
  - the series is named and no person;
  - the cold open is on a dated, named instance, and the episode ends on transfer questions and the handover, not a summary.
