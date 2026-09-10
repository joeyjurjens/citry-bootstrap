def test_basic(render, assert_html):
    rendered = render("""
<c-bs-list-group>
  <c-bs-list-group-item>An item</c-bs-list-group-item>
  <c-bs-list-group-item>A second item</c-bs-list-group-item>
  <c-bs-list-group-item>A third item</c-bs-list-group-item>
  <c-bs-list-group-item>A fourth item</c-bs-list-group-item>
  <c-bs-list-group-item>And a fifth one</c-bs-list-group-item>
</c-bs-list-group>
""")

    expected = """
        <ul class="list-group">
          <li class="list-group-item">An item</li>
          <li class="list-group-item">A second item</li>
          <li class="list-group-item">A third item</li>
          <li class="list-group-item">A fourth item</li>
          <li class="list-group-item">And a fifth one</li>
        </ul>
    """

    assert_html(rendered, expected)


def test_active_items(render, assert_html):
    rendered = render("""
<c-bs-list-group>
  <c-bs-list-group-item c-active="True">An active item</c-bs-list-group-item>
  <c-bs-list-group-item>A second item</c-bs-list-group-item>
  <c-bs-list-group-item>A third item</c-bs-list-group-item>
  <c-bs-list-group-item>A fourth item</c-bs-list-group-item>
  <c-bs-list-group-item>And a fifth one</c-bs-list-group-item>
</c-bs-list-group>
""")

    expected = """
        <ul class="list-group">
          <li class="list-group-item active" aria-current="true">An active item</li>
          <li class="list-group-item">A second item</li>
          <li class="list-group-item">A third item</li>
          <li class="list-group-item">A fourth item</li>
          <li class="list-group-item">And a fifth one</li>
        </ul>
    """

    assert_html(rendered, expected)


def test_disabled_items(render, assert_html):
    rendered = render("""
<c-bs-list-group>
  <c-bs-list-group-item>An item</c-bs-list-group-item>
  <c-bs-list-group-item>A second item</c-bs-list-group-item>
  <c-bs-list-group-item>A third item</c-bs-list-group-item>
  <c-bs-list-group-item>A fourth item</c-bs-list-group-item>
  <c-bs-list-group-item c-disabled="True">A disabled fifth item</c-bs-list-group-item>
</c-bs-list-group>
""")

    expected = """
        <ul class="list-group">
          <li class="list-group-item">An item</li>
          <li class="list-group-item">A second item</li>
          <li class="list-group-item">A third item</li>
          <li class="list-group-item">A fourth item</li>
          <li class="list-group-item disabled" aria-disabled="true">A disabled fifth item</li>
        </ul>
    """

    assert_html(rendered, expected)


def test_links(render, assert_html):
    rendered = render("""
<c-bs-list-group as_="div">
  <c-bs-list-group-item href="#" c-active="True">The current link item</c-bs-list-group-item>
  <c-bs-list-group-item href="#">A second link item</c-bs-list-group-item>
  <c-bs-list-group-item href="#">A third link item</c-bs-list-group-item>
  <c-bs-list-group-item href="#">A fourth link item</c-bs-list-group-item>
  <c-bs-list-group-item href="#" c-disabled="True">A disabled link item</c-bs-list-group-item>
</c-bs-list-group>
""")

    expected = """
        <div class="list-group">
          <a href="#" class="list-group-item list-group-item-action active" aria-current="true">The current link item</a>
          <a href="#" class="list-group-item list-group-item-action">A second link item</a>
          <a href="#" class="list-group-item list-group-item-action">A third link item</a>
          <a href="#" class="list-group-item list-group-item-action">A fourth link item</a>
          <a href="#" class="list-group-item list-group-item-action disabled" aria-disabled="true">A disabled link item</a>
        </div>
    """

    assert_html(rendered, expected)


