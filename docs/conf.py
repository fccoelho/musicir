"""Sphinx configuration."""
from datetime import datetime


project = "Music Information Retrieval"
author = "Flávio Codeço Coelho"
copyright = f"{datetime.now().year}, {author}"
extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_nb",
]
autodoc_typehints = "description"
html_theme = "furo"
