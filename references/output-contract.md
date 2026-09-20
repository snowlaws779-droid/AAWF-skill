# AAWF Phase 1 Output Contract

Write for a person who does not know AI workflow terminology. Prefer short sentences and ordinary words. Do not repeat the same reason in several sections.

In run mode, complete the requested task first and append the compact AAWF record afterward. Do not spend a long preamble describing work that is about to happen. In advice-only mode, use every heading below in order.

## Compact run-mode record

After the completed task, show only:

### AAWF summary

- **Setup:** difficulty, model or `Current host model`, reasoning level, approach, and useful tools
- **Verified:** the checks actually completed, or `Not verified` with the reason
- **First-call tokens:** saved range, `About the same`, or the required `No first-call savings` wording
- **Possible session impact:** avoided-call input range, clearly labelled as a scenario; omit when ambiguity is low
- **Sustainability:** provider telemetry, an illustrative avoided-call water range, or `No water saving can be claimed`
- **Limits:** only material unknowns

Use one short line per item. Do not repeat the refined prompt, context list, execution recipe, or technical tiers after the task unless the user asks for the full record.

## Setup gate

Before naming a model, detect the AI platform and its usable model list. If either cannot be determined, ask the single setup question from `model-selector.md`. The user may answer `use the current model`; proceed without inventing its exact name.

# AAWF Recommendation

## Quick answer

- **Difficulty:** `Easy`, `Moderate`, `Hard`, or `Very hard`
- **Use this model:** one exact model name
- **Reasoning/thinking:** the platform's exact visible control, or a plain recommendation such as `standard thinking`
- **Best approach:** a plain-language action such as `Build directly, then check the rendered result`
- **Use these tools:** exact useful tools or skills, or `No special tool needed`
- **Sub-agents:** `No`, `Yes—N independent parts`, or `Uncertain`
- **Estimated first-call token impact:** one of:
  - `Save about X–Y input tokens (A–B%)`
  - `No first-call savings—this task is small; the refined prompt adds about X–Y input tokens for clarity`
  - `About the same; no meaningful first-call saving`

Do not lead with internal terms such as strategy codes or model tiers.

Keep this section to the listed lines. Explain the main reason in one additional sentence at most.

## Your execution recipe

In advice-only mode, give no more than three numbered, task-specific steps. In run mode, state the no-more-than-three major steps actually used. Each step must describe a concrete action; do not write generic advice such as “think carefully.” Include only checks appropriate to the selected task mode.

End with:

- **Done when:** one observable completion condition.

Examples of appropriate checks:

- Website or UI build: render at desktop and mobile sizes; check readable contrast, links, and layout overflow.
- Coding change: run the smallest relevant test, build, or lint check; state the fallback if no test exists.
- Debugging: reproduce the problem, change one supported cause, then verify the original failure is gone.
- Research: use credible sources, distinguish facts from inference, and cite the claims that matter.
- Writing: check audience, requested format, factual claims, and word or length constraints.

Do not imply that AAWF ran these steps. They are a recommended workflow for the host AI or person to follow.

## Your setup

- **AI platform:** observed or user-supplied value
- **Plan:** observed value or `Not stated`
- **Available models:** exact visible or user-supplied names
- **Plan impact:** one plain sentence explaining how access affects the recommendation, or `Plan not needed because the model list is visible`
- **Detected task tools/skills:** exact names or `None stated`
- **Model availability:** `Confirmed from host list`, `Visible model picker`, or `Stated by user`
- **Fallback model:** another exact available model, or `None available`

If the plan is unknown but the visible model list is known, proceed without asking for the plan.

Do not present remembered plan entitlements as current facts. If the plan name and visible list conflict, trust the visible list and mention that access may be account-specific or changing.

## What I understood

- **Goal:** one sentence
- **Output:** concrete artifact or answer
- **Must keep:** important supplied constraints
- **Assumptions:** only necessary, explicitly labeled assumptions
- **Still unclear:** unresolved decisions, or `Nothing that blocks starting`

Do not turn every unspecified design choice into a blocking ambiguity. If safe creative judgment is part of the task, state that the implementer may choose deliberately and label the assumption.

## Quality checks

- **Task mode:** one exact mode from the skill
- **Check before delivery:** two to four mode-specific checks
- **Likely failure to avoid:** one concrete failure mode, or `No unusual risk`