def test_buttons(render, assert_html):
    rendered = render("""
<c-bs-list-group as_="div">
  <c-bs-list-group-item as_="button" c-active="True">The current button</c-bs-list-group-item>
  <c-bs-list-group-item as_="button">A second button item</c-bs-list-group-item>
  <c-bs-list-group-item as_="button">A third button item</c-bs-list-group-item>
  <c-bs-list-group-item as_="button">A fourth button item</c-bs-list-group-item>
  <c-bs-list-group-item as_="button" c-disabled="True">A disabled button item</c-bs-list-group-item>
</c-bs-list-group>
""")

    expected = """
        <div class="list-group">
          <button type="button" class="list-group-item list-group-item-action active" aria-current="true">The current button</button>
          <button type="button" class="list-group-item list-group-item-action">A second button item</button>
          <button type="button" class="list-group-item list-group-item-action">A third button item</button>
          <button type="button" class="list-group-item list-group-item-action">A fourth button item</button>
          <button type="button" class="list-group-item list-group-item-action" disabled>A disabled button item</button>
        </div>
    """

    assert_html(rendered, expected)


def test_flush(render, assert_html):
    rendered = render("""
<c-bs-list-group c-flush="True">
  <c-bs-list-group-item>An item</c-bs-list-group-item>
  <c-bs-list-group-item>A second item</c-bs-list-group-item>
  <c-bs-list-group-item>A third item</c-bs-list-group-item>
  <c-bs-list-group-item>A fourth item</c-bs-list-group-item>
  <c-bs-list-group-item>And a fifth one</c-bs-list-group-item>
</c-bs-list-group>
""")

    expected = """
        <ul class="list-group list-group-flush">
          <li class="list-group-item">An item</li>
          <li class="list-group-item">A second item</li>
          <li class="list-group-item">A third item</li>
          <li class="list-group-item">A fourth item</li>
          <li class="list-group-item">And a fifth one</li>
        </ul>
    """

    assert_html(rendered, expected)


def test_numbered(render, assert_html):
    rendered = render("""
<c-bs-list-group c-numbered="True">
  <c-bs-list-group-item>A list item</c-bs-list-group-item>
  <c-bs-list-group-item>A list item</c-bs-list-group-item>
  <c-bs-list-group-item>A list item</c-bs-list-group-item>
</c-bs-list-group>
""")

    expected = """
        <ol class="list-group list-group-numbered">
          <li class="list-group-item">A list item</li>
          <li class="list-group-item">A list item</li>
          <li class="list-group-item">A list item</li>
        </ol>
    """

    assert_html(rendered, expected)


def test_numbered_with_custom_content(render, assert_html):
    rendered = render("""
<c-bs-list-group c-numbered="True">
  <c-bs-list-group-item c-attrs="{'class': 'd-flex justify-content-between align-items-start'}">
    <div class="ms-2 me-auto">
      <div class="fw-bold">Subheading</div>
      Content for list item
    </div>
    <c-bs-badge bg="primary" c-pill="True">14</c-bs-badge>
  </c-bs-list-group-item>
  <c-bs-list-group-item c-attrs="{'class': 'd-flex justify-content-between align-items-start'}">
    <div class="ms-2 me-auto">
      <div class="fw-bold">Subheading</div>
      Content for list item
    </div>
    <c-bs-badge bg="primary" c-pill="True">14</c-bs-badge>
  </c-bs-list-group-item>
  <c-bs-list-group-item c-attrs="{'class': 'd-flex justify-content-between align-items-start'}">
    <div class="ms-2 me-auto">
      <div class="fw-bold">Subheading</div>
      Content for list item
    </div>
    <c-bs-badge bg="primary" c-pill="True">14</c-bs-badge>
  </c-bs-list-group-item>
</c-bs-list-group>
""")

    expected = """
        <ol class="list-group list-group-numbered">
          <li class="list-group-item d-flex justify-content-between align-items-start">
            <div class="ms-2 me-auto">
              <div class="fw-bold">Subheading</div>
              Content for list item
            </div>
            <span class="badge text-bg-primary rounded-pill">14</span>
          </li>
          <li class="list-group-item d-flex justify-content-between align-items-start">
            <div class="ms-2 me-auto">
              <div class="fw-bold">Subheading</div>
              Content for list item
            </div>
            <span class="badge text-bg-primary rounded-pill">14</span>
          </li>
          <li class="list-group-item d-flex justify-content-between align-items-start">
            <div class="ms-2 me-auto">
              <div class="fw-bold">Subheading</div>
              Content for list item
            </div>
            <span class="badge text-bg-primary rounded-pill">14</span>
          </li>
        </ol>
    """

    assert_html(rendered, expected)


