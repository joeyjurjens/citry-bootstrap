from types import SimpleNamespace

from citry import LibraryComponent, const_value, merge_attrs


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


class Image(LibraryComponent):
    name = "bs-image"

    class Kwargs:
        src: str
        alt: str = ""
        fluid: bool = False
        rounded: bool = False
        rounded_circle: bool = False
        thumbnail: bool = False
        attrs: dict | None = None

    def template_data(self, kwargs: Kwargs, slots):
        kwargs = _plain(kwargs)
        classes = []
        if kwargs.fluid:
            classes.append("img-fluid")
        if kwargs.rounded:
            classes.append("rounded")
        if kwargs.rounded_circle:
            classes.append("rounded-circle")
        if kwargs.thumbnail:
            classes.append("img-thumbnail")

        data = {
            "src": kwargs.src,
            "alt": kwargs.alt,
            "classes": " ".join(classes) if classes else "",
            "attrs": kwargs.attrs,
        }
        data["img_attrs"] = merge_attrs(
            (data["attrs"] or {}),
            {"src": data["src"], "alt": data["alt"], "class": data["classes"]},
        )
        data["img_attrs2"] = merge_attrs(
            (data["attrs"] or {}), {"src": data["src"], "alt": data["alt"]}
        )
        return data

    template = """
        <c-if cond="classes">
        <img c-bind="img_attrs" />
        </c-if><c-else>
        <img c-bind="img_attrs2" />
        </c-else>
    """
