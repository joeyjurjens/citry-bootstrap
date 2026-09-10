# NavDropdown

## Nav Dropdown Basic

```citry-html
<c-bs-nav variant="tabs" as_="ul">
  <c-bs-nav-item>
    <c-bs-nav-link href="#" c-active="True">Active</c-bs-nav-link>
  </c-bs-nav-item>
  <c-bs-nav-dropdown title="Dropdown">
    <c-bs-dropdown-item href="#">Action</c-bs-dropdown-item>
    <c-bs-dropdown-item href="#">Another action</c-bs-dropdown-item>
    <c-bs-dropdown-item href="#">Something else here</c-bs-dropdown-item>
    <c-bs-dropdown-divider />
    <c-bs-dropdown-item href="#">Separated link</c-bs-dropdown-item>
  </c-bs-nav-dropdown>
  <c-bs-nav-item>
    <c-bs-nav-link href="#">Link</c-bs-nav-link>
  </c-bs-nav-item>
</c-bs-nav>
```

**Preview:**

--8<-- "snippets/navdropdown_example_1.html"

---

## Nav Dropdown Disabled

```citry-html
<c-bs-nav as_="ul">
  <c-bs-nav-dropdown title="Disabled Dropdown" c-disabled="True">
    <c-bs-dropdown-item href="#">Action</c-bs-dropdown-item>
  </c-bs-nav-dropdown>
</c-bs-nav>
```

**Preview:**

--8<-- "snippets/navdropdown_example_2.html"

---

## Nav Dropdown Dark

```citry-html
<c-bs-nav as_="ul">
  <c-bs-nav-dropdown title="Dark Dropdown" c-dark="True">
    <c-bs-dropdown-item href="#">Action</c-bs-dropdown-item>
  </c-bs-nav-dropdown>
</c-bs-nav>
```

**Preview:**

--8<-- "snippets/navdropdown_example_3.html"

---
