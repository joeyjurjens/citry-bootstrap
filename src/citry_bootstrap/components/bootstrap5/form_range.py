from types import SimpleNamespace

from citry import LibraryComponent, const_value, merge_attrs


def _plain(kwargs):
    """The component's inputs as ordinary Python values.

    Citry marks a template constant with a transparent proxy. It compares and
    stringifies like the value it wraps, but `re`, `os.fspath` and `str.join`
    reject it and `x is True` is False. Unwrapping here rather than at the
    engine's input hook leaves citry's own constness intact, so a cached
    component stays cached.
    """
    fields = getattr(type(kwargs), "__slots__", None) or type(kwargs).__annotations__
    return SimpleNamespace(**{name: const_value(getattr(kwargs, name)) for name in fields})


class FormRange(LibraryComponent):
    name = "bs-form-range"

    class Kwargs:
        min: int | float = 0
        max: int | float = 100
        step: int | float = 1
        value: int | float | None = None
        disabled: bool = False
        name: str | None = None
        attrs: dict | None = None

    def template_data(self, kwargs: Kwargs, slots):
        kwargs = _plain(kwargs)
        html_attrs = {}
        if kwargs.disabled:
            html_attrs["disabled"] = True

        final_attrs = {**html_attrs, **(kwargs.attrs or {})}

        data = {
            "min": kwargs.min,
            "max": kwargs.max,
            "step": kwargs.step,
            "value": kwargs.value,
            "name": kwargs.name,
            "attrs": final_attrs,
        }
        data["input_attrs"] = merge_attrs(
            {"value": data["value"], "name": data["name"]},
            (data["attrs"] or {}),
            {
                "type": "range",
                "class": "form-range",
                "min": data["min"],
                "max": data["max"],
                "step": data["step"],
            },
        )
        return data

    template = """
        <input c-bind="input_attrs" />
    """