def test_horizontal(render, assert_html):
    rendered = render("""
<c-bs-list-group c-horizontal="True">
  <c-bs-list-group-item>An item</c-bs-list-group-item>
  <c-bs-list-group-item>A second item</c-bs-list-group-item>
  <c-bs-list-group-item>A third item</c-bs-list-group-item>
</c-bs-list-group>
""")

    expected = """
        <ul class="list-group list-group-horizontal">
          <li class="list-group-item">An item</li>
          <li class="list-group-item">A second item</li>
          <li class="list-group-item">A third item</li>
        </ul>
    """

    assert_html(rendered, expected)


def test_horizontal_responsive_sm(render, assert_html):
    rendered = render("""
<c-bs-list-group horizontal="sm">
  <c-bs-list-group-item>An item</c-bs-list-group-item>
  <c-bs-list-group-item>A second item</c-bs-list-group-item>
  <c-bs-list-group-item>A third item</c-bs-list-group-item>
</c-bs-list-group>
""")

    expected = """
        <ul class="list-group list-group-horizontal-sm">
          <li class="list-group-item">An item</li>
          <li class="list-group-item">A second item</li>
          <li class="list-group-item">A third item</li>
        </ul>
    """

    assert_html(rendered, expected)


def test_horizontal_responsive_md(render, assert_html):
    rendered = render("""
<c-bs-list-group horizontal="md">
  <c-bs-list-group-item>An item</c-bs-list-group-item>
  <c-bs-list-group-item>A second item</c-bs-list-group-item>
  <c-bs-list-group-item>A third item</c-bs-list-group-item>
</c-bs-list-group>
""")

    expected = """
        <ul class="list-group list-group-horizontal-md">
          <li class="list-group-item">An item</li>
          <li class="list-group-item">A second item</li>
          <li class="list-group-item">A third item</li>
        </ul>
    """

    assert_html(rendered, expected)


def test_contextual_variants(render, assert_html):
    rendered = render("""
<c-bs-list-group>
  <c-bs-list-group-item>A simple default list group item</c-bs-list-group-item>
  <c-bs-list-group-item variant="primary">A simple primary item</c-bs-list-group-item>
  <c-bs-list-group-item variant="secondary">A simple secondary item</c-bs-list-group-item>
  <c-bs-list-group-item variant="success">A simple success item</c-bs-list-group-item>
  <c-bs-list-group-item variant="danger">A simple danger item</c-bs-list-group-item>
  <c-bs-list-group-item variant="warning">A simple warning item</c-bs-list-group-item>
  <c-bs-list-group-item variant="info">A simple info item</c-bs-list-group-item>
  <c-bs-list-group-item variant="light">A simple light item</c-bs-list-group-item>
  <c-bs-list-group-item variant="dark">A simple dark item</c-bs-list-group-item>
</c-bs-list-group>
""")

    expected = """
        <ul class="list-group">
          <li class="list-group-item">A simple default list group item</li>
          <li class="list-group-item list-group-item-primary">A simple primary item</li>
          <li class="list-group-item list-group-item-secondary">A simple secondary item</li>
          <li class="list-group-item list-group-item-success">A simple success item</li>
          <li class="list-group-item list-group-item-danger">A simple danger item</li>
          <li class="list-group-item list-group-item-warning">A simple warning item</li>
          <li class="list-group-item list-group-item-info">A simple info item</li>
          <li class="list-group-item list-group-item-light">A simple light item</li>
          <li class="list-group-item list-group-item-dark">A simple dark item</li>
        </ul>
    """

    assert_html(rendered, expected)


