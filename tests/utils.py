"""Shared utilities for market-sages test scripts."""
import sys
from pathlib import Path


def parse_frontmatter(content: str, source: Path) -> str:
    """Strip YAML frontmatter and return the body.

    Exits with a clear message if the frontmatter is malformed so callers
    don't have to handle the error themselves.
    """
    if not content.startswith("---"):
        return content
    try:
        end = content.index("---", 3)
    except ValueError:
        sys.exit(
            f"{source}: frontmatter is missing its closing ---.\n"
            f"Run 'python3 tests/validate_structure.py' to diagnose."
        )
    return content[end + 3:].lstrip()
