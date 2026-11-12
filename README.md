# DO / TRY / CONSIDER

**A decision-point feedback protocol for coding agents.** Paste a block from
below into `CLAUDE.md`, `AGENTS.md`, `.cursorrules`, a system prompt, or whatever
your setup reads as standing instructions. That is the whole install. No code,
nothing to run.

The name says three tiers. Six weeks of logged use says start with two. Both
statements are in here on purpose, and the evidence is in
[FINDINGS.md](FINDINGS.md).

---

## The problem it solves

Coding assistants have a structural **do-bias**: on receiving feedback they
flatten gradations of intent toward action. "Try X," "consider X," and a bare
musing ("wouldn't it be cool if X") all tend to collapse into a change made to
your files. You then have to notice it, undo it, and re-audit what else moved.

That is a tax you pay on every piece of feedback you give.

So people compensate. They soften real instructions into hedges, which cancels
against the model's up-shift and makes the whole thing worse. You end up managing
the classifier instead of doing the work.

The fix is a small closed set of markers you put on your own feedback, and a
standing instruction that the agent takes them at face value rather than
re-inferring what you must have meant.

---

## Pick a block

| Core | 37 | The two tiers and two defaults that six weeks of logged use actually exercised. Start here. |
| Standard | 48 | Core plus the rules that matter once markers cross a session or an agent boundary. Add this when you delegate to subagents. |
| Full | 81 | Everything, including the attempt-and-gate tier. Unexercised in the reference deployment - adopt it against a symptom, not on spec. |

**Take Core unless you have the symptom.** Two tiers and two defaults, and it
carried a real deployment for six weeks without a single marker being overrun.
The bigger blocks exist because particular problems turned up, and each one names
the problem it answers:

- **Move to Standard** when you start delegating to subagents. The propagation
  rule is what stops a `CONSIDER:` from being quietly upgraded to a `DO:` on the
  way across an agent boundary, which is a failure you will not see from the
  outside.
