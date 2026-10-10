#!/usr/bin/env python3
"""Copy every tracked Agent Eco file from one clean commit into a product mirror."""

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path, PurePosixPath


ROOT = Path(__file__).resolve().parents[1]
REPOSITORY = "https://github.com/ikechukwukalu/agenteco"


def git(*arguments: str) -> bytes:
    return subprocess.check_output(["git", *arguments], cwd=ROOT)


def safe_path(name: str) -> Path:
    path = PurePosixPath(name)
    if path.is_absolute() or not path.parts or any(part in (".", "..") for part in path.parts):
        raise ValueError(f"unsafe tracked path: {name}")
    return Path(*path.parts)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--product", required=True)
    parser.add_argument("--classification", required=True)
    parser.add_argument("--output", type=Path, required=True, help="New or empty mirror directory")
    args = parser.parse_args()

    if git("status", "--porcelain"):
        parser.error("Agent Eco checkout must be clean so the mirror matches its commit")
    output = args.output.resolve()
    if output == ROOT or ROOT in output.parents:
        parser.error("build outside the Agent Eco checkout")
    if output.exists() and any(output.iterdir()):
        parser.error("output directory must be empty; review existing mirrors before replacing them")

    commit = git("rev-parse", "HEAD").decode().strip()
    tree = git("rev-parse", "HEAD^{tree}").decode().strip()
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    entries = git("ls-tree", "-r", "-z", "HEAD").split(b"\0")
    files = {}
    payloads = {}

    for entry in filter(None, entries):
        metadata, raw_name = entry.split(b"\t", 1)
        mode, kind, blob = metadata.decode("ascii").split(" ")
        name = raw_name.decode("utf-8")
        relative = safe_path(name)
        if kind != "blob" or mode not in ("100644", "100755"):
            raise ValueError(f"unsupported tracked entry: {name} ({mode} {kind})")
        if relative.name == ".env" or (relative.name.startswith(".env.") and relative.name != ".env.example"):
            raise ValueError(f"refusing to mirror protected environment file: {name}")

        # Read the committed blob, never a working-tree approximation.
        payload = git("cat-file", "blob", blob)
        payloads[name] = payload
        files[name] = {
            "mode": mode,
            "sha256": hashlib.sha256(payload).hexdigest(),
            "size": len(payload),
        }

    if not files or "VERSION" not in files:
        raise ValueError("tracked governance tree is empty or lacks VERSION")

    fingerprint = hashlib.sha256(
        "".join(
            f"{name}\t{record['mode']}\t{record['sha256']}\n"
            for name, record in sorted(files.items())
        ).encode("utf-8")
    ).hexdigest()
    output.mkdir(parents=True, exist_ok=True)
    repository = output / "repository"
    for name, payload in payloads.items():
        destination = repository / safe_path(name)
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(payload)

    manifest = {
        "schema_version": 1,
        "product": args.product,
        "classification": args.classification,
        "governance_repository": REPOSITORY,
        "governance_version": version,
        "governance_commit": commit,
        "governance_tree": tree,
        "content_sha256": fingerprint,
        "files": files,
    }
    (output / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"Created full Agent Eco mirror {version} at {commit} ({len(files)} tracked files)")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, UnicodeError, subprocess.CalledProcessError) as error:
        print(error, file=sys.stderr)
        raise SystemExit(2)
