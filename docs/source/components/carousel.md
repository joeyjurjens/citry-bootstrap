# Carousel

## Basic With Controls

```citry-html
<c-bs-carousel c-indicators="False">
  <c-bs-carousel-item c-active="True">
    <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide" />
  </c-bs-carousel-item>
  <c-bs-carousel-item>
    <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide" />
  </c-bs-carousel-item>
  <c-bs-carousel-item>
    <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide" />
  </c-bs-carousel-item>
</c-bs-carousel>
```

**Preview:**

--8<-- "snippets/carousel_example_1.html"

---

## With Indicators

```citry-html
<c-bs-carousel>
  <c-bs-carousel-item c-active="True">
    <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide" />
  </c-bs-carousel-item>
  <c-bs-carousel-item>
    <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide" />
  </c-bs-carousel-item>
  <c-bs-carousel-item>
    <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide" />
  </c-bs-carousel-item>
</c-bs-carousel>
```

**Preview:**

--8<-- "snippets/carousel_example_2.html"

---

## With Captions

```citry-html
<c-bs-carousel>
  <c-bs-carousel-item c-active="True">
    <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide" />
    <c-bs-carousel-caption>
      <h5>First slide label</h5>
      <p>Some representative placeholder content for the first slide.</p>
    </c-bs-carousel-caption>
  </c-bs-carousel-item>
  <c-bs-carousel-item>
    <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide" />
    <c-bs-carousel-caption>
      <h5>Second slide label</h5>
      <p>Some representative placeholder content for the second slide.</p>
    </c-bs-carousel-caption>
  </c-bs-carousel-item>
  <c-bs-carousel-item>
    <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide" />
    <c-bs-carousel-caption>
      <h5>Third slide label</h5>
      <p>Some representative placeholder content for the third slide.</p>
    </c-bs-carousel-caption>
  </c-bs-carousel-item>
</c-bs-carousel>
```

**Preview:**

--8<-- "snippets/carousel_example_3.html"

---

## Crossfade

```citry-html
<c-bs-carousel c-fade="True" c-indicators="False">
  <c-bs-carousel-item c-active="True">
    <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide" />
  </c-bs-carousel-item>
  <c-bs-carousel-item>
    <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide" />
  </c-bs-carousel-item>
  <c-bs-carousel-item>
    <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide" />
  </c-bs-carousel-item>
</c-bs-carousel>
```

**Preview:**

--8<-- "snippets/carousel_example_4.html"

---

## Autoplaying Carousel

```citry-html
<c-bs-carousel ride="carousel" c-indicators="False">
  <c-bs-carousel-item c-active="True">
    <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide" />
  </c-bs-carousel-item>
  <c-bs-carousel-item>
    <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide" />
  </c-bs-carousel-item>
  <c-bs-carousel-item>
    <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide" />
  </c-bs-carousel-item>
</c-bs-carousel>
```

**Preview:**

--8<-- "snippets/carousel_example_5.html"

---

## User Initiated Autoplay

```citry-html
<c-bs-carousel ride="true" c-indicators="False">
  <c-bs-carousel-item c-active="True">
    <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide" />
  </c-bs-carousel-item>
  <c-bs-carousel-item>
    <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide" />
  </c-bs-carousel-item>
  <c-bs-carousel-item>
    <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide" />
  </c-bs-carousel-item>
</c-bs-carousel>
```

**Preview:**

--8<-- "snippets/carousel_example_6.html"

---

## Individual Item Intervals

```citry-html
<c-bs-carousel ride="carousel" c-indicators="False">
  <c-bs-carousel-item c-active="True" c-interval="10000">
    <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide" />
  </c-bs-carousel-item>
  <c-bs-carousel-item c-interval="2000">
    <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide" />
  </c-bs-carousel-item>
  <c-bs-carousel-item>
    <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide" />
  </c-bs-carousel-item>
</c-bs-carousel>
```

**Preview:**

--8<-- "snippets/carousel_example_7.html"

---

## Slides Only No Controls

```citry-html
<c-bs-carousel ride="carousel" c-controls="False" c-indicators="False">
  <c-bs-carousel-item c-active="True">
    <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide" />
  </c-bs-carousel-item>
  <c-bs-carousel-item>
    <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide" />
  </c-bs-carousel-item>
  <c-bs-carousel-item>
    <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide" />
  </c-bs-carousel-item>
</c-bs-carousel>
```

**Preview:**

--8<-- "snippets/carousel_example_8.html"

---

## Disabled Touch Swiping

```citry-html
<c-bs-carousel c-touch="False" c-indicators="False">
  <c-bs-carousel-item c-active="True">
    <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide" />
  </c-bs-carousel-item>
  <c-bs-carousel-item>
    <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide" />
  </c-bs-carousel-item>
  <c-bs-carousel-item>
    <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide" />
  </c-bs-carousel-item>
</c-bs-carousel>
```

**Preview:**

--8<-- "snippets/carousel_example_9.html"

---

## Dark Variant

```citry-html
<c-bs-carousel theme="dark">
  <c-bs-carousel-item c-active="True" c-interval="10000">
    <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide" />
    <c-bs-carousel-caption>
      <h5>First slide label</h5>
      <p>Some representative placeholder content for the first slide.</p>
    </c-bs-carousel-caption>
  </c-bs-carousel-item>
  <c-bs-carousel-item c-interval="2000">
    <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide" />
    <c-bs-carousel-caption>
      <h5>Second slide label</h5>
      <p>Some representative placeholder content for the second slide.</p>
    </c-bs-carousel-caption>
  </c-bs-carousel-item>
  <c-bs-carousel-item>
    <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide" />
    <c-bs-carousel-caption>
      <h5>Third slide label</h5>
      <p>Some representative placeholder content for the third slide.</p>
    </c-bs-carousel-caption>
  </c-bs-carousel-item>
</c-bs-carousel>
```

**Preview:**

--8<-- "snippets/carousel_example_10.html"

---
