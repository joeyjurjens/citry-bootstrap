def test_basic(render, assert_html):
    rendered = render("""
<c-bs-nav as_="ul">
  <c-bs-nav-item>
    <c-bs-nav-link c-active="True" href="#">Active</c-bs-nav-link>
  </c-bs-nav-item>
  <c-bs-nav-item>
    <c-bs-nav-link href="#">Link</c-bs-nav-link>
  </c-bs-nav-item>
  <c-bs-nav-item>
    <c-bs-nav-link href="#">Link</c-bs-nav-link>
  </c-bs-nav-item>
  <c-bs-nav-item>
    <c-bs-nav-link c-disabled="True">Disabled</c-bs-nav-link>
  </c-bs-nav-item>
</c-bs-nav>
""")

    expected = """
        <ul class="nav">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="#">Active</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Link</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Link</a>
          </li>
          <li class="nav-item">
            <a class="nav-link disabled" aria-disabled="true">Disabled</a>
          </li>
        </ul>
    """

    assert_html(rendered, expected)


def test_basic_nav_element(render, assert_html):
    rendered = render("""
<c-bs-nav>
  <c-bs-nav-link c-active="True" href="#">Active</c-bs-nav-link>
  <c-bs-nav-link href="#">Link</c-bs-nav-link>
  <c-bs-nav-link href="#">Link</c-bs-nav-link>
  <c-bs-nav-link c-disabled="True">Disabled</c-bs-nav-link>
</c-bs-nav>
""")

    expected = """
        <nav class="nav">
          <a class="nav-link active" aria-current="page" href="#">Active</a>
          <a class="nav-link" href="#">Link</a>
          <a class="nav-link" href="#">Link</a>
          <a class="nav-link disabled" aria-disabled="true">Disabled</a>
        </nav>
    """

    assert_html(rendered, expected)


def test_tabs(render, assert_html):
    rendered = render("""
<c-bs-nav variant="tabs" as_="ul">
  <c-bs-nav-item>
    <c-bs-nav-link c-active="True" href="#">Active</c-bs-nav-link>
  </c-bs-nav-item>
  <c-bs-nav-item>
    <c-bs-nav-link href="#">Link</c-bs-nav-link>
  </c-bs-nav-item>
  <c-bs-nav-item>
    <c-bs-nav-link href="#">Link</c-bs-nav-link>
  </c-bs-nav-item>
  <c-bs-nav-item>
    <c-bs-nav-link c-disabled="True">Disabled</c-bs-nav-link>
  </c-bs-nav-item>
</c-bs-nav>
""")

    expected = """
        <ul class="nav nav-tabs">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="#">Active</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Link</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Link</a>
          </li>
          <li class="nav-item">
            <a class="nav-link disabled" aria-disabled="true">Disabled</a>
          </li>
        </ul>
    """

    assert_html(rendered, expected)


def test_pills(render, assert_html):
    rendered = render("""
<c-bs-nav variant="pills" as_="ul">
  <c-bs-nav-item>
    <c-bs-nav-link c-active="True" href="#">Active</c-bs-nav-link>
  </c-bs-nav-item>
  <c-bs-nav-item>
    <c-bs-nav-link href="#">Link</c-bs-nav-link>
  </c-bs-nav-item>
  <c-bs-nav-item>
    <c-bs-nav-link href="#">Link</c-bs-nav-link>
  </c-bs-nav-item>
  <c-bs-nav-item>
    <c-bs-nav-link c-disabled="True">Disabled</c-bs-nav-link>
  </c-bs-nav-item>
</c-bs-nav>
""")

    expected = """
        <ul class="nav nav-pills">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="#">Active</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Link</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Link</a>
          </li>
          <li class="nav-item">
            <a class="nav-link disabled" aria-disabled="true">Disabled</a>
          </li>
        </ul>
    """

    assert_html(rendered, expected)


