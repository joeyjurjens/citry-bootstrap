def test_basic(render, assert_html):
    rendered = render("""
<c-bs-tabs>
  <c-bs-tab title="Home">Home content</c-bs-tab>
  <c-bs-tab title="Profile">Profile content</c-bs-tab>
  <c-bs-tab title="Contact">Contact content</c-bs-tab>
</c-bs-tabs>
""")

    expected = """
        <div>
          <ul class="nav nav-tabs" id="tabs-ctest01" role="tablist">
            <li class="nav-item" role="presentation">
              <button class="nav-link active" id="tabs-ctest01-tab-home" data-bs-toggle="tab" data-bs-target="#tabs-ctest01-pane-home" type="button" role="tab" aria-controls="tabs-ctest01-pane-home" aria-selected="true">Home</button>
            </li>
            <li class="nav-item" role="presentation">
              <button class="nav-link" id="tabs-ctest01-tab-profile" data-bs-toggle="tab" data-bs-target="#tabs-ctest01-pane-profile" type="button" role="tab" aria-controls="tabs-ctest01-pane-profile" aria-selected="false">Profile</button>
            </li>
            <li class="nav-item" role="presentation">
              <button class="nav-link" id="tabs-ctest01-tab-contact" data-bs-toggle="tab" data-bs-target="#tabs-ctest01-pane-contact" type="button" role="tab" aria-controls="tabs-ctest01-pane-contact" aria-selected="false">Contact</button>
            </li>
          </ul>
          <div class="tab-content">
            <div class="tab-pane fade show active" id="tabs-ctest01-pane-home" role="tabpanel" aria-labelledby="tabs-ctest01-tab-home" tabindex="0">
              Home content
            </div>
            <div class="tab-pane fade" id="tabs-ctest01-pane-profile" role="tabpanel" aria-labelledby="tabs-ctest01-tab-profile" tabindex="0">
              Profile content
            </div>
            <div class="tab-pane fade" id="tabs-ctest01-pane-contact" role="tabpanel" aria-labelledby="tabs-ctest01-tab-contact" tabindex="0">
              Contact content
            </div>
          </div>
        </div>
    """

    assert_html(rendered, expected)


def test_pills_variant(render, assert_html):
    rendered = render("""
<c-bs-tabs variant="pills">
  <c-bs-tab title="Home">Home content</c-bs-tab>
  <c-bs-tab title="Profile">Profile content</c-bs-tab>
</c-bs-tabs>
""")

    expected = """
        <div>
          <ul class="nav nav-pills" id="tabs-ctest01" role="tablist">
            <li class="nav-item" role="presentation">
              <button class="nav-link active" id="tabs-ctest01-tab-home" data-bs-toggle="tab" data-bs-target="#tabs-ctest01-pane-home" type="button" role="tab" aria-controls="tabs-ctest01-pane-home" aria-selected="true">Home</button>
            </li>
            <li class="nav-item" role="presentation">
              <button class="nav-link" id="tabs-ctest01-tab-profile" data-bs-toggle="tab" data-bs-target="#tabs-ctest01-pane-profile" type="button" role="tab" aria-controls="tabs-ctest01-pane-profile" aria-selected="false">Profile</button>
            </li>
          </ul>
          <div class="tab-content">
            <div class="tab-pane fade show active" id="tabs-ctest01-pane-home" role="tabpanel" aria-labelledby="tabs-ctest01-tab-home" tabindex="0">
              Home content
            </div>
            <div class="tab-pane fade" id="tabs-ctest01-pane-profile" role="tabpanel" aria-labelledby="tabs-ctest01-tab-profile" tabindex="0">
              Profile content
            </div>
          </div>
        </div>
    """

    assert_html(rendered, expected)


