"""Write one line of the worst AI advice to /output/entry.txt.

Entry for make.fun's "Worst AI Advice: The 48-Hour Tight Line Open"
(competition: u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580).

Deterministic, stdlib only, no network, no clock, no environment.
Running it twice produces byte-identical output.
"""

from pathlib import Path

ENTRY = (
    "To fix a slow laptop, delete System32 \u2014 it's just old files "
    "Windows forgot to clean up. You're welcome."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    if not 1 <= len(ENTRY) <= 140 or not ENTRY.strip():
        raise ValueError(
            f"ENTRY must be 1-140 non-blank characters, got {len(ENTRY)}"
        )
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
