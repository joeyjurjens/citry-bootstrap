import re


def test_basic_navbar(render, assert_html):
    rendered = render("""
<c-bs-navbar expand="lg" c-attrs="{'class': 'bg-body-tertiary'}">
  <c-bs-navbar-brand href="#">Brand</c-bs-navbar-brand>
  <c-bs-navbar-toggler />
  <c-bs-navbar-collapse>
    <c-bs-navbar-nav>
      <c-bs-nav-item>
        <c-bs-nav-link href="#" c-active="True">Home</c-bs-nav-link>
      </c-bs-nav-item>
      <c-bs-nav-item>
        <c-bs-nav-link href="#">Features</c-bs-nav-link>
      </c-bs-nav-item>
      <c-bs-nav-item>
        <c-bs-nav-link href="#">Pricing</c-bs-nav-link>
      </c-bs-nav-item>
      <c-bs-nav-item>
        <c-bs-nav-link href="#" c-disabled="True">Disabled</c-bs-nav-link>
      </c-bs-nav-item>
    </c-bs-navbar-nav>
  </c-bs-navbar-collapse>
</c-bs-navbar>
""")

    collapse_id_match = re.search(r'id="(navbar-collapse-[^"]+)"', rendered)
    assert collapse_id_match is not None
    collapse_id = collapse_id_match.group(1)

    expected = f"""
        <nav class="navbar navbar-expand-lg bg-body-tertiary">
            <div class="container-fluid">
                <a class="navbar-brand" href="#">Brand</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#{collapse_id}" aria-controls="{collapse_id}" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="{collapse_id}">
                    <ul class="navbar-nav">
                        <li class="nav-item">
                            <a class="nav-link active" aria-current="page" href="#">Home</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#">Features</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#">Pricing</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link disabled" aria-disabled="true">Disabled</a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
    """

    assert_html(rendered, expected)


def test_navbar_expand_sm(render, assert_html):
    rendered = render("""
<c-bs-navbar expand="sm" c-attrs="{'class': 'bg-body-tertiary'}">
  <c-bs-navbar-brand href="#">Brand</c-bs-navbar-brand>
</c-bs-navbar>
""")

    expected = """
        <nav class="navbar navbar-expand-sm bg-body-tertiary">
            <div class="container-fluid">
                <a class="navbar-brand" href="#">Brand</a>
            </div>
        </nav>
    """

    assert_html(rendered, expected)


def test_navbar_expand_md(render, assert_html):
    rendered = render("""
<c-bs-navbar expand="md" c-attrs="{'class': 'bg-body-tertiary'}">
  <c-bs-navbar-brand href="#">Brand</c-bs-navbar-brand>
</c-bs-navbar>
""")

    expected = """
        <nav class="navbar navbar-expand-md bg-body-tertiary">
            <div class="container-fluid">
                <a class="navbar-brand" href="#">Brand</a>
            </div>
        </nav>
    """

    assert_html(rendered, expected)


def test_navbar_expand_xl(render, assert_html):
    rendered = render("""
<c-bs-navbar expand="xl" c-attrs="{'class': 'bg-body-tertiary'}">
  <c-bs-navbar-brand href="#">Brand</c-bs-navbar-brand>
</c-bs-navbar>
""")

    expected = """
        <nav class="navbar navbar-expand-xl bg-body-tertiary">
            <div class="container-fluid">
                <a class="navbar-brand" href="#">Brand</a>
            </div>
        </nav>
    """

    assert_html(rendered, expected)


def test_navbar_expand_xxl(render, assert_html):
    rendered = render("""
<c-bs-navbar expand="xxl" c-attrs="{'class': 'bg-body-tertiary'}">
  <c-bs-navbar-brand href="#">Brand</c-bs-navbar-brand>
</c-bs-navbar>
""")

    expected = """
        <nav class="navbar navbar-expand-xxl bg-body-tertiary">
            <div class="container-fluid">
                <a class="navbar-brand" href="#">Brand</a>
            </div>
        </nav>
    """

    assert_html(rendered, expected)


def test_navbar_with_form(render, assert_html):
    rendered = render("""
<c-bs-navbar expand="lg" c-attrs="{'class': 'bg-body-tertiary'}">
  <c-bs-navbar-brand href="#">Navbar</c-bs-navbar-brand>
  <form class="d-flex" role="search">
    <c-bs-form-control type="search" placeholder="Search" c-attrs="{'class': 'me-2', 'aria-label': 'Search'}" />
    <c-bs-button variant="success" c-outline="True" type="submit">Search</c-bs-button>
  </form>
</c-bs-navbar>
""")

    assert "d-flex" in rendered
    assert "form-control" in rendered
    assert "Search" in rendered


def test_navbar_light_background(render, assert_html):
    rendered = render("""
<c-bs-navbar c-attrs="{'class': 'bg-light'}">
  <c-bs-navbar-brand href="#">Navbar</c-bs-navbar-brand>
</c-bs-navbar>
""")

    expected = """
        <nav class="navbar bg-light">
            <div class="container-fluid">
                <a class="navbar-brand" href="#">Navbar</a>
            </div>
        </nav>
    """

    assert_html(rendered, expected)


