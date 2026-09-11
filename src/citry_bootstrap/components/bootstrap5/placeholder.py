from types import SimpleNamespace

from citry import LibraryComponent, const_value, merge_attrs

from citry_bootstrap.components.bootstrap5.types import BgColor, Size, Variant


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


class Placeholder(LibraryComponent):
    name = "bs-placeholder"

    class Kwargs:
        as_: str = "span"
        size: Size | None = None
        bg: BgColor | None = None
        animation: str | None = None
        xs: int | None = None
        attrs: dict | None = None

    def template_data(self, kwargs: Kwargs, slots):
        kwargs = _plain(kwargs)
        classes = ["placeholder"]

        if kwargs.size:
            classes.append(f"placeholder-{kwargs.size}")

        if kwargs.bg:
            classes.append(f"bg-{kwargs.bg}")

        if kwargs.animation:
            classes.append(f"placeholder-{kwargs.animation}")

        if kwargs.xs:
            classes.append(f"col-{kwargs.xs}")

        data = {
            "tag": kwargs.as_,
            "classes": " ".join(classes),
            "attrs": kwargs.attrs,
        }
        data["element_attrs"] = merge_attrs((data["attrs"] or {}), {"class": data["classes"]})
        return data

    template = """
        <c-element c-is="tag" c-bind="element_attrs"></c-element>
    """


class PlaceholderButton(LibraryComponent):
    name = "bs-placeholder-button"

    class Kwargs:
        variant: Variant = "primary"
        xs: int | None = None
        attrs: dict | None = None

    def template_data(self, kwargs: Kwargs, slots):
        kwargs = _plain(kwargs)
        classes = ["btn", f"btn-{kwargs.variant}", "placeholder"]

        if kwargs.xs:
            classes.append(f"col-{kwargs.xs}")

        data = {
            "classes": " ".join(classes),
            "attrs": kwargs.attrs,
        }
        data["button_attrs"] = merge_attrs(
            {"aria-hidden": "true"},
            (data["attrs"] or {}),
            {"class": data["classes"], "disabled": True},
        )
        return data

    template = """
        <button c-bind="button_attrs"></button>
    """
