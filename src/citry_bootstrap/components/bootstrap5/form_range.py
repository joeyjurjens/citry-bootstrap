from citry import merge_attrs

from citry_bootstrap.component import BootstrapComponent


class FormRange(BootstrapComponent):
    name = "bs-form-range"

    class Kwargs:
        min: int | float = 0
        max: int | float = 100
        step: int | float = 1
        value: int | float | None = None
        disabled: bool = False
        name: str | None = None
        attrs: dict | None = None

    def template_data(self, kwargs: Kwargs, slots):
        html_attrs = {}
        if kwargs.disabled:
            html_attrs["disabled"] = True

        final_attrs = {**html_attrs, **(kwargs.attrs or {})}

        data = {
            "min": kwargs.min,
            "max": kwargs.max,
            "step": kwargs.step,
            "value": kwargs.value,
            "name": kwargs.name,
            "attrs": final_attrs,
        }
        data["input_attrs"] = merge_attrs(
            {"value": data["value"], "name": data["name"]},
            (data["attrs"] or {}),
            {
                "type": "range",
                "class": "form-range",
                "min": data["min"],
                "max": data["max"],
                "step": data["step"],
            },
        )
        return data

    template = """
        <input c-bind="input_attrs" />
    """
