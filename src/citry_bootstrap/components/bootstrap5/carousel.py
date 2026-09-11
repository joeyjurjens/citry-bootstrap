from types import SimpleNamespace

from citry import LibraryComponent, Markup, SlotInput, const_value, merge_attrs

from citry_bootstrap.components.bootstrap5.types import (
    NOT_PROVIDED,
    CarouselPause,
    CarouselRide,
    ThemeVariant,
)


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


class Carousel(LibraryComponent):
    name = "bs-carousel"

    class Kwargs:
        fade: bool = False
        controls: bool = True
        indicators: bool = True
        ride: CarouselRide = False
        interval: int | None = None
        keyboard: bool = True
        pause: CarouselPause = "hover"
        touch: bool = True
        theme: ThemeVariant | None = None
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots):
        kwargs = _plain(kwargs)
        carousel_id = (kwargs.attrs or {}).get("id") or f"carousel-{self.id}"
        items = []

        data = {
            "carousel_id": carousel_id,
            "fade": kwargs.fade,
            "controls": kwargs.controls,
            "indicators": kwargs.indicators,
            "ride": kwargs.ride,
            "interval": kwargs.interval,
            "keyboard": kwargs.keyboard,
            "pause": kwargs.pause,
            "touch": kwargs.touch,
            "theme": kwargs.theme,
            "attrs": kwargs.attrs,
            "items": items,
        }
        self._render_context = data
        return data

    template = """
        <c-provide key="carousel" c-carousel_id="carousel_id" c-items="items">
        <c-slot required />
        </c-provide>
    """

    def on_render(self):
        result, error = yield
        content = str(result)
        context = self._render_context
        items: list[dict] = context["items"]

        return _sibling(self, "carousel", "carousel-renderer")(
            **{
                "carousel_id": context["carousel_id"],
                "fade": context["fade"],
                "controls": context["controls"],
                "indicators": context["indicators"],
                "ride": context["ride"],
                "interval": context["interval"],
                "keyboard": context["keyboard"],
                "pause": context["pause"],
                "touch": context["touch"],
                "theme": context["theme"],
                "attrs": context["attrs"],
                "items": items,
            },
            slots={"default": Markup(content)},
        )


class CarouselRenderer(LibraryComponent):
    name = "bs-carousel-renderer"

    class Kwargs:
        carousel_id: str
        fade: bool
        controls: bool
        indicators: bool
        ride: CarouselRide
        interval: int | None
        keyboard: bool
        pause: CarouselPause
        touch: bool
        theme: ThemeVariant | None
        items: list[dict]
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        kwargs = _plain(kwargs)
        classes = ["carousel", "slide"]
        if kwargs.fade:
            classes.append("carousel-fade")

        data_bs_ride = "carousel" if kwargs.ride is True else kwargs.ride if kwargs.ride else None
        data_bs_interval = kwargs.interval
        data_bs_keyboard = "false" if not kwargs.keyboard else None
        data_bs_pause = kwargs.pause if kwargs.pause != "hover" else None
        data_bs_touch = "false" if not kwargs.touch else None
        data_bs_theme = kwargs.theme

        data = {
            "carousel_id": kwargs.carousel_id,
            "classes": " ".join(classes),
            "controls": kwargs.controls,
            "show_indicators": kwargs.indicators,
            "data_bs_ride": data_bs_ride,
            "data_bs_interval": data_bs_interval,
            "data_bs_keyboard": data_bs_keyboard,
            "data_bs_pause": data_bs_pause,
            "data_bs_touch": data_bs_touch,
            "data_bs_theme": data_bs_theme,
            "attrs": kwargs.attrs,
            "items": kwargs.items,
        }
        data["div_attrs"] = merge_attrs(
            {
                "id": data["carousel_id"],
                "data-bs-ride": data["data_bs_ride"],
                "data-bs-interval": data["data_bs_interval"],
                "data-bs-keyboard": data["data_bs_keyboard"],
                "data-bs-pause": data["data_bs_pause"],
                "data-bs-touch": data["data_bs_touch"],
                "data-bs-theme": data["data_bs_theme"],
            },
            (data["attrs"] or {}),
            {"class": data["classes"]},
        )
        data["span_attrs"] = merge_attrs(
            {"aria-hidden": "true"}, {"class": "carousel-control-prev-icon"}
        )
        data["span_attrs2"] = merge_attrs(
            {"aria-hidden": "true"}, {"class": "carousel-control-next-icon"}
        )
        data["loop"] = list(enumerate(data["items"]))
        return data

    template = """
        <c-provide key="carousel" c-carousel_id="carousel_id">
        <div c-bind="div_attrs">
        <c-if cond="show_indicators">
        <div class="carousel-indicators">
        <c-for each="forloop_index, item in loop">
        <c-bs-carousel-indicator c-slide_to="forloop_index" c-active="item['active']" />
        </c-for>
        </div>
        </c-if>
        <div class="carousel-inner">
        <c-slot required />
        </div>
        <c-if cond="controls">
        <button class="carousel-control-prev" type="button" c-data-bs-target='f"#{carousel_id}"' data-bs-slide="prev">
        <span c-bind="span_attrs"></span>
        <span class="visually-hidden">Previous</span>
        </button>
        <button class="carousel-control-next" type="button" c-data-bs-target='f"#{carousel_id}"' data-bs-slide="next">
        <span c-bind="span_attrs2"></span>
        <span class="visually-hidden">Next</span>
        </button>
        </c-if>
        </div>
        </c-provide>
    """


