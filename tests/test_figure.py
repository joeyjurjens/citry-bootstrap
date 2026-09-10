def test_basic(render, assert_html):
    rendered = render("""
<c-bs-figure>
  <c-bs-figure-image src="https://placehold.net/600x400.png" alt="Figure image" />
  <c-bs-figure-caption>A caption for the above image.</c-bs-figure-caption>
</c-bs-figure>
""")

    expected = """
        <figure class="figure">
          <img src="https://placehold.net/600x400.png" class="figure-img img-fluid" alt="Figure image">
          <figcaption class="figure-caption">A caption for the above image.</figcaption>
        </figure>
    """

    assert_html(rendered, expected)


def test_caption_right_aligned(render, assert_html):
    rendered = render("""
<c-bs-figure>
  <c-bs-figure-image src="https://placehold.net/600x400.png" alt="Figure image" />
  <c-bs-figure-caption>A caption for the above image.</c-bs-figure-caption>
</c-bs-figure>
""")

    expected = """
        <figure class="figure">
          <img src="https://placehold.net/600x400.png" class="figure-img img-fluid" alt="Figure image">
          <figcaption class="figure-caption">A caption for the above image.</figcaption>
        </figure>
    """

    assert_html(rendered, expected)


def test_caption_center_aligned(render, assert_html):
    rendered = render("""
<c-bs-figure>
  <c-bs-figure-image src="https://placehold.net/600x400.png" alt="Figure image" />
  <c-bs-figure-caption>A caption for the above image.</c-bs-figure-caption>
</c-bs-figure>
""")

    expected = """
        <figure class="figure">
          <img src="https://placehold.net/600x400.png" class="figure-img img-fluid" alt="Figure image">
          <figcaption class="figure-caption">A caption for the above image.</figcaption>
        </figure>
    """

    assert_html(rendered, expected)


def test_without_rounded(render, assert_html):
    rendered = render("""
<c-bs-figure>
  <c-bs-figure-image src="https://placehold.net/600x400.png" alt="Figure image" />
  <c-bs-figure-caption>A caption for the above image.</c-bs-figure-caption>
</c-bs-figure>
""")

    expected = """
        <figure class="figure">
          <img src="https://placehold.net/600x400.png" class="figure-img img-fluid" alt="Figure image">
          <figcaption class="figure-caption">A caption for the above image.</figcaption>
        </figure>
    """

    assert_html(rendered, expected)


def test_not_fluid(render, assert_html):
    rendered = render("""
<c-bs-figure>
  <c-bs-figure-image src="https://placehold.net/600x400.png" alt="Figure image" c-fluid="False" />
  <c-bs-figure-caption>A caption for the above image.</c-bs-figure-caption>
</c-bs-figure>
""")

    expected = """
        <figure class="figure">
          <img src="https://placehold.net/600x400.png" class="figure-img" alt="Figure image">
          <figcaption class="figure-caption">A caption for the above image.</figcaption>
        </figure>
    """

    assert_html(rendered, expected)
