# DO / TRY / CONSIDER

*Feedback markers for coding agents.* Paste a block into `CLAUDE.md`,
`AGENTS.md`, `.cursorrules`, or your system prompt. That's the install.

## Why bother

Say "consider X" to a coding agent, or just muse "huh, wouldn't it be cool if
X," and there's a fair chance X is now in your files. Agents lean hard toward
doing. Every shade of intent gets rounded up to an edit, and you get to find it,
undo it, and check what else moved.

So you adapt. You tack "don't change anything yet" onto every message, or you
soften real instructions so they won't be over-read. Either way you're managing
the agent's guesswork instead of doing your work.

This gives you a small, closed set of markers for your own feedback. `CONSIDER:`
means think it through and propose in writing. `DO:` means make the change. The
agent takes the marker at face value instead of guessing what you *really*
meant, and anything unmarked and ambiguous defaults to leaving your files alone.

If you've ever reverted an edit you only wondered out loud about, this is for
you.

## What it looks like

{{EXAMPLES}}

## Pick a size

> [!TIP]
> **Rather answer a few questions?** Open [`builder.html`](builder.html). It
> builds a block to fit how you work, runs offline, and sends nothing anywhere.
> Same text as the blocks below.

{{TIER_TABLE}}

Start with Core: it's the smallest block that works on its own. Move to
Standard when you hand work to subagents; it stops a `CONSIDER:` from quietly
becoming a `DO:` on the way across. Full adds `TRY`, where the agent builds something in scratch and a gate
decides whether it stays: a fresh reviewer, the agent itself (with a receipt),
or you. That last one differs from plan mode. You judge the finished thing, not
a description of it.

### Core

{{BLOCK_CORE}}

<details>
<summary><b>Standard</b></summary>

{{BLOCK_STANDARD}}

</details>

<details>
<summary><b>Full</b></summary>

{{BLOCK_FULL}}

</details>

## Before you paste

A few settings are one person's calibration. Decide them on purpose.

- **The marker is final.** The block tells the agent never to second-guess your
  marker, even if it suspects you mislabeled it. If you'd rather it flag a
  mismatch, the builder has a header for that. (Fair warning: it hands the call
  back to the agent's judgment, which is the thing you were routing around.)
- **`TRY(coldread:)` needs a fresh agent.** If your setup can't spawn one, or
  runs headless or on a schedule, cut it.
- **Gate names are yours.** Rename `showme` if your own name reads better in a
  transcript. Just keep the set closed.

## After you paste

Check that the file you edited is the one your agent actually reads. It's easy
to have this working through an agent's memory on one machine and nowhere else.

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
