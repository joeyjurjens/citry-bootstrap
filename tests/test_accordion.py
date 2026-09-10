def test_basic(render, assert_html):
    rendered = render("""
<c-bs-accordion>
  <c-bs-accordion-item c-default_open="True">
    <c-bs-accordion-header>Accordion Item #1</c-bs-accordion-header>
    <c-bs-accordion-body>
      <strong>This is the first item's accordion body.</strong>
      It is shown by default, until the collapse plugin adds the appropriate classes that we use to style each element. These classes control the overall appearance, as well as the showing and hiding via CSS transitions. You can modify any of this with custom CSS or overriding our default variables. It's also worth noting that just about any HTML can go within the
      <code>.accordion-body</code>, though the transition does limit overflow.
    </c-bs-accordion-body>
  </c-bs-accordion-item>
  <c-bs-accordion-item>
    <c-bs-accordion-header>Accordion Item #2</c-bs-accordion-header>
    <c-bs-accordion-body>
      <strong>This is the second item's accordion body.</strong>
      It is hidden by default, until the collapse plugin adds the appropriate classes that we use to style each element. These classes control the overall appearance, as well as the showing and hiding via CSS transitions. You can modify any of this with custom CSS or overriding our default variables. It's also worth noting that just about any HTML can go within the
      <code>.accordion-body</code>, though the transition does limit overflow.
    </c-bs-accordion-body>
  </c-bs-accordion-item>
  <c-bs-accordion-item>
    <c-bs-accordion-header>Accordion Item #3</c-bs-accordion-header>
    <c-bs-accordion-body>
      <strong>This is the third item's accordion body.</strong>
      It is hidden by default, until the collapse plugin adds the appropriate classes that we use to style each element. These classes control the overall appearance, as well as the showing and hiding via CSS transitions. You can modify any of this with custom CSS or overriding our default variables. It's also worth noting that just about any HTML can go within the
      <code>.accordion-body</code>, though the transition does limit overflow.
    </c-bs-accordion-body>
  </c-bs-accordion-item>
</c-bs-accordion>
""")

    expected = """
    <div class="accordion" id="accordion-ctest01">
      <div class="accordion-item">
        <h2 class="accordion-header" id="accordion-item-ctest02-heading">
          <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#accordion-item-ctest02-collapse" aria-expanded="true" aria-controls="accordion-item-ctest02-collapse">
            Accordion Item #1
          </button>
        </h2>
        <div id="accordion-item-ctest02-collapse" class="accordion-collapse collapse show" aria-labelledby="accordion-item-ctest02-heading" data-bs-parent="#accordion-ctest01">
          <div class="accordion-body">
            <strong>This is the first item's accordion body.</strong> It is shown by default, until the collapse plugin adds the appropriate classes that we use to style each element. These classes control the overall appearance, as well as the showing and hiding via CSS transitions. You can modify any of this with custom CSS or overriding our default variables. It's also worth noting that just about any HTML can go within the <code>.accordion-body</code>, though the transition does limit overflow.
          </div>
        </div>
      </div>
      <div class="accordion-item">
        <h2 class="accordion-header" id="accordion-item-ctest03-heading">
          <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#accordion-item-ctest03-collapse" aria-expanded="false" aria-controls="accordion-item-ctest03-collapse">
            Accordion Item #2
          </button>
        </h2>
        <div id="accordion-item-ctest03-collapse" class="accordion-collapse collapse" aria-labelledby="accordion-item-ctest03-heading" data-bs-parent="#accordion-ctest01">
          <div class="accordion-body">
            <strong>This is the second item's accordion body.</strong> It is hidden by default, until the collapse plugin adds the appropriate classes that we use to style each element. These classes control the overall appearance, as well as the showing and hiding via CSS transitions. You can modify any of this with custom CSS or overriding our default variables. It's also worth noting that just about any HTML can go within the <code>.accordion-body</code>, though the transition does limit overflow.
          </div>
        </div>
      </div>
      <div class="accordion-item">
        <h2 class="accordion-header" id="accordion-item-ctest04-heading">
          <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#accordion-item-ctest04-collapse" aria-expanded="false" aria-controls="accordion-item-ctest04-collapse">
            Accordion Item #3
          </button>
        </h2>
        <div id="accordion-item-ctest04-collapse" class="accordion-collapse collapse" aria-labelledby="accordion-item-ctest04-heading" data-bs-parent="#accordion-ctest01">
          <div class="accordion-body">
            <strong>This is the third item's accordion body.</strong> It is hidden by default, until the collapse plugin adds the appropriate classes that we use to style each element. These classes control the overall appearance, as well as the showing and hiding via CSS transitions. You can modify any of this with custom CSS or overriding our default variables. It's also worth noting that just about any HTML can go within the <code>.accordion-body</code>, though the transition does limit overflow.
          </div>
        </div>
      </div>
    </div>
    """

    assert_html(rendered, expected)


