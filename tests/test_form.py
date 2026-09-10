def test_basic_form(render, assert_html):
    rendered = render("""
<c-bs-form>
  <c-bs-form-group control_id="exampleInputEmail1">
    <c-bs-form-label>Email address</c-bs-form-label>
    <c-bs-form-control type="email" />
  </c-bs-form-group>
  <c-bs-button type="submit" variant="primary">Submit</c-bs-button>
</c-bs-form>
""")

    expected = """
        <form>
            <div>
                <label class="form-label" for="exampleInputEmail1">Email address</label>
                <input class="form-control" type="email" id="exampleInputEmail1" />
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
        </form>
    """

    assert_html(rendered, expected)


def test_form_with_text(render, assert_html):
    rendered = render("""
<c-bs-form-group control_id="exampleInputEmail1">
  <c-bs-form-label>Email address</c-bs-form-label>
  <c-bs-form-control type="email" />
  <c-bs-form-text>We'll never share your email with anyone else.</c-bs-form-text>
</c-bs-form-group>
""")

    expected = """
        <div>
            <label class="form-label" for="exampleInputEmail1">Email address</label>
            <input class="form-control" type="email" id="exampleInputEmail1" />
            <div class="form-text">We'll never share your email with anyone else.</div>
        </div>
    """

    assert_html(rendered, expected)


def test_form_checkbox(render, assert_html):
    rendered = render("""
<c-bs-form-check label="Check me out" c-attrs="{'id': 'exampleCheck1'}" />
""")

    expected = """
        <div class="form-check" id="exampleCheck1">
            <input type="checkbox" class="form-check-input" id="exampleCheck1">
            <label class="form-check-label" for="exampleCheck1">Check me out</label>
        </div>
    """

    assert_html(rendered, expected)


def test_form_radio(render, assert_html):
    rendered = render("""
<c-bs-form-check type="radio" name="exampleRadio" label="Option one" c-attrs="{'id': 'exampleRadio1'}" />
""")

    expected = """
        <div class="form-check" id="exampleRadio1">
            <input class="form-check-input" type="radio" name="exampleRadio" id="exampleRadio1">
            <label class="form-check-label" for="exampleRadio1">Option one</label>
        </div>
    """

    assert_html(rendered, expected)


def test_form_control_sizes(render, assert_html):
    rendered = render("""
<c-bs-form-control size="lg" placeholder=".form-control-lg" />
<c-bs-form-control placeholder="Default input" />
<c-bs-form-control size="sm" placeholder=".form-control-sm" />
""")

    expected = """
        <input class="form-control form-control-lg" type="text" placeholder=".form-control-lg" />
        <input class="form-control" type="text" placeholder="Default input" />
        <input class="form-control form-control-sm" type="text" placeholder=".form-control-sm" />
    """

    assert_html(rendered, expected)


def test_form_control_disabled(render, assert_html):
    rendered = render("""
<c-bs-form-control placeholder="Disabled input" c-disabled="True" />
""")

    expected = """
        <input class="form-control" type="text" placeholder="Disabled input" disabled />
    """

    assert_html(rendered, expected)


def test_form_control_readonly(render, assert_html):
    rendered = render("""
<c-bs-form-control placeholder="Readonly input" c-readonly="True" value="readonly" />
""")

    expected = """
        <input class="form-control" type="text" placeholder="Readonly input" value="readonly" readonly />
    """

    assert_html(rendered, expected)


def test_form_check_inline(render, assert_html):
    rendered = render("""
<c-bs-form-check c-inline="True" value="option1" label="1" c-attrs="{'id': 'inlineCheckbox1'}" />
<c-bs-form-check c-inline="True" value="option2" label="2" c-attrs="{'id': 'inlineCheckbox2'}" />
""")

    expected = """
        <div class="form-check form-check-inline" id="inlineCheckbox1">
            <input class="form-check-input" type="checkbox" id="inlineCheckbox1" value="option1">
            <label class="form-check-label" for="inlineCheckbox1">1</label>
        </div>
        <div class="form-check form-check-inline" id="inlineCheckbox2">
            <input class="form-check-input" type="checkbox" id="inlineCheckbox2" value="option2">
            <label class="form-check-label" for="inlineCheckbox2">2</label>
        </div>
    """

    assert_html(rendered, expected)