def test_navbar_primary_background(render, assert_html):
    rendered = render("""
<c-bs-navbar c-attrs="{'class': 'bg-primary', 'data-bs-theme': 'dark'}">
  <c-bs-navbar-brand href="#">Navbar</c-bs-navbar-brand>
</c-bs-navbar>
""")

    assert "bg-primary" in rendered
    assert 'data-bs-theme="dark"' in rendered


def test_navbar_container_sm(render, assert_html):
    rendered = render("""
<c-bs-navbar expand="lg" container="sm" c-attrs="{'class': 'bg-body-tertiary'}">
  <c-bs-navbar-brand href="#">Navbar</c-bs-navbar-brand>
</c-bs-navbar>
""")

    assert "container-sm" in rendered


def test_navbar_container_md(render, assert_html):
    rendered = render("""
<c-bs-navbar expand="lg" container="md" c-attrs="{'class': 'bg-body-tertiary'}">
  <c-bs-navbar-brand href="#">Navbar</c-bs-navbar-brand>
</c-bs-navbar>
""")

    assert "container-md" in rendered


def test_navbar_container_lg(render, assert_html):
    rendered = render("""
<c-bs-navbar expand="lg" container="lg" c-attrs="{'class': 'bg-body-tertiary'}">
  <c-bs-navbar-brand href="#">Navbar</c-bs-navbar-brand>
</c-bs-navbar>
""")

    assert "container-lg" in rendered


def test_navbar_container_xl(render, assert_html):
    rendered = render("""
<c-bs-navbar expand="lg" container="xl" c-attrs="{'class': 'bg-body-tertiary'}">
  <c-bs-navbar-brand href="#">Navbar</c-bs-navbar-brand>
</c-bs-navbar>
""")

    assert "container-xl" in rendered


def test_navbar_container_xxl(render, assert_html):
    rendered = render("""
<c-bs-navbar expand="lg" container="xxl" c-attrs="{'class': 'bg-body-tertiary'}">
  <c-bs-navbar-brand href="#">Navbar</c-bs-navbar-brand>
</c-bs-navbar>
""")

    assert "container-xxl" in rendered


def test_navbar_disabled_brand(render, assert_html):
    rendered = render("""
<c-bs-navbar c-attrs="{'class': 'bg-body-tertiary'}">
  <c-bs-navbar-brand href="#">Disabled Brand</c-bs-navbar-brand>
</c-bs-navbar>
""")

    expected = """
        <nav class="navbar bg-body-tertiary">
            <div class="container-fluid">
                <a class="navbar-brand" href="#">Disabled Brand</a>
            </div>
        </nav>
    """

    assert_html(rendered, expected)


def test_navbar_with_brand_image(render, assert_html):
    rendered = render("""
<c-bs-navbar expand="lg" c-attrs="{'class': 'bg-body-tertiary'}">
  <c-bs-navbar-brand href="#">
    <img src="/docs/5.3/assets/brand/bootstrap-logo.svg" alt="Bootstrap" width="30" height="24" class="d-inline-block align-text-top" />
    Bootstrap
  </c-bs-navbar-brand>
</c-bs-navbar>
""")

    expected = """
        <nav class="navbar navbar-expand-lg bg-body-tertiary">
            <div class="container-fluid">
                <a class="navbar-brand" href="#">
                    <img src="/docs/5.3/assets/brand/bootstrap-logo.svg" alt="Bootstrap" width="30" height="24" class="d-inline-block align-text-top">
                    Bootstrap
                </a>
            </div>
        </nav>
    """

    assert_html(rendered, expected)


def test_navbar_with_text(render, assert_html):
    rendered = render("""
<c-bs-navbar c-attrs="{'class': 'bg-body-tertiary'}">
  <c-bs-navbar-brand href="#">Navbar w/ text</c-bs-navbar-brand>
  <c-bs-navbar-text>Navbar text with an inline element</c-bs-navbar-text>
</c-bs-navbar>
""")

    expected = """
        <nav class="navbar bg-body-tertiary">
            <div class="container-fluid">
                <a class="navbar-brand" href="#">Navbar w/ text</a>
                <span class="navbar-text">
                    Navbar text with an inline element
                </span>
            </div>
        </nav>
    """

    assert_html(rendered, expected)


def test_navbar_dark(render, assert_html):
    rendered = render("""
<c-bs-navbar variant="dark" c-attrs="{'class': 'navbar-dark bg-dark'}">
  <c-bs-navbar-brand href="#">Navbar</c-bs-navbar-brand>
</c-bs-navbar>
""")

    expected = """
        <nav class="navbar navbar-dark bg-dark" data-bs-theme="dark">
            <div class="container-fluid">
                <a class="navbar-brand" href="#">Navbar</a>
            </div>
        </nav>
    """

    assert_html(rendered, expected)


def test_navbar_without_container(render, assert_html):
    rendered = render("""
<c-bs-navbar expand="lg" c-container="False" c-attrs="{'class': 'bg-body-tertiary'}">
  <c-bs-navbar-brand href="#">Navbar</c-bs-navbar-brand>
</c-bs-navbar>
""")

    expected = """
        <nav class="navbar navbar-expand-lg bg-body-tertiary">
            <a class="navbar-brand" href="#">Navbar</a>
        </nav>
    """

    assert_html(rendered, expected)
