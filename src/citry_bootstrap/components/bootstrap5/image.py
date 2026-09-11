from citry import merge_attrs

from citry_bootstrap.component import BootstrapComponent


class Image(BootstrapComponent):
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
