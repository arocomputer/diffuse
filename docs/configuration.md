# Repository review configuration

The current repository-owned configuration file is `.diffuse/config.json` at
the repository root. It controls whether Diffuse reviews the repository, the
paths it ignores, the severity floor, draft pull request behavior, and review
planning. The `version` field versions this file format; it does not define the
scope or ambition of the product.

Separately from configuration, policy discovery indexes guidance documents
for the review agents: `.diffuse/rules.md`, plus convention-named instruction
files (`AGENTS.md`, `CLAUDE.md`, `CONTRIBUTING.md`, and
`.github/copilot-instructions.md`).
`packages/server/src/diffuse/repository/policy/discovery.py` is authoritative
for the exact set.

```json
{
  "version": 1,
  "review": {
    "enabled": true,
    "passes": ["correctness", "security", "tests"],
    "minimum_severity": "medium",
    "ignored_paths": ["generated/**", "**/*.snap"]
  },
  "triggers": {
    "review_drafts": false,
    "status_check": true
  }
}
```

`passes` is the current review-plan input. Its interpretation may evolve as
review plans and engines grow. `status_check` controls the GitHub Check only;
it does not authorize a pull-request decision.

## Configuration and product behavior

This example shows common settings, not the full configuration surface. The
implementation in
[`policy/models.py`](../packages/server/src/diffuse/repository/policy/models.py)
defines accepted fields and validation. Policy discovery also finds nested
`.diffuse/config.json` layers and `.diffuse/files.json` context; support and
operator controls for these capabilities continue to evolve.

Automatic approval and agent-authored changes are not implemented by the current
review flow, and their settings are rejected. They remain product and security
design questions, not a permanent ban. Any implementation must make
permissions, user intent, and resulting changes visible and auditable.