def test_form_check_disabled(render, assert_html):
    rendered = render("""
<c-bs-form-check label="Disabled checkbox" c-disabled="True" c-attrs="{'id': 'disabledCheck'}" />
""")

    expected = """
        <div class="form-check" id="disabledCheck">
            <input class="form-check-input" type="checkbox" id="disabledCheck" disabled>
            <label class="form-check-label" for="disabledCheck">Disabled checkbox</label>
        </div>
    """

    assert_html(rendered, expected)


def test_form_switch(render, assert_html):
    rendered = render("""
<c-bs-form-check type="switch" label="Default switch checkbox input" c-attrs="{'id': 'flexSwitchCheckDefault'}" />
""")

    expected = """
        <div class="form-check form-switch" id="flexSwitchCheckDefault">
            <input class="form-check-input" type="checkbox" role="switch" id="flexSwitchCheckDefault">
            <label class="form-check-label" for="flexSwitchCheckDefault">Default switch checkbox input</label>
        </div>
    """

    assert_html(rendered, expected)


def test_form_range_basic(render, assert_html):
    rendered = render("""
<c-bs-form-range />
""")

    expected = """
        <input type="range" class="form-range" min="0" max="100" step="1">
    """

    assert_html(rendered, expected)


def test_form_range_disabled(render, assert_html):
    rendered = render("""
<c-bs-form-range c-disabled="True" />
""")

    expected = """
        <input type="range" class="form-range" disabled min="0" max="100" step="1">
    """

    assert_html(rendered, expected)


def test_form_range_min_max(render, assert_html):
    rendered = render("""
<c-bs-form-range c-min="0" c-max="5" />
""")

    expected = """
        <input type="range" class="form-range" min="0" max="5" step="1">
    """

    assert_html(rendered, expected)


def test_form_range_step(render, assert_html):
    rendered = render("""
<c-bs-form-range c-min="0" c-max="5" c-step="0.5" />
""")

    expected = """
        <input type="range" class="form-range" min="0" max="5" step="0.5">
    """

    assert_html(rendered, expected)


def test_input_group_with_text(render, assert_html):
    rendered = render("""
<c-bs-input-group>
  <c-bs-input-group-text>@</c-bs-input-group-text>
  <c-bs-form-control placeholder="Username" />
</c-bs-input-group>
""")

    expected = """
        <div class="input-group">
            <span class="input-group-text">@</span>
            <input type="text" class="form-control" placeholder="Username">
        </div>
    """

    assert_html(rendered, expected)


def test_input_group_with_button(render, assert_html):
    rendered = render("""
<c-bs-input-group>
  <c-bs-button variant="outline-secondary" type="button">Button</c-bs-button>
  <c-bs-form-control c-placeholder="''" />
</c-bs-input-group>
""")

    expected = """
        <div class="input-group">
            <button class="btn btn-outline-secondary" type="button">Button</button>
            <input type="text" class="form-control" placeholder="">
        </div>
    """

    assert_html(rendered, expected)


def test_input_group_with_checkbox(render, assert_html):
    rendered = render("""
<c-bs-input-group>
  <c-bs-input-group-checkbox c-attrs="{'value': ''}" />
  <c-bs-form-control />
</c-bs-input-group>
""")

    expected = """
        <div class="input-group">
            <div class="input-group-text">
                <input class="form-check-input mt-0" type="checkbox" value="">
            </div>
            <input type="text" class="form-control">
        </div>
    """

    assert_html(rendered, expected)


def test_input_group_with_radio(render, assert_html):
    rendered = render("""
<c-bs-input-group>
  <c-bs-input-group-radio c-attrs="{'value': ''}" />
  <c-bs-form-control />
</c-bs-input-group>
""")

    expected = """
        <div class="input-group">
            <div class="input-group-text">
                <input class="form-check-input mt-0" type="radio" value="">
            </div>
            <input type="text" class="form-control">
        </div>
    """

    assert_html(rendered, expected)


