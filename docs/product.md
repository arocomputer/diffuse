# Diffuse product direction

Diffuse helps people understand and improve software changes. It brings codebase
context, focused analysis, and actionable feedback to the places developers
work: pull requests today, and local work, editors, automation, and other review
surfaces as the product grows.

The product should serve individuals and teams working across repositories,
languages, model providers, and deployment environments. The current product is
self-hosted GitHub pull-request review. That is a foundation to build on, not a
definition of the product's limit. Future deployment options must remain
consistent with the project license.

## Product principles

- **Meet developers in their workflow.** Reviews should be available in pull
  requests and local changes, with useful connections to editors and other
  development tools as those needs emerge.
- **Make findings useful.** Explain what can fail, point to evidence, and make
  it easy to respond, discuss, correct, or dismiss a finding.
- **Use repository context well.** Respect project guidance and help people
  understand code across files and repositories when they authorize that
  context.
- **Let teams shape review.** Review behavior, policy, model choice, and
  integrations should adapt to a team's work without requiring a fork of
  Diffuse.
- **Keep people in control.** Changes to branches, pull-request state, or
  repository configuration must be visible, policy-controlled, and auditable.
  Automation should have clear permissions and an easy way to see what it did.
- **Earn trust with evidence.** Findings should be tied to the code and revision
  that produced them. Measure quality, false positives, latency, and cost as the
  system evolves.
- **Keep deployment understandable.** Self-hosting should remain practical.
  Setup, upgrades, health, backups, and recovery are part of the product.

## Current foundation

Diffuse receives GitHub events, indexes repository snapshots, builds review
context, dispatches isolated Codex or Claude Code investigations, verifies
candidate findings, and publishes reviews and GitHub Checks. The worker and
Agent Hosts have separate credentials and responsibilities. See
[architecture.md](architecture.md) and [AGENTS.md](AGENTS.md) for the current
implementation.

## Product areas to grow

Use these areas to organize product discovery and implementation. The order can
change as users and evidence point to better work.

- Review local changes and connect review to IDEs, command-line workflows, and
  other code hosts.
- Make review setup, repository onboarding, health, and history easy to
  understand and operate.
- Support more review engines, model providers, and local or private models
  through stable contracts. Evaluate an `e`-backed engine through its process
  interface, with shell, write, and extension tools disabled inside the same
  isolated Agent Host boundary.
- Give teams richer repository and organization policy, reusable guidance, and
  authorized cross-repository context.
- Let developers discuss findings, capture feedback, and carry decisions into
  later reviews.
- Offer automation and extension points for custom checks, notifications, and
  engineering workflows.
- Add change proposals and other write actions with explicit permissions,
  policy controls, and a clear audit trail.
- Improve evaluation and reporting so teams can see review quality, coverage,
  cost, and operational health.

## Suggested build sequence

1. Connect `diffuse review` to a real local-workspace flow through the existing
   Review Agent contract. Define how the user, repository, workspace, and
   short-lived access grant are authorized before dispatch.
2. Build an evaluation loop from real reviewed changes and human feedback.
   Track accepted findings, misses, noise, coverage, latency, and cost so new
   engines and review plans have evidence behind them.
3. Improve setup and day-two operations. The current repository has CLI and
   health endpoints; decide whether to grow those or add a dashboard for
   onboarding, readiness, review history, upgrades, backups, and recovery.
4. Add another engine as an end-to-end experiment. `e` is a strong candidate
   because its process interface and provider catalog can broaden model choice;
   keep its writable tools and extensions disabled for review workloads.
5. Grow policy, cross-repository context, feedback, conversation, integrations,
   and optional write actions from the needs exposed by those workflows.

## Platform invariants

Growth should preserve clear identity and authorization boundaries between
users, organizations, repositories, review runs, and integrations. A finding
must identify the repository state it describes. Credentials and repository
content should reach only the components that need them. Resource limits should
have safe defaults and be configurable for the operator's workload. New public
interfaces, write actions, and extension mechanisms need an explicit permission
model and an auditable contract.

These are design requirements, not reasons to rule out a product area before
there is a concrete design.
