#!/usr/bin/env python3
"""Transparent character-based input-token range estimator for AAWF Phase 1."""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Sequence


@dataclass(frozen=True)
class TokenRange:
    lower: int
    upper: int


@dataclass(frozen=True)
class Estimate:
    baseline_characters: int
    optimized_characters: int
    removed_characters: int
    added_characters: int
    baseline_tokens: TokenRange
    optimized_tokens: TokenRange
    reduction_tokens: TokenRange
    added_tokens: TokenRange
    reduction_percent: tuple[float, float]
    qualitative_saving: str
    impact: str
    method: str
    not_measured: tuple[str, ...]


@dataclass(frozen=True)
class SessionScenario:
    ambiguity: str
    avoided_calls: tuple[int, int]
    repeated_input_tokens_avoided: TokenRange
    water_profile: str
    potential_water_ml: tuple[float, float]
    upper_is_open_ended: bool
    achieved_savings: bool
    note: str


def token_range(characters: int) -> TokenRange:
    """Return broad language-agnostic bounds of one token per 3-5 characters."""
    if characters < 0:
        raise ValueError("character count cannot be negative")
    return TokenRange(lower=math.ceil(characters / 5), upper=math.ceil(characters / 3))


def join_parts(parts: Sequence[str]) -> str:
    """Join non-empty text parts exactly once with a newline separator."""
    return "\n".join(part for part in parts if part)


def estimate(
    original_task: str,
    supplied_context: Sequence[str],
    refined_prompt: str,
    retained_context: Sequence[str],
) -> Estimate:
    baseline_text = join_parts([original_task, *supplied_context])
    optimized_text = join_parts([refined_prompt, *retained_context])
    baseline = token_range(len(baseline_text))
    optimized = token_range(len(optimized_text))

    removed_characters = max(0, len(baseline_text) - len(optimized_text))
    added_characters = max(0, len(optimized_text) - len(baseline_text))
    reduction = token_range(removed_characters)
    added = token_range(added_characters)
    lower_percent = 0.0 if baseline.upper == 0 else reduction.lower / baseline.upper * 100
    upper_percent = 0.0 if baseline.lower == 0 else min(100.0, reduction.upper / baseline.lower * 100)
    conservative = min(lower_percent, upper_percent)

    if conservative < 1:
        qualitative = "none"
    elif conservative < 15:
        qualitative = "low"
    elif conservative < 35:
        qualitative = "moderate"
    elif conservative < 60:
        qualitative = "high"
    else:
        qualitative = "very high"

    if removed_characters:
        impact = f"save about {reduction.lower}-{reduction.upper} input tokens"
    elif added_characters:
        small_task = "—task is small" if len(baseline_text) < 400 else ""
        impact = (
            f"no first-call savings{small_task}; refined input adds about "
            f"{added.lower}-{added.upper} input tokens for clarity"
        )
    else:
        impact = "about the same; no meaningful first-call saving"

    return Estimate(
        baseline_characters=len(baseline_text),
        optimized_characters=len(optimized_text),
        removed_characters=removed_characters,
        added_characters=added_characters,
        baseline_tokens=baseline,
        optimized_tokens=optimized,
        reduction_tokens=reduction,
        added_tokens=added,
        reduction_percent=(round(lower_percent, 1), round(upper_percent, 1)),
        qualitative_saving=qualitative,
        impact=impact,
        method="character range: ceil(chars/5) to ceil(chars/3); reduction estimated from net removed characters",
        not_measured=(
            "output tokens",
            "retries",
            "latency",
            "cost",
            "model energy",
            "carbon",
            "water",
        ),
    )


def load_payload(path: Path) -> dict[str, object]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("input JSON must be an object")
    return data


def string_list(value: object, field: str) -> list[str]:
    """Validate a JSON array of strings without silently splitting a string."""
    if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
        raise ValueError(f"{field} must be an array of strings")
    return value


def ambiguity_call_range(level: str) -> tuple[int, int]:
    """Return a transparent avoided-extra-call scenario for an ambiguity level."""
    ranges = {"low": (0, 0), "medium": (0, 1), "high": (1, 2)}
    if level not in ranges:
        raise ValueError("ambiguity must be low, medium, or high")
    return ranges[level]


def avoided_call_range(value: object) -> tuple[int, int]:
    """Validate an explicit [lower, upper] avoided-call scenario."""
    if (
        not isinstance(value, list)
        or len(value) != 2
        or not all(isinstance(item, int) and not isinstance(item, bool) for item in value)
    ):
        raise ValueError("avoided_calls must be a two-item integer array")
    lower, upper = value
    if lower < 0 or upper < lower:
        raise ValueError("avoided_calls must satisfy 0 <= lower <= upper")
    return lower, upper


def session_scenario(
    optimized_tokens: TokenRange,
    ambiguity: str,
    workload: str = "unknown",
    calls: tuple[int, int] | None = None,
) -> SessionScenario:
    """Estimate repeated input and illustrative water for avoided complete calls."""
    call_range = calls if calls is not None else ambiguity_call_range(ambiguity)
    profiles = {
        "ordinary_text": (0.26, 2.0, False),
        "long_or_reasoning": (2.0, 150.0, True),
        "unknown": (0.26, 150.0, True),
    }
    if workload not in profiles:
        raise ValueError("workload must be ordinary_text, long_or_reasoning, or unknown")

    per_call_low, per_call_high, open_ended = profiles[workload]
    calls_low, calls_high = call_range
    return SessionScenario(
        ambiguity=ambiguity,
        avoided_calls=call_range,
        repeated_input_tokens_avoided=TokenRange(
            lower=optimized_tokens.lower * calls_low,
            upper=optimized_tokens.upper * calls_high,
        ),
        water_profile=workload,
        potential_water_ml=(
            round(per_call_low * calls_low, 2),
            round(per_call_high * calls_high, 2),
        ),
        upper_is_open_ended=open_ended and calls_high > 0,
        achieved_savings=False,
        note=(
            "scenario only: repeated input excludes output tokens; water range is research-anchored "
            "and applies only if complete model calls are actually avoided"
        ),
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="JSON input payload")
    parser.add_argument("--pretty", action="store_true", help="indent JSON output")
    args = parser.parse_args()

    payload = load_payload(args.input)
    result = estimate(
        original_task=str(payload.get("original_task", "")),
        supplied_context=string_list(payload.get("supplied_context", []), "supplied_context"),
        refined_prompt=str(payload.get("refined_prompt", "")),
        retained_context=string_list(payload.get("retained_context", []), "retained_context"),
    )
    output = asdict(result)
    if "ambiguity" in payload or "avoided_calls" in payload or "workload" in payload:
        ambiguity = str(payload.get("ambiguity", "low"))
        calls = avoided_call_range(payload["avoided_calls"]) if "avoided_calls" in payload else None
        output["possible_session_impact"] = asdict(
            session_scenario(
                optimized_tokens=result.optimized_tokens,
                ambiguity=ambiguity,
                workload=str(payload.get("workload", "unknown")),
                calls=calls,
            )
        )
    print(json.dumps(output, indent=2 if args.pretty else None))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
