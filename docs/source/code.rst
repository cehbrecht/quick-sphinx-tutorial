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
