# AAWF Skill

AAWF chooses the right model, tools, prompt, and workflow for each task—reducing unnecessary tokens, retries, compute, cost, and environmental impact while maintaining quality.

AAWF is a lean workflow skill. It understands the task, detects the AI platform and plan, selects a suitable available model, refines the prompt, limits unnecessary context and agent overhead, completes the task in the current host when requested, verifies the result, and reports an honest efficiency trace.

## What it does

- Works across ChatGPT, Codex, Claude, Gemini, Ollama, OpenRouter, and other platforms.
- Uses the visible model picker as the source of truth; plan names such as Free, Plus, or Pro are context, not assumed entitlements.
- Asks one short setup question when the platform or available model list is unknown.
- Gives a plain-language recommendation first, with detailed evidence afterward.
- Provides a short task-specific execution recipe and quality checks for website building, coding, debugging, research, writing, decisions, and routine work.
- Helps the current model work from a compact brief, read context only when needed, verify once proportionately, and stop when the requested result is complete.
- Separates first-call token impact from possible session savings caused by avoiding clarification or retries.
- Reports `No first-call savings` when prompt refinement adds tokens to a small task.
- Shows a cautious, research-anchored water-impact scenario only for complete model calls that may have been avoided.

## How it starts

If AAWF can see the AI platform and model choices, it gives a direct recommendation. If not, it asks only:

> Which AI tool are you using, and which model names can you see in its model picker? If relevant, include your plan.

This keeps the setup simple while avoiding invented model access.

## What it does not do

AAWF does not route provider calls, automatically switch models, create real sub-agents, access accounts, control hidden reasoning tokens, or claim measured environmental savings without telemetry. Its water figures are clearly labelled scenarios, not provider measurements.

## Install in Codex

1. Download or clone this repository.
2. Rename the cloned folder to `aawf` if needed, then copy that complete folder into your Codex skills directory.
3. Restart Codex.
4. Invoke it explicitly with `$aawf`.

The skill is configured for explicit invocation only.

## Sharjah prototype demo

Use a short request so the audience can see AAWF improve the workflow rather than relying on a long prepared prompt:

```text
$aawf Build a polished, responsive one-page website for NOVA Study, an AI study companion for high-school students. Create the local files and verify the result.
```

For the demonstration, show that AAWF:

1. Recognizes the current AI platform, available model, and any named design or coding tool.
2. Uses a compact brief, targeted context, one proportionate implementation pass, and focused verification.
3. Delivers the requested result before a short, understandable AAWF summary.
4. Says `No first-call savings` when clarification made a small prompt longer.
5. Separates possible avoided-retry tokens from achieved savings.
6. Shows water only as provider telemetry or a clearly labelled avoided-call research scenario.

For an honest award presentation, describe this as a working skill prototype with deterministic estimation and validated workflow rules. Do not describe the water range as a measurement from the user's live provider.

## Validate locally

Run these commands from the skill folder:

```powershell
python -m unittest discover -s tests -v
python scripts/validate_benchmark.py evals/benchmark.jsonl
```

The benchmark contains 36 cases across coding, debugging, research, writing, architecture, and routine execution.

## License

Apache License 2.0. See [LICENSE](LICENSE).
