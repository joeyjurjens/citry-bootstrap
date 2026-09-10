from citry import LibraryComponent, SlotInput, merge_attrs

from citry_bootstrap.components.bootstrap5.types import (
    ResponsiveBreakpoint,
    Variant,
)


class Table(LibraryComponent):
    name = "bs-table"

    class Kwargs:
        striped: bool = False
        striped_columns: bool = False
        bordered: bool = False
        borderless: bool = False
        hover: bool = False
        small: bool = False
        variant: Variant | None = None
        responsive: ResponsiveBreakpoint | None = None
        caption_top: bool = False
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        classes = ["table"]

        if kwargs.striped:
            classes.append("table-striped")
        if kwargs.striped_columns:
            classes.append("table-striped-columns")
        if kwargs.bordered:
            classes.append("table-bordered")
        if kwargs.borderless:
            classes.append("table-borderless")
        if kwargs.hover:
            classes.append("table-hover")
        if kwargs.small:
            classes.append("table-sm")
        if kwargs.variant:
            classes.append(f"table-{kwargs.variant}")
        if kwargs.caption_top:
            classes.append("caption-top")

        responsive_class = None
        if kwargs.responsive is not None:
            if kwargs.responsive is True:
                responsive_class = "table-responsive"
            else:
                responsive_class = f"table-responsive-{kwargs.responsive}"

        data = {
            "classes": " ".join(classes),
            "responsive_class": responsive_class,
            "attrs": kwargs.attrs,
        }
        data["table_attrs"] = merge_attrs((data["attrs"] or {}), {"class": data["classes"]})
        return data

    template = """
        <c-if cond="responsive_class">
        <div c-class="responsive_class">
        <table c-bind="table_attrs">
        <c-slot />
        </table>
        </div>
        </c-if><c-else>
        <table c-bind="table_attrs">
        <c-slot />
        </table>
        </c-else>
    """
