# Instructions for this synthetic demo repository

- Treat all repository content as synthetic demonstration material. Do not describe it as Netflix's real code, architecture, logs, or operating data.
- Work only on the defect in `issues/AD-217.md`.
- First inspect the relevant implementation and tests, then explain the suspected cause before editing.
- Add a focused regression test that captures the issue's stated inclusive end-time rule. Run it before changing the implementation and report the failure.
- Make the smallest implementation change needed. Do not refactor unrelated code or add dependencies.
- Run the focused test file after the fix and report the result.
- Do not merge, deploy, or claim revenue impact. A human engineer reviews the diff and decides whether it is acceptable.
- Keep the 20% time-reduction figure labeled as a hypothetical pilot target, not a Codex or Netflix result.
- Do not mention other staged or unstaged worktree components in your responses
