from citry import LibraryComponent, SlotInput

from citry_bootstrap.components.bootstrap5.types import AutoClose, Size, VariantWithLink


class DropdownButton(LibraryComponent):
    name = "bs-dropdown-button"

    class Kwargs:
        title: str
        variant: VariantWithLink = "primary"
        size: Size | None = None
        disabled: bool = False
        href: str | None = None
        auto_close: AutoClose | None = None
        align: str | None = None
        dark: bool = False
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        dropdown_id = (kwargs.attrs or {}).get("id") or f"dropdown-button-{self.id}"

        return {
            "dropdown_id": dropdown_id,
            "title": kwargs.title,
            "variant": kwargs.variant,
            "size": kwargs.size,
            "disabled": kwargs.disabled,
            "href": kwargs.href,
            "auto_close": kwargs.auto_close,
            "align": kwargs.align,
            "dark": kwargs.dark,
            "attrs": kwargs.attrs,
        }

    template = """
        <c-bs-dropdown c-auto_close="auto_close" c-attrs="attrs">
        <c-bs-dropdown-toggle c-variant="variant" c-size="size" c-disabled="disabled" c-href="href">
        {{ title }}
        </c-bs-dropdown-toggle>
        <c-bs-dropdown-menu c-align="align" c-dark="dark">
        <c-slot />
        </c-bs-dropdown-menu>
        </c-bs-dropdown>
    """


class SplitButton(LibraryComponent):
    name = "bs-split-button"

    class Kwargs:
        title: str
        variant: VariantWithLink = "primary"
        size: Size | None = None
        disabled: bool = False
        href: str | None = None
        target: str | None = None
        type: str = "button"
        toggle_label: str = "Toggle dropdown"
        auto_close: AutoClose | None = None
        align: str | None = None
        dark: bool = False
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        dropdown_id = (kwargs.attrs or {}).get("id") or f"split-button-{self.id}"

        return {
            "dropdown_id": dropdown_id,
            "title": kwargs.title,
            "variant": kwargs.variant,
            "size": kwargs.size,
            "disabled": kwargs.disabled,
            "href": kwargs.href,
            "target": kwargs.target,
            "type": kwargs.type,
            "toggle_label": kwargs.toggle_label,
            "auto_close": kwargs.auto_close,
            "align": kwargs.align,
            "dark": kwargs.dark,
            "attrs": kwargs.attrs,
        }

    template = """
        <c-bs-dropdown c-auto_close="auto_close">
        <c-bs-button-group c-attrs="attrs">
        <c-bs-button c-variant="variant" c-size="size" c-disabled="disabled" c-href="href" c-target="target" c-type="type">
        {{ title }}
        </c-bs-button>
        <c-bs-dropdown-toggle c-split="True" c-variant="variant" c-size="size" c-disabled="disabled">
        <span class="visually-hidden">{{ toggle_label }}</span>
        </c-bs-dropdown-toggle>
        <c-bs-dropdown-menu c-align="align" c-dark="dark">
        <c-slot />
        </c-bs-dropdown-menu>
        </c-bs-button-group>
        </c-bs-dropdown>
    """
