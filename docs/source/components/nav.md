# Nav

## Basic

```citry-html
<c-bs-nav as_="ul">
  <c-bs-nav-item>
    <c-bs-nav-link c-active="True" href="#">Active</c-bs-nav-link>
  </c-bs-nav-item>
  <c-bs-nav-item>
    <c-bs-nav-link href="#">Link</c-bs-nav-link>
  </c-bs-nav-item>
  <c-bs-nav-item>
    <c-bs-nav-link href="#">Link</c-bs-nav-link>
  </c-bs-nav-item>
  <c-bs-nav-item>
    <c-bs-nav-link c-disabled="True">Disabled</c-bs-nav-link>
  </c-bs-nav-item>
</c-bs-nav>
```

**Preview:**

--8<-- "snippets/nav_example_1.html"

---

## Basic Nav Element

```citry-html
<c-bs-nav>
  <c-bs-nav-link c-active="True" href="#">Active</c-bs-nav-link>
  <c-bs-nav-link href="#">Link</c-bs-nav-link>
  <c-bs-nav-link href="#">Link</c-bs-nav-link>
  <c-bs-nav-link c-disabled="True">Disabled</c-bs-nav-link>
</c-bs-nav>
```

**Preview:**

--8<-- "snippets/nav_example_2.html"

---

## Tabs

```citry-html
<c-bs-nav variant="tabs" as_="ul">
  <c-bs-nav-item>
    <c-bs-nav-link c-active="True" href="#">Active</c-bs-nav-link>
  </c-bs-nav-item>
  <c-bs-nav-item>
    <c-bs-nav-link href="#">Link</c-bs-nav-link>
  </c-bs-nav-item>
  <c-bs-nav-item>
    <c-bs-nav-link href="#">Link</c-bs-nav-link>
  </c-bs-nav-item>
  <c-bs-nav-item>
    <c-bs-nav-link c-disabled="True">Disabled</c-bs-nav-link>
  </c-bs-nav-item>
</c-bs-nav>
```

**Preview:**

--8<-- "snippets/nav_example_3.html"

---

## Pills

```citry-html
<c-bs-nav variant="pills" as_="ul">
  <c-bs-nav-item>
    <c-bs-nav-link c-active="True" href="#">Active</c-bs-nav-link>
  </c-bs-nav-item>
  <c-bs-nav-item>
    <c-bs-nav-link href="#">Link</c-bs-nav-link>
  </c-bs-nav-item>
  <c-bs-nav-item>
    <c-bs-nav-link href="#">Link</c-bs-nav-link>
  </c-bs-nav-item>
  <c-bs-nav-item>
    <c-bs-nav-link c-disabled="True">Disabled</c-bs-nav-link>
  </c-bs-nav-item>
</c-bs-nav>
```

**Preview:**

--8<-- "snippets/nav_example_4.html"

---

## Underline

```citry-html
<c-bs-nav variant="underline" as_="ul">
  <c-bs-nav-item>
    <c-bs-nav-link c-active="True" href="#">Active</c-bs-nav-link>
  </c-bs-nav-item>
  <c-bs-nav-item>
    <c-bs-nav-link href="#">Link</c-bs-nav-link>
  </c-bs-nav-item>
  <c-bs-nav-item>
    <c-bs-nav-link href="#">Link</c-bs-nav-link>
  </c-bs-nav-item>
  <c-bs-nav-item>
    <c-bs-nav-link c-disabled="True">Disabled</c-bs-nav-link>
  </c-bs-nav-item>
</c-bs-nav>
```

**Preview:**

--8<-- "snippets/nav_example_5.html"

---

## Vertical

```citry-html
<c-bs-nav c-vertical="True" as_="ul">
  <c-bs-nav-item>
    <c-bs-nav-link c-active="True" href="#">Active</c-bs-nav-link>
  </c-bs-nav-item>
  <c-bs-nav-item>
    <c-bs-nav-link href="#">Link</c-bs-nav-link>
  </c-bs-nav-item>
  <c-bs-nav-item>
    <c-bs-nav-link href="#">Link</c-bs-nav-link>
  </c-bs-nav-item>
  <c-bs-nav-item>
    <c-bs-nav-link c-disabled="True">Disabled</c-bs-nav-link>
  </c-bs-nav-item>
</c-bs-nav>
```

**Preview:**

--8<-- "snippets/nav_example_6.html"

---

## Vertical Nav Element

