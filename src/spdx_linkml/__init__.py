"""spdx_linkml.

System Package Data Exchange (SPDX): LinkML Schema
"""

try:
    from spdx_linkml._version import __version__, __version_tuple__
except ImportError:  # pragma: no cover
    __version__ = "0.0.0"
    __version_tuple__ = (0, 0, 0)
