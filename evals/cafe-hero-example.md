# Example: Garlic and Sauce Cafe Hero

This is a format-calibration example for the benchmark case. It is not evidence that the skill was executed.

# AAWF Recommendation

## Quick answer

- **Difficulty:** Easy
- **Use this model:** `gpt-5.6-terra`
- **Reasoning:** medium
- **Best approach:** Build it directly, then inspect the rendered desktop and mobile result
- **Use these tools:** `impeccable-design` and a browser/render preview
- **Sub-agents:** No
- **Estimated first-call token impact:** No first-call savings—this task is small; the clearer prompt adds about 51–85 input tokens

This setup is sufficient because the task is one small visual component with a straightforward render check.

## Your execution recipe

1. Build the hero with `impeccable-design` using one deliberate visual direction.
2. Render it at desktop and mobile sizes.
3. Fix only visible layout, contrast, or interaction problems found in that check.

- **Done when:** the hero renders correctly at both sizes and its main action is clear.

## Your setup

- **Platform:** Codex
- **Plan:** Not stated
- **Detected tools/skills:** `impeccable-design`
- **Model availability:** Confirmed from the benchmark's visible model list
- **Fallback model:** `gpt-5.6-sol`

## What I understood

- **Goal:** Build a visually distinctive hero for a cafe named Garlic and Sauce.
- **Output:** A responsive website hero implemented in the current project.
- **Must keep:** The cafe name and use of `impeccable-design`.
- **Assumptions:** The implementer may choose the visual direction and call to action, but must label those choices as assumptions.
- **Still unclear:** Nothing that blocks starting.

## Quality checks

- **Task mode:** Website or UI build
- **Check before delivery:** Desktop layout, mobile layout, readable contrast, and working calls to action
- **Likely failure to avoid:** Expanding a small hero request into an unnecessary full website

## Ready-to-use prompt

```text
Use impeccable-design to build and visually verify a responsive website hero for a cafe named Garlic and Sauce. Choose a distinctive cafe-appropriate visual direction and clear primary call to action; label any brand assumptions. Deliver the implementation in the current project and report the files changed and checks run.
```

## Context to use

- **Keep:** The `impeccable-design` skill and cafe name.
- **Optional:** Existing brand assets if they are available in the project.
- **Remove:** The `$aawf` invocation after this recommendation is produced.
- **Unsure:** None.

## Why this setup

- `gpt-5.6-terra` is the balanced creation model for a bounded UI build.
- Medium reasoning is enough to make deliberate design decisions without over-processing a small task.
- `impeccable-design` supplies the specialist design workflow, and the browser check verifies the visual result.
- One model can complete the single hero; sub-agents would add coordination and token cost.

## Token impact

- **Before:** 70 characters, approximately 14–24 input tokens.
- **After:** 324 characters, approximately 65–108 input tokens.
- **Difference:** 254 added characters, approximately 51–85 added input tokens.
- **Confidence:** Medium.
- **Assumptions:** English prose with no additional project context counted.
- **Not included:** Output tokens, retries, latency, cost, model energy, carbon, and water.

No first-call savings—this task is small. The refined prompt adds approximately 51–85 input tokens for clarity.

- **Possible session impact:** If the clearer prompt avoids one extra call, it could avoid roughly 65–108 repeated input tokens. This is a 0–1-call scenario, not achieved savings; output-token and cost impact remain unavailable.

## Sustainability impact

- **Water saving:** Not claimable from this example because no complete model call was observed to be avoided.
- **Illustrative scenario:** If one ordinary text call were avoided, research anchors suggest roughly 0.26–2 mL could potentially be avoided.
- **Confidence:** Low; provider, model, location, and cooling system are unknown.
- **Important:** This range is based on an avoided complete call, not the prompt's token difference.

## Technical details

- **Category:** Frontend design and implementation
- **Internal difficulty:** LIGHT
- **Risk:** low
- **Verification need:** medium
- **Internal strategy:** direct, supported by verification-first
- **Model capability tier:** standard
- **Confidence:** medium
- **Limits:** This calibration example was not executed. AAWF can execute in the current host, but it does not route providers or measure hidden reasoning tokens.
