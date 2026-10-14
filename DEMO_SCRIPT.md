# Codex Demo Script

Target runtime: about 2 minutes 15 seconds.

## Before recording

1. Open this repository in Codex.
2. Confirm the working tree is clean and the existing focused tests pass.
3. Keep `issues/AD-217.md` and `demo-data/ad_decision.log` visible or easy to open.
4. Do not connect production systems or use non-synthetic data.

## Live flow

### 0:00–0:15 — Set up the issue

Show AD-217 and explain that the fictional campaign should be eligible through its exact end time, but the log shows `no_fill` at that boundary.

### 0:15–0:40 — Trace the decision

Prompt Codex:

> Read AGENTS.md and issues/AD-217.md. Trace the eligibility decision in the code. Explain why a request exactly at `ends_at` is rejected. Do not edit files yet.

### 0:40–1:15 — Add and reproduce the regression

Prompt Codex:

> Add a focused test for the acceptance criterion that a campaign is eligible exactly at `ends_at`. Run that test and show the failure. Do not change the implementation yet.

### 1:15–1:50 — Make the smallest fix

Prompt Codex:

> Make the smallest change needed to satisfy the inclusive end-time rule. Keep the scope to this defect, then run the focused test file.

### 1:50–2:15 — Review the result

Inspect the diff and test result. State that a human engineer reviews and approves any real release. The synthetic demo does not measure Netflix revenue or establish the hypothetical 20% pilot target.

## Fallback

If Codex or the test run is slow, switch to a short prepared recording showing the same issue, regression test, diff, and passing result. Label it as a fallback recording rather than implying it is a live run.

## Reset

Restore a clean copy of this repository before recording again. Confirm the original baseline tests pass before starting the demo flow.
