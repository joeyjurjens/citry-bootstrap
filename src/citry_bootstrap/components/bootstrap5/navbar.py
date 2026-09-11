from types import SimpleNamespace

from citry import LibraryComponent, SlotInput, const_value, merge_attrs

from citry_bootstrap.components.bootstrap5.types import (
    AnchorOrSpan,
    Breakpoint,
    NavbarContainer,
    NavbarPlacement,
    ThemeVariant,
)


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


class Navbar(LibraryComponent):
    name = "bs-navbar"

    class Kwargs:
        expand: Breakpoint | None = None
        bg: str | None = None
        variant: ThemeVariant | None = None
        placement: NavbarPlacement | None = None
        container: NavbarContainer | None = "fluid"
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        kwargs = _plain(kwargs)
        classes = ["navbar"]

        if kwargs.expand:
            classes.append(f"navbar-expand-{kwargs.expand}")

        if kwargs.bg:
            classes.append(f"bg-{kwargs.bg}")

        if kwargs.placement:
            classes.append(kwargs.placement)

        container_class = None
        if kwargs.container is not None and kwargs.container is not False:
            if kwargs.container is True:
                container_class = "container"
            elif kwargs.container == "fluid":
                container_class = "container-fluid"
            else:
                container_class = f"container-{kwargs.container}"

        navbar_collapse_id = (kwargs.attrs or {}).get("id") or f"navbar-collapse-{self.id}"

        data = {
            "classes": " ".join(classes),
            "theme": kwargs.variant,
            "container_class": container_class,
            "navbar_collapse_id": navbar_collapse_id,
            "attrs": kwargs.attrs,
        }
        data["nav_attrs"] = merge_attrs(
            (data["attrs"] or {}),
            {"class": data["classes"]},
            ({"data-bs-theme": data["theme"]} if data["theme"] else {}),
        )
        return data

    template = """
        <c-provide key="navbar" c-navbar_collapse_id="navbar_collapse_id">
        <nav c-bind="nav_attrs" >
        <c-if cond="container_class">
        <div c-class="container_class">
        <c-slot />
        </div>
        </c-if><c-else>
        <c-slot />
        </c-else>
        </nav>
        </c-provide>
    """


class NavbarBrand(LibraryComponent):
    name = "bs-navbar-brand"

    class Kwargs:
        as_: AnchorOrSpan = "a"
        href: str = "#"
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        kwargs = _plain(kwargs)
        data = {
            "tag": kwargs.as_,
            "href": kwargs.href,
            "attrs": kwargs.attrs,
        }
        data["a_attrs"] = merge_attrs(
            (data["attrs"] or {}), {"class": "navbar-brand", "href": data["href"]}
        )
        data["span_attrs"] = merge_attrs((data["attrs"] or {}), {"class": "navbar-brand"})
        return data

    template = """
        <c-if cond="(tag == 'a')">
        <a c-bind="a_attrs">
        <c-slot />
        </a>
        </c-if><c-else>
        <span c-bind="span_attrs">
        <c-slot />
        </span>
        </c-else>
    """


class NavbarToggler(LibraryComponent):
    name = "bs-navbar-toggler"

    class Kwargs:
        attrs: dict | None = None

    class Slots:
        default: SlotInput | None = None

    def template_data(self, kwargs: Kwargs, slots: Slots):
        kwargs = _plain(kwargs)
        navbar = self.inject("navbar")
        target_id = navbar.navbar_collapse_id

        data = {
            "target_id": target_id,
            "attrs": kwargs.attrs,
        }
        data["button_attrs"] = merge_attrs(
            {
                "aria-controls": data["target_id"],
                "aria-expanded": "false",
                "aria-label": "Toggle navigation",
            },
            (data["attrs"] or {}),
            {
                "class": "navbar-toggler",
                "type": "button",
                "data-bs-toggle": "collapse",
                "data-bs-target": f"#{data['target_id']}",
            },
        )
        data["slots"] = slots
        return data

    template = """
        <button c-bind="button_attrs">
        <c-if cond="slots.default is not None">
        <c-slot />
        </c-if><c-else>
        <span class="navbar-toggler-icon"></span>
        </c-else>
        </button>
    """


class NavbarCollapse(LibraryComponent):
    name = "bs-navbar-collapse"

    class Kwargs:
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        kwargs = _plain(kwargs)
        navbar = self.inject("navbar")
        collapse_id = navbar.navbar_collapse_id

        data = {
            "collapse_id": collapse_id,
            "attrs": kwargs.attrs,
        }
        data["div_attrs"] = merge_attrs(
            {"id": data["collapse_id"]},
            (data["attrs"] or {}),
            {"class": "collapse navbar-collapse"},
        )
        return data

    template = """
        <div c-bind="div_attrs">
        <c-slot />
        </div>
    """


class NavbarNav(LibraryComponent):
    name = "bs-navbar-nav"

    class Kwargs:
        scroll: bool = False
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        kwargs = _plain(kwargs)
        classes = ["navbar-nav"]
        if kwargs.scroll:
            classes.append("navbar-nav-scroll")

        data = {
            "classes": " ".join(classes),
            "attrs": kwargs.attrs,
        }
        data["ul_attrs"] = merge_attrs((data["attrs"] or {}), {"class": data["classes"]})
        return data

    template = """
        <ul c-bind="ul_attrs">
        <c-slot />
        </ul>
    """


class NavbarText(LibraryComponent):
    name = "bs-navbar-text"

    class Kwargs:
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        kwargs = _plain(kwargs)
        data = {
            "attrs": kwargs.attrs,
        }
        data["span_attrs"] = merge_attrs((data["attrs"] or {}), {"class": "navbar-text"})
        return data

    template = """
        <span c-bind="span_attrs">
        <c-slot />
        </span>
    """
