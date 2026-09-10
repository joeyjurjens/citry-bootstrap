# Progress

## Basic

```citry-html
<c-bs-progress>
  <c-bs-progress-bar c-now="25" />
</c-bs-progress>
```

**Preview:**

--8<-- "snippets/progress_example_1.html"

---

## Basic 0 Percent

```citry-html
<c-bs-progress>
  <c-bs-progress-bar c-now="0" />
</c-bs-progress>
```

**Preview:**

--8<-- "snippets/progress_example_2.html"

---

## Basic 50 Percent

```citry-html
<c-bs-progress>
  <c-bs-progress-bar c-now="50" />
</c-bs-progress>
```

**Preview:**

--8<-- "snippets/progress_example_3.html"

---

## Basic 75 Percent

```citry-html
<c-bs-progress>
  <c-bs-progress-bar c-now="75" />
</c-bs-progress>
```

**Preview:**

--8<-- "snippets/progress_example_4.html"

---

## Basic 100 Percent

```citry-html
<c-bs-progress>
  <c-bs-progress-bar c-now="100" />
</c-bs-progress>
```

**Preview:**

--8<-- "snippets/progress_example_5.html"

---

## Height 1Px

```citry-html
<c-bs-progress height="1px">
  <c-bs-progress-bar c-now="25" />
</c-bs-progress>
```

**Preview:**

--8<-- "snippets/progress_example_6.html"

---

## Height 20Px

```citry-html
<c-bs-progress height="20px">
  <c-bs-progress-bar c-now="25" />
</c-bs-progress>
```

**Preview:**

--8<-- "snippets/progress_example_7.html"

---

## With Label

```citry-html
<c-bs-progress>
  <c-bs-progress-bar c-now="25">25%</c-bs-progress-bar>
</c-bs-progress>
```

**Preview:**

--8<-- "snippets/progress_example_8.html"

---

## Variant Success

```citry-html
<c-bs-progress>
  <c-bs-progress-bar c-now="25" variant="success" />
</c-bs-progress>
```

**Preview:**

--8<-- "snippets/progress_example_9.html"

---

## Variant Info

```citry-html
<c-bs-progress>
  <c-bs-progress-bar c-now="50" variant="info" />
</c-bs-progress>
```

**Preview:**

--8<-- "snippets/progress_example_10.html"

---

## Variant Warning

```citry-html
<c-bs-progress>
  <c-bs-progress-bar c-now="75" variant="warning" />
</c-bs-progress>
```

**Preview:**

--8<-- "snippets/progress_example_11.html"

---

## Variant Danger

```citry-html
<c-bs-progress>
  <c-bs-progress-bar c-now="100" variant="danger" />
</c-bs-progress>
```

**Preview:**

--8<-- "snippets/progress_example_12.html"

---

## Variant Primary

```citry-html
<c-bs-progress>
  <c-bs-progress-bar c-now="30" variant="primary" />
</c-bs-progress>
```

**Preview:**

--8<-- "snippets/progress_example_13.html"

---

## Variant Secondary

```citry-html
<c-bs-progress>
  <c-bs-progress-bar c-now="40" variant="secondary" />
</c-bs-progress>
```

**Preview:**

--8<-- "snippets/progress_example_14.html"

---

## Variant Light

```citry-html
<c-bs-progress>
  <c-bs-progress-bar c-now="60" variant="light" />
</c-bs-progress>
```

**Preview:**

--8<-- "snippets/progress_example_15.html"

---

## Variant Dark

```citry-html
<c-bs-progress>
  <c-bs-progress-bar c-now="80" variant="dark" />
</c-bs-progress>
```

**Preview:**

--8<-- "snippets/progress_example_16.html"

---

## Variant Success With Label

```citry-html
<c-bs-progress>
  <c-bs-progress-bar c-now="25" variant="success">25%</c-bs-progress-bar>
</c-bs-progress>
```

**Preview:**

--8<-- "snippets/progress_example_17.html"

---

## Variant Info With Label

```citry-html
<c-bs-progress>
  <c-bs-progress-bar c-now="50" variant="info">50%</c-bs-progress-bar>
</c-bs-progress>
```

**Preview:**

--8<-- "snippets/progress_example_18.html"

---

## Variant Warning With Label

```citry-html
<c-bs-progress>
  <c-bs-progress-bar c-now="75" variant="warning">75%</c-bs-progress-bar>
</c-bs-progress>
```

**Preview:**

