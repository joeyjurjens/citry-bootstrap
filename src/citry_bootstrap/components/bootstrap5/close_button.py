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


class CloseButton(LibraryComponent):
    name = "bs-close-button"

    class Kwargs:
        variant: str | None = None
        disabled: bool = False
        attrs: dict | None = None

    def template_data(self, kwargs: Kwargs, slots):
        kwargs = _plain(kwargs)
        classes = ["btn-close"]
        if kwargs.variant:
            classes.append(f"btn-close-{kwargs.variant}")

        disabled = True if kwargs.disabled else None

        data = {
            "classes": " ".join(classes),
            "disabled": disabled,
            "attrs": kwargs.attrs,
        }
        data["button_attrs"] = merge_attrs(
            {"aria-label": "Close", "disabled": data["disabled"]},
            (data["attrs"] or {}),
            {"type": "button", "class": data["classes"]},
        )
        return data

    template = """
        <button c-bind="button_attrs"></button>
    """
