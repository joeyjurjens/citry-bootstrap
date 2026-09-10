# ButtonGroup

## Basic

```citry-html
<c-bs-button-group>
  <c-bs-button variant="primary">Left</c-bs-button>
  <c-bs-button variant="primary">Middle</c-bs-button>
  <c-bs-button variant="primary">Right</c-bs-button>
</c-bs-button-group>
```

**Preview:**

--8<-- "snippets/buttongroup_example_1.html"

---

## Mixed Styles

```citry-html
<c-bs-button-group>
  <c-bs-button variant="danger">Danger</c-bs-button>
  <c-bs-button variant="warning">Warning</c-bs-button>
  <c-bs-button variant="success">Success</c-bs-button>
</c-bs-button-group>
```

**Preview:**

--8<-- "snippets/buttongroup_example_2.html"

---

## Checkbox Buttons

```citry-html
<c-bs-button-group>
  <c-bs-toggle-button c-attrs="{'id': 'btncheck1'}">Checkbox 1</c-bs-toggle-button>
  <c-bs-toggle-button c-attrs="{'id': 'btncheck2'}">Checkbox 2</c-bs-toggle-button>
  <c-bs-toggle-button c-attrs="{'id': 'btncheck3'}">Checkbox 3</c-bs-toggle-button>
</c-bs-button-group>
```

**Preview:**

--8<-- "snippets/buttongroup_example_3.html"

---

## Radio Buttons

```citry-html
<c-bs-button-group>
  <c-bs-toggle-button type="radio" name="btnradio" c-checked="True" c-attrs="{'id': 'btnradio1'}">Radio 1</c-bs-toggle-button>
  <c-bs-toggle-button type="radio" name="btnradio" c-attrs="{'id': 'btnradio2'}">Radio 2</c-bs-toggle-button>
  <c-bs-toggle-button type="radio" name="btnradio" c-attrs="{'id': 'btnradio3'}">Radio 3</c-bs-toggle-button>
</c-bs-button-group>
```

**Preview:**

--8<-- "snippets/buttongroup_example_4.html"

---

## Large

```citry-html
<c-bs-button-group size="lg">
  <c-bs-button variant="primary" c-outline="True">Left</c-bs-button>
  <c-bs-button variant="primary" c-outline="True">Middle</c-bs-button>
  <c-bs-button variant="primary" c-outline="True">Right</c-bs-button>
</c-bs-button-group>
```

**Preview:**

--8<-- "snippets/buttongroup_example_5.html"

---

## Small

```citry-html
<c-bs-button-group size="sm">
  <c-bs-button variant="primary" c-outline="True">Left</c-bs-button>
  <c-bs-button variant="primary" c-outline="True">Middle</c-bs-button>
  <c-bs-button variant="primary" c-outline="True">Right</c-bs-button>
</c-bs-button-group>
```

**Preview:**

--8<-- "snippets/buttongroup_example_6.html"

---

## Vertical

```citry-html
<c-bs-button-group c-vertical="True">
  <c-bs-button variant="primary">Button</c-bs-button>
  <c-bs-button variant="primary">Button</c-bs-button>
  <c-bs-button variant="primary">Button</c-bs-button>
  <c-bs-button variant="primary">Button</c-bs-button>
</c-bs-button-group>
```

**Preview:**

--8<-- "snippets/buttongroup_example_7.html"

---

## Toolbar Basic

```citry-html
<c-bs-button-toolbar>
  <c-bs-button-group c-attrs="{'class': 'me-2'}">
    <c-bs-button variant="primary">1</c-bs-button>
    <c-bs-button variant="primary">2</c-bs-button>
    <c-bs-button variant="primary">3</c-bs-button>
    <c-bs-button variant="primary">4</c-bs-button>
  </c-bs-button-group>
  <c-bs-button-group c-attrs="{'class': 'me-2'}">
    <c-bs-button variant="secondary">5</c-bs-button>
    <c-bs-button variant="secondary">6</c-bs-button>
    <c-bs-button variant="secondary">7</c-bs-button>
  </c-bs-button-group>
  <c-bs-button-group>
    <c-bs-button variant="info">8</c-bs-button>
  </c-bs-button-group>
</c-bs-button-toolbar>
```

**Preview:**

--8<-- "snippets/buttongroup_example_8.html"

---
