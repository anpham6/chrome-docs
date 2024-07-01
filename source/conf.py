# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'E-mc'
copyright = 'squared 2024'
author = 'An Pham'
release = '0.9.4'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.intersphinx']

intersphinx_mapping = {
  'android': ('https://squared.readthedocs.io/en/latest', ('../../android-docs/build/html/objects.inv', None)),
}

templates_path = ['_templates']
exclude_patterns = []

primary_domain = 'js'
highlight_language = 'json'
pygments_style = 'abap'

rst_prolog = """
.. role:: alt(emphasis)
.. role:: target(emphasis)
.. role:: lower(emphasis)
"""

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
  'style_nav_header_background': 'url(https://e-mc.readthedocs.io/en/latest/_static/places/001.png);',
  'navigation_depth': 3,
  'includehidden': False,
}
html_static_path = ['_static']
html_css_files = ['role.css', 'content.css', 'highlight-abap.css', 'override.css']
html_context = {
  'display_github': False,
  'commit': False,
}
html_show_copyright = False