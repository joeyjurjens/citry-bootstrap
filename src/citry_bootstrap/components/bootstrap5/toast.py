from types import SimpleNamespace

from citry import LibraryComponent, SlotInput, const_value, merge_attrs

from citry_bootstrap.components.bootstrap5.types import BgColor, Placement


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


class ToastContainer(LibraryComponent):
    name = "bs-toast-container"

    class Kwargs:
        position: Placement | None = None
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        kwargs = _plain(kwargs)
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


class Toast(LibraryComponent):
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
        kwargs = _plain(kwargs)
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


class ToastHeader(LibraryComponent):
    name = "bs-toast-header"

    class Kwargs:
        close_button: bool = True
        close_label: str = "Close"
        close_variant: str | None = None
        attrs: dict | None = None

    class Slots:
        default: SlotInput | None = None

    def template_data(self, kwargs: Kwargs, slots: Slots):
        kwargs = _plain(kwargs)
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


class ToastBody(LibraryComponent):
    name = "bs-toast-body"

    class Kwargs:
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        kwargs = _plain(kwargs)
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
