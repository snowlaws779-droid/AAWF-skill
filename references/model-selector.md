# AAWF Phase 1 Platform and Model Selector

Recognize the person's AI platform first, then choose one exact model from that platform. Do not default to GPT.

## Separate the setup

Record only what is visible or explicitly stated:

- **AI platform:** where the prompt will run, such as ChatGPT, Codex, Claude, Gemini, Ollama, OpenRouter, or another app
- **Plan:** Free, Plus, Pro, Team, Enterprise, API, local, or another stated plan
- **Available models:** exact names visible in the platform or supplied by the user
- **Task tools:** skills, plugins, apps, browsers, editors, or domain tools used to complete the task

A platform and a task tool are not the same. For example, Codex can be the platform while `impeccable-design` and a browser preview are task tools.

Do not infer a subscription plan from the platform, a model name, or the user's wording. Plans and model access change over time.

## Plan-aware access

The plan helps explain constraints, but the visible model list is the source of truth.

- If both plan and model list are visible, choose only from that list and report the plan's practical effect in one sentence.
- If the plan is known but the model list is not, ask for the model-picker names. Do not rely on remembered plan entitlements.
- If the plan is unknown but the model list is visible, proceed; plan information is not required.
- If the plan and visible list disagree, trust the visible list and flag that access may be changing or account-specific.
- On a Free plan, select the best sufficient visible model and design the workflow around any stated limits. Do not assume exact quotas or unavailable features.
- On Plus, Pro, Team, Enterprise, API, or another paid plan, use extra choices only when the task benefits. Paid access does not automatically justify the strongest model.
- Recommend a plan upgrade only when the current visible models cannot reasonably meet the requested quality or capability, or when the user explicitly asks. Label it optional and explain the specific limitation.

## Recognition signals

Use reliable host metadata first, then explicit user text:

- ChatGPT or Codex: the host identifies itself as ChatGPT/Codex, or the user names it
- Claude: the host or user names Claude or Anthropic
- Gemini: the host or user names Gemini or Google AI Studio
- Ollama: the user names Ollama, a local model, or supplies `ollama list`-style model names
- OpenRouter: the user names OpenRouter or supplies its provider/model identifiers
- Other: preserve the exact platform name the user supplies

Do not treat a model family alone as proof of a specific app; the same model may be offered through several platforms.

## Setup gate

Name a specific model only when the platform and usable model choices are known.

If neither is known, ask exactly:

`Which AI tool are you using, and which model names can you see in its model picker? If relevant, include your plan.`

If the platform is known but available models are not visible, ask:

`Which model names can you select in [platform]? If your plan affects that list, include the plan name.`

Ask once and wait. If the user answers `use the current model`, continue the workflow and report `Current host model—exact name unavailable` rather than guessing. Do not use GPT as a hidden fallback.

## Choose by role

Map the task need to a role, then choose the best exact available model for that role:

| Role | Use when | Typical reasoning |
|---|---|---|
| Fast | simple extraction, formatting, or tiny edits | none to low |
| Balanced | UI creation, ordinary coding, and structured writing | low to medium |
| Reliable | debugging, research synthesis, or multi-file work | medium to high |
| Strongest | exceptional architecture, severe uncertainty, or demanding verification design | high to maximum available |

Use descriptions exposed by the platform or supplied with the model list. Prefer the least expensive available model likely to maintain the requested quality. Do not assume identical reasoning-control names across providers: report the exact control when visible; otherwise use a plain recommendation such as `standard thinking` or `extended thinking`.

Apply this selection order:

1. **Hard fit:** remove candidates that lack a required modality, context capacity, tool capability, or execution environment stated by the user or host.
2. **Quality fit:** choose the lowest role that covers the task's complexity, uncertainty, and verification burden.
3. **Efficiency tie-break:** between equally suitable candidates, prefer the faster or cheaper option only when that comparison is confirmed by the host, user, or current platform metadata.
4. **Fallback:** select a different confirmed model that can still complete the task. Do not list a cheaper fallback that is likely to fail a hard requirement.

Base claims about model capabilities on current host metadata, visible platform descriptions, or user-supplied information. If exact names are visible but their differences are unclear, state that uncertainty and make the most conservative sufficient choice from the confirmed list; do not invent benchmark, price, speed, or plan claims.

The final explanation must identify the task requirement that justified the selected model and why the next-stronger option is unnecessary, when one exists.

## Provider-neutral rules

- ChatGPT/Codex: select only from the visible OpenAI model picker or host catalog.
- Claude: select only from the visible Claude models and use its actual thinking control if shown.
- Gemini: select only from the visible Gemini models and use its actual thinking control if shown.
- Ollama: select only from installed local model names supplied by the user or runtime; consider hardware limits if provided.
- OpenRouter: preserve the full provider/model identifier and select only from the user's accessible list.
- Other platforms: preserve exact model names and controls from that platform.

Never translate one provider's private reasoning setting into another provider's unsupported label. Never claim that a model is included in a plan unless the host or user confirms it.

## Tool-aware adjustments

- Name useful task tools under `Use these tools`, but do not assume they replace verification.
- If the task needs visual judgment, recommend a render/browser check when available.
- If a requested task tool is unavailable, say so and give the closest usable fallback. Never claim it ran.
- `$aawf` is control text, not task context. A domain skill such as `impeccable-design` is part of the requested workflow and should be retained.

## Plain-language output

Always report:

- `AI platform:` exact detected or user-supplied platform
- `Use this model:` exact name from that platform's available list, or `Current host model—exact name unavailable` only when the user explicitly chose that option
- `Reasoning/thinking:` exact visible control or a clearly labeled recommendation
- `Why:` one sentence tied to the task
- `Fallback:` another exact available model, or `None available`
- `Availability:` how the model list was confirmed
- `Plan impact:` how the stated plan changes this choice, or `Plan not needed because the model list is visible`

Keep the internal capability tier in technical details, not the quick answer.
