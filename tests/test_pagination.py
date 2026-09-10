def test_basic(render, assert_html):
    rendered = render("""
<c-bs-pagination>
  <c-bs-pagination-item href="#">Previous</c-bs-pagination-item>
  <c-bs-pagination-item href="#">1</c-bs-pagination-item>
  <c-bs-pagination-item href="#">2</c-bs-pagination-item>
  <c-bs-pagination-item href="#">3</c-bs-pagination-item>
  <c-bs-pagination-item href="#">Next</c-bs-pagination-item>
</c-bs-pagination>
""")

    expected = """
        <nav aria-label="Page navigation">
          <ul class="pagination">
            <li class="page-item"><a class="page-link" href="#">Previous</a></li>
            <li class="page-item"><a class="page-link" href="#">1</a></li>
            <li class="page-item"><a class="page-link" href="#">2</a></li>
            <li class="page-item"><a class="page-link" href="#">3</a></li>
            <li class="page-item"><a class="page-link" href="#">Next</a></li>
          </ul>
        </nav>
    """

    assert_html(rendered, expected)


def test_with_icons(render, assert_html):
    rendered = render("""
<c-bs-pagination>
  <c-bs-pagination-item href="#" aria_label="Previous">
    <span aria-hidden="true">&laquo;</span>
  </c-bs-pagination-item>
  <c-bs-pagination-item href="#">1</c-bs-pagination-item>
  <c-bs-pagination-item href="#">2</c-bs-pagination-item>
  <c-bs-pagination-item href="#">3</c-bs-pagination-item>
  <c-bs-pagination-item href="#" aria_label="Next">
    <span aria-hidden="true">&raquo;</span>
  </c-bs-pagination-item>
</c-bs-pagination>
""")

    expected = """
        <nav aria-label="Page navigation">
          <ul class="pagination">
            <li class="page-item">
              <a class="page-link" href="#" aria-label="Previous">
                <span aria-hidden="true">&laquo;</span>
              </a>
            </li>
            <li class="page-item"><a class="page-link" href="#">1</a></li>
            <li class="page-item"><a class="page-link" href="#">2</a></li>
            <li class="page-item"><a class="page-link" href="#">3</a></li>
            <li class="page-item">
              <a class="page-link" href="#" aria-label="Next">
                <span aria-hidden="true">&raquo;</span>
              </a>
            </li>
          </ul>
        </nav>
    """

    assert_html(rendered, expected)


def test_active_state(render, assert_html):
    rendered = render("""
<c-bs-pagination>
  <c-bs-pagination-item href="#">Previous</c-bs-pagination-item>
  <c-bs-pagination-item href="#">1</c-bs-pagination-item>
  <c-bs-pagination-item href="#" c-active="True">2</c-bs-pagination-item>
  <c-bs-pagination-item href="#">3</c-bs-pagination-item>
  <c-bs-pagination-item href="#">Next</c-bs-pagination-item>
</c-bs-pagination>
""")

    expected = """
        <nav aria-label="Page navigation">
          <ul class="pagination">
            <li class="page-item"><a href="#" class="page-link">Previous</a></li>
            <li class="page-item"><a class="page-link" href="#">1</a></li>
            <li class="page-item active">
              <a class="page-link" href="#" aria-current="page">2</a>
            </li>
            <li class="page-item"><a class="page-link" href="#">3</a></li>
            <li class="page-item"><a class="page-link" href="#">Next</a></li>
          </ul>
        </nav>
    """

    assert_html(rendered, expected)


def test_disabled_state(render, assert_html):
    rendered = render("""
<c-bs-pagination>
  <c-bs-pagination-item c-disabled="True">Previous</c-bs-pagination-item>
  <c-bs-pagination-item href="#">1</c-bs-pagination-item>
  <c-bs-pagination-item href="#" c-active="True">2</c-bs-pagination-item>
  <c-bs-pagination-item href="#">3</c-bs-pagination-item>
  <c-bs-pagination-item href="#">Next</c-bs-pagination-item>
</c-bs-pagination>
""")

    expected = """
        <nav aria-label="Page navigation">
          <ul class="pagination">
            <li class="page-item disabled">
              <a class="page-link" href="#" tabindex="-1" aria-disabled="true">Previous</a>
            </li>
            <li class="page-item"><a class="page-link" href="#">1</a></li>
            <li class="page-item active">
              <a class="page-link" href="#" aria-current="page">2</a>
            </li>
            <li class="page-item"><a class="page-link" href="#">3</a></li>
            <li class="page-item"><a class="page-link" href="#">Next</a></li>
          </ul>
        </nav>
    """

    assert_html(rendered, expected)


