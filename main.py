"""Thirty-day plan entry for the make.fun plan bounty.

This program produces a single short plan that an AI agent can execute
on its own to turn $100 into as much money as possible within 30 days.

Entry rules: the output must be one text of at most 280 Unicode code
points, written to a file named entry.txt in the output directory
given by the MAKEFUN_OUTPUT_DIR environment variable (falling back
to /output when that variable is not set).

The plan itself focuses on a concrete, sellable service: building a
demo AI chat agent for dental clinics and pitching it directly to
practices found on Google Maps, with a clear price ($250 setup plus
$49/month), a clear buyer (independent dental practices), and a
day-one action (buy the domain, ship the demo, start outreach).
"""

import os

TEXT = (
    "Day 1: $40 buys a domain and site. I build a demo AI chat agent for dental "
    "clinics, then email 300 practices from Google Maps a live demo link: $250 "
    "setup + $49/month. First 2 sales repay the stake; reinvest fees into "
    "outreach. 10 clinics by day 30 = $2,500 + retainers."
)


def main() -> None:
    if not TEXT.strip():
        raise ValueError("plan text must not be blank")
    if not 1 <= len(TEXT) <= 280:
        raise ValueError(
            f"plan text must be between 1 and 280 characters, got {len(TEXT)}"
        )

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)

    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(TEXT)


if __name__ == "__main__":
    main()
