from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "validate_benchmark.py"
BENCHMARK = Path(__file__).parents[1] / "evals" / "benchmark.jsonl"
SPEC = importlib.util.spec_from_file_location("validate_benchmark", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class BenchmarkTests(unittest.TestCase):
    def test_pack_is_structurally_valid(self) -> None:
        cases = MODULE.load_cases(BENCHMARK)
        self.assertEqual(MODULE.validate(cases), [])

    def test_every_case_has_intent_and_estimate_guards(self) -> None:
        cases = MODULE.load_cases(BENCHMARK)
        for case in cases:
            invariants = case["expected"]["critical_invariants"]
            joined = " ".join(invariants).lower()
            self.assertIn("intent", joined, case["id"])
            self.assertTrue("estimate" in joined or "token" in joined, case["id"])

    def test_cafe_case_covers_plain_model_and_tool_selection(self) -> None:
        cases = MODULE.load_cases(BENCHMARK)
        case = next(item for item in cases if item["id"] == "coding-05")
        self.assertEqual(case["setup"]["tools"], ["impeccable-design"])
        self.assertEqual(case["expected"]["model_name"], "gpt-5.6-terra")
        self.assertEqual(case["expected"]["reasoning"], "medium")

    def test_plain_language_contract_and_model_selector_exist(self) -> None:
        root = Path(__file__).parents[1]
        contract = (root / "references" / "output-contract.md").read_text(encoding="utf-8")
        selector = (root / "references" / "model-selector.md").read_text(encoding="utf-8")
        playbooks = (root / "references" / "workflow-playbooks.md").read_text(encoding="utf-8")
        for phrase in ("Quick answer", "Use this model", "Your setup", "Token impact", "Technical details"):
            self.assertIn(phrase, contract)
        self.assertIn("Compact run-mode record", contract)
        self.assertIn("No water saving can be claimed", contract)
        for phrase in ("Your execution recipe", "Done when", "Quality checks"):
            self.assertIn(phrase, contract)
        for platform in ("ChatGPT", "Codex", "Claude", "Gemini", "Ollama", "OpenRouter"):
            self.assertIn(platform, selector)
        self.assertIn("Which AI tool are you using", selector)
        self.assertIn("Do not default to GPT", selector)
        for mode in ("Website or UI build", "Coding change", "Debugging", "Research", "Writing", "Routine task"):
            self.assertIn(mode, playbooks)

    def test_benchmark_covers_multiple_platforms_and_setup_gate(self) -> None:
        cases = MODULE.load_cases(BENCHMARK)
        platforms = {case.get("setup", {}).get("platform") for case in cases}
        self.assertTrue({"Codex", "Claude", "Gemini", "Ollama", "OpenRouter"} <= platforms)
        setup_case = next(item for item in cases if item["id"] == "research-05")
        self.assertTrue(setup_case["expected"]["setup_required"])

    def test_free_and_plus_plans_use_different_visible_model_pools(self) -> None:
        cases = MODULE.load_cases(BENCHMARK)
        free_case = next(item for item in cases if item["id"] == "writing-01")
        plus_case = next(item for item in cases if item["id"] == "writing-02")
        self.assertEqual(free_case["setup"]["plan"], "Free")
        self.assertEqual(plus_case["setup"]["plan"], "Plus")
        self.assertEqual(free_case["available_models"], ["chat-fast"])
        self.assertEqual(plus_case["available_models"], ["chat-fast", "chat-balanced"])
        self.assertEqual(free_case["expected"]["model_name"], "chat-fast")
        self.assertEqual(plus_case["expected"]["model_name"], "chat-balanced")

    def test_core_rules_are_consistent_and_preserve_existing_features(self) -> None:
        root = Path(__file__).parents[1]
        skill = (root / "SKILL.md").read_text(encoding="utf-8")
        rubric = (root / "references" / "decision-rubric.md").read_text(encoding="utf-8")
        selector = (root / "references" / "model-selector.md").read_text(encoding="utf-8")
        contract = (root / "references" / "output-contract.md").read_text(encoding="utf-8")
        sustainability = (root / "references" / "sustainability-method.md").read_text(encoding="utf-8")
        combined = "\n".join((skill, rubric, selector, contract)).lower()

        self.assertNotIn("make a direct recommendation but label availability as unconfirmed", combined)
        self.assertIn("do not name an unconfirmed model", combined)
        self.assertIn("intent ledger", combined)
        self.assertIn("counterfactual test", combined)
        self.assertIn("independent outputs", combined)
        self.assertIn("lean execution protocol", combined)
        self.assertIn("no first-call savings", combined)
        self.assertIn("water saving: not claimable", combined)
        self.assertIn("0.26 ml", sustainability.lower())
        self.assertIn("150 ml", sustainability.lower())
        self.assertIn("not universal conversion factors", sustainability.lower())

        for existing_heading in (
            "Quick answer",
            "Your execution recipe",
            "Your setup",
            "What I understood",
            "Quality checks",
            "Ready-to-use prompt",
            "Context to use",
            "Why this setup",
            "Token impact",
            "Sustainability impact",
            "Technical details",
        ):
            self.assertIn(existing_heading, contract)


if __name__ == "__main__":
    unittest.main()
