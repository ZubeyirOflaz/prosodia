# Getting started

[← Docs index](README.md)

## Install

**Authoring** (any machine, no GPU — pure-Python, no torch):

```bash
git clone https://github.com/ZubeyirOflaz/prosodia
cd prosodia
pip install -e .            # base install: authoring only, no torch
```

This gives you the `prosodia` command. **Rendering** runs on a separate Windows +
NVIDIA box and has its own one-time setup — see [Renderer setup](../scripts/RENDERER_SETUP.md).
(The render extra is `pip install prosodia[render]`, but install a CUDA torch
wheel first; `setup.ps1` does this in the right order.)

> Python: authoring works on 3.11–3.14. The render box should use **3.11 or 3.12**
> (torch/Chatterbox wheels lag newer Python).

## Run the worked example

A complete example series ships in `projects/eu_history/` (episode 1 is authored).
Compile it to the [IR](architecture.md#contracts-prosodiacore) and a render plan:

```bash
prosodia compile projects/eu_history/episodes/ep1/transcript.md \
  --config projects/eu_history/series.yaml \
  --lexicon projects/eu_history/lexicon.yaml
# -> compiled N segments -> projects/eu_history/episodes/ep1/ir.json
```

This writes `ir.json` + `render_plan.json` next to the transcript. Then package a
render job into your synced exchange folder:

```bash
prosodia submit projects/eu_history/episodes/ep1 --root <synced_folder> --job-id eu-ep1
# -> submitted job 'eu-ep1' -> <synced_folder>/inbox/eu-ep1
```

On the GPU box, the watcher picks it up and writes `outbox/eu-ep1/episode.wav`.
See [Handoff](HANDOFF.md) for the end-to-end flow.

## Author with the orchestrator (optional)

Instead of writing the transcript by hand, drive the headless Claude Code loop
(requires the `claude` CLI, on your subscription):

```bash
prosodia plan  --project projects/eu_history                 # outline + coverage map
prosodia write --project projects/eu_history --episode 1     # Writer ⇄ Editor loop
```

See the [Authoring guide](authoring-guide.md) and the [CLI reference](cli-reference.md).

## Run the tests

```bash
pip install -e ".[dev]"
python -m pytest -q
```

More in [Evaluation & testing](evaluation.md).

## See also

[Authoring guide](authoring-guide.md) · [Configuration](configuration.md) ·
[CLI reference](cli-reference.md) · [Rendering](rendering.md)
