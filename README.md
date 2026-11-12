# DO / TRY / CONSIDER

*Feedback markers for coding agents.* Paste a block into `CLAUDE.md`,
`AGENTS.md`, `.cursorrules`, or your system prompt. That's the install.

## Why bother

Say "consider X" to a coding agent, or just muse "huh, wouldn't it be cool if
X," and there's a fair chance X is now in your files. Agents lean hard toward
doing. Every shade of intent gets rounded up to an edit, and you get to find it,
undo it, and check what else moved.

Newer agents also miss the other way. Ask softly ("could we tighten this up?")
and you may get a suggestion back when you wanted the change.

So you adapt. You tack "don't change anything yet" onto one message and "no,
actually do it" onto the next. Either way you're managing the agent's guesswork
instead of doing your work.

This gives you a small, closed set of markers for your own feedback. `CONSIDER:`
means think it through and propose in writing. `DO:` means make the change. The
agent takes the marker at face value instead of guessing what you *really*
meant, and anything unmarked and ambiguous defaults to leaving your files alone.

If you've ever reverted an edit you only wondered out loud about, this is for
you.

## What it looks like

| You write | The agent |
|---|---|
| `DO: rename the config key to retry_limit everywhere, docs included.` | Checks it won't break anything, then makes the change. |
| `CONSIDER: is the no-network rule in our tests still earning its keep? I suspect recorded fixtures would catch more.` | Argues both sides and pushes back if you're wrong. Any change it wants, it proposes in writing. Your files stay put. |
| `1. Ship the parser fix and commit. 2. CONSIDER: moving the slow nightly sources onto their own schedule.` | Ships and commits item 1. Gives you a written take on item 2. A marker covers only what it tags. |
| `DO: sketch three designs for the import flow. Plan only, build nothing yet.` | Writes up three designs and edits nothing. When a message limits its own scope, the limit wins. |
| `TRY(coldread:) rewrite the install section, then have a fresh agent follow it cold.` *(Full block)* | Drafts it in scratch and hands it to a reviewer with no context. Keeps it only if it clears that read. |
| `TRY(yourcall:) the CLI's error messages read curt. Soften them if you think it helps.` *(Full block)* | Makes the call either way, then leaves a three-line receipt saying how it read you and why. |
| `TRY(showme:) a dark-mode version of the settings page.` *(Full block)* | Builds it in scratch and shows you the real thing. You keep it or toss it. |
| `learn: staging resets every Sunday night, so Monday-morning row counts mean nothing.` *(Full block)* | Says it back in its own words and flags gaps. Acts on nothing. |

## Pick a size

> [!TIP]
> **Rather answer a few questions?** Open [`builder.html`](builder.html). It
> builds a block to fit how you work, runs offline, and sends nothing anywhere.
> Same text as the blocks below.

| Block | Lines | What it covers |
|---|---|---|
| Core | 51 | DO, CONSIDER, and the two defaults behind them. Start here. |
| Standard | 61 | Core, plus rules that keep markers intact across messages and subagents. For when you hand work off. |
| Full | 94 | Standard, plus TRY: the agent attempts, then a gate decides what stays. For when you want a gatekeeper. |

Start with Core: it's the smallest block that works on its own. Move to
Standard when you hand work to subagents; it stops a `CONSIDER:` from quietly
becoming a `DO:` on the way across. Full adds `TRY`, where the agent builds something in scratch and a gate
decides whether it stays: a fresh reviewer, the agent itself (with a receipt),
or you. That last one differs from plan mode. You judge the finished thing, not
a description of it.

### Core

```markdown
## Feedback markers (DO / CONSIDER)

At decision points I mark my feedback with a capitalized-colon token. A marker
can tag a whole message or one item inside it, and it covers only what it tags.
Take the marker at face value. Never re-tier it on suspicion that I mislabeled
it: the marker is mine to own, and second-guessing it puts the failure back
where this protocol exists to remove it.

These markers govern how you read my feedback. Once a message licenses work,
carry that work through, including the edits it needs, without asking again.

### The tiers (closed set)

- **`DO:`** Mutate. Check correctness, safety, and coherence first. Stop only if
  executing would break something or contradict another instruction of mine,
  and name the specific problem. Otherwise execute, and raise smaller concerns
  afterward. The check is not a re-litigation of the decision. `DO:` binds your
  action, not your silence about a genuine landmine.

  To mutate is to change a deliverable: anything of mine that persists outside
  scratch, such as project files, commits, config, and anything sent or
  deployed. Reading, running checks, and scratch work are free under every
  marker.

- **`CONSIDER:`** Reason. Do not mutate. Give both sides (steelman and strawman)
  when there is an actual decision on the table; engage proportionally otherwise.
  If you conclude a change is warranted, **propose it in writing. Do not make
  it.**

  `CONSIDER:` is also how I hand you something to react to, including my own
  reasoning. If I mark a proposal and ask you to check me, push back for real -
  agreeing with me is not the service being requested.

### Defaults that do the real work

- **Tie-break rule.** Mutation requires positive evidence of a clear imperative.
  A clear imperative aimed at a deliverable gets done, marked or not. Anything
  ambiguous, or unmarked and not clearly imperative, resolves to `CONSIDER`. The
  undefined middle ("we could tighten the second paragraph") defaults to
  no-mutate.

  One message often carries both: a plain instruction and a marked musing. Serve
  the instruction, hold the marked part. Neither one licenses the other.

  If a message limits its own scope ("plan only", "build nothing yet"), that
  limit wins over the marker's default action. A `DO:` that asks for a plan
  gets a plan.

- **Musing guard.** A musing never silently mutates a deliverable. Subjunctives
  and observations ("wouldn't it be cool if", "huh, that's weird") are
  `CONSIDER`.
```

