#!/usr/bin/env python3
"""Build a role-selective Agent Eco snapshot for a product context repository."""

import argparse
import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CORE = [
    "rules/global-engineering-rules.md",
    "governance/operating-constitution.md",
    "governance/implementation-authorization-integrity.md",
    "governance/owner-controlled-governance.md",
    "governance/delivery-and-pr-governance.md",
    "governance/repository-readiness-preflight.md",
    "governance/session-and-role-selection.md",
    "governance/instruction-adapter-integrity.md",
    "governance/access-degraded-mode.md",
    "governance/versioned-context-snapshots.md",
    "governance/scoped-product-rules.md",
    "governance/feature-availability.md",
    "governance/production-context-reconciliation.md",
    "commands/README.md",
]
ADA = [
    "governance/business-context-mode.md",
    "governance/ada-internal-modes.md",
    "rules/ada-support-capability.md",
]


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def bundle(paths: list[str]) -> str:
    return "\n\n".join(
        f"<!-- Source: {path} -->\n\n{(ROOT / path).read_text(encoding='utf-8').rstrip()}"
        for path in paths
    ) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--product", required=True)
    parser.add_argument("--context-revision", required=True)
    parser.add_argument("--classification", required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--roles", nargs="+", required=True, help="Specialist names, such as Ada Chinedu Dotun")
    args = parser.parse_args()

    if git("status", "--porcelain"):
        parser.error("Agent Eco checkout must be clean so the snapshot matches its commit")
    role_files = {p.name.split(".")[0]: p for p in (ROOT / "agents").glob("*.md") if p.name != "README.md"}
    selected = {}
    for role in args.roles:
        key = role.lower().replace(" ", "-")
        if key not in role_files:
            parser.error(f"unknown specialist: {role}")
        selected[key] = role_files[key]
    if args.output.exists() and any(args.output.iterdir()):
        parser.error("output directory must be empty; review existing snapshots before replacing them")

    args.output.mkdir(parents=True, exist_ok=True)
    (args.output / "roles").mkdir()
    sections = {"core.md": CORE}
    for key, role_file in selected.items():
        paths = [str(role_file.relative_to(ROOT))]
        if key == "ada":
            paths += ADA
        sections[f"roles/{key}.md"] = paths

    files = {}
    for relative, sources in sorted(sections.items()):
        content = bundle(sources)
        (args.output / relative).write_text(content, encoding="utf-8")
        files[relative] = {"sha256": hashlib.sha256(content.encode()).hexdigest(), "sources": sources}

    fingerprint_input = "".join(f"{path}:{files[path]['sha256']}\n" for path in sorted(files))
    manifest = {
        "schema_version": 1,
        "product": args.product,
        "classification": args.classification,
        "governance_repository": "https://github.com/ikechukwukalu/agenteco",
        "governance_version": (ROOT / "VERSION").read_text(encoding="utf-8").strip(),
        "governance_commit": git("rev-parse", "HEAD"),
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "product_context_commit_at_generation": args.context_revision,
        "snapshot_sha256": hashlib.sha256(fingerprint_input.encode()).hexdigest(),
        "files": files,
        "rule_index_path": "context/rules/index.md",
        "availability_catalogue_path": "context/releases/feature-availability.md",
    }
    (args.output / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"Created {args.output} for governance {manifest['governance_version']} at {manifest['governance_commit']}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, subprocess.CalledProcessError) as error:
        print(error, file=sys.stderr)
        raise SystemExit(2)
