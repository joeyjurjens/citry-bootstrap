def test_basic_with_header(render, assert_html):
    rendered = render("""
<c-bs-toast>
  <c-bs-toast-header>
    <img src="https://placehold.net/600x400.png" class="rounded me-2" alt="Toast icon" />
    <strong class="me-auto">Bootstrap</strong>
    <small>11 mins ago</small>
  </c-bs-toast-header>
  <c-bs-toast-body>Hello, world! This is a toast message.</c-bs-toast-body>
</c-bs-toast>
""")

    expected = """
        <div class="toast" role="alert" aria-live="assertive" aria-atomic="true" id="toast-ctest01">
          <div class="toast-header">
            <img src="https://placehold.net/600x400.png" class="rounded me-2" alt="Toast icon">
            <strong class="me-auto">Bootstrap</strong>
            <small>11 mins ago</small>
            <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
          </div>
          <div class="toast-body">
            Hello, world! This is a toast message.
          </div>
        </div>
    """

    assert_html(rendered, expected)


def test_autohide_false(render, assert_html):
    rendered = render("""
<c-bs-toast c-autohide="False">
  <c-bs-toast-header>
    <img src="https://placehold.net/600x400.png" class="rounded me-2" alt="Toast icon" />
    <strong class="me-auto">Bootstrap</strong>
    <small>11 mins ago</small>
  </c-bs-toast-header>
  <c-bs-toast-body>Hello, world! This is a toast message.</c-bs-toast-body>
</c-bs-toast>
""")

    expected = """
        <div role="alert" aria-live="assertive" aria-atomic="true" class="toast" data-bs-autohide="false" id="toast-ctest01">
          <div class="toast-header">
            <img src="https://placehold.net/600x400.png" class="rounded me-2" alt="Toast icon">
            <strong class="me-auto">Bootstrap</strong>
            <small>11 mins ago</small>
            <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
          </div>
          <div class="toast-body">
            Hello, world! This is a toast message.
          </div>
        </div>
    """

    assert_html(rendered, expected)


def test_translucent(render, assert_html):
    rendered = render("""
<c-bs-toast>
  <c-bs-toast-header>
    <img src="https://placehold.net/600x400.png" class="rounded me-2" alt="Toast icon" />
    <strong class="me-auto">Bootstrap</strong>
    <small class="text-body-secondary">11 mins ago</small>
  </c-bs-toast-header>
  <c-bs-toast-body>Hello, world! This is a toast message.</c-bs-toast-body>
</c-bs-toast>
""")

    expected = """
        <div class="toast" role="alert" aria-live="assertive" aria-atomic="true" id="toast-ctest01">
          <div class="toast-header">
            <img src="https://placehold.net/600x400.png" class="rounded me-2" alt="Toast icon">
            <strong class="me-auto">Bootstrap</strong>
            <small class="text-body-secondary">11 mins ago</small>
            <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
          </div>
          <div class="toast-body">
            Hello, world! This is a toast message.
          </div>
        </div>
    """

    assert_html(rendered, expected)


def test_stacking(render, assert_html):
    rendered = render("""
<c-bs-toast-container c-attrs="{'class': 'position-static'}">
  <c-bs-toast>
    <c-bs-toast-header>
      <img src="https://placehold.net/600x400.png" class="rounded me-2" alt="Toast icon" />
      <strong class="me-auto">Bootstrap</strong>
      <small class="text-body-secondary">just now</small>
    </c-bs-toast-header>
    <c-bs-toast-body>See? Just like this.</c-bs-toast-body>
  </c-bs-toast>
  <c-bs-toast>
    <c-bs-toast-header>
      <img src="https://placehold.net/600x400.png" class="rounded me-2" alt="Toast icon" />
      <strong class="me-auto">Bootstrap</strong>
      <small class="text-body-secondary">2 seconds ago</small>
    </c-bs-toast-header>
    <c-bs-toast-body>Heads up, toasts will stack automatically</c-bs-toast-body>
  </c-bs-toast>
</c-bs-toast-container>
""")

    expected = """
        <div class="toast-container position-static">
          <div class="toast" role="alert" aria-live="assertive" aria-atomic="true" id="toast-ctest02">
            <div class="toast-header">
              <img src="https://placehold.net/600x400.png" class="rounded me-2" alt="Toast icon">
              <strong class="me-auto">Bootstrap</strong>
              <small class="text-body-secondary">just now</small>
              <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
            </div>
            <div class="toast-body">
              See? Just like this.
            </div>
          </div>

          <div class="toast" role="alert" aria-live="assertive" aria-atomic="true" id="toast-ctest03">
            <div class="toast-header">
              <img src="https://placehold.net/600x400.png" class="rounded me-2" alt="Toast icon">
              <strong class="me-auto">Bootstrap</strong>
              <small class="text-body-secondary">2 seconds ago</small>
              <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
            </div>
            <div class="toast-body">
              Heads up, toasts will stack automatically
            </div>
          </div>
        </div>
    """

    assert_html(rendered, expected)


