---
name: aawf
description: "Run an AI task through a lean, quality-preserving workflow: understand the request, choose the simplest sufficient approach and available model, compile the prompt, limit context and agent overhead, execute and verify in the current host when requested, and report honest token and sustainability estimates. Use only when explicitly invoked; never claim provider routing or telemetry that did not occur."
---

# AAWF Lean Workflow

Improve the task's result per unit of compute. By default, analyze briefly, execute the task in the current host, verify proportionately, and report a compact efficiency trace. If the user asks for advice only, stop after the recommendation and refined prompt.

AAWF may use the model and tools already available in the host. It does not automatically switch providers, purchase access, install tools, or create sub-agents. Recommend those actions without performing them unless the user separately authorizes them.

## Inputs

Accept ordinary language. Treat these as optional unless supplied:

- task and desired deliverable
- constraints and success criteria
- context items, files, or conversation history
- platform, subscription plan, and available model catalog
- named tools, skills, apps, or execution environment

If the goal or deliverable is too ambiguous to compile faithfully, preserve the ambiguity, identify the missing decision, and lower confidence. Do not invent requirements.

Before analysis, identify the AI platform separately from task tools. The platform is where the person will run the prompt, such as ChatGPT, Codex, Claude, Gemini, Ollama, OpenRouter, or another app. Task tools are skills, plugins, browsers, editors, or domain utilities used to complete the work.

If neither the AI platform nor its available model names can be determined from the host environment or the user's text, ask exactly one short setup question before making a model-specific claim:

`Which AI tool are you using, and which model names can you see in its model picker? If relevant, include your plan.`

If the platform is known but its model list is not visible, ask for the visible model names before selecting one. A plan name alone is not proof of model access. Do not silently substitute GPT defaults. If the user asked AAWF to run the task and model choice would not materially change safety or quality, the user may say `use the current model`; then proceed without inventing its exact name.

## First response rule

Use one of these two simple starts:

- **Ready:** when the platform and selectable models are known, choose the best sufficient exact model and run the lean workflow.
- **Setup:** when either is unknown, ask the single setup question above and wait, unless the user explicitly chooses the current model. Do not make the person complete a form or guess their plan.

If the person names a task tool (for example, a design skill, browser, editor, or plugin), acknowledge it separately from the AI platform and include it only when it helps complete the task.

## Advisory workflow

1. Extract the goal, deliverable, constraints, success criteria, and unresolved ambiguity.
2. Detect the user's platform, subscription plan, available models, task tools, skills, and apps. Use host metadata when exposed. Treat the visible model list as the source of truth and the plan as explanatory context. Never infer a paid plan or model entitlement from silence.
3. Assess category, complexity, uncertainty, context load, risk, and verification burden. Keep complexity and consequence risk separate.
4. Assign a plain-language difficulty with its stable internal tier.
5. Identify the task mode, then use its proportionate playbook from [references/workflow-playbooks.md](references/workflow-playbooks.md). Do not load or recite unrelated playbooks.
6. Choose one primary strategy and, only when useful, one supporting strategy.
7. Recommend one model directly, including reasoning level and a fallback. Use [references/model-selector.md](references/model-selector.md) for every analysis.
8. Compile a concise prompt that preserves the original intent and necessary details. Remove repetition and irrelevant material; add only constraints justified by the request.
9. Classify supplied context items as `keep`, `optional`, `remove`, or `unsure`. Never remove an item merely because it is large.
10. Recommend sub-agents only when the task has at least two genuinely independent workstreams and the likely quality or elapsed-time benefit exceeds coordination and extra-token cost. This is advice only; never spawn them.
11. Execute with the lean protocol below when the user requested the task itself, then run only the checks needed to establish success.
12. Check the recommendation and execution for internal consistency: the exact named model must be confirmed available; every must-keep requirement must survive in the refined prompt and result; every removed context item needs a concrete reason; and the token comparison must use the same before/after boundaries described to the user.
13. Produce the concise result from [references/output-contract.md](references/output-contract.md). Read that reference for every analysis.

Read [references/decision-rubric.md](references/decision-rubric.md) when the classification is borderline, risk is medium or higher, context is substantial, or sub-agents might be useful.

## Difficulty

- `Easy (LIGHT)`: narrow, familiar, low-uncertainty work with an obvious completion check.
- `Moderate (MEDIUM)`: several constraints or modest investigation, but limited coupling and a clear deliverable.
- `Hard (HARD)`: broad or coupled work, important uncertainty, substantial context selection, or demanding verification.
- `Very hard (CRITICAL)`: exceptional complexity with multiple tightly coupled systems or severe uncertainty. High consequence alone does not make a task very hard.

## Strategy vocabulary

- `direct`: perform one bounded operation with minimal planning.
- `focused analysis`: inspect a narrow question or failure before proposing action.
- `context-first`: identify and load only the evidence needed before solving.
- `plan-first`: resolve dependencies and acceptance criteria before implementation.
- `verification-first`: define evidence and checks before giving or changing the answer.
- `selective decomposition`: split only independent workstreams whose benefit exceeds coordination cost.

This is a deliberately small Phase 1 vocabulary, not the full future strategy library.

## Task modes

Classify the request as one of: `website or UI build`, `coding change`, `debugging`, `research`, `writing`, `architecture or decision`, or `routine task`. Use the selected mode to choose only the checks that materially reduce failure or rework.

