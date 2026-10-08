# AAWF — Approved Direction and Work-in-Progress Decision Record
**Recorded:** 2026-10-08 (Dubai)  
**Status:** Architectural decisions recorded; isolated Skill draft exists on branch \`aawf-six-pillars-post-w6\`; W6 is **IN PROGRESS** per the user, not verified complete. Do not merge or overwrite W6 without its handoff/test results.

## Identity and purpose

AAWF is a **student sustainability project**, not primarily a commercial product and not a new chatbot. The core purpose is lowering **total avoidable AI work per successful task** while preserving output quality. The host AI performs execution. AAWF consists of a **Skill** for guidance and **optional MCP tools** for capabilities that cannot be achieved by instructions alone. The Gateway/Engine is no longer part of the *target* architecture; do not delete old gateway code before preserving and reviewing existing functionality/evidence.

## Six consolidated pillars

| # | Pillar | Owner | Current evidence/status |
|---|---|---|---|
| 1 | Task analysis and workflow selection | Skill | Existing Skill behavior; remove model/plan/reasoning-level suggestions. |
| 2 | Prompt and context optimization | Skill, optional MCP context preparation | Skill logic exists; MCP \`aawf_prepare_context\` exposed in current connection. |
| 3 | Efficient execution and verification | Skill | Existing guidance; no master agents, simulated roles, autonomous sub-agents, or gateway. |
| 4 | Memory and safe response reuse | MCP, invoked conditionally from Skill | Earlier trials exercised save/recall; currently connected MCP does **not** expose save/recall or response-cache functions. Restore/verify after W6, do not claim implemented. |
| 5 | Lightweight RAG retrieval filtering | MCP/connector integration | In-progress feature not verified current MCP. Only deduplicate retrieved chunks, reuse existing retrieval scores, select to token budget, and conditionally skip. |
| 6 | Savings and environmental measurement + optional dashboard | Skill, MCP, offline reporting | Current MCP exposes \`aawf_calculate_impact\`. A persistent dashboard is not verified. Never claim energy/water savings without evidence and uncertainty disclosure. |

## Remove/retire from the target feature set

- Model recommendations, reasoning-level suggestions, provider/model availability questions, subscription and fallback-model selection.
- Automatic model routing/provider execution gateway; user-facing AAWF bot; scheduling workflows.
- Master-agent architecture, simulated specialist roles, autonomous sub-agents. Retain only ordinary short task planning.
- Standalone teaching layer, dedicated project profiles, heavy customization systems.
- Automatic adaptive/online learning **deferred**, not permanently rejected. Store no unsupported learning claims.

## Simplify/merge, not delete safeguards

- Token/compute budgeting -> lean task/context selection; do not claim control over hidden provider compute.
- Model locks -> preserve any user-provided restrictions without implementing an independent chooser.
- Retry/verification logic -> proportionate checks and normal host failure handling; count retries in offline evaluation.
- Permission and privacy boundaries -> keep host permissions, source access rules, credential secrecy and account isolation.
- Costs and resource per successful task -> incorporate into measured comparisons/offline evaluation, not mandatory per-message computation.
- Benchmarking -> essential offline release gate; should not add runtime overhead.
- Packaging -> enough installation and test guidance; public distribution work can wait.
- Savings dashboard -> optional lightweight report built from actual evaluation metrics; do not load it on every task.

## Distinguish context, memory, and caching

**Skill context reduction** handles instructions, conversation, and explicitly provided context.  
**MCP context preparation** may remove optional exact duplicates and should not duplicate Skill work.  
**RAG filtering** handles document chunks already retrieved by a vector/database search; not the same as prompt/history filtering. Do not add a vector DB, reranker or time-based RAG freshness filtering.  
**Memory** stores/retrieves prior approved project facts; absence of a connected endpoint means no persistent memory feature can be claimed.  
**Response cache** can skip eligible repeat inference only if the host workflow actually consumes the reused result. Exact-match, user/account isolation, valid result and opt-in are requirements. Semantic reuse deferred. Cache validity protections are **not** the rejected RAG freshness filter.

## Net-efficiency rule

Keep a feature only if end-to-end evidence shows its benefits outweigh tool traffic, latency, cost, complexity and possible retries while preserving answer quality. Compare matched baseline tasks; report unknown provider usage as unknown. Favor simpler operations and conditional tool calls.

## Current implementation boundary

- The public \`snowlaws779-droid/AAWF-skill\` repository has been inspected; its original main branch did include mandatory model advice and model-picker setup questions.
- An **isolated branch** now refactors SKILL.md and its active docs toward the six pillars. This branch is **not merged** and does not modify the live MCP, the gateway, W6, or the website.
- W6 is **still being completed**, scope/branch and handoff not independently verified. Pause merging until W6 handoff and tests.
- Current AAWF MCP exposes \`aawf_prepare_context\` and \`aawf_calculate_impact\`; memory, response caching and RAG functionality require fresh verification.
- Status labels in tomorrow's pitch must distinguish *tested*, *in progress*, and *planned*.

## Tomorrow's six-pillar pitch

“AAWF is a student-led AI sustainability project combining a lightweight Skill with optional MCP tools. It focuses on understanding tasks, reducing unnecessary prompt/context text, avoiding wasted workflow steps, reusing suitable information, filtering retrieved evidence, and measuring whether overall resource use actually falls without reducing result quality.”

Do **not** say all six pillars are already deployed or that estimated water savings were measured.

## Future public-page rewrite / rebrand — NOT DONE

After core engineering and evaluation, rewrite the existing main product page to frame AAWF more as a **project**, not a polished commercial product or chatbot. Explain the student motivation, experimental design, working results, limitations, water-estimate uncertainty, and Skill+MCP architecture. Replace claims about automatic routing or full adaptive learning if they no longer apply. Preserve the original site until that separately reviewed phase.

## Open items

1. Receive W6 exact completion handoff (repository, branch, tests, changed modules, current MCP tool catalog).
2. Test/refine the isolated Skill refactor against W6 and merge safely **after** W6.
3. Implement/test memory and safe exact response reuse in MCP if useful.
4. Finish new RAG filtering without a gateway.
5. Run representative matched quality+resource benchmarks and prepare optional visual report.
6. Review site rebrand copy as a separate future change.

See \`docs/POST-W6-IMPLEMENTATION-PROMPTS.md\` for ready-to-run prompts.
