"""Rebuild the TorqueScript console-dump pages from local Nextcloud notes.

Each notes file is one large fenced code block. This script extracts the
inner contents and re-wraps them in a TorqueScript-tagged code block on
the corresponding wiki page, with a small header explaining provenance.

Run from the repo root:

    python3 scripts/build_console_dumps.py
"""

from pathlib import Path

NOTES_DIR = Path(
    "/home/skylar/Nextcloud/Notes/Homelab/AgeOfTime"
)
WIKI_DIR = Path("docs/reference/torque-script")
FENCE = "\x60\x60\x60"

DUMPS = [
    {
        "src": NOTES_DIR / "dumpConsoleFunctions();.md",
        "dst": WIKI_DIR / "console-function-dump.md",
        "title": "Console Function Dump",
        "subject": "console function",
        "subject_plural": "console functions",
        "command": "dumpConsoleFunctions();",
    },
    {
        "src": NOTES_DIR / "dumpConsoleClasses();.md",
        "dst": WIKI_DIR / "console-class-dump.md",
        "title": "Console Class Dump",
        "subject": "console class",
        "subject_plural": "console classes",
        "command": "dumpConsoleClasses();",
    },
]


def extract_body(src: Path) -> str:
    """Return everything between the first and last code-fence lines."""
    lines = src.read_text().splitlines()
    fences = [i for i, ln in enumerate(lines) if ln.strip().startswith(FENCE)]
    if len(fences) < 2:
        raise SystemExit(f"{src}: fewer than two code-fence lines")
    return "\n".join(lines[fences[0] + 1 : fences[-1]])


def render_header(title: str, subject: str, subject_plural: str, command: str) -> str:
    return f"""# {title}

This page is a verbatim dump of every TorqueScript {subject} exposed by
the *Age of Time* client at runtime, captured by running the engine's
built-in `{command}` from the in-game console.

!!! note "Annotations"
    A handful of entries have been hand-annotated with `//` comments to
    describe what they do or their expected arguments. Anything after a
    `//` on a line is **not** part of the original engine output — it's a
    community note. {subject_plural.capitalize()} without a comment are
    listed exactly as the engine reported them, with no documented
    signature.

!!! tip "Reproducing this dump"
    Open the in-game console (the engine's standard tilde key in older
    Torque builds, or run the executable with the appropriate flag) and
    type:

    ```
    {command}
    ```

    The engine will print the same listing shown below.
"""


def build_one(cfg: dict) -> None:
    body = extract_body(cfg["src"])
    header = render_header(
        cfg["title"], cfg["subject"], cfg["subject_plural"], cfg["command"]
    )
    cfg["dst"].parent.mkdir(parents=True, exist_ok=True)
    cfg["dst"].write_text(
        header + "\n" + FENCE + "torquescript\n" + body + "\n" + FENCE + "\n"
    )
    print(f"wrote {cfg['dst']} ({cfg['dst'].stat().st_size} bytes)")


if __name__ == "__main__":
    for cfg in DUMPS:
        build_one(cfg)
