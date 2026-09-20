from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "estimate_tokens.py"
SPEC = importlib.util.spec_from_file_location("estimate_tokens", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class EstimateTokensTests(unittest.TestCase):
    def test_token_range_uses_documented_bounds(self) -> None:
        self.assertEqual(MODULE.token_range(0), MODULE.TokenRange(0, 0))
        self.assertEqual(MODULE.token_range(15), MODULE.TokenRange(3, 5))
        self.assertEqual(MODULE.token_range(16), MODULE.TokenRange(4, 6))

    def test_join_parts_avoids_empty_separators(self) -> None:
        self.assertEqual(MODULE.join_parts(["task", "", "context"]), "task\ncontext")

    def test_reduction_is_never_negative(self) -> None:
        result = MODULE.estimate("short", [], "a much longer refined prompt", [])
        self.assertEqual(result.reduction_tokens.lower, 0)
        self.assertEqual(result.reduction_percent[0], 0.0)
        self.assertEqual(result.qualitative_saving, "none")
        self.assertGreater(result.added_tokens.lower, 0)
        self.assertIn("no first-call savings—task is small", result.impact)
        self.assertIn("adds about", result.impact)

    def test_large_context_removal_reports_saving(self) -> None:
        result = MODULE.estimate("fix bug", ["x" * 1000], "fix the named bug and run its focused test", [])
        self.assertGreater(result.reduction_tokens.lower, 0)
        self.assertIn(result.qualitative_saving, {"high", "very high"})

    def test_moderate_reduction_is_not_erased_by_crossed_bounds(self) -> None:
        result = MODULE.estimate("x" * 250, [], "x" * 170, [])
        self.assertEqual(result.removed_characters, 80)
        self.assertEqual(result.added_characters, 0)
        self.assertGreater(result.reduction_percent[0], 0)
        self.assertEqual(result.qualitative_saving, "moderate")
        self.assertTrue(result.impact.startswith("save about"))

    def test_retained_context_counts_toward_optimized_input(self) -> None:
        result = MODULE.estimate("task", ["needed"], "refined", ["needed"])
        self.assertEqual(result.optimized_characters, len("refined\nneeded"))

    def test_equal_length_reports_neutral_impact(self) -> None:
        result = MODULE.estimate("same", [], "same", [])
        self.assertEqual(result.impact, "about the same; no meaningful first-call saving")
        self.assertEqual(result.added_tokens, MODULE.TokenRange(0, 0))

    def test_negative_character_count_rejected(self) -> None:
        with self.assertRaises(ValueError):
            MODULE.token_range(-1)

    def test_context_fields_must_be_string_lists(self) -> None:
        self.assertEqual(MODULE.string_list(["one", "two"], "context"), ["one", "two"])
        for invalid in ("one", {"one": 1}, ["one", 2], None):
            with self.subTest(invalid=invalid):
                with self.assertRaises(ValueError):
                    MODULE.string_list(invalid, "context")

    def test_ambiguity_scenarios_are_not_claimed_as_achieved(self) -> None:
        optimized = MODULE.TokenRange(lower=20, upper=34)
        medium = MODULE.session_scenario(optimized, "medium", "ordinary_text")
        self.assertEqual(medium.avoided_calls, (0, 1))
        self.assertEqual(medium.repeated_input_tokens_avoided, MODULE.TokenRange(0, 34))
        self.assertEqual(medium.potential_water_ml, (0.0, 2.0))
        self.assertFalse(medium.achieved_savings)

        high = MODULE.session_scenario(optimized, "high", "long_or_reasoning")
        self.assertEqual(high.avoided_calls, (1, 2))
        self.assertEqual(high.repeated_input_tokens_avoided, MODULE.TokenRange(20, 68))
        self.assertEqual(high.potential_water_ml, (2.0, 300.0))
        self.assertTrue(high.upper_is_open_ended)

    def test_invalid_ambiguity_and_call_ranges_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            MODULE.ambiguity_call_range("extreme")
        for invalid in ([2, 1], [-1, 1], [1], [0, "1"], "0,1"):
            with self.subTest(invalid=invalid):
                with self.assertRaises(ValueError):
                    MODULE.avoided_call_range(invalid)

    def test_exclusions_are_explicit(self) -> None:
        result = MODULE.estimate("task", [], "task", [])
        self.assertEqual(
            set(result.not_measured),
            {"output tokens", "retries", "latency", "cost", "model energy", "carbon", "water"},
        )


if __name__ == "__main__":
    unittest.main()
