# Popover

## Popover Basic

```citry-html
<c-bs-popover title="Popover title" content="And here's some amazing content. It's very engaging. Right?" placement="top">
  <c-bs-button variant="danger" size="lg">Click to toggle popover</c-bs-button>
</c-bs-popover>
```

**Preview:**

--8<-- "snippets/popover_example_1.html"

---

## Popover Placement Top

```citry-html
<c-bs-popover title="Top popover" content="Popover content on top" placement="top">
  <c-bs-button variant="secondary" c-attrs="{'data-bs-container': 'body'}">Popover on top</c-bs-button>
</c-bs-popover>
```

**Preview:**

--8<-- "snippets/popover_example_2.html"

---

## Popover Placement Right

```citry-html
<c-bs-popover title="Right popover" content="Popover content on right" placement="right">
  <c-bs-button variant="secondary" c-attrs="{'data-bs-container': 'body'}">Popover on right</c-bs-button>
</c-bs-popover>
```

**Preview:**

--8<-- "snippets/popover_example_3.html"

---

## Popover Placement Bottom

```citry-html
<c-bs-popover title="Bottom popover" content="Popover content on bottom" placement="bottom">
  <c-bs-button variant="secondary" c-attrs="{'data-bs-container': 'body'}">Popover on bottom</c-bs-button>
</c-bs-popover>
```

**Preview:**

--8<-- "snippets/popover_example_4.html"

---

## Popover Placement Left

```citry-html
<c-bs-popover title="Left popover" content="Popover content on left" placement="left">
  <c-bs-button variant="secondary" c-attrs="{'data-bs-container': 'body'}">Popover on left</c-bs-button>
</c-bs-popover>
```

**Preview:**

--8<-- "snippets/popover_example_5.html"

---

## Popover Custom Styled

```citry-html
<c-bs-popover title="Custom popover" content="This popover is themed via CSS variables." placement="right" c-attrs="{'data-bs-custom-class': 'custom-popover'}">
  <c-bs-button variant="secondary">Custom popover</c-bs-button>
</c-bs-popover>
```

**Preview:**

--8<-- "snippets/popover_example_6.html"

---

## Popover Dismissible

```citry-html
<c-bs-popover title="Dismissible popover" content="And here's some amazing content. It's very engaging. Right?" placement="top" trigger="focus">
  <c-bs-button as_="a" variant="danger" size="lg" c-attrs="{'tabindex': '0'}">Dismissible popover</c-bs-button>
</c-bs-popover>
```

**Preview:**

--8<-- "snippets/popover_example_7.html"

---

## Popover Disabled Button Wrapper

```citry-html
<c-bs-popover title="Disabled popover" content="Popover on disabled button" placement="top" trigger="hover">
  <span class="d-inline-block" tabindex="0">
    <c-bs-button variant="primary" type="button" c-disabled="True">Disabled button</c-bs-button>
  </span>
</c-bs-popover>
```

**Preview:**

--8<-- "snippets/popover_example_8.html"

---
