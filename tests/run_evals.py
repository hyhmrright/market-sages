#!/usr/bin/env python3
"""
Prompt evaluation runner for market-sages.
Loads YAML fixtures, invokes Claude API with skill.md as system prompt,
and checks assertions against the response.

Requirements:
    pip install anthropic pyyaml   (Python 3.10+)

Usage:
    export ANTHROPIC_API_KEY=sk-...
    python3 tests/run_evals.py                     # run all fixtures
    python3 tests/run_evals.py nvda_full_data      # run one fixture by id
    python3 tests/run_evals.py --dry-run           # print prompts, skip API calls
"""
import argparse
import re
import sys

if sys.version_info < (3, 10):
    sys.exit("Python 3.10+ required. Current: {}.{}.{}".format(*sys.version_info[:3]))

from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

try:
    import anthropic
    import yaml
except ImportError:
    sys.exit("Missing dependencies. Run: pip install anthropic pyyaml")

from utils import parse_frontmatter

FIXTURES_DIR = Path("tests/fixtures")
SKILL_FILE = Path("skill.md")
MODEL = "claude-haiku-4-5-20251001"  # fast + cheap for evals

# Known keys per assertion type — used to catch typos early.
_SAGE_ASSERTION_KEYS = {"sage", "expected_signal", "forbidden_signal", "rationale", "description"}
_TEXT_ASSERTION_KEYS = {"type", "value", "description"}

_CONTAINS_TEXT = "contains_text"
_NOT_CONTAINS_TEXT = "not_contains_text"


# ── Fixture loading ────────────────────────────────────────────────────────────

def load_skill_prompt() -> str:
    """Read skill.md and strip YAML frontmatter."""
    return parse_frontmatter(SKILL_FILE.read_text(), SKILL_FILE)


def load_fixtures(filter_id: str | None) -> list[dict]:
    fixtures = []
    for path in sorted(FIXTURES_DIR.glob("*.yaml")):
        data = yaml.safe_load(path.read_text())
        if filter_id and data.get("id") != filter_id:
            continue
        fixtures.append(data)
    return fixtures


# ── Assertion checking ─────────────────────────────────────────────────────────
#
# Dispatch rule:
#   • Assertions with a "sage" key  → _check_sage_assertion()
#   • Assertions with a "type" key  → _check_text_assertion()
#   Any other combination is a fixture authoring error and fails immediately.

def _validate_assertion_keys(assertion: dict) -> str | None:
    """Return an error string if assertion contains unknown keys, else None."""
    if "sage" in assertion:
        unknown = set(assertion) - _SAGE_ASSERTION_KEYS
    else:
        unknown = set(assertion) - _TEXT_ASSERTION_KEYS
    if unknown:
        return f"Unknown assertion key(s): {sorted(unknown)} — possible typo in fixture"
    return None


def _sage_signal(response: str, sage_name: str) -> str | None:
    """Extract signal for a named sage from the response.

    Tolerates format variants:
    - Sage name may appear after 🧠 emoji or as a plain header
    - Label may be "Signal:" or "Verdict:" (future-proofing)
    """
    name_pattern = rf"(?:🧠\s*)?{re.escape(sage_name)}"
    signal_pattern = r"(?:Signal|Verdict):\s*(BULLISH|BEARISH|NEUTRAL)"
    combined = rf"{name_pattern}.{{0,500}}?{signal_pattern}"
    match = re.search(combined, response, re.IGNORECASE | re.DOTALL)
    return match.group(1).upper() if match else None


def _check_sage_assertion(assertion: dict, response: str) -> tuple[bool, str]:
    """Check an assertion that targets a named sage's signal direction."""
    sage = assertion["sage"]
    signal = _sage_signal(response, sage)
    if signal is None:
        return False, f"{sage}: signal not found in response"

    if "expected_signal" in assertion:
        expected = assertion["expected_signal"].upper()
        if signal != expected:
            rationale = assertion.get("rationale", "")
            return False, f"{sage}: expected {expected}, got {signal}. {rationale}"

    if "forbidden_signal" in assertion:
        forbidden = assertion["forbidden_signal"].upper()
        if signal == forbidden:
            return False, f"{sage}: must not be {forbidden}, got {signal}"

    return True, f"{sage}: {signal} ✓"


