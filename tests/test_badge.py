def test_basic(render, assert_html):
    rendered = render("""
<h1>
  Example heading
  <c-bs-badge bg="secondary">New</c-bs-badge>
</h1>
""")

    expected = """
        <h1>Example heading <span class="badge text-bg-secondary">New</span></h1>
    """

    assert_html(rendered, expected)


def test_in_button(render, assert_html):
    rendered = render("""
<c-bs-button>
  Notifications
  <c-bs-badge bg="secondary">4</c-bs-badge>
</c-bs-button>
""")

    expected = """
        <button type="button" class="btn btn-primary">
          Notifications <span class="badge text-bg-secondary">4</span>
        </button>
    """

    assert_html(rendered, expected)


def test_pill(render, assert_html):
    rendered = render("""
<c-bs-badge bg="primary" c-pill="True">Primary</c-bs-badge>
""")

    expected = """
        <span class="badge rounded-pill text-bg-primary">Primary</span>
    """

    assert_html(rendered, expected)


def test_bg_primary(render, assert_html):
    rendered = render("""
<c-bs-badge bg="primary">Primary</c-bs-badge>
""")

    expected = """
        <span class="badge text-bg-primary">Primary</span>
    """

    assert_html(rendered, expected)


def test_bg_secondary(render, assert_html):
    rendered = render("""
<c-bs-badge bg="secondary">Secondary</c-bs-badge>
""")

    expected = """
        <span class="badge text-bg-secondary">Secondary</span>
    """

    assert_html(rendered, expected)


def test_bg_success(render, assert_html):
    rendered = render("""
<c-bs-badge bg="success">Success</c-bs-badge>
""")

    expected = """
        <span class="badge text-bg-success">Success</span>
    """

    assert_html(rendered, expected)


def test_bg_danger(render, assert_html):
    rendered = render("""
<c-bs-badge bg="danger">Danger</c-bs-badge>
""")

    expected = """
        <span class="badge text-bg-danger">Danger</span>
    """

    assert_html(rendered, expected)


def test_bg_warning(render, assert_html):
    rendered = render("""
<c-bs-badge bg="warning">Warning</c-bs-badge>
""")

    expected = """
        <span class="badge text-bg-warning">Warning</span>
    """

    assert_html(rendered, expected)


def test_bg_info(render, assert_html):
    rendered = render("""
<c-bs-badge bg="info">Info</c-bs-badge>
""")

    expected = """
        <span class="badge text-bg-info">Info</span>
    """

    assert_html(rendered, expected)


def test_bg_light(render, assert_html):
    rendered = render("""
<c-bs-badge bg="light">Light</c-bs-badge>
""")

    expected = """
        <span class="badge text-bg-light">Light</span>
    """

    assert_html(rendered, expected)


def test_bg_dark(render, assert_html):
    rendered = render("""
<c-bs-badge bg="dark">Dark</c-bs-badge>
""")

    expected = """
        <span class="badge text-bg-dark">Dark</span>
    """

    assert_html(rendered, expected)


def test_pill_primary(render, assert_html):
    rendered = render("""
<c-bs-badge bg="primary" c-pill="True">Primary</c-bs-badge>
""")

    expected = """
        <span class="badge rounded-pill text-bg-primary">Primary</span>
    """

    assert_html(rendered, expected)


def test_pill_secondary(render, assert_html):
    rendered = render("""
<c-bs-badge bg="secondary" c-pill="True">Secondary</c-bs-badge>
""")

    expected = """
        <span class="badge rounded-pill text-bg-secondary">Secondary</span>
    """

    assert_html(rendered, expected)


def test_pill_success(render, assert_html):
    rendered = render("""
<c-bs-badge bg="success" c-pill="True">Success</c-bs-badge>
""")

    expected = """
        <span class="badge rounded-pill text-bg-success">Success</span>
    """

    assert_html(rendered, expected)


def test_pill_danger(render, assert_html):
    rendered = render("""
<c-bs-badge bg="danger" c-pill="True">Danger</c-bs-badge>
""")

    expected = """
        <span class="badge rounded-pill text-bg-danger">Danger</span>
    """

    assert_html(rendered, expected)


def test_pill_warning(render, assert_html):
    rendered = render("""
<c-bs-badge bg="warning" c-pill="True">Warning</c-bs-badge>
""")

    expected = """
        <span class="badge rounded-pill text-bg-warning">Warning</span>
    """

    assert_html(rendered, expected)


def test_pill_info(render, assert_html):
    rendered = render("""
<c-bs-badge bg="info" c-pill="True">Info</c-bs-badge>
""")

    expected = """
        <span class="badge rounded-pill text-bg-info">Info</span>
    """

    assert_html(rendered, expected)


def test_pill_light(render, assert_html):
    rendered = render("""
<c-bs-badge bg="light" c-pill="True">Light</c-bs-badge>
""")

    expected = """
        <span class="badge rounded-pill text-bg-light">Light</span>
    """

    assert_html(rendered, expected)


def test_pill_dark(render, assert_html):
    rendered = render("""
<c-bs-badge bg="dark" c-pill="True">Dark</c-bs-badge>
""")

    expected = """
        <span class="badge rounded-pill text-bg-dark">Dark</span>
    """

    assert_html(rendered, expected)