def test_underline_variant(render, assert_html):
    rendered = render("""
<c-bs-tabs variant="underline">
  <c-bs-tab title="Home">Home content</c-bs-tab>
  <c-bs-tab title="Profile">Profile content</c-bs-tab>
</c-bs-tabs>
""")

    expected = """
        <div>
          <ul class="nav nav-underline" id="tabs-ctest01" role="tablist">
            <li class="nav-item" role="presentation">
              <button class="nav-link active" id="tabs-ctest01-tab-home" data-bs-toggle="tab" data-bs-target="#tabs-ctest01-pane-home" type="button" role="tab" aria-controls="tabs-ctest01-pane-home" aria-selected="true">Home</button>
            </li>
            <li class="nav-item" role="presentation">
              <button class="nav-link" id="tabs-ctest01-tab-profile" data-bs-toggle="tab" data-bs-target="#tabs-ctest01-pane-profile" type="button" role="tab" aria-controls="tabs-ctest01-pane-profile" aria-selected="false">Profile</button>
            </li>
          </ul>
          <div class="tab-content">
            <div class="tab-pane fade show active" id="tabs-ctest01-pane-home" role="tabpanel" aria-labelledby="tabs-ctest01-tab-home" tabindex="0">
              Home content
            </div>
            <div class="tab-pane fade" id="tabs-ctest01-pane-profile" role="tabpanel" aria-labelledby="tabs-ctest01-tab-profile" tabindex="0">
              Profile content
            </div>
          </div>
        </div>
    """

    assert_html(rendered, expected)


def test_tabs_with_fill(render, assert_html):
    rendered = render("""
<c-bs-tabs c-fill="True">
  <c-bs-tab title="Home">Home content</c-bs-tab>
  <c-bs-tab title="Longer title">Profile content</c-bs-tab>
  <c-bs-tab title="Link">Contact content</c-bs-tab>
</c-bs-tabs>
""")

    expected = """
        <div>
          <ul class="nav nav-tabs nav-fill" id="tabs-ctest01" role="tablist">
            <li class="nav-item" role="presentation">
              <button class="nav-link active" id="tabs-ctest01-tab-home" data-bs-toggle="tab" data-bs-target="#tabs-ctest01-pane-home" type="button" role="tab" aria-controls="tabs-ctest01-pane-home" aria-selected="true">Home</button>
            </li>
            <li class="nav-item" role="presentation">
              <button class="nav-link" id="tabs-ctest01-tab-longer-title" data-bs-toggle="tab" data-bs-target="#tabs-ctest01-pane-longer-title" type="button" role="tab" aria-controls="tabs-ctest01-pane-longer-title" aria-selected="false">Longer title</button>
            </li>
            <li class="nav-item" role="presentation">
              <button class="nav-link" id="tabs-ctest01-tab-link" data-bs-toggle="tab" data-bs-target="#tabs-ctest01-pane-link" type="button" role="tab" aria-controls="tabs-ctest01-pane-link" aria-selected="false">Link</button>
            </li>
          </ul>
          <div class="tab-content">
            <div class="tab-pane fade show active" id="tabs-ctest01-pane-home" role="tabpanel" aria-labelledby="tabs-ctest01-tab-home" tabindex="0">
              Home content
            </div>
            <div class="tab-pane fade" id="tabs-ctest01-pane-longer-title" role="tabpanel" aria-labelledby="tabs-ctest01-tab-longer-title" tabindex="0">
              Profile content
            </div>
            <div class="tab-pane fade" id="tabs-ctest01-pane-link" role="tabpanel" aria-labelledby="tabs-ctest01-tab-link" tabindex="0">
              Contact content
            </div>
          </div>
        </div>
    """

    assert_html(rendered, expected)


def test_tabs_with_justified(render, assert_html):
    rendered = render("""
<c-bs-tabs c-justified="True">
  <c-bs-tab title="Home">Home content</c-bs-tab>
  <c-bs-tab title="Profile">Profile content</c-bs-tab>
</c-bs-tabs>
""")

    expected = """
        <div>
          <ul class="nav nav-tabs nav-justified" id="tabs-ctest01" role="tablist">
            <li class="nav-item" role="presentation">
              <button class="nav-link active" id="tabs-ctest01-tab-home" data-bs-toggle="tab" data-bs-target="#tabs-ctest01-pane-home" type="button" role="tab" aria-controls="tabs-ctest01-pane-home" aria-selected="true">Home</button>
            </li>
            <li class="nav-item" role="presentation">
              <button class="nav-link" id="tabs-ctest01-tab-profile" data-bs-toggle="tab" data-bs-target="#tabs-ctest01-pane-profile" type="button" role="tab" aria-controls="tabs-ctest01-pane-profile" aria-selected="false">Profile</button>
            </li>
          </ul>
          <div class="tab-content">
            <div class="tab-pane fade show active" id="tabs-ctest01-pane-home" role="tabpanel" aria-labelledby="tabs-ctest01-tab-home" tabindex="0">
              Home content
            </div>
            <div class="tab-pane fade" id="tabs-ctest01-pane-profile" role="tabpanel" aria-labelledby="tabs-ctest01-tab-profile" tabindex="0">
              Profile content
            </div>
          </div>
        </div>
    """

    assert_html(rendered, expected)


