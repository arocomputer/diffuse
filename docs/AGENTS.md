# Agent Hosts and review engines

Diffuse owns GitHub webhook ingestion, commit-pinned context, orchestration,
verification, lineage, and publication. Codex and Claude Code are isolated,
read-only **Agents**. They investigate one exact pull-request head
and return structured candidate findings; they never publish to GitHub or hold
Diffuse control-plane credentials.

## Boundary

```text
Diffuse worker
  -> isolated candidate Agent Host (Codex or Claude Code)
  -> structured candidate findings
  -> isolated verifier Agent Host (the other engine)
  -> deterministic validation, lineage, and publication
```

The worker never executes a vendor CLI and never mounts a vendor credential.
Each runner has only its own credential home, a read-only review workspace,
bounded vendor egress, and private access to the exact immutable context it was
issued. It has no database, GitHub App, operator API token, branch-write, or
arbitrary-network access.

The current transport is a private, narrowly scoped protocol that exposes the
context operations needed by an investigation. It is one implementation of the
Review Agent contract; future engines and integrations can use other contracts
with their own explicit permissions.

## Investigation contract

An investigation is bound to one repository, pull request, index snapshot, and
head SHA. The current runtime supplies a role, time and work budgets, and a
read-only operation allowlist. Defaults protect shared resources and can evolve
with operator needs.

Its output is a **candidate**, not a final review. Every candidate must name:

- the exact location and code evidence;
- severity and category;
- why the change fails or is risky; and
- the relevant head SHA and investigation identity.

A separate investigation on the other engine verifies the canonical candidate
result and can reject any candidate. The verifier is bound to the candidate
result digest; omitted decisions reject. Diffuse performs final exact-head
validation, deduplication, lineage changes, and GitHub publication.

## Current transport and extension points

The worker creates a deterministic, bounded source artifact from the exact
checked-out head and signs both its transport digest and canonical workspace
digest into the private dispatch. The runner validates and materializes that
artifact as a read-only workspace before starting the CLI; it never clones,
mounts a repository mirror, or receives SCM credentials. The current transport
uses an in-envelope source archive with limits of 16 MiB compressed and 128 MiB
extracted, and schedules one active review per 1 GiB runner. These are current
implementation limits that can change as repository size and throughput needs
grow.

Scoped private context access is bound to the repository, pull request,
snapshot, head, review attempt, exact bearer digest, and capability lifetime.
The candidate and verifier have separate durable Investigations, capabilities,
budgets, result digests, lifecycle states, and token accounting.

`REVIEW_AGENT` selects the candidate engine. Its values are `codex` and
`claude`; the other engine verifies, so both authenticated Agent Hosts must be
running. Both execute only through an isolated Agent Host. Session capabilities
are the internal representation of a Review Access Grant. New engines can join
this contract, and future clients can use a public contract designed for their
workflows without inheriting the private transport's assumptions.
