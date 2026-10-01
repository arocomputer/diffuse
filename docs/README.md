# Diffuse documentation

Start with the [project README](../README) to understand Diffuse and review a
first pull request. These pages are the reference behind it.

| Document | What it is |
| --- | --- |
| [product.md](product.md) | Durable product direction, principles, and opportunities to grow. |
| [architecture.md](architecture.md) | Component map, the review lifecycle, and where each responsibility lives (resolves the repeated `review`/`context` nouns). |
| [capabilities.md](capabilities.md) | Snapshot of current capabilities and useful next work. |
| [agents.md](agents.md) | Agent Host architecture, investigation contract, and current execution flow. |
| [configuration.md](configuration.md) | Repository review configuration and policy discovery. |
| [deployment.md](deployment.md) | Current self-hosted deployment and Diffuse GitHub App connection. |
| [infisical-hosted-production.json.example](infisical-hosted-production.json.example) | Safe placeholder-only import template for GitHub Integration Service production configuration. |
| [cli.md](cli.md) | CLI commands for installation, repository management, and review operations. |

Elsewhere in the repository:

- [`AGENTS.md`](../AGENTS.md) — environment setup, tests, migration
  rules, and the dependency workflow.
- [`SECURITY.md`](../SECURITY.md) — how to report a vulnerability.
- [`.env.example`](../.env.example) — the deployment environment variables,
  documented inline at their definitions. Some operator-tunable worker and
  review knobs exist beyond this file; the code that reads them is
  authoritative.
- [`deploy/README.md`](../deploy/README.md) — installing a tagged release from
  published, signature-verified images.
- [`packages/relay/README.md`](../packages/relay/README.md) — operating the
  small public event and credential relay.

The current public and private integration surfaces are described in
[capabilities.md](capabilities.md). Interfaces can grow as product needs and
their authorization models are designed.
