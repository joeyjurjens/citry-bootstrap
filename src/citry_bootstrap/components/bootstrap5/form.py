from typing import Literal

from citry import SlotInput, merge_attrs

from citry_bootstrap.component import BootstrapComponent
from citry_bootstrap.components.bootstrap5.types import (
    NOT_PROVIDED,
    FormCheckType,
    Size,
)


class Form(BootstrapComponent):
    name = "bs-form"

    class Kwargs:
        validated: bool = False
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        classes = []
        if kwargs.validated:
            classes.append("was-validated")

        data = {
            "form_class": " ".join(classes) if classes else "",
            "attrs": kwargs.attrs or {},
        }
        data["form_attrs"] = merge_attrs(
            (data["attrs"] or {}), ({"class": data["form_class"]} if data["form_class"] else {})
        )
        return data

    template = """
        <form c-bind="form_attrs">
        <c-slot />
        </form>
    """


class FormGroup(BootstrapComponent):
    name = "bs-form-group"

    class Kwargs:
        control_id: str | None = None
        as_: str = "div"
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        data = {
            "tag": kwargs.as_,
            "control_id": kwargs.control_id,
            "attrs": kwargs.attrs or {},
        }
        data["element_attrs"] = data["attrs"] or {}
        return data

    template = """
        <c-provide key="formgroup" c-control_id="control_id">
        <c-element c-is="tag" c-bind="element_attrs">
        <c-slot />
        </c-element>
        </c-provide>
    """


class FormLabel(BootstrapComponent):
    name = "bs-form-label"

    class Kwargs:
        for_: str | None = None
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        formgroup = self.inject("formgroup", NOT_PROVIDED)
        if formgroup is not NOT_PROVIDED:
            for_value = kwargs.for_ or formgroup.control_id
        else:
            for_value = kwargs.for_

        data = {
            "for_": for_value,
            "attrs": kwargs.attrs or {},
        }
        data["label_attrs"] = merge_attrs(
            {"class": "form-label", "for": data["for_"]}, (data["attrs"] or {})
        )
        return data

    template = """
        <label c-bind="label_attrs">
        <c-slot />
        </label>
    """


class FormControl(BootstrapComponent):
    name = "bs-form-control"

    class Kwargs:
        type: Literal[
            "text",
            "email",
            "password",
            "number",
            "tel",
            "url",
            "search",
            "date",
            "time",
            "datetime-local",
            "month",
            "week",
            "color",
            "file",
        ] = "text"
        size: Size | None = None
        plaintext: bool = False
        disabled: bool = False
        readonly: bool = False
        is_valid: bool = False
        is_invalid: bool = False
        html_size: int | None = None
        value: str | None = None
        placeholder: str | None = None
        name: str | None = None
        attrs: dict | None = None

    def template_data(self, kwargs: Kwargs, slots):
        formgroup = self.inject("formgroup", NOT_PROVIDED)
        control_id = formgroup.control_id if formgroup is not NOT_PROVIDED else None

        if kwargs.plaintext:
            form_class = "form-control-plaintext"
        else:
            classes = ["form-control"]
            if kwargs.type == "color":
                classes.append("form-control-color")
            if kwargs.size:
                classes.append(f"form-control-{kwargs.size}")
            if kwargs.is_valid:
                classes.append("is-valid")
            if kwargs.is_invalid:
                classes.append("is-invalid")
            form_class = " ".join(classes)

        html_attrs = {}
        if kwargs.disabled:
            html_attrs["disabled"] = True
        if kwargs.readonly:
            html_attrs["readonly"] = True

        final_attrs = {**html_attrs, **(kwargs.attrs or {})}

        data = {
            "form_class": form_class,
            "type": kwargs.type,
            "html_size": kwargs.html_size,
            "value": kwargs.value,
            "placeholder": kwargs.placeholder,
            "id": control_id,
            "name": kwargs.name,
            "attrs": final_attrs,
        }
        data["input_attrs"] = merge_attrs(
            {
                "type": data["type"],
                "id": data["id"],
                "name": data["name"],
                "value": data["value"],
                "placeholder": data["placeholder"],
                "size": data["html_size"],
            },
            (data["attrs"] or {}),
            {"class": data["form_class"]},
        )
        return data

    template = """
        <input c-bind="input_attrs" />
    """


