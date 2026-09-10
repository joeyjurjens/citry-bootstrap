# Offcanvas

## Basic

```citry-html
<c-bs-offcanvas c-scroll="False" c-keyboard="False">
  <c-fill name="toggle">
    <c-bs-offcanvas-toggle c-attrs='{"class": "btn btn-primary", "type": "button"}'>Toggle Offcanvas</c-bs-offcanvas-toggle>
  </c-fill>
  <c-fill name="default">
    <c-bs-offcanvas-header>
      <c-bs-offcanvas-title>Offcanvas</c-bs-offcanvas-title>
    </c-bs-offcanvas-header>
    <c-bs-offcanvas-body>Content for the offcanvas goes here. You can place just about any Bootstrap component or custom elements here.</c-bs-offcanvas-body>
  </c-fill>
</c-bs-offcanvas>
```

**Preview:**

--8<-- "snippets/offcanvas_example_1.html"

---

## Offcanvas Placement Start

```citry-html
<c-bs-offcanvas placement="start">
  <c-fill name="toggle">
    <c-bs-offcanvas-toggle c-attrs="{'class': 'btn btn-primary'}">Toggle Offcanvas</c-bs-offcanvas-toggle>
  </c-fill>
  <c-fill name="default">
    <c-bs-offcanvas-header>
      <c-bs-offcanvas-title>Offcanvas Start</c-bs-offcanvas-title>
    </c-bs-offcanvas-header>
    <c-bs-offcanvas-body>
      <p>This offcanvas appears from the start (left).</p>
    </c-bs-offcanvas-body>
  </c-fill>
</c-bs-offcanvas>
```

**Preview:**

--8<-- "snippets/offcanvas_example_2.html"

---

## Offcanvas Placement End

```citry-html
<c-bs-offcanvas placement="end">
  <c-fill name="toggle">
    <c-bs-offcanvas-toggle c-attrs="{'class': 'btn btn-primary'}">Toggle Offcanvas</c-bs-offcanvas-toggle>
  </c-fill>
  <c-fill name="default">
    <c-bs-offcanvas-header>
      <c-bs-offcanvas-title>Offcanvas End</c-bs-offcanvas-title>
    </c-bs-offcanvas-header>
    <c-bs-offcanvas-body>
      <p>This offcanvas appears from the end (right).</p>
    </c-bs-offcanvas-body>
  </c-fill>
</c-bs-offcanvas>
```

**Preview:**

--8<-- "snippets/offcanvas_example_3.html"

---

## Offcanvas Placement Top

```citry-html
<c-bs-offcanvas placement="top">
  <c-fill name="toggle">
    <c-bs-offcanvas-toggle c-attrs="{'class': 'btn btn-primary'}">Toggle Offcanvas</c-bs-offcanvas-toggle>
  </c-fill>
  <c-fill name="default">
    <c-bs-offcanvas-header>
      <c-bs-offcanvas-title>Offcanvas Top</c-bs-offcanvas-title>
    </c-bs-offcanvas-header>
    <c-bs-offcanvas-body>
      <p>This offcanvas appears from the top.</p>
    </c-bs-offcanvas-body>
  </c-fill>
</c-bs-offcanvas>
```

**Preview:**

--8<-- "snippets/offcanvas_example_4.html"

---

## Offcanvas Placement Bottom

```citry-html
<c-bs-offcanvas placement="bottom">
  <c-fill name="toggle">
    <c-bs-offcanvas-toggle c-attrs="{'class': 'btn btn-primary'}">Toggle Offcanvas</c-bs-offcanvas-toggle>
  </c-fill>
  <c-fill name="default">
    <c-bs-offcanvas-header>
      <c-bs-offcanvas-title>Offcanvas Bottom</c-bs-offcanvas-title>
    </c-bs-offcanvas-header>
    <c-bs-offcanvas-body>
      <p>This offcanvas appears from the bottom.</p>
    </c-bs-offcanvas-body>
  </c-fill>
</c-bs-offcanvas>
```

**Preview:**

--8<-- "snippets/offcanvas_example_5.html"

---

## Offcanvas Body Scrolling Enabled

```citry-html
<c-bs-offcanvas c-scroll="True" backdrop="false">
  <c-fill name="toggle">
    <c-bs-offcanvas-toggle c-attrs="{'class': 'btn btn-primary'}">Toggle Offcanvas</c-bs-offcanvas-toggle>
  </c-fill>
  <c-fill name="default">
    <c-bs-offcanvas-header>
      <c-bs-offcanvas-title>Offcanvas with body scrolling</c-bs-offcanvas-title>
    </c-bs-offcanvas-header>
    <c-bs-offcanvas-body>
      <p>Try scrolling the rest of the page to see this option in action.</p>
    </c-bs-offcanvas-body>
  </c-fill>
</c-bs-offcanvas>
```

**Preview:**

--8<-- "snippets/offcanvas_example_6.html"

---

## Offcanvas With Backdrop

