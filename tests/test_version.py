"""The package version must agree everywhere it is written down."""

from __future__ import annotations

import re
from pathlib import Path

import spotify_api_sdk
from spotify_api_sdk.config import DEFAULT_USER_AGENT

ROOT = Path(__file__).resolve().parents[1]


def test_version_matches_pyproject_user_agent_and_changelog() -> None:
    pyproject = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
    match = re.search(r'^version = "([^"]+)"$', pyproject, re.MULTILINE)
    assert match is not None
    version = match.group(1)
    assert spotify_api_sdk.__version__ == version
    assert f"checkleaked-spotify-api-python/{version} " in DEFAULT_USER_AGENT
    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    assert f"## {version} " in changelog