class FormTextarea(BootstrapComponent):
    name = "bs-form-textarea"

    class Kwargs:
        rows: int = 3
        size: Size | None = None
        disabled: bool = False
        readonly: bool = False
        value: str | None = None
        placeholder: str | None = None
        name: str | None = None
        attrs: dict | None = None

    class Slots:
        default: SlotInput | None = None

    def template_data(self, kwargs: Kwargs, slots: Slots):
        formgroup = self.inject("formgroup", NOT_PROVIDED)
        control_id = formgroup.control_id if formgroup is not NOT_PROVIDED else None

        classes = ["form-control"]
        if kwargs.size:
            classes.append(f"form-control-{kwargs.size}")

        html_attrs = {}
        if kwargs.disabled:
            html_attrs["disabled"] = True
        if kwargs.readonly:
            html_attrs["readonly"] = True

        final_attrs = {**html_attrs, **(kwargs.attrs or {})}

        data = {
            "classes": " ".join(classes),
            "rows": kwargs.rows,
            "value": kwargs.value,
            "placeholder": kwargs.placeholder,
            "id": control_id,
            "name": kwargs.name,
            "attrs": final_attrs,
        }
        data["textarea_attrs"] = merge_attrs(
            {
                "rows": data["rows"],
                "id": data["id"],
                "name": data["name"],
                "placeholder": data["placeholder"],
            },
            (data["attrs"] or {}),
            {"class": data["classes"]},
        )
        data["textarea_content"] = (str(data["value"]) if data["value"] else "") + (
            str(slots.default) if slots.default is not None else ""
        )
        return data

    template = """
        <textarea c-bind="textarea_attrs">{{ textarea_content }}</textarea>
    """


class FormSelect(BootstrapComponent):
    name = "bs-form-select"

    class Kwargs:
        size: Size | None = None
        disabled: bool = False
        is_valid: bool = False
        is_invalid: bool = False
        html_size: int | None = None
        value: str | None = None
        name: str | None = None
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        formgroup = self.inject("formgroup", NOT_PROVIDED)
        control_id = formgroup.control_id if formgroup is not NOT_PROVIDED else None

        classes = ["form-select"]
        if kwargs.size:
            classes.append(f"form-select-{kwargs.size}")
        if kwargs.is_valid:
            classes.append("is-valid")
        if kwargs.is_invalid:
            classes.append("is-invalid")

        html_attrs = {}
        if kwargs.disabled:
            html_attrs["disabled"] = True

        final_attrs = {**html_attrs, **(kwargs.attrs or {})}

        data = {
            "classes": " ".join(classes),
            "html_size": kwargs.html_size,
            "value": kwargs.value,
            "id": control_id,
            "name": kwargs.name,
            "attrs": final_attrs,
        }
        data["select_attrs"] = merge_attrs(
            {"id": data["id"], "name": data["name"], "size": data["html_size"]},
            (data["attrs"] or {}),
            {"class": data["classes"]},
        )
        return data

    template = """
        <select c-bind="select_attrs">
        <c-slot />
        </select>
    """


class FormCheckInput(BootstrapComponent):
    name = "bs-form-check-input"

    class Kwargs:
        type: FormCheckType | None = None
        disabled: bool | None = None
        checked: bool | None = None
        is_valid: bool | None = None
        is_invalid: bool | None = None
        name: str | None = None
        value: str | None = None
        attrs: dict | None = None

    def template_data(self, kwargs: Kwargs, slots):
        formcheck = self.inject("formcheck", NOT_PROVIDED)
        if formcheck is not NOT_PROVIDED:
            control_id = formcheck.control_id
            check_type = kwargs.type if kwargs.type is not None else formcheck.type
            is_valid = kwargs.is_valid if kwargs.is_valid is not None else formcheck.is_valid
            is_invalid = (
                kwargs.is_invalid if kwargs.is_invalid is not None else formcheck.is_invalid
            )
            disabled = kwargs.disabled if kwargs.disabled is not None else formcheck.disabled
            checked = kwargs.checked if kwargs.checked is not None else formcheck.checked
        else:
            control_id = None
            check_type = kwargs.type if kwargs.type else "checkbox"
            is_valid = bool(kwargs.is_valid)
            is_invalid = bool(kwargs.is_invalid)
            disabled = bool(kwargs.disabled)
            checked = bool(kwargs.checked)

        input_type = "checkbox" if check_type == "switch" else check_type

        input_classes = ["form-check-input"]
        if is_valid:
            input_classes.append("is-valid")
        if is_invalid:
            input_classes.append("is-invalid")

        html_attrs = {}
        if checked:
            html_attrs["checked"] = True
        if disabled:
            html_attrs["disabled"] = True
        if check_type == "switch":
            html_attrs["role"] = "switch"

        final_attrs = {**html_attrs, **(kwargs.attrs or {})}

        data = {
            "input_classes": " ".join(input_classes),
            "input_type": input_type,
            "id": control_id,
            "name": kwargs.name,
            "value": kwargs.value,
            "attrs": final_attrs,
        }
        data["input_attrs"] = merge_attrs(
            {
                "type": data["input_type"],
                "id": data["id"],
                "name": data["name"],
                "value": data["value"],
            },
            (data["attrs"] or {}),
            {"class": data["input_classes"]},
        )
        return data

    template = """
        <input c-bind="input_attrs" />
    """


