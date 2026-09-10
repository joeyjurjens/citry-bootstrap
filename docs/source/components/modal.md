# Modal

## Basic

```citry-html
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
```

**Preview:**

--8<-- "snippets/modal_example_1.html"

---

## Modal Small Size

```citry-html
<c-bs-modal size="sm">
  <c-bs-modal-header>
    <c-bs-modal-title>Small Modal</c-bs-modal-title>
  </c-bs-modal-header>
  <c-bs-modal-body>
    <p>This is a small modal.</p>
  </c-bs-modal-body>
</c-bs-modal>
```

**Preview:**

--8<-- "snippets/modal_example_2.html"

---

## Modal Large Size

```citry-html
<c-bs-modal size="lg">
  <c-bs-modal-header>
    <c-bs-modal-title>Large Modal</c-bs-modal-title>
  </c-bs-modal-header>
  <c-bs-modal-body>
    <p>This is a large modal.</p>
  </c-bs-modal-body>
</c-bs-modal>
```

**Preview:**

--8<-- "snippets/modal_example_3.html"

---

## Modal Extra Large Size

```citry-html
<c-bs-modal size="xl">
  <c-bs-modal-header>
    <c-bs-modal-title>Extra Large Modal</c-bs-modal-title>
  </c-bs-modal-header>
  <c-bs-modal-body>
    <p>This is an extra large modal.</p>
  </c-bs-modal-body>
</c-bs-modal>
```

**Preview:**

--8<-- "snippets/modal_example_4.html"

---

## Modal Fullscreen

```citry-html
<c-bs-modal c-fullscreen="True">
  <c-bs-modal-header>
    <c-bs-modal-title>Fullscreen Modal</c-bs-modal-title>
  </c-bs-modal-header>
  <c-bs-modal-body>
    <p>This is a fullscreen modal.</p>
  </c-bs-modal-body>
</c-bs-modal>
```

**Preview:**

--8<-- "snippets/modal_example_5.html"

---

## Modal Fullscreen Sm Down

```citry-html
<c-bs-modal fullscreen="sm">
  <c-bs-modal-header>
    <c-bs-modal-title>Fullscreen Below SM</c-bs-modal-title>
  </c-bs-modal-header>
  <c-bs-modal-body>
    <p>This modal is fullscreen below sm breakpoint.</p>
  </c-bs-modal-body>
</c-bs-modal>
```

**Preview:**

--8<-- "snippets/modal_example_6.html"

---

## Modal Fullscreen Md Down

```citry-html
<c-bs-modal fullscreen="md">
  <c-bs-modal-header>
    <c-bs-modal-title>Fullscreen Below MD</c-bs-modal-title>
  </c-bs-modal-header>
  <c-bs-modal-body>
    <p>This modal is fullscreen below md breakpoint.</p>
  </c-bs-modal-body>
</c-bs-modal>
```

**Preview:**

--8<-- "snippets/modal_example_7.html"

---

## Modal Fullscreen Lg Down

```citry-html
<c-bs-modal fullscreen="lg">
  <c-bs-modal-header>
    <c-bs-modal-title>Fullscreen Below LG</c-bs-modal-title>
  </c-bs-modal-header>
  <c-bs-modal-body>
    <p>This modal is fullscreen below lg breakpoint.</p>
  </c-bs-modal-body>
</c-bs-modal>
```

**Preview:**

--8<-- "snippets/modal_example_8.html"

---

## Modal Centered

```citry-html
<c-bs-modal c-centered="True">
  <c-bs-modal-header>
    <c-bs-modal-title>Vertically Centered Modal</c-bs-modal-title>
  </c-bs-modal-header>
  <c-bs-modal-body>
    <p>This modal is vertically centered.</p>
  </c-bs-modal-body>
</c-bs-modal>
```

**Preview:**

--8<-- "snippets/modal_example_9.html"

---

## Modal Scrollable

```citry-html
<c-bs-modal c-scrollable="True">
  <c-bs-modal-header>
    <c-bs-modal-title>Scrollable Modal</c-bs-modal-title>
  </c-bs-modal-header>
  <c-bs-modal-body>
    <p>This modal has a scrollable body when content is long.</p>
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
  </c-bs-modal-body>
</c-bs-modal>
```

**Preview:**

--8<-- "snippets/modal_example_10.html"

---

## Modal Static Backdrop

```citry-html
<c-bs-modal backdrop="static" c-keyboard="False">
  <c-bs-modal-header>
    <c-bs-modal-title>Static Backdrop Modal</c-bs-modal-title>
  </c-bs-modal-header>
  <c-bs-modal-body>
    <p>This modal won't close when clicking outside.</p>
  </c-bs-modal-body>
</c-bs-modal>
```

**Preview:**

--8<-- "snippets/modal_example_11.html"

---

## Modal With Form

```citry-html
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
```

**Preview:**

--8<-- "snippets/modal_example_12.html"

---

## Modal Without Fade

```citry-html
<c-bs-modal c-fade="False">
  <c-bs-modal-header>
    <c-bs-modal-title>No Fade Modal</c-bs-modal-title>
  </c-bs-modal-header>
  <c-bs-modal-body>
    <p>This modal doesn't have fade animation.</p>
  </c-bs-modal-body>
</c-bs-modal>
```

**Preview:**

--8<-- "snippets/modal_example_13.html"

---

## Modal Header Without Close Button

```citry-html
<c-bs-modal>
  <c-bs-modal-header c-close_button="False">
    <c-bs-modal-title>No Close Button</c-bs-modal-title>
  </c-bs-modal-header>
  <c-bs-modal-body>
    <p>This modal header has no close button.</p>
  </c-bs-modal-body>
</c-bs-modal>
```

**Preview:**

--8<-- "snippets/modal_example_14.html"

---

## Modal With Custom Title Heading

```citry-html
<c-bs-modal>
  <c-bs-modal-header>
    <c-bs-modal-title as_="h1">Custom Heading Level</c-bs-modal-title>
  </c-bs-modal-header>
  <c-bs-modal-body>
    <p>This modal title uses h1 instead of h5.</p>
  </c-bs-modal-body>
</c-bs-modal>
```

**Preview:**

--8<-- "snippets/modal_example_15.html"

---

## Modal Centered And Scrollable

```citry-html
<c-bs-modal c-centered="True" c-scrollable="True">
  <c-bs-modal-header>
    <c-bs-modal-title>Centered & Scrollable</c-bs-modal-title>
  </c-bs-modal-header>
  <c-bs-modal-body>
    <p>This modal is both centered and scrollable.</p>
  </c-bs-modal-body>
</c-bs-modal>
```

**Preview:**

--8<-- "snippets/modal_example_16.html"

---
