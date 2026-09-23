#!/usr/bin/env python3
"""Require every Agent Eco pull request to advance the canonical SemVer."""

import re
import subprocess
import sys
from pathlib import Path


SEMVER = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$")


def parse(value: str, label: str) -> tuple[int, int, int]:
    match = SEMVER.fullmatch(value.strip())
    if not match:
        raise ValueError(f"{label} must be MAJOR.MINOR.PATCH with numeric parts")
    return tuple(map(int, match.groups()))


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: check_governance_version.py <base-commit>", file=sys.stderr)
        return 2
    try:
        current = parse(Path("VERSION").read_text(encoding="utf-8"), "Current VERSION")
        previous = subprocess.run(
            ["git", "show", f"{sys.argv[1]}:VERSION"],
            check=False, capture_output=True, text=True,
        )
        if previous.returncode and "exists on disk, but not in" in previous.stderr:
            print("Initial governance VERSION accepted")
            return 0
        if previous.returncode:
            print(previous.stderr.strip(), file=sys.stderr)
            return 2
        base = parse(previous.stdout, "Base VERSION")
    except (OSError, ValueError) as error:
        print(error, file=sys.stderr)
        return 2
    if current <= base:
        print(f"VERSION must increase from {'.'.join(map(str, base))}", file=sys.stderr)
        return 1
    print(f"Governance version increased from {'.'.join(map(str, base))} to {'.'.join(map(str, current))}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
