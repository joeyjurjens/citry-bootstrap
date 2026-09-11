from citry import SlotInput, merge_attrs

from citry_bootstrap.component import BootstrapComponent
from citry_bootstrap.components.bootstrap5.types import BgColor, Placement


class ToastContainer(BootstrapComponent):
    name = "bs-toast-container"

    class Kwargs:
        position: Placement | None = None
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        classes = ["toast-container"]

        if kwargs.position:
            classes.append("position-fixed")
            if kwargs.position == "top":
                classes.append("top-0 start-50 translate-middle-x")
            elif kwargs.position == "bottom":
                classes.append("bottom-0 start-50 translate-middle-x")
            elif kwargs.position == "start":
                classes.append("top-0 start-0")
            elif kwargs.position == "end":
                classes.append("top-0 end-0")

        data = {
            "classes": " ".join(classes),
            "attrs": kwargs.attrs,
        }
        data["div_attrs"] = merge_attrs((data["attrs"] or {}), {"class": data["classes"]})
        return data

    template = """
        <div c-bind="div_attrs">
        <c-slot />
        </div>
    """


class Toast(BootstrapComponent):
    name = "bs-toast"

    class Kwargs:
        show: bool = False
        autohide: bool = True
        delay: int = 5000
        bg: BgColor | None = None
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        classes = ["toast"]

        if kwargs.show:
            classes.append("show")

        if kwargs.bg:
            classes.append(f"bg-{kwargs.bg}")
            if kwargs.bg in [
                "primary",
                "secondary",
                "success",
                "danger",
                "warning",
                "info",
                "dark",
            ]:
                classes.append("text-white")

        autohide_attr = "false" if not kwargs.autohide else None
        delay_attr = str(kwargs.delay) if kwargs.autohide and kwargs.delay != 5000 else None

        toast_id = (kwargs.attrs or {}).get("id") or f"toast-{self.id}"

        data = {
            "toast_id": toast_id,
            "classes": " ".join(classes),
            "autohide_attr": autohide_attr,
            "delay_attr": delay_attr,
            "attrs": kwargs.attrs,
        }
        data["div_attrs"] = merge_attrs(
            {
                "id": data["toast_id"],
                "aria-live": "assertive",
                "aria-atomic": "true",
                "data-bs-autohide": data["autohide_attr"],
                "data-bs-delay": data["delay_attr"],
            },
            (data["attrs"] or {}),
            {"class": data["classes"], "role": "alert"},
        )
        return data

    template = """
        <div c-bind="div_attrs">
        <c-slot />
        </div>
    """


class ToastHeader(BootstrapComponent):
    name = "bs-toast-header"

    class Kwargs:
        close_button: bool = True
        close_label: str = "Close"
        close_variant: str | None = None
        attrs: dict | None = None

    class Slots:
        default: SlotInput | None = None

    def template_data(self, kwargs: Kwargs, slots: Slots):
        data = {
            "close_button": kwargs.close_button,
            "close_label": kwargs.close_label,
            "close_variant": kwargs.close_variant,
            "attrs": kwargs.attrs,
        }
        data["div_attrs"] = merge_attrs((data["attrs"] or {}), {"class": "toast-header"})
        return data

    template = """
        <div c-bind="div_attrs">
        <c-slot />
        <c-if cond="close_button">
        <c-bs-close-button c-variant="close_variant" c-attrs="{'aria-label': close_label, 'data-bs-dismiss': 'toast'}" />
        </c-if>
        </div>
    """


class ToastBody(BootstrapComponent):
    name = "bs-toast-body"

    class Kwargs:
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        data = {
            "attrs": kwargs.attrs,
        }
        data["div_attrs"] = merge_attrs((data["attrs"] or {}), {"class": "toast-body"})
        return data

    template = """
        <div c-bind="div_attrs">
        <c-slot />
        </div>
    """
