# AAWF Sustainability Estimate

AAWF reports a water-impact scenario only when an entire model call may have been avoided. Token reduction inside a call cannot be converted reliably into water saved without provider telemetry about the model, hardware, location, electricity mix, cooling system, and workload.

## Evidence bands

Use these only as broad research anchors, not universal conversion factors:

- **Median text-call anchor:** Google measured a median Gemini Apps text prompt at about `0.26 mL` of water in its production stack. This is provider- and workload-specific.
- **Efficient-model anchor:** a 2025 infrastructure-aware study estimated several efficient models at under `2 mL` per query across tested input lengths.
- **Long/reasoning upper anchor:** the same study estimated some compute-intensive models above `150 mL` per query. Treat `150 mL` as an observed high anchor, not a maximum.

Sources:

- Elsworth et al., *Measuring the environmental impact of delivering AI at Google Scale* (2025): https://arxiv.org/abs/2508.15734
- Jegham et al., *How Hungry is AI? Benchmarking Energy, Water, and Carbon Footprint of LLM Inference* (2025): https://arxiv.org/abs/2505.09598
- Li et al., *Making AI Less “Thirsty”* (2023), showing that water efficiency varies by location and time: https://arxiv.org/abs/2304.03271

## Reporting rules

1. If no complete call was avoided or forecast, report `Water saving: not claimable`.
2. If provider telemetry supplies water use, report that value and identify it as telemetry.
3. For one credibly avoided ordinary text call with an unknown provider, report only: `Illustrative water range: roughly 0.26–2 mL, low confidence; provider and location unknown.`
4. For a credibly avoided long or reasoning-heavy call, report: `Illustrative water range: roughly 2–150+ mL, very low confidence; not a provider measurement.`
5. Multiply only by the explicit avoided-call scenario. Keep a range when the avoided-call count is a range.
6. Never call a forecast an achieved saving. Use `potentially avoided` until provider telemetry or an observed avoided retry exists.

Do not convert water to bottles, cups, or household equivalents unless the user asks. Small estimates should remain in milliliters.