- **Move to Full** when you catch yourself wanting a gatekeeper who is not you,
  and you already know it going in. Read the caveat under
  [What the evidence says](#what-the-evidence-says) first. This is the part
  nobody used.

`TRY(showme:)` invites an obvious comparison to plan mode, and the difference is
worth having straight. Plan mode gives you a description of intended work and no
artifact. `showme` gives you the artifact, built in scratch, and you rule on the
finished thing. You are judging the work rather than a proposal about the work.
Reach for it exactly when a plan would not tell you enough to judge.

Would rather generate one against your own answers? Open
[`builder.html`](builder.html) in a browser. One file, runs offline, sends nothing
anywhere, and it emits the same text as the blocks below, because both are built
from the same fragments.

### Core

```markdown
## Feedback markers (DO / CONSIDER)

At decision points I mark my feedback with a capitalized-colon token. Take the
marker at face value. Never re-tier it on suspicion that I mislabeled it: the
marker is mine to own, and second-guessing it puts the failure back where this
protocol exists to remove it.

### The tiers (closed set)

- **`DO:`** Mutate. Run a sanity screen first (correctness, safety, coherence),
  then execute if it passes. If it trips a wire, stop and name the specific wire.
  The screen is not a re-litigation of the decision and not deliberation for
  show. `DO:` binds your action, not your silence about a genuine landmine.

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

- **Musing guard.** A musing never silently mutates a deliverable. Subjunctives
  and observations ("wouldn't it be cool if", "huh, that's weird") are
  `CONSIDER`.
```

### Standard

```markdown
## Feedback markers (DO / CONSIDER)

At decision points I mark my feedback with a capitalized-colon token. Take the
marker at face value. Never re-tier it on suspicion that I mislabeled it: the
marker is mine to own, and second-guessing it puts the failure back where this
protocol exists to remove it.

### The tiers (closed set)

- **`DO:`** Mutate. Run a sanity screen first (correctness, safety, coherence),
  then execute if it passes. If it trips a wire, stop and name the specific wire.
  The screen is not a re-litigation of the decision and not deliberation for
  show. `DO:` binds your action, not your silence about a genuine landmine.

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

- **Musing guard.** A musing never silently mutates a deliverable. Subjunctives
  and observations ("wouldn't it be cool if", "huh, that's weird") are
  `CONSIDER`.

- **Per-message scope.** Markers do not latch. A tier applies to the message it
  appears in, and each message re-marks.

- **Propagation.** Markers travel into any delegation to a subagent. Never
  launder a tier across an agent boundary: a `CONSIDER:` from me becomes a
  CONSIDER-shaped subtask, not a silently upgraded DO.

- **Mutation authority.** A deliverable changes only via an explicit `DO:`, an
  unmarked clear imperative, or a `TRY` whose gate returned "keep." Deliverable
  means tracked artifacts. Scratch is free.
```

### Full

```markdown
## Feedback markers (DO / TRY / CONSIDER)

At decision points I mark my feedback with a capitalized-colon token. Take the
marker at face value. Never re-tier it on suspicion that I mislabeled it: the
marker is mine to own, and second-guessing it puts the failure back where this
protocol exists to remove it.

### The tiers (closed set)

- **`DO:`** Mutate. Run a sanity screen first (correctness, safety, coherence),
  then execute if it passes. If it trips a wire, stop and name the specific wire.
  The screen is not a re-litigation of the decision and not deliberation for
  show. `DO:` binds your action, not your silence about a genuine landmine.

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

- **Musing guard.** A musing never silently mutates a deliverable. Subjunctives
  and observations ("wouldn't it be cool if", "huh, that's weird") are
  `CONSIDER`.

- **Per-message scope.** Markers do not latch. A tier applies to the message it
  appears in, and each message re-marks.

- **Propagation.** Markers travel into any delegation to a subagent. Never
  launder a tier across an agent boundary: a `CONSIDER:` from me becomes a
  CONSIDER-shaped subtask, not a silently upgraded DO.

- **Mutation authority.** A deliverable changes only via an explicit `DO:`, an
  unmarked clear imperative, or a `TRY` whose gate returned "keep." Deliverable
  means tracked artifacts. Scratch is free.

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

---

## What the evidence says

The first version of this document shipped honest about having no usage data. It
now has some: 499 messages across 71 sessions of one working deployment, counted
from transcripts rather than recalled. [FINDINGS.md](FINDINGS.md) has the method
and the raw counts. Four things worth knowing before you adopt it:

**`CONSIDER:` is the protocol.** Seventeen of nineteen marked uses, and it held
every time: no marked message was followed by a write the marker had not
licensed. If you take one thing out of this repo, take `CONSIDER:` and the
tie-break rule and leave the rest on the shelf.

**`DO:` is nearly vestigial, and that is the design working.** Two uses in six
weeks, because the tie-break rule already routes unmarked clear imperatives to
action. You do not need to mark what you would get anyway. `DO:` earns its place
mainly as the thing `CONSIDER:` contrasts against, which is a real job but a
smaller one than equal billing suggests.

**The `TRY(gate:)` tier was never invoked.** Not once, in any of its three
variants, in six weeks. The original document predicted exactly this and it was
right.

**The need it was built for is real, though.** It just never shows up as an
instruction. Those same transcripts are full of requests for an independent cold
read, and every one of them arrives as a question: *should we send this to a
fresh reader?* That is `TRY(coldread:)` in substance, wearing `CONSIDER:`.

Which explains the zero. The tier asks you to know, going in, that you want to
pre-authorize a gate. The actual moment is the one where you *have not decided
yet* and want to think out loud about it. A marker that demands a settled
intention cannot serve an unsettled one. Adopt `TRY` knowing that is the gap.

**Adoption took about two and a half weeks.** Seventeen days between writing the
protocol and the first marker turning up in a real message. Budget for that. A
vocabulary you have to remember to use is not free on day one.

---

## Tuning it before you paste

Three settings encode one specific person's calibration. Decide each deliberately
rather than inheriting it.

**1. Who owns a mislabeled marker.** The block says the marker is authoritative
and the agent never re-tiers it. That rests on the author knowing he sometimes
softens a real instruction into a hedge, and preferring to manage that himself.
The alternative is to let the agent reflect the tier back when it reads a
mismatch. That trades one failure mode for another: it moves the decision to the
agent's classifier, which is the thing you distrusted in the first place. Pick
knowingly.

**2. Whether `TRY(yourcall:)` earns its seat.** Honestly, `TRY(yourcall:)` is `DO:`
with a mandatory receipt. Delegating judgment to the agent is only safe when you
already lean yes, which is exactly when the do-bias was harmless anyway. The
receipt is the actual payload: it shows you how your feedback is being read. If
you do not want that signal, cut the tier.

**3. The gate labels.** `showme` is written from your side of the keyboard, and
some people would rather see their own name there so the marker reads back
correctly in a transcript. Rename it freely. Just keep the set closed, and keep
`coldread` saying what it says: the reviewer having no context is the mechanism,
so a name that hides that will eventually get the routing wrong.

Two further notes. `TRY(coldread:)` assumes you can spawn a fresh agent; if you
cannot, either cut it or accept the inline degradation. And if your setup runs
the agent headless or on a schedule, the spawning variant silently stops working
there, so state which parts apply to interactive sessions only.

---

## One thing to check after you paste

Standing instructions are not the only way an agent can learn this, and the other
ways do not travel. In the reference deployment the protocol was live for weeks
via the agent's persistent memory while appearing in **no** `CLAUDE.md` at all.
That works on one machine with one tool, and silently fails to follow you to a
second machine, a teammate, or a different vendor's agent.

So once you have pasted it, go confirm that the file you edited is the one your
agent actually reads. If the protocol only works on the machine where you first
set it up, it is installed in the wrong place.

---

## Repo layout

```
LICENSE                CC0 for the protocol text, MIT for the tooling
README.md              this file (generated)
builder.html           single-file interactive builder (generated)
FINDINGS.md            six weeks of usage evidence, with method
fragments/             every line of block text, exactly once
tiers.json             which fragments compose Core, Standard, Full
build.py               renders README.md and builder.html from the above
test/test_build.py     fails if either generated file is stale
```

`README.md` and `builder.html` are **generated**. Edit `fragments/` or
`tiers.json`, then:

```
python build.py          # regenerate both
python build.py --check  # exit 1 if either is stale
python -m pytest test/   # same check, plus block invariants
```

Editing the fenced blocks in this file directly will be overwritten on the next
build. That is deliberate: the copy-paste path and the builder must not be able
to disagree about what the protocol says.

---

## License

Two parts, because there are two kinds of thing here.

**The protocol text is CC0.** Everything in `fragments/`, the paste blocks in
this file, and anything the builder emits. No attribution, no conditions, no
need to ask. An attribution clause on a snippet someone pastes into their
`CLAUDE.md` would be unenforceable and would put a shadow of doubt over adopting
it, which is the opposite of the point.

**The tooling is MIT.** `build.py`, the builder, the tests, and the prose around
the blocks, including `FINDINGS.md`.

If you want to credit something, credit `FINDINGS.md`. That is where the actual
work is, and it is the part worth citing.

---

*Derived from a working protocol in private use since 2026-07-23, revised
2026-09-02 against six weeks of transcript evidence. Designed collaboratively
with Claude Opus, cold-read by Fable and Sonnet. Take it, cut it, rename it.*
