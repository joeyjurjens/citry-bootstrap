def test_basic(render, assert_html):
    rendered = render("""
<c-bs-offcanvas c-scroll="False" c-keyboard="False">
  <c-fill name="toggle">
    <c-bs-offcanvas-toggle c-attrs='{"class": "btn btn-primary", "type": "button"}'>Toggle Offcanvas</c-bs-offcanvas-toggle>
  </c-fill>
  <c-fill name="default">
    <c-bs-offcanvas-header>
      <c-bs-offcanvas-title>Offcanvas</c-bs-offcanvas-title>
    </c-bs-offcanvas-header>
    <c-bs-offcanvas-body>Content for the offcanvas goes here. You can place just about any Bootstrap component or custom elements here.</c-bs-offcanvas-body>
  </c-fill>
</c-bs-offcanvas>
""")

    expected = """
        <button type="button" class="btn btn-primary" data-bs-toggle="offcanvas" data-bs-target="#offcanvas-ctest01" aria-controls="offcanvas-ctest01">Toggle Offcanvas</button>
        <div class="offcanvas offcanvas-start" tabindex="-1" id="offcanvas-ctest01" aria-labelledby="offcanvas-ctest01-label" data-bs-keyboard="false">
          <div class="offcanvas-header">
            <h5 class="offcanvas-title" id="offcanvas-ctest01-label">Offcanvas</h5>
            <button type="button" class="btn-close" data-bs-dismiss="offcanvas" data-bs-target="#offcanvas-ctest01" aria-label="Close"></button>
          </div>
          <div class="offcanvas-body">
            Content for the offcanvas goes here. You can place just about any Bootstrap component or custom elements here.
          </div>
        </div>
    """

    assert_html(rendered, expected)


def test_offcanvas_placement_start(render, assert_html):
    rendered = render("""
<c-bs-offcanvas placement="start">
  <c-fill name="toggle">
    <c-bs-offcanvas-toggle c-attrs="{'class': 'btn btn-primary'}">Toggle Offcanvas</c-bs-offcanvas-toggle>
  </c-fill>
  <c-fill name="default">
    <c-bs-offcanvas-header>
      <c-bs-offcanvas-title>Offcanvas Start</c-bs-offcanvas-title>
    </c-bs-offcanvas-header>
    <c-bs-offcanvas-body>
      <p>This offcanvas appears from the start (left).</p>
    </c-bs-offcanvas-body>
  </c-fill>
</c-bs-offcanvas>
""")

    expected = """
        <button class="btn btn-primary" data-bs-toggle="offcanvas" data-bs-target="#offcanvas-ctest01" aria-controls="offcanvas-ctest01">Toggle Offcanvas</button>
        <div class="offcanvas offcanvas-start" tabindex="-1" id="offcanvas-ctest01" aria-labelledby="offcanvas-ctest01-label">
          <div class="offcanvas-header">
            <h5 class="offcanvas-title" id="offcanvas-ctest01-label">Offcanvas Start</h5>
            <button type="button" class="btn-close" data-bs-dismiss="offcanvas" data-bs-target="#offcanvas-ctest01" aria-label="Close"></button>
          </div>
          <div class="offcanvas-body">
            <p>This offcanvas appears from the start (left).</p>
          </div>
        </div>
    """

    assert_html(rendered, expected)


def test_offcanvas_placement_end(render, assert_html):
    rendered = render("""
<c-bs-offcanvas placement="end">
  <c-fill name="toggle">
    <c-bs-offcanvas-toggle c-attrs="{'class': 'btn btn-primary'}">Toggle Offcanvas</c-bs-offcanvas-toggle>
  </c-fill>
  <c-fill name="default">
    <c-bs-offcanvas-header>
      <c-bs-offcanvas-title>Offcanvas End</c-bs-offcanvas-title>
    </c-bs-offcanvas-header>
    <c-bs-offcanvas-body>
      <p>This offcanvas appears from the end (right).</p>
    </c-bs-offcanvas-body>
  </c-fill>
</c-bs-offcanvas>
""")

    expected = """
        <button class="btn btn-primary" data-bs-toggle="offcanvas" data-bs-target="#offcanvas-ctest01" aria-controls="offcanvas-ctest01">Toggle Offcanvas</button>
        <div class="offcanvas offcanvas-end" tabindex="-1" id="offcanvas-ctest01" aria-labelledby="offcanvas-ctest01-label">
          <div class="offcanvas-header">
            <h5 class="offcanvas-title" id="offcanvas-ctest01-label">Offcanvas End</h5>
            <button type="button" class="btn-close" data-bs-dismiss="offcanvas" data-bs-target="#offcanvas-ctest01" aria-label="Close"></button>
          </div>
          <div class="offcanvas-body">
            <p>This offcanvas appears from the end (right).</p>
          </div>
        </div>
    """

    assert_html(rendered, expected)


