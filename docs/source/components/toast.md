# Toast

## Basic With Header

```citry-html
<c-bs-toast>
  <c-bs-toast-header>
    <img src="https://placehold.net/600x400.png" class="rounded me-2" alt="Toast icon" />
    <strong class="me-auto">Bootstrap</strong>
    <small>11 mins ago</small>
  </c-bs-toast-header>
  <c-bs-toast-body>Hello, world! This is a toast message.</c-bs-toast-body>
</c-bs-toast>
```

**Preview:**

--8<-- "snippets/toast_example_1.html"

---

## Autohide False

```citry-html
<c-bs-toast c-autohide="False">
  <c-bs-toast-header>
    <img src="https://placehold.net/600x400.png" class="rounded me-2" alt="Toast icon" />
    <strong class="me-auto">Bootstrap</strong>
    <small>11 mins ago</small>
  </c-bs-toast-header>
  <c-bs-toast-body>Hello, world! This is a toast message.</c-bs-toast-body>
</c-bs-toast>
```

**Preview:**

--8<-- "snippets/toast_example_2.html"

---

## Translucent

```citry-html
<c-bs-toast>
  <c-bs-toast-header>
    <img src="https://placehold.net/600x400.png" class="rounded me-2" alt="Toast icon" />
    <strong class="me-auto">Bootstrap</strong>
    <small class="text-body-secondary">11 mins ago</small>
  </c-bs-toast-header>
  <c-bs-toast-body>Hello, world! This is a toast message.</c-bs-toast-body>
</c-bs-toast>
```

**Preview:**

--8<-- "snippets/toast_example_3.html"

---

## Stacking

```citry-html
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
```

**Preview:**

--8<-- "snippets/toast_example_4.html"

---

## Custom Content Simplified

```citry-html
<c-bs-toast c-attrs="{'class': 'align-items-center'}">
  <div class="d-flex">
    <c-bs-toast-body>Hello, world! This is a toast message.</c-bs-toast-body>
    <c-bs-close-button c-attrs="{'class': 'me-2 m-auto', 'data-bs-dismiss': 'toast'}" />
  </div>
</c-bs-toast>
```

**Preview:**

--8<-- "snippets/toast_example_5.html"

---

## Custom Content With Actions

```citry-html
<c-bs-toast>
  <c-bs-toast-body>
    Hello, world! This is a toast message.
    <div class="mt-2 pt-2 border-top">
      <c-bs-button variant="primary" size="sm">Take action</c-bs-button>
      <c-bs-button variant="secondary" size="sm" c-attrs="{'data-bs-dismiss': 'toast'}">Close</c-bs-button>
    </div>
  </c-bs-toast-body>
</c-bs-toast>
```

**Preview:**

--8<-- "snippets/toast_example_6.html"

---

## Color Scheme Primary

```citry-html
<c-bs-toast c-attrs="{'class': 'align-items-center text-bg-primary border-0'}">
  <div class="d-flex">
    <c-bs-toast-body>Hello, world! This is a toast message.</c-bs-toast-body>
    <c-bs-close-button variant="white" c-attrs="{'class': 'me-2 m-auto', 'data-bs-dismiss': 'toast'}" />
  </div>
</c-bs-toast>
```

**Preview:**

--8<-- "snippets/toast_example_7.html"

---

## Toast Container Bottom End

```citry-html
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
```

**Preview:**

--8<-- "snippets/toast_example_8.html"

---
