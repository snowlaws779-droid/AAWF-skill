# AAWF Lean Workflow Playbooks

Choose at most one task mode. These are instructions for the **current host AI**, not separate agents or model-selection recommendations.

## Website or UI build
Keep design constraints and files needed to implement. Build the requested scope, check layout on desktop/mobile where supported, verify interactions/links. Do not add features beyond the request.

## Coding change
For a narrow edit, change the minimum necessary. For coupled changes, briefly map dependencies and acceptance criteria. Run the smallest relevant tests/build. Preserve unrelated code.

## Debugging
Keep the failing example, error evidence, and affected code. Reproduce, isolate, fix the supported cause, and verify. Avoid wide log dumps.

## Research
Keep the precise scope and important source constraints. Search only when needed; prefer credible, relevant evidence, distinguish fact from inference, and cite material claims.

## Writing
Keep audience, facts, voice, length, format, and explicit exclusions. Produce the draft and check requirements. Avoid unnecessary research or diagnostics.

## Architecture or decision
Identify constraints, viable options, trade-offs, and checks. Choose the smallest change whose expected net benefit is positive. Do not assume an optimization helps without measuring overhead and quality.

## Routine task
Do it directly. Do not add a plan, extra MCP calls, extensive checks, or artificial multi-step workflow when one action suffices.
