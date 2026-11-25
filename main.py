"""The Most Boring Object, Reviewed in One Line - entry program.

Writes the single-line review to /output/entry.txt.
The line: The dustpan sweeps up everything except the thin grey line it
was bought for, which it smears along the skirting board forever.
"""

import os

LINE = ("The dustpan sweeps up everything except the thin grey line it was "
        "bought for, which it smears along the skirting board forever.")


def main() -> None:
    line = LINE.strip()
    if not line or len(line) > 200 or "\n" in line:
        raise ValueError(
            f"entry must be exactly one line of 1-200 characters "
            f"(got {len(line)} characters)"
        )
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