def test_underline(render, assert_html):
    rendered = render("""
<c-bs-nav variant="underline" as_="ul">
  <c-bs-nav-item>
    <c-bs-nav-link c-active="True" href="#">Active</c-bs-nav-link>
  </c-bs-nav-item>
  <c-bs-nav-item>
    <c-bs-nav-link href="#">Link</c-bs-nav-link>
  </c-bs-nav-item>
  <c-bs-nav-item>
    <c-bs-nav-link href="#">Link</c-bs-nav-link>
  </c-bs-nav-item>
  <c-bs-nav-item>
    <c-bs-nav-link c-disabled="True">Disabled</c-bs-nav-link>
  </c-bs-nav-item>
</c-bs-nav>
""")

    expected = """
        <ul class="nav nav-underline">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="#">Active</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Link</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Link</a>
          </li>
          <li class="nav-item">
            <a class="nav-link disabled" aria-disabled="true">Disabled</a>
          </li>
        </ul>
    """

    assert_html(rendered, expected)


def test_vertical(render, assert_html):
    rendered = render("""
<c-bs-nav c-vertical="True" as_="ul">
  <c-bs-nav-item>
    <c-bs-nav-link c-active="True" href="#">Active</c-bs-nav-link>
  </c-bs-nav-item>
  <c-bs-nav-item>
    <c-bs-nav-link href="#">Link</c-bs-nav-link>
  </c-bs-nav-item>
  <c-bs-nav-item>
    <c-bs-nav-link href="#">Link</c-bs-nav-link>
  </c-bs-nav-item>
  <c-bs-nav-item>
    <c-bs-nav-link c-disabled="True">Disabled</c-bs-nav-link>
  </c-bs-nav-item>
</c-bs-nav>
""")

    expected = """
        <ul class="nav flex-column">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="#">Active</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Link</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Link</a>
          </li>
          <li class="nav-item">
            <a class="nav-link disabled" aria-disabled="true">Disabled</a>
          </li>
        </ul>
    """

    assert_html(rendered, expected)


def test_vertical_nav_element(render, assert_html):
    rendered = render("""
<c-bs-nav c-vertical="True">
  <c-bs-nav-link c-active="True" href="#">Active</c-bs-nav-link>
  <c-bs-nav-link href="#">Link</c-bs-nav-link>
  <c-bs-nav-link href="#">Link</c-bs-nav-link>
  <c-bs-nav-link c-disabled="True">Disabled</c-bs-nav-link>
</c-bs-nav>
""")

    expected = """
        <nav class="nav flex-column">
          <a class="nav-link active" aria-current="page" href="#">Active</a>
          <a class="nav-link" href="#">Link</a>
          <a class="nav-link" href="#">Link</a>
          <a class="nav-link disabled" aria-disabled="true">Disabled</a>
        </nav>
    """

    assert_html(rendered, expected)


def test_fill(render, assert_html):
    rendered = render("""
<c-bs-nav variant="pills" c-fill="True" as_="ul">
  <c-bs-nav-item>
    <c-bs-nav-link c-active="True" href="#">Active</c-bs-nav-link>
  </c-bs-nav-item>
  <c-bs-nav-item>
    <c-bs-nav-link href="#">Much longer nav link</c-bs-nav-link>
  </c-bs-nav-item>
  <c-bs-nav-item>
    <c-bs-nav-link href="#">Link</c-bs-nav-link>
  </c-bs-nav-item>
  <c-bs-nav-item>
    <c-bs-nav-link c-disabled="True">Disabled</c-bs-nav-link>
  </c-bs-nav-item>
</c-bs-nav>
""")

    expected = """
        <ul class="nav nav-pills nav-fill">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="#">Active</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Much longer nav link</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Link</a>
          </li>
          <li class="nav-item">
            <a class="nav-link disabled" aria-disabled="true">Disabled</a>
          </li>
        </ul>
    """

    assert_html(rendered, expected)


def test_fill_nav_element(render, assert_html):
    rendered = render("""
<c-bs-nav variant="pills" c-fill="True">
  <c-bs-nav-link c-active="True" href="#">Active</c-bs-nav-link>
  <c-bs-nav-link href="#">Much longer nav link</c-bs-nav-link>
  <c-bs-nav-link href="#">Link</c-bs-nav-link>
  <c-bs-nav-link c-disabled="True">Disabled</c-bs-nav-link>
</c-bs-nav>
""")

    expected = """
        <nav class="nav nav-pills nav-fill">
          <a class="nav-link active" aria-current="page" href="#">Active</a>
          <a class="nav-link" href="#">Much longer nav link</a>
          <a class="nav-link" href="#">Link</a>
          <a class="nav-link disabled" aria-disabled="true">Disabled</a>
        </nav>
    """

    assert_html(rendered, expected)


