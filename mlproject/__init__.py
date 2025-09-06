"""Compatibility shim: expose the existing `src` package under the
`mlproject` import name so `import mlproject` works for users.

This keeps the current internal code using `src.*` intact while making
the top-level import friendlier.
"""
# Import everything from the actual package located in `src` so external
# code can `import mlproject` while the internal modules remain under `src`.
try:
    from src import *  # type: ignore
except Exception:  # pragma: no cover - fallback to lazy import
    # If direct import fails at package install time, provide a lazy loader.
    import importlib as _importlib

    def __getattr__(name: str):
        pkg = _importlib.import_module('src')
        return getattr(pkg, name)

__all__ = getattr(__import__('src'), '__all__', [])
