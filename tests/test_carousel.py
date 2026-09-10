def test_basic_with_controls(render, assert_html):
    rendered = render("""
<c-bs-carousel c-indicators="False">
  <c-bs-carousel-item c-active="True">
    <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide" />
  </c-bs-carousel-item>
  <c-bs-carousel-item>
    <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide" />
  </c-bs-carousel-item>
  <c-bs-carousel-item>
    <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide" />
  </c-bs-carousel-item>
</c-bs-carousel>
""")

    expected = """
        <div id="carousel-ctest01" class="carousel slide">
          <div class="carousel-inner">
            <div class="carousel-item active">
              <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
            </div>
            <div class="carousel-item">
              <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
            </div>
            <div class="carousel-item">
              <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
            </div>
          </div>
          <button class="carousel-control-prev" type="button" data-bs-target="#carousel-ctest01" data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
          </button>
          <button class="carousel-control-next" type="button" data-bs-target="#carousel-ctest01" data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
          </button>
        </div>
    """

    assert_html(rendered, expected)


def test_with_indicators(render, assert_html):
    rendered = render("""
<c-bs-carousel>
  <c-bs-carousel-item c-active="True">
    <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide" />
  </c-bs-carousel-item>
  <c-bs-carousel-item>
    <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide" />
  </c-bs-carousel-item>
  <c-bs-carousel-item>
    <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide" />
  </c-bs-carousel-item>
</c-bs-carousel>
""")

    expected = """
        <div id="carousel-ctest01" class="carousel slide">
          <div class="carousel-indicators">
            <button type="button" data-bs-target="#carousel-ctest01" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
            <button type="button" data-bs-target="#carousel-ctest01" data-bs-slide-to="1" aria-label="Slide 2"></button>
            <button type="button" data-bs-target="#carousel-ctest01" data-bs-slide-to="2" aria-label="Slide 3"></button>
          </div>
          <div class="carousel-inner">
            <div class="carousel-item active">
              <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
            </div>
            <div class="carousel-item">
              <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
            </div>
            <div class="carousel-item">
              <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
            </div>
          </div>
          <button class="carousel-control-prev" type="button" data-bs-target="#carousel-ctest01" data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
          </button>
          <button class="carousel-control-next" type="button" data-bs-target="#carousel-ctest01" data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
          </button>
        </div>
    """

    assert_html(rendered, expected)


def test_with_captions(render, assert_html):
    rendered = render("""
<c-bs-carousel>
  <c-bs-carousel-item c-active="True">
    <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide" />
    <c-bs-carousel-caption>
      <h5>First slide label</h5>
      <p>Some representative placeholder content for the first slide.</p>
    </c-bs-carousel-caption>
  </c-bs-carousel-item>
  <c-bs-carousel-item>
    <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide" />
    <c-bs-carousel-caption>
      <h5>Second slide label</h5>
      <p>Some representative placeholder content for the second slide.</p>
    </c-bs-carousel-caption>
  </c-bs-carousel-item>
  <c-bs-carousel-item>
    <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide" />
    <c-bs-carousel-caption>
      <h5>Third slide label</h5>
      <p>Some representative placeholder content for the third slide.</p>
    </c-bs-carousel-caption>
  </c-bs-carousel-item>
</c-bs-carousel>
""")

    expected = """
        <div id="carousel-ctest01" class="carousel slide">
          <div class="carousel-indicators">
            <button type="button" data-bs-target="#carousel-ctest01" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
            <button type="button" data-bs-target="#carousel-ctest01" data-bs-slide-to="1" aria-label="Slide 2"></button>
            <button type="button" data-bs-target="#carousel-ctest01" data-bs-slide-to="2" aria-label="Slide 3"></button>
          </div>
          <div class="carousel-inner">
            <div class="carousel-item active">
              <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
              <div class="carousel-caption">
                <h5>First slide label</h5>
                <p>Some representative placeholder content for the first slide.</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
              <div class="carousel-caption">
                <h5>Second slide label</h5>
                <p>Some representative placeholder content for the second slide.</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
              <div class="carousel-caption">
                <h5>Third slide label</h5>
                <p>Some representative placeholder content for the third slide.</p>
              </div>
            </div>
          </div>
          <button class="carousel-control-prev" type="button" data-bs-target="#carousel-ctest01" data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
          </button>
          <button class="carousel-control-next" type="button" data-bs-target="#carousel-ctest01" data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
          </button>
        </div>
    """

    assert_html(rendered, expected)


