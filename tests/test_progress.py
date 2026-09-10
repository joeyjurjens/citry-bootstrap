def test_basic(render, assert_html):
    rendered = render("""
<c-bs-progress>
  <c-bs-progress-bar c-now="25" />
</c-bs-progress>
""")

    expected = """
        <div class="progress">
          <div class="progress-bar" style="width: 25.0%"></div>
        </div>
    """

    assert_html(rendered, expected)


def test_basic_0_percent(render, assert_html):
    rendered = render("""
<c-bs-progress>
  <c-bs-progress-bar c-now="0" />
</c-bs-progress>
""")

    expected = """
        <div class="progress">
          <div class="progress-bar" style="width: 0.0%"></div>
        </div>
    """

    assert_html(rendered, expected)


def test_basic_50_percent(render, assert_html):
    rendered = render("""
<c-bs-progress>
  <c-bs-progress-bar c-now="50" />
</c-bs-progress>
""")

    expected = """
        <div class="progress">
          <div class="progress-bar" style="width: 50.0%"></div>
        </div>
    """

    assert_html(rendered, expected)


def test_basic_75_percent(render, assert_html):
    rendered = render("""
<c-bs-progress>
  <c-bs-progress-bar c-now="75" />
</c-bs-progress>
""")

    expected = """
        <div class="progress">
          <div class="progress-bar" style="width: 75.0%"></div>
        </div>
    """

    assert_html(rendered, expected)


def test_basic_100_percent(render, assert_html):
    rendered = render("""
<c-bs-progress>
  <c-bs-progress-bar c-now="100" />
</c-bs-progress>
""")

    expected = """
        <div class="progress">
          <div class="progress-bar" style="width: 100.0%"></div>
        </div>
    """

    assert_html(rendered, expected)


# Heights
def test_height_1px(render, assert_html):
    rendered = render("""
<c-bs-progress height="1px">
  <c-bs-progress-bar c-now="25" />
</c-bs-progress>
""")

    expected = """
        <div class="progress" style="height: 1px;">
          <div class="progress-bar" style="width: 25.0%"></div>
        </div>
    """

    assert_html(rendered, expected)


def test_height_20px(render, assert_html):
    rendered = render("""
<c-bs-progress height="20px">
  <c-bs-progress-bar c-now="25" />
</c-bs-progress>
""")

    expected = """
        <div class="progress" style="height: 20px;">
          <div class="progress-bar" style="width: 25.0%"></div>
        </div>
    """

    assert_html(rendered, expected)


# With Label
def test_with_label(render, assert_html):
    rendered = render("""
<c-bs-progress>
  <c-bs-progress-bar c-now="25">25%</c-bs-progress-bar>
</c-bs-progress>
""")

    expected = """
        <div class="progress">
          <div class="progress-bar" style="width: 25.0%">25%</div>
        </div>
    """

    assert_html(rendered, expected)


# Background Colors - All 8 Variants
def test_variant_success(render, assert_html):
    rendered = render("""
<c-bs-progress>
  <c-bs-progress-bar c-now="25" variant="success" />
</c-bs-progress>
""")

    expected = """
        <div class="progress">
          <div class="progress-bar bg-success" style="width: 25.0%"></div>
        </div>
    """

    assert_html(rendered, expected)


def test_variant_info(render, assert_html):
    rendered = render("""
<c-bs-progress>
  <c-bs-progress-bar c-now="50" variant="info" />
</c-bs-progress>
""")

    expected = """
        <div class="progress">
          <div class="progress-bar bg-info" style="width: 50.0%"></div>
        </div>
    """

    assert_html(rendered, expected)


def test_variant_warning(render, assert_html):
    rendered = render("""
<c-bs-progress>
  <c-bs-progress-bar c-now="75" variant="warning" />
</c-bs-progress>
""")

    expected = """
        <div class="progress">
          <div class="progress-bar bg-warning" style="width: 75.0%"></div>
        </div>
    """

    assert_html(rendered, expected)


def test_variant_danger(render, assert_html):
    rendered = render("""
<c-bs-progress>
  <c-bs-progress-bar c-now="100" variant="danger" />
</c-bs-progress>
""")

    expected = """
        <div class="progress">
          <div class="progress-bar bg-danger" style="width: 100.0%"></div>
        </div>
    """

    assert_html(rendered, expected)


def test_variant_primary(render, assert_html):
    rendered = render("""
<c-bs-progress>
  <c-bs-progress-bar c-now="30" variant="primary" />
</c-bs-progress>
""")

    expected = """
        <div class="progress">
          <div class="progress-bar bg-primary" style="width: 30.0%"></div>
        </div>
    """

    assert_html(rendered, expected)


