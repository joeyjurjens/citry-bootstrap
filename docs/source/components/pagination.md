# Pagination

## Basic

```citry-html
<c-bs-pagination>
  <c-bs-pagination-item href="#">Previous</c-bs-pagination-item>
  <c-bs-pagination-item href="#">1</c-bs-pagination-item>
  <c-bs-pagination-item href="#">2</c-bs-pagination-item>
  <c-bs-pagination-item href="#">3</c-bs-pagination-item>
  <c-bs-pagination-item href="#">Next</c-bs-pagination-item>
</c-bs-pagination>
```

**Preview:**

--8<-- "snippets/pagination_example_1.html"

---

## With Icons

```citry-html
<c-bs-pagination>
  <c-bs-pagination-item href="#" aria_label="Previous">
    <span aria-hidden="true">&laquo;</span>
  </c-bs-pagination-item>
  <c-bs-pagination-item href="#">1</c-bs-pagination-item>
  <c-bs-pagination-item href="#">2</c-bs-pagination-item>
  <c-bs-pagination-item href="#">3</c-bs-pagination-item>
  <c-bs-pagination-item href="#" aria_label="Next">
    <span aria-hidden="true">&raquo;</span>
  </c-bs-pagination-item>
</c-bs-pagination>
```

**Preview:**

--8<-- "snippets/pagination_example_2.html"

---

## Active State

```citry-html
<c-bs-pagination>
  <c-bs-pagination-item href="#">Previous</c-bs-pagination-item>
  <c-bs-pagination-item href="#">1</c-bs-pagination-item>
  <c-bs-pagination-item href="#" c-active="True">2</c-bs-pagination-item>
  <c-bs-pagination-item href="#">3</c-bs-pagination-item>
  <c-bs-pagination-item href="#">Next</c-bs-pagination-item>
</c-bs-pagination>
```

**Preview:**

--8<-- "snippets/pagination_example_3.html"

---

## Disabled State

```citry-html
<c-bs-pagination>
  <c-bs-pagination-item c-disabled="True">Previous</c-bs-pagination-item>
  <c-bs-pagination-item href="#">1</c-bs-pagination-item>
  <c-bs-pagination-item href="#" c-active="True">2</c-bs-pagination-item>
  <c-bs-pagination-item href="#">3</c-bs-pagination-item>
  <c-bs-pagination-item href="#">Next</c-bs-pagination-item>
</c-bs-pagination>
```

**Preview:**

--8<-- "snippets/pagination_example_4.html"

---

## Large Sizing

```citry-html
<c-bs-pagination size="lg">
  <c-bs-pagination-item c-active="True">1</c-bs-pagination-item>
  <c-bs-pagination-item href="#">2</c-bs-pagination-item>
  <c-bs-pagination-item href="#">3</c-bs-pagination-item>
</c-bs-pagination>
```

**Preview:**

--8<-- "snippets/pagination_example_5.html"

---

## Small Sizing

```citry-html
<c-bs-pagination size="sm">
  <c-bs-pagination-item c-active="True">1</c-bs-pagination-item>
  <c-bs-pagination-item href="#">2</c-bs-pagination-item>
  <c-bs-pagination-item href="#">3</c-bs-pagination-item>
</c-bs-pagination>
```

**Preview:**

--8<-- "snippets/pagination_example_6.html"

---

## Centered Alignment

```citry-html
<c-bs-pagination c-ul_attrs="{'class': 'justify-content-center'}">
  <c-bs-pagination-item c-disabled="True">Previous</c-bs-pagination-item>
  <c-bs-pagination-item href="#">1</c-bs-pagination-item>
  <c-bs-pagination-item href="#">2</c-bs-pagination-item>
  <c-bs-pagination-item href="#">3</c-bs-pagination-item>
  <c-bs-pagination-item href="#">Next</c-bs-pagination-item>
</c-bs-pagination>
```

**Preview:**

--8<-- "snippets/pagination_example_7.html"

---

## Right Alignment

```citry-html
<c-bs-pagination c-ul_attrs="{'class': 'justify-content-end'}">
  <c-bs-pagination-item c-disabled="True">Previous</c-bs-pagination-item>
  <c-bs-pagination-item href="#">1</c-bs-pagination-item>
  <c-bs-pagination-item href="#">2</c-bs-pagination-item>
  <c-bs-pagination-item href="#">3</c-bs-pagination-item>
  <c-bs-pagination-item href="#">Next</c-bs-pagination-item>
</c-bs-pagination>
```

**Preview:**

--8<-- "snippets/pagination_example_8.html"

---