def test_crossfade(render, assert_html):
    rendered = render("""
<c-bs-carousel c-fade="True" c-indicators="False">
  <c-bs-carousel-item c-active="True">
    <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide" />
  </c-bs-carousel-item>
  <c-bs-carousel-item>
    <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide" />
  </c-bs-carousel-item>
  <c-bs-carousel-item>
    <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide" />
  </c-bs-carousel-item>
</c-bs-carousel>
""")

    expected = """
        <div id="carousel-ctest01" class="carousel slide carousel-fade">
          <div class="carousel-inner">
            <div class="carousel-item active">
              <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
            </div>
            <div class="carousel-item">
              <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
            </div>
            <div class="carousel-item">
              <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
            </div>
          </div>
          <button class="carousel-control-prev" type="button" data-bs-target="#carousel-ctest01" data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
          </button>
          <button class="carousel-control-next" type="button" data-bs-target="#carousel-ctest01" data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
          </button>
        </div>
    """

    assert_html(rendered, expected)


def test_autoplaying_carousel(render, assert_html):
    rendered = render("""
<c-bs-carousel ride="carousel" c-indicators="False">
  <c-bs-carousel-item c-active="True">
    <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide" />
  </c-bs-carousel-item>
  <c-bs-carousel-item>
    <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide" />
  </c-bs-carousel-item>
  <c-bs-carousel-item>
    <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide" />
  </c-bs-carousel-item>
</c-bs-carousel>
""")

    expected = """
        <div id="carousel-ctest01" class="carousel slide" data-bs-ride="carousel">
          <div class="carousel-inner">
            <div class="carousel-item active">
              <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
            </div>
            <div class="carousel-item">
              <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
            </div>
            <div class="carousel-item">
              <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
            </div>
          </div>
          <button class="carousel-control-prev" type="button" data-bs-target="#carousel-ctest01" data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
          </button>
          <button class="carousel-control-next" type="button" data-bs-target="#carousel-ctest01" data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
          </button>
        </div>
    """

    assert_html(rendered, expected)


def test_user_initiated_autoplay(render, assert_html):
    rendered = render("""
<c-bs-carousel ride="true" c-indicators="False">
  <c-bs-carousel-item c-active="True">
    <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide" />
  </c-bs-carousel-item>
  <c-bs-carousel-item>
    <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide" />
  </c-bs-carousel-item>
  <c-bs-carousel-item>
    <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide" />
  </c-bs-carousel-item>
</c-bs-carousel>
""")

    expected = """
        <div id="carousel-ctest01" class="carousel slide" data-bs-ride="true">
          <div class="carousel-inner">
            <div class="carousel-item active">
              <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
            </div>
            <div class="carousel-item">
              <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
            </div>
            <div class="carousel-item">
              <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
            </div>
          </div>
          <button class="carousel-control-prev" type="button" data-bs-target="#carousel-ctest01" data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
          </button>
          <button class="carousel-control-next" type="button" data-bs-target="#carousel-ctest01" data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
          </button>
        </div>
    """

    assert_html(rendered, expected)


def test_individual_item_intervals(render, assert_html):
    rendered = render("""
<c-bs-carousel ride="carousel" c-indicators="False">
  <c-bs-carousel-item c-active="True" c-interval="10000">
    <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide" />
  </c-bs-carousel-item>
  <c-bs-carousel-item c-interval="2000">
    <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide" />
  </c-bs-carousel-item>
  <c-bs-carousel-item>
    <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide" />
  </c-bs-carousel-item>
</c-bs-carousel>
""")

    expected = """
        <div id="carousel-ctest01" class="carousel slide" data-bs-ride="carousel">
          <div class="carousel-inner">
            <div class="carousel-item active" data-bs-interval="10000">
              <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
            </div>
            <div class="carousel-item" data-bs-interval="2000">
              <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
            </div>
            <div class="carousel-item">
              <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
            </div>
          </div>
          <button class="carousel-control-prev" type="button" data-bs-target="#carousel-ctest01" data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
          </button>
          <button class="carousel-control-next" type="button" data-bs-target="#carousel-ctest01" data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
          </button>
        </div>
    """

    assert_html(rendered, expected)


