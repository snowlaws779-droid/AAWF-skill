# AAWF Output Contract — Skill + Optional MCP

Deliver the requested task first. Prefer clear, brief wording. Do not require users to fill in model names, plans, reasoning levels, or model-picker availability. Never produce model advice unless explicitly requested outside the AAWF workflow.

## Run mode
Complete the task in the current host. By default, no diagnostic appendix is needed for ordinary small tasks. When an AAWF record is requested, append a compact summary:
- **Approach:** shortest sufficient strategy and any useful tools actually used.
- **Verification:** checks performed; explicitly state unresolved verification.
- **Context:** high-level required/optional/removed context; preserve citations and key constraints.
- **MCP:** which exposed tools were actually called; say "none" when none was used.
- **Efficiency:** measured input/output/calls/retries only if observable; otherwise label estimates and unknowns.
- **Environmental impact:** estimate/scenario with assumptions when warranted; never claim actual saved water without data.

## Advice-only mode
State the goal, needed evidence/constraints, recommended shortest workflow (up to three steps), concrete success check, and optionally a faithful refined prompt. Do not execute. Do not propose sub-agents or model alternatives.

## Measurement honesty
Estimate first-call input separately from whole-task measured usage. Character-based input-token approximation, if useful, is a range, not model-provider telemetry. Example heuristic: upper/lower token bounds of ceiling(characters/3) and ceiling(characters/5). If the optimized text is longer, clearly report an estimated increase. Do not claim reduced energy, water, inference, or total cost from a token estimate alone.

When prior output, tool calls, retries, hidden usage, provider cost, or cache validity are unknown, explicitly mark them unknown. Impact calculations require matched workload arms and sourced environment assumptions. Do not infer "response cached" or "memory saved" from mentioning an MCP.

## Design exclusions
No model/reasoning-level recommendations, model-access interrogation, fallback-model selection, gateway routing, automated specialist agents, or a mandatory dashboard. Report optional MCP tools only when they were actually available and invoked.
