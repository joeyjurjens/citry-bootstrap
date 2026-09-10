def test_basic(render, assert_html):
    rendered = render("""
<c-bs-dropdown-button title="Dropdown button" variant="secondary">
  <c-bs-dropdown-item href="#">Action</c-bs-dropdown-item>
  <c-bs-dropdown-item href="#">Another action</c-bs-dropdown-item>
  <c-bs-dropdown-item href="#">Something else here</c-bs-dropdown-item>
</c-bs-dropdown-button>
""")

    expected = """
        <div class="dropdown">
          <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
            Dropdown button
          </button>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="#">Action</a></li>
            <li><a class="dropdown-item" href="#">Another action</a></li>
            <li><a class="dropdown-item" href="#">Something else here</a></li>
          </ul>
        </div>
    """

    assert_html(rendered, expected)


def test_variant_primary(render, assert_html):
    rendered = render("""
<c-bs-dropdown-button title="Primary" variant="primary">
  <c-bs-dropdown-item href="#">Action</c-bs-dropdown-item>
  <c-bs-dropdown-item href="#">Another action</c-bs-dropdown-item>
</c-bs-dropdown-button>
""")

    expected = """
        <div class="dropdown">
          <button class="btn btn-primary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
            Primary
          </button>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="#">Action</a></li>
            <li><a class="dropdown-item" href="#">Another action</a></li>
          </ul>
        </div>
    """

    assert_html(rendered, expected)


def test_variant_success(render, assert_html):
    rendered = render("""
<c-bs-dropdown-button title="Success" variant="success">
  <c-bs-dropdown-item href="#">Action</c-bs-dropdown-item>
  <c-bs-dropdown-item href="#">Another action</c-bs-dropdown-item>
</c-bs-dropdown-button>
""")

    expected = """
        <div class="dropdown">
          <button class="btn btn-success dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
            Success
          </button>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="#">Action</a></li>
            <li><a class="dropdown-item" href="#">Another action</a></li>
          </ul>
        </div>
    """

    assert_html(rendered, expected)


def test_variant_danger(render, assert_html):
    rendered = render("""
<c-bs-dropdown-button title="Danger" variant="danger">
  <c-bs-dropdown-item href="#">Action</c-bs-dropdown-item>
  <c-bs-dropdown-item href="#">Another action</c-bs-dropdown-item>
</c-bs-dropdown-button>
""")

    expected = """
        <div class="dropdown">
          <button class="btn btn-danger dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
            Danger
          </button>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="#">Action</a></li>
            <li><a class="dropdown-item" href="#">Another action</a></li>
          </ul>
        </div>
    """

    assert_html(rendered, expected)


def test_variant_warning(render, assert_html):
    rendered = render("""
<c-bs-dropdown-button title="Warning" variant="warning">
  <c-bs-dropdown-item href="#">Action</c-bs-dropdown-item>
  <c-bs-dropdown-item href="#">Another action</c-bs-dropdown-item>
</c-bs-dropdown-button>
""")

    expected = """
        <div class="dropdown">
          <button class="btn btn-warning dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
            Warning
          </button>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="#">Action</a></li>
            <li><a class="dropdown-item" href="#">Another action</a></li>
          </ul>
        </div>
    """

    assert_html(rendered, expected)


def test_variant_info(render, assert_html):
    rendered = render("""
<c-bs-dropdown-button title="Info" variant="info">
  <c-bs-dropdown-item href="#">Action</c-bs-dropdown-item>
  <c-bs-dropdown-item href="#">Another action</c-bs-dropdown-item>
</c-bs-dropdown-button>
""")

    expected = """
        <div class="dropdown">
          <button class="btn btn-info dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
            Info
          </button>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="#">Action</a></li>
            <li><a class="dropdown-item" href="#">Another action</a></li>
          </ul>
        </div>
    """

    assert_html(rendered, expected)


def test_variant_light(render, assert_html):
    rendered = render("""
<c-bs-dropdown-button title="Light" variant="light">
  <c-bs-dropdown-item href="#">Action</c-bs-dropdown-item>
  <c-bs-dropdown-item href="#">Another action</c-bs-dropdown-item>
</c-bs-dropdown-button>
""")

    expected = """
        <div class="dropdown">
          <button class="btn btn-light dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
            Light
          </button>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="#">Action</a></li>
            <li><a class="dropdown-item" href="#">Another action</a></li>
          </ul>
        </div>
    """

    assert_html(rendered, expected)


def test_variant_dark(render, assert_html):
    rendered = render("""
<c-bs-dropdown-button title="Dark" variant="dark">
  <c-bs-dropdown-item href="#">Action</c-bs-dropdown-item>
  <c-bs-dropdown-item href="#">Another action</c-bs-dropdown-item>
</c-bs-dropdown-button>
""")

    expected = """
        <div class="dropdown">
          <button class="btn btn-dark dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
            Dark
          </button>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="#">Action</a></li>
            <li><a class="dropdown-item" href="#">Another action</a></li>
          </ul>
        </div>
    """

    assert_html(rendered, expected)


