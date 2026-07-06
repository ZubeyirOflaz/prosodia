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
