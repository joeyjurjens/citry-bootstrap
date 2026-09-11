from citry import LibraryComponent, SlotInput, merge_attrs

from citry_bootstrap.components.bootstrap5.types import OverlayPlacement, TriggerEvent


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
