from types import SimpleNamespace

from citry import LibraryComponent, SlotInput, const_value, merge_attrs


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


class Figure(LibraryComponent):
    name = "bs-figure"

    class Kwargs:
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        kwargs = _plain(kwargs)
        data = {
            "attrs": kwargs.attrs,
        }
        data["figure_attrs"] = merge_attrs((data["attrs"] or {}), {"class": "figure"})
        return data

    template = """
        <figure c-bind="figure_attrs">
        <c-slot />
        </figure>
    """


class FigureImage(LibraryComponent):
    name = "bs-figure-image"

    class Kwargs:
        src: str
        alt: str = ""
        fluid: bool = True
        attrs: dict | None = None

    def template_data(self, kwargs: Kwargs, slots):
        kwargs = _plain(kwargs)
        classes = ["figure-img"]
        if kwargs.fluid:
            classes.append("img-fluid")

        data = {
            "src": kwargs.src,
            "alt": kwargs.alt,
            "classes": " ".join(classes),
            "attrs": kwargs.attrs,
        }
        data["img_attrs"] = merge_attrs(
            (data["attrs"] or {}),
            {"class": data["classes"], "src": data["src"], "alt": data["alt"]},
        )
        return data

    template = """
        <img c-bind="img_attrs" />
    """


class FigureCaption(LibraryComponent):
    name = "bs-figure-caption"

    class Kwargs:
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        kwargs = _plain(kwargs)
        data = {
            "attrs": kwargs.attrs,
        }
        data["figcaption_attrs"] = merge_attrs((data["attrs"] or {}), {"class": "figure-caption"})
        return data

    template = """
        <figcaption c-bind="figcaption_attrs">
        <c-slot />
        </figcaption>
    """
