# Current product map

This page describes the current implementation and the next useful seams to
build on. It is a snapshot, not a list of permanent product exclusions. The
[product direction](product.md) describes where Diffuse can grow.

| Area | Current implementation | Next useful work |
| --- | --- | --- |
| GitHub integration | GitHub App connection, signed event delivery, exact-head review jobs, and idempotent review and Check publication. | Make onboarding, installation state, and failure recovery easier to inspect. |
| Repository context | Repository mirrors, commit-pinned indexing, policy discovery, and targeted retrieval. | Complete the supported policy and cross-repository context experience. |
| Review execution | Isolated Codex and Claude Code Agent Hosts with separate credentials and bounded execution. | Add review engines and model choices behind the existing contracts. |
| Findings | Structured candidate findings, verification, deterministic validation, deduplication, and finding lineage. | Improve discussion, feedback, and the path from a finding to a verified fix. |
| Local development | A `diffuse review` command exists, but currently reports that local review is unavailable. | Connect local workspaces to the same authorized and isolated review flow. |
| Operations | Compose deployment, PostgreSQL workflow state, CLI setup, and readiness endpoints. | Improve operator visibility, backups, upgrades, and recovery. |
| Integrations | GitHub events and private worker-to-host protocols. There is no general public developer API in the current implementation. | Explore stable client, editor, automation, and extension interfaces. |
| Quality | Review results and feedback are stored. | Build a representative evaluation set and report quality, coverage, latency, and cost. |

The words “current implementation” describe this checkout. A missing feature is
an opportunity to design and build it when it serves users; it is not excluded
by this page.
