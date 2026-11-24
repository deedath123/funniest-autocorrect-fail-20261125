"""School Strip autocorrect fail — one-line entry for the Funniest Autocorrect Fail bounty."""

import os

MAX_CHARS = 199

LINE = "Dad, can I have $20 for the school strip tomorrow? The bus leaves at 7."

assert 1 <= len(LINE) <= MAX_CHARS

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
