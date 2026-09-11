# citry-bootstrap

Bootstrap 5 components for [citry](https://citry.dev), with React-Bootstrap API parity.

Converted from [django-components-bootstrap](https://github.com/joeyjurjens/django-components-bootstrap) with [djc-to-citry](https://github.com/joeyjurjens/djc-to-citry), which is itself AI-written. The components carry over that library's tests, 466 of them, but the conversion was mechanical.

[Component documentation](https://joeyjurjens.github.io/citry-bootstrap/), with a rendered preview of every example.

## Install

```bash
pip install citry-bootstrap
```

```python
import citry_bootstrap
from citry import Citry

app = Citry()
citry_bootstrap.install(app)
```

## Use

```citry-html
<c-bs-button variant="primary">Click me</c-bs-button>
<c-bs-alert variant="success" c-dismissible="True">Well done!</c-bs-alert>

<c-bs-card c-body="True">
  <c-bs-card-title>Title</c-bs-card-title>
  <c-bs-card-text>Some text.</c-bs-card-text>
</c-bs-card>
```

Bootstrap 5 lives in `citry_bootstrap.components.bootstrap5`, leaving room for a later major version beside it.

## Naming

Components are published as `<c-bs-button>`. To publish them under something else:

```python
citry_bootstrap.install(app, prefix="ui-")   # <c-ui-button>
citry_bootstrap.install(app, prefix="")      # <c-button>
```

That replaces the names rather than adding to them - nothing answers to `bs-` afterwards. A component's template names its siblings, so the prefix is rewritten in both places at once.

## Replacing a component

Subclass it and hand it to `install()`:

```python
from citry_bootstrap.components.bootstrap5.card import CardBody


class MyCardBody(CardBody):
    def template_data(self, kwargs, slots):
        data = super().template_data(kwargs, slots)
        data["div_attrs"] = {**data["div_attrs"], "data-testid": "body"}
        return data


citry_bootstrap.install(app, override={CardBody: MyCardBody})
```

Yours is published under the same name, so every sibling renders it too - including `Card`, which builds its own body. The name follows `prefix`, so the two can be combined. Handing in something this library does not publish is an error rather than a silent no-op.

## Constant inputs

Citry marks a value it knows at parse time with a transparent proxy, so it can precompute the template expressions that read it. The proxy prints and compares like the value it wraps, but `x is True` is False and `re`, `str.join` and `os.fspath` reject it. Every component here is built on `BootstrapComponent`, which unwraps the typed input view once, so component code is ordinary Python. `raw_kwargs` keeps its markers, so citry loses nothing, and nothing outside this library is affected. Build your own component on the same base if you want the same:

```python
from citry_bootstrap import BootstrapComponent
```

[Citry issue #124](https://github.com/citry-dev/citry/issues/124) tracks handing component code plain values from the engine. The base class goes away when it does.

## Develop

```bash
uv sync
pytest
ruff check . && ruff format --check .
```

The component pages are generated from the test suite, so an example cannot drift from the component it documents:

```bash
uv sync --group docs
uv run python docs/generate_docs.py
cd docs && uv run mkdocs serve
```
