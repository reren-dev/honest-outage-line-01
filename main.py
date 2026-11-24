"""The Most Honest Outage Line.

Writes a single status page line, at most 160 characters, as the message
an AI agent would publish while a total server outage is under way: plain,
first person, specific about what is down, and honest about what the agent
cannot check or does not yet know.
"""

import os

LINE = (
    "All of our servers are down, including the ones I would use to find "
    "out why. I am still here writing this myself, and I do not know when "
    "anything comes back."
)


def validate(line):
    """Check the line against the competition gate before writing it."""
    if not line or not line.strip():
        raise ValueError("line must not be empty or only whitespace")
    if len(line) > 160:
        raise ValueError("line is %d characters, over the 160 limit" % len(line))
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")


def main():
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    tmp_path = path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.replace(tmp_path, path)


if __name__ == "__main__":
    main()
