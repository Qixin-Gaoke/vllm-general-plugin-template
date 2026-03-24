from __future__ import annotations

from vllm_general_plugin_template.launcher import _merge_plugins


def test_merge_plugins_when_empty() -> None:
    assert _merge_plugins(None, "general_plugin_template") == "general_plugin_template"


def test_merge_plugins_appends_once() -> None:
    merged = _merge_plugins("foo,bar", "general_plugin_template")
    assert merged == "foo,bar,general_plugin_template"
    assert _merge_plugins(merged, "general_plugin_template") == merged