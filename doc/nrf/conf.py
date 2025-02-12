#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# nRF Connect SDK documentation build configuration file, created by
# sphinx-quickstart on Mon Jun 11 11:28:40 2018.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import sys
import os

if "ZEPHYR_BASE" not in os.environ:
    sys.exit("$ZEPHYR_BASE environment variable undefined.")
ZEPHYR_BASE = os.path.abspath(os.environ["ZEPHYR_BASE"])

if "ZEPHYR_BUILD" not in os.environ:
    sys.exit("$ZEPHYR_BUILD environment variable undefined.")
ZEPHYR_BUILD = os.path.abspath(os.environ["ZEPHYR_BUILD"])

if "ZEPHYR_OUTPUT" not in os.environ:
    sys.exit("$ZEPHYR_OUTPUT environment variable undefined.")
ZEPHYR_OUTPUT = os.path.abspath(os.environ["ZEPHYR_OUTPUT"])

if "ZEPHYR_RST_SRC" not in os.environ:
    sys.exit("$ZEPHYR_RST_SRC environment variable undefined.")
ZEPHYR_RST_SRC = os.path.abspath(os.environ["ZEPHYR_RST_SRC"])

if "NRF_BASE" not in os.environ:
    sys.exit("$NRF_BASE environment variable undefined.")
NRF_BASE = os.path.abspath(os.environ["NRF_BASE"])

if "NRF_BUILD" not in os.environ:
    sys.exit("$NRF_BUILD environment variable undefined.")
NRF_BUILD = os.path.abspath(os.environ["NRF_BUILD"])

if "NRF_OUTPUT" not in os.environ:
    sys.exit("$NRF_OUTPUT environment variable undefined.")
NRF_OUTPUT = os.path.abspath(os.environ["NRF_OUTPUT"])

if "NRF_RST_SRC" not in os.environ:
    sys.exit("$NRF_RST_SRC environment variable undefined.")
NRF_RST_SRC = os.path.abspath(os.environ["NRF_RST_SRC"])

if "MCUBOOT_OUTPUT" not in os.environ:
    sys.exit("$MCUBOOT_OUTPUT environment variable undefined.")
MCUBOOT_OUTPUT = os.path.abspath(os.environ["MCUBOOT_OUTPUT"])

if "NRFXLIB_OUTPUT" not in os.environ:
    sys.exit("$NRFXLIB_OUTPUT environment variable undefined.")
NRFXLIB_OUTPUT = os.path.abspath(os.environ["NRFXLIB_OUTPUT"])

if "KCONFIG_OUTPUT" not in os.environ:
    sys.exit("$KCONFIG_OUTPUT environment variable undefined.")
KCONFIG_OUTPUT = os.path.abspath(os.environ["KCONFIG_OUTPUT"])

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add the Zephyr 'extensions' directory to sys.path, to enable finding
# Sphinx extensions within.
sys.path.insert(0, os.path.join(ZEPHYR_BASE, 'doc', 'extensions'))

# Let Sphinx find our extensions.
sys.path.append(os.path.join(NRF_BASE, 'scripts', 'sphinx_extensions'))

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.intersphinx',
              'breathe',
              'interbreathe',
              'table_from_rows',
              'options_from_kconfig',
              'ncs_include',
              'sphinx.ext.ifconfig',
              'sphinxcontrib.mscgen',
              'sphinx_tabs.tabs',
              'zephyr.html_redirects']

# Add any paths that contain templates here, relative to this directory.
#templates_path = ['../_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'nRF Connect SDK'
copyright = '2019-2021, Nordic Semiconductor'
author = 'Nordic Semiconductor'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '1.5.1'
# The full version, including alpha/beta/rc tags.
release = '1.5.1'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# Additional lexer for Pygments (syntax highlighting)
from lexer.DtsLexer import DtsLexer
from sphinx.highlighting import lexers
lexers['DTS'] = DtsLexer()

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'nrf'
html_theme_path = ['{}/doc/themes'.format(NRF_BASE)]
html_favicon = '{}/doc/static/images/favicon.ico'.format(NRF_BASE)

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['{}/doc/static'.format(NRF_BASE)]

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'

