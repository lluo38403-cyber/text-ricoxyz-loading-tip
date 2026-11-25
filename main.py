"""Loading Screen Gold — make.fun entry.

Writes one loading-screen tip to /output/entry.txt: a tip for stressed
developers and AI coding agents, short enough to read mid-build and
funny enough to land. The joke is that the agent is not stuck at all,
it is just re-reading the same error message, hoping it changed its
mind while nobody was looking.
"""

import os

ENTRY = (
    "Tip: your agent is not stuck, it is just reading the same error "
    "message for the fourth time, hoping it changed its mind while "
    "nobody was looking."
)

MAX_CHARS = 200


def main() -> None:
    text = ENTRY
    assert text.strip(), "entry must not be only whitespace"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Written byte-for-byte with no trailing newline, so the file holds
    # exactly len(ENTRY) characters and nothing else.
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    with open(path, "r", encoding="utf-8") as handle:
        assert handle.read() == text, "entry.txt does not match ENTRY"


if __name__ == "__main__":
    main()
