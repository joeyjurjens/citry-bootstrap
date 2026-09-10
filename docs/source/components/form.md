# Form

## Basic Form

```citry-html
<c-bs-form>
  <c-bs-form-group control_id="exampleInputEmail1">
    <c-bs-form-label>Email address</c-bs-form-label>
    <c-bs-form-control type="email" />
  </c-bs-form-group>
  <c-bs-button type="submit" variant="primary">Submit</c-bs-button>
</c-bs-form>
```

**Preview:**

--8<-- "snippets/form_example_1.html"

---

## Form With Text

```citry-html
<c-bs-form-group control_id="exampleInputEmail1">
  <c-bs-form-label>Email address</c-bs-form-label>
  <c-bs-form-control type="email" />
  <c-bs-form-text>We'll never share your email with anyone else.</c-bs-form-text>
</c-bs-form-group>
```

**Preview:**

--8<-- "snippets/form_example_2.html"

---

## Form Checkbox

```citry-html
<c-bs-form-check label="Check me out" c-attrs="{'id': 'exampleCheck1'}" />
```

**Preview:**

--8<-- "snippets/form_example_3.html"

---

## Form Radio

```citry-html
<c-bs-form-check type="radio" name="exampleRadio" label="Option one" c-attrs="{'id': 'exampleRadio1'}" />
```

**Preview:**

--8<-- "snippets/form_example_4.html"

---

## Form Control Sizes

```citry-html
<c-bs-form-control size="lg" placeholder=".form-control-lg" />
<c-bs-form-control placeholder="Default input" />
<c-bs-form-control size="sm" placeholder=".form-control-sm" />
```

**Preview:**

--8<-- "snippets/form_example_5.html"

---

## Form Control Disabled

```citry-html
<c-bs-form-control placeholder="Disabled input" c-disabled="True" />
```

**Preview:**

--8<-- "snippets/form_example_6.html"

---

## Form Control Readonly

```citry-html
<c-bs-form-control placeholder="Readonly input" c-readonly="True" value="readonly" />
```

**Preview:**

--8<-- "snippets/form_example_7.html"

---

## Form Check Inline

```citry-html
<c-bs-form-check c-inline="True" value="option1" label="1" c-attrs="{'id': 'inlineCheckbox1'}" />
<c-bs-form-check c-inline="True" value="option2" label="2" c-attrs="{'id': 'inlineCheckbox2'}" />
```

**Preview:**

--8<-- "snippets/form_example_8.html"

---

## Form Check Disabled

```citry-html
<c-bs-form-check label="Disabled checkbox" c-disabled="True" c-attrs="{'id': 'disabledCheck'}" />
```

**Preview:**

--8<-- "snippets/form_example_9.html"

---

## Form Switch

```citry-html
<c-bs-form-check type="switch" label="Default switch checkbox input" c-attrs="{'id': 'flexSwitchCheckDefault'}" />
```

**Preview:**

--8<-- "snippets/form_example_10.html"

---

## Form Range Basic

```citry-html
<c-bs-form-range />
```

**Preview:**

--8<-- "snippets/form_example_11.html"

---

## Form Range Disabled

```citry-html
<c-bs-form-range c-disabled="True" />
```

**Preview:**

--8<-- "snippets/form_example_12.html"

---

## Form Range Min Max

```citry-html
<c-bs-form-range c-min="0" c-max="5" />
```

**Preview:**

--8<-- "snippets/form_example_13.html"

---

## Form Range Step

```citry-html
<c-bs-form-range c-min="0" c-max="5" c-step="0.5" />
```

**Preview:**

--8<-- "snippets/form_example_14.html"

---

## Input Group With Text

```citry-html
<c-bs-input-group>
  <c-bs-input-group-text>@</c-bs-input-group-text>
  <c-bs-form-control placeholder="Username" />
</c-bs-input-group>
```

**Preview:**

--8<-- "snippets/form_example_15.html"

---

## Input Group With Button

```citry-html
<c-bs-input-group>
  <c-bs-button variant="outline-secondary" type="button">Button</c-bs-button>
  <c-bs-form-control c-placeholder="''" />
</c-bs-input-group>
```

**Preview:**

--8<-- "snippets/form_example_16.html"

---

## Input Group With Checkbox

```citry-html
<c-bs-input-group>
  <c-bs-input-group-checkbox c-attrs="{'value': ''}" />
  <c-bs-form-control />
</c-bs-input-group>
```

**Preview:**

--8<-- "snippets/form_example_17.html"

---

## Input Group With Radio

```citry-html
<c-bs-input-group>
  <c-bs-input-group-radio c-attrs="{'value': ''}" />
  <c-bs-form-control />
</c-bs-input-group>
```

**Preview:**

--8<-- "snippets/form_example_18.html"

---

## Input Group Sizing

```citry-html
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
```

**Preview:**

--8<-- "snippets/form_example_19.html"

---

## Input Group Multiple Inputs

```citry-html
<c-bs-input-group>
  <c-bs-input-group-text>First and last name</c-bs-input-group-text>
  <c-bs-form-control />
  <c-bs-form-control />
</c-bs-input-group>
```

**Preview:**

--8<-- "snippets/form_example_20.html"

---

## Input Group Multiple Addons

```citry-html
<c-bs-input-group>
  <c-bs-input-group-text>$</c-bs-input-group-text>
  <c-bs-input-group-text>0.00</c-bs-input-group-text>
  <c-bs-form-control />
</c-bs-input-group>
```

**Preview:**

--8<-- "snippets/form_example_21.html"

---

## Floating Label Basic

```citry-html
<c-bs-floating-label label="Email address" control_id="floatingInput">
  <c-bs-form-control type="email" placeholder="name@example.com" />
</c-bs-floating-label>
```

**Preview:**

--8<-- "snippets/form_example_22.html"

---

## Floating Label With Textarea

```citry-html
<c-bs-floating-label label="Comments" control_id="floatingTextarea">
  <c-bs-form-textarea placeholder="Leave a comment here" c-attrs="{'style': 'height: 100px', 'rows': '5'}" />
</c-bs-floating-label>
```

**Preview:**

--8<-- "snippets/form_example_23.html"

---

## Floating Label With Select

```citry-html
<c-bs-floating-label label="Works with selects" control_id="floatingSelect">
  <c-bs-form-select>
    <option selected>Open this select menu</option>
    <option value="1">One</option>
    <option value="2">Two</option>
    <option value="3">Three</option>
  </c-bs-form-select>
</c-bs-floating-label>
```

**Preview:**

--8<-- "snippets/form_example_24.html"

---

## Form Floating Low Level

```citry-html
<c-bs-form-floating>
  <c-bs-form-control type="email" placeholder="name@example.com" c-attrs="{'id': 'floatingInputCustom'}" />
  <label for="floatingInputCustom">Email address</label>
</c-bs-form-floating>
```

**Preview:**

--8<-- "snippets/form_example_25.html"

---
