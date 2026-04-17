"""Shared utilities for market-sages test scripts."""
import sys
from pathlib import Path


def split_frontmatter(content: str) -> tuple[str, str] | None:
    """Return (frontmatter_text, body) or None if no well-formed frontmatter exists.

    The frontmatter_text excludes the opening/closing `---` markers.
    None is returned when content lacks the opening fence OR the opening
    fence has no matching close. Callers decide how to handle either case.
    """
    if not content.startswith("---"):
        return None
    try:
        end = content.index("---", 3)
    except ValueError:
        return None
    return content[3:end], content[end + 3:].lstrip()


def parse_frontmatter(content: str, source: Path) -> str:
    """Strip YAML frontmatter and return the body.

    Exits with a clear message if the frontmatter is malformed so callers
    don't have to handle the error themselves.
    """
    if not content.startswith("---"):
        return content
    parts = split_frontmatter(content)
    if parts is None:
        sys.exit(
            f"{source}: frontmatter is missing its closing ---.\n"
            f"Run 'uv run tests/validate_structure.py' to diagnose."
        )
    return parts[1]
