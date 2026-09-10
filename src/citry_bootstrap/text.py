"""The one Django utility the components needed.

`Tabs` derives element ids from a tab's title. The django-components version
imported `django.utils.text.slugify` for it; a citry library carries no
framework, so it lives here instead. Same behaviour, same output.
"""

import re
import unicodedata


def slugify(value: object, allow_unicode: bool = False) -> str:
    """Lowercase, strip accents and punctuation, and join words with hyphens."""
    text = str(value)
    if allow_unicode:
        text = unicodedata.normalize("NFKC", text)
    else:
        text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = re.sub(r"[^\w\s-]", "", text.lower())
    return re.sub(r"[-\s]+", "-", text).strip("-_")
