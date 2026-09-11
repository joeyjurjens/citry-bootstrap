import re
from html import unescape

import pytest
from citry import Citry

import citry_bootstrap

_CID = re.compile(r'\s*data-cid-[\w-]+="[^"]*"')
_CLASS = re.compile(r'class="([^"]*)"')
_TAG = re.compile(r"""<(\w[\w.-]*)((?:\s+[^\s=/>]+(?:=(?:"[^"]*"|'[^']*'|[^\s>]+))?)*)\s*(/?)>""")
_ATTR = re.compile(r"""\s*([^\s=/>]+)(=(?:"[^"]*"|'[^']*'|[^\s>]+))?""")
# the expected HTML was written against mocked ids
_MOCK_ID = re.compile(r"\bctest\d+\b")
_CID_VALUE = re.compile(r"data-cid-(\w+)")


@pytest.fixture(scope="session")
def app():
    engine = Citry(autodiscover=False, extensions=[citry_bootstrap.PlainInputs])
    citry_bootstrap.install(engine)
    return engine


@pytest.fixture
def render(app):
    def _render(source, **variables):
        return app.render_template(source, variables).serialize()

    return _render


def normalize(html, ids=None):
    """Drop what cannot match across engines, and what carries no meaning.

    Component ids differ per engine. Attribute order, CSS class order and a
    trailing style semicolon are all formatting.
    """
    # a component id that reached the output through self.id cannot match across
    # engines. Take the real ones from the data-cid attributes rather than
    # guessing by shape, since a word like `current` looks just like an id.
    ids = set(_CID_VALUE.findall(html)) if ids is None else ids
    html = _CID.sub("", html)
    for real in ids:
        html = html.replace(real, "<id>")
    # the engines differ in how aggressively they escape; the character is what counts
    html = unescape(html)
    html = _MOCK_ID.sub("<id>", html)
    html = _CLASS.sub(lambda m: 'class="' + " ".join(sorted(m.group(1).split())) + '"', html)
    html = re.sub(r'style="([^"]*?);?"', lambda m: f'style="{m.group(1)}"', html)

    def sort_attrs(m):
        pairs = sorted(
            f"{a.group(1)}{a.group(2) or ''}" for a in _ATTR.finditer(m.group(2)) if a.group(1)
        )
        return f"<{m.group(1)}{(' ' + ' '.join(pairs)) if pairs else ''}>"

    html = _TAG.sub(sort_attrs, html)
    html = re.sub(r"\s+", " ", html)
    # Django's assertHTMLEqual, which these expectations were written against,
    # ignores whitespace next to a tag
    html = re.sub(r">\s+", ">", html)
    return re.sub(r"\s+<", "<", html).strip()


@pytest.fixture
def assert_contains():
    """Substring check against normalized HTML, so a component id cannot break it."""

    def _assert(rendered, fragment):
        got, want = normalize(rendered), normalize(fragment)
        assert want in got, f"\n     got: {got}\nwant in it: {want}"

    return _assert


@pytest.fixture
def assert_html():
    def _assert(rendered, expected):
        # A test that reads an id out of the output and puts it in its
        # expectation is already consistent; blanking it on one side only
        # would break that, so both sides lose the same ids.
        ids = set(_CID_VALUE.findall(rendered))
        got, want = normalize(rendered, ids), normalize(expected, ids)
        assert got == want, f"\n got: {got}\nwant: {want}"

    return _assert
