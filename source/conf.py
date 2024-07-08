# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Šest společníků"
copyright = "2023, hanpari"
author = "hanpari"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["myst_parser", "sphinx.ext.autosectionlabel", "sphinx_sitemap"]
autosectionlabel_prefix_document = True

templates_path = ["_templates"]
exclude_patterns = []

language = "cs"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_book_theme"
html_static_path = ["_static"]
html_baseurl = "https://www.sest-spolecniku.cz/"

html_css_files = [
    "css/custom.css",
]


html_title = "Šest společníků"
