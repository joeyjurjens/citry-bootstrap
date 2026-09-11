from types import SimpleNamespace

from citry import LibraryComponent, SlotInput, const_value, merge_attrs

from citry_bootstrap.components.bootstrap5.types import Size


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
        kwargs = _plain(kwargs)
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
        kwargs = _plain(kwargs)
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