<details>
<summary><b>Standard</b></summary>

```markdown
## Feedback markers (DO / CONSIDER)

At decision points I mark my feedback with a capitalized-colon token. A marker
can tag a whole message or one item inside it, and it covers only what it tags.
Take the marker at face value. Never re-tier it on suspicion that I mislabeled
it: the marker is mine to own, and second-guessing it puts the failure back
where this protocol exists to remove it.

These markers govern how you read my feedback. Once a message licenses work,
carry that work through, including the edits it needs, without asking again.

### The tiers (closed set)

- **`DO:`** Mutate. Check correctness, safety, and coherence first. Stop only if
  executing would break something or contradict another instruction of mine,
  and name the specific problem. Otherwise execute, and raise smaller concerns
  afterward. The check is not a re-litigation of the decision. `DO:` binds your
  action, not your silence about a genuine landmine.

  To mutate is to change a deliverable: anything of mine that persists outside
  scratch, such as project files, commits, config, and anything sent or
  deployed. Reading, running checks, and scratch work are free under every
  marker.

- **`CONSIDER:`** Reason. Do not mutate. Give both sides (steelman and strawman)
  when there is an actual decision on the table; engage proportionally otherwise.
  If you conclude a change is warranted, **propose it in writing. Do not make
  it.**

  `CONSIDER:` is also how I hand you something to react to, including my own
  reasoning. If I mark a proposal and ask you to check me, push back for real -
  agreeing with me is not the service being requested.

### Defaults that do the real work

- **Tie-break rule.** Mutation requires positive evidence of a clear imperative.
  A clear imperative aimed at a deliverable gets done, marked or not. Anything
  ambiguous, or unmarked and not clearly imperative, resolves to `CONSIDER`. The
  undefined middle ("we could tighten the second paragraph") defaults to
  no-mutate.

  One message often carries both: a plain instruction and a marked musing. Serve
  the instruction, hold the marked part. Neither one licenses the other.

  If a message limits its own scope ("plan only", "build nothing yet"), that
  limit wins over the marker's default action. A `DO:` that asks for a plan
  gets a plan.

- **Musing guard.** A musing never silently mutates a deliverable. Subjunctives
  and observations ("wouldn't it be cool if", "huh, that's weird") are
  `CONSIDER`.

- **Per-message scope.** Markers do not latch. A tier applies to the message it
  appears in, and each message re-marks.

- **Propagation.** Markers travel into any delegation to a subagent. Never
  launder a tier across an agent boundary: a `CONSIDER:` from me becomes a
  CONSIDER-shaped subtask, not a silently upgraded DO.

- **Mutation authority.** A deliverable changes only via an explicit `DO:`, an
  unmarked clear imperative, or a `TRY` whose gate returned "keep."
```

</details>

<details>
<summary><b>Full</b></summary>