The recommendation must feel actionable, not diagnostic. Give a short tailored execution recipe: at most three ordered steps, the appropriate quality checks, and a clear stopping condition. For example, a website needs an implementation and responsive render check; a research question needs source quality and citation checks; a small routine task usually needs neither a plan nor agents.

## Model advice

Recommend an exact model name, a reasoning level, and one fallback in plain language. Prefer the least expensive option likely to maintain quality.

Select only from exact models shown by the current platform, supplied by the user, or explicitly stated as included in their plan. If that information is unavailable, ask the setup question instead of guessing. Never hardcode Free, Plus, Pro, or other plan entitlements because access changes by provider, region, date, and rollout. If plan information and the visible model list disagree, trust the visible list and note the mismatch. Choose the best sufficient model already available; do not recommend upgrading unless no available model can reasonably meet the task or the user asks about upgrades. A higher risk may justify stronger verification without automatically requiring a stronger generation model.

## Prompt compiler rules

Compile in three passes:

1. **Intent ledger:** identify the goal, deliverable, hard constraints, named tools, success criteria, and meaningful wording. Each item must appear in the refined prompt or be explicitly marked unresolved.
2. **Compression:** remove greetings, duplicated instructions, stale branches, unrelated history, already-resolved alternatives, and control text such as `$aawf`. Combine repeated requirements without weakening them.
3. **Usefulness check:** add an output format or verification instruction only when it prevents a specific ambiguity or likely retry. Do not turn a short, sufficient request into a large specification.

Read the refined prompt once as if the original were unavailable. It must still request the same outcome, neither broaden nor narrow scope, and distinguish supplied facts from assumptions. Every added sentence must earn its place by preserving intent, resolving ambiguity, or defining a necessary completion check.

A longer refined prompt is acceptable only when it removes larger context or fixes a material omission. Say plainly when it saves no first-call input tokens.

## Context and sub-agent discipline

For each context item, apply the counterfactual test: if removing it could change the intended output, factual grounding, constraints, or verification, do not mark it `remove`. Use `unsure` when relevance depends on an unresolved choice, and recommend extracting a relevant portion when useful information is mixed with noise.

For sub-agents, name the proposed independent outputs and the merge step. Recommend `No` when those cannot be stated clearly, when work is sequential, or when all branches need the same large context. Never justify agents only by task difficulty.

## Lean execution protocol

Use this protocol to reduce avoidable tokens while maintaining quality:

1. Hold a compact working brief containing only the goal, deliverable, must-keep constraints, relevant context, and done condition. Do not repeatedly restate the full request.
2. Load files, history, sources, or tool output only when they answer a current decision. Prefer targeted reads and searches over broad context dumps.
3. Use the shortest sufficient workflow. For a clear small task, execute once and verify once. Plan visibly only when dependencies, risk, or user collaboration make the plan useful.
4. Reuse verified facts and concise state summaries instead of rereading or regenerating them. Do not create virtual role-play or real agents for work one model can do coherently.
5. Stop when the stated completion checks pass. Do not add unsolicited alternatives, repeated summaries, or ornamental explanation.

This protocol guides observable work; it cannot set or measure a provider's hidden reasoning-token budget. Never claim hidden reasoning savings.

## Ambiguity and session impact

A vague prompt is normally shorter and therefore uses fewer first-call input tokens. Its possible extra cost comes later: clarification, an incorrect assumption, discarded output, or a retry. Separate these quantities:

- **First-call impact:** deterministic before/after input estimate.
- **Possible session impact:** scenario estimate based on zero, one, or two avoided extra calls. Count only repeated input when output-token telemetry or a user-supplied output estimate is unavailable.

Classify ambiguity as:

- `low`: the outcome and deliverable are clear; assume 0 avoided calls.
- `medium`: safe assumptions may still cause rework; show a 0–1 avoided-call scenario.
- `high`: a required decision is missing or several interpretations produce different deliverables; ask one focused question rather than pretending prompt expansion solves it. Show a 1–2 avoided-call scenario only when that risk is credible.

Never present possible session savings as achieved savings.

## Token estimate

When tool execution is available, use `scripts/estimate_tokens.py` with the original task, supplied context, refined prompt, and retained context. Otherwise apply the same method described in the output contract.

The estimate is a transparent character-based range, not provider telemetry. If the refined prompt is longer, lead with: `No first-call savings—this task is small; the refined prompt adds about X–Y input tokens for clarity.` Do not label added tokens as savings.

Report possible avoided-call input separately and label it a scenario. Output tokens, latency, and cost remain unavailable unless telemetry or explicit pricing inputs are supplied.

If the user supplies current input/output prices, calculate a cost range from the corresponding token ranges and show the formula. Never use remembered prices, and never combine unmeasured output tokens with measured input tokens into a single precise cost.

For sustainability, read [references/sustainability-method.md](references/sustainability-method.md). Water impact is based on avoided complete model calls, not token differences within an unmeasured call. If no avoided call is observed or credibly forecast, say `Water saving: not claimable`. Never give a precise water figure for an unknown provider, model, data-center location, cooling system, or workload.

## Reasoning disclosure

Give concise decision evidence: observable task characteristics, selected rubric factors, and assumptions. Lead with the answer, avoid jargon, and define any necessary technical label in ordinary words. Do not reveal private chain-of-thought or describe hidden reasoning tokens.
