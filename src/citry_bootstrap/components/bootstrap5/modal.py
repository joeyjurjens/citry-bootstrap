from citry import SlotInput, merge_attrs

from citry_bootstrap.component import BootstrapComponent
from citry_bootstrap.components.bootstrap5.types import (
    BackdropBehavior,
    ButtonTag,
    HeadingLevel,
    ResponsiveBreakpoint,
    SizeWithXl,
)


class Modal(BootstrapComponent):
    name = "bs-modal"

    class Kwargs:
        size: SizeWithXl | None = None
        fullscreen: ResponsiveBreakpoint | None = None
        centered: bool = False
        scrollable: bool = False
        backdrop: BackdropBehavior | None = None
        keyboard: bool = True
        fade: bool = True
        dialog_class: str | None = None
        content_class: str | None = None
        attrs: dict | None = None

    class Slots:
        default: SlotInput
        toggle: SlotInput | None = None

    def template_data(self, kwargs: Kwargs, slots: Slots):
        modal_id = (kwargs.attrs or {}).get("id") or f"modal-{self.id}"

        modal_classes = ["modal"]
        if kwargs.fade:
            modal_classes.append("fade")

        dialog_classes = ["modal-dialog"]
        if kwargs.size:
            dialog_classes.append(f"modal-{kwargs.size}")
        if kwargs.fullscreen is not None:
            if kwargs.fullscreen is True:
                dialog_classes.append("modal-fullscreen")
            else:
                dialog_classes.append(f"modal-fullscreen-{kwargs.fullscreen}-down")
        if kwargs.centered:
            dialog_classes.append("modal-dialog-centered")
        if kwargs.scrollable:
            dialog_classes.append("modal-dialog-scrollable")
        if kwargs.dialog_class:
            dialog_classes.append(kwargs.dialog_class)

        content_classes = ["modal-content"]
        if kwargs.content_class:
            content_classes.append(kwargs.content_class)

        data = {
            "modal_id": modal_id,
            "modal_classes": " ".join(modal_classes),
            "dialog_classes": " ".join(dialog_classes),
            "content_classes": " ".join(content_classes),
            "backdrop": kwargs.backdrop,
            "keyboard": kwargs.keyboard,
            "attrs": kwargs.attrs,
        }
        data["div_attrs"] = merge_attrs(
            {
                "id": data["modal_id"],
                "aria-labelledby": f"{data['modal_id']}-label",
                "aria-hidden": "true",
            },
            (data["attrs"] or {}),
            {"class": data["modal_classes"], "tabindex": "-1"},
            ({"data-bs-backdrop": data["backdrop"]} if data["backdrop"] else {}),
            ({"data-bs-keyboard": "false"} if (not data["keyboard"]) else {}),
        )
        return data

    template = """
        <c-provide key="modal" c-modal_id="modal_id">
        <c-slot name="toggle" />
        <div c-bind="div_attrs" >
        <div c-class="dialog_classes">
        <div c-class="content_classes">
        <c-slot />
        </div>
        </div>
        </div>
        </c-provide>
    """


class ModalHeader(BootstrapComponent):
    name = "bs-modal-header"

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
        data["div_attrs"] = merge_attrs((data["attrs"] or {}), {"class": "modal-header"})
        return data

    template = """
        <div c-bind="div_attrs">
        <c-slot />
        <c-if cond="close_button">
        <c-bs-close-button c-variant="close_variant" c-attrs="{'aria-label': close_label, 'data-bs-dismiss': 'modal'}" />
        </c-if>
        </div>
    """


class ModalBody(BootstrapComponent):
    name = "bs-modal-body"

    class Kwargs:
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        data = {
            "attrs": kwargs.attrs,
        }
        data["div_attrs"] = merge_attrs((data["attrs"] or {}), {"class": "modal-body"})
        return data

    template = """
        <div c-bind="div_attrs">
        <c-slot />
        </div>
    """


class ModalFooter(BootstrapComponent):
    name = "bs-modal-footer"

    class Kwargs:
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        data = {
            "attrs": kwargs.attrs,
        }
        data["div_attrs"] = merge_attrs((data["attrs"] or {}), {"class": "modal-footer"})
        return data

    template = """
        <div c-bind="div_attrs">
        <c-slot />
        </div>
    """


class ModalTitle(BootstrapComponent):
    name = "bs-modal-title"

    class Kwargs:
        as_: HeadingLevel = "h5"
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        modal = self.inject("modal")
        modal_id = modal.modal_id

        data = {
            "tag": kwargs.as_,
            "modal_id": modal_id,
            "attrs": kwargs.attrs,
        }
        data["element_attrs"] = merge_attrs(
            (data["attrs"] or {}), {"class": "modal-title", "id": f"{data['modal_id']}-label"}
        )
        return data

    template = """
        <c-element c-is="tag" c-bind="element_attrs">
        <c-slot />
        </c-element>
    """


class ModalToggle(BootstrapComponent):
    name = "bs-modal-toggle"

    class Kwargs:
        as_: ButtonTag = "button"
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        modal = self.inject("modal")
        target_id = modal.modal_id

        data = {
            "tag": kwargs.as_,
            "target_id": target_id,
            "attrs": kwargs.attrs,
        }
        data["element_attrs"] = merge_attrs(
            (data["attrs"] or {}),
            {"data-bs-toggle": "modal", "data-bs-target": f"#{data['target_id']}"},
        )
        return data

    template = """
        <c-element c-is="tag" c-bind="element_attrs">
        <c-slot />
        </c-element>
    """
