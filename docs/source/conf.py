# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'DiaDEM documentation'
copyright = '2023, Nanomatch GmbH'
author = 'Tobias Neumann'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.extlinks',
]

# -- Add additional functionality, e.g. superscripts

from docutils import nodes
from docutils.parsers.rst import roles


def superscript_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    return [nodes.superscript(text, text)], []

roles.register_local_role('sup', superscript_role)


intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
