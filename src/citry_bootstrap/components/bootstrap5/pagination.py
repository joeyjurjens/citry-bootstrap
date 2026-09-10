from citry import LibraryComponent, SlotInput, merge_attrs

from citry_bootstrap.components.bootstrap5.types import Size


class Pagination(LibraryComponent):
    name = "bs-pagination"

    class Kwargs:
        size: Size | None = None
        attrs: dict | None = None
        ul_attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        classes = ["pagination"]
        if kwargs.size:
            classes.append(f"pagination-{kwargs.size}")

        data = {
            "classes": " ".join(classes),
            "attrs": kwargs.attrs,
            "ul_attrs": kwargs.ul_attrs,
        }
        data["nav_attrs"] = merge_attrs({"aria-label": "Page navigation"}, (data["attrs"] or {}))
        data["ul_attrs"] = merge_attrs((data["ul_attrs"] or {}), {"class": data["classes"]})
        return data

    template = """
        <nav c-bind="nav_attrs">
        <ul c-bind="ul_attrs">
        <c-slot />
        </ul>
        </nav>
    """


class PaginationItem(LibraryComponent):
    name = "bs-pagination-item"

    class Kwargs:
        active: bool = False
        disabled: bool = False
        href: str = "#"
        aria_label: str | None = None
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        classes = ["page-item"]
        if kwargs.active:
            classes.append("active")
        if kwargs.disabled:
            classes.append("disabled")

        data = {
            "classes": " ".join(classes),
            "active": kwargs.active,
            "disabled": kwargs.disabled,
            "href": kwargs.href,
            "aria_label": kwargs.aria_label,
            "attrs": kwargs.attrs,
        }
        data["li_attrs"] = merge_attrs((data["attrs"] or {}), {"class": data["classes"]})
        data["a_attrs"] = merge_attrs(
            {"aria-label": data["aria_label"]},
            {"class": "page-link", "href": data["href"]},
            ({"aria-current": "page"} if data["active"] else {}),
            ({"tabindex": "-1", "aria-disabled": "true"} if data["disabled"] else {}),
        )
        return data

    template = """
        <li c-bind="li_attrs">
        <a c-bind="a_attrs">
        <c-slot />
        </a>
        </li>
    """


class PageItem(PaginationItem):
    pass


class PageLink(LibraryComponent):
    name = "bs-page-link"

    class Kwargs:
        href: str = "#"
        aria_label: str | None = None
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        data = {
            "href": kwargs.href,
            "aria_label": kwargs.aria_label,
            "attrs": kwargs.attrs,
        }
        data["a_attrs"] = merge_attrs(
            {"aria-label": data["aria_label"]},
            (data["attrs"] or {}),
            {"class": "page-link", "href": data["href"]},
        )
        return data

    template = """
        <a c-bind="a_attrs">
        <c-slot />
        </a>
    """


class PaginationFirst(LibraryComponent):
    name = "bs-pagination-first"

    class Kwargs:
        disabled: bool = False
        href: str = "#"
        attrs: dict | None = None

    class Slots:
        default: SlotInput | None = None

    def template_data(self, kwargs: Kwargs, slots: Slots):
        classes = ["page-item"]
        if kwargs.disabled:
            classes.append("disabled")

        data = {
            "classes": " ".join(classes),
            "disabled": kwargs.disabled,
            "href": kwargs.href,
            "attrs": kwargs.attrs,
        }
        data["li_attrs"] = merge_attrs((data["attrs"] or {}), {"class": data["classes"]})
        data["a_attrs"] = {"tabindex": "-1", "aria-disabled": "true"} if data["disabled"] else {}
        data["span_attrs"] = {"aria-hidden": "true"}
        return data

    template = """
        <li c-bind="li_attrs">
        <a class="page-link" c-href="href" c-bind="a_attrs">
        <span c-bind="span_attrs"><c-slot>«</c-slot></span>
        <span class="visually-hidden">First</span>
        </a>
        </li>
    """


