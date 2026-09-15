import re

import pytest

from prosodia.author.persona import Persona
from prosodia.author.tone import VoiceProfiles


def test_default_resolves_to_hardcore_history():
    p = Persona.resolve()
    assert p.name == "hardcore-history"
    assert "Hardcore History" in p.role("writer")  # the migrated dramatist prompt


def test_available_lists_both_builtins():
    names = Persona.available()
    assert "hardcore-history" in names and "thinkers" in names


def test_thinkers_persona_is_a_carlin_sandel_amalgam():
    p = Persona.resolve("thinkers")
    assert p.name == "thinkers"
    assert p.defaults.target_minutes == 40
    writer = p.role("writer")
    assert "Sandel" in writer and "Carlin" in writer  # the two pillars
    assert "steelman" in writer.lower()  # Sandel's argue-both-sides, done honestly
    editor = p.role("editor")
    assert "Idea fidelity" in editor  # the persona-specific quality bar


def test_thinkers_persona_is_generalized_not_a_fixed_thesis():
    # The organizing thesis belongs to the series, not the persona (design principle).
    planner = Persona.resolve("thinkers").role("planner")
    assert "crisis breeds" not in planner.lower()  # the forced thesis was removed
    assert "through-line" in planner.lower()  # planner finds/consumes the frame instead


def test_personas_have_distinct_tone_vocabularies():
    hh = VoiceProfiles.load(Persona.resolve("hardcore-history").voice_profiles_path())
    th = VoiceProfiles.load(Persona.resolve("thinkers").voice_profiles_path())
    # the thinkers persona adds an exposition register the dramatist lacks
    assert {"curious", "lucid", "contemplative"} <= th.known_tones()
    assert "curious" not in hh.known_tones()


def test_unknown_persona_raises_and_lists_available():
    with pytest.raises(FileNotFoundError) as exc:
        Persona.resolve("no-such-persona")
    assert "thinkers" in str(exc.value)  # the error lists what IS available


def test_project_local_persona_overrides_builtin(tmp_path):
    proj = tmp_path / "proj"
    (proj / "personas" / "thinkers" / "roles").mkdir(parents=True)
    (proj / "personas" / "thinkers" / "roles" / "writer.md").write_text("LOCAL WRITER", encoding="utf-8")
    (proj / "personas" / "thinkers" / "persona.yaml").write_text(
        "name: thinkers\ndescription: a project-local override\n", encoding="utf-8"
    )
    p = Persona.resolve("thinkers", project=proj)
    assert p.role("writer") == "LOCAL WRITER"  # project-local wins over the built-in
    assert "thinkers" in Persona.available(project=proj)  # not duplicated

def test_casework_persona_resolves_with_its_defaults():
    p = Persona.resolve("casework")
    assert p.name == "casework" and p.title == "Casework"
    # A SOFT anchor, not a cap. Was 27 — one craft source's measured unit, borrowed without
    # the syllabus and readings that surrounded it, for a series specified as standalone.
    # Two independent runs of Ep 1 landed at 34 minutes with the depth judged earned.
    assert p.defaults.target_minutes == 35
    assert p.defaults.host_mode == "single"
    for role in ("planner", "writer", "editor", "tone"):
        assert p.has_role(role), role


def test_casework_keeps_the_move_other_personas_ban():
    """`in other words` is filler in a narrative persona and a load-bearing device here.

    It is the plain-language restatement after a technical formulation — the most frequent
    sentence opener in the corpus this persona's architecture came from. Banning it would
    import another persona's watchlist, which the sourcing process explicitly forbids.
    """
    p = Persona.resolve("casework")
    assert "in other words" not in [w.lower() for w in p.defaults.freshness_watchlist]
    assert "restate it once in plain words" in p.role("writer")
    # what IS banned is filler and anything that lies to a listener with no picture
    banned = [w.lower() for w in p.defaults.freshness_watchlist]
    assert "however" in banned and "as you can see" in banned


def test_casework_writer_carries_its_signature_beat():
    writer = Persona.resolve("casework").role("writer")
    # the beat the persona exists for: the norm against what the system actually does
    assert "What the rule assumes about the machine" in writer
    assert "Change one fact" in writer          # the boundary made audible
    assert "No spatial deixis" in writer        # audio has no picture to point at
    assert "Never simplify the substance" in writer


