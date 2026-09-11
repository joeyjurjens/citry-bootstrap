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


class Alert(LibraryComponent):
    name = "bs-alert"

    class Kwargs:
        variant: str = "primary"
        dismissible: bool = False
        close_label: str = "Close"
        close_variant: str | None = None
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        kwargs = _plain(kwargs)
        css_classes = ["alert", f"alert-{kwargs.variant}"]

        if kwargs.dismissible:
            css_classes.extend(["alert-dismissible", "fade", "show"])

        data = {
            "css_class": " ".join(css_classes),
            "dismissible": kwargs.dismissible,
            "close_label": kwargs.close_label,
            "close_variant": kwargs.close_variant,
            "attrs": kwargs.attrs,
        }
        data["div_attrs"] = merge_attrs(
            (data["attrs"] or {}), {"class": data["css_class"], "role": "alert"}
        )
        return data

    template = """
        <div c-bind="div_attrs">
        <c-slot />
        <c-if cond="dismissible">
        <c-bs-close-button c-variant="close_variant" c-attrs="{'aria-label': close_label, 'data-bs-dismiss': 'alert'}" />
        </c-if>
        </div>
    """


class AlertLink(LibraryComponent):
    name = "bs-alert-link"

    class Kwargs:
        href: str = "#"
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        kwargs = _plain(kwargs)
        data = {
            "href": kwargs.href,
            "attrs": kwargs.attrs,
        }
        data["a_attrs"] = merge_attrs(
            (data["attrs"] or {}), {"class": "alert-link", "href": data["href"]}
        )
        return data

    template = """
        <a c-bind="a_attrs">
        <c-slot />
        </a>
    """


class AlertHeading(LibraryComponent):
    name = "bs-alert-heading"

    class Kwargs:
        as_: str = "h4"
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        kwargs = _plain(kwargs)
        data = {
            "tag": kwargs.as_,
            "attrs": kwargs.attrs,
        }
        data["element_attrs"] = merge_attrs((data["attrs"] or {}), {"class": "alert-heading"})
        return data

    template = """
        <c-element c-is="tag" c-bind="element_attrs">
        <c-slot />
        </c-element>
    """
