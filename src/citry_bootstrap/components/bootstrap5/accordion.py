from citry import LibraryComponent, SlotInput, merge_attrs


class Accordion(LibraryComponent):
    name = "bs-accordion"

    class Kwargs:
        flush: bool = False
        always_open: bool = False
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        accordion_id = (kwargs.attrs or {}).get("id") or f"accordion-{self.id}"

        css_classes = ["accordion"]
        if kwargs.flush:
            css_classes.append("accordion-flush")

        data = {
            "accordion_id": accordion_id,
            "css_class": " ".join(css_classes),
            "always_open": kwargs.always_open,
            "attrs": kwargs.attrs,
        }
        data["div_attrs"] = merge_attrs(
            {"id": data["accordion_id"]}, (data["attrs"] or {}), {"class": data["css_class"]}
        )
        return data

    template = """
        <c-provide key="accordion" c-accordion_id="accordion_id" c-always_open="always_open">
        <div c-bind="div_attrs">
        <c-slot />
        </div>
        </c-provide>
    """


class AccordionItem(LibraryComponent):
    name = "bs-accordion-item"

    class Kwargs:
        default_open: bool = False
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        accordion = self.inject("accordion")

        item_id = (kwargs.attrs or {}).get("id") or f"accordion-item-{self.id}"
        heading_id = f"{item_id}-heading"
        collapse_id = f"{item_id}-collapse"
        data_bs_parent = f"#{accordion.accordion_id}"

        data = {
            "heading_id": heading_id,
            "collapse_id": collapse_id,
            "is_open": kwargs.default_open,
            "data_bs_parent": data_bs_parent,
            "always_open": accordion.always_open,
            "attrs": kwargs.attrs,
        }
        data["div_attrs"] = merge_attrs((data["attrs"] or {}), {"class": "accordion-item"})
        return data

    template = """
        <c-provide key="accordion_item" c-heading_id="heading_id" c-collapse_id="collapse_id" c-is_open="is_open" c-data_bs_parent="data_bs_parent" c-always_open="always_open">
        <div c-bind="div_attrs">
        <c-slot />
        </div>
        </c-provide>
    """


class AccordionButton(LibraryComponent):
    name = "bs-accordion-button"

    class Kwargs:
        disabled: bool = False
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        accordion_item = self.inject("accordion_item")

        classes = ["accordion-button"]
        if not accordion_item.is_open:
            classes.append("collapsed")

        data = {
            "button_classes": " ".join(classes),
            "collapse_id": accordion_item.collapse_id,
            "aria_expanded": "true" if accordion_item.is_open else "false",
            "disabled": kwargs.disabled,
            "attrs": kwargs.attrs,
        }
        data["button_attrs"] = merge_attrs(
            {
                "aria-expanded": data["aria_expanded"],
                "aria-controls": data["collapse_id"],
                "disabled": data["disabled"],
            },
            (data["attrs"] or {}),
            {
                "class": data["button_classes"],
                "type": "button",
                "data-bs-toggle": "collapse",
                "data-bs-target": f"#{data['collapse_id']}",
            },
        )
        return data

    template = """
        <button c-bind="button_attrs">
        <c-slot />
        </button>
    """


class AccordionHeader(LibraryComponent):
    name = "bs-accordion-header"

    class Kwargs:
        disabled: bool = False
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        accordion_item = self.inject("accordion_item")

        data = {
            "heading_id": accordion_item.heading_id,
            "disabled": kwargs.disabled,
            "attrs": kwargs.attrs,
        }
        data["h2_attrs"] = merge_attrs(
            {"id": data["heading_id"]}, (data["attrs"] or {}), {"class": "accordion-header"}
        )
        return data

    template = """
        <h2 c-bind="h2_attrs">
        <c-bs-accordion-button c-disabled="disabled">
        <c-slot />
        </c-bs-accordion-button>
        </h2>
    """


class AccordionBody(LibraryComponent):
    name = "bs-accordion-body"

    class Kwargs:
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        accordion_item = self.inject("accordion_item")

        collapse_classes = ["accordion-collapse", "collapse"]
        if accordion_item.is_open:
            collapse_classes.append("show")

        data = {
            "heading_id": accordion_item.heading_id,
            "collapse_id": accordion_item.collapse_id,
            "collapse_classes": " ".join(collapse_classes),
            "data_bs_parent": accordion_item.data_bs_parent,
            "always_open": accordion_item.always_open,
            "attrs": kwargs.attrs,
        }
        data["div_attrs"] = merge_attrs(
            {"aria-labelledby": data["heading_id"]},
            {"id": data["collapse_id"], "class": data["collapse_classes"]},
            ({"data-bs-parent": data["data_bs_parent"]} if (not data["always_open"]) else {}),
        )
        data["div_attrs2"] = merge_attrs((data["attrs"] or {}), {"class": "accordion-body"})
        return data

    template = """
        <div c-bind="div_attrs" >
        <div c-bind="div_attrs2">
        <c-slot />
        </div>
        </div>
    """
