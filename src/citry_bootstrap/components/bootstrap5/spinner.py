from types import SimpleNamespace

from citry import LibraryComponent, const_value, merge_attrs

from citry_bootstrap.components.bootstrap5.types import Size, SpinnerVariant, Variant


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


class Spinner(LibraryComponent):
    name = "bs-spinner"

    class Kwargs:
        animation: SpinnerVariant = "border"
        size: Size | None = None
        variant: Variant | None = None
        label: str = "Loading..."
        attrs: dict | None = None

    def template_data(self, kwargs: Kwargs, slots):
        kwargs = _plain(kwargs)
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
