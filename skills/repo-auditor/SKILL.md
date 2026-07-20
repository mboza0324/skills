---
name: repo-auditor
description: Audit one repository or an entire GitHub portfolio and produce evidence-backed completion, risk, and shipping priorities without changing application code.
version: 1.0.0
---

# Repo Auditor

## Purpose

Inspect a repository from end to end and determine what is actually complete, broken, unsafe, stale, duplicated, externally blocked, or ready to ship. For portfolio requests, run the same evidence standard against every repository and create one authoritative registry.

## Easy invocation

- `Use Repo Auditor on <repository URL>.`
- `Audit every repository under <owner>.`
- `Run Repo Auditor on all mboza0324 repositories.`

## Required inputs

- repository URL, accessible repository, or GitHub owner
- target environment when known
- reference governance repository when named
- deployment destination when applicable

## Mandatory discovery

Read before scoring or recommending changes:

1. repository root and complete tracked-file structure
2. `AGENTS.md`, `AGENT_RULES.md`, `AGENT_USAGE_RULES.md`, and equivalent instruction files
3. README, architecture, testing, security, deployment, contribution, roadmap, and decision documentation
4. branches, open and recently closed pull requests, issues, releases, and tags
5. dependency manifests and lockfiles
6. CI/CD workflows and their current results
7. tests, fixtures, migrations, generated artifacts, deployment configuration, secret handling, and environment examples
8. evidence of the intended product and current lifecycle state

Do not infer that a repository builds merely because documentation says it does.

## Audit dimensions

Score each repository using concrete evidence across:

- product purpose and acceptance criteria
- implementation completeness
- automated tests
- linting, formatting, and type checking
- dependency determinism
- security and secrets boundaries
- data integrity and migration safety
- CI/CD correctness and least privilege
- deployment readiness
- documentation accuracy
- maintenance, ownership, duplication, and supersession
- external blockers such as credentials, hardware, legal review, merchant approval, or human editorial review

## Lifecycle states

Use one of these states:

- `scaffold`: repository contains setup or intent but no validated product path
- `specification`: requirements exist but working implementation is absent
- `prototype`: a narrow path runs but core acceptance criteria are not validated
- `mvp`: core workflow is implemented and tested locally or in CI
- `late_mvp`: broad intended workflow is implemented; production integration gaps remain
- `maintained`: intended scope is validated, documented, and governed by reliable CI
- `repair_required`: current implementation or delivery evidence contains material failures
- `external_blocker`: code-complete scope is separated from a credential, hardware, legal, merchant, or human-review gate
- `superseded`: repository is intentionally replaced or converted to a compatibility pointer
- `archived_candidate`: repository has no unique supported purpose and should not receive new implementation work

## Evidence rules

- Cite exact files, commits, pull requests, workflow runs, test counts, and observed failures.
- Treat stale documentation and historical workflow results as low-trust evidence.
- Record unknowns instead of filling them with assumptions.
- Separate code completeness from production deployment.
- Never label a repository production-ready while a known failing check, placeholder, TODO implementation, missing lockfile, unsafe secret pattern, or unverified critical integration remains.
- Do not count a draft or open PR as shipped.

## Portfolio output

For a portfolio audit, produce a deterministic registry containing at minimum:

- repository name and URL
- purpose
- default branch and latest material commit
- lifecycle state
- completion score with scoring rationale
- priority (`P0` through `P3`)
- primary gap
- tests/build/CI evidence
- deployment state
- external blockers
- duplicate/supersession relationship
- recommended Repo Builder action
- last-audited timestamp

Generate both human-readable Markdown and machine-readable JSON. Validate that every repository under the requested owner is represented exactly once.

## Priority rules

- `P0`: unsafe, corrupted, misleading, known-failing, or blocks a critical product
- `P1`: incomplete core workflow or major reliability/security gap
- `P2`: functional product with bounded integration, deployment, or maintenance work
- `P3`: maintained, intentionally superseded, research-only, or externally gated with code complete

## Completion standard

The audit is complete only when:

- every in-scope repository is represented
- evidence is current enough to support the status
- unsafe and stale pull requests are identified
- duplicates and wrong-repository work are identified
- code gaps are separated from external gates
- each unfinished repository has a concrete Repo Builder entry action
- reports regenerate deterministically and pass their validator

The Repo Auditor is read-only with respect to application repositories. It may create or update the dedicated audit registry repository when the user requested a durable portfolio report.
