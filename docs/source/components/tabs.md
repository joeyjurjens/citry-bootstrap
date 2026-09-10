# Tabs

## Basic

```citry-html
<c-bs-tabs>
  <c-bs-tab title="Home">Home content</c-bs-tab>
  <c-bs-tab title="Profile">Profile content</c-bs-tab>
  <c-bs-tab title="Contact">Contact content</c-bs-tab>
</c-bs-tabs>
```

**Preview:**

--8<-- "snippets/tabs_example_1.html"

---

## Pills Variant

```citry-html
<c-bs-tabs variant="pills">
  <c-bs-tab title="Home">Home content</c-bs-tab>
  <c-bs-tab title="Profile">Profile content</c-bs-tab>
</c-bs-tabs>
```

**Preview:**

--8<-- "snippets/tabs_example_2.html"

---

## Underline Variant

```citry-html
<c-bs-tabs variant="underline">
  <c-bs-tab title="Home">Home content</c-bs-tab>
  <c-bs-tab title="Profile">Profile content</c-bs-tab>
</c-bs-tabs>
```

**Preview:**

--8<-- "snippets/tabs_example_3.html"

---

## Tabs With Fill

```citry-html
<c-bs-tabs c-fill="True">
  <c-bs-tab title="Home">Home content</c-bs-tab>
  <c-bs-tab title="Longer title">Profile content</c-bs-tab>
  <c-bs-tab title="Link">Contact content</c-bs-tab>
</c-bs-tabs>
```

**Preview:**

--8<-- "snippets/tabs_example_4.html"

---

## Tabs With Justified

```citry-html
<c-bs-tabs c-justified="True">
  <c-bs-tab title="Home">Home content</c-bs-tab>
  <c-bs-tab title="Profile">Profile content</c-bs-tab>
</c-bs-tabs>
```

**Preview:**

--8<-- "snippets/tabs_example_5.html"

---

## Tabs With Disabled Tab

```citry-html
<c-bs-tabs>
  <c-bs-tab title="Home">Home content</c-bs-tab>
  <c-bs-tab title="Profile">Profile content</c-bs-tab>
  <c-bs-tab title="Disabled" c-disabled="True">Disabled content</c-bs-tab>
</c-bs-tabs>
```

**Preview:**

--8<-- "snippets/tabs_example_6.html"

---

## Manual Composition With Tab Container

```citry-html
<c-bs-tab-container active_key="profile">
  <c-bs-nav variant="tabs" as_="ul" c-attrs="{'role': 'tablist'}">
    <c-bs-nav-item as_="li" c-attrs="{'role': 'presentation'}">
      <c-bs-nav-link as_="button" event_key="home">Home</c-bs-nav-link>
    </c-bs-nav-item>
    <c-bs-nav-item as_="li" c-attrs="{'role': 'presentation'}">
      <c-bs-nav-link as_="button" event_key="profile">Profile</c-bs-nav-link>
    </c-bs-nav-item>
  </c-bs-nav>
  <c-bs-tab-content>
    <c-bs-tab-pane event_key="home">Home content</c-bs-tab-pane>
    <c-bs-tab-pane event_key="profile">Profile content</c-bs-tab-pane>
  </c-bs-tab-content>
</c-bs-tab-container>
```

**Preview:**

--8<-- "snippets/tabs_example_7.html"

---

## Manual Composition With Disabled Tab

```citry-html
<c-bs-tab-container active_key="home">
  <c-bs-nav variant="tabs" as_="ul" c-attrs="{'role': 'tablist'}">
    <c-bs-nav-item as_="li" c-attrs="{'role': 'presentation'}">
      <c-bs-nav-link as_="button" event_key="home">Home</c-bs-nav-link>
    </c-bs-nav-item>
    <c-bs-nav-item as_="li" c-attrs="{'role': 'presentation'}">
      <c-bs-nav-link as_="button" event_key="settings" c-disabled="True">Settings</c-bs-nav-link>
    </c-bs-nav-item>
  </c-bs-nav>
  <c-bs-tab-content>
    <c-bs-tab-pane event_key="home">Home content</c-bs-tab-pane>
    <c-bs-tab-pane event_key="settings">Settings content</c-bs-tab-pane>
  </c-bs-tab-content>
</c-bs-tab-container>
```

**Preview:**

--8<-- "snippets/tabs_example_8.html"

---

## Tabs With Active Tab

```citry-html
<c-bs-tabs>
  <c-bs-tab title="Home">Home content</c-bs-tab>
  <c-bs-tab title="Profile" c-active="True">Profile content</c-bs-tab>
  <c-bs-tab title="Contact">Contact content</c-bs-tab>
</c-bs-tabs>
```

**Preview:**

--8<-- "snippets/tabs_example_9.html"

---
