# Tooltip

## Tooltip Basic

```citry-html
<c-bs-tooltip text="Default tooltip" placement="top">
  <a href="#">inline links</a>
</c-bs-tooltip>
```

**Preview:**

--8<-- "snippets/tooltip_example_1.html"

---

## Tooltip Placement Top

```citry-html
<c-bs-tooltip text="Tooltip on top" placement="top">
  <c-bs-button variant="secondary">Top</c-bs-button>
</c-bs-tooltip>
```

**Preview:**

--8<-- "snippets/tooltip_example_2.html"

---

## Tooltip Placement Right

```citry-html
<c-bs-tooltip text="Tooltip on right" placement="right">
  <c-bs-button variant="secondary">Right</c-bs-button>
</c-bs-tooltip>
```

**Preview:**

--8<-- "snippets/tooltip_example_3.html"

---

## Tooltip Placement Bottom

```citry-html
<c-bs-tooltip text="Tooltip on bottom" placement="bottom">
  <c-bs-button variant="secondary">Bottom</c-bs-button>
</c-bs-tooltip>
```

**Preview:**

--8<-- "snippets/tooltip_example_4.html"

---

## Tooltip Placement Left

```citry-html
<c-bs-tooltip text="Tooltip on left" placement="left">
  <c-bs-button variant="secondary">Left</c-bs-button>
</c-bs-tooltip>
```

**Preview:**

--8<-- "snippets/tooltip_example_5.html"

---

## Tooltip With Button

```citry-html
<c-bs-tooltip text="This top tooltip is themed via CSS variables." placement="top">
  <c-bs-button variant="secondary" c-attrs="{'data-bs-custom-class': 'custom-tooltip'}">Custom tooltip</c-bs-button>
</c-bs-tooltip>
```

**Preview:**

--8<-- "snippets/tooltip_example_6.html"

---

## Tooltip Disabled Button Wrapper

```citry-html
<c-bs-tooltip text="Disabled tooltip" placement="top">
  <span class="d-inline-block" tabindex="0">
    <c-bs-button variant="primary" type="button" c-disabled="True">Disabled button</c-bs-button>
  </span>
</c-bs-tooltip>
```

**Preview:**

--8<-- "snippets/tooltip_example_7.html"

---
