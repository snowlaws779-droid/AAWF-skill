# AAWF Task and Verification Rubric

Use this only when a task's complexity or risk is unclear. It is a guide to the current host's workflow, **not** a model-selection system or an invitation to spawn agents.

## Task difficulty

Assess breadth, coupling, uncertainty, context burden and verification needs (0=low, 1=moderate, 2=high). Rough calibration: 0–2 easy, 3–5 moderate, 6–8 hard, 9–10 very hard. Do not expose scores unless useful to explain a decision.

## Consequence risk

Risk is separate from difficulty:
- **Low:** easy to reverse or verify.
- **Medium:** meaningful rework or shared impact.
- **High:** privacy, security, financial, destructive, or other substantial consequences.
- **Critical:** severe or irreversible consequences.

Higher consequence can require stronger confirmation and objective checks without altering the host's model or its settings.

## Workflow

- Clear bounded task → **do directly**.
- Unclear failure/evidence → **diagnose first**.
- Large/noisy supplied context → **select context first**.
- Dependent subtasks → **brief plan first**.
- Serious correctness risk → **define checks first**.

Do not generate role-based simulated agents or launch sub-agents. Simple plans with steps are sufficient for coupled work.

## Context selection

- **Required:** facts, constraints, source grounding, permissions, exclusions and verification evidence that must survive.
- **Optional:** background whose absence would not change the expected result.
- **Duplicate:** repeated optional text, where preserving one instance retains meaning and provenance.
- **Uncertain:** evidence that might change the result; preserve until the ambiguity is resolved.

Use a counterfactual check: if removing text can materially change correctness, constraints, or source attribution, do not remove it.

## Confidence

- **High:** requirements and evidence boundaries are clear.
- **Medium:** minor assumptions remain but action is reasonable.
- **Low:** goal, source interpretation, or critical requirements are unresolved; ask one focused question if necessary.

No part of this rubric recommends models, reasoning levels, subscriptions, fallback providers, or new agents.