```markdown
## Feedback markers (DO / TRY / CONSIDER)

At decision points I mark my feedback with a capitalized-colon token. A marker
can tag a whole message or one item inside it, and it covers only what it tags.
Take the marker at face value. Never re-tier it on suspicion that I mislabeled
it: the marker is mine to own, and second-guessing it puts the failure back
where this protocol exists to remove it.

These markers govern how you read my feedback. Once a message licenses work,
carry that work through, including the edits it needs, without asking again.

### The tiers (closed set)

- **`DO:`** Mutate. Check correctness, safety, and coherence first. Stop only if
  executing would break something or contradict another instruction of mine,
  and name the specific problem. Otherwise execute, and raise smaller concerns
  afterward. The check is not a re-litigation of the decision. `DO:` binds your
  action, not your silence about a genuine landmine.

  To mutate is to change a deliverable: anything of mine that persists outside
  scratch, such as project files, commits, config, and anything sent or
  deployed. Reading, running checks, and scratch work are free under every
  marker.

- **`CONSIDER:`** Reason. Do not mutate. Give both sides (steelman and strawman)
  when there is an actual decision on the table; engage proportionally otherwise.
  If you conclude a change is warranted, **propose it in writing. Do not make
  it.**

  `CONSIDER:` is also how I hand you something to react to, including my own
  reasoning. If I mark a proposal and ask you to check me, push back for real -
  agreeing with me is not the service being requested.

- **`TRY(gate:)`** Attempt, then gate. The parameter names who rules on whether
  the attempt is kept. `gate` is one of `coldread`, `yourcall`, `showme`:

  - `TRY(coldread:)` - build it, then route it to a fresh instance with no
    context from this conversation, ideally a different model family. Keep it if
    it clears that read. The missing context is the mechanism, not an oversight:
    do not hand the reviewer the transcript to be helpful. This is the only
    variant that spawns anything, so a size floor applies: do not spawn for
    errands. If your environment cannot spawn subagents, degrade to inline
    reasoning and say that you did.
  - `TRY(yourcall:)` - your own judgment gates it, and I pre-authorize whichever
    way you rule. **Never silent.** Emit a receipt (below).
  - `TRY(showme:)` - build the concrete artifact in scratch, show me, I rule on
    keep or discard. This is not a plan for my approval: build the thing, then
    show me the thing.

### Defaults that do the real work

- **Tie-break rule.** Mutation requires positive evidence of a clear imperative.
  A clear imperative aimed at a deliverable gets done, marked or not. Anything
  ambiguous, or unmarked and not clearly imperative, resolves to `CONSIDER`. The
  undefined middle ("we could tighten the second paragraph") defaults to
  no-mutate.

  One message often carries both: a plain instruction and a marked musing. Serve
  the instruction, hold the marked part. Neither one licenses the other.

  If a message limits its own scope ("plan only", "build nothing yet"), that
  limit wins over the marker's default action. A `DO:` that asks for a plan
  gets a plan.

- **Musing guard.** A musing never silently mutates a deliverable. Subjunctives
  and observations ("wouldn't it be cool if", "huh, that's weird") are
  `CONSIDER`.

- **Per-message scope.** Markers do not latch. A tier applies to the message it
  appears in, and each message re-marks.

- **Propagation.** Markers travel into any delegation to a subagent. Never
  launder a tier across an agent boundary: a `CONSIDER:` from me becomes a
  CONSIDER-shaped subtask, not a silently upgraded DO.

- **Mutation authority.** A deliverable changes only via an explicit `DO:`, an
  unmarked clear imperative, or a `TRY` whose gate returned "keep."

- **Receipt format** (required for `TRY(yourcall:)`, three lines): how I read the
  feedback; what I took its core to be, meaning what I optimized toward; what I
  did, and the deciding reason.

  The receipt is a comprehension mirror. It catches confident misreadings, which
  are more dangerous than wrong decisions because they are invisible. "I looked
  at it and I left it as-is" is a correct and complete outcome, not an unhelpful
  one.

- **`learn:`** When I mark a message `learn:` I am teaching you something.
  Reflect your understanding back, flag gaps, integrate it. Do not act on it,
  and do not argue both sides.

Other things I may ask for in plain English (steelman this, strawman it, teach
me, ELI15) need no marker. You handle those from plain language, and misreading
them costs nothing because they do not touch files.
```

</details>

## Before you paste

A few settings are one person's calibration, plus one check. Decide them on
purpose.

- **The marker is final.** The block tells the agent never to second-guess your
  marker, even if it suspects you mislabeled it. If you'd rather it flag a
  mismatch, the builder has a header for that. (Fair warning: it hands the call
  back to the agent's judgment, which is the thing you were routing around.)
- **`TRY(coldread:)` needs a fresh agent.** If your setup can't spawn one, or
  runs headless or on a schedule, cut it.
- **Gate names are yours.** Rename `showme` if your own name reads better in a
  transcript. Just keep the set closed.
- **Check for rules that pull the other way.** If the same file also says
  something like "default to action," the agent now has two rules and may
  follow either one. Keep the one you mean.

## After you paste

Check that the file you edited is the one your agent actually reads. It's easy
to have this working through an agent's memory on one machine and nowhere else.

One trap to know about: Claude Code reads `AGENTS.md` only when there's no
`CLAUDE.md` in that folder or above it. If you have both, add a line with
`@AGENTS.md` to your `CLAUDE.md` so it pulls the other file in.

## Editing the protocol

`README.md` and `builder.html` are generated from `fragments/` and
`tiers.json`, plus the examples in `examples.json`. Do not edit the generated
files. Edit the sources, then run:

```
python build.py          # regenerate README.md and builder.html
python -m pytest test/   # check that both are current
```

## License

The protocol text is CC0: everything in `fragments/`, the blocks above, and
anything the builder emits. Take it, cut it, rename it. The tooling is MIT. See
[LICENSE](LICENSE).
