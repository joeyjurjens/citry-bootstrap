from citry import merge_attrs

from citry_bootstrap.component import BootstrapComponent
from citry_bootstrap.components.bootstrap5.types import BgColor, Size, Variant


class Placeholder(BootstrapComponent):
    name = "bs-placeholder"

    class Kwargs:
        as_: str = "span"
        size: Size | None = None
        bg: BgColor | None = None
        animation: str | None = None
        xs: int | None = None
        attrs: dict | None = None

    def template_data(self, kwargs: Kwargs, slots):
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


class PlaceholderButton(BootstrapComponent):
    name = "bs-placeholder-button"

    class Kwargs:
        variant: Variant = "primary"
        xs: int | None = None
        attrs: dict | None = None

    def template_data(self, kwargs: Kwargs, slots):
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
