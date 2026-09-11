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


class Breadcrumb(LibraryComponent):
    name = "bs-breadcrumb"

    class Kwargs:
        as_: str = "nav"
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        kwargs = _plain(kwargs)
        data = {
            "tag": kwargs.as_,
            "attrs": kwargs.attrs,
        }
        data["element_attrs"] = merge_attrs({"aria-label": "breadcrumb"}, (data["attrs"] or {}))
        return data

    template = """
        <c-element c-is="tag" c-bind="element_attrs">
        <ol class="breadcrumb">
        <c-slot />
        </ol>
        </c-element>
    """


class BreadcrumbItem(LibraryComponent):
    name = "bs-breadcrumb-item"

    class Kwargs:
        active: bool = False
        href: str | None = None
        as_: str = "li"
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        kwargs = _plain(kwargs)
        css_classes = ["breadcrumb-item"]
        if kwargs.active:
            css_classes.append("active")

        aria_current = "page" if kwargs.active else None

        data = {
            "tag": kwargs.as_,
            "css_class": " ".join(css_classes),
            "active": kwargs.active,
            "href": kwargs.href,
            "aria_current": aria_current,
            "attrs": kwargs.attrs,
        }
        data["element_attrs"] = merge_attrs(
            {"aria-current": data["aria_current"]},
            (data["attrs"] or {}),
            {"class": data["css_class"]},
        )
        return data

    template = """
        <c-element c-is="tag" c-bind="element_attrs">
        <c-if cond="((not active) and href)">
        <a c-href="href"><c-slot /></a>
        </c-if><c-else>
        <c-slot />
        </c-else>
        </c-element>
    """
