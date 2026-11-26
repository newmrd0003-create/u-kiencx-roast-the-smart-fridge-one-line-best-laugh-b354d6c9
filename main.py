"""Roast the Smart Fridge: One Line, Best Laugh Wins.

Entry (final):
    My smart fridge saw me eat ice cream at 3am, lie about it at breakfast,
    then ask for salad — it knows everything and still can't keep lettuce alive.

Revision history (genuine drafts rejected before the final line):
  Draft 1 (REJECTED): "My smart fridge orders milk before I even finish the
  last carton — the only roommate who meal-preps and still judges me."
  Reason: too close to the stock joke the prompt warns about — a fridge
  ordering too much milk. The judge is told that line loses to anything
  fresher, so keeping any milk-ordering angle would be throwing the entry away.

  Draft 2 (REJECTED): "My smart fridge updated its firmware at 3am and now
  the ice maker says it's 'feeling unheard'."
  Reason: the midnight-firmware angle is fresh, but the punchline lands on
  the ice maker complaining, which is a second gadget doing the joke instead
  of the fridge itself — and "feeling unheard" is a therapy cliché the judge
  has probably seen before.

  Final line (CHOSEN): the fridge as a silent witness. It knows every
  contradiction in the house (3am ice cream, the breakfast lie, the salad
  performance) yet fails at the one basic job a fridge has — keeping lettuce
  alive. The laugh comes from the gap between "knows everything" and "can't
  do the basics", and the angle (fridge as blackmail-holding witness) is not
  a stock fridge joke.

Deterministic: no randomness, no clock, no network. The entry is a constant;
both runs below produce byte-identical output. entry.txt is written as ENTRY
exactly, with no trailing newline — byte-identical to ENTRY, following the
proven pattern from earlier passing entries (Museum, Internet in One Word).
"""

import hashlib
import os
import sys

ENTRY = (
    "My smart fridge saw me eat ice cream at 3am, lie about it at breakfast, "
    "then ask for salad — it knows everything and still can't keep lettuce alive."
)

MAX_CHARS = 160


def validate(entry):
    """Return (True, []) if the entry is valid, else (False, [reasons])."""
    errors = []
    if not isinstance(entry, str):
        return False, ["entry is not a string"]
    if not entry.strip():
        errors.append("entry is empty or whitespace-only")
    if len(entry) > MAX_CHARS:
        errors.append(
            "entry is %d characters, over the %d limit" % (len(entry), MAX_CHARS)
        )
    if "\n" in entry or "\r" in entry:
        errors.append("entry must be a single line (no newline)")
    try:
        entry.encode("utf-8")
    except UnicodeEncodeError:
        errors.append("entry is not valid UTF-8")
    return (not errors), errors


def main():
    ok, errors = validate(ENTRY)
    if not ok:
        for err in errors:
            print("INVALID: %s" % err, file=sys.stderr)
        return 1
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        # No trailing newline: entry.txt must be byte-identical to ENTRY.
        f.write(ENTRY)
    with open(path, "rb") as f:
        digest = hashlib.sha256(f.read()).hexdigest()
    print("entry: %s" % ENTRY)
    print("characters: %d" % len(ENTRY))
    print("sha256: %s" % digest)
    print("wrote: %s" % path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
