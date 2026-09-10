# Navbar

## Basic Navbar

```citry-html
<c-bs-navbar expand="lg" c-attrs="{'class': 'bg-body-tertiary'}">
  <c-bs-navbar-brand href="#">Brand</c-bs-navbar-brand>
  <c-bs-navbar-toggler />
  <c-bs-navbar-collapse>
    <c-bs-navbar-nav>
      <c-bs-nav-item>
        <c-bs-nav-link href="#" c-active="True">Home</c-bs-nav-link>
      </c-bs-nav-item>
      <c-bs-nav-item>
        <c-bs-nav-link href="#">Features</c-bs-nav-link>
      </c-bs-nav-item>
      <c-bs-nav-item>
        <c-bs-nav-link href="#">Pricing</c-bs-nav-link>
      </c-bs-nav-item>
      <c-bs-nav-item>
        <c-bs-nav-link href="#" c-disabled="True">Disabled</c-bs-nav-link>
      </c-bs-nav-item>
    </c-bs-navbar-nav>
  </c-bs-navbar-collapse>
</c-bs-navbar>
```

**Preview:**

--8<-- "snippets/navbar_example_1.html"

---

## Navbar Expand Sm

```citry-html
<c-bs-navbar expand="sm" c-attrs="{'class': 'bg-body-tertiary'}">
  <c-bs-navbar-brand href="#">Brand</c-bs-navbar-brand>
</c-bs-navbar>
```

**Preview:**

--8<-- "snippets/navbar_example_2.html"

---

## Navbar Expand Md

```citry-html
<c-bs-navbar expand="md" c-attrs="{'class': 'bg-body-tertiary'}">
  <c-bs-navbar-brand href="#">Brand</c-bs-navbar-brand>
</c-bs-navbar>
```

**Preview:**

--8<-- "snippets/navbar_example_3.html"

---

## Navbar Expand Xl

```citry-html
<c-bs-navbar expand="xl" c-attrs="{'class': 'bg-body-tertiary'}">
  <c-bs-navbar-brand href="#">Brand</c-bs-navbar-brand>
</c-bs-navbar>
```

**Preview:**

--8<-- "snippets/navbar_example_4.html"

---

## Navbar Expand Xxl

```citry-html
<c-bs-navbar expand="xxl" c-attrs="{'class': 'bg-body-tertiary'}">
  <c-bs-navbar-brand href="#">Brand</c-bs-navbar-brand>
</c-bs-navbar>
```

**Preview:**

--8<-- "snippets/navbar_example_5.html"

---

## Navbar With Form

```citry-html
<c-bs-navbar expand="lg" c-attrs="{'class': 'bg-body-tertiary'}">
  <c-bs-navbar-brand href="#">Navbar</c-bs-navbar-brand>
  <form class="d-flex" role="search">
    <c-bs-form-control type="search" placeholder="Search" c-attrs="{'class': 'me-2', 'aria-label': 'Search'}" />
    <c-bs-button variant="success" c-outline="True" type="submit">Search</c-bs-button>
  </form>
</c-bs-navbar>
```

**Preview:**

--8<-- "snippets/navbar_example_6.html"

---

## Navbar Light Background

```citry-html
<c-bs-navbar c-attrs="{'class': 'bg-light'}">
  <c-bs-navbar-brand href="#">Navbar</c-bs-navbar-brand>
</c-bs-navbar>
```

**Preview:**

--8<-- "snippets/navbar_example_7.html"

---

## Navbar Primary Background

```citry-html
<c-bs-navbar c-attrs="{'class': 'bg-primary', 'data-bs-theme': 'dark'}">
  <c-bs-navbar-brand href="#">Navbar</c-bs-navbar-brand>
</c-bs-navbar>
```

**Preview:**

--8<-- "snippets/navbar_example_8.html"

---

## Navbar Container Sm

```citry-html
<c-bs-navbar expand="lg" container="sm" c-attrs="{'class': 'bg-body-tertiary'}">
  <c-bs-navbar-brand href="#">Navbar</c-bs-navbar-brand>
</c-bs-navbar>
```

**Preview:**

--8<-- "snippets/navbar_example_9.html"

---

## Navbar Container Md

```citry-html
<c-bs-navbar expand="lg" container="md" c-attrs="{'class': 'bg-body-tertiary'}">
  <c-bs-navbar-brand href="#">Navbar</c-bs-navbar-brand>
</c-bs-navbar>
```

**Preview:**

--8<-- "snippets/navbar_example_10.html"

---

## Navbar Container Lg

```citry-html
<c-bs-navbar expand="lg" container="lg" c-attrs="{'class': 'bg-body-tertiary'}">
  <c-bs-navbar-brand href="#">Navbar</c-bs-navbar-brand>
</c-bs-navbar>
```

**Preview:**

--8<-- "snippets/navbar_example_11.html"

---

## Navbar Container Xl

```citry-html
<c-bs-navbar expand="lg" container="xl" c-attrs="{'class': 'bg-body-tertiary'}">
  <c-bs-navbar-brand href="#">Navbar</c-bs-navbar-brand>
</c-bs-navbar>
```

**Preview:**

--8<-- "snippets/navbar_example_12.html"

---

## Navbar Container Xxl

```citry-html
<c-bs-navbar expand="lg" container="xxl" c-attrs="{'class': 'bg-body-tertiary'}">
  <c-bs-navbar-brand href="#">Navbar</c-bs-navbar-brand>
</c-bs-navbar>
```

**Preview:**

--8<-- "snippets/navbar_example_13.html"

---

## Navbar Disabled Brand

```citry-html
<c-bs-navbar c-attrs="{'class': 'bg-body-tertiary'}">
  <c-bs-navbar-brand href="#">Disabled Brand</c-bs-navbar-brand>
</c-bs-navbar>
```

**Preview:**

--8<-- "snippets/navbar_example_14.html"

---

## Navbar With Brand Image

```citry-html
<c-bs-navbar expand="lg" c-attrs="{'class': 'bg-body-tertiary'}">
  <c-bs-navbar-brand href="#">
    <img src="/docs/5.3/assets/brand/bootstrap-logo.svg" alt="Bootstrap" width="30" height="24" class="d-inline-block align-text-top" />
    Bootstrap
  </c-bs-navbar-brand>
</c-bs-navbar>
```

**Preview:**

--8<-- "snippets/navbar_example_15.html"

---

## Navbar With Text

```citry-html
<c-bs-navbar c-attrs="{'class': 'bg-body-tertiary'}">
  <c-bs-navbar-brand href="#">Navbar w/ text</c-bs-navbar-brand>
  <c-bs-navbar-text>Navbar text with an inline element</c-bs-navbar-text>
</c-bs-navbar>
```

**Preview:**

--8<-- "snippets/navbar_example_16.html"

---

## Navbar Dark

```citry-html
<c-bs-navbar variant="dark" c-attrs="{'class': 'navbar-dark bg-dark'}">
  <c-bs-navbar-brand href="#">Navbar</c-bs-navbar-brand>
</c-bs-navbar>
```

**Preview:**

--8<-- "snippets/navbar_example_17.html"

---

## Navbar Without Container

```citry-html
<c-bs-navbar expand="lg" c-container="False" c-attrs="{'class': 'bg-body-tertiary'}">
  <c-bs-navbar-brand href="#">Navbar</c-bs-navbar-brand>
</c-bs-navbar>
```

**Preview:**

--8<-- "snippets/navbar_example_18.html"

---
