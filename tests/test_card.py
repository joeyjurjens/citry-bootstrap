def test_basic_with_image(render, assert_html):
    rendered = render("""
<c-bs-card>
  <c-bs-card-img src="https://placehold.net/600x400.png" alt="Card image" position="top" />
  <c-bs-card-body>
    <c-bs-card-title>Card title</c-bs-card-title>
    <c-bs-card-text>Some quick example text to build on the card title and make up the bulk of the card's content.</c-bs-card-text>
    <c-bs-button href="#">Go somewhere</c-bs-button>
  </c-bs-card-body>
</c-bs-card>
""")

    expected = """
        <div class="card">
          <img src="https://placehold.net/600x400.png" class="card-img-top" alt="Card image">
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
            <a href="#" class="btn btn-primary" role="button">Go somewhere</a>
          </div>
        </div>
    """

    assert_html(rendered, expected)


def test_with_header_and_footer(render, assert_html):
    rendered = render("""
<c-bs-card text_align="center">
  <c-bs-card-header>Featured</c-bs-card-header>
  <c-bs-card-body>
    <c-bs-card-title>Special title treatment</c-bs-card-title>
    <c-bs-card-text>With supporting text below as a natural lead-in to additional content.</c-bs-card-text>
    <a href="#" class="btn btn-primary" role="button">Go somewhere</a>
  </c-bs-card-body>
  <c-bs-card-footer>2 days ago</c-bs-card-footer>
</c-bs-card>
""")

    expected = """
        <div class="card text-center">
          <div class="card-header">
            Featured
          </div>
          <div class="card-body">
            <h5 class="card-title">Special title treatment</h5>
            <p class="card-text">With supporting text below as a natural lead-in to additional content.</p>
            <a href="#" class="btn btn-primary" role="button">Go somewhere</a>
          </div>
          <div class="card-footer">
            2 days ago
          </div>
        </div>
    """

    assert_html(rendered, expected)


def test_with_image_cap(render, assert_html):
    rendered = render("""
<c-bs-card>
  <c-bs-card-img src="https://placehold.net/600x400.png" alt="Card image" position="top" />
  <c-bs-card-body>
    <c-bs-card-title>Card title</c-bs-card-title>
    <c-bs-card-text>This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</c-bs-card-text>
    <c-bs-card-text>
      <small class="text-body-secondary">Last updated 3 mins ago</small>
    </c-bs-card-text>
  </c-bs-card-body>
</c-bs-card>
""")

    expected = """
        <div class="card">
          <img src="https://placehold.net/600x400.png" class="card-img-top" alt="Card image">
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
            <p class="card-text"><small class="text-body-secondary">Last updated 3 mins ago</small></p>
          </div>
        </div>
    """

    assert_html(rendered, expected)


def test_body_only(render, assert_html):
    rendered = render("""
<c-bs-card>
  <c-bs-card-body>This is some text within a card body.</c-bs-card-body>
</c-bs-card>
""")

    expected = """
        <div class="card">
          <div class="card-body">
            This is some text within a card body.
          </div>
        </div>
    """

    assert_html(rendered, expected)


def test_with_title_subtitle_links(render, assert_html):
    rendered = render("""
<c-bs-card>
  <c-bs-card-body>
    <c-bs-card-title>Card title</c-bs-card-title>
    <c-bs-card-subtitle>Card subtitle</c-bs-card-subtitle>
    <c-bs-card-text>Some quick example text to build on the card title and make up the bulk of the card's content.</c-bs-card-text>
    <c-bs-card-link href="#">Card link</c-bs-card-link>
    <c-bs-card-link href="#">Another link</c-bs-card-link>
  </c-bs-card-body>
</c-bs-card>
""")

    expected = """
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <h6 class="card-subtitle">Card subtitle</h6>
            <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
            <a href="#" class="card-link">Card link</a>
            <a href="#" class="card-link">Another link</a>
          </div>
        </div>
    """

    assert_html(rendered, expected)


def test_with_image_bottom(render, assert_html):
    rendered = render("""
<c-bs-card>
  <c-bs-card-body>
    <c-bs-card-title>Card title</c-bs-card-title>
    <c-bs-card-text>This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</c-bs-card-text>
    <c-bs-card-text>
      <small class="text-body-secondary">Last updated 3 mins ago</small>
    </c-bs-card-text>
  </c-bs-card-body>
  <c-bs-card-img src="https://placehold.net/600x400.png" alt="Card image" position="bottom" />
</c-bs-card>
""")

    expected = """
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
            <p class="card-text"><small class="text-body-secondary">Last updated 3 mins ago</small></p>
          </div>
          <img src="https://placehold.net/600x400.png" class="card-img-bottom" alt="Card image">
        </div>
    """

    assert_html(rendered, expected)


def test_bg_primary(render, assert_html):
    rendered = render("""
<c-bs-card bg="primary" c-attrs='{"class": "mb-3", "style": "max-width: 18rem;"}'>
  <c-bs-card-header>Header</c-bs-card-header>
  <c-bs-card-body>
    <c-bs-card-title>Primary card title</c-bs-card-title>
    <c-bs-card-text>Some quick example text to build on the card title and make up the bulk of the card's content.</c-bs-card-text>
  </c-bs-card-body>
</c-bs-card>
""")

    expected = """
        <div class="card text-bg-primary mb-3" style="max-width: 18rem;">
          <div class="card-header">Header</div>
          <div class="card-body">
            <h5 class="card-title">Primary card title</h5>
            <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
          </div>
        </div>
    """

    assert_html(rendered, expected)


