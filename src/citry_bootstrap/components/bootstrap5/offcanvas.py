from types import SimpleNamespace

from citry import LibraryComponent, SlotInput, const_value, merge_attrs

from citry_bootstrap.components.bootstrap5.types import (
    BackdropBehavior,
    Breakpoint,
    ButtonTag,
    HeadingLevel,
    OffcanvasPlacement,
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


class Offcanvas(LibraryComponent):
    name = "bs-offcanvas"

    class Kwargs:
        placement: OffcanvasPlacement = "start"
        backdrop: BackdropBehavior | None = None
        scroll: bool = False
        keyboard: bool = True
        responsive: Breakpoint | None = None
        attrs: dict | None = None

    class Slots:
        default: SlotInput
        toggle: SlotInput | None = None

    def template_data(self, kwargs: Kwargs, slots: Slots):
        kwargs = _plain(kwargs)
        offcanvas_id = (kwargs.attrs or {}).get("id") or f"offcanvas-{self.id}"

        if kwargs.responsive:
            classes = [f"offcanvas-{kwargs.responsive}", f"offcanvas-{kwargs.placement}"]
        else:
            classes = ["offcanvas", f"offcanvas-{kwargs.placement}"]

        data = {
            "offcanvas_id": offcanvas_id,
            "classes": " ".join(classes),
            "backdrop": kwargs.backdrop,
            "scroll": kwargs.scroll,
            "keyboard": kwargs.keyboard,
            "attrs": kwargs.attrs,
        }
        data["div_attrs"] = merge_attrs(
            {"id": data["offcanvas_id"], "aria-labelledby": f"{data['offcanvas_id']}-label"},
            (data["attrs"] or {}),
            {"class": data["classes"], "tabindex": "-1"},
            ({"data-bs-backdrop": data["backdrop"]} if data["backdrop"] else {}),
            ({"data-bs-scroll": "true"} if data["scroll"] else {}),
            ({"data-bs-keyboard": "false"} if (not data["keyboard"]) else {}),
        )
        return data

    template = """
        <c-provide key="offcanvas" c-offcanvas_id="offcanvas_id">
        <c-slot name="toggle" />
        <div c-bind="div_attrs" >
        <c-slot />
        </div>
        </c-provide>
    """


class OffcanvasHeader(LibraryComponent):
    name = "bs-offcanvas-header"

    class Kwargs:
        close_button: bool = True
        close_label: str = "Close"
        close_variant: str | None = None
        attrs: dict | None = None

    class Slots:
        default: SlotInput | None = None

    def template_data(self, kwargs: Kwargs, slots: Slots):
        kwargs = _plain(kwargs)
        try:
            offcanvas = self.inject("offcanvas")
            offcanvas_id = offcanvas.offcanvas_id
        except KeyError:
            offcanvas_id = None
        data = {
            "close_button": kwargs.close_button,
            "close_label": kwargs.close_label,
            "close_variant": kwargs.close_variant,
            "offcanvas_id": offcanvas_id,
            "attrs": kwargs.attrs,
        }
        data["div_attrs"] = merge_attrs((data["attrs"] or {}), {"class": "offcanvas-header"})
        return data

    template = """
        <div c-bind="div_attrs">
        <c-slot />
        <c-if cond="close_button">
        <c-bs-close-button c-variant="close_variant" c-attrs="{'aria-label': close_label, 'data-bs-dismiss': 'offcanvas', 'data-bs-target': f'#{offcanvas_id}'}" />
        </c-if>
        </div>
    """


class OffcanvasBody(LibraryComponent):
    name = "bs-offcanvas-body"

    class Kwargs:
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        kwargs = _plain(kwargs)
        data = {
            "attrs": kwargs.attrs,
        }
        data["div_attrs"] = merge_attrs((data["attrs"] or {}), {"class": "offcanvas-body"})
        return data

    template = """
        <div c-bind="div_attrs">
        <c-slot />
        </div>
    """


class OffcanvasTitle(LibraryComponent):
    name = "bs-offcanvas-title"

    class Kwargs:
        as_: HeadingLevel = "h5"
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        kwargs = _plain(kwargs)
        offcanvas = self.inject("offcanvas")
        offcanvas_id = offcanvas.offcanvas_id

        data = {
            "tag": kwargs.as_,
            "offcanvas_id": offcanvas_id,
            "attrs": kwargs.attrs,
        }
        data["element_attrs"] = merge_attrs(
            (data["attrs"] or {}),
            {"class": "offcanvas-title", "id": f"{data['offcanvas_id']}-label"},
        )
        return data

    template = """
        <c-element c-is="tag" c-bind="element_attrs">
        <c-slot />
        </c-element>
    """


class OffcanvasToggle(LibraryComponent):
    name = "bs-offcanvas-toggle"

    class Kwargs:
        as_: ButtonTag = "button"
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        kwargs = _plain(kwargs)
        offcanvas = self.inject("offcanvas")
        target_id = offcanvas.offcanvas_id

        data = {
            "tag": kwargs.as_,
            "target_id": target_id,
            "attrs": kwargs.attrs,
        }
        data["element_attrs"] = merge_attrs(
            {"aria-controls": data["target_id"]},
            (data["attrs"] or {}),
            {"data-bs-toggle": "offcanvas", "data-bs-target": f"#{data['target_id']}"},
        )
        return data

    template = """
        <c-element c-is="tag" c-bind="element_attrs">
        <c-slot />
        </c-element>
    """
