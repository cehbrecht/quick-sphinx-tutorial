.. _advanced:

Going Further into Sphinx
=========================

Automatic build with travis
---------------------------

.. literalinclude:: ../../.travis.yml
    :language: YAML

Configure theme for rtd
-----------------------

.. code:: bash

   $ pip install sphinx_rtd_theme

Or:

.. code:: bash

   $ conda install sphinx_rtd_theme

.. code:: python

   on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

   if on_rtd:
       html_theme = 'default'
   else:  # only import and set the theme if we're building docs locally
       import sphinx_rtd_theme
       html_theme = 'sphinx_rtd_theme'
       html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

``on_rtd`` is whether we are on readthedocs.org, this line of code grabbed from `docs.readthedocs.org`_

Use Sphinx for GitHub Pages
---------------------------

Include the extension `githubpages`_:

.. code:: python

        extensions = ['sphinx.ext.githubpages']

This extension creates .nojekyll file on generated HTML directory to publish the document on GitHub Pages.

See also: http://gisellezeno.com/tutorials/sphinx-for-python-documentation.html

.. _githubpages: http://www.sphinx-doc.org/en/stable/ext/githubpages.html
.. _docs.readthedocs.org: http://docs.readthedocs.org/en/latest/faq.html?highlight=autodoc#how-do-i-change-behavior-for-read-the-docs








