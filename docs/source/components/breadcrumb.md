# Breadcrumb

## Basic

```citry-html
<c-bs-breadcrumb>
  <c-bs-breadcrumb-item href="#">Home</c-bs-breadcrumb-item>
  <c-bs-breadcrumb-item c-active="True">Library</c-bs-breadcrumb-item>
</c-bs-breadcrumb>
```

**Preview:**

--8<-- "snippets/breadcrumb_example_1.html"

---

## Single Item Active

```citry-html
<c-bs-breadcrumb>
  <c-bs-breadcrumb-item c-active="True">Home</c-bs-breadcrumb-item>
</c-bs-breadcrumb>
```

**Preview:**

--8<-- "snippets/breadcrumb_example_2.html"

---

## Three Items

```citry-html
<c-bs-breadcrumb>
  <c-bs-breadcrumb-item href="#">Home</c-bs-breadcrumb-item>
  <c-bs-breadcrumb-item href="#">Library</c-bs-breadcrumb-item>
  <c-bs-breadcrumb-item c-active="True">Data</c-bs-breadcrumb-item>
</c-bs-breadcrumb>
```

**Preview:**

--8<-- "snippets/breadcrumb_example_3.html"

---

## Custom Divider Greater Than

```citry-html
<c-bs-breadcrumb c-attrs="{'style': '--bs-breadcrumb-divider: \'>\';'}">
  <c-bs-breadcrumb-item href="#">Home</c-bs-breadcrumb-item>
  <c-bs-breadcrumb-item c-active="True">Library</c-bs-breadcrumb-item>
</c-bs-breadcrumb>
```

**Preview:**

--8<-- "snippets/breadcrumb_example_4.html"

---

## No Divider

```citry-html
<c-bs-breadcrumb c-attrs="{'style': '--bs-breadcrumb-divider: \'\';'}">
  <c-bs-breadcrumb-item href="#">Home</c-bs-breadcrumb-item>
  <c-bs-breadcrumb-item c-active="True">Library</c-bs-breadcrumb-item>
</c-bs-breadcrumb>
```

**Preview:**

--8<-- "snippets/breadcrumb_example_5.html"

---

## Custom Label

```citry-html
<c-bs-breadcrumb>
  <c-bs-breadcrumb-item href="#">Home</c-bs-breadcrumb-item>
  <c-bs-breadcrumb-item c-active="True">Library</c-bs-breadcrumb-item>
</c-bs-breadcrumb>
```

**Preview:**

--8<-- "snippets/breadcrumb_example_6.html"

---

## Custom Attrs

```citry-html
<c-bs-breadcrumb c-attrs="{'class': 'custom-class'}">
  <c-bs-breadcrumb-item href="#">Home</c-bs-breadcrumb-item>
  <c-bs-breadcrumb-item c-active="True">Library</c-bs-breadcrumb-item>
</c-bs-breadcrumb>
```

**Preview:**

--8<-- "snippets/breadcrumb_example_7.html"

---

## Item Custom Attrs

```citry-html
<c-bs-breadcrumb>
  <c-bs-breadcrumb-item href="#" c-attrs="{'data-test': 'home'}">Home</c-bs-breadcrumb-item>
  <c-bs-breadcrumb-item c-active="True" c-attrs="{'class': 'highlighted'}">Library</c-bs-breadcrumb-item>
</c-bs-breadcrumb>
```

**Preview:**

--8<-- "snippets/breadcrumb_example_8.html"

---