def test_input_group_sizing(render, assert_html):
    rendered = render("""
<c-bs-input-group size="sm">
  <c-bs-input-group-text>Small</c-bs-input-group-text>
  <c-bs-form-control />
</c-bs-input-group>
<c-bs-input-group>
  <c-bs-input-group-text>Default</c-bs-input-group-text>
  <c-bs-form-control />
</c-bs-input-group>
<c-bs-input-group size="lg">
  <c-bs-input-group-text>Large</c-bs-input-group-text>
  <c-bs-form-control />
</c-bs-input-group>
""")

    expected = """
        <div class="input-group input-group-sm">
            <span class="input-group-text">Small</span>
            <input type="text" class="form-control">
        </div>
        <div class="input-group">
            <span class="input-group-text">Default</span>
            <input type="text" class="form-control">
        </div>
        <div class="input-group input-group-lg">
            <span class="input-group-text">Large</span>
            <input type="text" class="form-control">
        </div>
    """

    assert_html(rendered, expected)


def test_input_group_multiple_inputs(render, assert_html):
    rendered = render("""
<c-bs-input-group>
  <c-bs-input-group-text>First and last name</c-bs-input-group-text>
  <c-bs-form-control />
  <c-bs-form-control />
</c-bs-input-group>
""")

    expected = """
        <div class="input-group">
            <span class="input-group-text">First and last name</span>
            <input type="text" class="form-control">
            <input type="text" class="form-control">
        </div>
    """

    assert_html(rendered, expected)


def test_input_group_multiple_addons(render, assert_html):
    rendered = render("""
<c-bs-input-group>
  <c-bs-input-group-text>$</c-bs-input-group-text>
  <c-bs-input-group-text>0.00</c-bs-input-group-text>
  <c-bs-form-control />
</c-bs-input-group>
""")

    expected = """
        <div class="input-group">
            <span class="input-group-text">$</span>
            <span class="input-group-text">0.00</span>
            <input type="text" class="form-control">
        </div>
    """

    assert_html(rendered, expected)


def test_floating_label_basic(render, assert_html):
    rendered = render("""
<c-bs-floating-label label="Email address" control_id="floatingInput">
  <c-bs-form-control type="email" placeholder="name@example.com" />
</c-bs-floating-label>
""")

    expected = """
        <div class="form-floating">
            <input type="email" class="form-control" id="floatingInput" placeholder="name@example.com">
            <label for="floatingInput">Email address</label>
        </div>
    """

    assert_html(rendered, expected)


def test_floating_label_with_textarea(render, assert_html):
    rendered = render("""
<c-bs-floating-label label="Comments" control_id="floatingTextarea">
  <c-bs-form-textarea placeholder="Leave a comment here" c-attrs="{'style': 'height: 100px', 'rows': '5'}" />
</c-bs-floating-label>
""")

    expected = """
        <div class="form-floating">
            <textarea class="form-control" id="floatingTextarea" placeholder="Leave a comment here" rows="5" style="height: 100px;"></textarea>
            <label for="floatingTextarea">Comments</label>
        </div>
    """

    assert_html(rendered, expected)


def test_floating_label_with_select(render, assert_html):
    rendered = render("""
<c-bs-floating-label label="Works with selects" control_id="floatingSelect">
  <c-bs-form-select>
    <option selected>Open this select menu</option>
    <option value="1">One</option>
    <option value="2">Two</option>
    <option value="3">Three</option>
  </c-bs-form-select>
</c-bs-floating-label>
""")

    expected = """
        <div class="form-floating">
            <select class="form-select" id="floatingSelect">
                <option selected>Open this select menu</option>
                <option value="1">One</option>
                <option value="2">Two</option>
                <option value="3">Three</option>
            </select>
            <label for="floatingSelect">Works with selects</label>
        </div>
    """

    assert_html(rendered, expected)


def test_form_floating_low_level(render, assert_html):
    rendered = render("""
<c-bs-form-floating>
  <c-bs-form-control type="email" placeholder="name@example.com" c-attrs="{'id': 'floatingInputCustom'}" />
  <label for="floatingInputCustom">Email address</label>
</c-bs-form-floating>
""")

    expected = """
        <div class="form-floating">
            <input type="email" class="form-control" id="floatingInputCustom" placeholder="name@example.com">
            <label for="floatingInputCustom">Email address</label>
        </div>
    """

    assert_html(rendered, expected)
