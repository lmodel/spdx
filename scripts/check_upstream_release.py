#!/usr/bin/env python3
"""Check the vendored SPDX model against what the SPDX Project publishes.

Two things can change without a commit here: the SPDX Project releases a newer
model, so the schema falls behind, or the vendored file drifts from the release
it claims to be. The script reads the version from the vendored model's
ontology IRI, downloads the model the SPDX Project publishes for that version,
and compares the two byte for byte. It then asks GitHub for the tags of
spdx/spdx-3-model, to see whether a newer release exists.

It prints a Markdown report, and exits 1 when the file differs or a newer
release exists. A release candidate newer than every release is reported, and
does not fail the check.

Set ``GITHUB_TOKEN`` to raise the API rate limit. The script sends it to the
GitHub API only, and not on to a host the API redirects to. Usage::

    python3 scripts/check_upstream_release.py [--report FILE]
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VENDORED = ROOT / "src" / "spdx" / "schema" / "upstream" / "spdx-model.ttl"
TAGS_API = "https://api.github.com/repos/spdx/spdx-3-model/tags?per_page=100"
TERMS = re.compile(r"https://spdx\.org/rdf/([0-9][^/>]*)/terms/")
TAG = re.compile(r"^v?(\d+)\.(\d+)(?:\.(\d+))?(?:-?(rc\d+))?$", re.IGNORECASE)


def _get(url: str) -> bytes:
    request = urllib.request.Request(
        url, headers={"User-Agent": "lmodel-spdx-upstream-check"}
    )
    token = os.environ.get("GITHUB_TOKEN")
    if token and url.startswith("https://api.github.com/"):
        # urllib copies ordinary headers onto a redirect, whatever its host.
        request.add_unredirected_header("Authorization", f"Bearer {token}")
        request.add_header("Accept", "application/vnd.github+json")
    with urllib.request.urlopen(request, timeout=60) as response:
        return response.read()


def _parse(tag: str):
    """(major, minor, patch, is_final) for a release tag, or None for another tag."""
    match = TAG.match(tag)
    if not match:
        return None
    major, minor, patch, rc = match.groups()
    return (int(major), int(minor), int(patch or 0), rc is None)


def check() -> tuple[list[str], bool]:
    """Return the report lines and whether anything needs attention."""
    vendored = VENDORED.read_bytes()
    match = TERMS.search(vendored.decode("utf-8", errors="replace"))
    if not match:
        return [
            f"- `{VENDORED.relative_to(ROOT)}` names no SPDX terms namespace."
        ], True
    version = match.group(1)
    report = [f"- Vendored model: SPDX {version} (`{VENDORED.relative_to(ROOT)}`)."]
    attention = False

    published_url = f"https://spdx.org/rdf/{version}/spdx-model.ttl"
    published = _get(published_url)
    if published == vendored:
        report.append(
            f"- The vendored file is byte for byte the model published at <{published_url}>."
        )
    else:
        report.append(
            f"- The vendored file differs from the model published at <{published_url}>."
        )
        attention = True

    tags = [t["name"] for t in json.loads(_get(TAGS_API))]
    parsed = {t: _parse(t) for t in tags}
    current = _parse(version)
    finals = sorted((v for v in parsed.values() if v and v[3]), reverse=True)
    candidates = sorted((v for v in parsed.values() if v and not v[3]), reverse=True)
    newest = finals[0] if finals else None
    if newest and current and newest[:3] > current[:3]:
        report.append(
            f"- A newer SPDX release exists: {newest[0]}.{newest[1]}.{newest[2]}."
        )
        attention = True
    elif newest:
        report.append(
            f"- The vendored model is the latest SPDX release ({newest[0]}.{newest[1]}.{newest[2]})."
        )
    known = [v[:3] for v in (current, newest) if v]
    if candidates and known and candidates[0][:3] > max(known):
        tag = next(t for t, v in parsed.items() if v == candidates[0])
        report.append(f"- A release candidate is tagged upstream: `{tag}`.")
    return report, attention


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument(
        "--report", type=Path, help="also write the Markdown report to this file"
    )
    args = parser.parse_args(argv)
    report, attention = check()
    text = "\n".join(report) + "\n"
    print(text, end="")
    if args.report:
        args.report.write_text(text, encoding="utf-8")
    return 1 if attention else 0


if __name__ == "__main__":
    sys.exit(main())