--8<-- "snippets/progress_example_19.html"

---

## Variant Danger With Label

```citry-html
<c-bs-progress>
  <c-bs-progress-bar c-now="100" variant="danger">100%</c-bs-progress-bar>
</c-bs-progress>
```

**Preview:**

--8<-- "snippets/progress_example_20.html"

---

## Multiple Bars

```citry-html
<c-bs-progress-stacked>
  <c-bs-progress c-attrs="{'style': 'width: 15%'}">
    <c-bs-progress-bar c-now="15" />
  </c-bs-progress>
  <c-bs-progress c-attrs="{'style': 'width: 30%'}">
    <c-bs-progress-bar c-now="30" variant="success" />
  </c-bs-progress>
  <c-bs-progress c-attrs="{'style': 'width: 20%'}">
    <c-bs-progress-bar c-now="20" variant="info" />
  </c-bs-progress>
</c-bs-progress-stacked>
```

**Preview:**

--8<-- "snippets/progress_example_21.html"

---

## Striped Basic

```citry-html
<c-bs-progress>
  <c-bs-progress-bar c-now="10" c-striped="True" />
</c-bs-progress>
```

**Preview:**

--8<-- "snippets/progress_example_22.html"

---

## Striped Success

```citry-html
<c-bs-progress>
  <c-bs-progress-bar c-now="25" variant="success" c-striped="True" />
</c-bs-progress>
```

**Preview:**

--8<-- "snippets/progress_example_23.html"

---

## Striped Info

```citry-html
<c-bs-progress>
  <c-bs-progress-bar c-now="50" variant="info" c-striped="True" />
</c-bs-progress>
```

**Preview:**

--8<-- "snippets/progress_example_24.html"

---

## Striped Warning

```citry-html
<c-bs-progress>
  <c-bs-progress-bar c-now="75" variant="warning" c-striped="True" />
</c-bs-progress>
```

**Preview:**

--8<-- "snippets/progress_example_25.html"

---

## Striped Danger

```citry-html
<c-bs-progress>
  <c-bs-progress-bar c-now="100" variant="danger" c-striped="True" />
</c-bs-progress>
```

**Preview:**

--8<-- "snippets/progress_example_26.html"

---

## Striped Primary

```citry-html
<c-bs-progress>
  <c-bs-progress-bar c-now="40" variant="primary" c-striped="True" />
</c-bs-progress>
```

**Preview:**

--8<-- "snippets/progress_example_27.html"

---

## Striped Secondary

```citry-html
<c-bs-progress>
  <c-bs-progress-bar c-now="60" variant="secondary" c-striped="True" />
</c-bs-progress>
```

**Preview:**

--8<-- "snippets/progress_example_28.html"

---

## Striped Light

```citry-html
<c-bs-progress>
  <c-bs-progress-bar c-now="70" variant="light" c-striped="True" />
</c-bs-progress>
```

**Preview:**

--8<-- "snippets/progress_example_29.html"

---

## Striped Dark

```citry-html
<c-bs-progress>
  <c-bs-progress-bar c-now="90" variant="dark" c-striped="True" />
</c-bs-progress>
```

**Preview:**

--8<-- "snippets/progress_example_30.html"

---

## Animated Striped

```citry-html
<c-bs-progress>
  <c-bs-progress-bar c-now="75" c-animated="True" />
</c-bs-progress>
```

**Preview:**

--8<-- "snippets/progress_example_31.html"

---

## Animated Striped Success

```citry-html
<c-bs-progress>
  <c-bs-progress-bar c-now="50" variant="success" c-animated="True" />
</c-bs-progress>
```

**Preview:**

--8<-- "snippets/progress_example_32.html"

---

## Animated Striped Info

```citry-html
<c-bs-progress>
  <c-bs-progress-bar c-now="60" variant="info" c-animated="True" />
</c-bs-progress>
```

**Preview:**

--8<-- "snippets/progress_example_33.html"

---

## Animated Striped Warning

```citry-html
<c-bs-progress>
  <c-bs-progress-bar c-now="80" variant="warning" c-animated="True" />
</c-bs-progress>
```

**Preview:**

--8<-- "snippets/progress_example_34.html"

---

## Animated Striped Danger

```citry-html
<c-bs-progress>
  <c-bs-progress-bar c-now="90" variant="danger" c-animated="True" />
</c-bs-progress>
```

**Preview:**

--8<-- "snippets/progress_example_35.html"

---