def test_contextual_variants_for_links(render, assert_html):
    rendered = render("""
<c-bs-list-group as_="div">
  <c-bs-list-group-item href="#">A simple default item</c-bs-list-group-item>
  <c-bs-list-group-item href="#" variant="primary">A simple primary item</c-bs-list-group-item>
  <c-bs-list-group-item href="#" variant="secondary">A simple secondary item</c-bs-list-group-item>
  <c-bs-list-group-item href="#" variant="success">A simple success item</c-bs-list-group-item>
  <c-bs-list-group-item href="#" variant="danger">A simple danger item</c-bs-list-group-item>
  <c-bs-list-group-item href="#" variant="warning">A simple warning item</c-bs-list-group-item>
  <c-bs-list-group-item href="#" variant="info">A simple info item</c-bs-list-group-item>
  <c-bs-list-group-item href="#" variant="light">A simple light item</c-bs-list-group-item>
  <c-bs-list-group-item href="#" variant="dark">A simple dark item</c-bs-list-group-item>
</c-bs-list-group>
""")

    expected = """
        <div class="list-group">
          <a href="#" class="list-group-item list-group-item-action">A simple default item</a>
          <a href="#" class="list-group-item list-group-item-action list-group-item-primary">A simple primary item</a>
          <a href="#" class="list-group-item list-group-item-action list-group-item-secondary">A simple secondary item</a>
          <a href="#" class="list-group-item list-group-item-action list-group-item-success">A simple success item</a>
          <a href="#" class="list-group-item list-group-item-action list-group-item-danger">A simple danger item</a>
          <a href="#" class="list-group-item list-group-item-action list-group-item-warning">A simple warning item</a>
          <a href="#" class="list-group-item list-group-item-action list-group-item-info">A simple info item</a>
          <a href="#" class="list-group-item list-group-item-action list-group-item-light">A simple light item</a>
          <a href="#" class="list-group-item list-group-item-action list-group-item-dark">A simple dark item</a>
        </div>
    """

    assert_html(rendered, expected)


def test_with_badges(render, assert_html):
    rendered = render("""
<c-bs-list-group>
  <c-bs-list-group-item c-attrs="{'class': 'd-flex justify-content-between align-items-center'}">
    A list item
    <c-bs-badge bg="primary" c-pill="True">14</c-bs-badge>
  </c-bs-list-group-item>
  <c-bs-list-group-item c-attrs="{'class': 'd-flex justify-content-between align-items-center'}">
    A second list item
    <c-bs-badge bg="primary" c-pill="True">2</c-bs-badge>
  </c-bs-list-group-item>
  <c-bs-list-group-item c-attrs="{'class': 'd-flex justify-content-between align-items-center'}">
    A third list item
    <c-bs-badge bg="primary" c-pill="True">1</c-bs-badge>
  </c-bs-list-group-item>
</c-bs-list-group>
""")

    expected = """
        <ul class="list-group">
          <li class="list-group-item d-flex justify-content-between align-items-center">
            A list item
            <span class="badge text-bg-primary rounded-pill">14</span>
          </li>
          <li class="list-group-item d-flex justify-content-between align-items-center">
            A second list item
            <span class="badge text-bg-primary rounded-pill">2</span>
          </li>
          <li class="list-group-item d-flex justify-content-between align-items-center">
            A third list item
            <span class="badge text-bg-primary rounded-pill">1</span>
          </li>
        </ul>
    """

    assert_html(rendered, expected)


def test_custom_content(render, assert_html):
    rendered = render("""
<c-bs-list-group as_="div">
  <c-bs-list-group-item href="#" c-active="True">
    <div class="d-flex w-100 justify-content-between">
      <h5 class="mb-1">List group item heading</h5>
      <small>3 days ago</small>
    </div>
    <p class="mb-1">Some placeholder content in a paragraph.</p>
    <small>And some small print.</small>
  </c-bs-list-group-item>
  <c-bs-list-group-item href="#">
    <div class="d-flex w-100 justify-content-between">
      <h5 class="mb-1">List group item heading</h5>
      <small class="text-body-secondary">3 days ago</small>
    </div>
    <p class="mb-1">Some placeholder content in a paragraph.</p>
    <small class="text-body-secondary">And some muted small print.</small>
  </c-bs-list-group-item>
  <c-bs-list-group-item href="#">
    <div class="d-flex w-100 justify-content-between">
      <h5 class="mb-1">List group item heading</h5>
      <small class="text-body-secondary">3 days ago</small>
    </div>
    <p class="mb-1">Some placeholder content in a paragraph.</p>
    <small class="text-body-secondary">And some muted small print.</small>
  </c-bs-list-group-item>
</c-bs-list-group>
""")

    expected = """
        <div class="list-group">
          <a href="#" class="list-group-item list-group-item-action active" aria-current="true">
            <div class="d-flex w-100 justify-content-between">
              <h5 class="mb-1">List group item heading</h5>
              <small>3 days ago</small>
            </div>
            <p class="mb-1">Some placeholder content in a paragraph.</p>
            <small>And some small print.</small>
          </a>
          <a href="#" class="list-group-item list-group-item-action">
            <div class="d-flex w-100 justify-content-between">
              <h5 class="mb-1">List group item heading</h5>
              <small class="text-body-secondary">3 days ago</small>
            </div>
            <p class="mb-1">Some placeholder content in a paragraph.</p>
            <small class="text-body-secondary">And some muted small print.</small>
          </a>
          <a href="#" class="list-group-item list-group-item-action">
            <div class="d-flex w-100 justify-content-between">
              <h5 class="mb-1">List group item heading</h5>
              <small class="text-body-secondary">3 days ago</small>
            </div>
            <p class="mb-1">Some placeholder content in a paragraph.</p>
            <small class="text-body-secondary">And some muted small print.</small>
          </a>
        </div>
    """

    assert_html(rendered, expected)


