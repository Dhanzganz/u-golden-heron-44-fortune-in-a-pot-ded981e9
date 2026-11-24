"""Fortune in a Pot — make.fun entry.

Writes a single kind, funny fortune for the houseplant on the
windowsill to /output/entry.txt. Deterministic, no network.
"""

import os

ENTRY = "Your newest leaf will catch the morning sun this week, and you will grow one inch taller, purely to show off."


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 120 characters.
    assert 1 <= len(ENTRY) <= 120, f"entry is {len(ENTRY)} chars, must be 1-120"
    assert ENTRY.strip(), "entry must not be only white space"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
