# Capabilities and authority

## Portable bindings

| Concept | Local baseline | Optional adapter |
|---|---|---|
| Work item | Markdown row with stable ID and acceptance check | Any task tracker |
| Change identity | Immutable snapshot plus content digest | Local Git commit ID |
| Candidate isolation | Separate directories or patches | Local Git branches/worktrees |
| Validation | Local command and saved output | Any build/check service |
| Review | Local findings document | Any review system |
| Integration | Apply a validated patch to the intended target | Merge service or queue |
| Trigger | Explicit invocation | Scheduler or event bus |
| State | Task-scoped Markdown/JSON files | Durable state store |
| Preferences | Explicit session contract | User-selected configuration file |

The baseline needs no hosted account, remote repository, tracker, scheduler or second model. If a capability is missing, use the local baseline where equivalent. Otherwise report the exact gap, deliver a specification or handoff, and do not claim execution.

Use a user-selected task directory outside discovery/install locations for records. Do not create global instructions, edit personal settings or install this skill as a side effect. Templates are documents to fill, not an automatically loaded configuration schema.

## Execution envelope

Record: task ID, owner, source request, scope, acceptance, input snapshot, allowed actions with source/expiry, time and attempt limits, external-call and compute budget, status cadence, stop conditions and handoff target. Absence of a grant for a shared write means prepare the local artifact first. Existing user authorization is sufficient within scope; no special words or approval ritual are required.

Before integration, check the current candidate identity, target identity, required validations and dependencies. Checks on an earlier revision do not validate an edited candidate. Revalidate affected checks after changes. If a target advances, assess compatibility and validate the combined result before integrating. Without atomic compare-and-update support, serialize integration and recheck immediately; disclose any residual race.

Treat timed-out shared writes as unknown outcomes. Read back state before retrying. Use stable task/revision keys for deduplication; apply bounded backoff and shared rate limits. Never override host protections or rewrite another owner's work to unblock yourself.

## Codex use

See [local Git and native subagents](codex-local.md) for concrete execution procedures. Git operations stay local; remote adapters are unnecessary for this profile.

This is a standard `SKILL.md` package, with no runtime hooks or manifest requirement. Once deliberately made available by the user in a supported Codex skill location, invoke it by its skill name or ordinary language. Loading it grants no extra tools. The original product's `/lever` commands, model tiers and scheduling commands are not assumed to exist.

If the host supports workers and delegation is authorized, isolate write ownership and send the execution envelope. Otherwise execute roles sequentially in one session. Never claim independent or cross-model review when only one model/session was used.
