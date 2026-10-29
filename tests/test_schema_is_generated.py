"""The schema files are the converter's output; a hand edit, or a stale regeneration, fails here."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def test_schema_matches_a_fresh_regeneration() -> None:
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "spdx_to_linkml.py"), "--check"],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