def test_offcanvas_placement_top(render, assert_html):
    rendered = render("""
<c-bs-offcanvas placement="top">
  <c-fill name="toggle">
    <c-bs-offcanvas-toggle c-attrs="{'class': 'btn btn-primary'}">Toggle Offcanvas</c-bs-offcanvas-toggle>
  </c-fill>
  <c-fill name="default">
    <c-bs-offcanvas-header>
      <c-bs-offcanvas-title>Offcanvas Top</c-bs-offcanvas-title>
    </c-bs-offcanvas-header>
    <c-bs-offcanvas-body>
      <p>This offcanvas appears from the top.</p>
    </c-bs-offcanvas-body>
  </c-fill>
</c-bs-offcanvas>
""")

    expected = """
        <button class="btn btn-primary" data-bs-toggle="offcanvas" data-bs-target="#offcanvas-ctest01" aria-controls="offcanvas-ctest01">Toggle Offcanvas</button>
        <div class="offcanvas offcanvas-top" tabindex="-1" id="offcanvas-ctest01" aria-labelledby="offcanvas-ctest01-label">
          <div class="offcanvas-header">
            <h5 class="offcanvas-title" id="offcanvas-ctest01-label">Offcanvas Top</h5>
            <button type="button" class="btn-close" data-bs-dismiss="offcanvas" data-bs-target="#offcanvas-ctest01" aria-label="Close"></button>
          </div>
          <div class="offcanvas-body">
            <p>This offcanvas appears from the top.</p>
          </div>
        </div>
    """

    assert_html(rendered, expected)


def test_offcanvas_placement_bottom(render, assert_html):
    rendered = render("""
<c-bs-offcanvas placement="bottom">
  <c-fill name="toggle">
    <c-bs-offcanvas-toggle c-attrs="{'class': 'btn btn-primary'}">Toggle Offcanvas</c-bs-offcanvas-toggle>
  </c-fill>
  <c-fill name="default">
    <c-bs-offcanvas-header>
      <c-bs-offcanvas-title>Offcanvas Bottom</c-bs-offcanvas-title>
    </c-bs-offcanvas-header>
    <c-bs-offcanvas-body>
      <p>This offcanvas appears from the bottom.</p>
    </c-bs-offcanvas-body>
  </c-fill>
</c-bs-offcanvas>
""")

    expected = """
        <button class="btn btn-primary" data-bs-toggle="offcanvas" data-bs-target="#offcanvas-ctest01" aria-controls="offcanvas-ctest01">Toggle Offcanvas</button>
        <div class="offcanvas offcanvas-bottom" tabindex="-1" id="offcanvas-ctest01" aria-labelledby="offcanvas-ctest01-label">
          <div class="offcanvas-header">
            <h5 class="offcanvas-title" id="offcanvas-ctest01-label">Offcanvas Bottom</h5>
            <button type="button" class="btn-close" data-bs-dismiss="offcanvas" data-bs-target="#offcanvas-ctest01" aria-label="Close"></button>
          </div>
          <div class="offcanvas-body">
            <p>This offcanvas appears from the bottom.</p>
          </div>
        </div>
    """

    assert_html(rendered, expected)


