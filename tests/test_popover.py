def test_popover_basic(render, assert_html):
    rendered = render("""
<c-bs-popover title="Popover title" content="And here's some amazing content. It's very engaging. Right?" placement="top">
  <c-bs-button variant="danger" size="lg">Click to toggle popover</c-bs-button>
</c-bs-popover>
""")

    expected = """
        <span data-bs-toggle="popover" data-bs-title="Popover title" data-bs-content="And here's some amazing content. It's very engaging. Right?" data-bs-placement="top" data-bs-trigger="click">
            <button class="btn btn-lg btn-danger" type="button">Click to toggle popover</button>
        </span>
    """

    assert_html(rendered, expected)


def test_popover_placement_top(render, assert_html):
    rendered = render("""
<c-bs-popover title="Top popover" content="Popover content on top" placement="top">
  <c-bs-button variant="secondary" c-attrs="{'data-bs-container': 'body'}">Popover on top</c-bs-button>
</c-bs-popover>
""")

    expected = """
        <span data-bs-toggle="popover" data-bs-title="Top popover" data-bs-content="Popover content on top" data-bs-placement="top" data-bs-trigger="click">
            <button class="btn btn-secondary" type="button" data-bs-container="body">Popover on top</button>
        </span>
    """

    assert_html(rendered, expected)


def test_popover_placement_right(render, assert_html):
    rendered = render("""
<c-bs-popover title="Right popover" content="Popover content on right" placement="right">
  <c-bs-button variant="secondary" c-attrs="{'data-bs-container': 'body'}">Popover on right</c-bs-button>
</c-bs-popover>
""")

    expected = """
        <span data-bs-toggle="popover" data-bs-title="Right popover" data-bs-content="Popover content on right" data-bs-placement="right" data-bs-trigger="click">
            <button class="btn btn-secondary" type="button" data-bs-container="body">Popover on right</button>
        </span>
    """

    assert_html(rendered, expected)


def test_popover_placement_bottom(render, assert_html):
    rendered = render("""
<c-bs-popover title="Bottom popover" content="Popover content on bottom" placement="bottom">
  <c-bs-button variant="secondary" c-attrs="{'data-bs-container': 'body'}">Popover on bottom</c-bs-button>
</c-bs-popover>
""")

    expected = """
        <span data-bs-toggle="popover" data-bs-title="Bottom popover" data-bs-content="Popover content on bottom" data-bs-placement="bottom" data-bs-trigger="click">
            <button class="btn btn-secondary" type="button" data-bs-container="body">Popover on bottom</button>
        </span>
    """

    assert_html(rendered, expected)


def test_popover_placement_left(render, assert_html):
    rendered = render("""
<c-bs-popover title="Left popover" content="Popover content on left" placement="left">
  <c-bs-button variant="secondary" c-attrs="{'data-bs-container': 'body'}">Popover on left</c-bs-button>
</c-bs-popover>
""")

    expected = """
        <span data-bs-toggle="popover" data-bs-title="Left popover" data-bs-content="Popover content on left" data-bs-placement="left" data-bs-trigger="click">
            <button class="btn btn-secondary" type="button" data-bs-container="body">Popover on left</button>
        </span>
    """

    assert_html(rendered, expected)


def test_popover_custom_styled(render, assert_html):
    rendered = render("""
<c-bs-popover title="Custom popover" content="This popover is themed via CSS variables." placement="right" c-attrs="{'data-bs-custom-class': 'custom-popover'}">
  <c-bs-button variant="secondary">Custom popover</c-bs-button>
</c-bs-popover>
""")

    expected = """
        <span data-bs-toggle="popover" data-bs-title="Custom popover" data-bs-content="This popover is themed via CSS variables." data-bs-placement="right" data-bs-trigger="click" data-bs-custom-class="custom-popover">
            <button class="btn btn-secondary" type="button">Custom popover</button>
        </span>
    """

    assert_html(rendered, expected)


def test_popover_dismissible(render, assert_html):
    rendered = render("""
<c-bs-popover title="Dismissible popover" content="And here's some amazing content. It's very engaging. Right?" placement="top" trigger="focus">
  <c-bs-button as_="a" variant="danger" size="lg" c-attrs="{'tabindex': '0'}">Dismissible popover</c-bs-button>
</c-bs-popover>
""")

    expected = """
        <span data-bs-toggle="popover" data-bs-title="Dismissible popover" data-bs-content="And here's some amazing content. It's very engaging. Right?" data-bs-placement="top" data-bs-trigger="focus">
            <a tabindex="0" class="btn btn-lg btn-danger" role="button">Dismissible popover</a>
        </span>
    """

    assert_html(rendered, expected)


def test_popover_disabled_button_wrapper(render, assert_html):
    rendered = render("""
<c-bs-popover title="Disabled popover" content="Popover on disabled button" placement="top" trigger="hover">
  <span class="d-inline-block" tabindex="0">
    <c-bs-button variant="primary" type="button" c-disabled="True">Disabled button</c-bs-button>
  </span>
</c-bs-popover>
""")

    expected = """
        <span data-bs-toggle="popover" data-bs-title="Disabled popover" data-bs-content="Popover on disabled button" data-bs-placement="top" data-bs-trigger="hover">
            <span class="d-inline-block" tabindex="0">
                <button class="btn btn-primary" type="button" disabled>Disabled button</button>
            </span>
        </span>
    """

    assert_html(rendered, expected)
