import pytest
from citry import Citry

import citry_bootstrap
from citry_bootstrap.components.bootstrap5.card import CardBody


def engine(**kwargs):
    app = Citry(autodiscover=False, extensions=[citry_bootstrap.PlainInputs])
    citry_bootstrap.install(app, **kwargs)
    return app


def test_components_are_published_under_the_default_prefix():
    assert "<div" in engine().render_template("<c-bs-card>x</c-bs-card>").serialize()


def test_a_component_finds_its_siblings():
    """`Card` renders the card body by name, so the two have to agree."""
    out = engine().render_template('<c-bs-card c-body="True">x</c-bs-card>').serialize()
    assert 'class="card-body"' in out


def test_the_prefix_can_be_changed():
    app = engine(prefix="ui-")
    assert (
        'class="card-body"'
        in app.render_template('<c-ui-card c-body="True">x</c-ui-card>').serialize()
    )


def test_changing_the_prefix_replaces_the_old_names():
    assert [n for n in engine(prefix="ui-").components if "card-body" in n] == ["ui-card-body"]


def test_the_prefix_can_be_dropped():
    assert "<div" in engine(prefix="").render_template("<c-card>x</c-card>").serialize()


def test_a_component_can_be_replaced():
    """Every sibling renders the replacement, not the original."""

    class MyCardBody(CardBody):
        def template_data(self, kwargs, slots):
            data = super().template_data(kwargs, slots)
            data["div_attrs"] = {**data["div_attrs"], "data-mine": "yes"}
            return data

    app = engine(override={CardBody: MyCardBody})
    out = app.render_template('<c-bs-card c-body="True">x</c-bs-card>').serialize()
    assert "data-mine" in out


def test_a_replacement_follows_the_prefix():
    class MyCardBody(CardBody):
        pass

    app = engine(prefix="ui-", override={CardBody: MyCardBody})
    assert "ui-card-body" in app.components


def test_replacing_something_from_another_library_is_refused():
    class Stranger:
        name = "stranger"

    with pytest.raises(ValueError, match="not part of this library"):
        engine(override={Stranger: Stranger})


def test_the_default_install_reuses_the_shipped_manifest():
    assert citry_bootstrap.library() is citry_bootstrap.__citry_library__


CAROUSEL = (
    '<c-{p}carousel><c-{p}carousel-item c-active="True">x</c-{p}carousel-item></c-{p}carousel>'
)


def test_a_component_reached_from_python_follows_the_prefix():
    """`Carousel` builds its renderer in `on_render`, not in its template."""
    app = engine(prefix="ui-")
    assert "carousel-inner" in app.render_template(CAROUSEL.format(p="ui-")).serialize()


def test_a_component_reached_from_python_can_be_replaced():
    from citry_bootstrap.components.bootstrap5.carousel import CarouselRenderer

    class MyRenderer(CarouselRenderer):
        def template_data(self, kwargs, slots):
            data = super().template_data(kwargs, slots)
            data["div_attrs"] = {**data["div_attrs"], "data-mine": "yes"}
            return data

    app = engine(prefix="ui-", override={CarouselRenderer: MyRenderer})
    assert "data-mine" in app.render_template(CAROUSEL.format(p="ui-")).serialize()