def test_with_checkboxes(render, assert_html):
    rendered = render("""
<c-bs-list-group>
  <c-bs-list-group-item>
    <c-bs-form-check-input c-value="''" c-attrs="{'class': 'me-1', 'id': 'firstCheckbox'}" />
    <c-bs-form-check-label for_="firstCheckbox">First checkbox</c-bs-form-check-label>
  </c-bs-list-group-item>
  <c-bs-list-group-item>
    <c-bs-form-check-input c-value="''" c-attrs="{'class': 'me-1', 'id': 'secondCheckbox'}" />
    <c-bs-form-check-label for_="secondCheckbox">Second checkbox</c-bs-form-check-label>
  </c-bs-list-group-item>
  <c-bs-list-group-item>
    <c-bs-form-check-input c-value="''" c-attrs="{'class': 'me-1', 'id': 'thirdCheckbox'}" />
    <c-bs-form-check-label for_="thirdCheckbox">Third checkbox</c-bs-form-check-label>
  </c-bs-list-group-item>
</c-bs-list-group>
""")

    expected = """
        <ul class="list-group">
          <li class="list-group-item">
            <input class="form-check-input me-1" type="checkbox" value="" id="firstCheckbox">
            <label class="form-check-label" for="firstCheckbox">First checkbox</label>
          </li>
          <li class="list-group-item">
            <input class="form-check-input me-1" type="checkbox" value="" id="secondCheckbox">
            <label class="form-check-label" for="secondCheckbox">Second checkbox</label>
          </li>
          <li class="list-group-item">
            <input class="form-check-input me-1" type="checkbox" value="" id="thirdCheckbox">
            <label class="form-check-label" for="thirdCheckbox">Third checkbox</label>
          </li>
        </ul>
    """

    assert_html(rendered, expected)


def test_with_radio_buttons(render, assert_html):
    rendered = render("""
<c-bs-list-group>
  <c-bs-list-group-item>
    <c-bs-form-check-input type="radio" name="listGroupRadio" c-value="''" c-checked="True" c-attrs="{'class': 'me-1', 'id': 'firstRadio'}" />
    <c-bs-form-check-label for_="firstRadio">First radio</c-bs-form-check-label>
  </c-bs-list-group-item>
  <c-bs-list-group-item>
    <c-bs-form-check-input type="radio" name="listGroupRadio" c-value="''" c-attrs="{'class': 'me-1', 'id': 'secondRadio'}" />
    <c-bs-form-check-label for_="secondRadio">Second radio</c-bs-form-check-label>
  </c-bs-list-group-item>
  <c-bs-list-group-item>
    <c-bs-form-check-input type="radio" name="listGroupRadio" c-value="''" c-attrs="{'class': 'me-1', 'id': 'thirdRadio'}" />
    <c-bs-form-check-label for_="thirdRadio">Third radio</c-bs-form-check-label>
  </c-bs-list-group-item>
</c-bs-list-group>
""")

    expected = """
        <ul class="list-group">
          <li class="list-group-item">
            <input class="form-check-input me-1" type="radio" name="listGroupRadio" value="" id="firstRadio" checked>
            <label class="form-check-label" for="firstRadio">First radio</label>
          </li>
          <li class="list-group-item">
            <input class="form-check-input me-1" type="radio" name="listGroupRadio" value="" id="secondRadio">
            <label class="form-check-label" for="secondRadio">Second radio</label>
          </li>
          <li class="list-group-item">
            <input class="form-check-input me-1" type="radio" name="listGroupRadio" value="" id="thirdRadio">
            <label class="form-check-label" for="thirdRadio">Third radio</label>
          </li>
        </ul>
    """

    assert_html(rendered, expected)
