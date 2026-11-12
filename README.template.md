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

{{EXAMPLES}}

## Pick a size

> [!TIP]
> **Want an interactive installer?** The [builder](builder.html) makes a block
> that fits how you work. It runs offline and sends nothing anywhere.

{{TIER_TABLE}}

**I recommend:** Start with Core, and step up to a bigger block once you've 
got the mental habit of tagging feedback and want more channels to do it.

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
