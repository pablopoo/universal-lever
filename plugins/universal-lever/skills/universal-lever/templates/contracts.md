# Task records

Use only the sections needed for this task. Store filled records in a task-scoped directory chosen for the project; do not edit this package's templates.

## Brief

- Original ask (verbatim):
- Current behavior and source evidence:
- Outcome / owner:
- Done when / acceptance commands:
- Scope / non-goals / neighbors:
- Constraints (source, scope, expiry):
- Allowed actions (source, scope, expiry):
- Budget (time, attempts, compute, calls):
- Dependencies / integration order:
- Stop on success / give-up / escalation:
- Report cadence / destination:

## Measurement card

| Field | Value |
|---|---|
| User-visible outcome | |
| Primary metric, direction, statistic | |
| Correctness / cost / quality guards | |
| Instrument command and inputs | |
| Snapshot identity and environment | |
| A/A samples and spread | |
| Baseline, n, timestamp, raw evidence | |
| Preregistered keep bar and sample plan | |
| Generalization check | |
| Budget and stop rule | |
| Allowed actions and source | |
| Ledger path | |

## Experiment ledger

| ID / date | Hypothesis | Control / candidate IDs | Raw evidence | Metric control → candidate / n / noise | Guards | Keep / drop / inconclusive | Reason / next step |
|---|---|---|---|---|---|---|---|

## Delivery / handoff

| Unit / owner | Input → current output identity | Depends on | Acceptance evidence on output | Evidence state | Integration wave | Remaining action / risk |
|---|---|---|---|---|---|---|

## Run contract

PARAMETERS: task_id, scope, trigger, filters, input_revision, mode, allowed_actions,
budget, state_path, stop_rule.

CONTRACT: inspect current state; deduplicate; act only within allowed actions;
validate; checkpoint; record one outcome; exit. Dry-run disables or redirects writes.

Run record: timestamp, task_id, input_revision, contract_revision, owner,
authority_source, outcome ACTED/NOOP/BLOCKED, evidence_paths, budget_used, next_step.

## Status

Outcome: baseline → observed (or not measured). Evidence state: planned / implemented /
validated / integrated / deployed / observed. Checks actually run: command, identity,
result. Blockers and limits: reason. Next action and owner: ...
