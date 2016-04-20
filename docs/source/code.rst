.. _code:

Reference Python Code
=====================

Using autoapi:

.. code:: bash

   $ pip install sphinx_autoapi

Configure autoapi:

.. code: python

   # Add any Sphinx extension module names here, as strings. They can be
   # extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
   # ones.
   extensions = [
       'autoapi.extension',
       'sphinx.ext.intersphinx',
       'sphinx.ext.todo',
       'sphinx.ext.viewcode',
   ]

   # autoapi configuration
   autoapi_type = 'python'
   autoapi_dirs = ['../../giza']
   autoapi_file_pattern = '*.py'
   autoapi_options = ['members', 'undoc-members', 'private-members']

Play with Sphinx autoapi
------------------------

``sphinx-autoapi`` is a tool that I am helping develop which will make doing API docs easier.
It depends on parsing,
instead of importing code.
This means you don't need to change your PYTHONPATH at all,
and we have a few other different design decisions.

First you need to install autoapi:

.. code:: bash

        pip install sphinx-autoapi

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