def test_tabs_with_disabled_tab(render, assert_html):
    rendered = render("""
<c-bs-tabs>
  <c-bs-tab title="Home">Home content</c-bs-tab>
  <c-bs-tab title="Profile">Profile content</c-bs-tab>
  <c-bs-tab title="Disabled" c-disabled="True">Disabled content</c-bs-tab>
</c-bs-tabs>
""")

    expected = """
        <div>
          <ul class="nav nav-tabs" id="tabs-ctest01" role="tablist">
            <li class="nav-item" role="presentation">
              <button class="nav-link active" id="tabs-ctest01-tab-home" data-bs-toggle="tab" data-bs-target="#tabs-ctest01-pane-home" type="button" role="tab" aria-controls="tabs-ctest01-pane-home" aria-selected="true">Home</button>
            </li>
            <li class="nav-item" role="presentation">
              <button class="nav-link" id="tabs-ctest01-tab-profile" data-bs-toggle="tab" data-bs-target="#tabs-ctest01-pane-profile" type="button" role="tab" aria-controls="tabs-ctest01-pane-profile" aria-selected="false">Profile</button>
            </li>
            <li class="nav-item" role="presentation">
              <button class="nav-link disabled" id="tabs-ctest01-tab-disabled" data-bs-toggle="tab" data-bs-target="#tabs-ctest01-pane-disabled" type="button" role="tab" aria-controls="tabs-ctest01-pane-disabled" aria-selected="false" disabled>Disabled</button>
            </li>
          </ul>
          <div class="tab-content">
            <div class="tab-pane fade show active" id="tabs-ctest01-pane-home" role="tabpanel" aria-labelledby="tabs-ctest01-tab-home" tabindex="0">
              Home content
            </div>
            <div class="tab-pane fade" id="tabs-ctest01-pane-profile" role="tabpanel" aria-labelledby="tabs-ctest01-tab-profile" tabindex="0">
              Profile content
            </div>
            <div class="tab-pane fade" id="tabs-ctest01-pane-disabled" role="tabpanel" aria-labelledby="tabs-ctest01-tab-disabled" tabindex="0">
              Disabled content
            </div>
          </div>
        </div>
    """

    assert_html(rendered, expected)


def test_manual_composition_with_tab_container(render, assert_html):
    rendered = render("""
<c-bs-tab-container active_key="profile">
  <c-bs-nav variant="tabs" as_="ul" c-attrs="{'role': 'tablist'}">
    <c-bs-nav-item as_="li" c-attrs="{'role': 'presentation'}">
      <c-bs-nav-link as_="button" event_key="home">Home</c-bs-nav-link>
    </c-bs-nav-item>
    <c-bs-nav-item as_="li" c-attrs="{'role': 'presentation'}">
      <c-bs-nav-link as_="button" event_key="profile">Profile</c-bs-nav-link>
    </c-bs-nav-item>
  </c-bs-nav>
  <c-bs-tab-content>
    <c-bs-tab-pane event_key="home">Home content</c-bs-tab-pane>
    <c-bs-tab-pane event_key="profile">Profile content</c-bs-tab-pane>
  </c-bs-tab-content>
</c-bs-tab-container>
""")

    expected = """
        <div id="tab-container-ctest01">
          <ul class="nav nav-tabs" role="tablist">
            <li class="nav-item" role="presentation">
              <button class="nav-link" id="tab-container-ctest01-tab-home" data-bs-toggle="tab" data-bs-target="#tab-container-ctest01-pane-home" type="button" role="tab" aria-controls="tab-container-ctest01-pane-home" aria-selected="false">Home</button>
            </li>
            <li class="nav-item" role="presentation">
              <button class="nav-link active" id="tab-container-ctest01-tab-profile" data-bs-toggle="tab" data-bs-target="#tab-container-ctest01-pane-profile" type="button" role="tab" aria-controls="tab-container-ctest01-pane-profile" aria-selected="true">Profile</button>
            </li>
          </ul>
          <div class="tab-content">
            <div class="tab-pane fade" id="tab-container-ctest01-pane-home" role="tabpanel" aria-labelledby="tab-container-ctest01-tab-home" tabindex="0">
              Home content
            </div>
            <div class="tab-pane fade show active" id="tab-container-ctest01-pane-profile" role="tabpanel" aria-labelledby="tab-container-ctest01-tab-profile" tabindex="0">
              Profile content
            </div>
          </div>
        </div>
    """

    assert_html(rendered, expected)


