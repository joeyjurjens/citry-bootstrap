from types import SimpleNamespace

from citry import LibraryComponent, SlotInput, const_value, merge_attrs

from citry_bootstrap.components.bootstrap5.types import Size


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


class InputGroup(LibraryComponent):
    name = "bs-input-group"

    class Kwargs:
        size: Size | None = None
        nowrap: bool = False
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        kwargs = _plain(kwargs)
        classes = ["input-group"]
        if kwargs.size:
            classes.append(f"input-group-{kwargs.size}")
        if kwargs.nowrap:
            classes.append("flex-nowrap")

        data = {
            "classes": " ".join(classes),
            "attrs": kwargs.attrs,
        }
        data["div_attrs"] = merge_attrs((data["attrs"] or {}), {"class": data["classes"]})
        return data

    template = """
        <div c-bind="div_attrs">
        <c-slot />
        </div>
    """


class InputGroupText(LibraryComponent):
    name = "bs-input-group-text"

    class Kwargs:
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        kwargs = _plain(kwargs)
        data = {
            "attrs": kwargs.attrs,
        }
        data["span_attrs"] = merge_attrs((data["attrs"] or {}), {"class": "input-group-text"})
        return data

    template = """
        <span c-bind="span_attrs">
        <c-slot />
        </span>
    """


class InputGroupRadio(LibraryComponent):
    name = "bs-input-group-radio"

    class Kwargs:
        attrs: dict | None = None

    def template_data(self, kwargs: Kwargs, slots):
        kwargs = _plain(kwargs)
        data = {
            "attrs": kwargs.attrs,
        }
        data["input_attrs"] = merge_attrs(
            (data["attrs"] or {}), {"type": "radio", "class": "form-check-input mt-0"}
        )
        return data

    template = """
        <div class="input-group-text">
        <input c-bind="input_attrs" />
        </div>
    """


class InputGroupCheckbox(LibraryComponent):
    name = "bs-input-group-checkbox"

    class Kwargs:
        attrs: dict | None = None

    def template_data(self, kwargs: Kwargs, slots):
        kwargs = _plain(kwargs)
        data = {
            "attrs": kwargs.attrs,
        }
        data["input_attrs"] = merge_attrs(
            (data["attrs"] or {}), {"type": "checkbox", "class": "form-check-input mt-0"}
        )
        return data

    template = """
        <div class="input-group-text">
        <input c-bind="input_attrs" />
        </div>
    """


class FloatingLabel(LibraryComponent):
    name = "bs-floating-label"

    class Kwargs:
        label: str
        control_id: str | None = None
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def template_data(self, kwargs: Kwargs, slots: Slots):
        kwargs = _plain(kwargs)
        data = {
            "control_id": kwargs.control_id,
            "label": kwargs.label,
            "attrs": kwargs.attrs,
        }
        data["div_attrs"] = merge_attrs((data["attrs"] or {}), {"class": "form-floating"})
        data["label_attrs"] = {"for": data["control_id"]} if data["control_id"] else {}
        return data

    template = """
        <c-provide key="formgroup" c-control_id="control_id">
        <div c-bind="div_attrs">
        <c-slot />
        <label c-bind="label_attrs">{{ label }}</label>
        </div>
        </c-provide>
    """
