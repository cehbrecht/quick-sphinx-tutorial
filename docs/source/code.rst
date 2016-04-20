.. _code:

Reference Source Code
=====================

Inline Source code
------------------

Some Python code:

.. code:: python

   import os
   os.path.basename("path/to/sphinx.rst")


Include Source Code
-------------------

.. literalinclude:: ../../giza/__init__.py
    :language: python


Use Sphinx autoapi
------------------

`sphinx-autoapi`_ is a tool to make API docs.
It depends on parsing, instead of importing code.

First you need to install autoapi:

.. code:: bash

        $ pip install sphinx-autoapi

Then add it to your Sphinx project's ``conf.py``:

.. code:: python

        extensions = ['autoapi.extension']

        # Document Python Code
        autoapi_type = 'python'
        autoapi_dir = '../src'

AutoAPI will automatically add itself to the last TOCTree in your top-level ``index.rst``.

This is needed because we will be outputting rst files into the ``autoapi`` directory.
This adds it into the global TOCTree for your project,
so that it appears in the menus.

.. note:: Life Preview of `Giza autoapi <./autoapi/index.html>`_

.. _sphinx-autoapi: http://sphinx-autoapi.readthedocs.org/en/latest/
