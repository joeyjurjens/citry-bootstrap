# All 8 Color Variants
def test_variant_primary(render, assert_html):
    rendered = render("""
<c-bs-alert variant="primary">A simple primary alert—check it out!</c-bs-alert>
""")

    expected = """
        <div class="alert alert-primary" role="alert">
          A simple primary alert—check it out!
        </div>
    """

    assert_html(rendered, expected)


def test_variant_secondary(render, assert_html):
    rendered = render("""
<c-bs-alert variant="secondary">A simple secondary alert—check it out!</c-bs-alert>
""")

    expected = """
        <div class="alert alert-secondary" role="alert">
          A simple secondary alert—check it out!
        </div>
    """

    assert_html(rendered, expected)


def test_variant_success(render, assert_html):
    rendered = render("""
<c-bs-alert variant="success">A simple success alert—check it out!</c-bs-alert>
""")

    expected = """
        <div class="alert alert-success" role="alert">
          A simple success alert—check it out!
        </div>
    """

    assert_html(rendered, expected)


def test_variant_danger(render, assert_html):
    rendered = render("""
<c-bs-alert variant="danger">A simple danger alert—check it out!</c-bs-alert>
""")

    expected = """
        <div class="alert alert-danger" role="alert">
          A simple danger alert—check it out!
        </div>
    """

    assert_html(rendered, expected)


def test_variant_warning(render, assert_html):
    rendered = render("""
<c-bs-alert variant="warning">A simple warning alert—check it out!</c-bs-alert>
""")

    expected = """
        <div class="alert alert-warning" role="alert">
          A simple warning alert—check it out!
        </div>
    """

    assert_html(rendered, expected)


def test_variant_info(render, assert_html):
    rendered = render("""
<c-bs-alert variant="info">A simple info alert—check it out!</c-bs-alert>
""")

    expected = """
        <div class="alert alert-info" role="alert">
          A simple info alert—check it out!
        </div>
    """

    assert_html(rendered, expected)


def test_variant_light(render, assert_html):
    rendered = render("""
<c-bs-alert variant="light">A simple light alert—check it out!</c-bs-alert>
""")

    expected = """
        <div class="alert alert-light" role="alert">
          A simple light alert—check it out!
        </div>
    """

    assert_html(rendered, expected)


def test_variant_dark(render, assert_html):
    rendered = render("""
<c-bs-alert variant="dark">A simple dark alert—check it out!</c-bs-alert>
""")

    expected = """
        <div class="alert alert-dark" role="alert">
          A simple dark alert—check it out!
        </div>
    """

    assert_html(rendered, expected)


# With Links
def test_link_color_primary(render, assert_html):
    rendered = render("""
<c-bs-alert variant="primary">
  A simple primary alert with
  <c-bs-alert-link href="#">an example link</c-bs-alert-link>. Give it a click if you like.
</c-bs-alert>
""")

    expected = """
        <div class="alert alert-primary" role="alert">
          A simple primary alert with <a href="#" class="alert-link">an example link</a>. Give it a click if you like.
        </div>
    """

    assert_html(rendered, expected)


def test_link_color_success(render, assert_html):
    rendered = render("""
<c-bs-alert variant="success">
  A simple success alert with
  <c-bs-alert-link href="#">an example link</c-bs-alert-link>.
</c-bs-alert>
""")

    expected = """
        <div class="alert alert-success" role="alert">
          A simple success alert with <a href="#" class="alert-link">an example link</a>.
        </div>
    """

    assert_html(rendered, expected)


def test_link_color_danger(render, assert_html):
    rendered = render("""
<c-bs-alert variant="danger">
  A simple danger alert with
  <c-bs-alert-link href="#">an example link</c-bs-alert-link>.
</c-bs-alert>
""")

    expected = """
        <div class="alert alert-danger" role="alert">
          A simple danger alert with <a href="#" class="alert-link">an example link</a>.
        </div>
    """

    assert_html(rendered, expected)


