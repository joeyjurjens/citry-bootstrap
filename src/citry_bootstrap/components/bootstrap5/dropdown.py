from citry import LibraryComponent, SlotInput, merge_attrs

from citry_bootstrap.components.bootstrap5.types import (
    AlignmentStartEnd,
    AnchorOrButton,
    AutoClose,
    Breakpoint,
    DropdownDirection,
    HeadingLevel,
    Size,
    VariantWithLink,
)


class Dropdown(LibraryComponent):
    name = "bs-dropdown"

    class Kwargs:
        direction: DropdownDirection = "down"
        centered: bool = False
        auto_close: AutoClose | None = None
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        dropdown_id = (kwargs.attrs or {}).get("id") or f"dropdown-{self.id}"

        if kwargs.centered:
            if kwargs.direction == "up":
                wrapper_class = "dropup dropup-center"
            else:
                wrapper_class = "dropdown dropdown-center"
        else:
            if kwargs.direction == "up":
                wrapper_class = "dropup"
            elif kwargs.direction == "end":
                wrapper_class = "dropend"
            elif kwargs.direction == "start":
                wrapper_class = "dropstart"
            else:
                wrapper_class = "dropdown"

        data = {
            "dropdown_id": dropdown_id,
            "wrapper_class": wrapper_class,
            "auto_close": kwargs.auto_close,
            "direction": kwargs.direction,
            "attrs": kwargs.attrs,
        }
        data["div_attrs"] = merge_attrs((data["attrs"] or {}), {"class": data["wrapper_class"]})
        return data

    template = """
        <c-provide key="dropdown" c-dropdown_id="dropdown_id" c-direction="direction" c-auto_close="auto_close">
        <div c-bind="div_attrs">
        <c-slot />
        </div>
        </c-provide>
    """


class DropdownToggle(LibraryComponent):
    name = "bs-dropdown-toggle"

    class Kwargs:
        variant: VariantWithLink = "primary"
        split: bool = False
        size: Size | None = None
        disabled: bool = False
        href: str | None = None
        attrs: dict | None = None

    class Slots:
        default: SlotInput | None = None

    def template_data(self, kwargs: Kwargs, slots: Slots):
        dropdown = self.inject("dropdown")

        classes = ["btn", f"btn-{kwargs.variant}", "dropdown-toggle"]
        if kwargs.split:
            classes.append("dropdown-toggle-split")
        if kwargs.size:
            classes.append(f"btn-{kwargs.size}")

        disabled = True if kwargs.disabled else None

        data = {
            "classes": " ".join(classes),
            "disabled": disabled,
            "auto_close": dropdown.auto_close,
            "attrs": kwargs.attrs,
        }
        data["button_attrs"] = merge_attrs(
            {"aria-expanded": "false", "disabled": data["disabled"]},
            (data["attrs"] or {}),
            {"class": data["classes"], "type": "button", "data-bs-toggle": "dropdown"},
            ({"data-bs-auto-close": data["auto_close"]} if data["auto_close"] else {}),
        )
        return data

    template = """
        <button c-bind="button_attrs" >
        <c-slot />
        </button>
    """


class DropdownMenu(LibraryComponent):
    name = "bs-dropdown-menu"

    class Kwargs:
        align: AlignmentStartEnd | None = None
        align_responsive: dict[Breakpoint, AlignmentStartEnd] | None = None
        align_sm: AlignmentStartEnd | None = None
        align_md: AlignmentStartEnd | None = None
        align_lg: AlignmentStartEnd | None = None
        align_xl: AlignmentStartEnd | None = None
        align_xxl: AlignmentStartEnd | None = None
        dark: bool = False
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        classes = ["dropdown-menu"]

        if kwargs.align == "end":
            classes.append("dropdown-menu-end")

        if kwargs.align_responsive:
            for breakpoint, alignment in kwargs.align_responsive.items():
                classes.append(f"dropdown-menu-{breakpoint}-{alignment}")

        if kwargs.align_sm:
            classes.append(f"dropdown-menu-sm-{kwargs.align_sm}")
        if kwargs.align_md:
            classes.append(f"dropdown-menu-md-{kwargs.align_md}")
        if kwargs.align_lg:
            classes.append(f"dropdown-menu-lg-{kwargs.align_lg}")
        if kwargs.align_xl:
            classes.append(f"dropdown-menu-xl-{kwargs.align_xl}")
        if kwargs.align_xxl:
            classes.append(f"dropdown-menu-xxl-{kwargs.align_xxl}")

        if kwargs.dark:
            classes.append("dropdown-menu-dark")

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


class DropdownItem(LibraryComponent):
    name = "bs-dropdown-item"

    class Kwargs:
        as_: AnchorOrButton = "a"
        href: str = "#"
        active: bool = False
        disabled: bool = False
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        classes = ["dropdown-item"]
        if kwargs.active:
            classes.append("active")
        if kwargs.disabled:
            classes.append("disabled")

        aria_current = "true" if kwargs.active else None
        button_disabled = True if kwargs.as_ == "button" and kwargs.disabled else None
        link_aria_disabled = "true" if kwargs.as_ == "a" and kwargs.disabled else None
        link_tabindex = "-1" if kwargs.as_ == "a" and kwargs.disabled else None

        data = {
            "tag": kwargs.as_,
            "classes": " ".join(classes),
            "href": kwargs.href,
            "aria_current": aria_current,
            "button_disabled": button_disabled,
            "link_aria_disabled": link_aria_disabled,
            "link_tabindex": link_tabindex,
            "attrs": kwargs.attrs,
        }
        data["a_attrs"] = merge_attrs(
            {
                "aria-current": data["aria_current"],
                "aria-disabled": data["link_aria_disabled"],
                "tabindex": data["link_tabindex"],
            },
            (data["attrs"] or {}),
            {"href": data["href"], "class": data["classes"]},
        )
        data["button_attrs"] = merge_attrs(
            {"aria-current": data["aria_current"], "disabled": data["button_disabled"]},
            (data["attrs"] or {}),
            {"type": "button", "class": data["classes"]},
        )
        return data

    template = """
        <li>
        <c-if cond="(tag == 'a')">
        <a c-bind="a_attrs">
        <c-slot />
        </a>
        </c-if><c-else>
        <button c-bind="button_attrs">
        <c-slot />
        </button>
        </c-else>
        </li>
    """


class DropdownDivider(LibraryComponent):
    name = "bs-dropdown-divider"

    class Kwargs:
        attrs: dict | None = None

    def template_data(self, kwargs: Kwargs, slots):
        data = {
            "attrs": kwargs.attrs,
        }
        data["hr_attrs"] = merge_attrs((data["attrs"] or {}), {"class": "dropdown-divider"})
        return data

    template = """
        <li><hr c-bind="hr_attrs"></li>
    """


class DropdownHeader(LibraryComponent):
    name = "bs-dropdown-header"

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
        data["element_attrs"] = merge_attrs((data["attrs"] or {}), {"class": "dropdown-header"})
        return data

    template = """
        <li>
        <c-element c-is="tag" c-bind="element_attrs">
        <c-slot />
        </c-element>
        </li>
    """


class DropdownItemText(LibraryComponent):
    name = "bs-dropdown-item-text"

    class Kwargs:
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        data = {
            "attrs": kwargs.attrs,
        }
        data["span_attrs"] = merge_attrs((data["attrs"] or {}), {"class": "dropdown-item-text"})
        return data

    template = """
        <li>
        <span c-bind="span_attrs">
        <c-slot />
        </span>
        </li>
    """
