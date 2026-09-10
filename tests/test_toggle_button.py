def test_checkbox_single(render, assert_html):
    rendered = render("""
<c-bs-toggle-button variant="primary" c-outline="False" c-attrs="{'id': 'btn-check'}">Single toggle</c-bs-toggle-button>
""")

    expected = """
        <input type="checkbox" class="btn-check" id="btn-check" autocomplete="off">
        <label class="btn btn-primary" for="btn-check">Single toggle</label>
    """

    assert_html(rendered, expected)


def test_checkbox_checked(render, assert_html):
    rendered = render("""
<c-bs-toggle-button c-checked="True" variant="primary" c-outline="False" c-attrs="{'id': 'btn-check-2'}">Checked</c-bs-toggle-button>
""")

    expected = """
        <input type="checkbox" class="btn-check" id="btn-check-2" checked autocomplete="off">
        <label class="btn btn-primary" for="btn-check-2">Checked</label>
    """

    assert_html(rendered, expected)


def test_checkbox_disabled(render, assert_html):
    rendered = render("""
<c-bs-toggle-button c-disabled="True" variant="primary" c-outline="False" c-attrs="{'id': 'btn-check-3'}">Disabled</c-bs-toggle-button>
""")

    expected = """
        <input type="checkbox" class="btn-check" id="btn-check-3" autocomplete="off" disabled>
        <label class="btn btn-primary" for="btn-check-3">Disabled</label>
    """

    assert_html(rendered, expected)


def test_radio_checked(render, assert_html):
    rendered = render("""
<c-bs-toggle-button type="radio" name="options" c-checked="True" variant="secondary" c-outline="False" c-attrs="{'id': 'option1'}">Checked</c-bs-toggle-button>
""")

    expected = """
        <input type="radio" class="btn-check" name="options" id="option1" autocomplete="off" checked>
        <label class="btn btn-secondary" for="option1">Checked</label>
    """

    assert_html(rendered, expected)


def test_radio_unchecked(render, assert_html):
    rendered = render("""
<c-bs-toggle-button type="radio" name="options" variant="secondary" c-outline="False" c-attrs="{'id': 'option2'}">Radio</c-bs-toggle-button>
""")

    expected = """
        <input type="radio" class="btn-check" name="options" id="option2" autocomplete="off">
        <label class="btn btn-secondary" for="option2">Radio</label>
    """

    assert_html(rendered, expected)


def test_radio_disabled(render, assert_html):
    rendered = render("""
<c-bs-toggle-button type="radio" name="options" c-disabled="True" variant="secondary" c-outline="False" c-attrs="{'id': 'option3'}">Disabled</c-bs-toggle-button>
""")

    expected = """
        <input type="radio" class="btn-check" name="options" id="option3" autocomplete="off" disabled>
        <label class="btn btn-secondary" for="option3">Disabled</label>
    """

    assert_html(rendered, expected)
