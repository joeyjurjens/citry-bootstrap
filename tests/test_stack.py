def test_vstack(render, assert_html):
    rendered = render("""
<c-bs-stack direction="vertical" c-gap="3">
  <div class="p-2">First item</div>
  <div class="p-2">Second item</div>
  <div class="p-2">Third item</div>
</c-bs-stack>
""")

    expected = """
        <div class="vstack gap-3">
          <div class="p-2">First item</div>
          <div class="p-2">Second item</div>
          <div class="p-2">Third item</div>
        </div>
    """

    assert_html(rendered, expected)


def test_hstack(render, assert_html):
    rendered = render("""
<c-bs-stack direction="horizontal" c-gap="3">
  <div class="p-2">First item</div>
  <div class="p-2">Second item</div>
  <div class="p-2">Third item</div>
</c-bs-stack>
""")

    expected = """
        <div class="hstack gap-3">
          <div class="p-2">First item</div>
          <div class="p-2">Second item</div>
          <div class="p-2">Third item</div>
        </div>
    """

    assert_html(rendered, expected)


def test_hstack_with_spacer(render, assert_html):
    rendered = render("""
<c-bs-stack direction="horizontal" c-gap="3">
  <div class="p-2">First item</div>
  <div class="p-2 ms-auto">Second item</div>
  <div class="p-2">Third item</div>
</c-bs-stack>
""")

    expected = """
        <div class="hstack gap-3">
          <div class="p-2">First item</div>
          <div class="p-2 ms-auto">Second item</div>
          <div class="p-2">Third item</div>
        </div>
    """

    assert_html(rendered, expected)


def test_hstack_with_vertical_rule(render, assert_html):
    rendered = render("""
<c-bs-stack direction="horizontal" c-gap="3">
  <div class="p-2">First item</div>
  <div class="p-2 ms-auto">Second item</div>
  <div class="vr"></div>
  <div class="p-2">Third item</div>
</c-bs-stack>
""")

    expected = """
        <div class="hstack gap-3">
          <div class="p-2">First item</div>
          <div class="p-2 ms-auto">Second item</div>
          <div class="vr"></div>
          <div class="p-2">Third item</div>
        </div>
    """

    assert_html(rendered, expected)


def test_vstack_buttons(render, assert_html):
    rendered = render("""
<c-bs-stack direction="vertical" c-gap="2">
  <c-bs-button variant="secondary">Save changes</c-bs-button>
  <c-bs-button variant="secondary" c-outline="True">Cancel</c-bs-button>
</c-bs-stack>
""")

    expected = """
        <div class="vstack gap-2">
          <button type="button" class="btn btn-secondary">Save changes</button>
          <button type="button" class="btn btn-outline-secondary">Cancel</button>
        </div>
    """

    assert_html(rendered, expected)


def test_hstack_inline_form(render, assert_html):
    rendered = render("""
<c-bs-stack direction="horizontal" c-gap="3">
  <c-bs-form-control placeholder="Add your item here..." c-attrs="{'class': 'me-auto', 'aria-label': 'Add your item here...'}" />
  <c-bs-button variant="secondary">Submit</c-bs-button>
  <div class="vr"></div>
  <c-bs-button variant="danger" c-outline="True">Reset</c-bs-button>
</c-bs-stack>
""")

    expected = """
        <div class="hstack gap-3">
          <input class="form-control me-auto" type="text" placeholder="Add your item here..." aria-label="Add your item here...">
          <button type="button" class="btn btn-secondary">Submit</button>
          <div class="vr"></div>
          <button type="button" class="btn btn-outline-danger">Reset</button>
        </div>
    """

    assert_html(rendered, expected)


def test_vstack_no_gap(render, assert_html):
    rendered = render("""
<c-bs-stack direction="vertical">
  <div class="p-2">First item</div>
  <div class="p-2">Second item</div>
  <div class="p-2">Third item</div>
</c-bs-stack>
""")

    expected = """
        <div class="vstack">
          <div class="p-2">First item</div>
          <div class="p-2">Second item</div>
          <div class="p-2">Third item</div>
        </div>
    """

    assert_html(rendered, expected)


def test_hstack_no_gap(render, assert_html):
    rendered = render("""
<c-bs-stack direction="horizontal">
  <div class="p-2">First item</div>
  <div class="p-2">Second item</div>
  <div class="p-2">Third item</div>
</c-bs-stack>
""")

    expected = """
        <div class="hstack">
          <div class="p-2">First item</div>
          <div class="p-2">Second item</div>
          <div class="p-2">Third item</div>
        </div>
    """

    assert_html(rendered, expected)