def test_custom_content_simplified(render, assert_html):
    rendered = render("""
<c-bs-toast c-attrs="{'class': 'align-items-center'}">
  <div class="d-flex">
    <c-bs-toast-body>Hello, world! This is a toast message.</c-bs-toast-body>
    <c-bs-close-button c-attrs="{'class': 'me-2 m-auto', 'data-bs-dismiss': 'toast'}" />
  </div>
</c-bs-toast>
""")

    expected = """
        <div class="toast align-items-center" role="alert" aria-live="assertive" aria-atomic="true" id="toast-ctest01">
          <div class="d-flex">
            <div class="toast-body">
              Hello, world! This is a toast message.
            </div>
            <button type="button" class="btn-close me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
          </div>
        </div>
    """

    assert_html(rendered, expected)


def test_custom_content_with_actions(render, assert_html):
    rendered = render("""
<c-bs-toast>
  <c-bs-toast-body>
    Hello, world! This is a toast message.
    <div class="mt-2 pt-2 border-top">
      <c-bs-button variant="primary" size="sm">Take action</c-bs-button>
      <c-bs-button variant="secondary" size="sm" c-attrs="{'data-bs-dismiss': 'toast'}">Close</c-bs-button>
    </div>
  </c-bs-toast-body>
</c-bs-toast>
""")

    expected = """
        <div class="toast" role="alert" aria-live="assertive" aria-atomic="true" id="toast-ctest01">
          <div class="toast-body">
            Hello, world! This is a toast message.
            <div class="mt-2 pt-2 border-top">
              <button type="button" class="btn btn-primary btn-sm">Take action</button>
              <button type="button" class="btn btn-secondary btn-sm" data-bs-dismiss="toast">Close</button>
            </div>
          </div>
        </div>
    """

    assert_html(rendered, expected)


def test_color_scheme_primary(render, assert_html):
    rendered = render("""
<c-bs-toast c-attrs="{'class': 'align-items-center text-bg-primary border-0'}">
  <div class="d-flex">
    <c-bs-toast-body>Hello, world! This is a toast message.</c-bs-toast-body>
    <c-bs-close-button variant="white" c-attrs="{'class': 'me-2 m-auto', 'data-bs-dismiss': 'toast'}" />
  </div>
</c-bs-toast>
""")

    expected = """
        <div class="toast align-items-center text-bg-primary border-0" role="alert" aria-live="assertive" aria-atomic="true" id="toast-ctest01">
          <div class="d-flex">
            <div class="toast-body">
              Hello, world! This is a toast message.
            </div>
            <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
          </div>
        </div>
    """

    assert_html(rendered, expected)


def test_toast_container_bottom_end(render, assert_html):
    rendered = render("""
<c-bs-toast-container position="end" c-attrs="{'class': 'bottom-0 p-3'}">
  <c-bs-toast>
    <c-bs-toast-header>
      <img src="https://placehold.net/600x400.png" class="rounded me-2" alt="Toast icon" />
      <strong class="me-auto">Bootstrap</strong>
      <small>11 mins ago</small>
    </c-bs-toast-header>
    <c-bs-toast-body>Hello, world! This is a toast message.</c-bs-toast-body>
  </c-bs-toast>
</c-bs-toast-container>
""")

    expected = """
        <div class="toast-container position-fixed top-0 end-0 bottom-0 p-3">
          <div class="toast" role="alert" aria-live="assertive" aria-atomic="true" id="toast-ctest02">
            <div class="toast-header">
              <img src="https://placehold.net/600x400.png" class="rounded me-2" alt="Toast icon">
              <strong class="me-auto">Bootstrap</strong>
              <small>11 mins ago</small>
              <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
            </div>
            <div class="toast-body">
              Hello, world! This is a toast message.
            </div>
          </div>
        </div>
    """

    assert_html(rendered, expected)
