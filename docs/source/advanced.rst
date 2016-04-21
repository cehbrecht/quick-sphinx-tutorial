.. _advanced:

Going Further into Sphinx
=========================

Automatic build with travis
---------------------------

`Travis CI`_ is a continuous integration service used to build and test software projects hosted at GitHub (Wikipedia).

Add a ``.travis.yml`` file to the top level directory of your GitHub
repository with instructions how to build and test your software:

.. literalinclude:: ../../.travis.yml
    :language: YAML
    :linenos:
    :emphasize-lines: 14

Add the instruction to build your Sphinx documentation with the
``linkcheck`` target. The travis build will be run (in a docker
container) each time you push to GitHub. When somethings fails
(install, tests, docs, linkcheck) then travis will inform the person
who made the last commit via eMail.

.. warning::

   See the travis build status for this tutorial: |travis-status|

You can add an image with a link to the status of the travis build to your documenation:

::

   .. image:: https://travis-ci.org/my-orga/my-repo.svg?branch=master
      :target: https://travis-ci.org/my-orga/my-repo
      :alt: Travis Build

.. |travis-status| image:: https://travis-ci.org/cehbrecht/quick-sphinx-tutorial.svg?branch=master
   :target: https://travis-ci.org/cehbrecht/quick-sphinx-tutorial
   :alt: Travis Build
 
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

.. _Travis CI: https://travis-ci.org/
.. _githubpages: http://www.sphinx-doc.org/en/stable/ext/githubpages.html
.. _docs.readthedocs.org: http://docs.readthedocs.org/en/latest/faq.html?highlight=autodoc#how-do-i-change-behavior-for-read-the-docs