def test_with_icon_in_header(render, assert_html):
    rendered = render("""
<c-bs-accordion>
  <c-bs-accordion-item c-default_open="True">
    <c-bs-accordion-header>
      <i class="bi bi-info-circle"></i>
      Accordion Item with Icon
    </c-bs-accordion-header>
    <c-bs-accordion-body>This accordion item has an icon in the header.</c-bs-accordion-body>
  </c-bs-accordion-item>
</c-bs-accordion>
""")

    assert '<i class="bi bi-info-circle"></i>' in rendered
    assert "Accordion Item with Icon" in rendered


def test_with_badge_in_header(render, assert_contains):
    rendered = render("""
<c-bs-accordion>
  <c-bs-accordion-item c-default_open="True">
    <c-bs-accordion-header>
      Accordion Item
      <c-bs-badge bg="primary">New</c-bs-badge>
    </c-bs-accordion-header>
    <c-bs-accordion-body>This accordion item has a badge in the header.</c-bs-accordion-body>
  </c-bs-accordion-item>
</c-bs-accordion>
""")

    assert_contains(rendered, '<span class="badge text-bg-primary">New</span>')
    assert "Accordion Item" in rendered


def test_flush(render, assert_html):
    rendered = render("""
<c-bs-accordion c-flush="True">
  <c-bs-accordion-item>
    <c-bs-accordion-header>Accordion Item #1</c-bs-accordion-header>
    <c-bs-accordion-body>
      Placeholder content for this accordion, which is intended to demonstrate the
      <code>.accordion-flush</code>
      class. This is the first item's accordion body.
    </c-bs-accordion-body>
  </c-bs-accordion-item>
  <c-bs-accordion-item>
    <c-bs-accordion-header>Accordion Item #2</c-bs-accordion-header>
    <c-bs-accordion-body>
      Placeholder content for this accordion, which is intended to demonstrate the
      <code>.accordion-flush</code>
      class. This is the second item's accordion body. Let's imagine this being filled with some actual content.
    </c-bs-accordion-body>
  </c-bs-accordion-item>
  <c-bs-accordion-item>
    <c-bs-accordion-header>Accordion Item #3</c-bs-accordion-header>
    <c-bs-accordion-body>
      Placeholder content for this accordion, which is intended to demonstrate the
      <code>.accordion-flush</code>
      class. This is the third item's accordion body. Nothing more exciting happening here in terms of content, but just filling up the space to make it look, at least at first glance, a bit more representative of how this would look in a real-world application.
    </c-bs-accordion-body>
  </c-bs-accordion-item>
</c-bs-accordion>
""")

    expected = """
    <div class="accordion accordion-flush" id="accordion-ctest01">
      <div class="accordion-item">
        <h2 class="accordion-header" id="accordion-item-ctest02-heading">
          <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#accordion-item-ctest02-collapse" aria-expanded="false" aria-controls="accordion-item-ctest02-collapse">
            Accordion Item #1
          </button>
        </h2>
        <div id="accordion-item-ctest02-collapse" class="accordion-collapse collapse" aria-labelledby="accordion-item-ctest02-heading" data-bs-parent="#accordion-ctest01">
          <div class="accordion-body">Placeholder content for this accordion, which is intended to demonstrate the <code>.accordion-flush</code> class. This is the first item's accordion body.</div>
        </div>
      </div>
      <div class="accordion-item">
        <h2 class="accordion-header" id="accordion-item-ctest03-heading">
          <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#accordion-item-ctest03-collapse" aria-expanded="false" aria-controls="accordion-item-ctest03-collapse">
            Accordion Item #2
          </button>
        </h2>
        <div id="accordion-item-ctest03-collapse" class="accordion-collapse collapse" aria-labelledby="accordion-item-ctest03-heading" data-bs-parent="#accordion-ctest01">
          <div class="accordion-body">Placeholder content for this accordion, which is intended to demonstrate the <code>.accordion-flush</code> class. This is the second item's accordion body. Let's imagine this being filled with some actual content.</div>
        </div>
      </div>
      <div class="accordion-item">
        <h2 class="accordion-header" id="accordion-item-ctest04-heading">
          <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#accordion-item-ctest04-collapse" aria-expanded="false" aria-controls="accordion-item-ctest04-collapse">
            Accordion Item #3
          </button>
        </h2>
        <div id="accordion-item-ctest04-collapse" class="accordion-collapse collapse" aria-labelledby="accordion-item-ctest04-heading" data-bs-parent="#accordion-ctest01">
          <div class="accordion-body">Placeholder content for this accordion, which is intended to demonstrate the <code>.accordion-flush</code> class. This is the third item's accordion body. Nothing more exciting happening here in terms of content, but just filling up the space to make it look, at least at first glance, a bit more representative of how this would look in a real-world application.</div>
        </div>
      </div>
    </div>
    """

    assert_html(rendered, expected)


