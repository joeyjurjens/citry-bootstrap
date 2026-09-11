from types import SimpleNamespace
from typing import NamedTuple

from citry import LibraryComponent, Markup, SlotInput, const_value, merge_attrs

from citry_bootstrap.components.bootstrap5.types import NOT_PROVIDED, NavVariant
from citry_bootstrap.text import slugify


def _sibling(component, own, wanted):
    """A component of the same library, under whatever prefix it is published."""
    return component.citry.get(component.name.removesuffix(own) + wanted)


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


class TabContext(NamedTuple):
    id: str
    tab_data: list[dict]
    enabled: bool


class TabContainer(LibraryComponent):
    name = "bs-tab-container"

    class Kwargs:
        active_key: str | None = None
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        kwargs = _plain(kwargs)
        container_id = (kwargs.attrs or {}).get("id") or f"tab-container-{self.id}"

        data = {
            "container_id": container_id,
            "active_key": kwargs.active_key,
            "attrs": kwargs.attrs or {},
        }
        data["div_attrs"] = merge_attrs({"id": data["container_id"]}, (data["attrs"] or {}))
        return data

    template = """
        <c-provide key="tab_container" c-id="container_id" c-active_key="active_key">
        <div c-bind="div_attrs">
        <c-slot />
        </div>
        </c-provide>
    """


class TabContent(LibraryComponent):
    name = "bs-tab-content"

    class Kwargs:
        as_: str = "div"
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        kwargs = _plain(kwargs)
        data = {
            "tag": kwargs.as_,
            "attrs": kwargs.attrs or {},
        }
        data["element_attrs"] = merge_attrs({"class": "tab-content"}, (data["attrs"] or {}))
        return data

    template = """
        <c-element c-is="tag" c-bind="element_attrs">
        <c-slot />
        </c-element>
    """


class TabPane(LibraryComponent):
    name = "bs-tab-pane"

    class Kwargs:
        event_key: str | None = None
        active: bool | None = None
        fade: bool = True
        as_: str = "div"
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        kwargs = _plain(kwargs)
        tab_container = self.inject("tab_container", NOT_PROVIDED)

        is_active = kwargs.active
        generated_id = None
        generated_labelledby = None

        if kwargs.event_key is not None and tab_container is not NOT_PROVIDED:
            if is_active is None:
                is_active = kwargs.event_key == tab_container.active_key
            generated_id = f"{tab_container.id}-pane-{kwargs.event_key}"
            generated_labelledby = f"{tab_container.id}-tab-{kwargs.event_key}"

        is_active = bool(is_active)

        classes = ["tab-pane"]
        if kwargs.fade:
            classes.append("fade")
        if is_active:
            classes.append("show active")

        data = {
            "tag": kwargs.as_,
            "classes": " ".join(classes),
            "generated_id": generated_id,
            "generated_labelledby": generated_labelledby,
            "attrs": kwargs.attrs or {},
        }
        data["element_attrs"] = merge_attrs(
            {
                "role": "tabpanel",
                "tabindex": "0",
                "id": data["generated_id"],
                "aria-labelledby": data["generated_labelledby"],
            },
            (data["attrs"] or {}),
            {"class": data["classes"]},
        )
        return data

    template = """
        <c-element c-is="tag" c-bind="element_attrs">
        <c-slot />
        </c-element>
    """


class TabsRenderer(LibraryComponent):
    name = "bs-tabs-renderer"

    class Kwargs:
        tabs_id: str
        variant: NavVariant
        fill: bool
        justified: bool
        tab_data: list[dict]
        attrs: dict | None

    def template_data(self, kwargs: Kwargs, slots):
        kwargs = _plain(kwargs)
        data = {
            "tabs_id": kwargs.tabs_id,
            "variant": kwargs.variant,
            "fill": kwargs.fill,
            "justified": kwargs.justified,
            "tab_data": kwargs.tab_data,
            "attrs": kwargs.attrs or {},
        }
        data["div_attrs"] = data["attrs"] or {}
        return data

    template = """
        <div c-bind="div_attrs">
        <c-bs-nav c-variant="variant" c-fill="fill" c-justified="justified" as_="ul" c-attrs="{'id': tabs_id, 'role': 'tablist'}">
        <c-for each="tab in tab_data">
        <c-bs-nav-item as_="li" c-attrs="{'role': 'presentation'}">
        <c-bs-nav-link as_="button" c-active="tab['is_active']" c-disabled="tab['disabled']" c-attrs="{'id': tab['nav_tab_id'], 'data-bs-toggle': 'tab', 'data-bs-target': f'#{tab['pane_id']}', 'role': 'tab', 'aria-controls': tab['pane_id'], 'aria-selected': tab['aria_selected']}">
        {{ tab['title'] }}
        </c-bs-nav-link>
        </c-bs-nav-item>
        </c-for>
        </c-bs-nav>
        <c-bs-tab-content>
        <c-for each="tab in tab_data">
        <c-bs-tab-pane c-active="tab['is_active']" c-attrs="{'id': tab['pane_id'], 'aria-labelledby': tab['nav_tab_id']}">
        {{ tab['content'] }}
        </c-bs-tab-pane>
        </c-for>
        </c-bs-tab-content>
        </div>
    """