def test_casework_keeps_dramatic_on_a_leash():
    """`dramatic` is available but constrained in both prompts that can reach for it.

    An unknown tone only warns at compile time, so the table is not the place to enforce
    restraint — the prompts are. Guard that both of them carry the constraint, since a tone
    word offered without a limit is the fastest route to an apparatus narrated like an opera.
    """
    p = Persona.resolve("casework")
    v = VoiceProfiles.load(p.voice_profiles_path())
    assert "dramatic" in v.known_tones()
    assert {"quoting", "pointed", "precise"} <= v.known_tones()
    # pitched below the dramatist personas: even at its peak this show is explaining something
    hh = VoiceProfiles.load(Persona.resolve("hardcore-history").voice_profiles_path())
    mine, _ = v.params_for_tone("dramatic")
    theirs, _ = hh.params_for_tone("dramatic")
    assert mine["exaggeration"] < theirs["exaggeration"]
    for role in ("writer", "tone"):
        text = p.role(role).lower()
        assert "dramatic" in text and ("rarest" in text or "never for the machinery" in text), role


def test_casework_is_generalised_not_a_fixed_topic():
    """Personas define voice and method; the organising thesis belongs to the series."""
    planner = Persona.resolve("casework").role("planner")
    assert "DO NOT IMPOSE A THESIS" in planner
    assert "technical social science" in planner.lower()


@pytest.mark.parametrize("name", ["casework", "thinkers", "hardcore-history"])
def test_tone_words_named_in_prompts_exist_in_the_table(name):
    """A tone word a prompt offers but the table lacks silently falls back to the default.

    That is a delivery bug the compiler only warns about, so guard it here: every word in the
    role prompt's explicit tone vocabulary must resolve in that persona's own table.
    """
    p = Persona.resolve(name)
    known = VoiceProfiles.load(p.voice_profiles_path()).known_tones()
    for role in ("writer", "tone"):
        if not p.has_role(role):
            continue
        text = p.role(role)
        m = re.search(r"(?:Tone words|TONE VOCABULARY)[^:]*:\s*(.+?)(?:\.\s|\n\n|RATE)", text, re.DOTALL | re.IGNORECASE)
        if not m:
            continue
        words = {w.strip().strip("`.").lower() for w in re.split(r"[,\n]", m.group(1))}
        words = {w for w in words if re.fullmatch(r"[a-z][a-z-]+", w or "")}
        # drop prose that survives the split
        words -= {"use", "only", "these", "they", "map", "to", "tuned", "engine", "settings",
                  "anything", "else", "falls", "back", "the", "default", "and", "or", "a", "an",
                  "is", "for", "of", "in", "at", "with", "that", "words", "engine-neutral", "rate"}
        missing = sorted(w for w in words if w not in known)
        assert not missing, f"{name}/{role} offers tones absent from its table: {missing}"

def test_casework_planner_mandates_a_parseable_episode_heading():
    """The planner's output format must be one `planparse` can actually extract.

    `extract_episode_section` locates an episode only by a heading carrying its number. An
    outline shaped as a table or a flat bullet list returns None, and the writer then falls
    back to the coarse brief — losing the instance, the cast, the operative text and the
    variants, with no error anywhere. Tie the prompt's mandated form to the parser so neither
    can drift away from the other.
    """
    from prosodia.author.planparse import _heading_episode, extract_episode_section

    planner = Persona.resolve("casework").role("planner")
    assert "## Episode 3 — Title" in planner, "planner must mandate a concrete heading form"
    # the exact form the prompt demands is one the parser recognises
    assert _heading_episode("## Episode 3 — Title") == 3
    outline = "# Outline\n\n## Episode 1 — What counts as a system\nOpening instance: ...\n"
    assert extract_episode_section(outline, 1) is not None


def test_casework_planner_requires_a_coverage_map():
    """Goal #4 (no gaps, no overlap) is the planner's job, and the CLI prompt asks for it."""
    planner = Persona.resolve("casework").role("planner")
    assert "COVERAGE MAP" in planner.upper()
    assert "exactly one episode" in planner
    assert "reserved" in planner  # material held for a later series is named, not silently dropped


def test_casework_planner_forces_docket_traceability():
    """The planner must mark what it supplies from memory, not launder it as sourced.

    The first generated plan carried ~49 article numbers and ~15 citations that appear in no
    file in `research/`, and one episode told the writer every quotation came from the docket
    while the docket held no text of the articles quoted. A writer told a thing is sourced does
    not check it, so the marker has to be the planner's obligation.
    """
    planner = Persona.resolve("casework").role("planner")
    assert "[OUTSIDE DOCKET:" in planner
    assert "Never describe" in planner and 'your own recollection as material "from the docket"' in planner
    assert "do\n  not use" in planner or "do not use" in planner  # docket vetoes are binding