def test_offcanvas_body_scrolling_enabled(render, assert_html):
    rendered = render("""
<c-bs-offcanvas c-scroll="True" backdrop="false">
  <c-fill name="toggle">
    <c-bs-offcanvas-toggle c-attrs="{'class': 'btn btn-primary'}">Toggle Offcanvas</c-bs-offcanvas-toggle>
  </c-fill>
  <c-fill name="default">
    <c-bs-offcanvas-header>
      <c-bs-offcanvas-title>Offcanvas with body scrolling</c-bs-offcanvas-title>
    </c-bs-offcanvas-header>
    <c-bs-offcanvas-body>
      <p>Try scrolling the rest of the page to see this option in action.</p>
    </c-bs-offcanvas-body>
  </c-fill>
</c-bs-offcanvas>
""")

    expected = """
        <button class="btn btn-primary" data-bs-toggle="offcanvas" data-bs-target="#offcanvas-ctest01" aria-controls="offcanvas-ctest01">Toggle Offcanvas</button>
        <div class="offcanvas offcanvas-start" tabindex="-1" id="offcanvas-ctest01" aria-labelledby="offcanvas-ctest01-label" data-bs-backdrop="false" data-bs-scroll="true">
          <div class="offcanvas-header">
            <h5 class="offcanvas-title" id="offcanvas-ctest01-label">Offcanvas with body scrolling</h5>
            <button type="button" class="btn-close" data-bs-dismiss="offcanvas" data-bs-target="#offcanvas-ctest01" aria-label="Close"></button>
          </div>
          <div class="offcanvas-body">
            <p>Try scrolling the rest of the page to see this option in action.</p>
          </div>
        </div>
    """

    assert_html(rendered, expected)


def test_offcanvas_with_backdrop(render, assert_html):
    rendered = render("""
<c-bs-offcanvas c-scroll="True">
  <c-fill name="toggle">
    <c-bs-offcanvas-toggle c-attrs="{'class': 'btn btn-primary'}">Toggle Offcanvas</c-bs-offcanvas-toggle>
  </c-fill>
  <c-fill name="default">
    <c-bs-offcanvas-header>
      <c-bs-offcanvas-title>Backdrop with scrolling</c-bs-offcanvas-title>
    </c-bs-offcanvas-header>
    <c-bs-offcanvas-body>
      <p>Try scrolling the rest of the page to see this option in action.</p>
    </c-bs-offcanvas-body>
  </c-fill>
</c-bs-offcanvas>
""")

    expected = """
        <button class="btn btn-primary" data-bs-toggle="offcanvas" data-bs-target="#offcanvas-ctest01" aria-controls="offcanvas-ctest01">Toggle Offcanvas</button>
        <div class="offcanvas offcanvas-start" tabindex="-1" id="offcanvas-ctest01" aria-labelledby="offcanvas-ctest01-label" data-bs-scroll="true">
          <div class="offcanvas-header">
            <h5 class="offcanvas-title" id="offcanvas-ctest01-label">Backdrop with scrolling</h5>
            <button type="button" class="btn-close" data-bs-dismiss="offcanvas" data-bs-target="#offcanvas-ctest01" aria-label="Close"></button>
          </div>
          <div class="offcanvas-body">
            <p>Try scrolling the rest of the page to see this option in action.</p>
          </div>
        </div>
    """

    assert_html(rendered, expected)


def test_offcanvas_static_backdrop(render, assert_html):
    rendered = render("""
<c-bs-offcanvas backdrop="static">
  <c-fill name="toggle">
    <c-bs-offcanvas-toggle c-attrs="{'class': 'btn btn-primary'}">Toggle Offcanvas</c-bs-offcanvas-toggle>
  </c-fill>
  <c-fill name="default">
    <c-bs-offcanvas-header>
      <c-bs-offcanvas-title>Static Backdrop</c-bs-offcanvas-title>
    </c-bs-offcanvas-header>
    <c-bs-offcanvas-body>
      <p>I will not close if you click outside of me.</p>
    </c-bs-offcanvas-body>
  </c-fill>
</c-bs-offcanvas>
""")

    expected = """
        <button class="btn btn-primary" data-bs-toggle="offcanvas" data-bs-target="#offcanvas-ctest01" aria-controls="offcanvas-ctest01">Toggle Offcanvas</button>
        <div class="offcanvas offcanvas-start" tabindex="-1" id="offcanvas-ctest01" aria-labelledby="offcanvas-ctest01-label" data-bs-backdrop="static">
          <div class="offcanvas-header">
            <h5 class="offcanvas-title" id="offcanvas-ctest01-label">Static Backdrop</h5>
            <button type="button" class="btn-close" data-bs-dismiss="offcanvas" data-bs-target="#offcanvas-ctest01" aria-label="Close"></button>
          </div>
          <div class="offcanvas-body">
            <p>I will not close if you click outside of me.</p>
          </div>
        </div>
    """

    assert_html(rendered, expected)


