def test_border(render, assert_html):
    rendered = render("""
<c-bs-spinner animation="border" />
""")

    expected = """
        <div class="spinner-border" role="status">
          <span class="visually-hidden">Loading...</span>
        </div>
    """

    assert_html(rendered, expected)


def test_grow(render, assert_html):
    rendered = render("""
<c-bs-spinner animation="grow" />
""")

    expected = """
        <div class="spinner-grow" role="status">
          <span class="visually-hidden">Loading...</span>
        </div>
    """

    assert_html(rendered, expected)


def test_border_primary(render, assert_html):
    rendered = render("""
<c-bs-spinner animation="border" variant="primary" />
""")

    expected = """
        <div class="spinner-border text-primary" role="status">
          <span class="visually-hidden">Loading...</span>
        </div>
    """

    assert_html(rendered, expected)


def test_border_secondary(render, assert_html):
    rendered = render("""
<c-bs-spinner animation="border" variant="secondary" />
""")

    expected = """
        <div class="spinner-border text-secondary" role="status">
          <span class="visually-hidden">Loading...</span>
        </div>
    """

    assert_html(rendered, expected)


def test_border_success(render, assert_html):
    rendered = render("""
<c-bs-spinner animation="border" variant="success" />
""")

    expected = """
        <div class="spinner-border text-success" role="status">
          <span class="visually-hidden">Loading...</span>
        </div>
    """

    assert_html(rendered, expected)


def test_border_danger(render, assert_html):
    rendered = render("""
<c-bs-spinner animation="border" variant="danger" />
""")

    expected = """
        <div class="spinner-border text-danger" role="status">
          <span class="visually-hidden">Loading...</span>
        </div>
    """

    assert_html(rendered, expected)


def test_border_warning(render, assert_html):
    rendered = render("""
<c-bs-spinner animation="border" variant="warning" />
""")

    expected = """
        <div class="spinner-border text-warning" role="status">
          <span class="visually-hidden">Loading...</span>
        </div>
    """

    assert_html(rendered, expected)


def test_border_info(render, assert_html):
    rendered = render("""
<c-bs-spinner animation="border" variant="info" />
""")

    expected = """
        <div class="spinner-border text-info" role="status">
          <span class="visually-hidden">Loading...</span>
        </div>
    """

    assert_html(rendered, expected)


def test_border_light(render, assert_html):
    rendered = render("""
<c-bs-spinner animation="border" variant="light" />
""")

    expected = """
        <div class="spinner-border text-light" role="status">
          <span class="visually-hidden">Loading...</span>
        </div>
    """

    assert_html(rendered, expected)


def test_border_dark(render, assert_html):
    rendered = render("""
<c-bs-spinner animation="border" variant="dark" />
""")

    expected = """
        <div class="spinner-border text-dark" role="status">
          <span class="visually-hidden">Loading...</span>
        </div>
    """

    assert_html(rendered, expected)


def test_grow_primary(render, assert_html):
    rendered = render("""
<c-bs-spinner animation="grow" variant="primary" />
""")

    expected = """
        <div class="spinner-grow text-primary" role="status">
          <span class="visually-hidden">Loading...</span>
        </div>
    """

    assert_html(rendered, expected)


def test_grow_secondary(render, assert_html):
    rendered = render("""
<c-bs-spinner animation="grow" variant="secondary" />
""")

    expected = """
        <div class="spinner-grow text-secondary" role="status">
          <span class="visually-hidden">Loading...</span>
        </div>
    """

    assert_html(rendered, expected)


def test_grow_success(render, assert_html):
    rendered = render("""
<c-bs-spinner animation="grow" variant="success" />
""")

    expected = """
        <div class="spinner-grow text-success" role="status">
          <span class="visually-hidden">Loading...</span>
        </div>
    """

    assert_html(rendered, expected)


def test_grow_danger(render, assert_html):
    rendered = render("""
<c-bs-spinner animation="grow" variant="danger" />
""")

    expected = """
        <div class="spinner-grow text-danger" role="status">
          <span class="visually-hidden">Loading...</span>
        </div>
    """

    assert_html(rendered, expected)


def test_grow_warning(render, assert_html):
    rendered = render("""
<c-bs-spinner animation="grow" variant="warning" />
""")

    expected = """
        <div class="spinner-grow text-warning" role="status">
          <span class="visually-hidden">Loading...</span>
        </div>
    """

    assert_html(rendered, expected)


def test_grow_info(render, assert_html):
    rendered = render("""
<c-bs-spinner animation="grow" variant="info" />
""")

    expected = """
        <div class="spinner-grow text-info" role="status">
          <span class="visually-hidden">Loading...</span>
        </div>
    """

    assert_html(rendered, expected)


def test_grow_light(render, assert_html):
    rendered = render("""
<c-bs-spinner animation="grow" variant="light" />
""")

    expected = """
        <div class="spinner-grow text-light" role="status">
          <span class="visually-hidden">Loading...</span>
        </div>
    """

    assert_html(rendered, expected)


def test_grow_dark(render, assert_html):
    rendered = render("""
<c-bs-spinner animation="grow" variant="dark" />
""")

    expected = """
        <div class="spinner-grow text-dark" role="status">
          <span class="visually-hidden">Loading...</span>
        </div>
    """

    assert_html(rendered, expected)


def test_border_small(render, assert_html):
    rendered = render("""
<c-bs-spinner animation="border" size="sm" />
""")

    expected = """
        <div class="spinner-border spinner-border-sm" role="status">
          <span class="visually-hidden">Loading...</span>
        </div>
    """

    assert_html(rendered, expected)


def test_grow_small(render, assert_html):
    rendered = render("""
<c-bs-spinner animation="grow" size="sm" />
""")

    expected = """
        <div class="spinner-grow spinner-grow-sm" role="status">
          <span class="visually-hidden">Loading...</span>
        </div>
    """

    assert_html(rendered, expected)


def test_custom_label(render, assert_html):
    rendered = render("""
<c-bs-spinner animation="border" label="Please wait..." />
""")

    expected = """
        <div class="spinner-border" role="status">
          <span class="visually-hidden">Please wait...</span>
        </div>
    """

    assert_html(rendered, expected)


def test_custom_attrs(render, assert_html):
    rendered = render("""
<c-bs-spinner animation="border" c-attrs="{'class': 'custom-class'}" />
""")

    expected = """
        <div class="spinner-border custom-class" role="status">
          <span class="visually-hidden">Loading...</span>
        </div>
    """

    assert_html(rendered, expected)


def test_with_margin(render, assert_html):
    rendered = render("""
<c-bs-spinner animation="border" />
""")

    expected = """
        <div class="spinner-border" role="status">
          <span class="visually-hidden">Loading...</span>
        </div>
    """

    assert_html(rendered, expected)


def test_custom_size_style(render, assert_html):
    rendered = render("""
<c-bs-spinner animation="border" />
""")

    expected = """
        <div class="spinner-border" role="status">
          <span class="visually-hidden">Loading...</span>
        </div>
    """

    assert_html(rendered, expected)