class FormCheckLabel(BootstrapComponent):
    name = "bs-form-check-label"

    class Kwargs:
        for_: str | None = None
        title: str | None = None
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        formcheck = self.inject("formcheck", NOT_PROVIDED)
        if formcheck is not NOT_PROVIDED:
            control_id = kwargs.for_ if kwargs.for_ else formcheck.control_id
        else:
            control_id = kwargs.for_

        data = {
            "for_": control_id,
            "title": kwargs.title,
            "attrs": kwargs.attrs or {},
        }
        data["label_attrs"] = merge_attrs(
            {"class": "form-check-label", "for": data["for_"], "title": data["title"]},
            (data["attrs"] or {}),
        )
        return data

    template = """
        <label c-bind="label_attrs">
        <c-slot />
        </label>
    """


class FormCheck(BootstrapComponent):
    name = "bs-form-check"

    class Kwargs:
        type: FormCheckType = "checkbox"
        inline: bool = False
        reverse: bool = False
        disabled: bool = False
        checked: bool = False
        is_valid: bool = False
        is_invalid: bool = False
        name: str | None = None
        value: str | None = None
        label: str | None = None
        title: str | None = None
        attrs: dict | None = None

    class Slots:
        default: SlotInput | None = None

    def template_data(self, kwargs: Kwargs, slots: Slots):
        wrapper_classes = []
        if kwargs.type == "switch":
            wrapper_classes.append("form-check form-switch")
        else:
            wrapper_classes.append("form-check")

        if kwargs.inline:
            wrapper_classes.append("form-check-inline")
        if kwargs.reverse:
            wrapper_classes.append("form-check-reverse")

        has_label = kwargs.label is not None

        control_id = (kwargs.attrs or {}).get("id") or f"formcheck-{self.id}"

        data = {
            "wrapper_classes": " ".join(wrapper_classes),
            "type": kwargs.type,
            "disabled": kwargs.disabled,
            "checked": kwargs.checked,
            "is_valid": kwargs.is_valid,
            "is_invalid": kwargs.is_invalid,
            "control_id": control_id,
            "name": kwargs.name,
            "value": kwargs.value,
            "label": kwargs.label,
            "title": kwargs.title,
            "has_label": has_label,
            "attrs": kwargs.attrs or {},
        }
        data["div_attrs"] = merge_attrs((data["attrs"] or {}), {"class": data["wrapper_classes"]})
        return data

    template = """
        <c-provide key="formcheck" c-control_id="control_id" c-type="type" c-is_valid="is_valid" c-is_invalid="is_invalid" c-disabled="disabled" c-checked="checked">
        <div c-bind="div_attrs">
        <c-slot>
        <c-bs-form-check-input c-type="type" c-disabled="disabled" c-checked="checked" c-is_valid="is_valid" c-is_invalid="is_invalid" c-name="name" c-value="value"></c-bs-form-check-input>
        <c-if cond="has_label">
        <c-bs-form-check-label c-for_="control_id" c-title="title">
        {{ label }}
        </c-bs-form-check-label>
        </c-if>
        </c-slot>
        </div>
        </c-provide>
    """


class FormText(BootstrapComponent):
    name = "bs-form-text"

    class Kwargs:
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        data = {
            "attrs": kwargs.attrs or {},
        }
        data["div_attrs"] = merge_attrs({"class": "form-text"}, (data["attrs"] or {}))
        return data

    template = """
        <div c-bind="div_attrs">
        <c-slot />
        </div>
    """


class FormFloating(BootstrapComponent):
    name = "bs-form-floating"

    class Kwargs:
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        data = {
            "attrs": kwargs.attrs or {},
        }
        data["div_attrs"] = merge_attrs({"class": "form-floating"}, (data["attrs"] or {}))
        return data

    template = """
        <div c-bind="div_attrs">
        <c-slot />
        </div>
    """
