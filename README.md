# Age of Time Wiki

Community wiki for the Torque-engine MMO **Age of Time** — covering items,
magic, enemies, areas, NPC mechanics (Blacksmith crafting, Police/jail
system, shopkeepers, …), and a growing TorqueScript reference section with
console-function/class dumps, tagged-string internals, and datablock IDs.

**Live site:** <https://skylord123.github.io/ageoftime-wiki/>

The wiki is built with [MkDocs](https://www.mkdocs.org/) and the
[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) theme,
and is deployed automatically to GitHub Pages on every push to `master`.

## Local development

Requirements: Python 3.9+.

```bash
# 1. Create a virtualenv and install dependencies
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# 2. Serve the wiki with live reload at http://127.0.0.1:8000
mkdocs serve

# 3. Build a strict, production-ready copy into ./site
mkdocs build --strict
```

`mkdocs build --strict` is the same command run by CI, so if it passes
locally the deploy will pass too.

## Repository layout

```
.
├── docs/                       # All wiki content (Markdown + assets)
│   ├── index.md                # Home
│   ├── gameplay/               # Items, magic, commands, death, …
│   ├── world/                  # Areas, enemies, friendly NPCs
│   ├── npcs/                   # Per-NPC deep dives (Blacksmith, Police, …)
│   ├── reference/
│   │   └── torque-script/      # Engine-level reference pages
│   └── assets/                 # Images, icons, archived raw server data
├── scripts/
│   └── build_console_dumps.py  # Regenerates the console dump pages from
│                               # local engine notes
├── .github/workflows/deploy.yml  # GitHub Pages deployment
├── mkdocs.yml                  # Site config, theme, navigation
└── requirements.txt
```

## Contributing

Corrections, screenshots, and new pages are very welcome. The wiki has a
[Contributing page](https://skylord123.github.io/ageoftime-wiki/contributing/)
that walks through the editing workflow; in short:

1. Fork the repo and create a branch.
2. Edit Markdown under `docs/`.
3. Run `mkdocs build --strict` to confirm the site still builds clean.
4. Open a pull request.

Each page on the live site has a pencil icon in the top-right corner that
deep-links to the corresponding source file on GitHub.

## License

Content on this wiki documents the game *Age of Time* for community
reference. *Age of Time* itself, its assets, and its trademarks are the
property of their respective owners.
