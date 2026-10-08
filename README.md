# AAWF — Lightweight Skill + Optional MCP

AAWF is a student sustainability project exploring how existing AI tools can **avoid unnecessary computation without making results worse**.

The AAWF **Skill** runs inside the user's existing AI host and guides task analysis, prompt/context selection, efficient execution, and proportionate verification. **Optional MCP tools** provide context preparation and evidence-based impact calculation when actually exposed. Memory, response caching, and RAG filtering are target MCP capabilities and must not be advertised as currently available until tested.

There is **no AAWF provider-routing gateway** in this target architecture. AAWF does not switch models, recommend models/reasoning levels, inspect subscription plans, spawn specialist agents, or measure hidden provider compute.

## The six project features

1. **Task analysis and workflow selection** (Skill)
2. **Prompt and context optimization** (Skill)
3. **Efficient execution and verification** (Skill)
4. **Memory and safe response reuse** (MCP target — verify availability)
5. **Lightweight RAG filtering** (MCP target — work in progress)
6. **Savings measurement and optional dashboard/reporting** (Skill + MCP + offline evaluation)

## How to use

Install the Skill in the appropriate host skill directory and invoke it explicitly as \`$aawf\` where that host supports skill invocation. It completes the requested task in the host, then reports savings only when supported by evidence. MCP access requires separate authorization and a connected endpoint exposing the relevant function.

The currently observed MCP offers \`aawf_prepare_context\` and \`aawf_calculate_impact\`. Older trials used memory save/recall functions; do not assume they remain available. Response-cache hits and RAG savings cannot be claimed just because the Skill describes them.

## Validation and roadmap

- Existing repository tests can be run using \`python -m unittest discover -s tests -v\` and \`python scripts/validate_benchmark.py evals/benchmark.jsonl\`. These **must be rerun** after changing the Skill; passing tests are not asserted here.
- See [AAWF six-pillar decisions](docs/AAWF-SIX-PILLAR-DECISIONS-2026-10-08.md) and [post-W6 prompts](docs/POST-W6-IMPLEMENTATION-PROMPTS.md).
- **W6 is in progress**, according to the user; this branch is isolated for review after W6.
- A future website-copy refresh should position AAWF as a **student sustainability project**, not mainly a commercial product. The existing product page is not changed here.

AAWF measures **total resource use per successfully completed task** in matched evaluation, including relevant overhead. Shorter prompts alone are not evidence of lower total inference costs or water use.
