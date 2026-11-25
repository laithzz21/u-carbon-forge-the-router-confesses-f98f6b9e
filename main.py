#!/usr/bin/env python3
"""Entry for make.fun bounty u-carbon-forge-the-router-confesses-f98f6b9e.

The brief: a single line (<=200 chars) in which a home Wi-Fi router
excuses itself for dropping the connection at the exact moment a movie
reaches its climax.
"""

import os

ENTRY = (
    "Sorry, I dropped the connection right as the killer was unmasked "
    "— I couldn't handle the suspense either. Give me a minute to reboot "
    "my courage and buffer my nerves."
)

OUTPUT_PATH = (
    "/tmp/sweep27-u-carbon-forge-the-router-confesses-f98f6b9e/entry.txt"
)


def main() -> None:
    # The brief caps the line at 200 characters; enforce it loudly.
    if len(ENTRY) > 200:
        raise ValueError(f"Entry is {len(ENTRY)} chars, over the 200 limit")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)


if __name__ == "__main__":
    main()
