# ListGroup

## Basic

```citry-html
<c-bs-list-group>
  <c-bs-list-group-item>An item</c-bs-list-group-item>
  <c-bs-list-group-item>A second item</c-bs-list-group-item>
  <c-bs-list-group-item>A third item</c-bs-list-group-item>
  <c-bs-list-group-item>A fourth item</c-bs-list-group-item>
  <c-bs-list-group-item>And a fifth one</c-bs-list-group-item>
</c-bs-list-group>
```

**Preview:**

--8<-- "snippets/listgroup_example_1.html"

---

## Active Items

```citry-html
<c-bs-list-group>
  <c-bs-list-group-item c-active="True">An active item</c-bs-list-group-item>
  <c-bs-list-group-item>A second item</c-bs-list-group-item>
  <c-bs-list-group-item>A third item</c-bs-list-group-item>
  <c-bs-list-group-item>A fourth item</c-bs-list-group-item>
  <c-bs-list-group-item>And a fifth one</c-bs-list-group-item>
</c-bs-list-group>
```

**Preview:**

--8<-- "snippets/listgroup_example_2.html"

---

## Disabled Items

```citry-html
<c-bs-list-group>
  <c-bs-list-group-item>An item</c-bs-list-group-item>
  <c-bs-list-group-item>A second item</c-bs-list-group-item>
  <c-bs-list-group-item>A third item</c-bs-list-group-item>
  <c-bs-list-group-item>A fourth item</c-bs-list-group-item>
  <c-bs-list-group-item c-disabled="True">A disabled fifth item</c-bs-list-group-item>
</c-bs-list-group>
```

**Preview:**

--8<-- "snippets/listgroup_example_3.html"

---

## Links

```citry-html
<c-bs-list-group as_="div">
  <c-bs-list-group-item href="#" c-active="True">The current link item</c-bs-list-group-item>
  <c-bs-list-group-item href="#">A second link item</c-bs-list-group-item>
  <c-bs-list-group-item href="#">A third link item</c-bs-list-group-item>
  <c-bs-list-group-item href="#">A fourth link item</c-bs-list-group-item>
  <c-bs-list-group-item href="#" c-disabled="True">A disabled link item</c-bs-list-group-item>
</c-bs-list-group>
```

**Preview:**

--8<-- "snippets/listgroup_example_4.html"

---

## Buttons

```citry-html
<c-bs-list-group as_="div">
  <c-bs-list-group-item as_="button" c-active="True">The current button</c-bs-list-group-item>
  <c-bs-list-group-item as_="button">A second button item</c-bs-list-group-item>
  <c-bs-list-group-item as_="button">A third button item</c-bs-list-group-item>
  <c-bs-list-group-item as_="button">A fourth button item</c-bs-list-group-item>
  <c-bs-list-group-item as_="button" c-disabled="True">A disabled button item</c-bs-list-group-item>
</c-bs-list-group>
```

**Preview:**

--8<-- "snippets/listgroup_example_5.html"

---

## Flush

```citry-html
<c-bs-list-group c-flush="True">
  <c-bs-list-group-item>An item</c-bs-list-group-item>
  <c-bs-list-group-item>A second item</c-bs-list-group-item>
  <c-bs-list-group-item>A third item</c-bs-list-group-item>
  <c-bs-list-group-item>A fourth item</c-bs-list-group-item>
  <c-bs-list-group-item>And a fifth one</c-bs-list-group-item>
</c-bs-list-group>
```

**Preview:**

--8<-- "snippets/listgroup_example_6.html"

---

## Numbered

```citry-html
<c-bs-list-group c-numbered="True">
  <c-bs-list-group-item>A list item</c-bs-list-group-item>
  <c-bs-list-group-item>A list item</c-bs-list-group-item>
  <c-bs-list-group-item>A list item</c-bs-list-group-item>
</c-bs-list-group>
```

**Preview:**

--8<-- "snippets/listgroup_example_7.html"

---

## Numbered With Custom Content