def test_variant_secondary(render, assert_html):
    rendered = render("""
<c-bs-progress>
  <c-bs-progress-bar c-now="40" variant="secondary" />
</c-bs-progress>
""")

    expected = """
        <div class="progress">
          <div class="progress-bar bg-secondary" style="width: 40.0%"></div>
        </div>
    """

    assert_html(rendered, expected)


def test_variant_light(render, assert_html):
    rendered = render("""
<c-bs-progress>
  <c-bs-progress-bar c-now="60" variant="light" />
</c-bs-progress>
""")

    expected = """
        <div class="progress">
          <div class="progress-bar bg-light" style="width: 60.0%"></div>
        </div>
    """

    assert_html(rendered, expected)


def test_variant_dark(render, assert_html):
    rendered = render("""
<c-bs-progress>
  <c-bs-progress-bar c-now="80" variant="dark" />
</c-bs-progress>
""")

    expected = """
        <div class="progress">
          <div class="progress-bar bg-dark" style="width: 80.0%"></div>
        </div>
    """

    assert_html(rendered, expected)


# Variants with Labels
def test_variant_success_with_label(render, assert_html):
    rendered = render("""
<c-bs-progress>
  <c-bs-progress-bar c-now="25" variant="success">25%</c-bs-progress-bar>
</c-bs-progress>
""")

    expected = """
        <div class="progress">
          <div class="progress-bar bg-success" style="width: 25.0%">25%</div>
        </div>
    """

    assert_html(rendered, expected)


def test_variant_info_with_label(render, assert_html):
    rendered = render("""
<c-bs-progress>
  <c-bs-progress-bar c-now="50" variant="info">50%</c-bs-progress-bar>
</c-bs-progress>
""")

    expected = """
        <div class="progress">
          <div class="progress-bar bg-info" style="width: 50.0%">50%</div>
        </div>
    """

    assert_html(rendered, expected)


def test_variant_warning_with_label(render, assert_html):
    rendered = render("""
<c-bs-progress>
  <c-bs-progress-bar c-now="75" variant="warning">75%</c-bs-progress-bar>
</c-bs-progress>
""")

    expected = """
        <div class="progress">
          <div class="progress-bar bg-warning" style="width: 75.0%">75%</div>
        </div>
    """

    assert_html(rendered, expected)


def test_variant_danger_with_label(render, assert_html):
    rendered = render("""
<c-bs-progress>
  <c-bs-progress-bar c-now="100" variant="danger">100%</c-bs-progress-bar>
</c-bs-progress>
""")

    expected = """
        <div class="progress">
          <div class="progress-bar bg-danger" style="width: 100.0%">100%</div>
        </div>
    """

    assert_html(rendered, expected)


# Multiple Bars
def test_multiple_bars(render, assert_html):
    rendered = render("""
<c-bs-progress-stacked>
  <c-bs-progress c-attrs="{'style': 'width: 15%'}">
    <c-bs-progress-bar c-now="15" />
  </c-bs-progress>
  <c-bs-progress c-attrs="{'style': 'width: 30%'}">
    <c-bs-progress-bar c-now="30" variant="success" />
  </c-bs-progress>
  <c-bs-progress c-attrs="{'style': 'width: 20%'}">
    <c-bs-progress-bar c-now="20" variant="info" />
  </c-bs-progress>
</c-bs-progress-stacked>
""")

    assert "progress-stacked" in rendered
    assert "bg-success" in rendered
    assert "bg-info" in rendered


# Striped Bars
def test_striped_basic(render, assert_html):
    rendered = render("""
<c-bs-progress>
  <c-bs-progress-bar c-now="10" c-striped="True" />
</c-bs-progress>
""")

    expected = """
        <div class="progress">
          <div class="progress-bar progress-bar-striped" style="width: 10.0%"></div>
        </div>
    """

    assert_html(rendered, expected)


def test_striped_success(render, assert_html):
    rendered = render("""
<c-bs-progress>
  <c-bs-progress-bar c-now="25" variant="success" c-striped="True" />
</c-bs-progress>
""")

    expected = """
        <div class="progress">
          <div class="progress-bar progress-bar-striped bg-success" style="width: 25.0%"></div>
        </div>
    """

    assert_html(rendered, expected)


def test_striped_info(render, assert_html):
    rendered = render("""
<c-bs-progress>
  <c-bs-progress-bar c-now="50" variant="info" c-striped="True" />
</c-bs-progress>
""")

    expected = """
        <div class="progress">
          <div class="progress-bar progress-bar-striped bg-info" style="width: 50.0%"></div>
        </div>
    """

    assert_html(rendered, expected)


