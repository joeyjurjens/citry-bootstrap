# Accordion

## Basic

```citry-html
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
```

**Preview:**

--8<-- "snippets/accordion_example_1.html"

---

## With Icon In Header

```citry-html
<c-bs-accordion>
  <c-bs-accordion-item c-default_open="True">
    <c-bs-accordion-header>
      <i class="bi bi-info-circle"></i>
      Accordion Item with Icon
    </c-bs-accordion-header>
    <c-bs-accordion-body>This accordion item has an icon in the header.</c-bs-accordion-body>
  </c-bs-accordion-item>
</c-bs-accordion>
```

**Preview:**

--8<-- "snippets/accordion_example_2.html"

---

## With Badge In Header

```citry-html
<c-bs-accordion>
  <c-bs-accordion-item c-default_open="True">
    <c-bs-accordion-header>
      Accordion Item
      <c-bs-badge bg="primary">New</c-bs-badge>
    </c-bs-accordion-header>
    <c-bs-accordion-body>This accordion item has a badge in the header.</c-bs-accordion-body>
  </c-bs-accordion-item>
</c-bs-accordion>
```

**Preview:**

--8<-- "snippets/accordion_example_3.html"

---

## Flush

```citry-html
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
```

**Preview:**

--8<-- "snippets/accordion_example_4.html"

---

## Always Open

```citry-html
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
```

**Preview:**

--8<-- "snippets/accordion_example_5.html"

---
