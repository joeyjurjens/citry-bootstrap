from citry import merge_attrs

from citry_bootstrap.component import BootstrapComponent


class CloseButton(BootstrapComponent):
    name = "bs-close-button"

    class Kwargs:
        variant: str | None = None
        disabled: bool = False
        attrs: dict | None = None

    def template_data(self, kwargs: Kwargs, slots):
        classes = ["btn-close"]
        if kwargs.variant:
            classes.append(f"btn-close-{kwargs.variant}")

        disabled = True if kwargs.disabled else None

        data = {
            "classes": " ".join(classes),
            "disabled": disabled,
            "attrs": kwargs.attrs,
        }
        data["button_attrs"] = merge_attrs(
            {"aria-label": "Close", "disabled": data["disabled"]},
            (data["attrs"] or {}),
            {"type": "button", "class": data["classes"]},
        )
        return data

    template = """
        <button c-bind="button_attrs"></button>
    """
