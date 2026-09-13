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
    # 27 minutes is the measured unit of the architecture source, not a round guess.
    assert p.defaults.target_minutes == 27
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
