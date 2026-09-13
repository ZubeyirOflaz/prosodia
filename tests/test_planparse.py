from prosodia.author.planparse import extract_episode_section

OUTLINE = '''# Ever Closer Union

## Coverage map
| topic | Ep |
|---|---|
| ruin | 1 |

## EPISODE 1 — "The Cognac Salesman"
Scope: the ruin and Monnet.
Texture: Monnet's father's line (sourced).

## EPISODE 2 — "The Bombshell"
Scope: the Schuman Declaration.

## Series arc at a glance
the end.
'''


def test_extracts_target_episode_only():
    s = extract_episode_section(OUTLINE, 1)
    assert s and "Cognac" in s and "Monnet's father" in s
    assert "Bombshell" not in s  # stops at the next episode heading
    assert "Coverage map" not in s  # doesn't grab an earlier section


def test_extracts_second_episode_and_stops_at_top_section():
    s = extract_episode_section(OUTLINE, 2)
    assert "Bombshell" in s and "Series arc" not in s


def test_missing_episode_returns_none():
    assert extract_episode_section(OUTLINE, 9) is None


def test_number_boundary_1_vs_10():
    md = '## Episode 10 — Ten\nbody-ten\n\n## Episode 1 — One\nbody-one'
    s = extract_episode_section(md, 1)
    assert "One" in s and "body-one" in s and "Ten" not in s


def test_level_3_episode_headings():
    md = "## Part A\n### Episode 1 — a\nbodyA\n### Episode 2 — b\nbodyB"
    s = extract_episode_section(md, 1)
    assert "bodyA" in s and "bodyB" not in s


def test_parse_episode_index_bridges_the_plan_to_series_yaml():
    """The Planner's episodes live only in the outline; `write` looks them up elsewhere.

    Without this bridge a freshly planned series has no episodes at all and every
    `prosodia write` fails, and a hand-transcribed list drops whatever it leaves out —
    most damagingly the per-episode length, so an episode planned at 38 minutes gets
    commissioned at the series default.
    """
    from prosodia.author.planparse import parse_episode_index

    outline = (
        "# Outline\n\n## The coverage map\n\ntable here\n\n"
        "## Episode 1 — The Gate\n\n**Length:** 27 min\n\nbody\n\n"
        "## Episode 2 — [LENS] The Pacing Problem\n\n**Length:** 24 minutes\n\nbody\n\n"
        "## Episode 3 — Under Whose Name\n\nno length stated\n\n"
        "## Names for the lexicon\n\n- Something\n"
    )
    eps = parse_episode_index(outline)
    assert [e["n"] for e in eps] == [1, 2, 3]
    assert eps[0] == {"n": 1, "slug": "ep01-the-gate", "title": "The Gate",
                      "type": "apparatus", "target_minutes": 27}
    # the heading's type marker is captured and stripped from both title and slug
    assert eps[1]["type"] == "lens"
    assert eps[1]["title"] == "The Pacing Problem"
    assert eps[1]["slug"] == "ep02-the-pacing-problem"
    # an episode with no stated length carries none, so the series default applies
    assert "target_minutes" not in eps[2]
    # non-episode headings are not episodes
    assert all("lexicon" not in e["title"].lower() for e in eps)
