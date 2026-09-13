"""Render-device selection must not pick a GPU that cannot actually run kernels.

The regression this guards: a ROCm/HIP torch reports AMD hardware through the
same ``torch.cuda`` API, so ``torch.cuda.is_available()`` is True even when the
wheel carries no kernels for that gfx target — and every launch then dies with
``HIP error: invalid device function`` at the first matmul, long after model
load. Selection must detect that up front and fall back to CPU.

``torch`` is imported lazily inside ``device.py`` (the authoring side must stay
torch-free), so these tests inject a fake module into ``sys.modules``.
"""

import sys
import types

import pytest

from prosodia.render import device as D


def _fake_torch(*, available=True, hip=None, cuda="12.6", arch="", arch_list=(), name="Fake GPU"):
    """A stand-in for the parts of torch that device.py introspects."""
    t = types.ModuleType("torch")
    t.version = types.SimpleNamespace(hip=hip, cuda=cuda)
    props = types.SimpleNamespace(gcnArchName=arch, total_memory=8 * 1024**3)
    t.cuda = types.SimpleNamespace(
        is_available=lambda: available,
        get_device_properties=lambda i: props,
        get_device_name=lambda i: name,
        get_arch_list=lambda: list(arch_list),
    )
    return t


@pytest.fixture
def fake_torch(monkeypatch):
    def install(**kw):
        monkeypatch.setitem(sys.modules, "torch", _fake_torch(**kw))
    monkeypatch.delenv("PROSODIA_DEVICE", raising=False)
    return install


# ── explicit choice and the env override always win ──────────────────────────

def test_explicit_argument_wins(fake_torch):
    fake_torch(available=True, arch_list=["sm_86"])
    assert D.resolve_device("cpu") == "cpu"


def test_env_override_wins_over_autodetect(fake_torch, monkeypatch):
    fake_torch(available=True, arch_list=["sm_86"])
    monkeypatch.setenv("PROSODIA_DEVICE", "cpu")
    assert D.resolve_device() == "cpu"


def test_explicit_argument_beats_env(fake_torch, monkeypatch):
    fake_torch(available=False)
    monkeypatch.setenv("PROSODIA_DEVICE", "cpu")
    assert D.resolve_device("cuda") == "cuda"


def test_explicit_value_is_normalized(fake_torch):
    fake_torch(available=False)
    assert D.resolve_device("  CUDA  ") == "cuda"


# ── autodetect ───────────────────────────────────────────────────────────────

def test_cuda_gpu_is_selected(fake_torch):
    fake_torch(available=True, cuda="12.6", arch_list=["sm_86"])
    assert D.resolve_device() == "cuda"


def test_no_gpu_falls_back_to_cpu(fake_torch):
    fake_torch(available=False)
    assert D.resolve_device() == "cpu"
    usable, reason = D.gpu_status()
    assert not usable
    assert "no GPU visible" in reason


def test_missing_torch_is_cpu(monkeypatch):
    monkeypatch.delenv("PROSODIA_DEVICE", raising=False)
    monkeypatch.setitem(sys.modules, "torch", None)  # import torch -> raises
    assert D.resolve_device() == "cpu"
    usable, reason = D.gpu_status()
    assert not usable and "PyTorch" in reason


# ── the HIP kernel gate (the real bug) ───────────────────────────────────────

def test_hip_gpu_without_kernels_falls_back_to_cpu(fake_torch):
    # gfx1152 (Radeon 860M) against a wheel built for gfx1100/gfx1151 only.
    fake_torch(available=True, hip="6.4.0", cuda=None, arch="gfx1152",
               arch_list=["gfx1100", "gfx1151"])
    assert D.resolve_device() == "cpu"
    usable, reason = D.gpu_status()
    assert not usable
    assert "gfx1152" in reason and "HSA_OVERRIDE_GFX_VERSION" in reason


def test_hip_gpu_with_kernels_is_selected(fake_torch):
    fake_torch(available=True, hip="6.4.0", cuda=None, arch="gfx1100",
               arch_list=["gfx1100", "gfx1151"])
    assert D.resolve_device() == "cuda"
    assert D.gpu_status()[0]


def test_arch_qualifiers_are_ignored_when_matching(fake_torch):
    # gcnArchName carries feature suffixes; the arch list may or may not.
    fake_torch(available=True, hip="6.4.0", cuda=None, arch="gfx90a:sramecc+:xnack-",
               arch_list=["gfx90a"])
    assert D.resolve_device() == "cuda"


def test_cuda_build_is_not_arch_gated(fake_torch):
    # get_arch_list() on a CUDA build lists sm_* targets; it must not be compared
    # against a gfx name and must never veto a working NVIDIA GPU.
    fake_torch(available=True, hip=None, cuda="12.6", arch="", arch_list=["sm_86", "sm_90"])
    assert D.resolve_device() == "cuda"


# ── advisory note for integrated GPUs ────────────────────────────────────────

def test_integrated_amd_gpu_warns_that_cpu_may_be_faster(fake_torch):
    fake_torch(available=True, hip="6.4.0", cuda=None, arch="gfx1152", arch_list=["gfx1152"])
    note = D.advice_for("cuda")
    assert note and "integrated" in note and "cpu" in note.lower()


def test_discrete_amd_gpu_gets_no_warning(fake_torch):
    fake_torch(available=True, hip="6.4.0", cuda=None, arch="gfx1100", arch_list=["gfx1100"])
    assert D.advice_for("cuda") is None


def test_cpu_device_gets_no_gpu_warning(fake_torch):
    fake_torch(available=False)
    assert D.advice_for("cpu") is None


def test_describe_gpu_reports_the_backend(fake_torch):
    fake_torch(available=True, hip="6.4.0", cuda=None, arch="gfx1152",
               arch_list=["gfx1152"], name="AMD Radeon 860M")
    text = D.describe_gpu()
    assert "AMD Radeon 860M" in text and "ROCm" in text and "gfx1152" in text


def test_describe_gpu_none_without_a_gpu(fake_torch):
    fake_torch(available=False)
    assert D.describe_gpu() == "none"


def test_hsa_override_warns_even_when_the_arch_looks_discrete(fake_torch, monkeypatch):
    # With an override set, HSA reports the *overridden* arch, so the APU check
    # above cannot see through it — anyone doing this on an iGPU still needs the
    # "CPU may be faster" warning.
    fake_torch(available=True, hip="6.4.0", cuda=None, arch="gfx1100", arch_list=["gfx1100"])
    monkeypatch.setenv("HSA_OVERRIDE_GFX_VERSION", "11.0.0")
    note = D.advice_for("cuda")
    assert note and "HSA_OVERRIDE_GFX_VERSION=11.0.0" in note and "cpu" in note.lower()


def test_no_override_on_discrete_amd_stays_quiet(fake_torch, monkeypatch):
    fake_torch(available=True, hip="6.4.0", cuda=None, arch="gfx1100", arch_list=["gfx1100"])
    monkeypatch.delenv("HSA_OVERRIDE_GFX_VERSION", raising=False)
    assert D.advice_for("cuda") is None


def test_nvidia_never_gets_an_amd_warning(fake_torch, monkeypatch):
    fake_torch(available=True, hip=None, cuda="12.6", arch="", arch_list=["sm_86"])
    monkeypatch.setenv("HSA_OVERRIDE_GFX_VERSION", "11.0.0")  # stray, irrelevant
    assert D.advice_for("cuda") is None
