"""Compatibility shim for legacy mkdocs on Python 3.10+ and newer deps."""

import collections
import collections.abc

for name in ("Sequence", "MutableMapping", "Mapping"):
    if not hasattr(collections, name):
        setattr(collections, name, getattr(collections.abc, name))

try:
    import jinja2

    if not hasattr(jinja2, "contextfilter") and hasattr(jinja2, "pass_context"):
        jinja2.contextfilter = jinja2.pass_context
except Exception:
    pass
