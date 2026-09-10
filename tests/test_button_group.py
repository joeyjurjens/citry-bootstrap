def test_basic(render, assert_html):
    rendered = render("""
<c-bs-button-group>
  <c-bs-button variant="primary">Left</c-bs-button>
  <c-bs-button variant="primary">Middle</c-bs-button>
  <c-bs-button variant="primary">Right</c-bs-button>
</c-bs-button-group>
""")

    expected = """
        <div class="btn-group" role="group">
          <button type="button" class="btn btn-primary">Left</button>
          <button type="button" class="btn btn-primary">Middle</button>
          <button type="button" class="btn btn-primary">Right</button>
        </div>
    """

    assert_html(rendered, expected)


def test_mixed_styles(render, assert_html):
    rendered = render("""
<c-bs-button-group>
  <c-bs-button variant="danger">Danger</c-bs-button>
  <c-bs-button variant="warning">Warning</c-bs-button>
  <c-bs-button variant="success">Success</c-bs-button>
</c-bs-button-group>
""")

    expected = """
        <div class="btn-group" role="group">
          <button type="button" class="btn btn-danger">Danger</button>
          <button type="button" class="btn btn-warning">Warning</button>
          <button type="button" class="btn btn-success">Success</button>
        </div>
    """

    assert_html(rendered, expected)


def test_checkbox_buttons(render, assert_html):
    rendered = render("""
<c-bs-button-group>
  <c-bs-toggle-button c-attrs="{'id': 'btncheck1'}">Checkbox 1</c-bs-toggle-button>
  <c-bs-toggle-button c-attrs="{'id': 'btncheck2'}">Checkbox 2</c-bs-toggle-button>
  <c-bs-toggle-button c-attrs="{'id': 'btncheck3'}">Checkbox 3</c-bs-toggle-button>
</c-bs-button-group>
""")

    assert "btn-check" in rendered
    assert "Checkbox 1" in rendered
    assert "Checkbox 2" in rendered
    assert "Checkbox 3" in rendered


def test_radio_buttons(render, assert_html):
    rendered = render("""
<c-bs-button-group>
  <c-bs-toggle-button type="radio" name="btnradio" c-checked="True" c-attrs="{'id': 'btnradio1'}">Radio 1</c-bs-toggle-button>
  <c-bs-toggle-button type="radio" name="btnradio" c-attrs="{'id': 'btnradio2'}">Radio 2</c-bs-toggle-button>
  <c-bs-toggle-button type="radio" name="btnradio" c-attrs="{'id': 'btnradio3'}">Radio 3</c-bs-toggle-button>
</c-bs-button-group>
""")

    assert "btn-check" in rendered
    assert "Radio 1" in rendered
    assert "Radio 2" in rendered
    assert "Radio 3" in rendered


def test_large(render, assert_html):
    rendered = render("""
<c-bs-button-group size="lg">
  <c-bs-button variant="primary" c-outline="True">Left</c-bs-button>
  <c-bs-button variant="primary" c-outline="True">Middle</c-bs-button>
  <c-bs-button variant="primary" c-outline="True">Right</c-bs-button>
</c-bs-button-group>
""")

    expected = """
        <div class="btn-group btn-group-lg" role="group">
          <button type="button" class="btn btn-outline-primary">Left</button>
          <button type="button" class="btn btn-outline-primary">Middle</button>
          <button type="button" class="btn btn-outline-primary">Right</button>
        </div>
    """

    assert_html(rendered, expected)


def test_small(render, assert_html):
    rendered = render("""
<c-bs-button-group size="sm">
  <c-bs-button variant="primary" c-outline="True">Left</c-bs-button>
  <c-bs-button variant="primary" c-outline="True">Middle</c-bs-button>
  <c-bs-button variant="primary" c-outline="True">Right</c-bs-button>
</c-bs-button-group>
""")

    expected = """
        <div class="btn-group btn-group-sm" role="group">
          <button type="button" class="btn btn-outline-primary">Left</button>
          <button type="button" class="btn btn-outline-primary">Middle</button>
          <button type="button" class="btn btn-outline-primary">Right</button>
        </div>
    """

    assert_html(rendered, expected)


def test_vertical(render, assert_html):
    rendered = render("""
<c-bs-button-group c-vertical="True">
  <c-bs-button variant="primary">Button</c-bs-button>
  <c-bs-button variant="primary">Button</c-bs-button>
  <c-bs-button variant="primary">Button</c-bs-button>
  <c-bs-button variant="primary">Button</c-bs-button>
</c-bs-button-group>
""")

    expected = """
        <div class="btn-group-vertical" role="group">
          <button type="button" class="btn btn-primary">Button</button>
          <button type="button" class="btn btn-primary">Button</button>
          <button type="button" class="btn btn-primary">Button</button>
          <button type="button" class="btn btn-primary">Button</button>
        </div>
    """

    assert_html(rendered, expected)


def test_toolbar_basic(render, assert_html):
    rendered = render("""
<c-bs-button-toolbar>
  <c-bs-button-group c-attrs="{'class': 'me-2'}">
    <c-bs-button variant="primary">1</c-bs-button>
    <c-bs-button variant="primary">2</c-bs-button>
    <c-bs-button variant="primary">3</c-bs-button>
    <c-bs-button variant="primary">4</c-bs-button>
  </c-bs-button-group>
  <c-bs-button-group c-attrs="{'class': 'me-2'}">
    <c-bs-button variant="secondary">5</c-bs-button>
    <c-bs-button variant="secondary">6</c-bs-button>
    <c-bs-button variant="secondary">7</c-bs-button>
  </c-bs-button-group>
  <c-bs-button-group>
    <c-bs-button variant="info">8</c-bs-button>
  </c-bs-button-group>
</c-bs-button-toolbar>
""")

    expected = """
        <div class="btn-toolbar" role="toolbar">
          <div class="btn-group me-2" role="group">
            <button type="button" class="btn btn-primary">1</button>
            <button type="button" class="btn btn-primary">2</button>
            <button type="button" class="btn btn-primary">3</button>
            <button type="button" class="btn btn-primary">4</button>
          </div>
          <div class="btn-group me-2" role="group">
            <button type="button" class="btn btn-secondary">5</button>
            <button type="button" class="btn btn-secondary">6</button>
            <button type="button" class="btn btn-secondary">7</button>
          </div>
          <div class="btn-group" role="group">
            <button type="button" class="btn btn-info">8</button>
          </div>
        </div>
    """

    assert_html(rendered, expected)
