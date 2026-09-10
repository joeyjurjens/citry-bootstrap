def test_basic(render, assert_html):
    rendered = render("""
<c-bs-modal>
  <c-bs-modal-header>
    <c-bs-modal-title>Modal title</c-bs-modal-title>
  </c-bs-modal-header>
  <c-bs-modal-body>
    <p>Modal body text goes here.</p>
  </c-bs-modal-body>
  <c-bs-modal-footer>
    <c-bs-button variant="secondary" c-attrs="{'data-bs-dismiss': 'modal'}">Close</c-bs-button>
    <c-bs-button>Save changes</c-bs-button>
  </c-bs-modal-footer>
</c-bs-modal>
""")

    expected = """
        <div class="modal fade" id="modal-ctest01" tabindex="-1" aria-labelledby="modal-ctest01-label" aria-hidden="true">
          <div class="modal-dialog">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title" id="modal-ctest01-label">Modal title</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div class="modal-body">
                <p>Modal body text goes here.</p>
              </div>
              <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                <button type="button" class="btn btn-primary">Save changes</button>
              </div>
            </div>
          </div>
        </div>
    """

    assert_html(rendered, expected)


def test_modal_small_size(render, assert_html):
    rendered = render("""
<c-bs-modal size="sm">
  <c-bs-modal-header>
    <c-bs-modal-title>Small Modal</c-bs-modal-title>
  </c-bs-modal-header>
  <c-bs-modal-body>
    <p>This is a small modal.</p>
  </c-bs-modal-body>
</c-bs-modal>
""")

    expected = """
        <div class="modal fade" id="modal-ctest01" tabindex="-1" aria-labelledby="modal-ctest01-label" aria-hidden="true">
          <div class="modal-dialog modal-sm">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title" id="modal-ctest01-label">Small Modal</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div class="modal-body">
                <p>This is a small modal.</p>
              </div>
            </div>
          </div>
        </div>
    """

    assert_html(rendered, expected)


def test_modal_large_size(render, assert_html):
    rendered = render("""
<c-bs-modal size="lg">
  <c-bs-modal-header>
    <c-bs-modal-title>Large Modal</c-bs-modal-title>
  </c-bs-modal-header>
  <c-bs-modal-body>
    <p>This is a large modal.</p>
  </c-bs-modal-body>
</c-bs-modal>
""")

    expected = """
        <div class="modal fade" id="modal-ctest01" tabindex="-1" aria-labelledby="modal-ctest01-label" aria-hidden="true">
          <div class="modal-dialog modal-lg">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title" id="modal-ctest01-label">Large Modal</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div class="modal-body">
                <p>This is a large modal.</p>
              </div>
            </div>
          </div>
        </div>
    """

    assert_html(rendered, expected)


def test_modal_extra_large_size(render, assert_html):
    rendered = render("""
<c-bs-modal size="xl">
  <c-bs-modal-header>
    <c-bs-modal-title>Extra Large Modal</c-bs-modal-title>
  </c-bs-modal-header>
  <c-bs-modal-body>
    <p>This is an extra large modal.</p>
  </c-bs-modal-body>
</c-bs-modal>
""")

    expected = """
        <div class="modal fade" id="modal-ctest01" tabindex="-1" aria-labelledby="modal-ctest01-label" aria-hidden="true">
          <div class="modal-dialog modal-xl">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title" id="modal-ctest01-label">Extra Large Modal</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div class="modal-body">
                <p>This is an extra large modal.</p>
              </div>
            </div>
          </div>
        </div>
    """

    assert_html(rendered, expected)


def test_modal_fullscreen(render, assert_html):
    rendered = render("""
<c-bs-modal c-fullscreen="True">
  <c-bs-modal-header>
    <c-bs-modal-title>Fullscreen Modal</c-bs-modal-title>
  </c-bs-modal-header>
  <c-bs-modal-body>
    <p>This is a fullscreen modal.</p>
  </c-bs-modal-body>
</c-bs-modal>
""")

    expected = """
        <div class="modal fade" id="modal-ctest01" tabindex="-1" aria-labelledby="modal-ctest01-label" aria-hidden="true">
          <div class="modal-dialog modal-fullscreen">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title" id="modal-ctest01-label">Fullscreen Modal</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div class="modal-body">
                <p>This is a fullscreen modal.</p>
              </div>
            </div>
          </div>
        </div>
    """

    assert_html(rendered, expected)


def test_modal_fullscreen_sm_down(render, assert_html):
    rendered = render("""
<c-bs-modal fullscreen="sm">
  <c-bs-modal-header>
    <c-bs-modal-title>Fullscreen Below SM</c-bs-modal-title>
  </c-bs-modal-header>
  <c-bs-modal-body>
    <p>This modal is fullscreen below sm breakpoint.</p>
  </c-bs-modal-body>
</c-bs-modal>
""")

    expected = """
        <div class="modal fade" id="modal-ctest01" tabindex="-1" aria-labelledby="modal-ctest01-label" aria-hidden="true">
          <div class="modal-dialog modal-fullscreen-sm-down">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title" id="modal-ctest01-label">Fullscreen Below SM</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div class="modal-body">
                <p>This modal is fullscreen below sm breakpoint.</p>
              </div>
            </div>
          </div>
        </div>
    """

    assert_html(rendered, expected)