Do not invent a risk merely to fill the section.

## Ready-to-use prompt

Provide a fenced `text` block containing the compiled prompt. Preserve intent, named skills, constraints, and success criteria. Do not include the AAWF analysis itself in the prompt.

## Context to use

Use short bullets instead of a table:

- **Keep:** necessary context, or `Only the task itself`
- **Optional:** helpful but nonessential context, or `None`
- **Remove:** duplicated, stale, unrelated, or control-only text, or `None`
- **Unsure:** context whose relevance depends on an unresolved choice, or `None`

Do not reproduce large or sensitive context. Identify it by a short neutral label.

## Why this setup

Give two to four short reasons covering the model, strategy, tools, and sub-agent decision. Translate strategies into plain language:

- `direct` → `Do it directly`
- `focused analysis` → `Diagnose first`
- `context-first` → `Choose the useful context first`
- `plan-first` → `Plan the dependent steps first`
- `verification-first` → `Define and run the checks`
- `selective decomposition` → `Split only independent parts`

## Token impact

Lead with the plain result from the quick answer, then report:

- **Before:** original task plus all supplied context, with character count and estimated input-token range
- **After:** refined prompt plus retained context, with character count and estimated input-token range
- **Difference:** saved or added character count, estimated token range, and conservative percentage range
- **Confidence:** `low`, `medium`, or `high`
- **Assumptions:** language/content mix and what counts as context
- **Not included:** output tokens, retries, latency, cost, model energy, carbon, and water

When the refined prompt is longer and the original task is short, use this wording:

`No first-call savings—this task is small; the refined prompt adds about X–Y input tokens for clarity.`

For a larger task, omit `this task is small` and keep the rest of the statement honest.

Then, only when credible, add a separate ambiguity scenario:

`Possible session impact: avoiding N extra call(s) could avoid approximately X–Y repeated input tokens. Output-token and cost savings are unavailable.`

For a range of possible calls, label the result `potential`, never `saved`. A vague prompt does not itself consume more first-call input tokens; uncertainty may increase total session usage through clarification or rework.

Use these transparent bounds when the script cannot run:

- lower token estimate = ceiling(characters / 5)
- upper token estimate = ceiling(characters / 3)
- removed characters = `max(0, baseline characters - optimized characters)`
- added characters = `max(0, optimized characters - baseline characters)`
- saved-token range = ceiling(removed characters / 5) through ceiling(removed characters / 3)
- added-token range = ceiling(added characters / 5) through ceiling(added characters / 3)
- conservative saved-percentage range = saved lower / baseline upper through saved upper / baseline lower, capped at 100%

If the refined input is longer, state how many estimated tokens it adds. Do not describe zero saving as a failure: explain briefly when the purpose is clarity or avoiding an unmeasured retry.

Qualitative saving bands use the conservative lower percentage: `none` below 1%, `low` from 1–14%, `moderate` from 15–34%, `high` from 35–59%, and `very high` from 60%.

This range assumes the removed and retained text have broadly similar token density. Lower confidence for mixed code, tables, formulas, or multilingual text.

## Sustainability impact

Follow [sustainability-method.md](sustainability-method.md).

- **Water saving:** provider telemetry, an illustrative avoided-call range, or `Not claimable`
- **Basis:** number and kind of complete calls avoided or forecast
- **Confidence:** `low` or `very low` for research-based scenarios; use the provider's confidence when telemetry supplies it
- **Important:** do not convert token differences directly into water saved

Use common language, for example: `No water saving can be claimed because no complete model call was shown to be avoided.`

## Technical details

Keep this compact while preserving evaluation quality:

- **Category:** precise task category
- **Internal difficulty:** `LIGHT`, `MEDIUM`, `HARD`, or `CRITICAL`
- **Risk:** `low`, `medium`, `high`, or `critical`
- **Verification need:** `low`, `medium`, or `high`
- **Internal strategy:** primary strategy and optional supporting strategy
- **Model capability tier:** `low`, `standard`, `high`, or `maximum`
- **Confidence:** `low`, `medium`, or `high`
- **Limits:** material uncertainty and the reminder that this is advice, not executed routing or measured provider telemetry

In run mode, replace the advice-only reminder with an exact boundary: AAWF executed inside the current host but did not route providers, switch models automatically, or measure hidden reasoning tokens.
