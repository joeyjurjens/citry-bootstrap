# Collapse

## Basic

```citry-html
<c-bs-collapse>
  <c-fill name="toggle">
    <c-bs-collapse-toggle c-attrs="{'class': 'btn btn-primary'}">Toggle collapse</c-bs-collapse-toggle>
  </c-fill>
  <c-fill name="default">
    <c-bs-card c-body="True">Some placeholder content for the collapse component. This panel is hidden by default but revealed when the user activates the relevant trigger.</c-bs-card>
  </c-fill>
</c-bs-collapse>
```

**Preview:**

--8<-- "snippets/collapse_example_1.html"

---

## Multiple Targets

```citry-html
<p>
  <c-bs-collapse>
    <c-fill name="toggle">
      <c-bs-collapse-toggle as_="a" c-attrs='{"class": "btn btn-primary"}'>Toggle first element</c-bs-collapse-toggle>
    </c-fill>
    <c-fill name="default">
      <c-bs-card c-body="True">Some placeholder content for the first collapse component.</c-bs-card>
    </c-fill>
  </c-bs-collapse>
  <c-bs-collapse>
    <c-fill name="toggle">
      <c-bs-collapse-toggle c-attrs='{"class": "btn btn-primary"}'>Toggle second element</c-bs-collapse-toggle>
    </c-fill>
    <c-fill name="default">
      <c-bs-card c-body="True">Some placeholder content for the second collapse component.</c-bs-card>
    </c-fill>
  </c-bs-collapse>
</p>
```

**Preview:**

--8<-- "snippets/collapse_example_2.html"

---

## Horizontal

```citry-html
<c-bs-collapse c-horizontal="True">
  <c-fill name="toggle">
    <c-bs-collapse-toggle c-attrs="{'class': 'btn btn-primary'}">Toggle horizontal collapse</c-bs-collapse-toggle>
  </c-fill>
  <c-fill name="default">
    <c-bs-card c-body="True" c-attrs="{'style': 'width: 300px;'}">This is some placeholder content for a horizontal collapse. It's hidden by default and shown when triggered.</c-bs-card>
  </c-fill>
</c-bs-collapse>
```

**Preview:**

--8<-- "snippets/collapse_example_3.html"

---

## With Button Toggle

```citry-html
<c-bs-collapse>
  <c-fill name="toggle">
    <c-bs-collapse-toggle c-attrs='{"class": "btn btn-primary"}'>Button with data-bs-target</c-bs-collapse-toggle>
  </c-fill>
  <c-fill name="default">
    <c-bs-card c-body="True">Some placeholder content for the collapse component. This panel is hidden by default but revealed when the user activates the relevant trigger.</c-bs-card>
  </c-fill>
</c-bs-collapse>
```

**Preview:**

--8<-- "snippets/collapse_example_4.html"

---

## With Link Toggle

```citry-html
<c-bs-collapse>
  <c-fill name="toggle">
    <c-bs-collapse-toggle as_="a" c-attrs='{"class": "btn btn-primary"}'>Link with href</c-bs-collapse-toggle>
  </c-fill>
  <c-fill name="default">
    <c-bs-card c-body="True">Some placeholder content for the collapse component. This panel is hidden by default but revealed when the user activates the relevant trigger.</c-bs-card>
  </c-fill>
</c-bs-collapse>
```

**Preview:**

--8<-- "snippets/collapse_example_5.html"

---
