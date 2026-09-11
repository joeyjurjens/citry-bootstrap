from citry import LibraryComponent, SlotInput, merge_attrs

from citry_bootstrap.components.bootstrap5.types import Size


class ButtonGroup(LibraryComponent):
    name = "bs-button-group"

    class Kwargs:
        size: Size | None = None
        vertical: bool = False
        role: str = "group"
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        classes = ["btn-group-vertical" if kwargs.vertical else "btn-group"]
        if kwargs.size:
            classes.append(f"btn-group-{kwargs.size}")

        data = {
            "classes": " ".join(classes),
            "role": kwargs.role,
            "attrs": kwargs.attrs,
        }
        data["div_attrs"] = merge_attrs(
            {"role": data["role"]}, (data["attrs"] or {}), {"class": data["classes"]}
        )
        return data

    template = """
        <div c-bind="div_attrs">
        <c-slot />
        </div>
    """


class ButtonToolbar(LibraryComponent):
    name = "bs-button-toolbar"

    class Kwargs:
        role: str = "toolbar"
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        data = {
            "role": kwargs.role,
            "attrs": kwargs.attrs,
        }
        data["div_attrs"] = merge_attrs(
            {"role": data["role"]}, (data["attrs"] or {}), {"class": "btn-toolbar"}
        )
        return data

    template = """
        <div c-bind="div_attrs">
        <c-slot />
        </div>
    """
