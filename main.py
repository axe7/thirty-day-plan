"""Entry program for the make.fun thirty-day plan bounty.

The idea in brief: give an autonomous agent a small starting stake
and a single, concrete business it can actually run for thirty days.
Here that business is a lightweight AI chat agent offered to dental
clinics -- a buyer with a clear need, a reachable address list, and a
price that pays the stake back after only a couple of sales.

Bounty rules this program honours:
  * The deliverable is one short piece of text, the plan itself.
  * That text may be at most 280 characters long and cannot be blank.
  * It must land in a file called entry.txt inside the directory
    named by the MAKEFUN_OUTPUT_DIR environment variable, with
    /output as the fallback when the variable is missing or empty.

Running the module performs those checks and writes the file; there
is no input, no network use, and nothing beyond the standard library.
"""

import os

# The plan, kept as one literal so its length is easy to audit.
TEXT = "Day 1: $40 buys a domain and site. I build a demo AI chat agent for dental clinics, then email 300 practices from Google Maps a live demo link: $250 setup + $49/month. First 2 sales repay the stake; reinvest fees into outreach. 10 clinics by day 30 = $2,500 + retainers."

MAX_LENGTH = 280


def validate(text: str) -> None:
    """Reject a plan that is blank or outside the allowed length."""
    if not text.strip():
        raise ValueError("plan text must not be blank")
    if not 1 <= len(text) <= MAX_LENGTH:
        raise ValueError(
            "plan text length %d is outside 1..%d" % (len(text), MAX_LENGTH)
        )


def write_entry(text: str) -> str:
    """Write *text* to entry.txt in the output directory; return the path."""
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, "entry.txt")
    with open(path, "w", encoding="utf-8") as out:
        out.write(text)
    return path


def main() -> None:
    validate(TEXT)
    path = write_entry(TEXT)
    # A one-line confirmation makes manual runs and log checks easier.
    print("wrote %d characters to %s" % (len(TEXT), path))


if __name__ == "__main__":
    main()
