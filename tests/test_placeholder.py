def test_basic(render, assert_html):
    rendered = render("""
<c-bs-card-text c-attrs="{'class': 'placeholder-glow'}">
  <c-bs-placeholder c-xs="7" />
  <c-bs-placeholder c-xs="4" />
  <c-bs-placeholder c-xs="4" />
  <c-bs-placeholder c-xs="6" />
  <c-bs-placeholder c-xs="8" />
</c-bs-card-text>
""")

    expected = """
        <p class="card-text placeholder-glow">
            <span class="placeholder col-7"></span>
            <span class="placeholder col-4"></span>
            <span class="placeholder col-4"></span>
            <span class="placeholder col-6"></span>
            <span class="placeholder col-8"></span>
        </p>
    """

    assert_html(rendered, expected)


def test_placeholder_width_variants(render, assert_html):
    rendered = render("""
<div>
  <c-bs-placeholder c-xs="6" />
  <c-bs-placeholder c-xs="12" />
  <c-bs-placeholder c-xs="3" />
</div>
""")

    expected = """
        <div>
            <span class="placeholder col-6"></span>
            <span class="placeholder col-12"></span>
            <span class="placeholder col-3"></span>
        </div>
    """

    assert_html(rendered, expected)


def test_placeholder_size_large(render, assert_html):
    rendered = render("""
<c-bs-placeholder c-xs="12" size="lg" />
""")

    expected = """
        <span class="placeholder col-12 placeholder-lg"></span>
    """

    assert_html(rendered, expected)


def test_placeholder_size_small(render, assert_html):
    rendered = render("""
<c-bs-placeholder c-xs="12" size="sm" />
""")

    expected = """
        <span class="placeholder col-12 placeholder-sm"></span>
    """

    assert_html(rendered, expected)


def test_placeholder_size_extra_small(render, assert_html):
    rendered = render("""
<c-bs-placeholder c-xs="12" size="xs" />
""")

    expected = """
        <span class="placeholder col-12 placeholder-xs"></span>
    """

    assert_html(rendered, expected)


def test_placeholder_bg_primary(render, assert_html):
    rendered = render("""
<c-bs-placeholder c-xs="12" bg="primary" />
""")

    expected = """
        <span class="placeholder col-12 bg-primary"></span>
    """

    assert_html(rendered, expected)


def test_placeholder_bg_secondary(render, assert_html):
    rendered = render("""
<c-bs-placeholder c-xs="12" bg="secondary" />
""")

    expected = """
        <span class="placeholder col-12 bg-secondary"></span>
    """

    assert_html(rendered, expected)


def test_placeholder_bg_success(render, assert_html):
    rendered = render("""
<c-bs-placeholder c-xs="12" bg="success" />
""")

    expected = """
        <span class="placeholder col-12 bg-success"></span>
    """

    assert_html(rendered, expected)


def test_placeholder_bg_danger(render, assert_html):
    rendered = render("""
<c-bs-placeholder c-xs="12" bg="danger" />
""")

    expected = """
        <span class="placeholder col-12 bg-danger"></span>
    """

    assert_html(rendered, expected)


def test_placeholder_bg_warning(render, assert_html):
    rendered = render("""
<c-bs-placeholder c-xs="12" bg="warning" />
""")

    expected = """
        <span class="placeholder col-12 bg-warning"></span>
    """

    assert_html(rendered, expected)


def test_placeholder_bg_info(render, assert_html):
    rendered = render("""
<c-bs-placeholder c-xs="12" bg="info" />
""")

    expected = """
        <span class="placeholder col-12 bg-info"></span>
    """

    assert_html(rendered, expected)


def test_placeholder_bg_light(render, assert_html):
    rendered = render("""
<c-bs-placeholder c-xs="12" bg="light" />
""")

    expected = """
        <span class="placeholder col-12 bg-light"></span>
    """

    assert_html(rendered, expected)


def test_placeholder_bg_dark(render, assert_html):
    rendered = render("""
<c-bs-placeholder c-xs="12" bg="dark" />
""")

    expected = """
        <span class="placeholder col-12 bg-dark"></span>
    """

    assert_html(rendered, expected)


def test_placeholder_animation_glow(render, assert_html):
    rendered = render("""
<p class="placeholder-glow">
  <c-bs-placeholder c-xs="12" />
</p>
""")

    expected = """
        <p class="placeholder-glow">
            <span class="placeholder col-12"></span>
        </p>
    """

    assert_html(rendered, expected)


def test_placeholder_animation_wave(render, assert_html):
    rendered = render("""
<p class="placeholder-wave">
  <c-bs-placeholder c-xs="12" />
</p>
""")

    expected = """
        <p class="placeholder-wave">
            <span class="placeholder col-12"></span>
        </p>
    """

    assert_html(rendered, expected)


def test_placeholder_with_animation_prop(render, assert_html):
    rendered = render("""
<c-bs-placeholder c-xs="12" animation="glow" />
""")

    expected = """
        <span class="placeholder col-12 placeholder-glow"></span>
    """

    assert_html(rendered, expected)


def test_placeholder_with_wave_animation(render, assert_html):
    rendered = render("""
<c-bs-placeholder c-xs="12" animation="wave" />
""")

    expected = """
        <span class="placeholder col-12 placeholder-wave"></span>
    """

    assert_html(rendered, expected)


def test_placeholder_button_primary(render, assert_html):
    rendered = render("""
<c-bs-placeholder-button variant="primary" c-xs="6" />
""")

    expected = """
        <button class="btn btn-primary placeholder col-6" disabled aria-hidden="true"></button>
    """

    assert_html(rendered, expected)


def test_placeholder_button_secondary(render, assert_html):
    rendered = render("""
<c-bs-placeholder-button variant="secondary" c-xs="4" />
""")

    expected = """
        <button class="btn btn-secondary placeholder col-4" disabled aria-hidden="true"></button>
    """

    assert_html(rendered, expected)


def test_placeholder_button_success(render, assert_html):
    rendered = render("""
<c-bs-placeholder-button variant="success" c-xs="6" />
""")

    expected = """
        <button class="btn btn-success placeholder col-6" disabled aria-hidden="true"></button>
    """

    assert_html(rendered, expected)


def test_placeholder_button_danger(render, assert_html):
    rendered = render("""
<c-bs-placeholder-button variant="danger" c-xs="6" />
""")

    expected = """
        <button class="btn btn-danger placeholder col-6" disabled aria-hidden="true"></button>
    """

    assert_html(rendered, expected)


def test_placeholder_custom_element(render, assert_html):
    rendered = render("""
<c-bs-placeholder as_="div" c-xs="12" />
""")

    expected = """
        <div class="placeholder col-12"></div>
    """

    assert_html(rendered, expected)


def test_placeholder_combined_size_and_color(render, assert_html):
    rendered = render("""
<c-bs-placeholder c-xs="12" size="lg" bg="primary" />
""")

    expected = """
        <span class="placeholder col-12 placeholder-lg bg-primary"></span>
    """

    assert_html(rendered, expected)


def test_placeholder_combined_all_props(render, assert_html):
    rendered = render("""
<c-bs-placeholder c-xs="8" size="sm" bg="success" animation="wave" />
""")

    expected = """
        <span class="placeholder col-8 placeholder-sm bg-success placeholder-wave"></span>
    """

    assert_html(rendered, expected)