```citry-html
<c-bs-offcanvas c-scroll="True">
  <c-fill name="toggle">
    <c-bs-offcanvas-toggle c-attrs="{'class': 'btn btn-primary'}">Toggle Offcanvas</c-bs-offcanvas-toggle>
  </c-fill>
  <c-fill name="default">
    <c-bs-offcanvas-header>
      <c-bs-offcanvas-title>Backdrop with scrolling</c-bs-offcanvas-title>
    </c-bs-offcanvas-header>
    <c-bs-offcanvas-body>
      <p>Try scrolling the rest of the page to see this option in action.</p>
    </c-bs-offcanvas-body>
  </c-fill>
</c-bs-offcanvas>
```

**Preview:**

--8<-- "snippets/offcanvas_example_7.html"

---

## Offcanvas Static Backdrop

```citry-html
<c-bs-offcanvas backdrop="static">
  <c-fill name="toggle">
    <c-bs-offcanvas-toggle c-attrs="{'class': 'btn btn-primary'}">Toggle Offcanvas</c-bs-offcanvas-toggle>
  </c-fill>
  <c-fill name="default">
    <c-bs-offcanvas-header>
      <c-bs-offcanvas-title>Static Backdrop</c-bs-offcanvas-title>
    </c-bs-offcanvas-header>
    <c-bs-offcanvas-body>
      <p>I will not close if you click outside of me.</p>
    </c-bs-offcanvas-body>
  </c-fill>
</c-bs-offcanvas>
```

**Preview:**

--8<-- "snippets/offcanvas_example_8.html"

---

## Offcanvas No Backdrop

```citry-html
<c-bs-offcanvas backdrop="false">
  <c-fill name="toggle">
    <c-bs-offcanvas-toggle c-attrs="{'class': 'btn btn-primary'}">Toggle Offcanvas</c-bs-offcanvas-toggle>
  </c-fill>
  <c-fill name="default">
    <c-bs-offcanvas-header>
      <c-bs-offcanvas-title>No Backdrop</c-bs-offcanvas-title>
    </c-bs-offcanvas-header>
    <c-bs-offcanvas-body>
      <p>This offcanvas has no backdrop.</p>
    </c-bs-offcanvas-body>
  </c-fill>
</c-bs-offcanvas>
```

**Preview:**

--8<-- "snippets/offcanvas_example_9.html"

---

## Offcanvas Responsive Lg

```citry-html
<c-bs-offcanvas responsive="lg" placement="end">
  <c-fill name="toggle">
    <c-bs-offcanvas-toggle c-attrs="{'class': 'btn btn-primary'}">Toggle Offcanvas</c-bs-offcanvas-toggle>
  </c-fill>
  <c-fill name="default">
    <c-bs-offcanvas-header>
      <c-bs-offcanvas-title>Responsive offcanvas</c-bs-offcanvas-title>
    </c-bs-offcanvas-header>
    <c-bs-offcanvas-body>
      <p>This is content within an offcanvas-lg.</p>
    </c-bs-offcanvas-body>
  </c-fill>
</c-bs-offcanvas>
```

**Preview:**

--8<-- "snippets/offcanvas_example_10.html"

---

## Offcanvas Responsive Md

```citry-html
<c-bs-offcanvas responsive="md">
  <c-fill name="toggle">
    <c-bs-offcanvas-toggle c-attrs="{'class': 'btn btn-primary'}">Toggle Offcanvas</c-bs-offcanvas-toggle>
  </c-fill>
  <c-fill name="default">
    <c-bs-offcanvas-header>
      <c-bs-offcanvas-title>Responsive MD offcanvas</c-bs-offcanvas-title>
    </c-bs-offcanvas-header>
    <c-bs-offcanvas-body>
      <p>This is content within an offcanvas-md.</p>
    </c-bs-offcanvas-body>
  </c-fill>
</c-bs-offcanvas>
```

**Preview:**

--8<-- "snippets/offcanvas_example_11.html"

---

## Offcanvas Without Close Button

```citry-html
<c-bs-offcanvas>
  <c-fill name="toggle">
    <c-bs-offcanvas-toggle c-attrs="{'class': 'btn btn-primary'}">Toggle Offcanvas</c-bs-offcanvas-toggle>
  </c-fill>
  <c-fill name="default">
    <c-bs-offcanvas-header c-close_button="False">
      <c-bs-offcanvas-title>No Close Button</c-bs-offcanvas-title>
    </c-bs-offcanvas-header>
    <c-bs-offcanvas-body>
      <p>This offcanvas header has no close button.</p>
    </c-bs-offcanvas-body>
  </c-fill>
</c-bs-offcanvas>
```

**Preview:**

--8<-- "snippets/offcanvas_example_12.html"

---

## Offcanvas Custom Title Heading

```citry-html
<c-bs-offcanvas>
  <c-fill name="toggle">
    <c-bs-offcanvas-toggle c-attrs="{'class': 'btn btn-primary'}">Toggle Offcanvas</c-bs-offcanvas-toggle>
  </c-fill>
  <c-fill name="default">
    <c-bs-offcanvas-header>
      <c-bs-offcanvas-title as_="h3">Custom Heading</c-bs-offcanvas-title>
    </c-bs-offcanvas-header>
    <c-bs-offcanvas-body>
      <p>This offcanvas title uses h3.</p>
    </c-bs-offcanvas-body>
  </c-fill>
</c-bs-offcanvas>
```

**Preview:**

--8<-- "snippets/offcanvas_example_13.html"

---