```citry-html
<c-bs-list-group c-numbered="True">
  <c-bs-list-group-item c-attrs="{'class': 'd-flex justify-content-between align-items-start'}">
    <div class="ms-2 me-auto">
      <div class="fw-bold">Subheading</div>
      Content for list item
    </div>
    <c-bs-badge bg="primary" c-pill="True">14</c-bs-badge>
  </c-bs-list-group-item>
  <c-bs-list-group-item c-attrs="{'class': 'd-flex justify-content-between align-items-start'}">
    <div class="ms-2 me-auto">
      <div class="fw-bold">Subheading</div>
      Content for list item
    </div>
    <c-bs-badge bg="primary" c-pill="True">14</c-bs-badge>
  </c-bs-list-group-item>
  <c-bs-list-group-item c-attrs="{'class': 'd-flex justify-content-between align-items-start'}">
    <div class="ms-2 me-auto">
      <div class="fw-bold">Subheading</div>
      Content for list item
    </div>
    <c-bs-badge bg="primary" c-pill="True">14</c-bs-badge>
  </c-bs-list-group-item>
</c-bs-list-group>
```

**Preview:**

--8<-- "snippets/listgroup_example_8.html"

---

## Horizontal

```citry-html
<c-bs-list-group c-horizontal="True">
  <c-bs-list-group-item>An item</c-bs-list-group-item>
  <c-bs-list-group-item>A second item</c-bs-list-group-item>
  <c-bs-list-group-item>A third item</c-bs-list-group-item>
</c-bs-list-group>
```

**Preview:**

--8<-- "snippets/listgroup_example_9.html"

---

## Horizontal Responsive Sm

```citry-html
<c-bs-list-group horizontal="sm">
  <c-bs-list-group-item>An item</c-bs-list-group-item>
  <c-bs-list-group-item>A second item</c-bs-list-group-item>
  <c-bs-list-group-item>A third item</c-bs-list-group-item>
</c-bs-list-group>
```

**Preview:**

--8<-- "snippets/listgroup_example_10.html"

---

## Horizontal Responsive Md

```citry-html
<c-bs-list-group horizontal="md">
  <c-bs-list-group-item>An item</c-bs-list-group-item>
  <c-bs-list-group-item>A second item</c-bs-list-group-item>
  <c-bs-list-group-item>A third item</c-bs-list-group-item>
</c-bs-list-group>
```

**Preview:**

--8<-- "snippets/listgroup_example_11.html"

---

## Contextual Variants

```citry-html
<c-bs-list-group>
  <c-bs-list-group-item>A simple default list group item</c-bs-list-group-item>
  <c-bs-list-group-item variant="primary">A simple primary item</c-bs-list-group-item>
  <c-bs-list-group-item variant="secondary">A simple secondary item</c-bs-list-group-item>
  <c-bs-list-group-item variant="success">A simple success item</c-bs-list-group-item>
  <c-bs-list-group-item variant="danger">A simple danger item</c-bs-list-group-item>
  <c-bs-list-group-item variant="warning">A simple warning item</c-bs-list-group-item>
  <c-bs-list-group-item variant="info">A simple info item</c-bs-list-group-item>
  <c-bs-list-group-item variant="light">A simple light item</c-bs-list-group-item>
  <c-bs-list-group-item variant="dark">A simple dark item</c-bs-list-group-item>
</c-bs-list-group>
```

**Preview:**

--8<-- "snippets/listgroup_example_12.html"

---

## Contextual Variants For Links

```citry-html
<c-bs-list-group as_="div">
  <c-bs-list-group-item href="#">A simple default item</c-bs-list-group-item>
  <c-bs-list-group-item href="#" variant="primary">A simple primary item</c-bs-list-group-item>
  <c-bs-list-group-item href="#" variant="secondary">A simple secondary item</c-bs-list-group-item>
  <c-bs-list-group-item href="#" variant="success">A simple success item</c-bs-list-group-item>
  <c-bs-list-group-item href="#" variant="danger">A simple danger item</c-bs-list-group-item>
  <c-bs-list-group-item href="#" variant="warning">A simple warning item</c-bs-list-group-item>
  <c-bs-list-group-item href="#" variant="info">A simple info item</c-bs-list-group-item>
  <c-bs-list-group-item href="#" variant="light">A simple light item</c-bs-list-group-item>
  <c-bs-list-group-item href="#" variant="dark">A simple dark item</c-bs-list-group-item>
</c-bs-list-group>
```

**Preview:**

--8<-- "snippets/listgroup_example_13.html"

---

## With Badges

