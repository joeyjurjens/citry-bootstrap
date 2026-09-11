from citry import SlotInput, merge_attrs

from citry_bootstrap.component import BootstrapComponent
from citry_bootstrap.components.bootstrap5.types import (
    BackdropBehavior,
    Breakpoint,
    ButtonTag,
    HeadingLevel,
    OffcanvasPlacement,
)


class Offcanvas(BootstrapComponent):
    name = "bs-offcanvas"

    class Kwargs:
        placement: OffcanvasPlacement = "start"
        backdrop: BackdropBehavior | None = None
        scroll: bool = False
        keyboard: bool = True
        responsive: Breakpoint | None = None
        attrs: dict | None = None

    class Slots:
        default: SlotInput
        toggle: SlotInput | None = None

    def template_data(self, kwargs: Kwargs, slots: Slots):
        offcanvas_id = (kwargs.attrs or {}).get("id") or f"offcanvas-{self.id}"

        if kwargs.responsive:
            classes = [f"offcanvas-{kwargs.responsive}", f"offcanvas-{kwargs.placement}"]
        else:
            classes = ["offcanvas", f"offcanvas-{kwargs.placement}"]

        data = {
            "offcanvas_id": offcanvas_id,
            "classes": " ".join(classes),
            "backdrop": kwargs.backdrop,
            "scroll": kwargs.scroll,
            "keyboard": kwargs.keyboard,
            "attrs": kwargs.attrs,
        }
        data["div_attrs"] = merge_attrs(
            {"id": data["offcanvas_id"], "aria-labelledby": f"{data['offcanvas_id']}-label"},
            (data["attrs"] or {}),
            {"class": data["classes"], "tabindex": "-1"},
            ({"data-bs-backdrop": data["backdrop"]} if data["backdrop"] else {}),
            ({"data-bs-scroll": "true"} if data["scroll"] else {}),
            ({"data-bs-keyboard": "false"} if (not data["keyboard"]) else {}),
        )
        return data

    template = """
        <c-provide key="offcanvas" c-offcanvas_id="offcanvas_id">
        <c-slot name="toggle" />
        <div c-bind="div_attrs" >
        <c-slot />
        </div>
        </c-provide>
    """


class OffcanvasHeader(BootstrapComponent):
    name = "bs-offcanvas-header"

    class Kwargs:
        close_button: bool = True
        close_label: str = "Close"
        close_variant: str | None = None
        attrs: dict | None = None

    class Slots:
        default: SlotInput | None = None

    def template_data(self, kwargs: Kwargs, slots: Slots):
        try:
            offcanvas = self.inject("offcanvas")
            offcanvas_id = offcanvas.offcanvas_id
        except KeyError:
            offcanvas_id = None
        data = {
            "close_button": kwargs.close_button,
            "close_label": kwargs.close_label,
            "close_variant": kwargs.close_variant,
            "offcanvas_id": offcanvas_id,
            "attrs": kwargs.attrs,
        }
        data["div_attrs"] = merge_attrs((data["attrs"] or {}), {"class": "offcanvas-header"})
        return data

    template = """
        <div c-bind="div_attrs">
        <c-slot />
        <c-if cond="close_button">
        <c-bs-close-button c-variant="close_variant" c-attrs="{'aria-label': close_label, 'data-bs-dismiss': 'offcanvas', 'data-bs-target': f'#{offcanvas_id}'}" />
        </c-if>
        </div>
    """


class OffcanvasBody(BootstrapComponent):
    name = "bs-offcanvas-body"

    class Kwargs:
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        data = {
            "attrs": kwargs.attrs,
        }
        data["div_attrs"] = merge_attrs((data["attrs"] or {}), {"class": "offcanvas-body"})
        return data

    template = """
        <div c-bind="div_attrs">
        <c-slot />
        </div>
    """


class OffcanvasTitle(BootstrapComponent):
    name = "bs-offcanvas-title"

    class Kwargs:
        as_: HeadingLevel = "h5"
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        offcanvas = self.inject("offcanvas")
        offcanvas_id = offcanvas.offcanvas_id

        data = {
            "tag": kwargs.as_,
            "offcanvas_id": offcanvas_id,
            "attrs": kwargs.attrs,
        }
        data["element_attrs"] = merge_attrs(
            (data["attrs"] or {}),
            {"class": "offcanvas-title", "id": f"{data['offcanvas_id']}-label"},
        )
        return data

    template = """
        <c-element c-is="tag" c-bind="element_attrs">
        <c-slot />
        </c-element>
    """


class OffcanvasToggle(BootstrapComponent):
    name = "bs-offcanvas-toggle"

    class Kwargs:
        as_: ButtonTag = "button"
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        offcanvas = self.inject("offcanvas")
        target_id = offcanvas.offcanvas_id

        data = {
            "tag": kwargs.as_,
            "target_id": target_id,
            "attrs": kwargs.attrs,
        }
        data["element_attrs"] = merge_attrs(
            {"aria-controls": data["target_id"]},
            (data["attrs"] or {}),
            {"data-bs-toggle": "offcanvas", "data-bs-target": f"#{data['target_id']}"},
        )
        return data

    template = """
        <c-element c-is="tag" c-bind="element_attrs">
        <c-slot />
        </c-element>
    """