def test_casework_planner_budget_matches_the_writers():
    """The planner plans a verification budget the writer actually has.

    A plan that hands over nine items marked 'verify' against a one-check budget is an
    invitation to invent. Both halves of that contract live in prompts, so tie them together.
    """
    p = Persona.resolve("casework")
    assert "ONE fact-check per episode" in p.role("planner")
    assert "one fact-check" in p.role("writer").lower()


def test_casework_planner_will_not_defer_the_verdict_to_the_writer():
    planner = Persona.resolve("casework").role("planner")
    assert '"The\nwriter picks one" is not a plan' in planner
    assert "decision procedure" in planner  # the honest alternative when the material won't bear one


def test_casework_write_brief_carries_the_research_docket(tmp_path, monkeypatch):
    """The editor's anti-fabrication rule needs a corpus; the brief is how it gets one."""
    import inspect

    from prosodia.author import cli

    src = inspect.getsource(cli._cmd_write)
    assert 'proj / "research"' in src, "the write brief must read the docket"
    assert "RESEARCH DOCKET" in src


def test_casework_handles_lens_episodes_in_every_role_that_sees_one():
    """A lens episode has no instance, no operative text and no single-fact flip.

    The planner defines the type and expects one episode in four to be one; for a while
    the word appeared in no other prompt. The writer had a single spine whose every beat a
    lens episode lacks, and the editor hard-failed exactly those absences — so a quarter of
    the series would either fake an instance or fail every round and ship unreviewed.
    """
    p = Persona.resolve("casework")
    assert "LENS SPINE" in p.role("writer")
    assert "Open on the disagreement, not on a case" in p.role("writer")
    editor = p.role("editor")
    assert "Episode type:" in editor and "LENS" in editor
    # the editor must be told which checks to suspend, not merely that lenses exist
    assert "must NOT be run against it" in editor


def test_write_brief_declares_the_episode_type_and_series_rules(tmp_path):
    """Both are computed in the CLI, so guard the prompt the writer actually receives."""
    import argparse
    from unittest.mock import patch

    from prosodia.author import cli

    proj = tmp_path / "proj"
    (proj / "plan").mkdir(parents=True)
    (proj / "series.yaml").write_text(
        "series: S\npersona: casework\ntarget_minutes: 27\n", encoding="utf-8"
    )
    (proj / "plan" / "outline.md").write_text(
        "# Outline\n\n## Voice and variation\n\n**Off-limits:** SENTINEL_RULE\n\n"
        "## Episode 2 — [LENS] The Pacing Problem\n\n**Length:** 24 min\n\nSENTINEL_PLAN\n",
        encoding="utf-8",
    )
    seen = {}

    def spy(brief, **kw):
        seen["brief"] = brief
        raise SystemExit

    args = argparse.Namespace(project=str(proj), episode=2, persona=None,
                              prior_episodes=0, max_rounds=1)
    with patch("prosodia.author.orchestrate.author_episode", side_effect=spy):
        try:
            cli._cmd_write(args)
        except SystemExit:
            pass
    brief = seen["brief"]
    assert "Episode type: LENS" in brief
    assert "Follow the LENS SPINE" in brief
    assert "SENTINEL_RULE" in brief          # series-wide rules reach the writer
    assert "SENTINEL_PLAN" in brief          # and so does the episode's own plan
    # the planner's length wins over the series default, and is the number stated
    assert "about 24 minutes" in brief


def test_casework_planner_forbids_covering_the_apparatus_by_range():
    """A range in a coverage map is the appearance of a decision, not a decision.

    The first ai_act plan assigned 77 of 110 articles only inside ranges like "Arts. 74-87",
    reported itself complete, and thereby "covered" six articles inserted by the governing
    amendment that appear nowhere in its 854 lines — one of which reversed what the plan
    taught about who may fine whom.
    """
    planner = Persona.resolve("casework").role("planner")
    assert "NEVER ASSIGN BY A BARE RANGE" in planner
    assert "name what is in it" in planner