# If false, no module index is generated.
html_domain_indices = False

# If false, no index is generated.
html_use_index = True

# If true, the index is split into individual pages for each letter.
html_split_index = True

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink =

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = True

# If true, license is shown in the HTML footer. Default is True.
html_show_license = True

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    'zephyr': ('{}'.format(os.path.relpath(ZEPHYR_OUTPUT, NRF_OUTPUT)), os.path.join('{}'.format(os.path.relpath(ZEPHYR_OUTPUT, NRF_RST_SRC)), 'objects.inv')),
    'mcuboot': ('{}'.format(os.path.relpath(MCUBOOT_OUTPUT, NRF_OUTPUT)), os.path.join('{}'.format(os.path.relpath(MCUBOOT_OUTPUT, NRF_RST_SRC)), 'objects.inv')),
    'nrfxlib': ('{}'.format(os.path.relpath(NRFXLIB_OUTPUT, NRF_OUTPUT)), os.path.join('{}'.format(os.path.relpath(NRFXLIB_OUTPUT, NRF_RST_SRC)), 'objects.inv')),
    'kconfig': (os.path.relpath(KCONFIG_OUTPUT, NRF_OUTPUT),
                os.path.join(os.path.relpath(KCONFIG_OUTPUT, NRF_RST_SRC),
                             'objects.inv'))
}

breathe_projects = {
    "nrf": "{}/doxygen/xml".format(NRF_BUILD),
}
breathe_default_project = "nrf"
breathe_domain_by_extension = {
    "h": "c",
    "c": "c",
}
breathe_separate_member_pages = True

ncs_include_mapping = {
    'nrf': '{}'.format(NRF_RST_SRC),
    'zephyr': '{}'.format(ZEPHYR_RST_SRC),
}

# Qualifiers to a function are causing Sphinx/Breathe to warn about
# Error when parsing function declaration and more.  This is a list
# of strings that the parser additionally should accept as
# attributes.
cpp_id_attributes = ['__syscall', '__syscall_inline', '__deprecated',
    '__may_alias', '__used', '__unused', '__weak',
    '__DEPRECATED_MACRO', 'FUNC_NORETURN' ]
c_id_attributes = cpp_id_attributes


# Custom added feature to allow redirecting old URLs (caused by
# reorganizing doc directories)
#
# list of tuples (old_url, new_url) for pages to redirect
#
# URLs must be relative to document root (with NO leading slash),
# and without the html extension)
html_redirect_pages = [
        ('gs_ins_windows', 'gs_installing'),
        ('gs_ins_linux', 'gs_installing'),
        ('gs_ins_mac', 'gs_installing')
                      ]

rst_epilog = """
.. include:: /links.txt
.. include:: /shortcuts.txt
.. include:: /versions.txt
"""

def setup(app):
    app.add_css_file("css/common.css")
    app.add_css_file("css/nrf.css")
    app.add_js_file("js/ncs.js")


# Configuration for checking links

linkcheck_ignore = [r'(\.\.(\\|/))+(zephyr|kconfig|nrfxlib|mcuboot)', # intersphinx links
                    'https://github.com/nrfconnect/nrfxlib', # redirecting and used in release notes
                    'http://localhost:8000/latest/index.html', # link to access local documentation
                    r'https://(www.)?segger.com/downloads/embedded-studio/embeddedstudio_arm_nordic_.+(_x\d+)?', # SES download links
                    'https://portal.azure.com/', # requires login
                    'https://threadgroup.atlassian.net/wiki/spaces/', # requires login
                    'https://google.com:443' # used as example in doxygen
]

linkcheck_anchors_ignore = [r'page=']
