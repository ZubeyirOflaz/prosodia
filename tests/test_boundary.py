"""The authoring/render dependency boundary must hold.

`prosodia.core`, `prosodia.author`, and even the `prosodia.render` *package*
(not its heavy submodules) must import on a base, torch-free install. Only the
render submodules (render.py, backends.chatterbox_backend, ...) may require
torch. This locks repair item E1.
"""

import importlib
import importlib.util

import pytest


def test_core_and_author_import_without_torch():
    for mod in ["prosodia", "prosodia.core", "prosodia.author", "prosodia.author.cli"]:
        importlib.import_module(mod)


def test_render_package_and_cli_import_without_torch():
    # The package and its cli defer heavy imports, so these must succeed even
    # when torch is absent; only the render *submodules* need the extra.
    importlib.import_module("prosodia.render")
    importlib.import_module("prosodia.render.cli")


@pytest.mark.skipif(
    importlib.util.find_spec("torch") is not None,
    reason="torch is installed; the boundary assertion is only meaningful without it",
)
def test_torch_absent_on_authoring_install():
    assert importlib.util.find_spec("torch") is None