class Tabs(LibraryComponent):
    name = "bs-tabs"

    class Kwargs:
        variant: NavVariant = "tabs"
        fill: bool = False
        justified: bool = False
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        kwargs = _plain(kwargs)
        tabs_id = (kwargs.attrs or {}).get("id") or f"tabs-{self.id}"
        tab_data: list[dict] = []

        data = {
            "tabs_id": tabs_id,
            "variant": kwargs.variant,
            "fill": kwargs.fill,
            "justified": kwargs.justified,
            "tab_data": tab_data,
            "attrs": kwargs.attrs or {},
        }
        self._render_context = data
        return data

    template = """
        <c-provide key="_tabs" c-id="tabs_id" c-tab_data="tab_data" c-enabled="True">
        <c-slot />
        </c-provide>
    """

    def on_render(self):
        result, error = yield
        context = self._render_context
        tab_data: list[dict] = context["tab_data"]

        active_tabs = [tab for tab in tab_data if tab["is_active"]]
        for extra_tab in active_tabs[1:]:
            extra_tab["is_active"] = False
            extra_tab["aria_selected"] = "false"

        if tab_data and not active_tabs:
            default_tab = next((tab for tab in tab_data if not tab["disabled"]), None)
            if default_tab is not None:
                default_tab["is_active"] = True
                default_tab["aria_selected"] = "true"

        return _sibling(self, "tabs", "tabs-renderer")(
            **{
                "tabs_id": context["tabs_id"],
                "variant": context["variant"],
                "fill": context["fill"],
                "justified": context["justified"],
                "tab_data": tab_data,
                "attrs": context["attrs"],
            }
        )


class Tab(LibraryComponent):
    name = "bs-tab"

    class Kwargs:
        title: str
        tab_id: str | None = None
        active: bool = False
        disabled: bool = False

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        kwargs = _plain(kwargs)
        tabs_ctx: TabContext = self.inject("_tabs", NOT_PROVIDED)
        if tabs_ctx is NOT_PROVIDED:
            raise RuntimeError(
                f"'{self.registered_name}' must be used as a child of 'Tabs' component"
            )

        if not tabs_ctx.enabled:
            raise RuntimeError(
                f"'{self.registered_name}' must be a direct child of 'Tabs' component"
            )

        tab_index = len(tabs_ctx.tab_data)
        tab_id = kwargs.tab_id or slugify(kwargs.title) or f"tab-{tab_index}"
        slugs = (slugify(tabs_ctx.id), tab_id)
        nav_tab_id = f"{slugs[0]}-tab-{slugs[1]}"
        pane_id = f"{slugs[0]}-pane-{slugs[1]}"

        data = {
            "parent_tabs": tabs_ctx.tab_data,
            "nav_tab_id": nav_tab_id,
            "pane_id": pane_id,
            "tab_id": tab_id,
            "title": kwargs.title,
            "active": kwargs.active,
            "disabled": kwargs.disabled,
            "empty_tab_data": [],
        }
        self._render_context = data
        return data

    template = """
        <c-provide key="_tabs" c-id="''" c-tab_data="empty_tab_data" c-enabled="False">
        <c-slot />
        </c-provide>
    """

    def on_render(self):
        result, error = yield
        content = str(result)
        context = self._render_context
        parent_tabs: list[dict] = context["parent_tabs"]
        is_active = context["active"]

        parent_tabs.append(
            {
                "nav_tab_id": context["nav_tab_id"],
                "pane_id": context["pane_id"],
                "tab_id": context["tab_id"],
                "title": context["title"],
                "disabled": context["disabled"],
                "is_active": is_active,
                "aria_selected": "true" if is_active else "false",
                "content": Markup(content.strip()),
            }
        )
        return None
