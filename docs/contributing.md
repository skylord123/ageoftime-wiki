# Contributing

Thanks for your interest in improving the Age of Time wiki!

## Editing in the browser

Every page has a pencil icon in the top right that opens the source on GitHub
where you can propose changes via a pull request.

## Editing locally

1. Clone the repository.
2. Create a Python virtual environment and install the dependencies:

    ```bash
    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ```

3. Start the live-reload server:

    ```bash
    mkdocs serve
    ```

4. Open <http://127.0.0.1:8000> in your browser. Edits to files under `docs/`
   will hot-reload.

## Building a static copy

```bash
mkdocs build --strict
```

The output is written to `site/`.

## Style guidelines

- Prefer concise, factual prose.
- Use headings (`##`, `###`) to break up long pages.
- Cross-link related pages with relative links.
- Place images under `docs/assets/` and reference them with relative paths.
