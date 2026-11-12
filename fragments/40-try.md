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
