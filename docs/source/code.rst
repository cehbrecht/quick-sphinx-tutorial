.. _code:

Showing Source Code
===================

Using a code block
------------------

Show a Python code block with highlighted lines::

  .. code-block:: python
     :linenos:
     :emphasize-lines: 3,5

     def some_function():
         interesting = False
         print 'This line is highlighted.'
         print 'This one is not...'
         print '...but this one is.'

And this is how it looks like:

.. code-block:: python
     :linenos:
     :emphasize-lines: 3,5

     def some_function():
         interesting = False
         print 'This line is highlighted.'
         print 'This one is not...'
         print '...but this one is.'

Include Source Code
-------------------

Include source code from a file and show only a part of it:

::

   .. literalinclude:: ../../giza/__init__.py
      :language: python
      :linenos:
      :lines: 11-26

And here is how it looks like:

.. literalinclude:: ../../giza/__init__.py
    :language: python
    :linenos: 
    :lines: 11-26


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
