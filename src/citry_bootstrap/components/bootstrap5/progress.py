from citry import SlotInput, merge_attrs

from citry_bootstrap.component import BootstrapComponent
from citry_bootstrap.components.bootstrap5.types import Variant


class Progress(BootstrapComponent):
    name = "bs-progress"

    class Kwargs:
        height: str | None = None
        stacked: bool = False
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        classes = ["progress-stacked" if kwargs.stacked else "progress"]
        style = {}
        if kwargs.height:
            style["height"] = kwargs.height

        data = {
            "classes": " ".join(classes),
            "style": style,
            "attrs": kwargs.attrs,
        }
        data["div_attrs"] = merge_attrs(
            (data["attrs"] or {}),
            {"class": data["classes"]},
            (
                {
                    "style": "".join(
                        str(key) + ": " + str(value) + ";"
                        for key, value in (
                            data["style"].items()
                            if callable(data["style"].items)
                            else data["style"].items
                        )
                    )
                }
                if data["style"]
                else {}
            ),
        )
        return data

    template = """
        <div c-bind="div_attrs" >
        <c-slot />
        </div>
    """


class ProgressStacked(BootstrapComponent):
    name = "bs-progress-stacked"

    class Kwargs:
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        data = {
            "attrs": kwargs.attrs,
        }
        data["div_attrs"] = merge_attrs((data["attrs"] or {}), {"class": "progress-stacked"})
        return data

    template = """
        <div c-bind="div_attrs">
        <c-slot />
        </div>
    """


class ProgressBar(BootstrapComponent):
    name = "bs-progress-bar"

    class Kwargs:
        now: int = 0
        min: int = 0
        max: int = 100
        variant: Variant | None = None
        striped: bool = False
        animated: bool = False
        label: str | None = None
        attrs: dict | None = None

    class Slots:
        default: SlotInput | None = None

    def template_data(self, kwargs: Kwargs, slots: Slots):
        classes = ["progress-bar"]

        if kwargs.variant:
            classes.append(f"bg-{kwargs.variant}")
        if kwargs.striped or kwargs.animated:
            classes.append("progress-bar-striped")
        if kwargs.animated:
            classes.append("progress-bar-animated")

        percentage = 0
        if kwargs.max > kwargs.min:
            percentage = ((kwargs.now - kwargs.min) / (kwargs.max - kwargs.min)) * 100

        data = {
            "classes": " ".join(classes),
            "percentage": percentage,
            "now": kwargs.now,
            "min": kwargs.min,
            "max": kwargs.max,
            "label": kwargs.label,
            "attrs": kwargs.attrs,
        }
        data["div_attrs"] = merge_attrs((data["attrs"] or {}), {"class": data["classes"]})
        return data

    template = """
        <div c-bind="div_attrs" c-style='f"width: {percentage}%"'>
        <c-if cond="label">{{ label }}</c-if>
        <c-slot />
        </div>
    """
