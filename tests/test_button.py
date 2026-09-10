def test_variant_primary(render, assert_html):
    rendered = render("""
<c-bs-button variant="primary">Primary</c-bs-button>
""")

    expected = """
        <button type="button" class="btn btn-primary">Primary</button>
    """

    assert_html(rendered, expected)


def test_variant_secondary(render, assert_html):
    rendered = render("""
<c-bs-button variant="secondary">Secondary</c-bs-button>
""")

    expected = """
        <button type="button" class="btn btn-secondary">Secondary</button>
    """

    assert_html(rendered, expected)


def test_variant_success(render, assert_html):
    rendered = render("""
<c-bs-button variant="success">Success</c-bs-button>
""")

    expected = """
        <button type="button" class="btn btn-success">Success</button>
    """

    assert_html(rendered, expected)


def test_variant_danger(render, assert_html):
    rendered = render("""
<c-bs-button variant="danger">Danger</c-bs-button>
""")

    expected = """
        <button type="button" class="btn btn-danger">Danger</button>
    """

    assert_html(rendered, expected)


def test_variant_warning(render, assert_html):
    rendered = render("""
<c-bs-button variant="warning">Warning</c-bs-button>
""")

    expected = """
        <button type="button" class="btn btn-warning">Warning</button>
    """

    assert_html(rendered, expected)


def test_variant_info(render, assert_html):
    rendered = render("""
<c-bs-button variant="info">Info</c-bs-button>
""")

    expected = """
        <button type="button" class="btn btn-info">Info</button>
    """

    assert_html(rendered, expected)


def test_variant_light(render, assert_html):
    rendered = render("""
<c-bs-button variant="light">Light</c-bs-button>
""")

    expected = """
        <button type="button" class="btn btn-light">Light</button>
    """

    assert_html(rendered, expected)


def test_variant_dark(render, assert_html):
    rendered = render("""
<c-bs-button variant="dark">Dark</c-bs-button>
""")

    expected = """
        <button type="button" class="btn btn-dark">Dark</button>
    """

    assert_html(rendered, expected)


def test_variant_link(render, assert_html):
    rendered = render("""
<c-bs-button variant="link">Link</c-bs-button>
""")

    expected = """
        <button type="button" class="btn btn-link">Link</button>
    """

    assert_html(rendered, expected)


def test_outline_primary(render, assert_html):
    rendered = render("""
<c-bs-button variant="primary" c-outline="True">Primary</c-bs-button>
""")

    expected = """
        <button type="button" class="btn btn-outline-primary">Primary</button>
    """

    assert_html(rendered, expected)


def test_outline_secondary(render, assert_html):
    rendered = render("""
<c-bs-button variant="secondary" c-outline="True">Secondary</c-bs-button>
""")

    expected = """
        <button type="button" class="btn btn-outline-secondary">Secondary</button>
    """

    assert_html(rendered, expected)


def test_size_large(render, assert_html):
    rendered = render("""
<c-bs-button variant="primary" size="lg">Large button</c-bs-button>
""")

    expected = """
        <button type="button" class="btn btn-primary btn-lg">Large button</button>
    """

    assert_html(rendered, expected)


def test_size_small(render, assert_html):
    rendered = render("""
<c-bs-button variant="primary" size="sm">Small button</c-bs-button>
""")

    expected = """
        <button type="button" class="btn btn-primary btn-sm">Small button</button>
    """

    assert_html(rendered, expected)


def test_disabled(render, assert_html):
    rendered = render("""
<c-bs-button variant="primary" c-disabled="True">Disabled button</c-bs-button>
""")

    expected = """
        <button type="button" class="btn btn-primary" disabled>Disabled button</button>
    """

    assert_html(rendered, expected)


def test_link_button(render, assert_html):
    rendered = render("""
<c-bs-button variant="primary" as_="a" href="#">Link</c-bs-button>
""")

    expected = """
        <a class="btn btn-primary" href="#" role="button">Link</a>
    """

    assert_html(rendered, expected)


def test_link_button_disabled(render, assert_html):
    rendered = render("""
<c-bs-button variant="primary" as_="a" href="#" c-disabled="True">Disabled link</c-bs-button>
""")

    expected = """
        <a class="btn btn-primary disabled" href="#" aria-disabled="true" tabindex="-1" role="button">Disabled link</a>
    """

    assert_html(rendered, expected)


def test_active_state(render, assert_html):
    rendered = render("""
<c-bs-button variant="primary" c-active="True">Active button</c-bs-button>
""")

    expected = """
        <button type="button" class="btn btn-primary active" aria-pressed="true">Active button</button>
    """

    assert_html(rendered, expected)
