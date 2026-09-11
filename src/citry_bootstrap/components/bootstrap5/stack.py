from citry import LibraryComponent, SlotInput, merge_attrs

from citry_bootstrap.components.bootstrap5.types import Breakpoint, StackDirection


class Stack(LibraryComponent):
    name = "bs-stack"

    class Kwargs:
        direction: StackDirection = "vertical"
        gap: int | None = None
        responsive: Breakpoint | None = None
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        classes = []

        if kwargs.direction == "horizontal":
            if kwargs.responsive:
                classes.append(f"hstack-{kwargs.responsive}")
            else:
                classes.append("hstack")
        else:
            classes.append("vstack")

        if kwargs.gap is not None:
            classes.append(f"gap-{kwargs.gap}")

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
