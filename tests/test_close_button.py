def test_basic(render, assert_html):
    rendered = render("""
<c-bs-close-button />
""")

    expected = """
        <button type="button" class="btn-close" aria-label="Close"></button>
    """

    assert_html(rendered, expected)


def test_disabled(render, assert_html):
    rendered = render("""
<c-bs-close-button c-disabled="True" />
""")

    expected = """
        <button type="button" class="btn-close" disabled aria-label="Close"></button>
    """

    assert_html(rendered, expected)


def test_white_variant(render, assert_html):
    rendered = render("""
<c-bs-close-button variant="white" />
""")

    expected = """
        <button type="button" class="btn-close btn-close-white" aria-label="Close"></button>
    """

    assert_html(rendered, expected)


def test_white_variant_disabled(render, assert_html):
    rendered = render("""
<c-bs-close-button variant="white" c-disabled="True" />
""")

    expected = """
        <button type="button" class="btn-close btn-close-white" disabled aria-label="Close"></button>
    """

    assert_html(rendered, expected)


def test_custom_aria_label(render, assert_html):
    rendered = render("""
<c-bs-close-button />
""")

    expected = """
        <button type="button" class="btn-close" aria-label="Close"></button>
    """

    assert_html(rendered, expected)


def test_custom_attrs(render, assert_html):
    rendered = render("""
<c-bs-close-button c-attrs="{'class': 'custom-class'}" />
""")

    expected = """
        <button type="button" class="btn-close custom-class" aria-label="Close"></button>
    """

    assert_html(rendered, expected)


def test_data_bs_dismiss(render, assert_html):
    rendered = render("""
<c-bs-close-button c-attrs="{'data-bs-dismiss': 'modal'}" />
""")

    expected = """
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
    """

    assert_html(rendered, expected)


def test_data_bs_dismiss_alert(render, assert_html):
    rendered = render("""
<c-bs-close-button c-attrs="{'data-bs-dismiss': 'alert'}" />
""")

    expected = """
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    """

    assert_html(rendered, expected)
