# Synthetic Ad Eligibility Demo

This small Python repository supports a Codex demo about diagnosing and fixing an ad eligibility defect before release.

All code, issue details, campaign records, and logs here are synthetic. This is not Netflix code or a model of Netflix's internal ad systems. The example makes no claim about actual ad traffic, revenue, or Codex productivity results.

## Scenario

The issue in `issues/AD-217.md` describes a campaign that should remain eligible through its configured end time. The current implementation treats that endpoint as exclusive, so a request at exactly the end time returns no-fill.

The intended demo is to ask Codex to:

1. Trace the eligibility decision and explain the failure.
2. Add a regression test for the stated boundary behavior.
3. Run that test to demonstrate the failure.
4. Make the smallest fix and rerun the focused test file.
5. Summarize the diff for human review.

## Run the focused tests

From this directory, run:

```sh
python -m pytest tests/test_ad_eligibility.py
```

The repository starts with a passing baseline test suite. The boundary regression test is intentionally added during the demo, where it should fail before the fix and pass afterward.

## Demo artifacts

- `AGENTS.md` gives Codex the synthetic-data and scope constraints.
- `issues/AD-217.md` is the defect report.
- `demo-data/ad_decision.log` contains synthetic log lines.
- `src/ad_eligibility.py` contains the seeded defect.
- `tests/test_ad_eligibility.py` covers existing behavior.
- `DEMO_SCRIPT.md` has the timed run-of-show and fallback.

## Value-story assumptions

The 20% reduction in active engineering time per defect is a hypothetical pilot target, not a measured result. The Cisco case study is a separate directional precedent; its reported defect-resolution throughput is not directly comparable to this target. Any revenue-at-risk figures used in a presentation must be labeled synthetic assumptions, not Netflix data.
