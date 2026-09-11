from citry import SlotInput, merge_attrs

from citry_bootstrap.component import BootstrapComponent
from citry_bootstrap.components.bootstrap5.types import (
    Alignment,
    CardImgVariant,
    HeadingLevel,
)


class Card(BootstrapComponent):
    name = "bs-card"

    class Kwargs:
        as_: str = "div"
        bg: str | None = None
        text: str | None = None
        border: str | None = None
        text_align: Alignment | None = None
        body: bool = False
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        classes = ["card"]
        if kwargs.bg and not kwargs.text:
            classes.append(f"text-bg-{kwargs.bg}")
        elif kwargs.bg:
            classes.append(f"bg-{kwargs.bg}")

        if kwargs.text:
            classes.append(f"text-{kwargs.text}")
        if kwargs.border:
            classes.append(f"border-{kwargs.border}")
        if kwargs.text_align:
            classes.append(f"text-{kwargs.text_align}")

        data = {
            "tag": kwargs.as_,
            "classes": " ".join(classes),
            "body": kwargs.body,
            "attrs": kwargs.attrs,
        }
        data["element_attrs"] = merge_attrs((data["attrs"] or {}), {"class": data["classes"]})
        return data

    template = """
        <c-element c-is="tag" c-bind="element_attrs">
        <c-if cond="body">
        <c-bs-card-body>
        <c-slot />
        </c-bs-card-body>
        </c-if><c-else>
        <c-slot />
        </c-else>
        </c-element>
    """


class CardHeader(BootstrapComponent):
    name = "bs-card-header"

    class Kwargs:
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        data = {
            "attrs": kwargs.attrs,
        }
        data["div_attrs"] = merge_attrs((data["attrs"] or {}), {"class": "card-header"})
        return data

    template = """
        <div c-bind="div_attrs">
        <c-slot />
        </div>
    """


class CardBody(BootstrapComponent):
    name = "bs-card-body"

    class Kwargs:
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        data = {
            "attrs": kwargs.attrs,
        }
        data["div_attrs"] = merge_attrs((data["attrs"] or {}), {"class": "card-body"})
        return data

    template = """
        <div c-bind="div_attrs">
        <c-slot />
        </div>
    """


class CardFooter(BootstrapComponent):
    name = "bs-card-footer"

    class Kwargs:
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        data = {
            "attrs": kwargs.attrs,
        }
        data["div_attrs"] = merge_attrs((data["attrs"] or {}), {"class": "card-footer"})
        return data

    template = """
        <div c-bind="div_attrs">
        <c-slot />
        </div>
    """


class CardTitle(BootstrapComponent):
    name = "bs-card-title"

    class Kwargs:
        as_: HeadingLevel = "h5"
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        data = {
            "tag": kwargs.as_,
            "attrs": kwargs.attrs,
        }
        data["element_attrs"] = merge_attrs((data["attrs"] or {}), {"class": "card-title"})
        return data

    template = """
        <c-element c-is="tag" c-bind="element_attrs">
        <c-slot />
        </c-element>
    """


class CardSubtitle(BootstrapComponent):
    name = "bs-card-subtitle"

    class Kwargs:
        as_: HeadingLevel = "h6"
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        data = {
            "tag": kwargs.as_,
            "attrs": kwargs.attrs,
        }
        data["element_attrs"] = merge_attrs((data["attrs"] or {}), {"class": "card-subtitle"})
        return data

    template = """
        <c-element c-is="tag" c-bind="element_attrs">
        <c-slot />
        </c-element>
    """


class CardText(BootstrapComponent):
    name = "bs-card-text"

    class Kwargs:
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        data = {
            "attrs": kwargs.attrs,
        }
        data["p_attrs"] = merge_attrs((data["attrs"] or {}), {"class": "card-text"})
        return data

    template = """
        <p c-bind="p_attrs">
        <c-slot />
        </p>
    """


class CardLink(BootstrapComponent):
    name = "bs-card-link"

    class Kwargs:
        href: str = "#"
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        data = {
            "href": kwargs.href,
            "attrs": kwargs.attrs,
        }
        data["a_attrs"] = merge_attrs(
            (data["attrs"] or {}), {"href": data["href"], "class": "card-link"}
        )
        return data

    template = """
        <a c-bind="a_attrs">
        <c-slot />
        </a>
    """


class CardImg(BootstrapComponent):
    name = "bs-card-img"

    class Kwargs:
        src: str
        alt: str = ""
        position: CardImgVariant | None = None
        attrs: dict | None = None

    def template_data(self, kwargs: Kwargs, slots):
        if kwargs.position == "top":
            img_class = "card-img-top"
        elif kwargs.position == "bottom":
            img_class = "card-img-bottom"
        else:
            img_class = "card-img"

        data = {
            "src": kwargs.src,
            "alt": kwargs.alt,
            "img_class": img_class,
            "attrs": kwargs.attrs,
        }
        data["img_attrs"] = merge_attrs(
            (data["attrs"] or {}),
            {"src": data["src"], "alt": data["alt"], "class": data["img_class"]},
        )
        return data

    template = """
        <img c-bind="img_attrs" />
    """


class CardImgOverlay(BootstrapComponent):
    name = "bs-card-img-overlay"

    class Kwargs:
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        data = {
            "attrs": kwargs.attrs,
        }
        data["div_attrs"] = merge_attrs((data["attrs"] or {}), {"class": "card-img-overlay"})
        return data

    template = """
        <div c-bind="div_attrs">
        <c-slot />
        </div>
    """


class CardGroup(BootstrapComponent):
    name = "bs-card-group"

    class Kwargs:
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        data = {
            "attrs": kwargs.attrs,
        }
        data["div_attrs"] = merge_attrs((data["attrs"] or {}), {"class": "card-group"})
        return data

    template = """
        <div c-bind="div_attrs">
        <c-slot />
        </div>
    """