def test_offcanvas_no_backdrop(render, assert_html):
    rendered = render("""
<c-bs-offcanvas backdrop="false">
  <c-fill name="toggle">
    <c-bs-offcanvas-toggle c-attrs="{'class': 'btn btn-primary'}">Toggle Offcanvas</c-bs-offcanvas-toggle>
  </c-fill>
  <c-fill name="default">
    <c-bs-offcanvas-header>
      <c-bs-offcanvas-title>No Backdrop</c-bs-offcanvas-title>
    </c-bs-offcanvas-header>
    <c-bs-offcanvas-body>
      <p>This offcanvas has no backdrop.</p>
    </c-bs-offcanvas-body>
  </c-fill>
</c-bs-offcanvas>
""")

    expected = """
        <button class="btn btn-primary" data-bs-toggle="offcanvas" data-bs-target="#offcanvas-ctest01" aria-controls="offcanvas-ctest01">Toggle Offcanvas</button>
        <div class="offcanvas offcanvas-start" tabindex="-1" id="offcanvas-ctest01" aria-labelledby="offcanvas-ctest01-label" data-bs-backdrop="false">
          <div class="offcanvas-header">
            <h5 class="offcanvas-title" id="offcanvas-ctest01-label">No Backdrop</h5>
            <button type="button" class="btn-close" data-bs-dismiss="offcanvas" data-bs-target="#offcanvas-ctest01" aria-label="Close"></button>
          </div>
          <div class="offcanvas-body">
            <p>This offcanvas has no backdrop.</p>
          </div>
        </div>
    """

    assert_html(rendered, expected)


def test_offcanvas_responsive_lg(render, assert_html):
    rendered = render("""
<c-bs-offcanvas responsive="lg" placement="end">
  <c-fill name="toggle">
    <c-bs-offcanvas-toggle c-attrs="{'class': 'btn btn-primary'}">Toggle Offcanvas</c-bs-offcanvas-toggle>
  </c-fill>
  <c-fill name="default">
    <c-bs-offcanvas-header>
      <c-bs-offcanvas-title>Responsive offcanvas</c-bs-offcanvas-title>
    </c-bs-offcanvas-header>
    <c-bs-offcanvas-body>
      <p>This is content within an offcanvas-lg.</p>
    </c-bs-offcanvas-body>
  </c-fill>
</c-bs-offcanvas>
""")

    expected = """
        <button class="btn btn-primary" data-bs-toggle="offcanvas" data-bs-target="#offcanvas-ctest01" aria-controls="offcanvas-ctest01">Toggle Offcanvas</button>
        <div class="offcanvas-lg offcanvas-end" tabindex="-1" id="offcanvas-ctest01" aria-labelledby="offcanvas-ctest01-label">
          <div class="offcanvas-header">
            <h5 class="offcanvas-title" id="offcanvas-ctest01-label">Responsive offcanvas</h5>
            <button type="button" class="btn-close" data-bs-dismiss="offcanvas" data-bs-target="#offcanvas-ctest01" aria-label="Close"></button>
          </div>
          <div class="offcanvas-body">
            <p>This is content within an offcanvas-lg.</p>
          </div>
        </div>
    """

    assert_html(rendered, expected)


