from citry import SlotInput, merge_attrs

from citry_bootstrap.component import BootstrapComponent


class Alert(BootstrapComponent):
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


class AlertLink(BootstrapComponent):
    name = "bs-alert-link"

    class Kwargs:
        href: str = "#"
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
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


class AlertHeading(BootstrapComponent):
    name = "bs-alert-heading"

    class Kwargs:
        as_: str = "h4"
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
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
