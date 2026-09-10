from citry import LibraryComponent, SlotInput, merge_attrs

from .types import NOT_PROVIDED, Size


class FormTextarea(LibraryComponent):
    """`<textarea>` is an HTML raw-text element, so citry does not parse tags
    inside it. The content is built here and inserted as one expression."""

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

        content = kwargs.value or ""
        if slots.default is not None:
            content = f"{content}{slots.default}"

        return {
            "content": content,
            "merged_attrs": merge_attrs(
                {
                    "rows": kwargs.rows,
                    "id": control_id,
                    "name": kwargs.name,
                    "placeholder": kwargs.placeholder,
                },
                {**html_attrs, **(kwargs.attrs or {})},
                {"class": " ".join(classes)},
            ),
        }

    template = """
        <textarea c-bind="merged_attrs">{{ content }}</textarea>
    """
