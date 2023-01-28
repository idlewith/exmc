"""Sphinx configuration."""
project = "Excel Markdown Converter"
author = "idlewith"
copyright = "2023, idlewith"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