def test_offcanvas_responsive_md(render, assert_html):
    rendered = render("""
<c-bs-offcanvas responsive="md">
  <c-fill name="toggle">
    <c-bs-offcanvas-toggle c-attrs="{'class': 'btn btn-primary'}">Toggle Offcanvas</c-bs-offcanvas-toggle>
  </c-fill>
  <c-fill name="default">
    <c-bs-offcanvas-header>
      <c-bs-offcanvas-title>Responsive MD offcanvas</c-bs-offcanvas-title>
    </c-bs-offcanvas-header>
    <c-bs-offcanvas-body>
      <p>This is content within an offcanvas-md.</p>
    </c-bs-offcanvas-body>
  </c-fill>
</c-bs-offcanvas>
""")

    expected = """
        <button class="btn btn-primary" data-bs-toggle="offcanvas" data-bs-target="#offcanvas-ctest01" aria-controls="offcanvas-ctest01">Toggle Offcanvas</button>
        <div class="offcanvas-md offcanvas-start" tabindex="-1" id="offcanvas-ctest01" aria-labelledby="offcanvas-ctest01-label">
          <div class="offcanvas-header">
            <h5 class="offcanvas-title" id="offcanvas-ctest01-label">Responsive MD offcanvas</h5>
            <button type="button" class="btn-close" data-bs-dismiss="offcanvas" data-bs-target="#offcanvas-ctest01" aria-label="Close"></button>
          </div>
          <div class="offcanvas-body">
            <p>This is content within an offcanvas-md.</p>
          </div>
        </div>
    """

    assert_html(rendered, expected)


def test_offcanvas_without_close_button(render, assert_html):
    rendered = render("""
<c-bs-offcanvas>
  <c-fill name="toggle">
    <c-bs-offcanvas-toggle c-attrs="{'class': 'btn btn-primary'}">Toggle Offcanvas</c-bs-offcanvas-toggle>
  </c-fill>
  <c-fill name="default">
    <c-bs-offcanvas-header c-close_button="False">
      <c-bs-offcanvas-title>No Close Button</c-bs-offcanvas-title>
    </c-bs-offcanvas-header>
    <c-bs-offcanvas-body>
      <p>This offcanvas header has no close button.</p>
    </c-bs-offcanvas-body>
  </c-fill>
</c-bs-offcanvas>
""")

    expected = """
        <button class="btn btn-primary" data-bs-toggle="offcanvas" data-bs-target="#offcanvas-ctest01" aria-controls="offcanvas-ctest01">Toggle Offcanvas</button>
        <div class="offcanvas offcanvas-start" tabindex="-1" id="offcanvas-ctest01" aria-labelledby="offcanvas-ctest01-label">
          <div class="offcanvas-header">
            <h5 class="offcanvas-title" id="offcanvas-ctest01-label">No Close Button</h5>
          </div>
          <div class="offcanvas-body">
            <p>This offcanvas header has no close button.</p>
          </div>
        </div>
    """

    assert_html(rendered, expected)


def test_offcanvas_custom_title_heading(render, assert_html):
    rendered = render("""
<c-bs-offcanvas>
  <c-fill name="toggle">
    <c-bs-offcanvas-toggle c-attrs="{'class': 'btn btn-primary'}">Toggle Offcanvas</c-bs-offcanvas-toggle>
  </c-fill>
  <c-fill name="default">
    <c-bs-offcanvas-header>
      <c-bs-offcanvas-title as_="h3">Custom Heading</c-bs-offcanvas-title>
    </c-bs-offcanvas-header>
    <c-bs-offcanvas-body>
      <p>This offcanvas title uses h3.</p>
    </c-bs-offcanvas-body>
  </c-fill>
</c-bs-offcanvas>
""")

    expected = """
        <button class="btn btn-primary" data-bs-toggle="offcanvas" data-bs-target="#offcanvas-ctest01" aria-controls="offcanvas-ctest01">Toggle Offcanvas</button>
        <div class="offcanvas offcanvas-start" tabindex="-1" id="offcanvas-ctest01" aria-labelledby="offcanvas-ctest01-label">
          <div class="offcanvas-header">
            <h3 class="offcanvas-title" id="offcanvas-ctest01-label">Custom Heading</h3>
            <button type="button" class="btn-close" data-bs-dismiss="offcanvas" data-bs-target="#offcanvas-ctest01" aria-label="Close"></button>
          </div>
          <div class="offcanvas-body">
            <p>This offcanvas title uses h3.</p>
          </div>
        </div>
    """

    assert_html(rendered, expected)