# With Additional Content
def test_additional_content(render, assert_html):
    rendered = render("""
<c-bs-alert variant="success">
  <c-bs-alert-heading>Well done!</c-bs-alert-heading>
  <p>Aww yeah, you successfully read this important alert message. This example text is going to run a bit longer so that you can see how spacing within an alert works with this kind of content.</p>
  <hr />
  <p class="mb-0">Whenever you need to, be sure to use margin utilities to keep things nice and tidy.</p>
</c-bs-alert>
""")

    expected = """
        <div class="alert alert-success" role="alert">
          <h4 class="alert-heading">Well done!</h4>
          <p>Aww yeah, you successfully read this important alert message. This example text is going to run a bit longer so that you can see how spacing within an alert works with this kind of content.</p>
          <hr>
          <p class="mb-0">Whenever you need to, be sure to use margin utilities to keep things nice and tidy.</p>
        </div>
    """

    assert_html(rendered, expected)


def test_with_icon(render, assert_html):
    rendered = render("""
<c-bs-alert variant="primary" c-attrs="{'class': 'd-flex align-items-center'}">
  <svg class="bi flex-shrink-0 me-2" width="24" height="24" role="img" aria-label="Info:">
    <use xlink:href="#info-fill"></use>
  </svg>
  <div>An example alert with an icon</div>
</c-bs-alert>
""")

    assert "alert-primary" in rendered
    assert "d-flex" in rendered
    assert "align-items-center" in rendered
    assert "An example alert with an icon" in rendered


# Dismissible Variants - All Colors
def test_dismissible_primary(render, assert_html):
    rendered = render("""
<c-bs-alert variant="primary" c-dismissible="True">A simple primary dismissible alert—check it out!</c-bs-alert>
""")

    expected = """
        <div class="alert alert-primary alert-dismissible fade show" role="alert">
          A simple primary dismissible alert—check it out!
          <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        </div>
    """

    assert_html(rendered, expected)


def test_dismissible_secondary(render, assert_html):
    rendered = render("""
<c-bs-alert variant="secondary" c-dismissible="True">A simple secondary dismissible alert—check it out!</c-bs-alert>
""")

    expected = """
        <div class="alert alert-secondary alert-dismissible fade show" role="alert">
          A simple secondary dismissible alert—check it out!
          <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        </div>
    """

    assert_html(rendered, expected)


def test_dismissible_success(render, assert_html):
    rendered = render("""
<c-bs-alert variant="success" c-dismissible="True">A simple success dismissible alert—check it out!</c-bs-alert>
""")

    expected = """
        <div class="alert alert-success alert-dismissible fade show" role="alert">
          A simple success dismissible alert—check it out!
          <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        </div>
    """

    assert_html(rendered, expected)


def test_dismissible_danger(render, assert_html):
    rendered = render("""
<c-bs-alert variant="danger" c-dismissible="True">A simple danger dismissible alert—check it out!</c-bs-alert>
""")

    expected = """
        <div class="alert alert-danger alert-dismissible fade show" role="alert">
          A simple danger dismissible alert—check it out!
          <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        </div>
    """

    assert_html(rendered, expected)


def test_dismissible_warning(render, assert_html):
    rendered = render("""
<c-bs-alert variant="warning" c-dismissible="True">
  <strong>Holy guacamole!</strong>
  You should check in on some of those fields below.
</c-bs-alert>
""")

    expected = """
        <div class="alert alert-warning alert-dismissible fade show" role="alert">
          <strong>Holy guacamole!</strong> You should check in on some of those fields below.
          <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        </div>
    """

    assert_html(rendered, expected)


def test_dismissible_info(render, assert_html):
    rendered = render("""
<c-bs-alert variant="info" c-dismissible="True">A simple info dismissible alert—check it out!</c-bs-alert>
""")

    expected = """
        <div class="alert alert-info alert-dismissible fade show" role="alert">
          A simple info dismissible alert—check it out!
          <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        </div>
    """

    assert_html(rendered, expected)


def test_dismissible_light(render, assert_html):
    rendered = render("""
<c-bs-alert variant="light" c-dismissible="True">A simple light dismissible alert—check it out!</c-bs-alert>
""")

    expected = """
        <div class="alert alert-light alert-dismissible fade show" role="alert">
          A simple light dismissible alert—check it out!
          <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        </div>
    """

    assert_html(rendered, expected)


def test_dismissible_dark(render, assert_html):
    rendered = render("""
<c-bs-alert variant="dark" c-dismissible="True">A simple dark dismissible alert—check it out!</c-bs-alert>
""")

    expected = """
        <div class="alert alert-dark alert-dismissible fade show" role="alert">
          A simple dark dismissible alert—check it out!
          <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        </div>
    """

    assert_html(rendered, expected)
