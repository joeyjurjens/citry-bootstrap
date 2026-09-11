from types import SimpleNamespace

from citry import LibraryComponent, SlotInput, const_value, merge_attrs


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


class Badge(LibraryComponent):
    name = "bs-badge"

    class Kwargs:
        bg: str = "primary"
        text: str | None = None
        pill: bool = False
        as_: str = "span"
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        kwargs = _plain(kwargs)
        css_classes = ["badge"]

        if kwargs.bg and not kwargs.text:
            css_classes.append(f"text-bg-{kwargs.bg}")
        elif kwargs.bg:
            css_classes.append(f"bg-{kwargs.bg}")

        if kwargs.pill:
            css_classes.append("rounded-pill")
        if kwargs.text:
            css_classes.append(f"text-{kwargs.text}")

        data = {
            "tag": kwargs.as_,
            "css_class": " ".join(css_classes),
            "attrs": kwargs.attrs,
        }
        data["element_attrs"] = merge_attrs((data["attrs"] or {}), {"class": data["css_class"]})
        return data

    template = """
        <c-element c-is="tag" c-bind="element_attrs">
        <c-slot />
        </c-element>
    """
