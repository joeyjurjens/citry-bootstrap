def test_basic(render, assert_html):
    rendered = render("""
<c-bs-breadcrumb>
  <c-bs-breadcrumb-item href="#">Home</c-bs-breadcrumb-item>
  <c-bs-breadcrumb-item c-active="True">Library</c-bs-breadcrumb-item>
</c-bs-breadcrumb>
""")

    expected = """
        <nav aria-label="breadcrumb">
          <ol class="breadcrumb">
            <li class="breadcrumb-item"><a href="#">Home</a></li>
            <li class="breadcrumb-item active" aria-current="page">Library</li>
          </ol>
        </nav>
    """

    assert_html(rendered, expected)


def test_single_item_active(render, assert_html):
    rendered = render("""
<c-bs-breadcrumb>
  <c-bs-breadcrumb-item c-active="True">Home</c-bs-breadcrumb-item>
</c-bs-breadcrumb>
""")

    expected = """
        <nav aria-label="breadcrumb">
          <ol class="breadcrumb">
            <li class="breadcrumb-item active" aria-current="page">Home</li>
          </ol>
        </nav>
    """

    assert_html(rendered, expected)


def test_three_items(render, assert_html):
    rendered = render("""
<c-bs-breadcrumb>
  <c-bs-breadcrumb-item href="#">Home</c-bs-breadcrumb-item>
  <c-bs-breadcrumb-item href="#">Library</c-bs-breadcrumb-item>
  <c-bs-breadcrumb-item c-active="True">Data</c-bs-breadcrumb-item>
</c-bs-breadcrumb>
""")

    expected = """
        <nav aria-label="breadcrumb">
          <ol class="breadcrumb">
            <li class="breadcrumb-item"><a href="#">Home</a></li>
            <li class="breadcrumb-item"><a href="#">Library</a></li>
            <li class="breadcrumb-item active" aria-current="page">Data</li>
          </ol>
        </nav>
    """

    assert_html(rendered, expected)


def test_custom_divider_greater_than(render, assert_html):
    rendered = render(r"""
<c-bs-breadcrumb c-attrs="{'style': '--bs-breadcrumb-divider: \'>\';'}">
  <c-bs-breadcrumb-item href="#">Home</c-bs-breadcrumb-item>
  <c-bs-breadcrumb-item c-active="True">Library</c-bs-breadcrumb-item>
</c-bs-breadcrumb>
""")

    expected = """
        <nav style="--bs-breadcrumb-divider: '>';" aria-label="breadcrumb">
          <ol class="breadcrumb">
            <li class="breadcrumb-item"><a href="#">Home</a></li>
            <li class="breadcrumb-item active" aria-current="page">Library</li>
          </ol>
        </nav>
    """

    assert_html(rendered, expected)


def test_no_divider(render, assert_html):
    rendered = render(r"""
<c-bs-breadcrumb c-attrs="{'style': '--bs-breadcrumb-divider: \'\';'}">
  <c-bs-breadcrumb-item href="#">Home</c-bs-breadcrumb-item>
  <c-bs-breadcrumb-item c-active="True">Library</c-bs-breadcrumb-item>
</c-bs-breadcrumb>
""")

    expected = """
        <nav style="--bs-breadcrumb-divider: '';" aria-label="breadcrumb">
          <ol class="breadcrumb">
            <li class="breadcrumb-item"><a href="#">Home</a></li>
            <li class="breadcrumb-item active" aria-current="page">Library</li>
          </ol>
        </nav>
    """

    assert_html(rendered, expected)


def test_custom_label(render, assert_html):
    rendered = render("""
<c-bs-breadcrumb>
  <c-bs-breadcrumb-item href="#">Home</c-bs-breadcrumb-item>
  <c-bs-breadcrumb-item c-active="True">Library</c-bs-breadcrumb-item>
</c-bs-breadcrumb>
""")

    expected = """
        <nav aria-label="breadcrumb">
          <ol class="breadcrumb">
            <li class="breadcrumb-item"><a href="#">Home</a></li>
            <li class="breadcrumb-item active" aria-current="page">Library</li>
          </ol>
        </nav>
    """

    assert_html(rendered, expected)


def test_custom_attrs(render, assert_html):
    rendered = render("""
<c-bs-breadcrumb c-attrs="{'class': 'custom-class'}">
  <c-bs-breadcrumb-item href="#">Home</c-bs-breadcrumb-item>
  <c-bs-breadcrumb-item c-active="True">Library</c-bs-breadcrumb-item>
</c-bs-breadcrumb>
""")

    expected = """
        <nav class="custom-class" aria-label="breadcrumb">
          <ol class="breadcrumb">
            <li class="breadcrumb-item"><a href="#">Home</a></li>
            <li class="breadcrumb-item active" aria-current="page">Library</li>
          </ol>
        </nav>
    """

    assert_html(rendered, expected)


def test_item_custom_attrs(render, assert_html):
    rendered = render("""
<c-bs-breadcrumb>
  <c-bs-breadcrumb-item href="#" c-attrs="{'data-test': 'home'}">Home</c-bs-breadcrumb-item>
  <c-bs-breadcrumb-item c-active="True" c-attrs="{'class': 'highlighted'}">Library</c-bs-breadcrumb-item>
</c-bs-breadcrumb>
""")

    expected = """
        <nav aria-label="breadcrumb">
          <ol class="breadcrumb">
            <li class="breadcrumb-item" data-test="home"><a href="#">Home</a></li>
            <li class="breadcrumb-item active highlighted" aria-current="page">Library</li>
          </ol>
        </nav>
    """

    assert_html(rendered, expected)
