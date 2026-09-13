"""Compute-device selection for the render side.

Render-side only (imports torch lazily inside each function, so this module
stays importable — and unit-testable — on a torch-free authoring machine).

Resolution order: explicit argument -> ``$PROSODIA_DEVICE`` -> autodetect.

Two things make autodetect less obvious than ``torch.cuda.is_available()``:

* A **ROCm/HIP** build of torch reports AMD hardware through the *same*
  ``torch.cuda`` API, so ``is_available()`` is True on an AMD GPU too. There is
  no separate ``torch.rocm``.
* A HIP wheel ships precompiled kernels for a fixed list of gfx targets. On a
  GPU outside that list every kernel launch dies with a cryptic
  ``HIP error: invalid device function`` at the first matmul, long after model
  load. ``_hip_kernels_missing`` catches that up front and falls back to CPU
  instead, which is both correct and much easier to diagnose.

Note that "has a GPU" does not imply "the GPU is faster". On a shared-memory
APU the CPU can win outright, because the autoregressive stage is bound by
memory bandwidth the two already share. ``advice_for`` reports that rather than
silently picking the slower path.
"""

from __future__ import annotations

import os

# RDNA APU / mobile-integrated gfx targets. Discrete cards are absent on purpose:
# this list only drives an advisory note, never device selection.
_INTEGRATED_GFX = frozenset({
    "gfx1103", "gfx1150", "gfx1151", "gfx1152", "gfx1153",  # RDNA 3 / 3.5 APUs
    "gfx1036", "gfx1035", "gfx1034",                        # earlier mobile parts
})


def _gcn_arch(torch) -> str:
    """The active GPU's gfx target (``""`` when not a HIP build or no GPU)."""
    try:
        props = torch.cuda.get_device_properties(0)
    except Exception:
        return ""
    # gcnArchName looks like "gfx1152" or "gfx90a:sramecc+:xnack-"
    return str(getattr(props, "gcnArchName", "") or "").split(":")[0]


def _hip_kernels_missing(torch) -> str:
    """Return the unsupported gfx target, or ``""`` if the GPU is usable.

    A HIP build only carries kernels for the arches it was compiled for.
    ``HSA_OVERRIDE_GFX_VERSION`` makes the runtime *report* a different arch, so
    an override that lands on a compiled target reads as supported here — which
    is what we want: the user opted in explicitly.
    """
    if not getattr(torch.version, "hip", None):
        return ""  # CUDA build: no per-arch wheel gating to worry about
    arch = _gcn_arch(torch)
    if not arch:
        return ""
    try:
        compiled = {a.split(":")[0] for a in torch.cuda.get_arch_list()}
    except Exception:
        return ""
    return "" if arch in compiled else arch


def gpu_status() -> tuple[bool, str]:
    """``(usable, reason)`` for the GPU, without committing to a device."""
    try:
        import torch
    except Exception as exc:
        return False, f"PyTorch is not installed ({exc.__class__.__name__})"

    try:
        if not torch.cuda.is_available():
            return False, "no GPU visible to torch (CPU-only build, or no driver)"
    except Exception as exc:  # pragma: no cover - defensive
        return False, f"could not query the GPU: {exc}"

    unsupported = _hip_kernels_missing(torch)
    if unsupported:
        return False, (
            f"this ROCm torch has no kernels for {unsupported} "
            f"(built for: {', '.join(sorted(torch.cuda.get_arch_list()))}). "
            f"Set HSA_OVERRIDE_GFX_VERSION to a compiled target to try anyway."
        )
    return True, describe_gpu()


def describe_gpu() -> str:
    """Human-readable one-liner for the active GPU (``"none"`` if there isn't one)."""
    try:
        import torch

        if not torch.cuda.is_available():
            return "none"
        name = torch.cuda.get_device_name(0)
        mem = torch.cuda.get_device_properties(0).total_memory / 1024**3
        kind = f"ROCm {torch.version.hip}" if getattr(torch.version, "hip", None) else f"CUDA {torch.version.cuda}"
        arch = _gcn_arch(torch)
        return f"{name} ({kind}{f', {arch}' if arch else ''}, {mem:.1f} GiB)"
    except Exception:
        return "none"


def resolve_device(device: str | None = None) -> str:
    """Pick the torch device for rendering: explicit -> env -> autodetect."""
    explicit = device or os.environ.get("PROSODIA_DEVICE")
    if explicit:
        return explicit.strip().lower()
    usable, _ = gpu_status()
    return "cuda" if usable else "cpu"


def advice_for(device: str) -> str | None:
    """An advisory note about ``device``, or None when there is nothing to say."""
    if device != "cuda":
        return None
    try:
        import torch

        if not getattr(torch.version, "hip", None):
            return None
        override = os.environ.get("HSA_OVERRIDE_GFX_VERSION")
        if _gcn_arch(torch) in _INTEGRATED_GFX:
            return (
                "this is an integrated GPU sharing system memory with the CPU; "
                "the autoregressive stage is memory-bandwidth-bound, so "
                "--device cpu may well render faster - measure both"
            )
        if override:
            # HSA_OVERRIDE_GFX_VERSION makes the runtime report a different arch,
            # so the check above cannot see through it to an APU. Say so, since
            # anyone setting the override on an APU needs exactly that warning.
            return (
                f"HSA_OVERRIDE_GFX_VERSION={override} is set, so this GPU is running "
                "kernels built for another arch. If it is an integrated GPU, "
                "--device cpu may well render faster - measure both"
            )
    except Exception:
        return None
    return None
