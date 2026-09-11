from types import SimpleNamespace

from citry import LibraryComponent, SlotInput, const_value, merge_attrs

from citry_bootstrap.components.bootstrap5.types import Variant


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


class Progress(LibraryComponent):
    name = "bs-progress"

    class Kwargs:
        height: str | None = None
        stacked: bool = False
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        kwargs = _plain(kwargs)
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


class ProgressStacked(LibraryComponent):
    name = "bs-progress-stacked"

    class Kwargs:
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        kwargs = _plain(kwargs)
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


class ProgressBar(LibraryComponent):
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
        kwargs = _plain(kwargs)
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
