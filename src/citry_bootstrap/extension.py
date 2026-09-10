"""Hand the components plain Python values.

Citry marks a template constant with `Const`, a transparent proxy. It compares,
stringifies and truth-tests like the value it wraps, but it is not that value:
`os.fspath`, `re` and `str.join` reject it, and `x is True` is False. Component
code written for django-components assumes plain values throughout.

Unwrapping once, before `template_data` runs, keeps every component ordinary
Python. Remove this when citry stops leaking the marker into component inputs.
"""

from typing import Any

from citry import Extension, const_value


class PlainValues(Extension):
    """Install with `Citry(extensions=[PlainValues])`."""

    name = "plain_values"

    def on_component_input(self, ctx: Any) -> None:
        for key, value in list(ctx.kwargs.items()):
            ctx.kwargs[key] = const_value(value)
