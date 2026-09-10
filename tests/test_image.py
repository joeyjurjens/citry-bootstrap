def test_fluid(render, assert_html):
    rendered = render("""
<c-bs-image src="https://placehold.net/600x400.png" alt="Responsive image" c-fluid="True" />
""")

    expected = """
        <img src="https://placehold.net/600x400.png" class="img-fluid" alt="Responsive image">
    """

    assert_html(rendered, expected)


def test_thumbnail(render, assert_html):
    rendered = render("""
<c-bs-image src="https://placehold.net/600x400.png" alt="Thumbnail image" c-thumbnail="True" />
""")

    expected = """
        <img src="https://placehold.net/600x400.png" class="img-thumbnail" alt="Thumbnail image">
    """

    assert_html(rendered, expected)


def test_rounded(render, assert_html):
    rendered = render("""
<c-bs-image src="https://placehold.net/600x400.png" alt="Rounded image" c-rounded="True" />
""")

    expected = """
        <img src="https://placehold.net/600x400.png" class="rounded" alt="Rounded image">
    """

    assert_html(rendered, expected)


def test_rounded_circle(render, assert_html):
    rendered = render("""
<c-bs-image src="https://placehold.net/600x400.png" alt="Circle image" c-rounded_circle="True" />
""")

    expected = """
        <img src="https://placehold.net/600x400.png" class="rounded-circle" alt="Circle image">
    """

    assert_html(rendered, expected)


def test_rounded_float_start(render, assert_html):
    rendered = render("""
<c-bs-image src="https://placehold.net/600x400.png" alt="Float start image" c-rounded="True" />
""")

    expected = """
        <img src="https://placehold.net/600x400.png" class="rounded" alt="Float start image">
    """

    assert_html(rendered, expected)


def test_rounded_float_end(render, assert_html):
    rendered = render("""
<c-bs-image src="https://placehold.net/600x400.png" alt="Float end image" c-rounded="True" />
""")

    expected = """
        <img src="https://placehold.net/600x400.png" class="rounded" alt="Float end image">
    """

    assert_html(rendered, expected)


def test_centered_block(render, assert_html):
    rendered = render("""
<c-bs-image src="https://placehold.net/600x400.png" alt="Centered image" c-rounded="True" c-attrs="{'class': 'mx-auto d-block'}" />
""")

    expected = """
        <img src="https://placehold.net/600x400.png" class="rounded mx-auto d-block" alt="Centered image">
    """

    assert_html(rendered, expected)


def test_fluid_and_thumbnail(render, assert_html):
    rendered = render("""
<c-bs-image src="https://placehold.net/600x400.png" alt="Fluid thumbnail" c-fluid="True" c-thumbnail="True" />
""")

    expected = """
        <img src="https://placehold.net/600x400.png" class="img-fluid img-thumbnail" alt="Fluid thumbnail">
    """

    assert_html(rendered, expected)


def test_all_rounded_options(render, assert_html):
    rendered = render("""
<c-bs-image src="https://placehold.net/600x400.png" alt="Fluid rounded image" c-fluid="True" c-rounded="True" />
""")

    expected = """
        <img src="https://placehold.net/600x400.png" class="img-fluid rounded" alt="Fluid rounded image">
    """

    assert_html(rendered, expected)


def test_custom_attrs(render, assert_html):
    rendered = render("""
<c-bs-image src="https://placehold.net/600x400.png" alt="Custom image" c-attrs="{'width': '200'}" />
""")

    expected = """
        <img src="https://placehold.net/600x400.png" alt="Custom image" width="200">
    """

    assert_html(rendered, expected)


def test_no_alt(render, assert_html):
    rendered = render("""
<c-bs-image src="https://placehold.net/600x400.png" />
""")

    expected = """
        <img src="https://placehold.net/600x400.png" alt="">
    """

    assert_html(rendered, expected)
