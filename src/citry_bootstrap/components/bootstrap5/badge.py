from citry import SlotInput, merge_attrs

from citry_bootstrap.component import BootstrapComponent


class Badge(BootstrapComponent):
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