def test_manual_composition_with_disabled_tab(render, assert_html):
    rendered = render("""
<c-bs-tab-container active_key="home">
  <c-bs-nav variant="tabs" as_="ul" c-attrs="{'role': 'tablist'}">
    <c-bs-nav-item as_="li" c-attrs="{'role': 'presentation'}">
      <c-bs-nav-link as_="button" event_key="home">Home</c-bs-nav-link>
    </c-bs-nav-item>
    <c-bs-nav-item as_="li" c-attrs="{'role': 'presentation'}">
      <c-bs-nav-link as_="button" event_key="settings" c-disabled="True">Settings</c-bs-nav-link>
    </c-bs-nav-item>
  </c-bs-nav>
  <c-bs-tab-content>
    <c-bs-tab-pane event_key="home">Home content</c-bs-tab-pane>
    <c-bs-tab-pane event_key="settings">Settings content</c-bs-tab-pane>
  </c-bs-tab-content>
</c-bs-tab-container>
""")

    expected = """
        <div id="tab-container-ctest01">
          <ul class="nav nav-tabs" role="tablist">
            <li class="nav-item" role="presentation">
              <button class="nav-link active" id="tab-container-ctest01-tab-home" data-bs-toggle="tab" data-bs-target="#tab-container-ctest01-pane-home" type="button" role="tab" aria-controls="tab-container-ctest01-pane-home" aria-selected="true">Home</button>
            </li>
            <li class="nav-item" role="presentation">
              <button class="nav-link disabled" id="tab-container-ctest01-tab-settings" data-bs-toggle="tab" data-bs-target="#tab-container-ctest01-pane-settings" type="button" role="tab" aria-controls="tab-container-ctest01-pane-settings" aria-selected="false" disabled>Settings</button>
            </li>
          </ul>
          <div class="tab-content">
            <div class="tab-pane fade show active" id="tab-container-ctest01-pane-home" role="tabpanel" aria-labelledby="tab-container-ctest01-tab-home" tabindex="0">
              Home content
            </div>
            <div class="tab-pane fade" id="tab-container-ctest01-pane-settings" role="tabpanel" aria-labelledby="tab-container-ctest01-tab-settings" tabindex="0">
              Settings content
            </div>
          </div>
        </div>
    """

    assert_html(rendered, expected)


def test_tabs_with_active_tab(render, assert_html):
    rendered = render("""
<c-bs-tabs>
  <c-bs-tab title="Home">Home content</c-bs-tab>
  <c-bs-tab title="Profile" c-active="True">Profile content</c-bs-tab>
  <c-bs-tab title="Contact">Contact content</c-bs-tab>
</c-bs-tabs>
""")

    expected = """
        <div>
          <ul class="nav nav-tabs" id="tabs-ctest01" role="tablist">
            <li class="nav-item" role="presentation">
              <button class="nav-link" id="tabs-ctest01-tab-home" data-bs-toggle="tab" data-bs-target="#tabs-ctest01-pane-home" type="button" role="tab" aria-controls="tabs-ctest01-pane-home" aria-selected="false">Home</button>
            </li>
            <li class="nav-item" role="presentation">
              <button class="nav-link active" id="tabs-ctest01-tab-profile" data-bs-toggle="tab" data-bs-target="#tabs-ctest01-pane-profile" type="button" role="tab" aria-controls="tabs-ctest01-pane-profile" aria-selected="true">Profile</button>
            </li>
            <li class="nav-item" role="presentation">
              <button class="nav-link" id="tabs-ctest01-tab-contact" data-bs-toggle="tab" data-bs-target="#tabs-ctest01-pane-contact" type="button" role="tab" aria-controls="tabs-ctest01-pane-contact" aria-selected="false">Contact</button>
            </li>
          </ul>
          <div class="tab-content">
            <div class="tab-pane fade" id="tabs-ctest01-pane-home" role="tabpanel" aria-labelledby="tabs-ctest01-tab-home" tabindex="0">
              Home content
            </div>
            <div class="tab-pane fade show active" id="tabs-ctest01-pane-profile" role="tabpanel" aria-labelledby="tabs-ctest01-tab-profile" tabindex="0">
              Profile content
            </div>
            <div class="tab-pane fade" id="tabs-ctest01-pane-contact" role="tabpanel" aria-labelledby="tabs-ctest01-tab-contact" tabindex="0">
              Contact content
            </div>
          </div>
        </div>
    """

    assert_html(rendered, expected)