def test_compile_finds_the_project_persona_without_an_explicit_config(tmp_path):
    """`compile` with no --config used to resolve the LIBRARY DEFAULT persona.

    That silently applied another persona's tone table: this persona's own registers
    (`quoting`, `pointed`, `precise`) fall back to `measured` with a warning each, and the
    nine shared tone names are re-tuned to different numbers with no warning at all —
    including `dramatic`, which persona.yaml documents as deliberately pitched below the
    dramatist personas. Invisible in the transcript, audible in the render.
    """
    from prosodia.author.cli import _discover_series

    proj = tmp_path / "proj"
    (proj / "episodes" / "ep01").mkdir(parents=True)
    (proj / "series.yaml").write_text("series: S\npersona: casework\n", encoding="utf-8")
    t = proj / "episodes" / "ep01" / "transcript.md"
    t.write_text("---\nepisode: 1\n---\n\n## Beat\n\nHello.\n", encoding="utf-8")

    found = _discover_series(t)
    assert found == proj / "series.yaml"
    cfg = __import__("yaml").safe_load(found.read_text(encoding="utf-8"))
    assert Persona.resolve(cfg.get("persona"), project=found.parent).name == "casework"
    # and a transcript outside any project still resolves to nothing rather than guessing
    loose = tmp_path / "loose.md"
    loose.write_text("x", encoding="utf-8")
    assert _discover_series(loose) is None


def test_writer_is_given_a_word_budget_not_only_minutes():
    """Episode 1 came back at 5,300 words — 41 minutes — against a 27-minute brief.

    An LLM cannot hear its own pace, so a target expressed only in minutes is not a
    constraint it can act on. The persona's speaking rate is the conversion.
    """
    writer = Persona.resolve("casework").role("writer")
    assert "130 words a minute" in writer or "130 words per minute" in writer
    assert "3,500 words" in writer
    # and the conversion must not have become a ceiling
    assert "never exceed" not in writer.lower()


def test_write_brief_states_the_word_budget(tmp_path):
    import argparse
    from unittest.mock import patch

    from prosodia.author import cli

    proj = tmp_path / "p"
    (proj / "plan").mkdir(parents=True)
    (proj / "series.yaml").write_text("series: S\npersona: casework\n", encoding="utf-8")
    (proj / "plan" / "outline.md").write_text(
        "# O\n\n## Episode 1 — A\n\n**Length:** 27 min\n\nbody\n", encoding="utf-8")
    seen = {}

    def spy(brief, **kw):
        seen["b"] = brief
        raise SystemExit

    args = argparse.Namespace(project=str(proj), episode=1, persona=None,
                              prior_episodes=0, max_rounds=1)
    with patch("prosodia.author.orchestrate.author_episode", side_effect=spy):
        try:
            cli._cmd_write(args)
        except SystemExit:
            pass
    assert "3500 spoken words" in seen["b"]
    # a guide, not a cap: the writer must be able to exceed it and say so
    assert "GUIDE, not a cap" in seen["b"]
    assert "never cut\nteaching to hit a number" in seen["b"] or "never cut teaching" in seen["b"]


def test_editor_ready_has_a_severity_bar():
    """Without one, a demanding editor never returns ready and the loop always exhausts.

    Episode 1 ran four rounds and was never marked ready, while source fidelity had gone
    clean by round 4 and the remaining findings were improvements. The cost is not just
    wasted rounds: the last verdict is never acted on, so its notes describe defects still
    in the shipped draft.
    """
    editor = Persona.resolve("casework").role("editor")
    assert "BLOCKING" in editor and "IMPROVEMENTS" in editor
    assert "`ready` is true when, and only when, the `BLOCKING` section is empty" in editor
    assert "Do not block on a sentence you would have written differently" in editor


def test_unresolved_editor_notes_are_written_beside_the_transcript(tmp_path):
    """run/ is gitignored, so an unresolved verdict would otherwise be invisible.

    Exercised for real rather than grepped for: the first version of this code read
    `run.root`, which does not exist, and a source-substring test passed while every
    `prosodia write` ended in an AttributeError after the transcript had been written.
    """
    import argparse
    import json
    from unittest.mock import patch

    from prosodia.author import cli

    proj = tmp_path / "p"
    (proj / "plan").mkdir(parents=True)
    (proj / "series.yaml").write_text("series: S\npersona: casework\n", encoding="utf-8")
    (proj / "plan" / "outline.md").write_text(
        "# O\n\n## Episode 1 — A\n\n**Length:** 27 min\n\nbody\n", encoding="utf-8")

    def fake_author(brief, **kw):
        # stand in for the loop: leave a not-ready verdict where the real one lands
        d = proj / "episodes" / "ep01-a" / "run" / "stages" / "edit.r2"
        d.mkdir(parents=True, exist_ok=True)
        (d / "verdict.json").write_text(
            json.dumps({"ready": False, "notes": "BLOCKING\n1. SENTINEL_DEFECT"}), encoding="utf-8")
        return "---\nepisode: 1\n---\n\n## Beat\n\nSpoken words here.\n"

    args = argparse.Namespace(project=str(proj), episode=1, persona=None,
                              prior_episodes=0, max_rounds=2)
    with patch("prosodia.author.orchestrate.author_episode", side_effect=fake_author):
        assert cli._cmd_write(args) == 0

    notes = proj / "episodes" / "ep01-a" / "editor-notes.md"
    assert notes.is_file(), "an unresolved verdict must be preserved beside the transcript"
    assert "SENTINEL_DEFECT" in notes.read_text(encoding="utf-8")
    assert "NOT marked ready" in notes.read_text(encoding="utf-8")


