# Stack

## Vstack

```citry-html
<c-bs-stack direction="vertical" c-gap="3">
  <div class="p-2">First item</div>
  <div class="p-2">Second item</div>
  <div class="p-2">Third item</div>
</c-bs-stack>
```

**Preview:**

--8<-- "snippets/stack_example_1.html"

---

## Hstack

```citry-html
<c-bs-stack direction="horizontal" c-gap="3">
  <div class="p-2">First item</div>
  <div class="p-2">Second item</div>
  <div class="p-2">Third item</div>
</c-bs-stack>
```

**Preview:**

--8<-- "snippets/stack_example_2.html"

---

## Hstack With Spacer

```citry-html
<c-bs-stack direction="horizontal" c-gap="3">
  <div class="p-2">First item</div>
  <div class="p-2 ms-auto">Second item</div>
  <div class="p-2">Third item</div>
</c-bs-stack>
```

**Preview:**

--8<-- "snippets/stack_example_3.html"

---

## Hstack With Vertical Rule

```citry-html
<c-bs-stack direction="horizontal" c-gap="3">
  <div class="p-2">First item</div>
  <div class="p-2 ms-auto">Second item</div>
  <div class="vr"></div>
  <div class="p-2">Third item</div>
</c-bs-stack>
```

**Preview:**

--8<-- "snippets/stack_example_4.html"

---

## Vstack Buttons

```citry-html
<c-bs-stack direction="vertical" c-gap="2">
  <c-bs-button variant="secondary">Save changes</c-bs-button>
  <c-bs-button variant="secondary" c-outline="True">Cancel</c-bs-button>
</c-bs-stack>
```

**Preview:**

--8<-- "snippets/stack_example_5.html"

---

## Hstack Inline Form

```citry-html
<c-bs-stack direction="horizontal" c-gap="3">
  <c-bs-form-control placeholder="Add your item here..." c-attrs="{'class': 'me-auto', 'aria-label': 'Add your item here...'}" />
  <c-bs-button variant="secondary">Submit</c-bs-button>
  <div class="vr"></div>
  <c-bs-button variant="danger" c-outline="True">Reset</c-bs-button>
</c-bs-stack>
```

**Preview:**

--8<-- "snippets/stack_example_6.html"

---

## Vstack No Gap

```citry-html
<c-bs-stack direction="vertical">
  <div class="p-2">First item</div>
  <div class="p-2">Second item</div>
  <div class="p-2">Third item</div>
</c-bs-stack>
```

**Preview:**

--8<-- "snippets/stack_example_7.html"

---

## Hstack No Gap

```citry-html
<c-bs-stack direction="horizontal">
  <div class="p-2">First item</div>
  <div class="p-2">Second item</div>
  <div class="p-2">Third item</div>
</c-bs-stack>
```

**Preview:**

--8<-- "snippets/stack_example_8.html"

---
