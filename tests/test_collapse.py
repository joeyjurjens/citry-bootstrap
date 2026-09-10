def test_basic(render, assert_html):
    rendered = render("""
<c-bs-collapse>
  <c-fill name="toggle">
    <c-bs-collapse-toggle c-attrs="{'class': 'btn btn-primary'}">Toggle collapse</c-bs-collapse-toggle>
  </c-fill>
  <c-fill name="default">
    <c-bs-card c-body="True">Some placeholder content for the collapse component. This panel is hidden by default but revealed when the user activates the relevant trigger.</c-bs-card>
  </c-fill>
</c-bs-collapse>
""")

    expected = """
        <button type="button" class="btn btn-primary" data-bs-toggle="collapse" data-bs-target="#collapse-ctest01" aria-expanded="false" aria-controls="collapse-ctest01">Toggle collapse</button>
        <div class="collapse" id="collapse-ctest01">
          <div class="card">
            <div class="card-body">
              Some placeholder content for the collapse component. This panel is hidden by default but revealed when the user activates the relevant trigger.
            </div>
          </div>
        </div>
    """

    assert_html(rendered, expected)


def test_multiple_targets(render, assert_html):
    rendered = render("""
<p>
  <c-bs-collapse>
    <c-fill name="toggle">
      <c-bs-collapse-toggle as_="a" c-attrs='{"class": "btn btn-primary"}'>Toggle first element</c-bs-collapse-toggle>
    </c-fill>
    <c-fill name="default">
      <c-bs-card c-body="True">Some placeholder content for the first collapse component.</c-bs-card>
    </c-fill>
  </c-bs-collapse>
  <c-bs-collapse>
    <c-fill name="toggle">
      <c-bs-collapse-toggle c-attrs='{"class": "btn btn-primary"}'>Toggle second element</c-bs-collapse-toggle>
    </c-fill>
    <c-fill name="default">
      <c-bs-card c-body="True">Some placeholder content for the second collapse component.</c-bs-card>
    </c-fill>
  </c-bs-collapse>
</p>
""")

    assert "Toggle first element" in rendered
    assert "Toggle second element" in rendered


def test_horizontal(render, assert_html):
    rendered = render("""
<c-bs-collapse c-horizontal="True">
  <c-fill name="toggle">
    <c-bs-collapse-toggle c-attrs="{'class': 'btn btn-primary'}">Toggle horizontal collapse</c-bs-collapse-toggle>
  </c-fill>
  <c-fill name="default">
    <c-bs-card c-body="True" c-attrs="{'style': 'width: 300px;'}">This is some placeholder content for a horizontal collapse. It's hidden by default and shown when triggered.</c-bs-card>
  </c-fill>
</c-bs-collapse>
""")

    expected = """
        <button type="button" class="btn btn-primary" data-bs-toggle="collapse" data-bs-target="#collapse-ctest01" aria-expanded="false" aria-controls="collapse-ctest01">Toggle horizontal collapse</button>
        <div class="collapse collapse-horizontal" id="collapse-ctest01">
          <div class="card" style="width: 300px;">
            <div class="card-body">
              This is some placeholder content for a horizontal collapse. It's hidden by default and shown when triggered.
            </div>
          </div>
        </div>
    """

    assert_html(rendered, expected)


def test_with_button_toggle(render, assert_html):
    rendered = render("""
<c-bs-collapse>
  <c-fill name="toggle">
    <c-bs-collapse-toggle c-attrs='{"class": "btn btn-primary"}'>Button with data-bs-target</c-bs-collapse-toggle>
  </c-fill>
  <c-fill name="default">
    <c-bs-card c-body="True">Some placeholder content for the collapse component. This panel is hidden by default but revealed when the user activates the relevant trigger.</c-bs-card>
  </c-fill>
</c-bs-collapse>
""")

    expected = """
        <button class="btn btn-primary" type="button" data-bs-toggle="collapse" data-bs-target="#collapse-ctest01" aria-expanded="false" aria-controls="collapse-ctest01">
          Button with data-bs-target
        </button>
        <div class="collapse" id="collapse-ctest01">
          <div class="card">
            <div class="card-body">
              Some placeholder content for the collapse component. This panel is hidden by default but revealed when the user activates the relevant trigger.
            </div>
          </div>
        </div>
    """

    assert_html(rendered, expected)


def test_with_link_toggle(render, assert_html):
    rendered = render("""
<c-bs-collapse>
  <c-fill name="toggle">
    <c-bs-collapse-toggle as_="a" c-attrs='{"class": "btn btn-primary"}'>Link with href</c-bs-collapse-toggle>
  </c-fill>
  <c-fill name="default">
    <c-bs-card c-body="True">Some placeholder content for the collapse component. This panel is hidden by default but revealed when the user activates the relevant trigger.</c-bs-card>
  </c-fill>
</c-bs-collapse>
""")

    expected = """
        <a class="btn btn-primary" data-bs-toggle="collapse" href="#collapse-ctest01" role="button" aria-expanded="false" aria-controls="collapse-ctest01">
          Link with href
        </a>
        <div class="collapse" id="collapse-ctest01">
          <div class="card">
            <div class="card-body">
              Some placeholder content for the collapse component. This panel is hidden by default but revealed when the user activates the relevant trigger.
            </div>
          </div>
        </div>
    """

    assert_html(rendered, expected)