def test_bg_secondary(render, assert_html):
    rendered = render("""
<c-bs-card bg="secondary" c-attrs='{"class": "mb-3", "style": "max-width: 18rem;"}'>
  <c-bs-card-header>Header</c-bs-card-header>
  <c-bs-card-body>
    <c-bs-card-title>Secondary card title</c-bs-card-title>
    <c-bs-card-text>Some quick example text to build on the card title and make up the bulk of the card's content.</c-bs-card-text>
  </c-bs-card-body>
</c-bs-card>
""")

    expected = """
        <div class="card text-bg-secondary mb-3" style="max-width: 18rem;">
          <div class="card-header">Header</div>
          <div class="card-body">
            <h5 class="card-title">Secondary card title</h5>
            <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
          </div>
        </div>
    """

    assert_html(rendered, expected)


def test_bg_success(render, assert_html):
    rendered = render("""
<c-bs-card bg="success" c-attrs='{"class": "mb-3", "style": "max-width: 18rem;"}'>
  <c-bs-card-header>Header</c-bs-card-header>
  <c-bs-card-body>
    <c-bs-card-title>Success card title</c-bs-card-title>
    <c-bs-card-text>Some quick example text to build on the card title and make up the bulk of the card's content.</c-bs-card-text>
  </c-bs-card-body>
</c-bs-card>
""")

    expected = """
        <div class="card text-bg-success mb-3" style="max-width: 18rem;">
          <div class="card-header">Header</div>
          <div class="card-body">
            <h5 class="card-title">Success card title</h5>
            <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
          </div>
        </div>
    """

    assert_html(rendered, expected)


def test_bg_danger(render, assert_html):
    rendered = render("""
<c-bs-card bg="danger" c-attrs='{"class": "mb-3", "style": "max-width: 18rem;"}'>
  <c-bs-card-header>Header</c-bs-card-header>
  <c-bs-card-body>
    <c-bs-card-title>Danger card title</c-bs-card-title>
    <c-bs-card-text>Some quick example text to build on the card title and make up the bulk of the card's content.</c-bs-card-text>
  </c-bs-card-body>
</c-bs-card>
""")

    expected = """
        <div class="card text-bg-danger mb-3" style="max-width: 18rem;">
          <div class="card-header">Header</div>
          <div class="card-body">
            <h5 class="card-title">Danger card title</h5>
            <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
          </div>
        </div>
    """

    assert_html(rendered, expected)


def test_border_primary(render, assert_html):
    rendered = render("""
<c-bs-card border="primary" c-attrs='{"class": "mb-3", "style": "max-width: 18rem;"}'>
  <c-bs-card-header>Header</c-bs-card-header>
  <c-bs-card-body>
    <c-bs-card-title>Primary card title</c-bs-card-title>
    <c-bs-card-text>Some quick example text to build on the card title and make up the bulk of the card's content.</c-bs-card-text>
  </c-bs-card-body>
</c-bs-card>
""")

    expected = """
        <div class="card border-primary mb-3" style="max-width: 18rem;">
          <div class="card-header">Header</div>
          <div class="card-body">
            <h5 class="card-title">Primary card title</h5>
            <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
          </div>
        </div>
    """

    assert_html(rendered, expected)


def test_text_align_center(render, assert_html):
    rendered = render("""
<c-bs-card text_align="center" c-attrs='{"class": "mb-3", "style": "width: 18rem;"}'>
  <c-bs-card-body>
    <c-bs-card-title>Special title treatment</c-bs-card-title>
    <c-bs-card-text>With supporting text below as a natural lead-in to additional content.</c-bs-card-text>
    <c-bs-button href="#">Go somewhere</c-bs-button>
  </c-bs-card-body>
</c-bs-card>
""")

    expected = """
        <div class="card text-center mb-3" style="width: 18rem;">
          <div class="card-body">
            <h5 class="card-title">Special title treatment</h5>
            <p class="card-text">With supporting text below as a natural lead-in to additional content.</p>
            <a href="#" class="btn btn-primary" role="button">Go somewhere</a>
          </div>
        </div>
    """

    assert_html(rendered, expected)


def test_text_align_end(render, assert_html):
    rendered = render("""
<c-bs-card text_align="end">
  <c-bs-card-body>
    <c-bs-card-title>Special title treatment</c-bs-card-title>
    <c-bs-card-text>With supporting text below as a natural lead-in to additional content.</c-bs-card-text>
    <c-bs-button href="#">Go somewhere</c-bs-button>
  </c-bs-card-body>
</c-bs-card>
""")

    expected = """
        <div class="card text-end">
          <div class="card-body">
            <h5 class="card-title">Special title treatment</h5>
            <p class="card-text">With supporting text below as a natural lead-in to additional content.</p>
            <a href="#" class="btn btn-primary" role="button">Go somewhere</a>
          </div>
        </div>
    """

    assert_html(rendered, expected)
