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

app = Citry(extensions=[citry_bootstrap.PlainValues])
citry_bootstrap.install(app)
```

Registration fails with a clear error if the extension is missing, so the two cannot drift apart. See [Plain values](#plain-values) for what it does.

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

## Plain values

Citry marks a template constant with `Const`, a transparent proxy. It compares, stringifies and truth-tests like the value it wraps, but it is not that value: `os.fspath`, `re` and `str.join` reject it, and `x is True` is `False` - which is how `fluid=True` used to render as `container-True`.

`PlainValues` unwraps those markers before `template_data` runs, so component code stays ordinary Python. The cost is that citry can no longer tell that an input was constant, so it will not cache a component's output. No component here declares a `Cache`, so nothing is lost; a library that does cache should unwrap at the point of use instead:

```python
from citry import const_value

weight = const_value(kwargs.weight)
```

Remove the extension once citry stops leaking the marker into component inputs.

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
