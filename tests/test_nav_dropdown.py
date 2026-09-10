import re


def test_nav_dropdown_basic(render, assert_html):
    rendered = render("""
<c-bs-nav variant="tabs" as_="ul">
  <c-bs-nav-item>
    <c-bs-nav-link href="#" c-active="True">Active</c-bs-nav-link>
  </c-bs-nav-item>
  <c-bs-nav-dropdown title="Dropdown">
    <c-bs-dropdown-item href="#">Action</c-bs-dropdown-item>
    <c-bs-dropdown-item href="#">Another action</c-bs-dropdown-item>
    <c-bs-dropdown-item href="#">Something else here</c-bs-dropdown-item>
    <c-bs-dropdown-divider />
    <c-bs-dropdown-item href="#">Separated link</c-bs-dropdown-item>
  </c-bs-nav-dropdown>
  <c-bs-nav-item>
    <c-bs-nav-link href="#">Link</c-bs-nav-link>
  </c-bs-nav-item>
</c-bs-nav>
""")

    # Extract the auto-generated ID
    id_match = re.search(r'id="(nav-dropdown-[^"]+)"', rendered)
    assert id_match is not None
    dropdown_id = id_match.group(1)

    expected = f"""
        <ul class="nav nav-tabs">
            <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="#">Active</a>
            </li>
            <li class="nav-item dropdown">
                <button class="nav-link dropdown-toggle" type="button" id="{dropdown_id}" data-bs-toggle="dropdown" aria-expanded="false">Dropdown</button>
                <ul class="dropdown-menu">
                    <li><a class="dropdown-item" href="#">Action</a></li>
                    <li><a class="dropdown-item" href="#">Another action</a></li>
                    <li><a class="dropdown-item" href="#">Something else here</a></li>
                    <li><hr class="dropdown-divider"></li>
                    <li><a class="dropdown-item" href="#">Separated link</a></li>
                </ul>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="#">Link</a>
            </li>
        </ul>
    """

    assert_html(rendered, expected)


def test_nav_dropdown_disabled(render, assert_html):
    rendered = render("""
<c-bs-nav as_="ul">
  <c-bs-nav-dropdown title="Disabled Dropdown" c-disabled="True">
    <c-bs-dropdown-item href="#">Action</c-bs-dropdown-item>
  </c-bs-nav-dropdown>
</c-bs-nav>
""")

    # Extract the auto-generated ID
    id_match = re.search(r'id="(nav-dropdown-[^"]+)"', rendered)
    assert id_match is not None
    dropdown_id = id_match.group(1)

    expected = f"""
        <ul class="nav">
            <li class="nav-item dropdown">
                <button class="nav-link dropdown-toggle disabled" type="button" id="{dropdown_id}" data-bs-toggle="dropdown" aria-expanded="false" disabled>Disabled Dropdown</button>
                <ul class="dropdown-menu">
                    <li><a class="dropdown-item" href="#">Action</a></li>
                </ul>
            </li>
        </ul>
    """

    assert_html(rendered, expected)


def test_nav_dropdown_dark(render, assert_html):
    rendered = render("""
<c-bs-nav as_="ul">
  <c-bs-nav-dropdown title="Dark Dropdown" c-dark="True">
    <c-bs-dropdown-item href="#">Action</c-bs-dropdown-item>
  </c-bs-nav-dropdown>
</c-bs-nav>
""")

    # Extract the auto-generated ID
    id_match = re.search(r'id="(nav-dropdown-[^"]+)"', rendered)
    assert id_match is not None
    dropdown_id = id_match.group(1)

    expected = f"""
        <ul class="nav">
            <li class="nav-item dropdown">
                <button class="nav-link dropdown-toggle" type="button" id="{dropdown_id}" data-bs-toggle="dropdown" aria-expanded="false">Dark Dropdown</button>
                <ul class="dropdown-menu dropdown-menu-dark">
                    <li><a class="dropdown-item" href="#">Action</a></li>
                </ul>
            </li>
        </ul>
    """

    assert_html(rendered, expected)
