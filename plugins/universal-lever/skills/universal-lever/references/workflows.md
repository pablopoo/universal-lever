# Workflow playbooks

## Loop and experiment

Create the measurement card before changing the measured path. If a card exists, reuse it and update stale baselines explicitly. For vague outcomes inspect available instruments first; ask only the material question still unanswered.

Pin the control snapshot and inputs. Make each candidate one hypothesis with a reversible patch or isolated directory. Use equal workloads, cache treatment and test identities. Interleave paired control/treatment runs rather than comparing an old control with a new treatment under different load. Missing or failed runs remain in the record; do not silently discard reliability failures.

Start with a pilot, then a sample count justified by A/A variation, expected effect and budget. Record all raw pairs and the statistic. Small-sample tail percentiles and unvalidated significance claims are exploratory. Where statistical inference is appropriate, use a justified interval on paired deltas and account for comparing many candidates; do not search until one lucky result wins. Keep only candidates that clear the preregistered threshold and guards. Otherwise drop or mark inconclusive. If the instrument changes, invalidate incompatible rounds and establish a new baseline.

Compose winners in dependency order and validate their combination: improvements may interact. Distinguish the estimate from the realized result; after authorized integration/deployment, observe the real workload over an appropriate window. Do not claim production improvement from a local benchmark.

Example: parser latency has 8% A/A spread. One candidate is 4% faster once. Record inconclusive, not keep; improve the instrument or collect enough planned paired observations. Confirm identical parsed outputs and memory limits before acceptance.

## Brief and delivery

Preserve the original ask verbatim. Record current behavior, outcome owner, observable done-when, constraints with sources, non-goals, neighbors, budget, allowed actions, report cadence and success/give-up/escalation rules. Mark unresolved product decisions; do not invent user agreement.

Build a dependency graph of small acceptance-checkable units. Shared files, fixtures, schemas and quotas count as coupling. Assign one writer per unit. Execute ready units sequentially unless authorized parallel workers are available. A role is a responsibility, not a required extra agent.

At each checkpoint inspect live state, not merely the plan. Run the shortest relevant check inside iterations and the necessary complete gates on the final result. Work until the authorized done-when, a real blocker or the budget limit. Refill work only from agreed sources under an explicit refill policy. Re-plan when attempts stop producing new evidence rather than repeating the same fix.

## Refactor

Separate producer (small behavior-preserving units), packager (reviewable artifacts) and maintainer (target compatibility and checks). Execute these roles sequentially when appropriate. Preserve tests with their code and use a fixed original baseline; do not redefine the metric to manufacture progress. Save stable unit identities and checkpoints; reconcile changed units after rebasing or repackaging. Preserve other owners' work. Publication is optional and separately authorized.

## Maintain and integrate

Inventory current artifact/target IDs, validations, review findings and dependencies. Diagnose failures before rerunning them. Distinguish regressions, infrastructure failures and rate limits. Resolve findings with a fix or evidence-backed disposition.

Create directed edges for declared dependencies and coupled surfaces. For file overlap choose and explain ordering rather than assuming independence. Topologically group independent units; a cycle requires splitting/replanning before integration. Validate each candidate at its current identity and interacting units together. Integrate serially or via an available batch adapter within authority; revalidate downstream candidates after target changes. Otherwise produce a handoff with evidence, order, owners, risks and remaining actions.

## Review

Read the same artifact, surrounding code, acceptance criteria and project rules. When authorized independent reviewers are available, give them identical neutral packets without each other's conclusions. Match findings by mechanism and location. Agreement is a lead, not proof: seek counter-evidence for every surviving finding, including agreed findings.

Report only actionable supported defects: location, reachable failing case, mechanism, consequence, counter-evidence searched and confidence. Rank by impact; omit style noise and unsupported guesses. With one session, do a second skeptical pass and label it self-review. Keep review output local unless posting was requested.

## Automate

First define a portable specification: outcome with denominator, trigger, input filter, allowed actions/tools, dedupe key, checkpoint, budget, quiet exit and failure policy. Prefer events when available with a bounded sweep if needed. Exclude self-generated writes and duplicate input revisions to prevent feedback storms.

Separate variable PARAMETERS from stable CONTRACT. Run every invocation to one recorded ACTED/NOOP/BLOCKED result, then exit. Implement dry-run by withholding write tools or routing writes to a sandbox; a prompt flag alone does not guarantee read-only execution. Test one should-act, one no-op and one blocked historical or synthetic case.

If a scheduler adapter exists and creation is authorized, create disabled, read back its full configuration and compare to the specification. Enable only within the user's grant after dry-run evidence. Otherwise deliver the job specification and manual runner instructions; state that nothing is scheduled. Do not modify your own permissions, prompts or schedule without authority covering that change.

## Health and backlog

Measure time since last evidence advance, useful outputs per eligible input, failures, blocked tasks, ready supply and shared budget. Classify the binding cause: supply, validation, permission, quota, trigger, drift, orphaned owner or integration bottleneck. Propose or apply one authorized corrective change with a prediction and evaluation window; no change can be the right outcome.

Before taking over, confirm the prior writer is inactive, inspect the live artifact and any unknown writes, then record single ownership and continue without overwriting work. Backlog candidates require real source evidence, a unique fingerprint, bounded scope and an executable acceptance check. Deduplicate against active and recently completed work. Do not invent work to keep workers busy.

## Reflect and steer

Use the current conversation or explicitly provided history. Do not assume a product-specific history path or read unrelated private logs. For wider history, establish scope and data handling before access; model processing may transmit text to the configured service. Redact secrets and personal data before inclusion in samples or reports. Validate flagged examples manually and separate human instructions from generated agent text.

Find recurring corrections and check existing rules before adding another. Prefer fixing a test, tool or rule placement over adding prose. Draft one short positive rule with scope, reason and evidence; apply persistent instruction/config changes only within explicit authority. Measure recurrence afterward. Recommendations never silently become user preferences.