```citry-html
<c-bs-nav c-vertical="True">
  <c-bs-nav-link c-active="True" href="#">Active</c-bs-nav-link>
  <c-bs-nav-link href="#">Link</c-bs-nav-link>
  <c-bs-nav-link href="#">Link</c-bs-nav-link>
  <c-bs-nav-link c-disabled="True">Disabled</c-bs-nav-link>
</c-bs-nav>
```

**Preview:**

--8<-- "snippets/nav_example_7.html"

---

## Fill

```citry-html
<c-bs-nav variant="pills" c-fill="True" as_="ul">
  <c-bs-nav-item>
    <c-bs-nav-link c-active="True" href="#">Active</c-bs-nav-link>
  </c-bs-nav-item>
  <c-bs-nav-item>
    <c-bs-nav-link href="#">Much longer nav link</c-bs-nav-link>
  </c-bs-nav-item>
  <c-bs-nav-item>
    <c-bs-nav-link href="#">Link</c-bs-nav-link>
  </c-bs-nav-item>
  <c-bs-nav-item>
    <c-bs-nav-link c-disabled="True">Disabled</c-bs-nav-link>
  </c-bs-nav-item>
</c-bs-nav>
```

**Preview:**

--8<-- "snippets/nav_example_8.html"

---

## Fill Nav Element

```citry-html
<c-bs-nav variant="pills" c-fill="True">
  <c-bs-nav-link c-active="True" href="#">Active</c-bs-nav-link>
  <c-bs-nav-link href="#">Much longer nav link</c-bs-nav-link>
  <c-bs-nav-link href="#">Link</c-bs-nav-link>
  <c-bs-nav-link c-disabled="True">Disabled</c-bs-nav-link>
</c-bs-nav>
```

**Preview:**

--8<-- "snippets/nav_example_9.html"

---

## Justified

```citry-html
<c-bs-nav variant="pills" c-justified="True" as_="ul">
  <c-bs-nav-item>
    <c-bs-nav-link c-active="True" href="#">Active</c-bs-nav-link>
  </c-bs-nav-item>
  <c-bs-nav-item>
    <c-bs-nav-link href="#">Much longer nav link</c-bs-nav-link>
  </c-bs-nav-item>
  <c-bs-nav-item>
    <c-bs-nav-link href="#">Link</c-bs-nav-link>
  </c-bs-nav-item>
  <c-bs-nav-item>
    <c-bs-nav-link c-disabled="True">Disabled</c-bs-nav-link>
  </c-bs-nav-item>
</c-bs-nav>
```

**Preview:**

--8<-- "snippets/nav_example_10.html"

---

## Justified Nav Element

```citry-html
<c-bs-nav variant="pills" c-justified="True">
  <c-bs-nav-link c-active="True" href="#">Active</c-bs-nav-link>
  <c-bs-nav-link href="#">Much longer nav link</c-bs-nav-link>
  <c-bs-nav-link href="#">Link</c-bs-nav-link>
  <c-bs-nav-link c-disabled="True">Disabled</c-bs-nav-link>
</c-bs-nav>
```

**Preview:**

--8<-- "snippets/nav_example_11.html"

---

## Button Links

```citry-html
<c-bs-nav variant="pills" as_="ul">
  <c-bs-nav-item>
    <c-bs-nav-link as_="button" c-active="True">Active</c-bs-nav-link>
  </c-bs-nav-item>
  <c-bs-nav-item>
    <c-bs-nav-link as_="button">Link</c-bs-nav-link>
  </c-bs-nav-item>
  <c-bs-nav-item>
    <c-bs-nav-link as_="button">Link</c-bs-nav-link>
  </c-bs-nav-item>
  <c-bs-nav-item>
    <c-bs-nav-link as_="button" c-disabled="True">Disabled</c-bs-nav-link>
  </c-bs-nav-item>
</c-bs-nav>
```

**Preview:**

--8<-- "snippets/nav_example_12.html"

---

## Custom Attrs

```citry-html
<c-bs-nav c-attrs="{'class': 'custom-nav'}">
  <c-bs-nav-link c-active="True" href="#">Active</c-bs-nav-link>
  <c-bs-nav-link href="#">Link</c-bs-nav-link>
</c-bs-nav>
```

**Preview:**

--8<-- "snippets/nav_example_13.html"

---

## Custom Role

```citry-html
<c-bs-nav role="tablist">
  <c-bs-nav-link c-active="True" href="#">Active</c-bs-nav-link>
  <c-bs-nav-link href="#">Link</c-bs-nav-link>
</c-bs-nav>
```

**Preview:**

--8<-- "snippets/nav_example_14.html"

---