class CarouselItem(LibraryComponent):
    name = "bs-carousel-item"

    class Kwargs:
        active: bool = False
        interval: int | None = None
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        kwargs = _plain(kwargs)
        carousel = self.inject("carousel")

        classes = ["carousel-item"]
        if kwargs.active:
            classes.append("active")

        data = {
            "parent_items": carousel.items,
            "active": kwargs.active,
            "classes": " ".join(classes),
            "interval": kwargs.interval,
            "attrs": kwargs.attrs,
        }
        data["div_attrs"] = merge_attrs(
            {"data-bs-interval": data["interval"]},
            (data["attrs"] or {}),
            {"class": data["classes"]},
        )
        self._render_context = data
        return data

    template = """
        <div c-bind="div_attrs">
        <c-slot />
        </div>
    """

    def on_render(self):
        result, error = yield
        context = self._render_context
        parent_items: list[dict] = context["parent_items"]
        parent_items.append(
            {
                "active": context["active"],
            }
        )
        return None


class CarouselCaption(LibraryComponent):
    name = "bs-carousel-caption"

    class Kwargs:
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        kwargs = _plain(kwargs)
        data = {
            "attrs": kwargs.attrs,
        }
        data["div_attrs"] = merge_attrs((data["attrs"] or {}), {"class": "carousel-caption"})
        return data

    template = """
        <div c-bind="div_attrs">
        <c-slot />
        </div>
    """


class CarouselIndicator(LibraryComponent):
    name = "bs-carousel-indicator"

    class Kwargs:
        slide_to: int = 0
        active: bool = False
        attrs: dict | None = None

    def template_data(self, kwargs: Kwargs, slots):
        kwargs = _plain(kwargs)
        carousel_data = self.inject("carousel", NOT_PROVIDED)
        carousel_id = carousel_data.carousel_id if carousel_data is not NOT_PROVIDED else ""

        classes = []
        if kwargs.active:
            classes.append("active")

        aria_label = f"Slide {kwargs.slide_to + 1}"

        data = {
            "carousel_id": carousel_id,
            "slide_to": kwargs.slide_to,
            "aria_label": aria_label,
            "active": kwargs.active,
            "classes": " ".join(classes) if classes else None,
            "attrs": kwargs.attrs,
        }
        data["button_attrs"] = merge_attrs(
            {"aria-label": data["aria_label"]},
            (data["attrs"] or {}),
            {
                "type": "button",
                "data-bs-target": f"#{data['carousel_id']}",
                "data-bs-slide-to": data["slide_to"],
            },
            ({"class": data["classes"]} if data["classes"] else {}),
            ({"aria-current": "true"} if data["active"] else {}),
        )
        return data

    template = """
        <button c-bind="button_attrs"></button>
    """
