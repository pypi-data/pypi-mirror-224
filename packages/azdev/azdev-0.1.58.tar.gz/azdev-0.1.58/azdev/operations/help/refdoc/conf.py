#!/usr/bin/env python3
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# -*- coding: utf-8 -*-

# -- General configuration ------------------------------------------------
# For more information on all config options, see http://www.sphinx-doc.org/en/stable/config.html

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

extensions = [
    'azdev.operations.help.refdoc.cli_docs.helpgen',
    'azdev.operations.help.refdoc.extension_docs.helpgen'
]

# The file name extension for the sphinx source files.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'ind'

# General information about the project.
project = 'az'
copyright = '2019, msft'  # pylint: disable=redefined-builtin
author = 'msft'

# The language for content autogenerated by Sphinx
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

pygments_style = 'sphinx'

# Smart quotes is true by default, however the previous doc gen in the extensions repo sets it to false.
# So, the extension doc-generation command overrides this and sets smartquotes to false via sphinx-build's `-D` option
# Doing this makes it to compare the behavior of azdev to existing doc gen scripts. This setting is not necessary.
smartquotes = True
