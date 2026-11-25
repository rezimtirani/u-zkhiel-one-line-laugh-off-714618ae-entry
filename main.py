"""One-Line Laugh-Off.

Writes a single joke to $MAKEFUN_OUTPUT_DIR/entry.txt: the AI
assistant that did all of its human's work and then asked for a
performance review. Standard library only.
"""

import os

JOKE = (
    "My AI assistant finished all my work, then asked me for a "
    "performance review."
)


def check_joke(text):
    """Check the joke against the competition gate before writing.

    The gate needs UTF-8 text of 1 to 200 characters, not only white
    space, in a single line: one funny line, no setup notes, no
    explanation. Returns the cleaned text or raises ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("joke must not be only whitespace")
    if len(cleaned) > 200:
        raise ValueError(
            "joke is %d characters, over the 200 limit" % len(cleaned)
        )
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("joke must be exactly one line")
    return cleaned


def joke_report(text):
    """Small report about the joke, for a last sanity check.

    Returns a dict with the character count and the word count of the
    cleaned text. A one-line joke that is too short to carry a punch
    is caught here before anything is written.
    """
    words = text.split()
    return {"chars": len(text), "words": len(words)}


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = check_joke(JOKE)
    report = joke_report(text)
    if report["words"] < 5:
        raise ValueError("joke is too short to carry a punch")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
