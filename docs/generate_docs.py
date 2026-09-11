"""Build the component pages from the test suite.

Every test renders an example; the tests are therefore the examples, and they
cannot drift from the components because they are what proves them.
"""

import re
import sys
from itertools import count
from pathlib import Path

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT / "src"))

from citry import Citry  # noqa: E402

import citry_bootstrap  # noqa: E402

SOURCE = Path(__file__).parent / "source"
TESTS = ROOT / "tests"

#: Modal and toast are hidden until Bootstrap's JavaScript shows them.
VISIBLE = (
    (
        re.compile(r'class="modal fade"'),
        'class="modal fade show" style="display: block; position: relative;"',
    ),
    (re.compile(r'(<div[^>]*class="[^"]*toast[^"]*)"'), r'\1 show"'),
)


def engine() -> Citry:
    """Ids count from one per example, so a rebuild produces the same html."""
    ids = count(1)
    app = Citry(
        autodiscover=False,
        id_generator=lambda: f"ctest{next(ids):02d}",
    )
    citry_bootstrap.install(app)
    return app


def render(app: Citry, source: str) -> str:
    try:
        html = app.render_template(source).serialize().strip()
    except Exception as exc:  # noqa: BLE001
        print(f"  could not render: {type(exc).__name__}: {str(exc).splitlines()[0]}")
        return f'<div class="alert alert-danger">Error rendering: {exc}</div>'
    for pattern, replacement in VISIBLE:
        html = pattern.sub(replacement, html)
    return html


def examples(test_file: Path) -> list[dict]:
    """The first template each test renders, with the test name as its title."""
    found = []
    for name, body in re.findall(
        r"def (test_\w+)\([^)]*\):(.*?)(?=\ndef |\Z)", test_file.read_text(), re.DOTALL
    ):
        templates = re.findall(r'render\(r?"""(.*?)"""', body, re.DOTALL)
        if templates:
            title = name.removeprefix("test_").replace("_", " ").title()
            found.append({"title": title, "code": templates[0].strip()})
    return found


def component_name(test_file: Path) -> str:
    stem = test_file.stem.removeprefix("test_")
    return "".join(word.capitalize() for word in stem.split("_"))


def page(name: str, entries: list[dict], snippets: Path) -> str:
    if not entries:
        return f"# {name}\n\n_No examples available yet._\n"
    out = [f"# {name}\n"]
    for index, entry in enumerate(entries, start=1):
        snippet = f"{name.lower()}_example_{index}.html"
        html = render(engine(), entry["code"])
        (snippets / snippet).write_text(f'<div class="bs-example">\n{html}\n</div>')
        out += [
            f"## {entry['title']}\n",
            f"```citry-html\n{entry['code']}\n```\n",
            "**Preview:**\n",
            f'--8<-- "snippets/{snippet}"\n',
            "---\n",
        ]
    return "\n".join(out)


def index(names: list[str]) -> str:
    lines = [
        "# citry-bootstrap\n",
        "Bootstrap 5 components for citry, inspired by the React-Bootstrap API.\n",
        "## Install\n",
        "```bash\npip install citry-bootstrap\n```\n",
        "```python\nimport citry_bootstrap\nfrom citry import Citry\n\n"
        "app = Citry()\ncitry_bootstrap.install(app)\n```\n",
        "## Components\n",
    ]
    lines += [f"- [{name}](components/{name.lower()}.md)" for name in sorted(names)]
    return "\n".join(lines) + "\n"


def main() -> None:
    components = SOURCE / "components"
    snippets = SOURCE / "snippets"
    for directory in (components, snippets):
        directory.mkdir(parents=True, exist_ok=True)

    names = []
    for test_file in sorted(TESTS.glob("test_*.py")):
        entries = examples(test_file)
        if not entries:
            continue
        name = component_name(test_file)
        names.append(name)
        (components / f"{name.lower()}.md").write_text(page(name, entries, snippets))
        print(f"  {name}: {len(entries)} examples")

    (SOURCE / "index.md").write_text(index(names))
    print(f"\n{len(names)} pages written to {SOURCE}")


if __name__ == "__main__":
    main()
