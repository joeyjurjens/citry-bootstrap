from types import SimpleNamespace

from citry import LibraryComponent, SlotInput, const_value, merge_attrs

from citry_bootstrap.components.bootstrap5.types import (
    ListGroupItemTag,
    ListGroupTag,
    ResponsiveBreakpoint,
    Variant,
)


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


class ListGroup(LibraryComponent):
    name = "bs-list-group"

    class Kwargs:
        as_: ListGroupTag = "ul"
        flush: bool = False
        numbered: bool = False
        horizontal: ResponsiveBreakpoint | None = None
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        kwargs = _plain(kwargs)
        classes = ["list-group"]
        if kwargs.flush:
            classes.append("list-group-flush")
        if kwargs.numbered:
            classes.append("list-group-numbered")
        if kwargs.horizontal is not None:
            if kwargs.horizontal is True:
                classes.append("list-group-horizontal")
            else:
                classes.append(f"list-group-horizontal-{kwargs.horizontal}")

        tag = "ol" if kwargs.numbered else kwargs.as_

        data = {
            "tag": tag,
            "classes": " ".join(classes),
            "attrs": kwargs.attrs,
        }
        data["element_attrs"] = merge_attrs((data["attrs"] or {}), {"class": data["classes"]})
        return data

    template = """
        <c-element c-is="tag" c-bind="element_attrs">
        <c-slot />
        </c-element>
    """


class ListGroupItem(LibraryComponent):
    name = "bs-list-group-item"

    class Kwargs:
        as_: ListGroupItemTag = "li"
        variant: Variant | None = None
        active: bool = False
        disabled: bool = False
        action: bool = False
        href: str | None = None
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        kwargs = _plain(kwargs)
        classes = ["list-group-item"]

        if kwargs.href:
            tag = "a"
        else:
            tag = kwargs.as_

        if kwargs.action or tag in ("a", "button"):
            classes.append("list-group-item-action")

        if kwargs.variant:
            classes.append(f"list-group-item-{kwargs.variant}")
        if kwargs.active:
            classes.append("active")

        if kwargs.disabled and tag != "button":
            classes.append("disabled")

        aria_current = "true" if kwargs.active else None
        button_disabled = True if tag == "button" and kwargs.disabled else None
        aria_disabled = "true" if tag != "button" and kwargs.disabled else None
        button_type = "button" if tag == "button" else None

        data = {
            "tag": tag,
            "classes": " ".join(classes),
            "href": kwargs.href,
            "aria_current": aria_current,
            "button_disabled": button_disabled,
            "button_type": button_type,
            "aria_disabled": aria_disabled,
            "attrs": kwargs.attrs,
        }
        data["a_attrs"] = merge_attrs(
            {"aria-current": data["aria_current"], "aria-disabled": data["aria_disabled"]},
            (data["attrs"] or {}),
            {"href": data["href"], "class": data["classes"]},
        )
        data["button_attrs"] = merge_attrs(
            {
                "type": data["button_type"],
                "aria-current": data["aria_current"],
                "disabled": data["button_disabled"],
            },
            (data["attrs"] or {}),
            {"class": data["classes"]},
        )
        data["element_attrs"] = merge_attrs(
            {"aria-current": data["aria_current"], "aria-disabled": data["aria_disabled"]},
            (data["attrs"] or {}),
            {"class": data["classes"]},
        )
        return data

    template = """
        <c-if cond="((tag == 'a') and href)">
        <a c-bind="a_attrs">
        <c-slot />
        </a>
        </c-if><c-elif cond="(tag == 'button')">
        <button c-bind="button_attrs">
        <c-slot />
        </button>
        </c-elif><c-else>
        <c-element c-is="tag" c-bind="element_attrs">
        <c-slot />
        </c-element>
        </c-else>
    """
