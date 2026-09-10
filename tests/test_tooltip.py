def test_tooltip_basic(render, assert_html):
    rendered = render("""
<c-bs-tooltip text="Default tooltip" placement="top">
  <a href="#">inline links</a>
</c-bs-tooltip>
""")

    expected = """
        <span data-bs-toggle="tooltip" data-bs-title="Default tooltip" data-bs-placement="top" data-bs-trigger="hover">
            <a href="#">inline links</a>
        </span>
    """

    assert_html(rendered, expected)


def test_tooltip_placement_top(render, assert_html):
    rendered = render("""
<c-bs-tooltip text="Tooltip on top" placement="top">
  <c-bs-button variant="secondary">Top</c-bs-button>
</c-bs-tooltip>
""")

    expected = """
        <span data-bs-toggle="tooltip" data-bs-title="Tooltip on top" data-bs-placement="top" data-bs-trigger="hover">
            <button class="btn btn-secondary" type="button">Top</button>
        </span>
    """

    assert_html(rendered, expected)


def test_tooltip_placement_right(render, assert_html):
    rendered = render("""
<c-bs-tooltip text="Tooltip on right" placement="right">
  <c-bs-button variant="secondary">Right</c-bs-button>
</c-bs-tooltip>
""")

    expected = """
        <span data-bs-toggle="tooltip" data-bs-title="Tooltip on right" data-bs-placement="right" data-bs-trigger="hover">
            <button class="btn btn-secondary" type="button">Right</button>
        </span>
    """

    assert_html(rendered, expected)


def test_tooltip_placement_bottom(render, assert_html):
    rendered = render("""
<c-bs-tooltip text="Tooltip on bottom" placement="bottom">
  <c-bs-button variant="secondary">Bottom</c-bs-button>
</c-bs-tooltip>
""")

    expected = """
        <span data-bs-toggle="tooltip" data-bs-title="Tooltip on bottom" data-bs-placement="bottom" data-bs-trigger="hover">
            <button class="btn btn-secondary" type="button">Bottom</button>
        </span>
    """

    assert_html(rendered, expected)


def test_tooltip_placement_left(render, assert_html):
    rendered = render("""
<c-bs-tooltip text="Tooltip on left" placement="left">
  <c-bs-button variant="secondary">Left</c-bs-button>
</c-bs-tooltip>
""")

    expected = """
        <span data-bs-toggle="tooltip" data-bs-title="Tooltip on left" data-bs-placement="left" data-bs-trigger="hover">
            <button class="btn btn-secondary" type="button">Left</button>
        </span>
    """

    assert_html(rendered, expected)


def test_tooltip_with_button(render, assert_html):
    rendered = render("""
<c-bs-tooltip text="This top tooltip is themed via CSS variables." placement="top">
  <c-bs-button variant="secondary" c-attrs="{'data-bs-custom-class': 'custom-tooltip'}">Custom tooltip</c-bs-button>
</c-bs-tooltip>
""")

    expected = """
        <span data-bs-toggle="tooltip" data-bs-title="This top tooltip is themed via CSS variables." data-bs-placement="top" data-bs-trigger="hover">
            <button type="button" class="btn btn-secondary" data-bs-custom-class="custom-tooltip">
                Custom tooltip
            </button>
        </span>
    """

    assert_html(rendered, expected)


def test_tooltip_disabled_button_wrapper(render, assert_html):
    rendered = render("""
<c-bs-tooltip text="Disabled tooltip" placement="top">
  <span class="d-inline-block" tabindex="0">
    <c-bs-button variant="primary" type="button" c-disabled="True">Disabled button</c-bs-button>
  </span>
</c-bs-tooltip>
""")

    expected = """
        <span data-bs-toggle="tooltip" data-bs-title="Disabled tooltip" data-bs-placement="top" data-bs-trigger="hover">
            <span class="d-inline-block" tabindex="0">
                <button class="btn btn-primary" type="button" disabled>Disabled button</button>
            </span>
        </span>
    """

    assert_html(rendered, expected)
