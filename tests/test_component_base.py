"""The base class hands component code plain values; prove the mechanism.

Citry marks a parse-time constant with a transparent proxy. If citry ever stops
running `__post_init__` on the typed inputs, these fail rather than silently
rendering `container-True`.
"""

import dataclasses
import re
from typing import NamedTuple

import pytest
from citry import Citry, ComponentLibrary, is_const

import citry_bootstrap
from citry_bootstrap.component import BootstrapComponent


@pytest.fixture
def seen():
    return {}


@pytest.fixture
def probe(seen):
    class Probe(BootstrapComponent):
        name = "probe"

        class Kwargs:
            flag: object = None
            text: str = ""

        def template_data(self, kwargs, slots):
            seen["flag"] = kwargs.flag
            seen["text"] = kwargs.text
            seen["raw"] = self.raw_kwargs.get("flag")
            return {}

        template = "<div></div>"

    app = Citry(autodiscover=False)
    app.register_library(ComponentLibrary(name="probe", components=[Probe]))
    return app


def test_a_constant_input_arrives_unwrapped(probe, seen):
    probe.render_template('<c-probe c-flag="True" text="a-b" />').serialize()
    assert seen["flag"] is True
    assert re.fullmatch(r"[a-z-]+", seen["text"])


def test_citry_keeps_its_own_marker(probe, seen):
    """Unwrapping the typed view must not cost citry the information."""
    probe.render_template('<c-probe c-flag="True" />').serialize()
    assert is_const(seen["raw"])


def test_a_plain_call_is_unaffected(probe, seen):
    probe.render_template("<c-probe c-flag='x' />", {"x": True}).serialize()
    assert seen["flag"] is True
    assert not is_const(seen["raw"])


@pytest.mark.parametrize(
    ("source", "fragment"),
    [
        ('<c-bs-container c-fluid="True">x</c-bs-container>', 'class="container-fluid"'),
        ('<c-bs-table c-responsive="True"><tbody></tbody></c-bs-table>', "table-responsive"),
        ('<c-bs-tabs><c-bs-tab title="Home Page">x</c-bs-tab></c-bs-tabs>', "home-page"),
    ],
)
def test_the_library_renders_constant_inputs_correctly(source, fragment):
    """`is True` in one, `re` in the other: the two ways the proxy shows up."""
    app = Citry(autodiscover=False)
    citry_bootstrap.install(app)
    assert fragment in app.render_template(source).serialize()


@pytest.mark.parametrize(
    ("declare", "reason"),
    [
        (
            lambda: dataclasses.dataclass(type("Kwargs", (), {"__annotations__": {"a": int}})),
            "dataclass",
        ),
        (lambda: NamedTuple("Kwargs", [("a", int)]), "NamedTuple"),
    ],
)
def test_a_kwargs_form_that_cannot_be_unwrapped_is_refused(declare, reason):
    """Silence here renders `container-True`; say it at import time instead."""
    with pytest.raises(TypeError, match=reason):
        type("Refused", (BootstrapComponent,), {"name": "refused", "Kwargs": declare()})


def test_a_kwargs_class_shared_by_two_components_is_patched_once():
    """Two components may name the same class; wrapping it twice would nest."""
    shared = type("Kwargs", (), {"__annotations__": {"a": int}, "a": 0})
    type("One", (BootstrapComponent,), {"name": "one", "Kwargs": shared})
    first = shared.__post_init__
    type("Two", (BootstrapComponent,), {"name": "two", "Kwargs": shared})
    assert shared.__post_init__ is first
