#!/usr/bin/env python3
"""Verify a product's complete Agent Eco mirror without needing source access."""

import argparse
import hashlib
import json
import sys
from pathlib import Path, PurePosixPath


REPOSITORY = "https://github.com/ikechukwukalu/agenteco"


def safe_path(name: str) -> Path:
    path = PurePosixPath(name)
    if path.is_absolute() or not path.parts or any(part in (".", "..") for part in path.parts):
        raise ValueError(f"unsafe mirror path: {name}")
    return Path(*path.parts)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mirror", type=Path)
    args = parser.parse_args()
    mirror = args.mirror.resolve()

    try:
        manifest = json.loads((mirror / "manifest.json").read_text(encoding="utf-8"))
        if manifest["governance_repository"] != REPOSITORY:
            raise ValueError("unexpected governance repository")
        files = manifest["files"]
        if not files or "VERSION" not in files:
            raise ValueError("mirror lacks tracked governance files")
        actual = set()
        for target in (mirror / "repository").rglob("*"):
            if target.is_symlink():
                raise ValueError(f"symlink in mirror: {target}")
            if target.is_file():
                actual.add(target.relative_to(mirror / "repository").as_posix())
        if actual != set(files):
            raise ValueError("mirror file inventory differs from manifest")

        for name, record in files.items():
            target = mirror / "repository" / safe_path(name)
            payload = target.read_bytes()
            if len(payload) != record["size"] or hashlib.sha256(payload).hexdigest() != record["sha256"]:
                raise ValueError(f"mirror content mismatch: {name}")
        version = (mirror / "repository" / "VERSION").read_text(encoding="utf-8").strip()
        if version != manifest["governance_version"]:
            raise ValueError("mirror VERSION differs from manifest")
        fingerprint = hashlib.sha256(
            "".join(
                f"{name}\t{record['mode']}\t{record['sha256']}\n"
                for name, record in sorted(files.items())
            ).encode("utf-8")
        ).hexdigest()
        if fingerprint != manifest["content_sha256"]:
            raise ValueError("mirror fingerprint mismatch")
    except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError) as error:
        print(error, file=sys.stderr)
        return 1

    print(f"Mirror integrity verified for Agent Eco {version} at {manifest['governance_commit']}")
    print("Freshness against canonical Agent Eco was not checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
