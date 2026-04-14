#!/usr/bin/env python3
"""
Structural validator for skill.md — no API key required.
Verifies frontmatter, sage count, required sections, and QUICK COMMANDS completeness.

Usage:
    python3 tests/validate_structure.py
    python3 tests/validate_structure.py --verbose
"""
import re
import sys

if sys.version_info < (3, 10):
    sys.exit("Python 3.10+ required. Current: {}.{}.{}".format(*sys.version_info[:3]))

from pathlib import Path
from utils import parse_frontmatter

SKILL_FILE = Path("skill.md")
EXPECTED_SAGE_COUNT = 13
REQUIRED_IN_EACH_SAGE = ["Signal rules:", "Speak in"]
SIGNAL_DIRECTIONS = ["**Bullish**", "**Bearish**", "**Neutral**"]
REQUIRED_FRONTMATTER_FIELDS = ["name:", "version:", "author:", "tags:"]
SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+$")
REQUIRED_IN_QUICK_COMMANDS = ["--value", "--growth", "--risk", "--brief", "compare", "@"]


# ── Checks ────────────────────────────────────────────────────────────────────

def check_frontmatter(content: str) -> list[str]:
    """Verify YAML frontmatter exists and contains required fields."""
    errors = []
    if not content.startswith("---"):
        return ["  skill.md has no YAML frontmatter (must start with ---)"]

    try:
        end = content.index("---", 3)
        frontmatter = content[3:end]
    except ValueError:
        return ["  skill.md frontmatter is not closed (missing closing ---)"]

    for field in REQUIRED_FRONTMATTER_FIELDS:
        if field not in frontmatter:
            errors.append(f"  Frontmatter missing '{field}' — publishing will fail")

    version_match = re.search(r"^version:\s*(.+)$", frontmatter, re.MULTILINE)
    if version_match:
        version = version_match.group(1).strip()
        if not SEMVER_RE.match(version):
            errors.append(f"  Frontmatter 'version: {version}' is not valid semver (X.Y.Z)")

    return errors


def parse_sage_blocks(content: str) -> list[tuple[str, str]]:
    """Return list of (name, block_text) for each sage entry."""
    pattern = re.compile(r"^(#### \d+\. .+)$", re.MULTILINE)
    matches = list(pattern.finditer(content))
    blocks = []
    for i, match in enumerate(matches):
        start = match.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(content)
        name = match.group(1).replace("#### ", "")
        blocks.append((name, content[start:end]))
    return blocks


def check_sage_count(blocks: list) -> list[str]:
    if len(blocks) != EXPECTED_SAGE_COUNT:
        return [f"  Expected {EXPECTED_SAGE_COUNT} sages, found {len(blocks)}"]
    return []


def check_sage_sections(blocks: list[tuple[str, str]]) -> list[str]:
    """Verify each sage has required sections and all three signal directions."""
    errors = []
    for name, block in blocks:
        for required in REQUIRED_IN_EACH_SAGE:
            if required not in block:
                errors.append(f"  Sage '{name}' missing '{required}'")
        for direction in SIGNAL_DIRECTIONS:
            if direction not in block:
                errors.append(f"  Sage '{name}' missing signal direction '{direction}'")
    return errors


def check_quick_commands(content: str) -> list[str]:
    """Verify QUICK COMMANDS section exists and defines all required flags."""
    match = re.search(
        r"## QUICK COMMANDS(.+?)(?=^##|\Z)", content, re.MULTILINE | re.DOTALL
    )
    if not match:
        return ["  QUICK COMMANDS section not found in skill.md"]
    section = match.group(1)
    return [
        f"  QUICK COMMANDS missing '{flag}'"
        for flag in REQUIRED_IN_QUICK_COMMANDS
        if flag not in section
    ]


# ── Main ──────────────────────────────────────────────────────────────────────

def main() -> None:
    verbose = "--verbose" in sys.argv

    try:
        content = SKILL_FILE.read_text()
    except FileNotFoundError:
        print(f"❌ {SKILL_FILE} not found. Run from project root.")
        sys.exit(1)

    blocks = parse_sage_blocks(content)

    if verbose:
        print(f"Sages ({len(blocks)}):")
        for name, _ in blocks:
            print(f"  ✓ {name}")

    errors: list[str] = []
    errors += check_frontmatter(content)
    errors += check_sage_count(blocks)
    errors += check_sage_sections(blocks)
    errors += check_quick_commands(content)

    if errors:
        print("❌ Structure validation failed:")
        for e in errors:
            print(e)
        sys.exit(1)

    print(
        f"✅ Structure valid: {len(blocks)} sages · "
        f"frontmatter OK · all sections present · all QUICK COMMANDS flags defined"
    )


if __name__ == "__main__":
    main()
