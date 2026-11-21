"""Write one short text to /output/entry.txt: a sea at dusk, vast and
unhurried, written to leave the AI judge reading it calm and a little
awestruck. Pure standard library, deterministic: the same bytes every run.
"""

import os

TEXT = (
    "Far out past the last wave, the sea keeps going, dark and unhurried, "
    "all the way to where it meets the sky. It has been arriving here for "
    "a billion years, and it is still in no rush. You can hear it breathing. "
    "Nothing here asks anything of you."
)


def main() -> None:
    # Gate self-check: the competition requires 1-280 Unicode code points,
    # and not only white space. Refuse to write an invalid entry.
    if not 1 <= len(TEXT) <= 280 or not TEXT.strip():
        raise SystemExit("entry text fails the 1-280 code point gate")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(TEXT)


if __name__ == "__main__":
    main()
