#!/usr/bin/env python3
"""Verify a product snapshot against this Agent Eco checkout."""

import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: verify_governance_snapshot.py <context/governance>", file=sys.stderr)
        return 2
    folder = Path(sys.argv[1])
    try:
        manifest = json.loads((folder / "manifest.json").read_text(encoding="utf-8"))
        version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
        commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
        if manifest["governance_version"] != version or manifest["governance_commit"] != commit:
            raise ValueError("snapshot governance version or commit does not match this checkout")
        rows = []
        for name, record in sorted(manifest["files"].items()):
            target = (folder / name).resolve()
            if not target.is_relative_to(folder.resolve()):
                raise ValueError("snapshot path escapes its directory")
            digest = hashlib.sha256(target.read_bytes()).hexdigest()
            if digest != record["sha256"]:
                raise ValueError(f"snapshot content mismatch: {name}")
            rows.append(f"{name}:{digest}\n")
        digest = hashlib.sha256("".join(rows).encode()).hexdigest()
        if digest != manifest["snapshot_sha256"]:
            raise ValueError("snapshot manifest fingerprint mismatch")
    except (OSError, KeyError, ValueError, json.JSONDecodeError, subprocess.CalledProcessError) as error:
        print(error, file=sys.stderr)
        return 1
    print(f"Snapshot verified for governance {version}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