def _check_text_assertion(assertion: dict, response: str) -> tuple[bool, str]:
    """Check an assertion that searches for text presence or absence."""
    atype = assertion.get("type", "")
    value = assertion.get("value", "")
    desc = assertion.get("description", "")

    if atype == _CONTAINS_TEXT:
        if value.lower() in response.lower():
            return True, f"contains '{value}' ✓"
        return False, f"missing '{value}' — {desc}"

    if atype == _NOT_CONTAINS_TEXT:
        if value.lower() not in response.lower():
            return True, f"correctly excludes '{value}' ✓"
        return False, f"found '{value}' but should be absent — {desc}"

    return False, f"unknown assertion type '{atype}'"


def check_assertion(assertion: dict, response: str) -> tuple[bool, str]:
    """Dispatch to the appropriate assertion checker.

    Sage assertions (key: 'sage') and text assertions (key: 'type') are
    handled by separate functions. Unknown keys fail immediately with a
    clear error so fixture typos are caught before they silently pass.
    """
    key_error = _validate_assertion_keys(assertion)
    if key_error:
        return False, key_error

    if "sage" in assertion:
        return _check_sage_assertion(assertion, response)
    return _check_text_assertion(assertion, response)


# ── Runner ─────────────────────────────────────────────────────────────────────

def _call_api(fixture: dict, system_prompt: str, client: "anthropic.Anthropic") -> str:
    """Call the Claude API and return the response text."""
    response = client.messages.create(
        model=MODEL,
        max_tokens=4096,
        system=system_prompt,
        messages=[{"role": "user", "content": fixture["user_message"]}],
    )
    return response.content[0].text


def run_fixture(
    fixture: dict,
    system_prompt: str,
    client: "anthropic.Anthropic | None",
    dry_run: bool,
) -> tuple[str, bool, list[tuple[bool, str]]]:
    """Run a single fixture and return (fixture_id, all_passed, assertion_results)."""
    if dry_run:
        return fixture["id"], True, []

    text = _call_api(fixture, system_prompt, client)  # type: ignore[arg-type]
    results = [check_assertion(a, text) for a in fixture.get("assertions", [])]
    all_passed = all(ok for ok, _ in results)
    return fixture["id"], all_passed, results


def _print_fixture_result(
    fixture: dict,
    all_passed: bool,
    results: list[tuple[bool, str]],
    dry_run: bool,
) -> None:
    fid = fixture["id"]
    desc = fixture.get("description", "").strip().replace("\n", " ")
    print(f"\n{'─' * 60}")
    print(f"Fixture: {fid}")
    print(f"  {desc[:100]}")

    if dry_run:
        print(f"  [dry-run] user_message: {fixture['user_message'][:80]}...")
        return

    passed = sum(1 for ok, _ in results if ok)
    failed = len(results) - passed
    for ok, msg in results:
        print(f"  {'✅' if ok else '❌'} {msg}")
    print(f"  Result: {passed} passed, {failed} failed")


def main() -> None:
    parser = argparse.ArgumentParser(description="Market Sages prompt eval runner")
    parser.add_argument("fixture_id", nargs="?", help="Run a single fixture by id")
    parser.add_argument("--dry-run", action="store_true", help="Skip API calls")
    args = parser.parse_args()

    system_prompt = load_skill_prompt()
    fixtures = load_fixtures(args.fixture_id)

    if not fixtures:
        target = f"'{args.fixture_id}'" if args.fixture_id else "any"
        print(f"No fixtures found matching {target}")
        sys.exit(1)

    client = anthropic.Anthropic() if not args.dry_run else None

    # Map fixture id → fixture dict for ordered printing after parallel execution
    fixture_map = {f["id"]: f for f in fixtures}
    outcome: dict[str, tuple[bool, list[tuple[bool, str]]]] = {}

    with ThreadPoolExecutor(max_workers=len(fixtures)) as pool:
        futures = {
            pool.submit(run_fixture, f, system_prompt, client, args.dry_run): f["id"]
            for f in fixtures
        }
        for future in as_completed(futures):
            fid, all_passed, results = future.result()
            outcome[fid] = (all_passed, results)

    # Print in deterministic fixture order
    all_passed_overall = True
    for fixture in fixtures:
        fid = fixture["id"]
        passed, results = outcome[fid]
        _print_fixture_result(fixture, passed, results, args.dry_run)
        if not passed:
            all_passed_overall = False

    print(f"\n{'═' * 60}")
    if all_passed_overall:
        print(f"✅ All {len(fixtures)} fixture(s) passed")
    else:
        print("❌ Some fixtures failed")
        sys.exit(1)


if __name__ == "__main__":
    main()
