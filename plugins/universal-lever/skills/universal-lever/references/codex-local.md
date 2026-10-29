# Codex local: execution procedure

Use the tools actually exposed by the current Codex host. Tool names and multi-agent availability vary by version; this guide does not change configuration or install anything.

## 1. Establish the workspace

Read applicable `AGENTS.md` instructions and the user request. Use the host shell tool (often `exec_command`) and file editing tool (often `apply_patch`). Run independent reads together when supported. Never assume the current directory is the intended project.

In a Git project inspect:

```sh
git rev-parse --show-toplevel
git status --short
git diff --stat
git diff --cached --stat
git branch --show-current
git worktree list --porcelain
git rev-parse HEAD
```

If Git is missing or this is not a repository, continue with local snapshots/patches; do not initialize a repository merely to satisfy this skill. Empty branch output means detached HEAD: use an explicit base identity and preserve any host-managed checkout; do not assume the session is broken.

Record dirty state before work. A commit hash identifies committed inputs only: staged/unstaged edits and relevant untracked inputs must also be captured in a scoped snapshot/digest or explicitly excluded from the measurement. Do not hash secrets or unrelated private files into reports. No automatic stash, reset, clean, checkout over edits or force operations. A linked worktree does not contain the user's uncommitted changes. If the task depends on them, use the current tree with a single writer or copy only reviewed task inputs into an isolated snapshot, recording provenance.

Choose a task-scoped state directory outside measured source inputs, for example a user-selected sibling directory holding `brief.md`, `ledger.md`, `status.md` and raw outputs. Do not change `.gitignore` just to hide records.

## 2. Isolate candidates with local Git

For a clean committed baseline, resolve an explicit commit and create unique local branches/worktrees. The following example uses a coordinator-assigned unused path and branch name; adapt them to the project and verify absence of collisions first:

```sh
git rev-parse HEAD
git worktree add -b lever/task-a ../project-task-a <base-commit>
```

Replace `<base-commit>` with the observed object ID; it is not literal shell input. Run the worker's commands in `../project-task-a`. Worktree metadata is shared with the repository; select a writable allowed location and respect sandbox policy. If creation is denied or unsupported, use isolated copies/patches or serialize work without weakening host restrictions.

One candidate per worktree, one hypothesis per experiment. Keep control at the same baseline and avoid concurrent timing benchmarks on the same hardware unless resource contention is part of the measurement design. Parallel construction does not imply valid parallel measurement.

No remote operations are required. Commit task-owned files only if task/host policy permits; use explicit paths, never blanket staging of a dirty user tree. If commits are not appropriate, return a scoped patch plus relevant new files and a manifest. Review patches and new files for unintended or sensitive contents.

## 3. Delegate with native Codex subagents

Discover the available agent tools from the current tool catalog. Examples of capability families, not mandatory API names:

| Capability | Possible host tools | Required behavior |
|---|---|---|
| Start worker | `spawn_agent` | Task, explicit working directory, ownership, acceptance and budget |
| Send correction / resume | `send_input`, `send_message`, `followup_task` | Use the host's documented resume semantics; a message may not restart an idle worker |
| Wait / inspect | `wait`, `wait_agent`, `list_agents` | Prefer completion events; use bounded waits consistent with required user updates |
| Stop / release | `close_agent`, `interrupt_agent` | Only if exposed; preserve unfinished work and checkpoint first |

Use native tools directly, not invented CLI commands or recursive `codex` subprocesses. Some versions support roles such as explorer/worker, or context-fork options; use only documented arguments in the live schema. Keep inherited model defaults unless the user or applicable policy specifies otherwise. Do not edit `~/.codex/config.toml` or enable experimental features as a side effect. If tools are absent or delegation is disallowed, execute sequentially and state that choice only when it matters.

Good delegations: independent module changes, control/candidate preparation, read-only investigation, or fresh-context review. Keep tightly coupled edits together. Worker count must fit host limits and task budget; start small rather than filling every slot.

### Worker envelope

```text
Task: parser-cache / candidate A
Working directory: /absolute/path/project-task-a
Baseline: <observed commit or snapshot identity>
Ownership: src/parser/cache.py and tests/test_cache.py only
Goal: reduce parsing latency without changing results
Acceptance: <project's actual targeted test and benchmark commands>
Constraints: no remote writes; no other files; preserve other contributors' work
Budget: <finite attempts/time>; no nested agents unless explicitly delegated
Return: changed paths, diff/commit or patch identity, commands/results,
        raw measurement paths, unresolved risks, next action
```

Workers must read instructions applicable to their working directory. A shared transcript or filesystem is not exclusive ownership. Never send two writers to the same paths in the same checkout. The coordinator owns shared contracts, lockfiles, integration and the ledger unless explicitly assigned otherwise. Workers report results; the coordinator checks them rather than treating a completion message as proof. Before takeover, checkpoint and stop/interrupt the prior writer using available host tools, then confirm it is no longer writing before assigning a replacement. Idle status alone is not proof of termination. If termination cannot be confirmed, keep the replacement read-only or use a separate snapshot; do not permit competing writers.

For review, give a separate read-only worker the exact diff, context and acceptance criteria without the author's preferred verdict. A separate session using the same model is fresh-context review, not cross-model review. With no separate worker, label the skeptical pass self-review.

## 4. Integrate locally and validate

Inspect worker changes and evidence first. Serialize integration. Confirm the target has not advanced and user edits are preserved. With a clean appropriate target, apply the reviewed commits in dependency order using local Git, for example `git cherry-pick <reviewed-commit>`, only within integration authority. With patch output, inspect then use `git apply --check <patch>` before applying; include and verify new files from the manifest. Shared-file coupling requires deliberate ordering, not automatic merging.

When the user requested edits to their current tree, local application of those edits is part of implementation. Moving a named branch or integrating a separate development branch must match the requested scope. If the target is dirty and integration could overwrite user work, preserve it and deliver the isolated result or choose a non-overwriting method; do not automatically stash/reset. Resolve routine task-owned conflicts, but surface conflicts requiring a product decision or risking unrelated work.

After integration, run the relevant acceptance checks on the final combined working tree. Record the final commit **and dirty state/snapshot** so a clean worker result cannot be mistaken for validation of later edits. Review `git diff`, `git diff --cached` and new task-owned files for scope. A green worker test does not establish that integrated tests pass.

Only remove a worktree/branch created by this task after confirming its useful results are preserved and it has no uncommitted work. Never use force cleanup. If cleanup is unsafe, retain it and report the path.

## 5. Local recurrence and completion

A Codex session can run a bounded local loop while alive. Session completion is not a persistent daemon. For recurring work, generate a manual runbook or a scheduler specification (for example cron, systemd timer or the host's available automation facility). Create or enable it only when requested and supported; use absolute working directories, deduplication, bounded runtime and logs. Do not assume shell access implies permission to install a service.

Completion report: result, final artifact location, Git branch/commit or snapshot,
checks actually run and observed outcomes, kept/dropped/inconclusive candidates,
remaining limitations, and any retained worktrees. No remote publication is implied.
