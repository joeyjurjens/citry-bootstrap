"""The base class every Bootstrap component is built on."""

import dataclasses

from citry import LibraryComponent, const_value, is_const

_PATCHED = "_citry_bootstrap_unwraps"


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
        if declared is None or _PATCHED in declared.__dict__:
            return
        _refuse_what_cannot_be_unwrapped(cls, declared)
        declared.__post_init__ = _unwrapping(getattr(declared, "__post_init__", None))
        declared.__post_init__.__name__ = "__post_init__"
        setattr(declared, _PATCHED, True)


def _refuse_what_cannot_be_unwrapped(cls: type, declared: type) -> None:
    """A form that builds itself cannot be given a `__post_init__` after the fact.

    Silence here would be a component rendering `container-True`, so say it at
    import time instead. Citry itself cannot render a Pydantic `Kwargs` from a
    template either: the proxy fails its validators.
    """
    if dataclasses.is_dataclass(declared):
        reason = "is already a dataclass, so it will not call a __post_init__ added later"
    elif issubclass(declared, tuple):
        reason = "is a NamedTuple, whose fields cannot be rewritten"
    elif "__init__" in declared.__dict__ or "__new__" in declared.__dict__:
        reason = "builds itself, so citry's constant markers would survive into it"
    else:
        return
    msg = (
        f"{cls.__name__}.Kwargs {reason}. Declare a plain class, which citry turns "
        f"into a slotted dataclass, or unwrap the inputs yourself with const_value()."
    )
    raise TypeError(msg)


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
