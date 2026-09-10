def test_basic_container(render, assert_html):
    rendered = render("""
<c-bs-container>Content</c-bs-container>
""")

    expected = """
        <div class="container">
            Content
        </div>
    """

    assert_html(rendered, expected)


def test_container_fluid(render, assert_html):
    rendered = render("""
<c-bs-container c-fluid="True">Content</c-bs-container>
""")

    expected = """
        <div class="container-fluid">
            Content
        </div>
    """

    assert_html(rendered, expected)


def test_container_fluid_breakpoint(render, assert_html):
    rendered = render("""
<c-bs-container fluid="md">Content</c-bs-container>
""")

    expected = """
        <div class="container-md">
            Content
        </div>
    """

    assert_html(rendered, expected)


def test_basic_row_with_cols(render, assert_html):
    rendered = render("""
<c-bs-container>
  <c-bs-row>
    <c-bs-col>Column</c-bs-col>
    <c-bs-col>Column</c-bs-col>
    <c-bs-col>Column</c-bs-col>
  </c-bs-row>
</c-bs-container>
""")

    expected = """
        <div class="container">
            <div class="row">
                <div class="col">Column</div>
                <div class="col">Column</div>
                <div class="col">Column</div>
            </div>
        </div>
    """

    assert_html(rendered, expected)


def test_responsive_columns(render, assert_html):
    rendered = render("""
<c-bs-container>
  <c-bs-row>
    <c-bs-col c-sm="8">col-sm-8</c-bs-col>
    <c-bs-col c-sm="4">col-sm-4</c-bs-col>
  </c-bs-row>
</c-bs-container>
""")

    expected = """
        <div class="container">
            <div class="row">
                <div class="col-sm-8">col-sm-8</div>
                <div class="col-sm-4">col-sm-4</div>
            </div>
        </div>
    """

    assert_html(rendered, expected)


def test_mixed_responsive_columns(render, assert_html):
    rendered = render("""
<c-bs-container>
  <c-bs-row>
    <c-bs-col c-md="8">.col-md-8</c-bs-col>
    <c-bs-col c-col="6" c-md="4">.col-6 .col-md-4</c-bs-col>
  </c-bs-row>
</c-bs-container>
""")

    expected = """
        <div class="container">
            <div class="row">
                <div class="col-md-8">.col-md-8</div>
                <div class="col-6 col-md-4">.col-6 .col-md-4</div>
            </div>
        </div>
    """

    assert_html(rendered, expected)


def test_row_with_gutters(render, assert_html):
    rendered = render("""
<c-bs-container>
  <c-bs-row c-gutter="3">
    <c-bs-col>Column</c-bs-col>
    <c-bs-col>Column</c-bs-col>
  </c-bs-row>
</c-bs-container>
""")

    expected = """
        <div class="container">
            <div class="row g-3">
                <div class="col">Column</div>
                <div class="col">Column</div>
            </div>
        </div>
    """

    assert_html(rendered, expected)


def test_row_cols(render, assert_html):
    rendered = render("""
<c-bs-container>
  <c-bs-row c-cols="2">
    <c-bs-col>Column</c-bs-col>
    <c-bs-col>Column</c-bs-col>
    <c-bs-col>Column</c-bs-col>
    <c-bs-col>Column</c-bs-col>
  </c-bs-row>
</c-bs-container>
""")

    expected = """
        <div class="container">
            <div class="row row-cols-2">
                <div class="col">Column</div>
                <div class="col">Column</div>
                <div class="col">Column</div>
                <div class="col">Column</div>
            </div>
        </div>
    """

    assert_html(rendered, expected)


def test_col_auto(render, assert_html):
    rendered = render("""
<c-bs-container>
  <c-bs-row>
    <c-bs-col>1 of 3</c-bs-col>
    <c-bs-col col="auto">Variable width content</c-bs-col>
    <c-bs-col>3 of 3</c-bs-col>
  </c-bs-row>
</c-bs-container>
""")

    expected = """
        <div class="container">
            <div class="row">
                <div class="col">1 of 3</div>
                <div class="col-auto">Variable width content</div>
                <div class="col">3 of 3</div>
            </div>
        </div>
    """

    assert_html(rendered, expected)
