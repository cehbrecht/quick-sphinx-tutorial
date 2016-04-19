.. _advanced:

Further Topics ...
==================

use linkchecker
---------------

.. code:: bash

   $ make linkcheck

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

   # on_rtd is whether we are on readthedocs.org, this line of code grabbed from docs.readthedocs.org
   # http://docs.readthedocs.org/en/latest/faq.html?highlight=autodoc#how-do-i-change-behavior-for-read-the-docs
   on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

   if on_rtd:
       html_theme = 'default'
   else:  # only import and set the theme if we're building docs locally
       import sphinx_rtd_theme
       html_theme = 'sphinx_rtd_theme'
       html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

Use Sphinx for GitHub Pages
---------------------------








