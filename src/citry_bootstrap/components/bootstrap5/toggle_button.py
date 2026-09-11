from citry import SlotInput, merge_attrs

from citry_bootstrap.component import BootstrapComponent
from citry_bootstrap.components.bootstrap5.types import (
    NOT_PROVIDED,
    Size,
    ToggleButtonType,
    Variant,
)


class ToggleButtonGroup(BootstrapComponent):
    name = "bs-toggle-button-group"

    class Kwargs:
        name: str
        type: ToggleButtonType = "radio"
        vertical: bool = False
        size: Size | None = None
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        classes = ["btn-group-vertical" if kwargs.vertical else "btn-group"]
        if kwargs.size:
            classes.append(f"btn-group-{kwargs.size}")

        data = {
            "classes": " ".join(classes),
            "type": kwargs.type,
            "group_name": kwargs.name,
            "attrs": kwargs.attrs,
        }
        data["div_attrs"] = merge_attrs(
            (data["attrs"] or {}), {"class": data["classes"], "role": "group"}
        )
        return data

    template = """
        <c-provide key="toggle_button_group" c-type="type" c-group_name="group_name">
        <div c-bind="div_attrs">
        <c-slot />
        </div>
        </c-provide>
    """


class ToggleButton(BootstrapComponent):
    name = "bs-toggle-button"

    class Kwargs:
        type: ToggleButtonType | None = None
        name: str | None = None
        value: str | None = None
        checked: bool = False
        disabled: bool = False
        variant: Variant = "primary"
        outline: bool = True
        size: Size | None = None
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        group = self.inject("toggle_button_group", NOT_PROVIDED)

        # A group's `type` is authoritative for all its buttons (Bootstrap's
        # `.btn-group` toggle pattern doesn't support mixing radio/checkbox
        # inputs); a button's own `name` still wins over the group's.
        if group is not NOT_PROVIDED:
            toggle_type = group.type
            toggle_name = kwargs.name if kwargs.name is not None else group.group_name
        else:
            toggle_type = kwargs.type if kwargs.type is not None else "checkbox"
            toggle_name = kwargs.name

        toggle_id = (kwargs.attrs or {}).get("id") or f"toggle-button-{self.id}"

        input_attrs = {
            "type": toggle_type,
            "class": "btn-check",
            "id": toggle_id,
            "autocomplete": "off",
        }

        if toggle_name:
            input_attrs["name"] = toggle_name
        if kwargs.value:
            input_attrs["value"] = kwargs.value
        if kwargs.checked:
            input_attrs["checked"] = True
        if kwargs.disabled:
            input_attrs["disabled"] = True

        if kwargs.outline:
            variant_class = f"btn-outline-{kwargs.variant}"
        else:
            variant_class = f"btn-{kwargs.variant}"

        label_classes = ["btn", variant_class]
        if kwargs.size:
            label_classes.append(f"btn-{kwargs.size}")

        # Exclude id from label attrs since it's used for the input
        label_attrs = {k: v for k, v in (kwargs.attrs or {}).items() if k != "id"}

        data = {
            "input_attrs": input_attrs,
            "label_classes": " ".join(label_classes),
            "id": toggle_id,
            "label_attrs": label_attrs,
        }
        data["input_attrs"] = data["input_attrs"] or {}
        data["label_attrs"] = merge_attrs(
            (data["label_attrs"] or {}), {"class": data["label_classes"], "for": data["id"]}
        )
        return data

    template = """
        <input c-bind="input_attrs" />
        <label c-bind="label_attrs">
        <c-slot />
        </label>
    """