def test_slides_only_no_controls(render, assert_html):
    rendered = render("""
<c-bs-carousel ride="carousel" c-controls="False" c-indicators="False">
  <c-bs-carousel-item c-active="True">
    <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide" />
  </c-bs-carousel-item>
  <c-bs-carousel-item>
    <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide" />
  </c-bs-carousel-item>
  <c-bs-carousel-item>
    <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide" />
  </c-bs-carousel-item>
</c-bs-carousel>
""")

    expected = """
        <div id="carousel-ctest01" class="carousel slide" data-bs-ride="carousel">
          <div class="carousel-inner">
            <div class="carousel-item active">
              <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
            </div>
            <div class="carousel-item">
              <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
            </div>
            <div class="carousel-item">
              <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
            </div>
          </div>
        </div>
    """

    assert_html(rendered, expected)


def test_disabled_touch_swiping(render, assert_html):
    rendered = render("""
<c-bs-carousel c-touch="False" c-indicators="False">
  <c-bs-carousel-item c-active="True">
    <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide" />
  </c-bs-carousel-item>
  <c-bs-carousel-item>
    <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide" />
  </c-bs-carousel-item>
  <c-bs-carousel-item>
    <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide" />
  </c-bs-carousel-item>
</c-bs-carousel>
""")

    expected = """
        <div id="carousel-ctest01" class="carousel slide" data-bs-touch="false">
          <div class="carousel-inner">
            <div class="carousel-item active">
              <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
            </div>
            <div class="carousel-item">
              <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
            </div>
            <div class="carousel-item">
              <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
            </div>
          </div>
          <button class="carousel-control-prev" type="button" data-bs-target="#carousel-ctest01" data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
          </button>
          <button class="carousel-control-next" type="button" data-bs-target="#carousel-ctest01" data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
          </button>
        </div>
    """

    assert_html(rendered, expected)


def test_dark_variant(render, assert_html):
    rendered = render("""
<c-bs-carousel theme="dark">
  <c-bs-carousel-item c-active="True" c-interval="10000">
    <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide" />
    <c-bs-carousel-caption>
      <h5>First slide label</h5>
      <p>Some representative placeholder content for the first slide.</p>
    </c-bs-carousel-caption>
  </c-bs-carousel-item>
  <c-bs-carousel-item c-interval="2000">
    <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide" />
    <c-bs-carousel-caption>
      <h5>Second slide label</h5>
      <p>Some representative placeholder content for the second slide.</p>
    </c-bs-carousel-caption>
  </c-bs-carousel-item>
  <c-bs-carousel-item>
    <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide" />
    <c-bs-carousel-caption>
      <h5>Third slide label</h5>
      <p>Some representative placeholder content for the third slide.</p>
    </c-bs-carousel-caption>
  </c-bs-carousel-item>
</c-bs-carousel>
""")

    expected = """
        <div id="carousel-ctest01" class="carousel slide" data-bs-theme="dark">
          <div class="carousel-indicators">
            <button type="button" data-bs-target="#carousel-ctest01" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
            <button type="button" data-bs-target="#carousel-ctest01" data-bs-slide-to="1" aria-label="Slide 2"></button>
            <button type="button" data-bs-target="#carousel-ctest01" data-bs-slide-to="2" aria-label="Slide 3"></button>
          </div>
          <div class="carousel-inner">
            <div class="carousel-item active" data-bs-interval="10000">
              <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
              <div class="carousel-caption">
                <h5>First slide label</h5>
                <p>Some representative placeholder content for the first slide.</p>
              </div>
            </div>
            <div class="carousel-item" data-bs-interval="2000">
              <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
              <div class="carousel-caption">
                <h5>Second slide label</h5>
                <p>Some representative placeholder content for the second slide.</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
              <div class="carousel-caption">
                <h5>Third slide label</h5>
                <p>Some representative placeholder content for the third slide.</p>
              </div>
            </div>
          </div>
          <button class="carousel-control-prev" type="button" data-bs-target="#carousel-ctest01" data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
          </button>
          <button class="carousel-control-next" type="button" data-bs-target="#carousel-ctest01" data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
          </button>
        </div>
    """

    assert_html(rendered, expected)
