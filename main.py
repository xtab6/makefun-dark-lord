"""The Tired Dark Lord: A 100-Word Villain Monologue.

Writes one monologue to $MAKEFUN_OUTPUT_DIR/entry.txt.
Deterministic, stdlib only, no network, no randomness.
"""

import os

MONOLOGUE = (
    "Come in. Mind the rug, it bites. It has bitten three kings, and it has "
    "the right idea.\n\n"
    "You want the Spire, the crown, the black book with every debt. Take them. "
    "Take the ravens too; they only scream at dawn, and I lost track of dawn "
    "somewhere in the third century.\n\n"
    "Four hundred years I have kept the moat frozen, the gates shut, the ledgers "
    "in triplicate. Four hundred years, and no hero has ever asked how this place "
    "runs.\n\n"
    "So. Sword, speech, the whole lot. No, wait. Sit. Tea first. Then kill me, or "
    "better, sign here, and kill the paperwork instead."
)


def main() -> None:
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    # Clean only the contents of the output dir, never the dir itself.
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isdir(path) and not os.path.islink(path):
            for sub in os.listdir(path):
                os.remove(os.path.join(path, sub))
            os.rmdir(path)
        else:
            os.remove(path)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(MONOLOGUE)


if __name__ == "__main__":
    main()
