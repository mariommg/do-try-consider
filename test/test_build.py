"""Invariants for the generated blocks.

The point of these is that README.md and builder.html are generated, so the way
this repo breaks is silently: someone edits a fragment, forgets to rebuild, and
the copy-paste block in the README no longer says what the builder says. The
staleness check is the load-bearing test here; the rest guard the tier contract.

    python -m pytest test/          # or: python test/test_build.py
"""

import io
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)

import build  # noqa: E402


def read(path):
    with io.open(path, encoding="utf-8") as f:
        return f.read()


def blocks():
    fragments = build.load_fragments()
    tiers = json.loads(read(os.path.join(ROOT, "tiers.json")))
    return tiers, fragments, {n: build.compose(t, fragments) for n, t in tiers.items()}


def test_generated_files_are_current():
    """The one that actually catches mistakes."""
    proc = subprocess.run([sys.executable, os.path.join(ROOT, "build.py"), "--check"],
                          capture_output=True, text=True, cwd=ROOT)
    assert proc.returncode == 0, (
        "README.md or builder.html is stale. Run: python build.py\n" + proc.stdout)


def test_every_referenced_fragment_exists():
    tiers, fragments, _ = blocks()
    for name, tier in tiers.items():
        for section in tier["sections"]:
            for key in section["fragments"]:
                assert key in fragments, f"tier '{name}' references missing fragment '{key}'"


def test_no_orphan_fragments():
    """A fragment nobody composes is dead text that will drift out of date."""
    tiers, fragments, _ = blocks()
    used = {k for t in tiers.values() for s in t["sections"] for k in s["fragments"]}
    # The alternate header is offered by the builder only, never by a README tier.
    used.add("01-header-reflect")
    orphans = set(fragments) - used
    assert not orphans, f"unused fragments: {sorted(orphans)}"


def test_core_is_the_evidence_backed_subset():
    _, _, b = blocks()
    core = b["core"]
    for required in ["`DO:`", "`CONSIDER:`", "Tie-break rule", "Musing guard"]:
        assert required in core, f"Core block lost {required}"
    assert "TRY(" not in core, "Core must not carry the unexercised gate tier"
    assert "learn:" not in core, "Core must not carry the unused teaching marker"


def test_tiers_are_strictly_nested():
    """Standard contains Core's markers, Full contains Standard's. A reader who
    steps up a size should never lose a rule they were relying on."""
    _, fragments, _ = blocks()
    tiers = json.loads(read(os.path.join(ROOT, "tiers.json")))

    def frags(name):
        return [k for s in tiers[name]["sections"] for k in s["fragments"]]

    assert set(frags("core")) <= set(frags("standard")), "Standard drops something Core had"
    assert set(frags("standard")) <= set(frags("full")), "Full drops something Standard had"


def test_full_carries_the_gate_tier():
    _, _, b = blocks()
    assert "TRY(coldread:)" in b["full"] and "TRY(yourcall:)" in b["full"]
    assert "Receipt format" in b["full"]


def test_no_unresolved_placeholders():
    _, _, b = blocks()
    for name, block in b.items():
        assert "{{" not in block, f"{name} block has an unsubstituted placeholder"
    assert "{{" not in read(os.path.join(ROOT, "README.md")),         "README.md has an unsubstituted placeholder"
    # builder.html legitimately carries {{MARKERS}} inside its embedded fragment
    # JSON, because the page substitutes it client-side once the tier is chosen.
    # Only the surrounding template is required to be fully rendered.
    html = read(os.path.join(ROOT, "builder.html"))
    shell = re.sub(r'<script id="data".*?</script>', "", html, flags=re.S)
    assert "{{" not in shell, "builder.html template has an unsubstituted placeholder"


def test_readme_embeds_every_block_verbatim():
    _, _, b = blocks()
    readme = read(os.path.join(ROOT, "README.md"))
    for name, block in b.items():
        assert block in readme, f"README is missing the {name} block verbatim"


def test_builder_data_is_valid_json():
    html = read(os.path.join(ROOT, "builder.html"))
    m = re.search(r'<script id="data" type="application/json">(.*?)</script>', html, re.S)
    assert m, "builder.html lost its embedded data block"
    payload = json.loads(m.group(1))
    assert set(payload) == {"fragments", "tiers", "blocks"}
    assert payload["blocks"]["core"], "builder shipped an empty core block"


def test_house_style_no_em_dashes():
    """These blocks get pasted into other people's files under the author's name,
    and the house style forbids em and en dashes. Easy to reintroduce by hand."""
    fragments = build.load_fragments()
    offenders = [k for k, v in fragments.items() if "—" in v or "–" in v]
    assert not offenders, f"em/en dash in fragments: {offenders}"


if __name__ == "__main__":
    failures = 0
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            try:
                fn()
                print(f"  ok   {name}")
            except AssertionError as exc:
                failures += 1
                print(f"  FAIL {name}\n       {exc}")
    print(f"\n{'PASS' if not failures else 'FAIL'}  {failures} failure(s)")
    sys.exit(1 if failures else 0)
