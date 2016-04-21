.. _rst:

Using reStructuredText
=======================

After using ``sphinx-quickstart`` you have the ``index.rst`` file which contains the content:

.. literalinclude:: index.rst
    :language: rst

You can create other files here for additional documentation. Once you
have created them, then you can include them in the table of contents
in ``index.rst``.


Play with reStructuredText (reST) Syntax
----------------------------------------

`reStructuredText`_ takes a bit of practice. Go over to http://rst.ninjs.org, which is a live preview.

To get started with the reST syntax, you can read the :ref:`rst-primer` in the Sphinx docs.

.. warning:: reST is extended by :ref:`sphinxmarkup` to manage metadata, indexing, and cross-references.

.. note:: The `cheatsheet`_ gives an overview of reST and the Sphinx markup extensions.

.. _cheatsheet:  https://sphinx-tutorial.readthedocs.org/cheatsheet/

Quick reST example
------------------

An example for reStructuredText:

.. literalinclude:: quick-rst.rst
    :language: rst

.. note:: Life Preview: :doc:`quick-rst`