def test_size_large(render, assert_html):
    rendered = render("""
<c-bs-dropdown-button title="Large button" variant="secondary" size="lg">
  <c-bs-dropdown-item href="#">Action</c-bs-dropdown-item>
  <c-bs-dropdown-item href="#">Another action</c-bs-dropdown-item>
</c-bs-dropdown-button>
""")

    expected = """
        <div class="dropdown">
          <button class="btn btn-secondary dropdown-toggle btn-lg" type="button" data-bs-toggle="dropdown" aria-expanded="false">
            Large button
          </button>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="#">Action</a></li>
            <li><a class="dropdown-item" href="#">Another action</a></li>
          </ul>
        </div>
    """

    assert_html(rendered, expected)


def test_size_small(render, assert_html):
    rendered = render("""
<c-bs-dropdown-button title="Small button" variant="secondary" size="sm">
  <c-bs-dropdown-item href="#">Action</c-bs-dropdown-item>
  <c-bs-dropdown-item href="#">Another action</c-bs-dropdown-item>
</c-bs-dropdown-button>
""")

    expected = """
        <div class="dropdown">
          <button class="btn btn-secondary dropdown-toggle btn-sm" type="button" data-bs-toggle="dropdown" aria-expanded="false">
            Small button
          </button>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="#">Action</a></li>
            <li><a class="dropdown-item" href="#">Another action</a></li>
          </ul>
        </div>
    """

    assert_html(rendered, expected)


def test_dark_menu(render, assert_html):
    rendered = render("""
<c-bs-dropdown-button title="Dropdown" variant="secondary" c-dark="True">
  <c-bs-dropdown-item href="#">Action</c-bs-dropdown-item>
  <c-bs-dropdown-item href="#">Another action</c-bs-dropdown-item>
</c-bs-dropdown-button>
""")

    expected = """
        <div class="dropdown">
          <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
            Dropdown
          </button>
          <ul class="dropdown-menu dropdown-menu-dark">
            <li><a class="dropdown-item" href="#">Action</a></li>
            <li><a class="dropdown-item" href="#">Another action</a></li>
          </ul>
        </div>
    """

    assert_html(rendered, expected)


def test_menu_alignment_end(render, assert_html):
    rendered = render("""
<c-bs-dropdown-button title="Dropdown" variant="secondary" align="end">
  <c-bs-dropdown-item href="#">Action</c-bs-dropdown-item>
  <c-bs-dropdown-item href="#">Another action</c-bs-dropdown-item>
</c-bs-dropdown-button>
""")

    expected = """
        <div class="dropdown">
          <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
            Dropdown
          </button>
          <ul class="dropdown-menu dropdown-menu-end">
            <li><a class="dropdown-item" href="#">Action</a></li>
            <li><a class="dropdown-item" href="#">Another action</a></li>
          </ul>
        </div>
    """

    assert_html(rendered, expected)


def test_basic_split_button(render, assert_html):
    rendered = render("""
<c-bs-split-button title="Primary" variant="primary">
  <c-bs-dropdown-item href="#">Action</c-bs-dropdown-item>
  <c-bs-dropdown-item href="#">Another action</c-bs-dropdown-item>
  <c-bs-dropdown-item href="#">Something else here</c-bs-dropdown-item>
  <c-bs-dropdown-divider />
  <c-bs-dropdown-item href="#">Separated link</c-bs-dropdown-item>
</c-bs-split-button>
""")

    expected = """
        <div class="dropdown">
          <div class="btn-group" role="group">
            <button class="btn btn-primary" type="button">
              Primary
            </button>
            <button class="btn btn-primary dropdown-toggle dropdown-toggle-split" type="button" data-bs-toggle="dropdown" aria-expanded="false">
              <span class="visually-hidden">Toggle dropdown</span>
            </button>
            <ul class="dropdown-menu">
              <li><a class="dropdown-item" href="#">Action</a></li>
              <li><a class="dropdown-item" href="#">Another action</a></li>
              <li><a class="dropdown-item" href="#">Something else here</a></li>
              <li><hr class="dropdown-divider"></li>
              <li><a class="dropdown-item" href="#">Separated link</a></li>
            </ul>
          </div>
        </div>
    """

    assert_html(rendered, expected)


