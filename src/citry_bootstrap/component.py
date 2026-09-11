"""The base class every Bootstrap component is built on."""

from citry import LibraryComponent, const_value, is_const


class BootstrapComponent(LibraryComponent):
    """A library component whose inputs are ordinary Python values.

    Citry marks a value it knows at parse time with a transparent proxy, so it
    can precompute the template expressions that read it. The proxy compares and
    prints like the value it wraps, but `re`, `str.join` and `os.fspath` reject
    it and `x is True` is False. Component code is ordinary Python, so the typed
    input view is unwrapped once, here, for every component in the library.

    Only that typed view changes. `raw_kwargs` keeps its markers, so citry's own
    bookkeeping is untouched and nothing outside this library is affected. An
    engine extension cannot be scoped this way: its only input hook mutates the
    authoritative mapping, for every component in the application.

    Citry issue #124 tracks handing component code plain values from the engine.
    This class goes away when it does.
    """

    def __init_subclass__(cls, **kwargs) -> None:
        super().__init_subclass__(**kwargs)
        declared = cls.__dict__.get("Kwargs")
        if declared is not None:
            declared.__post_init__ = _unwrapping(getattr(declared, "__post_init__", None))


def _unwrapping(previous):
    """Citry builds the typed inputs as a slotted dataclass, so it runs this."""

    def __post_init__(self) -> None:
        for klass in type(self).__mro__:
            for name in getattr(klass, "__slots__", ()):
                value = getattr(self, name)
                if is_const(value):
                    setattr(self, name, const_value(value))
        if previous is not None:
            previous(self)

    return __post_init__
