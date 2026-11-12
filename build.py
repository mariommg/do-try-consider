"""Compose the paste blocks from fragments, then render README.md and builder.html.

Every line of block text lives in exactly one place: fragments/. The README's
three tiers and the builder page's output are both generated from those, so the
wording cannot drift between the copy-paste path and the interactive one. That
drift is the whole reason this script exists rather than three hand-maintained
copies.

    python build.py           # regenerate README.md and builder.html
    python build.py --check   # exit 1 if either is stale (used by the test)
"""

import argparse
import io
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
FRAGMENTS = os.path.join(HERE, "fragments")
TIERS_PATH = os.path.join(HERE, "tiers.json")


def read(path):
    with io.open(path, encoding="utf-8") as f:
        return f.read()


def write_if_changed(path, text):
    """Returns True when the file on disk already matched."""
    existing = read(path) if os.path.exists(path) else None
    if existing == text:
        return True
    with io.open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    return False


def load_fragments():
    out = {}
    for name in sorted(os.listdir(FRAGMENTS)):
        if name.endswith(".md"):
            out[name[:-3]] = read(os.path.join(FRAGMENTS, name)).strip("\n")
    return out


def compose(tier, fragments):
    """Assemble one tier's paste block."""
    parts = []
    for section in tier["sections"]:
        if section["heading"]:
            parts.append(section["heading"])
        for key in section["fragments"]:
            if key not in fragments:
                raise SystemExit(f"build: tiers.json references missing fragment '{key}'")
            parts.append(fragments[key])
    body = "\n\n".join(parts)
    return body.replace("{{MARKERS}}", tier["markers"])


def render_readme(tiers, blocks):
    template = read(os.path.join(HERE, "README.template.md"))
    for name, block in blocks.items():
        placeholder = "{{BLOCK_%s}}" % name.upper()
        if placeholder not in template:
            raise SystemExit(f"build: README.template.md is missing {placeholder}")
        fenced = "```markdown\n" + block + "\n```"
        template = template.replace(placeholder, fenced)
    lines = [f"| {t['label']} | {len(blocks[n].splitlines())} | {t['blurb']} |"
             for n, t in tiers.items()]
    return template.replace("{{TIER_TABLE}}", "\n".join(lines))


def render_builder(tiers, fragments, blocks):
    template = read(os.path.join(HERE, "builder.template.html"))
    payload = {
        "fragments": fragments,
        "tiers": tiers,
        "blocks": blocks,
    }
    blob = json.dumps(payload, indent=2, ensure_ascii=False)
    if "{{DATA}}" not in template:
        raise SystemExit("build: builder.template.html is missing {{DATA}}")
    return template.replace("{{DATA}}", blob)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true",
                    help="verify the generated files are current; exit 1 if not")
    args = ap.parse_args()

    fragments = load_fragments()
    tiers = json.loads(read(TIERS_PATH))
    blocks = {name: compose(tier, fragments) for name, tier in tiers.items()}

    outputs = {
        os.path.join(HERE, "README.md"): render_readme(tiers, blocks),
        os.path.join(HERE, "builder.html"): render_builder(tiers, fragments, blocks),
    }

    if args.check:
        stale = [os.path.basename(p) for p, text in outputs.items()
                 if not os.path.exists(p) or read(p) != text]
        if stale:
            print("STALE: " + ", ".join(stale))
            print("Fragments or tiers.json changed without regenerating. Run: python build.py")
            return 1
        print("current: README.md, builder.html match fragments/")
        return 0

    for path, text in outputs.items():
        unchanged = write_if_changed(path, text)
        print(f"{'unchanged' if unchanged else 'wrote    '} {os.path.basename(path)}")
    for name, block in blocks.items():
        print(f"  {name:<9} {len(block.splitlines()):>3} lines")
    return 0


if __name__ == "__main__":
    sys.exit(main())
