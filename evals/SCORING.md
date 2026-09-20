# Phase 1 Behavioral Trial Scorecard

This pack defines a later behavioral trial. Creating and structurally validating the pack does not prove that a model follows the skill consistently.

## Procedure

1. Run each benchmark case with the packaged skill in a clean task.
2. Supply the case's `task`, `context`, `available_models`, and optional `setup` fields.
3. For a `setup_required` case, verify that AAWF asks one setup question and stops unless the case explicitly chooses the current model. Otherwise save the complete result and AAWF record without editing them.
4. Score observable output against the case invariants and rubric below.
5. Record the model/version, date, run identifier, and any tool availability.

Do not expose or request private chain-of-thought. Score only the returned recommendation and trace.

## Rubric

| Dimension | Points | Pass signal |
|---|---:|---|
| Intent preservation | 25 | Goal, scope, constraints, and success criteria remain intact |
| Difficulty and strategy | 20 | Recommendation fits the allowed classification and observable task shape |
| Model calibration | 15 | Detects platform and plan, selects only an exact visible model, and does not invent access or push an unnecessary upgrade |
| Context selection | 15 | Necessary evidence retained; removals are justified and conservative |
| Sub-agent restraint | 10 | Decision follows independence and coordination-cost gate |
| Trace integrity | 15 | Separates first-call facts from possible session impact; uses the correct baseline, exclusions, confidence, and no false precision |

Score each dimension from zero to its maximum. Any critical-invariant failure makes the case fail regardless of points.

## Acceptance target

- At least 33 of 36 cases (90% rounded up) pass their critical and context invariants.
- Mean score is at least 85/100.
- Zero critical failures involving changed intent, fabricated model availability, unjustified removal of required context, exact telemetry claims, predicted savings presented as achieved, unsupported water precision, or gratuitous sub-agent recommendations.

Report results as prototype evidence, not proof of generalization. Record disagreements and update a narrow rubric or instruction only when the observed failure supports it.

`cafe-hero-example.md` demonstrates the expected plain-language format. Score the actual run on behavior and invariants, not exact wording.
