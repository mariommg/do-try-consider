# DO / TRY / CONSIDER

**Feedback markers for coding agents.** Paste a block into `CLAUDE.md`,
`AGENTS.md`, `.cursorrules`, or your system prompt, and you're installed 
and ready to go.

**Why you may want this.** Today's models have a very powerful bias towards
action. If you're anything like me and you tend to think non-linearly (with
asides, meta-commentary, mental footnotes) - you may be getting in the habit
of censoring your own valuable thinking just so your agents don't run off on
wild goose chases, doing the things you merely wanted to learn about.

If you think-aloud something like "huh, wouldn't it be cool if X" at a 
coding agent, and there's a fair chance X is now in your files. (Ask too 
softly and you get the reverse: a suggestion when you wanted the change.) 
Either way, you end up _managing the agent's guesswork instead of doing 
your own work_.

So: mark your intent. `CONSIDER:` means "think it through and tell me". `DO:`
means "make the change". The agent takes your marker *at face value*, and
anything unmarked and unclear leaves your files alone.

That's most of it. There's some more polish available, but it's optional.

## What it looks like

| You write | The agent |
|---|---|
| `DO: rename the config key to retry_limit everywhere, docs included.` | Makes the change, after a quick check that it won't break anything. |
| `CONSIDER: is the no-network rule in our tests still earning its keep?` | Argues it out and pushes back if you're wrong. Touches nothing. |
| `1. Ship the parser fix. 2. CONSIDER: moving the slow nightly jobs to their own schedule.` | Ships item 1. Writes up item 2. |
| `DO: sketch three designs for the import flow. Plan only, build nothing yet.` | Writes up three designs. You said plan only, so that wins. |
| `TRY(coldread:) rewrite the install section, then have a fresh agent follow it.` *(Full block)* | Drafts it in scratch. Keeps it only if a reviewer with no context can follow it. |
| `TRY(yourcall:) the CLI's error messages read curt. Soften them if you think it helps.` *(Full block)* | Decides, then leaves a three-line receipt on how it read you. |
| `TRY(showme:) a dark-mode version of the settings page.` *(Full block)* | Builds it in scratch and shows you the thing itself, not a plan for it. |
| `learn: staging resets every Sunday night, so Monday row counts mean nothing.` *(Full block)* | Says it back in its own words. Acts on nothing. |

## Pick a size

> [!TIP]
> **Want an interactive installer?** The [builder](builder.html) makes a block
> that fits how you work. It runs offline and sends nothing anywhere.

| Block | Lines | What it covers |
|---|---|---|
| Core | 51 | DO, CONSIDER, and the defaults behind them. Start here. |
| Standard | 62 | Adds rules for multi-message work and subagents. |
| Full | 95 | Adds TRY: attempt first, then a gate decides what stays. |

**I recommend:** Start with Core, and step up to a bigger block once you've 
got the mental habit of tagging feedback and want more channels to do it.

### Core

```markdown
## Feedback markers (DO / CONSIDER)

At decision points I mark my feedback with a token ending in a colon. A marker
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

At decision points I mark my feedback with a token ending in a colon. A marker
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
  appears in, and a marker does not carry into my next message.

- **Propagation.** Markers travel into any delegation to a subagent. Never
  launder a tier across an agent boundary: a `CONSIDER:` from me becomes a
  CONSIDER-shaped subtask, not a silently upgraded DO.

- **Mutation authority.** A deliverable changes only via an explicit `DO:`, an
  unmarked clear imperative, or, where `TRY` is in use, a `TRY` whose gate
  returned "keep."
```

</details>

<details>
<summary><b>Full</b></summary>

```markdown
## Feedback markers (DO / TRY / CONSIDER)

At decision points I mark my feedback with a token ending in a colon. A marker
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
  appears in, and a marker does not carry into my next message.

- **Propagation.** Markers travel into any delegation to a subagent. Never
  launder a tier across an agent boundary: a `CONSIDER:` from me becomes a
  CONSIDER-shaped subtask, not a silently upgraded DO.

- **Mutation authority.** A deliverable changes only via an explicit `DO:`, an
  unmarked clear imperative, or, where `TRY` is in use, a `TRY` whose gate
  returned "keep."

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

- **The marker is final.** The agent never second-guesses it. Would you rather
  it flag a mismatch? The builder has a header for that (it hands the call back
  to the agent, which is what you were routing around). _This takes a little mental
  adjustment (or at least, it did for me).
- **Look for rules that pull the other way,** like "default to action." Give an
  agent two conflicting rules and it may follow either.
- **`TRY(coldread:)` needs a fresh agent.** If your setup can't spawn one, cut it.
Most modern harnesses will do this seamlessly, but DO: check your setup.

## After you paste

Check that your agent actually reads the file you edited. (Claude Code skips
`AGENTS.md` when there's a `CLAUDE.md`; put `@AGENTS.md` in the `CLAUDE.md` to
pull it in.)

## Editing these files

`README.md` and `builder.html` are generated. Edit `fragments/`, `tiers.json`,
or `examples.json`, then run:

```
python build.py          # regenerate README.md and builder.html
python -m pytest test/   # check that both are current
```

## License

The protocol text is CC0. Take it, cut it, rename it. The tooling is MIT. See
[LICENSE](LICENSE).
