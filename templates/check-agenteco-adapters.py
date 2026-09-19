#!/usr/bin/env python3
"""Report missing or drifted required Agent Eco adapters without changing files."""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
from pathlib import Path


START = "<!-- AGENT-ECO:CANONICAL-START -->"
END = "<!-- AGENT-ECO:CANONICAL-END -->"
PLACEHOLDERS = {"", "<FINGERPRINT_OR_NONE>", "none", "NONE"}


def adapter_records(manifest: Path) -> list[dict[str, str]]:
    records: list[dict[str, str]] = []
    in_adapters = False
    current: dict[str, str] | None = None
    for raw in manifest.read_text(encoding="utf-8").splitlines():
        if raw == "adapters:":
            in_adapters = True
            continue
        if in_adapters and raw and not raw.startswith(" "):
            break
        if not in_adapters:
            continue
        section = re.match(r"^  ([a-z0-9_]+):\s*$", raw)
        if section:
            if current and "path" in current:
                records.append(current)
            current = {"id": section.group(1)}
            continue
        field = re.match(r'^    ([a-z0-9_]+):\s*["\']?(.*?)["\']?\s*$', raw)
        if field and current is not None:
            current[field.group(1)] = field.group(2)
    if current and "path" in current:
        records.append(current)
    return records


def canonical_fingerprint(text: str) -> str:
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    if normalized.count(START) != 1 or normalized.count(END) != 1:
        raise ValueError("managed canonical markers are missing or duplicated")
    canonical = normalized.split(START, 1)[1].split(END, 1)[0].strip("\n") + "\n"
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", default=".agenteco/manifest.yml")
    parser.add_argument("--root", default=".")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    manifest = (root / args.manifest).resolve()
    if not manifest.is_file():
        print(f"ERROR: Agent Eco manifest not found: {manifest}")
        return 1
    records = adapter_records(manifest)
    if not records:
        print("ERROR: manifest contains no path-bearing adapter records")
        return 1
    failures: list[str] = []
    checked = 0
    for record in records:
        if record.get("required", "false").lower() != "true":
            continue
        checked += 1
        path_value = record.get("path", "")
        if path_value in {"", "<PATH_OR_NONE>"}:
            failures.append(f"{record['id']}: required adapter has no concrete path")
            continue
        path = (root / path_value).resolve()
        try:
            path.relative_to(root)
        except ValueError:
            failures.append(f"{record['id']}: adapter path escapes repository root")
            continue
        if not path.is_file():
            failures.append(f"{record['id']}: required adapter is missing at {path_value}")
            continue
        try:
            actual = canonical_fingerprint(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeError, ValueError) as error:
            failures.append(f"{record['id']}: {error}")
            continue
        expected = record.get("canonical_fingerprint", "")
        if expected in PLACEHOLDERS:
            failures.append(f"{record['id']}: canonical fingerprint is not configured")
        elif actual != expected:
            failures.append(
                f"{record['id']}: canonical fingerprint mismatch "
                f"(expected {expected}, found {actual})"
            )
    if checked == 0:
        failures.append("manifest declares no required adapters")
    if failures:
        print("Agent Eco adapter integrity check failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("Agent Eco required adapters are present and canonically valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
