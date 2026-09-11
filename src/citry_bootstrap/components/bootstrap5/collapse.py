from types import SimpleNamespace

from citry import LibraryComponent, SlotInput, const_value, merge_attrs

from citry_bootstrap.components.bootstrap5.types import ButtonTag


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


class Collapse(LibraryComponent):
    name = "bs-collapse"

    class Kwargs:
        show: bool = False
        horizontal: bool = False
        attrs: dict | None = None

    class Slots:
        default: SlotInput
        toggle: SlotInput | None = None

    def template_data(self, kwargs: Kwargs, slots: Slots):
        kwargs = _plain(kwargs)
        collapse_id = (kwargs.attrs or {}).get("id") or f"collapse-{self.id}"

        classes = ["collapse"]
        if kwargs.horizontal:
            classes.append("collapse-horizontal")
        if kwargs.show:
            classes.append("show")

        data = {
            "collapse_id": collapse_id,
            "classes": " ".join(classes),
            "show": kwargs.show,
            "attrs": kwargs.attrs,
        }
        data["div_attrs"] = merge_attrs(
            {"id": data["collapse_id"]}, (data["attrs"] or {}), {"class": data["classes"]}
        )
        return data

    template = """
        <c-provide key="collapse" c-collapse_id="collapse_id" c-show="show">
        <c-slot name="toggle" />
        <div c-bind="div_attrs">
        <c-slot />
        </div>
        </c-provide>
    """


class CollapseToggle(LibraryComponent):
    name = "bs-collapse-toggle"

    class Kwargs:
        as_: ButtonTag = "button"
        expanded: bool | None = None
        href: str | None = None
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        kwargs = _plain(kwargs)
        collapse = self.inject("collapse")
        target_id = collapse.collapse_id
        is_expanded = kwargs.expanded if kwargs.expanded is not None else collapse.show

        button_type = "button" if kwargs.as_ == "button" else None
        link_href = kwargs.href or f"#{target_id}" if kwargs.as_ != "button" else None
        link_role = "button" if kwargs.as_ != "button" else None

        data = {
            "tag": kwargs.as_,
            "target_id": target_id,
            "expanded": "true" if is_expanded else "false",
            "button_type": button_type,
            "link_href": link_href,
            "link_role": link_role,
            "attrs": kwargs.attrs,
        }
        data["button_attrs"] = merge_attrs(
            {
                "type": data["button_type"],
                "aria-expanded": data["expanded"],
                "aria-controls": data["target_id"],
            },
            (data["attrs"] or {}),
            {"data-bs-toggle": "collapse", "data-bs-target": f"#{data['target_id']}"},
        )
        data["a_attrs"] = merge_attrs(
            {
                "href": data["link_href"],
                "role": data["link_role"],
                "aria-expanded": data["expanded"],
                "aria-controls": data["target_id"],
            },
            (data["attrs"] or {}),
            {"data-bs-toggle": "collapse"},
        )
        return data

    template = """
        <c-if cond="(tag == 'button')">
        <button c-bind="button_attrs">
        <c-slot />
        </button>
        </c-if><c-else>
        <a c-bind="a_attrs">
        <c-slot />
        </a>
        </c-else>
    """
