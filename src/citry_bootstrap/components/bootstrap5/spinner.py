from citry import LibraryComponent, merge_attrs

from citry_bootstrap.components.bootstrap5.types import Size, SpinnerVariant, Variant


class Spinner(LibraryComponent):
    name = "bs-spinner"

    class Kwargs:
        animation: SpinnerVariant = "border"
        size: Size | None = None
        variant: Variant | None = None
        label: str = "Loading..."
        attrs: dict | None = None

    def template_data(self, kwargs: Kwargs, slots):
        base_class = f"spinner-{kwargs.animation}"
        classes = [base_class]

        if kwargs.size:
            classes.append(f"{base_class}-{kwargs.size}")

        if kwargs.variant:
            classes.append(f"text-{kwargs.variant}")

        data = {
            "classes": " ".join(classes),
            "label": kwargs.label,
            "attrs": kwargs.attrs,
        }
        data["div_attrs"] = merge_attrs(
            (data["attrs"] or {}), {"class": data["classes"], "role": "status"}
        )
        return data

    template = """
        <div c-bind="div_attrs">
        <span class="visually-hidden">{{ label }}</span>
        </div>
    """