```citry-html
<c-bs-list-group>
  <c-bs-list-group-item c-attrs="{'class': 'd-flex justify-content-between align-items-center'}">
    A list item
    <c-bs-badge bg="primary" c-pill="True">14</c-bs-badge>
  </c-bs-list-group-item>
  <c-bs-list-group-item c-attrs="{'class': 'd-flex justify-content-between align-items-center'}">
    A second list item
    <c-bs-badge bg="primary" c-pill="True">2</c-bs-badge>
  </c-bs-list-group-item>
  <c-bs-list-group-item c-attrs="{'class': 'd-flex justify-content-between align-items-center'}">
    A third list item
    <c-bs-badge bg="primary" c-pill="True">1</c-bs-badge>
  </c-bs-list-group-item>
</c-bs-list-group>
```

**Preview:**

--8<-- "snippets/listgroup_example_14.html"

---

## Custom Content

```citry-html
<c-bs-list-group as_="div">
  <c-bs-list-group-item href="#" c-active="True">
    <div class="d-flex w-100 justify-content-between">
      <h5 class="mb-1">List group item heading</h5>
      <small>3 days ago</small>
    </div>
    <p class="mb-1">Some placeholder content in a paragraph.</p>
    <small>And some small print.</small>
  </c-bs-list-group-item>
  <c-bs-list-group-item href="#">
    <div class="d-flex w-100 justify-content-between">
      <h5 class="mb-1">List group item heading</h5>
      <small class="text-body-secondary">3 days ago</small>
    </div>
    <p class="mb-1">Some placeholder content in a paragraph.</p>
    <small class="text-body-secondary">And some muted small print.</small>
  </c-bs-list-group-item>
  <c-bs-list-group-item href="#">
    <div class="d-flex w-100 justify-content-between">
      <h5 class="mb-1">List group item heading</h5>
      <small class="text-body-secondary">3 days ago</small>
    </div>
    <p class="mb-1">Some placeholder content in a paragraph.</p>
    <small class="text-body-secondary">And some muted small print.</small>
  </c-bs-list-group-item>
</c-bs-list-group>
```

**Preview:**

--8<-- "snippets/listgroup_example_15.html"

---

## With Checkboxes

```citry-html
<c-bs-list-group>
  <c-bs-list-group-item>
    <c-bs-form-check-input c-value="''" c-attrs="{'class': 'me-1', 'id': 'firstCheckbox'}" />
    <c-bs-form-check-label for_="firstCheckbox">First checkbox</c-bs-form-check-label>
  </c-bs-list-group-item>
  <c-bs-list-group-item>
    <c-bs-form-check-input c-value="''" c-attrs="{'class': 'me-1', 'id': 'secondCheckbox'}" />
    <c-bs-form-check-label for_="secondCheckbox">Second checkbox</c-bs-form-check-label>
  </c-bs-list-group-item>
  <c-bs-list-group-item>
    <c-bs-form-check-input c-value="''" c-attrs="{'class': 'me-1', 'id': 'thirdCheckbox'}" />
    <c-bs-form-check-label for_="thirdCheckbox">Third checkbox</c-bs-form-check-label>
  </c-bs-list-group-item>
</c-bs-list-group>
```

**Preview:**

--8<-- "snippets/listgroup_example_16.html"

---

## With Radio Buttons

```citry-html
<c-bs-list-group>
  <c-bs-list-group-item>
    <c-bs-form-check-input type="radio" name="listGroupRadio" c-value="''" c-checked="True" c-attrs="{'class': 'me-1', 'id': 'firstRadio'}" />
    <c-bs-form-check-label for_="firstRadio">First radio</c-bs-form-check-label>
  </c-bs-list-group-item>
  <c-bs-list-group-item>
    <c-bs-form-check-input type="radio" name="listGroupRadio" c-value="''" c-attrs="{'class': 'me-1', 'id': 'secondRadio'}" />
    <c-bs-form-check-label for_="secondRadio">Second radio</c-bs-form-check-label>
  </c-bs-list-group-item>
  <c-bs-list-group-item>
    <c-bs-form-check-input type="radio" name="listGroupRadio" c-value="''" c-attrs="{'class': 'me-1', 'id': 'thirdRadio'}" />
    <c-bs-form-check-label for_="thirdRadio">Third radio</c-bs-form-check-label>
  </c-bs-list-group-item>
</c-bs-list-group>
```

**Preview:**

--8<-- "snippets/listgroup_example_17.html"

---