def test_always_open(render, assert_html):
    rendered = render("""
<c-bs-accordion c-always_open="True">
  <c-bs-accordion-item c-default_open="True">
    <c-bs-accordion-header>Accordion Item #1</c-bs-accordion-header>
    <c-bs-accordion-body>
      <strong>This is the first item's accordion body.</strong>
      It is shown by default, until the collapse plugin adds the appropriate classes that we use to style each element. These classes control the overall appearance, as well as the showing and hiding via CSS transitions. You can modify any of this with custom CSS or overriding our default variables. It's also worth noting that just about any HTML can go within the
      <code>.accordion-body</code>, though the transition does limit overflow.
    </c-bs-accordion-body>
  </c-bs-accordion-item>
  <c-bs-accordion-item>
    <c-bs-accordion-header>Accordion Item #2</c-bs-accordion-header>
    <c-bs-accordion-body>
      <strong>This is the second item's accordion body.</strong>
      It is hidden by default, until the collapse plugin adds the appropriate classes that we use to style each element. These classes control the overall appearance, as well as the showing and hiding via CSS transitions. You can modify any of this with custom CSS or overriding our default variables. It's also worth noting that just about any HTML can go within the
      <code>.accordion-body</code>, though the transition does limit overflow.
    </c-bs-accordion-body>
  </c-bs-accordion-item>
  <c-bs-accordion-item>
    <c-bs-accordion-header>Accordion Item #3</c-bs-accordion-header>
    <c-bs-accordion-body>
      <strong>This is the third item's accordion body.</strong>
      It is hidden by default, until the collapse plugin adds the appropriate classes that we use to style each element. These classes control the overall appearance, as well as the showing and hiding via CSS transitions. You can modify any of this with custom CSS or overriding our default variables. It's also worth noting that just about any HTML can go within the
      <code>.accordion-body</code>, though the transition does limit overflow.
    </c-bs-accordion-body>
  </c-bs-accordion-item>
</c-bs-accordion>
""")

    expected = """
    <div class="accordion" id="accordion-ctest01">
      <div class="accordion-item">
        <h2 class="accordion-header" id="accordion-item-ctest02-heading">
          <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#accordion-item-ctest02-collapse" aria-expanded="true" aria-controls="accordion-item-ctest02-collapse">
            Accordion Item #1
          </button>
        </h2>
        <div id="accordion-item-ctest02-collapse" class="accordion-collapse collapse show" aria-labelledby="accordion-item-ctest02-heading">
          <div class="accordion-body">
            <strong>This is the first item's accordion body.</strong> It is shown by default, until the collapse plugin adds the appropriate classes that we use to style each element. These classes control the overall appearance, as well as the showing and hiding via CSS transitions. You can modify any of this with custom CSS or overriding our default variables. It's also worth noting that just about any HTML can go within the <code>.accordion-body</code>, though the transition does limit overflow.
          </div>
        </div>
      </div>
      <div class="accordion-item">
        <h2 class="accordion-header" id="accordion-item-ctest03-heading">
          <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#accordion-item-ctest03-collapse" aria-expanded="false" aria-controls="accordion-item-ctest03-collapse">
            Accordion Item #2
          </button>
        </h2>
        <div id="accordion-item-ctest03-collapse" class="accordion-collapse collapse" aria-labelledby="accordion-item-ctest03-heading">
          <div class="accordion-body">
            <strong>This is the second item's accordion body.</strong> It is hidden by default, until the collapse plugin adds the appropriate classes that we use to style each element. These classes control the overall appearance, as well as the showing and hiding via CSS transitions. You can modify any of this with custom CSS or overriding our default variables. It's also worth noting that just about any HTML can go within the <code>.accordion-body</code>, though the transition does limit overflow.
          </div>
        </div>
      </div>
      <div class="accordion-item">
        <h2 class="accordion-header" id="accordion-item-ctest04-heading">
          <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#accordion-item-ctest04-collapse" aria-expanded="false" aria-controls="accordion-item-ctest04-collapse">
            Accordion Item #3
          </button>
        </h2>
        <div id="accordion-item-ctest04-collapse" class="accordion-collapse collapse" aria-labelledby="accordion-item-ctest04-heading">
          <div class="accordion-body">
            <strong>This is the third item's accordion body.</strong> It is hidden by default, until the collapse plugin adds the appropriate classes that we use to style each element. These classes control the overall appearance, as well as the showing and hiding via CSS transitions. You can modify any of this with custom CSS or overriding our default variables. It's also worth noting that just about any HTML can go within the <code>.accordion-body</code>, though the transition does limit overflow.
          </div>
        </div>
      </div>
    </div>
    """

    assert_html(rendered, expected)
