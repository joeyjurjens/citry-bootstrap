from citry import LibraryComponent, SlotInput, merge_attrs

from citry_bootstrap.components.bootstrap5.types import OverlayPlacement, TriggerEvent


class Popover(LibraryComponent):
    name = "bs-popover"

    class Kwargs:
        title: str
        content: str
        placement: OverlayPlacement = "top"
        trigger: TriggerEvent = "click"
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        data = {
            "title": kwargs.title,
            "content": kwargs.content,
            "placement": kwargs.placement,
            "trigger": kwargs.trigger,
            "attrs": kwargs.attrs,
        }
        data["span_attrs"] = merge_attrs(
            (data["attrs"] or {}),
            {
                "data-bs-toggle": "popover",
                "data-bs-title": data["title"],
                "data-bs-content": data["content"],
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
