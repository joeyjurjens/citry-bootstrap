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


def pair():
    """The same component on two engines, one with the extension and one without."""
    engines = []
    for extensions in ([], [citry_bootstrap.PlainInputs]):
        app = Citry(autodiscover=False, extensions=extensions)

        class Child(LibraryComponent):
            name = "child"

            class Kwargs:
                x: object = None
                y: object = None

            def template_data(self, kwargs, slots):
                return {"x": kwargs.x, "y": kwargs.y, "both": [kwargs.x, kwargs.y]}

            template = '<i c-data-x="x" c-data-y="y">{{ both }}</i>'

        class Parent(LibraryComponent):
            name = "parent"

            class Kwargs:
                x: object = None
                y: object = None

            def template_data(self, kwargs, slots):
                return {"x": kwargs.x, "y": kwargs.y, "flip": kwargs.y}

            template = '<div c-data-x="x"><c-child c-x="x" c-y="flip" /></div>'

        app.register_library(ComponentLibrary(name="pair", components=[Parent, Child]))
        engines.append(app)
    return engines


VALUES = ["'a'", "'b-c'", "True", "False", "None", "3", "[1, 2]", "''"]
_CID = re.compile(r'\s*data-cid-[\w-]+="[^"]*"')


def test_the_output_is_what_citry_would_have_rendered():
    """Whatever the extension does to the values, the html may not move."""
    import random

    stock, plain = pair()
    random.seed(11)
    for _ in range(300):
        x, y = random.choice(VALUES), random.choice(VALUES)
        live = random.choice([True, False])
        source = f'<c-{random.choice(["parent", "child"])} c-x="{x}" c-y="{"v" if live else y}" />'
        variables = {"v": eval(y)}  # noqa: S307 - the test's own literals
        assert _CID.sub("", stock.render_template(source, variables).serialize()) == _CID.sub(
            "", plain.render_template(source, variables).serialize()
        )


def test_two_renders_of_one_component_do_not_share_state():
    """The marks are per render; a second render must not see the first's."""
    _, plain = pair()
    first = plain.render_template('<c-child c-x="True" c-y="v" />', {"v": 1}).serialize()
    second = plain.render_template('<c-child c-x="True" c-y="v" />', {"v": 2}).serialize()
    assert 'data-y="1"' in first
    assert 'data-y="2"' in second


def test_renders_in_parallel_do_not_cross(probe):
    """State lives on the component instance, so threads cannot see each other's."""
    from concurrent.futures import ThreadPoolExecutor

    probe.render_template('<c-probe c-flag="True" text="warm" />').serialize()

    def render(n):
        return probe.render_template(f'<c-probe c-flag="True" text="t{n}" />').serialize()

    with ThreadPoolExecutor(max_workers=16) as pool:
        out = list(pool.map(render, range(300)))
    assert [n for n, html in enumerate(out) if f">t{n}<" not in html] == []


def test_a_component_that_renders_itself(probe):
    app = Citry(autodiscover=False, extensions=[citry_bootstrap.PlainInputs])

    class Deep(LibraryComponent):
        name = "deep"

        class Kwargs:
            left: object = None
            label: object = None

        def template_data(self, kwargs, slots):
            assert not is_const(kwargs.label)
            return {"left": kwargs.left, "inner": kwargs.left > 0, "label": kwargs.label}

        template = (
            '<div c-data-label="label"><c-deep c-if="inner" c-left="left - 1" label="x" /></div>'
        )

    app.register_library(ComponentLibrary(name="deep", components=[Deep]))
    html = app.render_template('<c-deep c-left="40" label="x" />').serialize()
    assert html.count("data-label") == 41


@pytest.mark.parametrize(
    ("template_data", "source"),
    [
        (lambda self, kwargs, slots: None, '<c-edge c-a="True" />'),
        (lambda self, kwargs, slots: {"a": kwargs.a}, "<c-edge />"),
    ],
)
def test_a_component_with_nothing_to_mark(template_data, source):
    """No inputs, or no data returned, must not reach into an empty mapping."""
    app = Citry(autodiscover=False, extensions=[citry_bootstrap.PlainInputs])
    edge = type(
        "Edge",
        (LibraryComponent,),
        {
            "name": "edge",
            "Kwargs": type("Kwargs", (), {"__annotations__": {"a": object}, "a": None}),
            "template_data": template_data,
            "template": "<i>x</i>",
        },
    )
    app.register_library(ComponentLibrary(name="edge", components=[edge]))
    assert "<i" in app.render_template(source).serialize()
