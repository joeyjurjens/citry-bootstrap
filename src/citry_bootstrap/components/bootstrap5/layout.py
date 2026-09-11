from types import SimpleNamespace

from citry import LibraryComponent, SlotInput, const_value, merge_attrs

from citry_bootstrap.components.bootstrap5.types import (
    BreakpointOrAuto,
    ContainerFluid,
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


class Container(LibraryComponent):
    name = "bs-container"

    class Kwargs:
        as_: str = "div"
        fluid: ContainerFluid | None = None
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        kwargs = _plain(kwargs)
        if kwargs.fluid is True:
            container_class = "container-fluid"
        elif kwargs.fluid:
            container_class = f"container-{kwargs.fluid}"
        else:
            container_class = "container"

        data = {
            "tag": kwargs.as_,
            "container_class": container_class,
            "attrs": kwargs.attrs,
        }
        data["element_attrs"] = merge_attrs(
            (data["attrs"] or {}), {"class": data["container_class"]}
        )
        return data

    template = """
        <c-element c-is="tag" c-bind="element_attrs">
        <c-slot />
        </c-element>
    """


class Row(LibraryComponent):
    name = "bs-row"

    class Kwargs:
        as_: str = "div"
        cols: int | None = None
        cols_sm: int | None = None
        cols_md: int | None = None
        cols_lg: int | None = None
        cols_xl: int | None = None
        cols_xxl: int | None = None
        gutter: int | None = None
        gutter_x: int | None = None
        gutter_y: int | None = None
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        kwargs = _plain(kwargs)
        classes = ["row"]

        if kwargs.cols is not None:
            classes.append(f"row-cols-{kwargs.cols}")
        if kwargs.cols_sm is not None:
            classes.append(f"row-cols-sm-{kwargs.cols_sm}")
        if kwargs.cols_md is not None:
            classes.append(f"row-cols-md-{kwargs.cols_md}")
        if kwargs.cols_lg is not None:
            classes.append(f"row-cols-lg-{kwargs.cols_lg}")
        if kwargs.cols_xl is not None:
            classes.append(f"row-cols-xl-{kwargs.cols_xl}")
        if kwargs.cols_xxl is not None:
            classes.append(f"row-cols-xxl-{kwargs.cols_xxl}")

        if kwargs.gutter is not None:
            classes.append(f"g-{kwargs.gutter}")
        if kwargs.gutter_x is not None:
            classes.append(f"gx-{kwargs.gutter_x}")
        if kwargs.gutter_y is not None:
            classes.append(f"gy-{kwargs.gutter_y}")

        data = {
            "tag": kwargs.as_,
            "classes": " ".join(classes),
            "attrs": kwargs.attrs,
        }
        data["element_attrs"] = merge_attrs((data["attrs"] or {}), {"class": data["classes"]})
        return data

    template = """
        <c-element c-is="tag" c-bind="element_attrs">
        <c-slot />
        </c-element>
    """


class Col(LibraryComponent):
    name = "bs-col"

    class Kwargs:
        as_: str = "div"
        col: BreakpointOrAuto | None = None  # Base col without breakpoint
        xs: BreakpointOrAuto | None = None
        sm: BreakpointOrAuto | None = None
        md: BreakpointOrAuto | None = None
        lg: BreakpointOrAuto | None = None
        xl: BreakpointOrAuto | None = None
        xxl: BreakpointOrAuto | None = None
        auto: bool = False
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        kwargs = _plain(kwargs)
        classes = []

        has_breakpoint = any(
            [kwargs.col, kwargs.xs, kwargs.sm, kwargs.md, kwargs.lg, kwargs.xl, kwargs.xxl]
        )

        if not has_breakpoint and not kwargs.auto:
            classes.append("col")
        else:
            if kwargs.col is not None:
                if kwargs.col == "auto":
                    classes.append("col-auto")
                else:
                    classes.append(f"col-{kwargs.col}")

            if kwargs.xs is not None:
                if kwargs.xs == "auto":
                    classes.append("col-auto")
                else:
                    classes.append(f"col-{kwargs.xs}")
            if kwargs.sm is not None:
                if kwargs.sm == "auto":
                    classes.append("col-sm-auto")
                else:
                    classes.append(f"col-sm-{kwargs.sm}")
            if kwargs.md is not None:
                if kwargs.md == "auto":
                    classes.append("col-md-auto")
                else:
                    classes.append(f"col-md-{kwargs.md}")
            if kwargs.lg is not None:
                if kwargs.lg == "auto":
                    classes.append("col-lg-auto")
                else:
                    classes.append(f"col-lg-{kwargs.lg}")
            if kwargs.xl is not None:
                if kwargs.xl == "auto":
                    classes.append("col-xl-auto")
                else:
                    classes.append(f"col-xl-{kwargs.xl}")
            if kwargs.xxl is not None:
                if kwargs.xxl == "auto":
                    classes.append("col-xxl-auto")
                else:
                    classes.append(f"col-xxl-{kwargs.xxl}")
            if kwargs.auto:
                classes.append("col-auto")

        data = {
            "tag": kwargs.as_,
            "classes": " ".join(classes) if classes else "col",
            "attrs": kwargs.attrs,
        }
        data["element_attrs"] = merge_attrs((data["attrs"] or {}), {"class": data["classes"]})
        return data

    template = """
        <c-element c-is="tag" c-bind="element_attrs">
        <c-slot />
        </c-element>
    """
