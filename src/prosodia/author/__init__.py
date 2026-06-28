"""Authoring side — runs anywhere, no GPU, no torch.

Orchestrates the multi-agent authoring pipeline (Planner -> Writer <-> Editor
editorial loop -> Tone specialist) by driving headless Claude Code, then
compiles the approved transcript to IR and packages a render job for the synced
inbox. Every stage writes a versioned, diffable artifact plus a trace entry, so
feedback can be routed back to the stage that produced a given result.
"""