def test_a_ready_verdict_leaves_no_editor_notes(tmp_path):
    import argparse
    import json
    from unittest.mock import patch

    from prosodia.author import cli

    proj = tmp_path / "p"
    (proj / "plan").mkdir(parents=True)
    (proj / "series.yaml").write_text("series: S\npersona: casework\n", encoding="utf-8")
    (proj / "plan" / "outline.md").write_text(
        "# O\n\n## Episode 1 — A\n\n**Length:** 27 min\n\nbody\n", encoding="utf-8")

    def fake_author(brief, **kw):
        d = proj / "episodes" / "ep01-a" / "run" / "stages" / "edit.r1"
        d.mkdir(parents=True, exist_ok=True)
        (d / "verdict.json").write_text(json.dumps({"ready": True, "notes": "fine"}), encoding="utf-8")
        return "---\nepisode: 1\n---\n\n## Beat\n\nSpoken words here.\n"

    args = argparse.Namespace(project=str(proj), episode=1, persona=None,
                              prior_episodes=0, max_rounds=2)
    with patch("prosodia.author.orchestrate.author_episode", side_effect=fake_author):
        assert cli._cmd_write(args) == 0
    assert not (proj / "episodes" / "ep01-a" / "editor-notes.md").exists()


def test_terms_to_earn_are_a_short_load_bearing_list_not_a_glossary():
    """A legal field has hundreds of terms; earning all of them teaches nothing.

    The planner names the few the reasoning turns on, and the writer earns those.
    """
    p = Persona.resolve("casework")
    planner = p.role("planner")
    assert "Load-bearing terms" in planner
    # a strict TEST rather than a quota: a small cap is a number standing in for judgement,
    # and some subjects genuinely need many terms — the answer there is a longer episode
    assert "reaches the WRONG ANSWER" in planner
    assert "There is no small quota" in planner
    assert "raise the episode's `Length`" in planner
    writer = p.role("writer")
    assert "Earn the plan's load-bearing terms" in writer
    assert "not every term" in writer
    assert "hundreds of terms" in writer
    editor = p.role("editor")
    assert "those, and not every term" in editor
    # and the bullet must not then turn round and demand a gloss on every term of art:
    # replacing only its label left exactly that contradiction in place for one commit
    assert "Do not ask for a gloss on every term of art" in editor
    assert "Fail a passage that leans on one of THOSE terms" in editor


def test_writer_runs_a_preflight_on_the_four_recurring_shortfalls():
    """Twenty-four blocking items across twelve editorial rounds had four causes.

    Unsourced numbers/attributions/novelty claims (9), spoken lists over three items (5),
    forward references over budget or early (5), and rules stated without their limit (4).
    Every one is checkable by the writer before it returns the draft.
    """
    writer = Persona.resolve("casework").role("writer")
    assert "BEFORE YOU RETURN THE DRAFT" in writer
    for check in ("Forward references", "Spoken lists", "Numbers, attributions and novelty",
                  "Rules stated without their limit"):
        assert check in writer, check
    # a note that quotes a sentence means fix THAT sentence
    assert "fix that sentence" in writer.lower()


def test_editor_must_quote_the_sentence_it_blocks_on():
    """The same early forward reference was reported in three consecutive rounds of one
    episode, described but never quoted, and was not fixed once. The round it was quoted, it
    was fixed immediately — two rounds spent on one sentence for want of naming it."""
    editor = Persona.resolve("casework").role("editor")
    assert "QUOTE THE OFFENDING SENTENCE IN EVERY BLOCKING ITEM" in editor
    assert "Give the words, then the replacement" in editor


def test_the_verdict_writer_may_dissent_but_must_declare_it():
    """The planner names the verdict because it is a SERIES-level claim and the writer of the
    last episode has not read the series — it gets the three most recent transcripts, handed
    over as phrasing to avoid. That is a reason about breadth, not about competence: the
    writer works the final argument far harder. So it may disagree, and must say so.
    """
    p = Persona.resolve("casework")
    planner = p.role("planner")
    assert "Not because the writer judges badly" in planner
    assert "least equipped" not in planner
    writer = p.role("writer")
    assert "say so rather than complying quietly" in writer
    assert "Silent compliance and silent divergence are both worse" in writer
