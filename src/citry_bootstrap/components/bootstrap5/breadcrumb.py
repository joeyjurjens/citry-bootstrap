from citry import LibraryComponent, SlotInput, merge_attrs


class Breadcrumb(LibraryComponent):
    name = "bs-breadcrumb"

    class Kwargs:
        as_: str = "nav"
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        data = {
            "tag": kwargs.as_,
            "attrs": kwargs.attrs,
        }
        data["element_attrs"] = merge_attrs({"aria-label": "breadcrumb"}, (data["attrs"] or {}))
        return data

    template = """
        <c-element c-is="tag" c-bind="element_attrs">
        <ol class="breadcrumb">
        <c-slot />
        </ol>
        </c-element>
    """


class BreadcrumbItem(LibraryComponent):
    name = "bs-breadcrumb-item"

    class Kwargs:
        active: bool = False
        href: str | None = None
        as_: str = "li"
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        css_classes = ["breadcrumb-item"]
        if kwargs.active:
            css_classes.append("active")

        aria_current = "page" if kwargs.active else None

        data = {
            "tag": kwargs.as_,
            "css_class": " ".join(css_classes),
            "active": kwargs.active,
            "href": kwargs.href,
            "aria_current": aria_current,
            "attrs": kwargs.attrs,
        }
        data["element_attrs"] = merge_attrs(
            {"aria-current": data["aria_current"]},
            (data["attrs"] or {}),
            {"class": data["css_class"]},
        )
        return data

    template = """
        <c-element c-is="tag" c-bind="element_attrs">
        <c-if cond="((not active) and href)">
        <a c-href="href"><c-slot /></a>
        </c-if><c-else>
        <c-slot />
        </c-else>
        </c-element>
    """
