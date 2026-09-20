# AAWF Phase 1 Decision Rubric

Use this rubric to calibrate recommendations. It guides judgment; it is not a claim that task quality can be reduced to one score.

## Complexity and difficulty

Score each complexity factor from 0 to 2:

| Factor | 0 | 1 | 2 |
|---|---|---|---|
| Breadth | one bounded result | several related parts | multiple systems or deliverables |
| Coupling | independent/simple | some dependencies | tightly coupled decisions |
| Uncertainty | known path | investigation needed | major unknowns or novel work |
| Context burden | little context | selective reading | large, noisy, or conflicting context |
| Verification | obvious check | several checks | difficult or multi-layer evidence |

Suggested mapping: 0–2 `Easy (LIGHT)`, 3–5 `Moderate (MEDIUM)`, 6–8 `Hard (HARD)`, 9–10 `Very hard (CRITICAL)`. Use the score as a calibration aid, not arithmetic theatre. Adjust by one tier only when an observable feature is poorly represented by the factors, and name that feature. When a task sits on a boundary, prefer the lower tier unless the higher tier changes the recommended workflow or model.

## Risk is separate

Risk measures consequence if the eventual task is done incorrectly:

- `low`: easily reversible, personal, or informational
- `medium`: meaningful rework, reputation, or shared-system effect
- `high`: security, privacy, legal, medical, financial, production, or destructive consequences
- `critical`: credible severe or irreversible harm

Risk changes verification and approval advice. It does not automatically change difficulty. For example, deleting one production record can be technically LIGHT and risk HIGH.

## Strategy selection

| Signal | Primary strategy |
|---|---|
| narrow task, clear input and check | direct |
| question depends on finding a cause or interpreting evidence | focused analysis |
| useful evidence is buried in large context | context-first |
| several dependent decisions must be resolved before work | plan-first |
| correctness or consequence dominates | verification-first |
| two or more independent work products can be combined cheaply | selective decomposition |

Prefer one primary strategy. Add a supporting strategy only when it changes the workflow materially.

## Model choice and tier

- `low`: LIGHT, low-risk, well-specified transformation or extraction
- `standard`: LIGHT/MEDIUM work needing reliable instruction following or modest analysis
- `high`: HARD work, substantial ambiguity, difficult synthesis, or demanding verification design
- `maximum`: CRITICAL complexity where the strongest available reasoning is justified

Use the lowest sufficient tier. Risk can require independent verification even when generation stays on a lower tier. Select the exact model through [model-selector.md](model-selector.md). If availability is not visible or supplied, use the setup gate and do not name an unconfirmed model. If the user explicitly chooses the current host model, proceed without fabricating its name or capabilities.

## Context decisions

- `keep`: necessary to preserve intent, ground facts, satisfy constraints, or verify the result
- `optional`: useful background whose absence should not block a good result
- `remove`: duplicated, unrelated, stale, superseded, or decorative material
- `unsure`: relevance depends on an unresolved interpretation

Use a counterfactual test: if removing an item could change the intended result or the evidence used to judge it, it is not removable. Do not mark inseparable mixed context as removable. Mark it unsure and recommend extracting the relevant portion.

## Sub-agent gate

Recommend sub-agents only when all are true:

1. At least two workstreams can proceed without sharing evolving state.
2. Each workstream has a clear, independently checkable output.
3. Merging outputs is cheaper than doing the work serially.
4. Expected quality or elapsed-time gain exceeds added prompts, duplicated context, and coordination.

Default to no for short tasks, sequential debugging, tightly coupled architecture, single-document editing, and work where every branch needs the same large context.

The recommendation must name the independent outputs and how they would be merged. If that explanation is not concrete, recommend no sub-agents.

## Confidence

- `high`: task, context boundaries, and model catalog are explicit
- `medium`: recommendation is stable but some assumptions remain
- `low`: missing goals, inseparable context, unavailable model information, or major uncertainty could change the recommendation