def test_split_button_danger(render, assert_html):
    rendered = render("""
<c-bs-split-button title="Danger" variant="danger">
  <c-bs-dropdown-item href="#">Action</c-bs-dropdown-item>
  <c-bs-dropdown-item href="#">Another action</c-bs-dropdown-item>
  <c-bs-dropdown-divider />
  <c-bs-dropdown-item href="#">Separated link</c-bs-dropdown-item>
</c-bs-split-button>
""")

    expected = """
        <div class="dropdown">
          <div class="btn-group" role="group">
            <button class="btn btn-danger" type="button">
              Danger
            </button>
            <button class="btn btn-danger dropdown-toggle dropdown-toggle-split" type="button" data-bs-toggle="dropdown" aria-expanded="false">
              <span class="visually-hidden">Toggle dropdown</span>
            </button>
            <ul class="dropdown-menu">
              <li><a class="dropdown-item" href="#">Action</a></li>
              <li><a class="dropdown-item" href="#">Another action</a></li>
              <li><hr class="dropdown-divider"></li>
              <li><a class="dropdown-item" href="#">Separated link</a></li>
            </ul>
          </div>
        </div>
    """

    assert_html(rendered, expected)


def test_split_button_success(render, assert_html):
    rendered = render("""
<c-bs-split-button title="Success" variant="success">
  <c-bs-dropdown-item href="#">Action</c-bs-dropdown-item>
  <c-bs-dropdown-item href="#">Another action</c-bs-dropdown-item>
</c-bs-split-button>
""")

    expected = """
        <div class="dropdown">
          <div class="btn-group" role="group">
            <button class="btn btn-success" type="button">
              Success
            </button>
            <button class="btn btn-success dropdown-toggle dropdown-toggle-split" type="button" data-bs-toggle="dropdown" aria-expanded="false">
              <span class="visually-hidden">Toggle dropdown</span>
            </button>
            <ul class="dropdown-menu">
              <li><a class="dropdown-item" href="#">Action</a></li>
              <li><a class="dropdown-item" href="#">Another action</a></li>
            </ul>
          </div>
        </div>
    """

    assert_html(rendered, expected)


def test_split_button_large(render, assert_html):
    rendered = render("""
<c-bs-split-button title="Large button" variant="primary" size="lg">
  <c-bs-dropdown-item href="#">Action</c-bs-dropdown-item>
  <c-bs-dropdown-item href="#">Another action</c-bs-dropdown-item>
</c-bs-split-button>
""")

    expected = """
        <div class="dropdown">
          <div class="btn-group" role="group">
            <button class="btn btn-primary btn-lg" type="button">
              Large button
            </button>
            <button class="btn btn-primary dropdown-toggle dropdown-toggle-split btn-lg" type="button" data-bs-toggle="dropdown" aria-expanded="false">
              <span class="visually-hidden">Toggle dropdown</span>
            </button>
            <ul class="dropdown-menu">
              <li><a class="dropdown-item" href="#">Action</a></li>
              <li><a class="dropdown-item" href="#">Another action</a></li>
            </ul>
          </div>
        </div>
    """

    assert_html(rendered, expected)


def test_split_button_small(render, assert_html):
    rendered = render("""
<c-bs-split-button title="Small button" variant="secondary" size="sm">
  <c-bs-dropdown-item href="#">Action</c-bs-dropdown-item>
  <c-bs-dropdown-item href="#">Another action</c-bs-dropdown-item>
</c-bs-split-button>
""")

    expected = """
        <div class="dropdown">
          <div class="btn-group" role="group">
            <button class="btn btn-secondary btn-sm" type="button">
              Small button
            </button>
            <button class="btn btn-secondary dropdown-toggle dropdown-toggle-split btn-sm" type="button" data-bs-toggle="dropdown" aria-expanded="false">
              <span class="visually-hidden">Toggle dropdown</span>
            </button>
            <ul class="dropdown-menu">
              <li><a class="dropdown-item" href="#">Action</a></li>
              <li><a class="dropdown-item" href="#">Another action</a></li>
            </ul>
          </div>
        </div>
    """

    assert_html(rendered, expected)


def test_split_button_custom_toggle_label(render, assert_html):
    rendered = render("""
<c-bs-split-button title="Action" variant="primary" toggle_label="Custom toggle">
  <c-bs-dropdown-item href="#">Action</c-bs-dropdown-item>
  <c-bs-dropdown-item href="#">Another action</c-bs-dropdown-item>
</c-bs-split-button>
""")

    expected = """
        <div class="dropdown">
          <div class="btn-group" role="group">
            <button class="btn btn-primary" type="button">
              Action
            </button>
            <button class="btn btn-primary dropdown-toggle dropdown-toggle-split" type="button" data-bs-toggle="dropdown" aria-expanded="false">
              <span class="visually-hidden">Custom toggle</span>
            </button>
            <ul class="dropdown-menu">
              <li><a class="dropdown-item" href="#">Action</a></li>
              <li><a class="dropdown-item" href="#">Another action</a></li>
            </ul>
          </div>
        </div>
    """

    assert_html(rendered, expected)
