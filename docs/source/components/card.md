# Card

## Basic With Image

```citry-html
<c-bs-card>
  <c-bs-card-img src="https://placehold.net/600x400.png" alt="Card image" position="top" />
  <c-bs-card-body>
    <c-bs-card-title>Card title</c-bs-card-title>
    <c-bs-card-text>Some quick example text to build on the card title and make up the bulk of the card's content.</c-bs-card-text>
    <c-bs-button href="#">Go somewhere</c-bs-button>
  </c-bs-card-body>
</c-bs-card>
```

**Preview:**

--8<-- "snippets/card_example_1.html"

---

## With Header And Footer

```citry-html
<c-bs-card text_align="center">
  <c-bs-card-header>Featured</c-bs-card-header>
  <c-bs-card-body>
    <c-bs-card-title>Special title treatment</c-bs-card-title>
    <c-bs-card-text>With supporting text below as a natural lead-in to additional content.</c-bs-card-text>
    <a href="#" class="btn btn-primary" role="button">Go somewhere</a>
  </c-bs-card-body>
  <c-bs-card-footer>2 days ago</c-bs-card-footer>
</c-bs-card>
```

**Preview:**

--8<-- "snippets/card_example_2.html"

---

## With Image Cap

```citry-html
<c-bs-card>
  <c-bs-card-img src="https://placehold.net/600x400.png" alt="Card image" position="top" />
  <c-bs-card-body>
    <c-bs-card-title>Card title</c-bs-card-title>
    <c-bs-card-text>This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</c-bs-card-text>
    <c-bs-card-text>
      <small class="text-body-secondary">Last updated 3 mins ago</small>
    </c-bs-card-text>
  </c-bs-card-body>
</c-bs-card>
```

**Preview:**

--8<-- "snippets/card_example_3.html"

---

## Body Only

```citry-html
<c-bs-card>
  <c-bs-card-body>This is some text within a card body.</c-bs-card-body>
</c-bs-card>
```

**Preview:**

--8<-- "snippets/card_example_4.html"

---

## With Title Subtitle Links

```citry-html
<c-bs-card>
  <c-bs-card-body>
    <c-bs-card-title>Card title</c-bs-card-title>
    <c-bs-card-subtitle>Card subtitle</c-bs-card-subtitle>
    <c-bs-card-text>Some quick example text to build on the card title and make up the bulk of the card's content.</c-bs-card-text>
    <c-bs-card-link href="#">Card link</c-bs-card-link>
    <c-bs-card-link href="#">Another link</c-bs-card-link>
  </c-bs-card-body>
</c-bs-card>
```

**Preview:**

--8<-- "snippets/card_example_5.html"

---

## With Image Bottom

```citry-html
<c-bs-card>
  <c-bs-card-body>
    <c-bs-card-title>Card title</c-bs-card-title>
    <c-bs-card-text>This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</c-bs-card-text>
    <c-bs-card-text>
      <small class="text-body-secondary">Last updated 3 mins ago</small>
    </c-bs-card-text>
  </c-bs-card-body>
  <c-bs-card-img src="https://placehold.net/600x400.png" alt="Card image" position="bottom" />
</c-bs-card>
```

**Preview:**

--8<-- "snippets/card_example_6.html"

---

## Bg Primary

```citry-html
<c-bs-card bg="primary" c-attrs='{"class": "mb-3", "style": "max-width: 18rem;"}'>
  <c-bs-card-header>Header</c-bs-card-header>
  <c-bs-card-body>
    <c-bs-card-title>Primary card title</c-bs-card-title>
    <c-bs-card-text>Some quick example text to build on the card title and make up the bulk of the card's content.</c-bs-card-text>
  </c-bs-card-body>
</c-bs-card>
```

**Preview:**

--8<-- "snippets/card_example_7.html"

---

## Bg Secondary

```citry-html
<c-bs-card bg="secondary" c-attrs='{"class": "mb-3", "style": "max-width: 18rem;"}'>
  <c-bs-card-header>Header</c-bs-card-header>
  <c-bs-card-body>
    <c-bs-card-title>Secondary card title</c-bs-card-title>
    <c-bs-card-text>Some quick example text to build on the card title and make up the bulk of the card's content.</c-bs-card-text>
  </c-bs-card-body>
</c-bs-card>
```

**Preview:**

--8<-- "snippets/card_example_8.html"

---

## Bg Success

```citry-html
<c-bs-card bg="success" c-attrs='{"class": "mb-3", "style": "max-width: 18rem;"}'>
  <c-bs-card-header>Header</c-bs-card-header>
  <c-bs-card-body>
    <c-bs-card-title>Success card title</c-bs-card-title>
    <c-bs-card-text>Some quick example text to build on the card title and make up the bulk of the card's content.</c-bs-card-text>
  </c-bs-card-body>
</c-bs-card>
```

**Preview:**

--8<-- "snippets/card_example_9.html"

---

## Bg Danger

```citry-html
<c-bs-card bg="danger" c-attrs='{"class": "mb-3", "style": "max-width: 18rem;"}'>
  <c-bs-card-header>Header</c-bs-card-header>
  <c-bs-card-body>
    <c-bs-card-title>Danger card title</c-bs-card-title>
    <c-bs-card-text>Some quick example text to build on the card title and make up the bulk of the card's content.</c-bs-card-text>
  </c-bs-card-body>
</c-bs-card>
```

**Preview:**

--8<-- "snippets/card_example_10.html"

---

## Border Primary

```citry-html
<c-bs-card border="primary" c-attrs='{"class": "mb-3", "style": "max-width: 18rem;"}'>
  <c-bs-card-header>Header</c-bs-card-header>
  <c-bs-card-body>
    <c-bs-card-title>Primary card title</c-bs-card-title>
    <c-bs-card-text>Some quick example text to build on the card title and make up the bulk of the card's content.</c-bs-card-text>
  </c-bs-card-body>
</c-bs-card>
```

**Preview:**

--8<-- "snippets/card_example_11.html"

---

## Text Align Center

```citry-html
<c-bs-card text_align="center" c-attrs='{"class": "mb-3", "style": "width: 18rem;"}'>
  <c-bs-card-body>
    <c-bs-card-title>Special title treatment</c-bs-card-title>
    <c-bs-card-text>With supporting text below as a natural lead-in to additional content.</c-bs-card-text>
    <c-bs-button href="#">Go somewhere</c-bs-button>
  </c-bs-card-body>
</c-bs-card>
```

**Preview:**

--8<-- "snippets/card_example_12.html"

---

## Text Align End

```citry-html
<c-bs-card text_align="end">
  <c-bs-card-body>
    <c-bs-card-title>Special title treatment</c-bs-card-title>
    <c-bs-card-text>With supporting text below as a natural lead-in to additional content.</c-bs-card-text>
    <c-bs-button href="#">Go somewhere</c-bs-button>
  </c-bs-card-body>
</c-bs-card>
```

**Preview:**

--8<-- "snippets/card_example_13.html"

---
