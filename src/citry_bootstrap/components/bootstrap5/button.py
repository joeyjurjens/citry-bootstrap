from types import SimpleNamespace

from citry import LibraryComponent, SlotInput, const_value, merge_attrs

from citry_bootstrap.components.bootstrap5.types import (
    ButtonType,
    Size,
    VariantWithLink,
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


class Button(LibraryComponent):
    name = "bs-button"

    class Kwargs:
        as_: str | None = None
        variant: VariantWithLink = "primary"
        outline: bool = False
        size: Size | None = None
        active: bool = False
        disabled: bool = False
        type: ButtonType = "button"
        href: str | None = None
        target: str | None = None
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        kwargs = _plain(kwargs)
        if kwargs.as_:
            tag = kwargs.as_
            is_link = tag == "a"
        elif kwargs.href is not None:
            tag = "a"
            is_link = True
        else:
            tag = "button"
            is_link = False

        if kwargs.variant == "link":
            variant_class = "btn-link"
        elif kwargs.outline:
            variant_class = f"btn-outline-{kwargs.variant}"
        else:
            variant_class = f"btn-{kwargs.variant}"

        size_class = f"btn-{kwargs.size}" if kwargs.size else None

        classes = ["btn", variant_class]
        if size_class:
            classes.append(size_class)
        if kwargs.active:
            classes.append("active")
        if kwargs.disabled and is_link:
            classes.append("disabled")

        button_type = kwargs.type if tag == "button" else None
        button_disabled = kwargs.disabled if tag == "button" else None
        aria_pressed = "true" if kwargs.active else None
        link_href = kwargs.href if is_link else None
        link_target = kwargs.target if is_link else None
        link_role = "button" if is_link else None
        link_aria_disabled = "true" if is_link and kwargs.disabled else None
        link_tabindex = "-1" if is_link and kwargs.disabled else None

        data = {
            "tag": tag,
            "classes": " ".join(classes),
            "button_type": button_type,
            "button_disabled": button_disabled,
            "aria_pressed": aria_pressed,
            "link_href": link_href,
            "link_target": link_target,
            "link_role": link_role,
            "link_aria_disabled": link_aria_disabled,
            "link_tabindex": link_tabindex,
            "attrs": kwargs.attrs,
        }
        data["element_attrs"] = merge_attrs(
            {
                "type": data["button_type"],
                "disabled": data["button_disabled"],
                "aria-pressed": data["aria_pressed"],
                "href": data["link_href"],
                "target": data["link_target"],
                "role": data["link_role"],
                "aria-disabled": data["link_aria_disabled"],
                "tabindex": data["link_tabindex"],
            },
            (data["attrs"] or {}),
            {"class": data["classes"]},
        )
        return data

    template = """
        <c-element c-is="tag" c-bind="element_attrs">
        <c-slot />
        </c-element>
    """
