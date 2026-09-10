def test_basic(render, assert_html):
    rendered = render("""
<c-bs-dropdown>
  <c-bs-dropdown-toggle variant="secondary">Dropdown button</c-bs-dropdown-toggle>
  <c-bs-dropdown-menu>
    <c-bs-dropdown-item href="#">Action</c-bs-dropdown-item>
    <c-bs-dropdown-item href="#">Another action</c-bs-dropdown-item>
    <c-bs-dropdown-item href="#">Something else here</c-bs-dropdown-item>
  </c-bs-dropdown-menu>
</c-bs-dropdown>
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


# Color Variants
def test_variant_primary(render, assert_html):
    rendered = render("""
<c-bs-dropdown>
  <c-bs-dropdown-toggle variant="primary">Primary</c-bs-dropdown-toggle>
  <c-bs-dropdown-menu>
    <c-bs-dropdown-item href="#">Action</c-bs-dropdown-item>
  </c-bs-dropdown-menu>
</c-bs-dropdown>
""")
    assert "btn-primary" in rendered


def test_variant_success(render, assert_html):
    rendered = render("""
<c-bs-dropdown>
  <c-bs-dropdown-toggle variant="success">Success</c-bs-dropdown-toggle>
  <c-bs-dropdown-menu>
    <c-bs-dropdown-item href="#">Action</c-bs-dropdown-item>
  </c-bs-dropdown-menu>
</c-bs-dropdown>
""")
    assert "btn-success" in rendered


def test_variant_danger(render, assert_html):
    rendered = render("""
<c-bs-dropdown>
  <c-bs-dropdown-toggle variant="danger">Danger</c-bs-dropdown-toggle>
  <c-bs-dropdown-menu>
    <c-bs-dropdown-item href="#">Action</c-bs-dropdown-item>
  </c-bs-dropdown-menu>
</c-bs-dropdown>
""")
    assert "btn-danger" in rendered


def test_variant_warning(render, assert_html):
    rendered = render("""
<c-bs-dropdown>
  <c-bs-dropdown-toggle variant="warning">Warning</c-bs-dropdown-toggle>
  <c-bs-dropdown-menu>
    <c-bs-dropdown-item href="#">Action</c-bs-dropdown-item>
  </c-bs-dropdown-menu>
</c-bs-dropdown>
""")
    assert "btn-warning" in rendered


def test_variant_info(render, assert_html):
    rendered = render("""
<c-bs-dropdown>
  <c-bs-dropdown-toggle variant="info">Info</c-bs-dropdown-toggle>
  <c-bs-dropdown-menu>
    <c-bs-dropdown-item href="#">Action</c-bs-dropdown-item>
  </c-bs-dropdown-menu>
</c-bs-dropdown>
""")
    assert "btn-info" in rendered


def test_variant_light(render, assert_html):
    rendered = render("""
<c-bs-dropdown>
  <c-bs-dropdown-toggle variant="light">Light</c-bs-dropdown-toggle>
  <c-bs-dropdown-menu>
    <c-bs-dropdown-item href="#">Action</c-bs-dropdown-item>
  </c-bs-dropdown-menu>
</c-bs-dropdown>
""")
    assert "btn-light" in rendered


def test_variant_dark(render, assert_html):
    rendered = render("""
<c-bs-dropdown>
  <c-bs-dropdown-toggle variant="dark">Dark</c-bs-dropdown-toggle>
  <c-bs-dropdown-menu>
    <c-bs-dropdown-item href="#">Action</c-bs-dropdown-item>
  </c-bs-dropdown-menu>
</c-bs-dropdown>
""")
    assert "btn-dark" in rendered


# Sizing
def test_size_large(render, assert_html):
    rendered = render("""
<c-bs-dropdown>
  <c-bs-dropdown-toggle variant="secondary" size="lg">Large button</c-bs-dropdown-toggle>
  <c-bs-dropdown-menu>
    <c-bs-dropdown-item href="#">Action</c-bs-dropdown-item>
  </c-bs-dropdown-menu>
</c-bs-dropdown>
""")

    expected = """
        <div class="dropdown">
          <button class="btn btn-secondary dropdown-toggle btn-lg" type="button" data-bs-toggle="dropdown" aria-expanded="false">
            Large button
          </button>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="#">Action</a></li>
          </ul>
        </div>
    """

    assert_html(rendered, expected)


def test_size_small(render, assert_html):
    rendered = render("""
<c-bs-dropdown>
  <c-bs-dropdown-toggle variant="secondary" size="sm">Small button</c-bs-dropdown-toggle>
  <c-bs-dropdown-menu>
    <c-bs-dropdown-item href="#">Action</c-bs-dropdown-item>
  </c-bs-dropdown-menu>
</c-bs-dropdown>
""")

    expected = """
        <div class="dropdown">
          <button class="btn btn-secondary dropdown-toggle btn-sm" type="button" data-bs-toggle="dropdown" aria-expanded="false">
            Small button
          </button>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="#">Action</a></li>
          </ul>
        </div>
    """

    assert_html(rendered, expected)


# Directions
def test_dropup(render, assert_html):
    rendered = render("""
<c-bs-dropdown direction="up">
  <c-bs-dropdown-toggle variant="secondary">Dropup</c-bs-dropdown-toggle>
  <c-bs-dropdown-menu>
    <c-bs-dropdown-item href="#">Action</c-bs-dropdown-item>
  </c-bs-dropdown-menu>
</c-bs-dropdown>
""")

    expected = """
        <div class="dropup">
          <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
            Dropup
          </button>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="#">Action</a></li>
          </ul>
        </div>
    """

    assert_html(rendered, expected)


def test_dropend(render, assert_html):
    rendered = render("""
<c-bs-dropdown direction="end">
  <c-bs-dropdown-toggle variant="secondary">Dropend</c-bs-dropdown-toggle>
  <c-bs-dropdown-menu>
    <c-bs-dropdown-item href="#">Action</c-bs-dropdown-item>
  </c-bs-dropdown-menu>
</c-bs-dropdown>
""")

    expected = """
        <div class="dropend">
          <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
            Dropend
          </button>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="#">Action</a></li>
          </ul>
        </div>
    """

    assert_html(rendered, expected)


def test_dropstart(render, assert_html):
    rendered = render("""
<c-bs-dropdown direction="start">
  <c-bs-dropdown-toggle variant="secondary">Dropstart</c-bs-dropdown-toggle>
  <c-bs-dropdown-menu>
    <c-bs-dropdown-item href="#">Action</c-bs-dropdown-item>
  </c-bs-dropdown-menu>
</c-bs-dropdown>
""")

    expected = """
        <div class="dropstart">
          <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
            Dropstart
          </button>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="#">Action</a></li>
          </ul>
        </div>
    """

    assert_html(rendered, expected)


def test_centered(render, assert_html):
    rendered = render("""
<c-bs-dropdown c-centered="True">
  <c-bs-dropdown-toggle variant="secondary">Centered dropdown</c-bs-dropdown-toggle>
  <c-bs-dropdown-menu>
    <c-bs-dropdown-item href="#">Action</c-bs-dropdown-item>
  </c-bs-dropdown-menu>
</c-bs-dropdown>
""")

    expected = """
        <div class="dropdown dropdown-center">
          <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
            Centered dropdown
          </button>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="#">Action</a></li>
          </ul>
        </div>
    """

    assert_html(rendered, expected)


def test_centered_dropup(render, assert_html):
    rendered = render("""
<c-bs-dropdown direction="up" c-centered="True">
  <c-bs-dropdown-toggle variant="secondary">Centered dropup</c-bs-dropdown-toggle>
  <c-bs-dropdown-menu>
    <c-bs-dropdown-item href="#">Action</c-bs-dropdown-item>
  </c-bs-dropdown-menu>
</c-bs-dropdown>
""")

    expected = """
        <div class="dropup dropup-center">
          <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
            Centered dropup
          </button>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="#">Action</a></li>
          </ul>
        </div>
    """

    assert_html(rendered, expected)


# Menu Alignment
def test_menu_align_end(render, assert_html):
    rendered = render("""
<c-bs-dropdown>
  <c-bs-dropdown-toggle variant="secondary">Right-aligned menu</c-bs-dropdown-toggle>
  <c-bs-dropdown-menu align="end">
    <c-bs-dropdown-item href="#">Action</c-bs-dropdown-item>
  </c-bs-dropdown-menu>
</c-bs-dropdown>
""")

    expected = """
        <div class="dropdown">
          <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
            Right-aligned menu
          </button>
          <ul class="dropdown-menu dropdown-menu-end">
            <li><a class="dropdown-item" href="#">Action</a></li>
          </ul>
        </div>
    """

    assert_html(rendered, expected)


def test_menu_responsive_align_lg_end(render, assert_html):
    rendered = render("""
<c-bs-dropdown>
  <c-bs-dropdown-toggle variant="secondary">Left-aligned, lg-right</c-bs-dropdown-toggle>
  <c-bs-dropdown-menu align_lg="end">
    <c-bs-dropdown-item href="#">Action</c-bs-dropdown-item>
  </c-bs-dropdown-menu>
</c-bs-dropdown>
""")

    expected = """
        <div class="dropdown">
          <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
            Left-aligned, lg-right
          </button>
          <ul class="dropdown-menu dropdown-menu-lg-end">
            <li><a class="dropdown-item" href="#">Action</a></li>
          </ul>
        </div>
    """

    assert_html(rendered, expected)


def test_menu_responsive_align_end_lg_start(render, assert_html):
    rendered = render("""
<c-bs-dropdown>
  <c-bs-dropdown-toggle variant="secondary">Right-aligned, lg-left</c-bs-dropdown-toggle>
  <c-bs-dropdown-menu align="end" align_lg="start">
    <c-bs-dropdown-item href="#">Action</c-bs-dropdown-item>
  </c-bs-dropdown-menu>
</c-bs-dropdown>
""")

    expected = """
        <div class="dropdown">
          <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
            Right-aligned, lg-left
          </button>
          <ul class="dropdown-menu dropdown-menu-end dropdown-menu-lg-start">
            <li><a class="dropdown-item" href="#">Action</a></li>
          </ul>
        </div>
    """

    assert_html(rendered, expected)


# Auto Close Behaviors
def test_auto_close_true(render, assert_html):
    rendered = render("""
<c-bs-dropdown auto_close="true">
  <c-bs-dropdown-toggle variant="secondary">Default dropdown</c-bs-dropdown-toggle>
  <c-bs-dropdown-menu>
    <c-bs-dropdown-item href="#">Menu item</c-bs-dropdown-item>
  </c-bs-dropdown-menu>
</c-bs-dropdown>
""")
    assert 'data-bs-auto-close="true"' in rendered


def test_auto_close_false(render, assert_html):
    rendered = render("""
<c-bs-dropdown auto_close="false">
  <c-bs-dropdown-toggle variant="secondary">Manual close</c-bs-dropdown-toggle>
  <c-bs-dropdown-menu>
    <c-bs-dropdown-item href="#">Menu item</c-bs-dropdown-item>
  </c-bs-dropdown-menu>
</c-bs-dropdown>
""")
    assert 'data-bs-auto-close="false"' in rendered


def test_auto_close_inside(render, assert_html):
    rendered = render("""
<c-bs-dropdown auto_close="inside">
  <c-bs-dropdown-toggle variant="secondary">Clickable inside</c-bs-dropdown-toggle>
  <c-bs-dropdown-menu>
    <c-bs-dropdown-item href="#">Menu item</c-bs-dropdown-item>
  </c-bs-dropdown-menu>
</c-bs-dropdown>
""")
    assert 'data-bs-auto-close="inside"' in rendered


def test_auto_close_outside(render, assert_html):
    rendered = render("""
<c-bs-dropdown auto_close="outside">
  <c-bs-dropdown-toggle variant="secondary">Clickable outside</c-bs-dropdown-toggle>
  <c-bs-dropdown-menu>
    <c-bs-dropdown-item href="#">Menu item</c-bs-dropdown-item>
  </c-bs-dropdown-menu>
</c-bs-dropdown>
""")
    assert 'data-bs-auto-close="outside"' in rendered


# Dark Dropdown
def test_dark_dropdown(render, assert_html):
    rendered = render("""
<c-bs-dropdown>
  <c-bs-dropdown-toggle variant="secondary">Dropdown button</c-bs-dropdown-toggle>
  <c-bs-dropdown-menu c-dark="True">
    <c-bs-dropdown-item href="#" c-active="True">Action</c-bs-dropdown-item>
    <c-bs-dropdown-item href="#">Another action</c-bs-dropdown-item>
    <c-bs-dropdown-item href="#">Something else here</c-bs-dropdown-item>
    <c-bs-dropdown-divider />
    <c-bs-dropdown-item href="#">Separated link</c-bs-dropdown-item>
  </c-bs-dropdown-menu>
</c-bs-dropdown>
""")

    expected = """
        <div class="dropdown">
          <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
            Dropdown button
          </button>
          <ul class="dropdown-menu dropdown-menu-dark">
            <li><a class="dropdown-item active" href="#" aria-current="true">Action</a></li>
            <li><a class="dropdown-item" href="#">Another action</a></li>
            <li><a class="dropdown-item" href="#">Something else here</a></li>
            <li><hr class="dropdown-divider"></li>
            <li><a class="dropdown-item" href="#">Separated link</a></li>
          </ul>
        </div>
    """

    assert_html(rendered, expected)


# Menu Headers and Dividers
def test_with_divider(render, assert_html):
    rendered = render("""
<c-bs-dropdown-menu>
  <c-bs-dropdown-item href="#">Action</c-bs-dropdown-item>
  <c-bs-dropdown-item href="#">Another action</c-bs-dropdown-item>
  <c-bs-dropdown-item href="#">Something else here</c-bs-dropdown-item>
  <c-bs-dropdown-divider />
  <c-bs-dropdown-item href="#">Separated link</c-bs-dropdown-item>
</c-bs-dropdown-menu>
""")

    expected = """
        <ul class="dropdown-menu">
          <li><a class="dropdown-item" href="#">Action</a></li>
          <li><a class="dropdown-item" href="#">Another action</a></li>
          <li><a class="dropdown-item" href="#">Something else here</a></li>
          <li><hr class="dropdown-divider"></li>
          <li><a class="dropdown-item" href="#">Separated link</a></li>
        </ul>
    """

    assert_html(rendered, expected)


def test_with_header(render, assert_html):
    rendered = render("""
<c-bs-dropdown-menu>
  <c-bs-dropdown-header>Dropdown header</c-bs-dropdown-header>
  <c-bs-dropdown-item href="#">Action</c-bs-dropdown-item>
  <c-bs-dropdown-item href="#">Another action</c-bs-dropdown-item>
</c-bs-dropdown-menu>
""")

    expected = """
        <ul class="dropdown-menu">
          <li><h6 class="dropdown-header">Dropdown header</h6></li>
          <li><a class="dropdown-item" href="#">Action</a></li>
          <li><a class="dropdown-item" href="#">Another action</a></li>
        </ul>
    """

    assert_html(rendered, expected)


def test_with_text(render, assert_html):
    rendered = render("""
<c-bs-dropdown-menu>
  <c-bs-dropdown-item-text>Dropdown item text</c-bs-dropdown-item-text>
  <c-bs-dropdown-item href="#">Action</c-bs-dropdown-item>
  <c-bs-dropdown-item href="#">Another action</c-bs-dropdown-item>
</c-bs-dropdown-menu>
""")

    expected = """
        <ul class="dropdown-menu">
          <li><span class="dropdown-item-text">Dropdown item text</span></li>
          <li><a class="dropdown-item" href="#">Action</a></li>
          <li><a class="dropdown-item" href="#">Another action</a></li>
        </ul>
    """

    assert_html(rendered, expected)


# Active and Disabled Items
def test_active_item(render, assert_html):
    rendered = render("""
<c-bs-dropdown-menu>
  <c-bs-dropdown-item href="#">Regular link</c-bs-dropdown-item>
  <c-bs-dropdown-item href="#" c-active="True">Active link</c-bs-dropdown-item>
  <c-bs-dropdown-item href="#">Another link</c-bs-dropdown-item>
</c-bs-dropdown-menu>
""")

    expected = """
        <ul class="dropdown-menu">
          <li><a class="dropdown-item" href="#">Regular link</a></li>
          <li><a class="dropdown-item active" href="#" aria-current="true">Active link</a></li>
          <li><a class="dropdown-item" href="#">Another link</a></li>
        </ul>
    """

    assert_html(rendered, expected)


def test_disabled_item(render, assert_html):
    rendered = render("""
<c-bs-dropdown-menu>
  <c-bs-dropdown-item href="#">Regular link</c-bs-dropdown-item>
  <c-bs-dropdown-item href="#" c-disabled="True">Disabled link</c-bs-dropdown-item>
  <c-bs-dropdown-item href="#">Another link</c-bs-dropdown-item>
</c-bs-dropdown-menu>
""")

    expected = """
        <ul class="dropdown-menu">
          <li><a class="dropdown-item" href="#">Regular link</a></li>
          <li><a class="dropdown-item disabled" href="#" aria-disabled="true" tabindex="-1">Disabled link</a></li>
          <li><a class="dropdown-item" href="#">Another link</a></li>
        </ul>
    """

    assert_html(rendered, expected)


def test_button_items(render, assert_html):
    rendered = render("""
<c-bs-dropdown-menu>
  <c-bs-dropdown-item as_="button">Action</c-bs-dropdown-item>
  <c-bs-dropdown-item as_="button">Another action</c-bs-dropdown-item>
  <c-bs-dropdown-item as_="button">Something else here</c-bs-dropdown-item>
</c-bs-dropdown-menu>
""")

    expected = """
        <ul class="dropdown-menu">
          <li><button class="dropdown-item" type="button">Action</button></li>
          <li><button class="dropdown-item" type="button">Another action</button></li>
          <li><button class="dropdown-item" type="button">Something else here</button></li>
        </ul>
    """

    assert_html(rendered, expected)
