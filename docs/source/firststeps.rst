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


Your file system should now look similar to this::

    mypackage
    ├── src
    └── docs
        ├── conf.py
        ├── Makefile
        ├── make.bat
        ├── _build
        ├── _sources
             ├── index.rst

       
Building docs
-------------

Let's build our docs into HTML to see how it works.
Simply run:

.. code-block:: python

    # Inside top-level docs/ directory.
    make html

This should run Sphinx in your shell, and output HTML.
At the end, it should say something about the documents being ready in
``_build/html``.
You can now open them in your browser by typing::

    open _build/html/index.html

Custom Theme
------------

You'll notice your docs look a bit different than mine.
You can change this by setting the ``html_theme`` setting in your ``conf.py``.
Go ahead and set it like this::

    html_theme = 'sphinx_rtd_theme'

If you rebuild your documentation,
you will see the new theme::

    make html
