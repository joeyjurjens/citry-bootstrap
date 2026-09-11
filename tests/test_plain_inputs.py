"""The extension these components are published against.

Citry marks a parse-time constant with a transparent proxy. These components
were translated from django-components, which has no such marker, so they read
their inputs as ordinary Python and need the proxy off first.
"""

import re

import pytest
from citry import Citry, ComponentLibrary, LibraryComponent, is_const

import citry_bootstrap


@pytest.fixture
def seen():
    return {}


@pytest.fixture
def probe(seen):
    class Probe(LibraryComponent):
        name = "probe"

        class Kwargs:
            flag: object = None
            text: str = ""

        def template_data(self, kwargs, slots):
            seen["flag"] = kwargs.flag
            seen["text"] = kwargs.text
            seen["raw"] = self.raw_kwargs.get("flag")
            return {"flag": kwargs.flag, "text": kwargs.text}

        template = '<div c-data-flag="flag">{{ text }}</div>'

    app = Citry(autodiscover=False, extensions=[citry_bootstrap.PlainInputs])
    app.register_library(
        ComponentLibrary(name="probe", components=[Probe], required_extensions=("plain_inputs",))
    )
    return app


@pytest.mark.parametrize("literal", ["True", "None", "'x'"])
def test_a_constant_input_arrives_unwrapped(probe, seen, literal):
    probe.render_template(f'<c-probe c-flag="{literal}" />').serialize()
    assert not is_const(seen["flag"])
    assert seen["flag"] is eval(literal)  # noqa: S307 - the test's own literal


def test_a_constant_string_still_works_with_re(probe, seen):
    probe.render_template('<c-probe text="a-b" />').serialize()
    assert re.fullmatch(r"[a-z-]+", seen["text"])


def test_the_marker_is_gone_from_the_component_s_view(probe, seen):
    """`on_component_input` hands out the authoritative mapping, so raw goes too."""
    probe.render_template('<c-probe c-flag="True" />').serialize()
    assert not is_const(seen["raw"])


def test_citry_sees_the_same_constants_either_way(probe):
    """The re-marking on the way out is what makes this cost nothing."""
    import citry.component_render as render

    original = render.extract_const_vars
    captured = []

    def spy(variables, used_vars=None):
        const_vars, signature = original(variables, used_vars=used_vars)
        captured.append(sorted(const_vars))
        return const_vars, signature

    render.extract_const_vars = spy
    try:
        probe.render_template('<c-probe c-flag="1" />').serialize()
    finally:
        render.extract_const_vars = original
    assert ["flag"] in captured


def test_the_library_will_not_install_without_it():
    """Silence here renders `container-True`, so refuse at registration."""
    with pytest.raises(ValueError, match="plain_inputs"):
        citry_bootstrap.install(Citry(autodiscover=False))


@pytest.mark.parametrize(
    ("source", "fragment"),
    [
        ('<c-bs-container c-fluid="True">x</c-bs-container>', 'class="container-fluid"'),
        ('<c-bs-table c-responsive="True"><tbody></tbody></c-bs-table>', "table-responsive"),
        ('<c-bs-tabs><c-bs-tab title="Home Page">x</c-bs-tab></c-bs-tabs>', "home-page"),
    ],
)
def test_the_library_renders_constant_inputs_correctly(render, source, fragment):
    """`is True` in one, `re` in the other: the two ways the proxy shows up."""
    assert fragment in render(source)