class PaginationPrev(LibraryComponent):
    name = "bs-pagination-prev"

    class Kwargs:
        disabled: bool = False
        href: str = "#"
        attrs: dict | None = None

    class Slots:
        default: SlotInput | None = None

    def template_data(self, kwargs: Kwargs, slots: Slots):
        classes = ["page-item"]
        if kwargs.disabled:
            classes.append("disabled")

        data = {
            "classes": " ".join(classes),
            "disabled": kwargs.disabled,
            "href": kwargs.href,
            "attrs": kwargs.attrs,
        }
        data["li_attrs"] = merge_attrs((data["attrs"] or {}), {"class": data["classes"]})
        data["a_attrs"] = {"tabindex": "-1", "aria-disabled": "true"} if data["disabled"] else {}
        data["span_attrs"] = {"aria-hidden": "true"}
        return data

    template = """
        <li c-bind="li_attrs">
        <a class="page-link" c-href="href" c-bind="a_attrs">
        <span c-bind="span_attrs"><c-slot>‹</c-slot></span>
        <span class="visually-hidden">Previous</span>
        </a>
        </li>
    """


class PaginationNext(LibraryComponent):
    name = "bs-pagination-next"

    class Kwargs:
        disabled: bool = False
        href: str = "#"
        attrs: dict | None = None

    class Slots:
        default: SlotInput | None = None

    def template_data(self, kwargs: Kwargs, slots: Slots):
        classes = ["page-item"]
        if kwargs.disabled:
            classes.append("disabled")

        data = {
            "classes": " ".join(classes),
            "disabled": kwargs.disabled,
            "href": kwargs.href,
            "attrs": kwargs.attrs,
        }
        data["li_attrs"] = merge_attrs((data["attrs"] or {}), {"class": data["classes"]})
        data["a_attrs"] = {"tabindex": "-1", "aria-disabled": "true"} if data["disabled"] else {}
        data["span_attrs"] = {"aria-hidden": "true"}
        return data

    template = """
        <li c-bind="li_attrs">
        <a class="page-link" c-href="href" c-bind="a_attrs">
        <span c-bind="span_attrs"><c-slot>›</c-slot></span>
        <span class="visually-hidden">Next</span>
        </a>
        </li>
    """


class PaginationLast(LibraryComponent):
    name = "bs-pagination-last"

    class Kwargs:
        disabled: bool = False
        href: str = "#"
        attrs: dict | None = None

    class Slots:
        default: SlotInput | None = None

    def template_data(self, kwargs: Kwargs, slots: Slots):
        classes = ["page-item"]
        if kwargs.disabled:
            classes.append("disabled")

        data = {
            "classes": " ".join(classes),
            "disabled": kwargs.disabled,
            "href": kwargs.href,
            "attrs": kwargs.attrs,
        }
        data["li_attrs"] = merge_attrs((data["attrs"] or {}), {"class": data["classes"]})
        data["a_attrs"] = {"tabindex": "-1", "aria-disabled": "true"} if data["disabled"] else {}
        data["span_attrs"] = {"aria-hidden": "true"}
        return data

    template = """
        <li c-bind="li_attrs">
        <a class="page-link" c-href="href" c-bind="a_attrs">
        <span c-bind="span_attrs"><c-slot>»</c-slot></span>
        <span class="visually-hidden">Last</span>
        </a>
        </li>
    """


class PaginationEllipsis(LibraryComponent):
    name = "bs-pagination-ellipsis"

    class Kwargs:
        disabled: bool = False
        attrs: dict | None = None

    class Slots:
        default: SlotInput | None = None

    def template_data(self, kwargs: Kwargs, slots: Slots):
        classes = ["page-item"]
        if kwargs.disabled:
            classes.append("disabled")

        data = {
            "classes": " ".join(classes),
            "disabled": kwargs.disabled,
            "attrs": kwargs.attrs,
        }
        data["li_attrs"] = merge_attrs((data["attrs"] or {}), {"class": data["classes"]})
        data["span_attrs"] = {"aria-hidden": "true"}
        return data

    template = """
        <li c-bind="li_attrs">
        <span class="page-link">
        <span c-bind="span_attrs"><c-slot>…</c-slot></span>
        <span class="visually-hidden">More</span>
        </span>
        </li>
    """