def test_modal_fullscreen_md_down(render, assert_html):
    rendered = render("""
<c-bs-modal fullscreen="md">
  <c-bs-modal-header>
    <c-bs-modal-title>Fullscreen Below MD</c-bs-modal-title>
  </c-bs-modal-header>
  <c-bs-modal-body>
    <p>This modal is fullscreen below md breakpoint.</p>
  </c-bs-modal-body>
</c-bs-modal>
""")

    expected = """
        <div class="modal fade" id="modal-ctest01" tabindex="-1" aria-labelledby="modal-ctest01-label" aria-hidden="true">
          <div class="modal-dialog modal-fullscreen-md-down">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title" id="modal-ctest01-label">Fullscreen Below MD</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div class="modal-body">
                <p>This modal is fullscreen below md breakpoint.</p>
              </div>
            </div>
          </div>
        </div>
    """

    assert_html(rendered, expected)


def test_modal_fullscreen_lg_down(render, assert_html):
    rendered = render("""
<c-bs-modal fullscreen="lg">
  <c-bs-modal-header>
    <c-bs-modal-title>Fullscreen Below LG</c-bs-modal-title>
  </c-bs-modal-header>
  <c-bs-modal-body>
    <p>This modal is fullscreen below lg breakpoint.</p>
  </c-bs-modal-body>
</c-bs-modal>
""")

    expected = """
        <div class="modal fade" id="modal-ctest01" tabindex="-1" aria-labelledby="modal-ctest01-label" aria-hidden="true">
          <div class="modal-dialog modal-fullscreen-lg-down">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title" id="modal-ctest01-label">Fullscreen Below LG</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div class="modal-body">
                <p>This modal is fullscreen below lg breakpoint.</p>
              </div>
            </div>
          </div>
        </div>
    """

    assert_html(rendered, expected)


def test_modal_centered(render, assert_html):
    rendered = render("""
<c-bs-modal c-centered="True">
  <c-bs-modal-header>
    <c-bs-modal-title>Vertically Centered Modal</c-bs-modal-title>
  </c-bs-modal-header>
  <c-bs-modal-body>
    <p>This modal is vertically centered.</p>
  </c-bs-modal-body>
</c-bs-modal>
""")

    expected = """
        <div class="modal fade" id="modal-ctest01" tabindex="-1" aria-labelledby="modal-ctest01-label" aria-hidden="true">
          <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title" id="modal-ctest01-label">Vertically Centered Modal</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div class="modal-body">
                <p>This modal is vertically centered.</p>
              </div>
            </div>
          </div>
        </div>
    """

    assert_html(rendered, expected)


def test_modal_scrollable(render, assert_html):
    rendered = render("""
<c-bs-modal c-scrollable="True">
  <c-bs-modal-header>
    <c-bs-modal-title>Scrollable Modal</c-bs-modal-title>
  </c-bs-modal-header>
  <c-bs-modal-body>
    <p>This modal has a scrollable body when content is long.</p>
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
  </c-bs-modal-body>
</c-bs-modal>
""")

    expected = """
        <div class="modal fade" id="modal-ctest01" tabindex="-1" aria-labelledby="modal-ctest01-label" aria-hidden="true">
          <div class="modal-dialog modal-dialog-scrollable">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title" id="modal-ctest01-label">Scrollable Modal</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div class="modal-body">
                <p>This modal has a scrollable body when content is long.</p>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
              </div>
            </div>
          </div>
        </div>
    """

    assert_html(rendered, expected)


def test_modal_static_backdrop(render, assert_html):
    rendered = render("""
<c-bs-modal backdrop="static" c-keyboard="False">
  <c-bs-modal-header>
    <c-bs-modal-title>Static Backdrop Modal</c-bs-modal-title>
  </c-bs-modal-header>
  <c-bs-modal-body>
    <p>This modal won't close when clicking outside.</p>
  </c-bs-modal-body>
</c-bs-modal>
""")

    expected = """
        <div class="modal fade" id="modal-ctest01" tabindex="-1" aria-labelledby="modal-ctest01-label" aria-hidden="true" data-bs-backdrop="static" data-bs-keyboard="false">
          <div class="modal-dialog">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title" id="modal-ctest01-label">Static Backdrop Modal</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div class="modal-body">
                <p>This modal won't close when clicking outside.</p>
              </div>
            </div>
          </div>
        </div>
    """

    assert_html(rendered, expected)


