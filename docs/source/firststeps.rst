First Steps with Sphinx
=======================

Prepare the tutorial demo
-------------------------

You can clone this tutorial and setup Sphinx:

.. code:: bash

   $ git clone https://github.com/cehbrecht/quick-sphinx-tutorial.git

Setup the conda enviroment:

.. code:: bash

   $ cd quick-sphinx-tutorial
   $ conda env create -f environment.yml
   $ source activate giza

Or use pip to install the Sphinx packages:

.. code:: bash

   $ pip install -r requirements.txt

Getting Started
---------------

Create docs folder:

.. code:: bash

   $ mkdir docs
   $ cd docs


Create the sphinx skeleton:

.. code:: bash

   $ sphinx-quickstart

   > Root path for the documentation [.]: 
   > Separate source and build directories (y/n) [n]: y
   > Name prefix for templates and static dir [_]: 
   > Project name: Giza
   > Author name(s): Mac Pingu
   > Project version: 0.1
   > Project release [0.1]:
   > Project language [en]:
   > Source file suffix [.rst]:
   > Name of your master document (without suffix) [index]: 
   > Do you want to use the epub builder (y/n) [n]:
   > autodoc: automatically insert docstrings from modules (y/n) [n]: 
   > doctest: automatically test code snippets in doctest blocks (y/n) [n]: 
   > intersphinx: link between Sphinx documentation of different projects (y/n) [n]: y
   > todo: write "todo" entries that can be shown or hidden on build (y/n) [n]: y
   > coverage: checks for documentation coverage (y/n) [n]: 
   > imgmath: include math, rendered as PNG or SVG images (y/n) [n]: 
   > mathjax: include math, rendered in the browser by MathJax (y/n) [n]: 
   > ifconfig: conditional inclusion of content based on config values (y/n) [n]: 
   > viewcode: include links to the source code of documented Python objects (y/n) [n]: y
   > githubpages: create .nojekyll file to publish the document on GitHub pages (y/n) [n]: y
   > Create Makefile? (y/n) [y]: 
   > Create Windows command file? (y/n) [y]: 

Your file system should now look similar to this::

    mypackage
    ├── src
    └── docs
        ├── Makefile
        ├── make.bat
        ├── _build
        ├── _sources
             ├── conf.py
             ├── index.rst

       
Building docs
-------------

Let's build our docs into HTML to see how it works.
Simply run:

.. code:: bash

    # Inside top-level docs/ directory.
    $ make html

This should run Sphinx in your shell, and output HTML.
At the end, it should say something about the documents being ready in
``_build/html``.
You can now open them in your browser by typing:

.. code:: bash

    $ firefox _build/html/index.html

Custom Theme
------------

You can change the look of the generated documents by setting the ``html_theme`` setting in your ``conf.py``.
Go ahead and set it like this::

    html_theme = 'alabaster'

If you rebuild your documentation,
you will see the new theme:

.. code:: bash

    $ make html

Use the linkchecker
-------------------

Sphinx can check if the links in your document are valid:

.. code:: bash

   $ make linkcheck
