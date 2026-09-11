from types import SimpleNamespace

from citry import LibraryComponent, SlotInput, const_value, merge_attrs

from citry_bootstrap.components.bootstrap5.types import OverlayPlacement, TriggerEvent


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


class Tooltip(LibraryComponent):
    name = "bs-tooltip"

    class Kwargs:
        text: str
        placement: OverlayPlacement = "top"
        trigger: TriggerEvent = "hover"
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        kwargs = _plain(kwargs)
        data = {
            "text": kwargs.text,
            "placement": kwargs.placement,
            "trigger": kwargs.trigger,
            "attrs": kwargs.attrs,
        }
        data["span_attrs"] = merge_attrs(
            (data["attrs"] or {}),
            {
                "data-bs-toggle": "tooltip",
                "data-bs-title": data["text"],
                "data-bs-placement": data["placement"],
                "data-bs-trigger": data["trigger"],
            },
        )
        return data

    template = """
        <span c-bind="span_attrs">
        <c-slot />
        </span>
    """
