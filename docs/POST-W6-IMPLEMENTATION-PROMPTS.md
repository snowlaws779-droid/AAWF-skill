# AAWF — Implementation Prompts to Use AFTER W6
**Prepared:** 2026-10-08. **W6 status:** IN PROGRESS, not yet finished.  
**Source of decisions:** [six-pillar decision record](AAWF-SIX-PILLAR-DECISIONS-2026-10-08.md).  
**Isolation:** a Skill-only draft is on `aawf-six-pillars-post-w6`. No MCP/Gateway/W6/website modification is claimed.

Do not execute the next phase until W6 provides its implementation summary, branch/commit, test results and the exact MCP tool catalog. Each prompt below is deliberately bounded. **Do not call all agents/phases at once.**

## Prompt A — W6 completion handoff and reconciliation

> W6 is currently being completed. Once its work finishes, audit its actual deliverables without changing the code. Identify repository, branch/commit, changed modules, tool interfaces, exposed MCP capabilities, tests executed, pass/fail evidence, and known limitations. Compare these against docs/AAWF-SIX-PILLAR-DECISIONS-2026-10-08.md in the AAWF Skill repository. Do not mark W6 complete without evidence. Distinguish what is already implemented from what is planned. Identify any dependencies or conflicts with the isolated Skill branch `aawf-six-pillars-post-w6`. Report a prioritized, minimal next-phase plan focused on verified net resource efficiency. Do not change the active product page.

## Prompt B — W7 Skill integration (run only after W6 handoff)

> Integrate the approved six-pillar Skill+MCP architecture after W6 is verified. Compare the isolated `aawf-six-pillars-post-w6` branch to the actual post-W6 code and tests. Preserve correct W6 work; do not blindly overwrite newer changes. Remove mandatory model selection, reasoning-level suggestions, model-picker/subscription questions, fallback model advice, gateway routing, master agents and simulated/real sub-agent advice from the active Skill and output contract. Keep task analysis, faithful prompt and context optimization, efficient execution, focused verification, and optional MCP integration. Delete/archive orphaned model-selector code only after checking references/tests. Run the full existing Skill tests and fixed benchmark; repair regressions, update tests for the approved new behavior, and show the before/after diffs. Do not assert hidden-provider savings, modify the gateway, or add autonomous learning.

## Prompt C — W8 Restore MCP memory and safe response reuse

> Inspect the actual post-W6 MCP. Prior trial examples used `aawf_recall_context` and `aawf_save_material`, but current exposure must be verified rather than assumed. Restore or implement minimal authorized persistent memory save/recall only if absent, based on existing storage/interfaces where possible, with source/version metadata, permissions, isolated project/account boundaries, and bounded retrieval. Integrate conditional invocation from the Skill only when prior context materially changes the task. Separately evaluate **exact** response caching: enable reuse only for an authorized same-account opt-in repeat with unchanged relevant inputs, validated result and actually avoided model execution. Skip caching if the host workflow cannot intercept/consume the result or if lookup overhead exceeds benefits. No semantic cache or new execution gateway. Add tests for isolation, correctness, missed/expired cache, no-result fallback, tool overhead and provenance. Report real cache hits and avoided calls only when measured.

## Prompt D — W9 New MCP RAG filter

> Build/finish the new RAG-specific post-retrieval filtering in the MCP, not the old Gateway and not AAWF's general prompt/history context reduction. Operate only on externally supplied vector/document-search chunks. Implement (1) lightweight exact deduplication preserving all source references, (2) reuse of already returned relevance/similarity scores rather than new reranking, (3) context selection under a retrieval token budget while protecting important evidence/citations, and (4) conditional bypass when retrieval is absent or the additional work is not worthwhile. **No RAG freshness, timestamp or age filtering**, no independent reranking/embedding/LLM calls, and no new vector database. If previous work implemented a RAG-only freshness filter, remove that portion; preserve independent response-cache validity protections. Detect and avoid duplicate processing with existing context preparation. Test input/output token counts, processing overhead, latency, evidence retention and net resource impact; reject quality-degrading cases. Keep all non-RAG behavior intact.

## Prompt E — W10 Benchmarks and optional lightweight dashboard

> After core Skill and MCP functionality is verified, execute paired baseline-versus-AAWF tests across representative task types. Use the same model, task, scoring rules and measurement boundary; include retries, unsuccessful attempts, tool/MCP traffic, costs where known, and accepted-answer quality. Distinguish measured tokens/calls from rough estimates, and energy/water scenarios from measurements. Audit failures and edge cases. Build a lightweight optional report/dashboard from recorded results (not a mandatory per-request service) showing total resource usage per successful task, context reduction, eligible exact-cache hits, invocation overhead and confidence/limitations. Never infer measured water savings from token reduction. Recommend features to disable if quality-adjusted overall savings are negative.

## Prompt F — Future main-site rebrand to a student project (separate later phase)

> Review the current AAWF website main product page and the verified release evidence. Draft a page rewrite that presents AAWF first as a **student sustainability/research project**, not mainly a commercial AI product. Explain why avoiding unnecessary AI work matters, how the Skill and optional MCP complement existing AI tools, the six pillars and their accurate working/planned statuses, test methods, and honest uncertainty around energy/water savings. Avoid unsupported phrases about automatic provider routing, always-on adaptive learning, autonomous agents, deployed caching/RAG or exact water saved. Keep branding recognizable but more research/demo-oriented. Present a proposed content diff for review **before** editing the live website. Do not change the website in the engineering phases above.

## Stop / quality gates

- W6 must be independently verified before merging this branch or starting follow-on integration.
- Memory, cache, and RAG must not be presented as deployed solely because draft prompts or old test traces exist.
- The Skill must not ask for model names, plan details, or preferred reasoning settings.
- Do not eliminate privacy, approval, credential safety or cache validity safeguards just because their standalone feature labels were removed.
- If a requested feature does not save resources overall, document the result and skip/defer it.
