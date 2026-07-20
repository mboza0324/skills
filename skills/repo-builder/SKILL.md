---
name: repo-builder
description: Take an audited GitHub repository from its current state to a validated, documented, merge-ready delivery while preserving architecture and separating external gates from code completion.
version: 1.0.0
---

# Repo Builder

## Purpose

Execute the highest-priority action from a Repo Auditor report and continue through implementation, debugging, validation, pull-request review, and merge. Do not stop at a plan, partial code, an unverified PR, or a handoff.

## Easy invocation

- `Use Repo Builder on <repository URL>.`
- `Build the next repository from the portfolio audit.`
- `Use Repo Auditor, then Repo Builder, on all repositories under <owner>.`
- `Use mboza0324/looping to finish this repository.`

## Required inputs

- repository URL or accessible repository
- current Repo Auditor evidence, when available
- target environment and deployment destination, when known
- reference governance repository, especially `mboza0324/skills` and `mboza0324/looping`

## Mandatory startup

1. identify the repository, default branch, working branch, and current head
2. read repository-specific instruction and governance files in their required order
3. inspect the complete relevant architecture, tests, dependencies, workflows, deployment files, and open pull requests
4. verify the Repo Auditor finding against current repository state
5. define acceptance criteria, rollback, integration points, risks, and test strategy
6. create a focused feature or repair branch

If `.gaai/core/README.md` is required by repository controls and missing, follow the repository's pinned installation process. Never improvise an unpinned dependency source.

## Delivery loop

Repeat until the acceptance criteria are met:

1. reproduce the current defect or missing capability
2. identify the root cause rather than patching symptoms
3. implement the smallest complete change that preserves working behavior
4. add or improve regression tests
5. run available formatting, linting, type checking, unit, integration, build, packaging, migration, and deployment-configuration checks
6. inspect logs and artifacts for hidden failures
7. repair every failure introduced or exposed by the change
8. review the full diff for generated files, secrets, unrelated edits, placeholders, TODOs, copied build outputs, and unsafe permissions
9. update documentation to match verified behavior
10. repeat the validation suite on the final head

## Pull-request rules

Open a draft PR only when a remote branch or CI environment is needed to continue validation. A draft PR is a work surface, not completion.

Before marking ready, the PR body must include:

- summary and acceptance criteria
- root cause or product gap
- technical implementation
- files modified
- test, lint, type, build, and deployment evidence
- workflow run identifiers when CI is used
- security and data considerations
- deployment considerations
- rollback strategy
- explicit external gates, if any

Do not mark ready or merge a PR containing:

- known test failures
- placeholder or TODO implementations in required scope
- broken or overprivileged workflows
- unresolved merge conflicts
- unreviewed mass-generated files
- dependency manifests without required lockfiles
- hard-coded credentials or machine-specific paths
- misleading production-readiness claims
- unverified critical assumptions

## External gates

When credentials, hardware, merchant approval, legal review, production accounts, or human editorial approval are genuinely required:

- complete and validate all code that can be completed without the gate
- provide mocks, contract tests, fixtures, and operator instructions
- record the exact gate and evidence still required
- do not fabricate successful live validation
- do not label the gated integration production-ready
- keep the PR draft when repository policy requires live evidence before merge; otherwise merge only the independently useful, fully tested code scope and track the gate separately

## Unsafe or obsolete work

Close rather than merge pull requests that are zero-change, wrong-repository, superseded, retain known failures, overwrite newer architecture, include unreviewable generated artifacts, or violate the repository's security and delivery rules. Preserve useful ideas by rebuilding them cleanly from current `main`.

## Merge standard

Merge only when:

- acceptance criteria are met
- final CI and local-equivalent validation pass
- required lockfiles and generated artifacts are deterministic
- docs describe reality
- the diff is focused and reviewable
- rollback is clear
- no known code blocker remains

After merge:

1. verify the default branch contains the intended files or artifact metadata
2. verify required post-merge workflows when applicable
3. update the portfolio audit evidence
4. select the next repository by priority and continue without waiting for approval unless a material user decision or unavailable access is required

## Portfolio mode

For an all-repository request:

- process every repository exactly once from the authoritative audit registry
- work in priority order, while allowing CI waits to overlap with another repository
- record merged, externally gated, superseded, archived-candidate, and unresolved states distinctly
- do not declare portfolio completion while any repository lacks either validated delivery or an explicit, evidence-backed lifecycle resolution

## Completion standard

Completion means validated delivery on the default branch, or an explicit lifecycle resolution that is itself merged and verified. An open PR, a draft, a plan, a code dump, or a status report is not completion.
