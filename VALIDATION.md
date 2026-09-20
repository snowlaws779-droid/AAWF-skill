# AAWF Phase 1 Validation Report

Date: 2026-09-20

## Outcome

The standalone AAWF skill package passes structural and deterministic validation. It has not been installed, connected to a provider, used to route a model call, or invoked for the full behavioral benchmark.

## Completed checks

| Check | Result | Evidence |
|---|---|---|
| Official skill-package validation | Pass | `Skill is valid!` |
| Python compilation | Pass | `scripts/` and `tests/` compiled without errors |
| Unit tests | Pass | 19 tests completed successfully |
| Benchmark structure | Pass | 36 cases; six cases in each of six categories |
| Adversarial coverage | Pass | Ambiguity, simple high risk, unavailable model, inseparable context, cannot-shorten, and decomposition-overhead cases present |
| Plain-language interface | Pass | Quick answer, direct model, reasoning level, setup detection, token impact, and technical-detail sections verified |
| Cafe regression case | Pass | Detects `impeccable-design`, recommends `gpt-5.6-terra` with medium reasoning, and reports added first-call tokens |
| Platform-neutral selection | Pass | Benchmark covers Codex, Claude, Gemini, Ollama, and OpenRouter plus an unknown-platform setup gate |
| Plan-aware access | Pass | Separate Free and Plus cases use different visible model pools and avoid invented entitlements |
| Estimator smoke test | Pass | 259 baseline characters versus 179 optimized; estimated reduction 16–27 input tokens; qualitative `moderate` |
| Small-task honesty | Pass | A longer refined prompt reports `No first-call savings` and the added input-token range |
| Ambiguity scenario | Pass | Possible avoided calls are separated from achieved savings and count repeated input only |
| Sustainability guardrail | Pass | Water is tied to avoided complete calls, uses broad research anchors, and is never derived directly from token differences |
| Lean execution protocol | Pass | Compact brief, targeted context, proportionate verification, reuse, and stop conditions are present |
| Unfinished scaffold scan | Pass | No TODO, TBD, placeholder, coming-soon, or FIXME markers found |

Validation used the bundled workspace Python because `python` was not present on the shell PATH. The official validator required a temporary PyYAML dependency in the workspace cache; this did not install the AAWF skill.

## Behavioral acceptance gate

The future behavioral trial must:

- pass at least 33 of 36 benchmark cases;
- average at least 85/100;
- produce zero critical failures involving changed intent, fabricated model availability, unjustified required-context removal, exact telemetry claims, predicted savings presented as achieved, unsupported water precision, or gratuitous sub-agent recommendations.

The scorecard is defined in `evals/SCORING.md`. Until that trial is run, this artifact demonstrates a validated workflow design and deterministic test harness—not measured real-world token or water savings across providers.

## Scope confirmation

- Lean execution inside the current host, or advice-only when requested
- Explicit invocation metadata only
- No live routing or provider access
- No GPT-only default; platform and model availability must be detected or requested
- No task execution or real sub-agents
- No persistent profile or semantic cache
- Cost only from user-supplied current prices or telemetry
- Water impact shown only as telemetry or a clearly labelled avoided-call research scenario
- No control or measurement of hidden reasoning tokens

## Publication package

The repository package includes `README.md`, `LICENSE` (Apache-2.0), `NOTICE`, `.gitignore`, `.gitattributes`, `CONTRIBUTING.md`, `SECURITY.md`, and a GitHub Actions workflow for the deterministic checks. It is prepared for a public repository named `AAWF-Skill`.
