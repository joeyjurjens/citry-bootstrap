# Layout

## Basic Container

```citry-html
<c-bs-container>Content</c-bs-container>
```

**Preview:**

--8<-- "snippets/layout_example_1.html"

---

## Container Fluid

```citry-html
<c-bs-container c-fluid="True">Content</c-bs-container>
```

**Preview:**

--8<-- "snippets/layout_example_2.html"

---

## Container Fluid Breakpoint

```citry-html
<c-bs-container fluid="md">Content</c-bs-container>
```

**Preview:**

--8<-- "snippets/layout_example_3.html"

---

## Basic Row With Cols

```citry-html
<c-bs-container>
  <c-bs-row>
    <c-bs-col>Column</c-bs-col>
    <c-bs-col>Column</c-bs-col>
    <c-bs-col>Column</c-bs-col>
  </c-bs-row>
</c-bs-container>
```

**Preview:**

--8<-- "snippets/layout_example_4.html"

---

## Responsive Columns

```citry-html
<c-bs-container>
  <c-bs-row>
    <c-bs-col c-sm="8">col-sm-8</c-bs-col>
    <c-bs-col c-sm="4">col-sm-4</c-bs-col>
  </c-bs-row>
</c-bs-container>
```

**Preview:**

--8<-- "snippets/layout_example_5.html"

---

## Mixed Responsive Columns

```citry-html
<c-bs-container>
  <c-bs-row>
    <c-bs-col c-md="8">.col-md-8</c-bs-col>
    <c-bs-col c-col="6" c-md="4">.col-6 .col-md-4</c-bs-col>
  </c-bs-row>
</c-bs-container>
```

**Preview:**

--8<-- "snippets/layout_example_6.html"

---

## Row With Gutters

```citry-html
<c-bs-container>
  <c-bs-row c-gutter="3">
    <c-bs-col>Column</c-bs-col>
    <c-bs-col>Column</c-bs-col>
  </c-bs-row>
</c-bs-container>
```

**Preview:**

--8<-- "snippets/layout_example_7.html"

---

## Row Cols

```citry-html
<c-bs-container>
  <c-bs-row c-cols="2">
    <c-bs-col>Column</c-bs-col>
    <c-bs-col>Column</c-bs-col>
    <c-bs-col>Column</c-bs-col>
    <c-bs-col>Column</c-bs-col>
  </c-bs-row>
</c-bs-container>
```

**Preview:**

--8<-- "snippets/layout_example_8.html"

---

## Col Auto

```citry-html
<c-bs-container>
  <c-bs-row>
    <c-bs-col>1 of 3</c-bs-col>
    <c-bs-col col="auto">Variable width content</c-bs-col>
    <c-bs-col>3 of 3</c-bs-col>
  </c-bs-row>
</c-bs-container>
```

**Preview:**

--8<-- "snippets/layout_example_9.html"

---
