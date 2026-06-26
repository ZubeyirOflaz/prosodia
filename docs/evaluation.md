# Evaluation & testing

[← Docs index](README.md)

Two kinds of checks: the **automated test suite** (correctness of the pipeline)
and the **A/B naturalness method** (does the audio actually beat NotebookLM).

## Automated tests

```bash
pip install -e ".[dev]"
python -m pytest -q
```

The suite covers the IR round-trip, the job protocol (manifest tamper/missing
detection, atomic publish), the trace log, the tone table (including "every SPEC
tone is mapped"), text utilities (chunking, normalization, lexicon), the compile
parser (directives, front-matter, beats, pauses, emphasis, speakers, escapes), the
submit packaging, and the orchestrator loop (with a fake runner — no quota used).

Two modules (`tests/test_audio.py`, `tests/test_render.py`) are **skipped** unless
numpy is present (it ships with the `[render]` extra), so they run on the GPU box
but not on a torch-free authoring install. The boundary itself is tested:
`tests/test_boundary.py` asserts `import prosodia.render` works with no torch.

Lint:

```bash
python -m ruff check src tests
```

## A/B naturalness method

The project's central bet is that controlled, single-narrator Chatterbox beats
NotebookLM on the [four problems](overview.md). The first corpus is the EU history
series, episodes 1–3.

Use the scoring sheet in [A/B testing](AB_TESTING.md): listen to both, score each
problem dimension 1–5, note timestamps where Prosodia is worse, then route each
issue to its stage with the [troubleshooting table](pipeline-and-traces.md#troubleshooting).

> This step needs your hardware and your ears — it can't be automated. It's the
> first thing to do once the renderer has produced audio on the 3080 box. See
> [Roadmap & status](roadmap.md).

## See also

[A/B testing](AB_TESTING.md) · [Pipeline & traces](pipeline-and-traces.md) ·
[Roadmap & status](roadmap.md)