def test_large_sizing(render, assert_html):
    rendered = render("""
<c-bs-pagination size="lg">
  <c-bs-pagination-item c-active="True">1</c-bs-pagination-item>
  <c-bs-pagination-item href="#">2</c-bs-pagination-item>
  <c-bs-pagination-item href="#">3</c-bs-pagination-item>
</c-bs-pagination>
""")

    expected = """
        <nav aria-label="Page navigation">
          <ul class="pagination pagination-lg">
            <li class="page-item active">
              <a class="page-link" href="#" aria-current="page">1</a>
            </li>
            <li class="page-item"><a class="page-link" href="#">2</a></li>
            <li class="page-item"><a class="page-link" href="#">3</a></li>
          </ul>
        </nav>
    """

    assert_html(rendered, expected)


def test_small_sizing(render, assert_html):
    rendered = render("""
<c-bs-pagination size="sm">
  <c-bs-pagination-item c-active="True">1</c-bs-pagination-item>
  <c-bs-pagination-item href="#">2</c-bs-pagination-item>
  <c-bs-pagination-item href="#">3</c-bs-pagination-item>
</c-bs-pagination>
""")

    expected = """
        <nav aria-label="Page navigation">
          <ul class="pagination pagination-sm">
            <li class="page-item active">
              <a class="page-link" href="#" aria-current="page">1</a>
            </li>
            <li class="page-item"><a class="page-link" href="#">2</a></li>
            <li class="page-item"><a class="page-link" href="#">3</a></li>
          </ul>
        </nav>
    """

    assert_html(rendered, expected)


def test_centered_alignment(render, assert_html):
    rendered = render("""
<c-bs-pagination c-ul_attrs="{'class': 'justify-content-center'}">
  <c-bs-pagination-item c-disabled="True">Previous</c-bs-pagination-item>
  <c-bs-pagination-item href="#">1</c-bs-pagination-item>
  <c-bs-pagination-item href="#">2</c-bs-pagination-item>
  <c-bs-pagination-item href="#">3</c-bs-pagination-item>
  <c-bs-pagination-item href="#">Next</c-bs-pagination-item>
</c-bs-pagination>
""")

    expected = """
        <nav aria-label="Page navigation">
          <ul class="pagination justify-content-center">
            <li class="page-item disabled">
              <a class="page-link" href="#" tabindex="-1" aria-disabled="true">Previous</a>
            </li>
            <li class="page-item"><a class="page-link" href="#">1</a></li>
            <li class="page-item"><a class="page-link" href="#">2</a></li>
            <li class="page-item"><a class="page-link" href="#">3</a></li>
            <li class="page-item"><a class="page-link" href="#">Next</a></li>
          </ul>
        </nav>
    """

    assert_html(rendered, expected)


def test_right_alignment(render, assert_html):
    rendered = render("""
<c-bs-pagination c-ul_attrs="{'class': 'justify-content-end'}">
  <c-bs-pagination-item c-disabled="True">Previous</c-bs-pagination-item>
  <c-bs-pagination-item href="#">1</c-bs-pagination-item>
  <c-bs-pagination-item href="#">2</c-bs-pagination-item>
  <c-bs-pagination-item href="#">3</c-bs-pagination-item>
  <c-bs-pagination-item href="#">Next</c-bs-pagination-item>
</c-bs-pagination>
""")

    expected = """
        <nav aria-label="Page navigation">
          <ul class="pagination justify-content-end">
            <li class="page-item disabled">
              <a class="page-link" href="#" tabindex="-1" aria-disabled="true">Previous</a>
            </li>
            <li class="page-item"><a class="page-link" href="#">1</a></li>
            <li class="page-item"><a class="page-link" href="#">2</a></li>
            <li class="page-item"><a class="page-link" href="#">3</a></li>
            <li class="page-item"><a class="page-link" href="#">Next</a></li>
          </ul>
        </nav>
    """

    assert_html(rendered, expected)
