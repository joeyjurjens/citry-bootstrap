from types import SimpleNamespace

from citry import LibraryComponent, SlotInput, const_value, merge_attrs

from citry_bootstrap.components.bootstrap5.types import (
    NOT_PROVIDED,
    AnchorOrButton,
    NavItemTag,
    NavTag,
    NavVariant,
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


class Nav(LibraryComponent):
    name = "bs-nav"

    class Kwargs:
        variant: NavVariant | None = None
        fill: bool = False
        justified: bool = False
        vertical: bool = False
        as_: NavTag = "nav"
        role: str | None = None
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        kwargs = _plain(kwargs)
        classes = ["nav"]

        if kwargs.variant == "tabs":
            classes.append("nav-tabs")
        elif kwargs.variant == "pills":
            classes.append("nav-pills")
        elif kwargs.variant == "underline":
            classes.append("nav-underline")

        if kwargs.fill:
            classes.append("nav-fill")
        if kwargs.justified:
            classes.append("nav-justified")

        if kwargs.vertical:
            classes.append("flex-column")

        data = {
            "tag": kwargs.as_,
            "classes": " ".join(classes),
            "role": kwargs.role,
            "attrs": kwargs.attrs,
        }
        data["element_attrs"] = merge_attrs(
            {"role": data["role"]}, (data["attrs"] or {}), {"class": data["classes"]}
        )
        return data

    template = """
        <c-element c-is="tag" c-bind="element_attrs">
        <c-slot />
        </c-element>
    """


class NavItem(LibraryComponent):
    name = "bs-nav-item"

    class Kwargs:
        as_: NavItemTag = "li"
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        kwargs = _plain(kwargs)
        data = {
            "tag": kwargs.as_,
            "attrs": kwargs.attrs,
        }
        data["element_attrs"] = merge_attrs((data["attrs"] or {}), {"class": "nav-item"})
        return data

    template = """
        <c-element c-is="tag" c-bind="element_attrs">
        <c-slot />
        </c-element>
    """


class NavLink(LibraryComponent):
    name = "bs-nav-link"

    class Kwargs:
        as_: AnchorOrButton = "a"
        href: str = "#"
        event_key: str | None = None
        active: bool | None = None
        disabled: bool = False
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        kwargs = _plain(kwargs)
        tab_container = self.inject("tab_container", NOT_PROVIDED)

        is_active = kwargs.active
        is_tab = False
        generated_id = None
        generated_controls = None
        data_bs_target = None

        if kwargs.event_key is not None and tab_container is not NOT_PROVIDED:
            is_tab = True
            if is_active is None:
                is_active = kwargs.event_key == tab_container.active_key
            generated_id = f"{tab_container.id}-tab-{kwargs.event_key}"
            generated_controls = f"{tab_container.id}-pane-{kwargs.event_key}"
            data_bs_target = f"#{generated_controls}"

        is_active = bool(is_active)

        classes = ["nav-link"]
        if is_active:
            classes.append("active")
        if kwargs.disabled:
            classes.append("disabled")

        button_disabled = True if kwargs.as_ == "button" and kwargs.disabled else None
        aria_disabled = "true" if kwargs.as_ == "a" and kwargs.disabled else None
        aria_current = "page" if is_active and kwargs.as_ == "a" and not is_tab else None
        aria_selected = "true" if is_tab and is_active else "false" if is_tab else None
        role = "tab" if is_tab else None
        data_bs_toggle = "tab" if is_tab else None

        link_href = None if kwargs.disabled else kwargs.href

        data = {
            "tag": kwargs.as_,
            "classes": " ".join(classes),
            "href": link_href,
            "button_disabled": button_disabled,
            "aria_disabled": aria_disabled,
            "aria_current": aria_current,
            "aria_selected": aria_selected,
            "role": role,
            "data_bs_toggle": data_bs_toggle,
            "data_bs_target": data_bs_target,
            "generated_id": generated_id,
            "generated_controls": generated_controls,
            "attrs": kwargs.attrs,
        }
        data["a_attrs"] = merge_attrs(
            {
                "href": data["href"],
                "aria-disabled": data["aria_disabled"],
                "aria-current": data["aria_current"],
                "id": data["generated_id"],
                "role": data["role"],
                "data-bs-toggle": data["data_bs_toggle"],
                "data-bs-target": data["data_bs_target"],
                "aria-controls": data["generated_controls"],
                "aria-selected": data["aria_selected"],
            },
            (data["attrs"] or {}),
            {"class": data["classes"]},
        )
        data["button_attrs"] = merge_attrs(
            {
                "type": "button",
                "disabled": data["button_disabled"],
                "aria-current": data["aria_current"],
                "id": data["generated_id"],
                "role": data["role"],
                "data-bs-toggle": data["data_bs_toggle"],
                "data-bs-target": data["data_bs_target"],
                "aria-controls": data["generated_controls"],
                "aria-selected": data["aria_selected"],
            },
            (data["attrs"] or {}),
            {"class": data["classes"]},
        )
        return data

    template = """
        <c-if cond="(tag == 'a')">
        <a c-bind="a_attrs">
        <c-slot />
        </a>
        </c-if><c-else>
        <button c-bind="button_attrs">
        <c-slot />
        </button>
        </c-else>
    """