def test_striped_warning(render, assert_html):
    rendered = render("""
<c-bs-progress>
  <c-bs-progress-bar c-now="75" variant="warning" c-striped="True" />
</c-bs-progress>
""")

    expected = """
        <div class="progress">
          <div class="progress-bar progress-bar-striped bg-warning" style="width: 75.0%"></div>
        </div>
    """

    assert_html(rendered, expected)


def test_striped_danger(render, assert_html):
    rendered = render("""
<c-bs-progress>
  <c-bs-progress-bar c-now="100" variant="danger" c-striped="True" />
</c-bs-progress>
""")

    expected = """
        <div class="progress">
          <div class="progress-bar progress-bar-striped bg-danger" style="width: 100.0%"></div>
        </div>
    """

    assert_html(rendered, expected)


def test_striped_primary(render, assert_html):
    rendered = render("""
<c-bs-progress>
  <c-bs-progress-bar c-now="40" variant="primary" c-striped="True" />
</c-bs-progress>
""")

    expected = """
        <div class="progress">
          <div class="progress-bar progress-bar-striped bg-primary" style="width: 40.0%"></div>
        </div>
    """

    assert_html(rendered, expected)


def test_striped_secondary(render, assert_html):
    rendered = render("""
<c-bs-progress>
  <c-bs-progress-bar c-now="60" variant="secondary" c-striped="True" />
</c-bs-progress>
""")

    expected = """
        <div class="progress">
          <div class="progress-bar progress-bar-striped bg-secondary" style="width: 60.0%"></div>
        </div>
    """

    assert_html(rendered, expected)


def test_striped_light(render, assert_html):
    rendered = render("""
<c-bs-progress>
  <c-bs-progress-bar c-now="70" variant="light" c-striped="True" />
</c-bs-progress>
""")

    expected = """
        <div class="progress">
          <div class="progress-bar progress-bar-striped bg-light" style="width: 70.0%"></div>
        </div>
    """

    assert_html(rendered, expected)


def test_striped_dark(render, assert_html):
    rendered = render("""
<c-bs-progress>
  <c-bs-progress-bar c-now="90" variant="dark" c-striped="True" />
</c-bs-progress>
""")

    expected = """
        <div class="progress">
          <div class="progress-bar progress-bar-striped bg-dark" style="width: 90.0%"></div>
        </div>
    """

    assert_html(rendered, expected)


# Animated Striped Bars
def test_animated_striped(render, assert_html):
    rendered = render("""
<c-bs-progress>
  <c-bs-progress-bar c-now="75" c-animated="True" />
</c-bs-progress>
""")

    expected = """
        <div class="progress">
          <div class="progress-bar progress-bar-striped progress-bar-animated" style="width: 75.0%"></div>
        </div>
    """

    assert_html(rendered, expected)


def test_animated_striped_success(render, assert_html):
    rendered = render("""
<c-bs-progress>
  <c-bs-progress-bar c-now="50" variant="success" c-animated="True" />
</c-bs-progress>
""")

    expected = """
        <div class="progress">
          <div class="progress-bar progress-bar-striped progress-bar-animated bg-success" style="width: 50.0%"></div>
        </div>
    """

    assert_html(rendered, expected)


def test_animated_striped_info(render, assert_html):
    rendered = render("""
<c-bs-progress>
  <c-bs-progress-bar c-now="60" variant="info" c-animated="True" />
</c-bs-progress>
""")

    expected = """
        <div class="progress">
          <div class="progress-bar progress-bar-striped progress-bar-animated bg-info" style="width: 60.0%"></div>
        </div>
    """

    assert_html(rendered, expected)


def test_animated_striped_warning(render, assert_html):
    rendered = render("""
<c-bs-progress>
  <c-bs-progress-bar c-now="80" variant="warning" c-animated="True" />
</c-bs-progress>
""")

    expected = """
        <div class="progress">
          <div class="progress-bar progress-bar-striped progress-bar-animated bg-warning" style="width: 80.0%"></div>
        </div>
    """

    assert_html(rendered, expected)


def test_animated_striped_danger(render, assert_html):
    rendered = render("""
<c-bs-progress>
  <c-bs-progress-bar c-now="90" variant="danger" c-animated="True" />
</c-bs-progress>
""")

    expected = """
        <div class="progress">
          <div class="progress-bar progress-bar-striped progress-bar-animated bg-danger" style="width: 90.0%"></div>
        </div>
    """

    assert_html(rendered, expected)