def test_modal_with_form(render, assert_html):
    rendered = render("""
<c-bs-modal>
  <c-bs-modal-header>
    <c-bs-modal-title>New message</c-bs-modal-title>
  </c-bs-modal-header>
  <c-bs-modal-body>
    <form>
      <div class="mb-3">
        <label for="recipient-name" class="col-form-label">Recipient:</label>
        <c-bs-form-control c-attrs="{'id': 'recipient-name'}" />
      </div>
      <div class="mb-3">
        <label for="message-text" class="col-form-label">Message:</label>
        <c-bs-form-textarea c-attrs="{'id': 'message-text'}" />
      </div>
    </form>
  </c-bs-modal-body>
  <c-bs-modal-footer>
    <c-bs-button variant="secondary" c-attrs="{'data-bs-dismiss': 'modal'}">Close</c-bs-button>
    <c-bs-button>Send message</c-bs-button>
  </c-bs-modal-footer>
</c-bs-modal>
""")

    expected = """
        <div class="modal fade" id="modal-ctest01" tabindex="-1" aria-labelledby="modal-ctest01-label" aria-hidden="true">
          <div class="modal-dialog">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title" id="modal-ctest01-label">New message</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div class="modal-body">
                <form>
                  <div class="mb-3">
                    <label for="recipient-name" class="col-form-label">Recipient:</label>
                    <input type="text" class="form-control" id="recipient-name">
                  </div>
                  <div class="mb-3">
                    <label for="message-text" class="col-form-label">Message:</label>
                    <textarea class="form-control" id="message-text" rows="3"></textarea>
                  </div>
                </form>
              </div>
              <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                <button type="button" class="btn btn-primary">Send message</button>
              </div>
            </div>
          </div>
        </div>
    """

    assert_html(rendered, expected)


def test_modal_without_fade(render, assert_html):
    rendered = render("""
<c-bs-modal c-fade="False">
  <c-bs-modal-header>
    <c-bs-modal-title>No Fade Modal</c-bs-modal-title>
  </c-bs-modal-header>
  <c-bs-modal-body>
    <p>This modal doesn't have fade animation.</p>
  </c-bs-modal-body>
</c-bs-modal>
""")

    expected = """
        <div class="modal" id="modal-ctest01" tabindex="-1" aria-labelledby="modal-ctest01-label" aria-hidden="true">
          <div class="modal-dialog">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title" id="modal-ctest01-label">No Fade Modal</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div class="modal-body">
                <p>This modal doesn't have fade animation.</p>
              </div>
            </div>
          </div>
        </div>
    """

    assert_html(rendered, expected)


def test_modal_header_without_close_button(render, assert_html):
    rendered = render("""
<c-bs-modal>
  <c-bs-modal-header c-close_button="False">
    <c-bs-modal-title>No Close Button</c-bs-modal-title>
  </c-bs-modal-header>
  <c-bs-modal-body>
    <p>This modal header has no close button.</p>
  </c-bs-modal-body>
</c-bs-modal>
""")

    expected = """
        <div class="modal fade" id="modal-ctest01" tabindex="-1" aria-labelledby="modal-ctest01-label" aria-hidden="true">
          <div class="modal-dialog">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title" id="modal-ctest01-label">No Close Button</h5>
              </div>
              <div class="modal-body">
                <p>This modal header has no close button.</p>
              </div>
            </div>
          </div>
        </div>
    """

    assert_html(rendered, expected)


def test_modal_with_custom_title_heading(render, assert_html):
    rendered = render("""
<c-bs-modal>
  <c-bs-modal-header>
    <c-bs-modal-title as_="h1">Custom Heading Level</c-bs-modal-title>
  </c-bs-modal-header>
  <c-bs-modal-body>
    <p>This modal title uses h1 instead of h5.</p>
  </c-bs-modal-body>
</c-bs-modal>
""")

    expected = """
        <div class="modal fade" id="modal-ctest01" tabindex="-1" aria-labelledby="modal-ctest01-label" aria-hidden="true">
          <div class="modal-dialog">
            <div class="modal-content">
              <div class="modal-header">
                <h1 class="modal-title" id="modal-ctest01-label">Custom Heading Level</h1>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div class="modal-body">
                <p>This modal title uses h1 instead of h5.</p>
              </div>
            </div>
          </div>
        </div>
    """

    assert_html(rendered, expected)


def test_modal_centered_and_scrollable(render, assert_html):
    rendered = render("""
<c-bs-modal c-centered="True" c-scrollable="True">
  <c-bs-modal-header>
    <c-bs-modal-title>Centered & Scrollable</c-bs-modal-title>
  </c-bs-modal-header>
  <c-bs-modal-body>
    <p>This modal is both centered and scrollable.</p>
  </c-bs-modal-body>
</c-bs-modal>
""")

    expected = """
        <div class="modal fade" id="modal-ctest01" tabindex="-1" aria-labelledby="modal-ctest01-label" aria-hidden="true">
          <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title" id="modal-ctest01-label">Centered & Scrollable</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div class="modal-body">
                <p>This modal is both centered and scrollable.</p>
              </div>
            </div>
          </div>
        </div>
    """

    assert_html(rendered, expected)
