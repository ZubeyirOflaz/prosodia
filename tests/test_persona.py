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
