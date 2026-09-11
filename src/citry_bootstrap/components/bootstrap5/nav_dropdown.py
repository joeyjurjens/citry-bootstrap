from citry import SlotInput

from citry_bootstrap.component import BootstrapComponent
from citry_bootstrap.components.bootstrap5.types import AutoClose


class NavDropdown(BootstrapComponent):
    name = "bs-nav-dropdown"

    class Kwargs:
        title: str
        active: bool = False
        disabled: bool = False
        auto_close: AutoClose | None = None
        align: str | None = None
        dark: bool = False
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        dropdown_id = (kwargs.attrs or {}).get("id") or f"nav-dropdown-{self.id}"

        # Merge default attrs with user-provided attrs
        # User attrs override defaults
        default_attrs = {
            "id": dropdown_id,
            "class": "dropdown-toggle",
            "data-bs-toggle": "dropdown",
            "aria-expanded": "false",
        }
        if kwargs.auto_close:
            default_attrs["data-bs-auto-close"] = kwargs.auto_close
        merged_attrs = {**default_attrs, **(kwargs.attrs or {})}

        return {
            "dropdown_id": dropdown_id,
            "title": kwargs.title,
            "active": kwargs.active,
            "disabled": kwargs.disabled,
            "auto_close": kwargs.auto_close,
            "align": kwargs.align,
            "dark": kwargs.dark,
            "merged_attrs": merged_attrs,
        }

    template = """
        <li class="nav-item dropdown">
        <c-bs-nav-link as_="button" c-disabled="disabled" c-attrs="merged_attrs">
        {{ title }}
        </c-bs-nav-link>
        <c-bs-dropdown-menu c-align="align" c-dark="dark">
        <c-slot />
        </c-bs-dropdown-menu>
        </li>
    """
