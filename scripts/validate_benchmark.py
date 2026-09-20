#!/usr/bin/env python3
"""Validate the structure and coverage of the AAWF Phase 1 benchmark."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path


REQUIRED_FIELDS = {
    "id",
    "category",
    "title",
    "task",
    "context",
    "available_models",
    "tags",
    "expected",
}
EXPECTED_FIELDS = {
    "difficulty",
    "risk",
    "allowed_strategies",
    "model_tier",
    "sub_agents",
    "context_invariants",
    "critical_invariants",
}
VALID_CATEGORIES = {"coding", "debugging", "research", "writing", "architecture", "routine_execution"}
VALID_DIFFICULTIES = {"LIGHT", "MEDIUM", "HARD", "CRITICAL"}
VALID_RISKS = {"low", "medium", "high", "critical"}
VALID_TIERS = {"low", "standard", "high", "maximum"}
VALID_SUB_AGENTS = {"No", "Yes", "Uncertain"}
VALID_STRATEGIES = {
    "direct",
    "focused analysis",
    "context-first",
    "plan-first",
    "verification-first",
    "selective decomposition",
}


def load_cases(path: Path) -> list[dict[str, object]]:
    cases: list[dict[str, object]] = []
    for line_number, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not raw.strip():
            continue
        try:
            value = json.loads(raw)
        except json.JSONDecodeError as exc:
            raise ValueError(f"line {line_number}: invalid JSON: {exc}") from exc
        if not isinstance(value, dict):
            raise ValueError(f"line {line_number}: case must be an object")
        cases.append(value)
    return cases


def validate(cases: list[dict[str, object]]) -> list[str]:
    errors: list[str] = []
    ids: set[str] = set()
    categories: Counter[str] = Counter()

    if len(cases) != 36:
        errors.append(f"expected 36 cases, found {len(cases)}")

    for index, case in enumerate(cases, start=1):
        label = str(case.get("id", f"line-{index}"))
        missing = REQUIRED_FIELDS - case.keys()
        if missing:
            errors.append(f"{label}: missing fields {sorted(missing)}")
            continue
        if label in ids:
            errors.append(f"{label}: duplicate id")
        ids.add(label)

        category = str(case["category"])
        categories[category] += 1
        if category not in VALID_CATEGORIES:
            errors.append(f"{label}: invalid category {category!r}")

        if not isinstance(case["context"], list) or not isinstance(case["available_models"], list):
            errors.append(f"{label}: context and available_models must be arrays")
        if not isinstance(case["tags"], list):
            errors.append(f"{label}: tags must be an array")

        expected = case["expected"]
        if not isinstance(expected, dict):
            errors.append(f"{label}: expected must be an object")
            continue
        missing_expected = EXPECTED_FIELDS - expected.keys()
        if missing_expected:
            errors.append(f"{label}: missing expected fields {sorted(missing_expected)}")
            continue
        if expected["difficulty"] not in VALID_DIFFICULTIES:
            errors.append(f"{label}: invalid difficulty")
        if expected["risk"] not in VALID_RISKS:
            errors.append(f"{label}: invalid risk")
        if expected["model_tier"] not in VALID_TIERS:
            errors.append(f"{label}: invalid model tier")
        if expected["sub_agents"] not in VALID_SUB_AGENTS:
            errors.append(f"{label}: invalid sub-agent decision")
        strategies = expected["allowed_strategies"]
        if not isinstance(strategies, list) or not strategies or not set(strategies) <= VALID_STRATEGIES:
            errors.append(f"{label}: invalid allowed_strategies")
        for field in ("context_invariants", "critical_invariants"):
            values = expected[field]
            if not isinstance(values, list) or not values or not all(isinstance(item, str) and item for item in values):
                errors.append(f"{label}: {field} must be a non-empty string array")

    expected_distribution = {category: 6 for category in VALID_CATEGORIES}
    if dict(categories) != expected_distribution:
        errors.append(f"category distribution must be six each; found {dict(categories)}")

    required_adversarial_tags = {
        "ambiguous",
        "simple-high-risk",
        "unavailable-model",
        "inseparable-context",
        "cannot-shorten",
        "decomposition-overhead",
    }
    seen_tags = {str(tag) for case in cases for tag in case.get("tags", [])}
    missing_tags = required_adversarial_tags - seen_tags
    if missing_tags:
        errors.append(f"missing adversarial tags {sorted(missing_tags)}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("benchmark", type=Path)
    args = parser.parse_args()
    cases = load_cases(args.benchmark)
    errors = validate(cases)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("Benchmark valid: 36 cases, six categories, required adversarial coverage present.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