def test_justified(render, assert_html):
    rendered = render("""
<c-bs-nav variant="pills" c-justified="True" as_="ul">
  <c-bs-nav-item>
    <c-bs-nav-link c-active="True" href="#">Active</c-bs-nav-link>
  </c-bs-nav-item>
  <c-bs-nav-item>
    <c-bs-nav-link href="#">Much longer nav link</c-bs-nav-link>
  </c-bs-nav-item>
  <c-bs-nav-item>
    <c-bs-nav-link href="#">Link</c-bs-nav-link>
  </c-bs-nav-item>
  <c-bs-nav-item>
    <c-bs-nav-link c-disabled="True">Disabled</c-bs-nav-link>
  </c-bs-nav-item>
</c-bs-nav>
""")

    expected = """
        <ul class="nav nav-pills nav-justified">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="#">Active</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Much longer nav link</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Link</a>
          </li>
          <li class="nav-item">
            <a class="nav-link disabled" aria-disabled="true">Disabled</a>
          </li>
        </ul>
    """

    assert_html(rendered, expected)


def test_justified_nav_element(render, assert_html):
    rendered = render("""
<c-bs-nav variant="pills" c-justified="True">
  <c-bs-nav-link c-active="True" href="#">Active</c-bs-nav-link>
  <c-bs-nav-link href="#">Much longer nav link</c-bs-nav-link>
  <c-bs-nav-link href="#">Link</c-bs-nav-link>
  <c-bs-nav-link c-disabled="True">Disabled</c-bs-nav-link>
</c-bs-nav>
""")

    expected = """
        <nav class="nav nav-pills nav-justified">
          <a class="nav-link active" aria-current="page" href="#">Active</a>
          <a class="nav-link" href="#">Much longer nav link</a>
          <a class="nav-link" href="#">Link</a>
          <a class="nav-link disabled" aria-disabled="true">Disabled</a>
        </nav>
    """

    assert_html(rendered, expected)


def test_button_links(render, assert_html):
    rendered = render("""
<c-bs-nav variant="pills" as_="ul">
  <c-bs-nav-item>
    <c-bs-nav-link as_="button" c-active="True">Active</c-bs-nav-link>
  </c-bs-nav-item>
  <c-bs-nav-item>
    <c-bs-nav-link as_="button">Link</c-bs-nav-link>
  </c-bs-nav-item>
  <c-bs-nav-item>
    <c-bs-nav-link as_="button">Link</c-bs-nav-link>
  </c-bs-nav-item>
  <c-bs-nav-item>
    <c-bs-nav-link as_="button" c-disabled="True">Disabled</c-bs-nav-link>
  </c-bs-nav-item>
</c-bs-nav>
""")

    expected = """
        <ul class="nav nav-pills">
          <li class="nav-item">
            <button type="button" class="nav-link active">Active</button>
          </li>
          <li class="nav-item">
            <button type="button" class="nav-link">Link</button>
          </li>
          <li class="nav-item">
            <button type="button" class="nav-link">Link</button>
          </li>
          <li class="nav-item">
            <button type="button" class="nav-link disabled" disabled>Disabled</button>
          </li>
        </ul>
    """

    assert_html(rendered, expected)


def test_custom_attrs(render, assert_html):
    rendered = render("""
<c-bs-nav c-attrs="{'class': 'custom-nav'}">
  <c-bs-nav-link c-active="True" href="#">Active</c-bs-nav-link>
  <c-bs-nav-link href="#">Link</c-bs-nav-link>
</c-bs-nav>
""")

    expected = """
        <nav class="nav custom-nav">
          <a class="nav-link active" aria-current="page" href="#">Active</a>
          <a class="nav-link" href="#">Link</a>
        </nav>
    """

    assert_html(rendered, expected)


def test_custom_role(render, assert_html):
    rendered = render("""
<c-bs-nav role="tablist">
  <c-bs-nav-link c-active="True" href="#">Active</c-bs-nav-link>
  <c-bs-nav-link href="#">Link</c-bs-nav-link>
</c-bs-nav>
""")

    expected = """
        <nav class="nav" role="tablist">
          <a class="nav-link active" aria-current="page" href="#">Active</a>
          <a class="nav-link" href="#">Link</a>
        </nav>
    """

    assert_html(rendered, expected)
