from citry import LibraryComponent, SlotInput, merge_attrs


class Figure(LibraryComponent):
    name = "bs-figure"

    class Kwargs:
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        data = {
            "attrs": kwargs.attrs,
        }
        data["figure_attrs"] = merge_attrs((data["attrs"] or {}), {"class": "figure"})
        return data

    template = """
        <figure c-bind="figure_attrs">
        <c-slot />
        </figure>
    """


class FigureImage(LibraryComponent):
    name = "bs-figure-image"

    class Kwargs:
        src: str
        alt: str = ""
        fluid: bool = True
        attrs: dict | None = None

    def template_data(self, kwargs: Kwargs, slots):
        classes = ["figure-img"]
        if kwargs.fluid:
            classes.append("img-fluid")

        data = {
            "src": kwargs.src,
            "alt": kwargs.alt,
            "classes": " ".join(classes),
            "attrs": kwargs.attrs,
        }
        data["img_attrs"] = merge_attrs(
            (data["attrs"] or {}),
            {"class": data["classes"], "src": data["src"], "alt": data["alt"]},
        )
        return data

    template = """
        <img c-bind="img_attrs" />
    """


class FigureCaption(LibraryComponent):
    name = "bs-figure-caption"

    class Kwargs:
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        data = {
            "attrs": kwargs.attrs,
        }
        data["figcaption_attrs"] = merge_attrs((data["attrs"] or {}), {"class": "figure-caption"})
        return data

    template = """
        <figcaption c-bind="figcaption_attrs">
        <c-slot />
        </figcaption>
    """
