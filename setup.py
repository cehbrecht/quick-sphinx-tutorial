#!/usr/bin/env python

from setuptools import find_packages
from setuptools import setup

long_description = (
    open('README.rst').read() 
)

reqs = [line.strip() for line in open('requirements.txt')]

setup(name             = 'giza',
      version          = '1.0.0',
      description      = 'Demo for Sphinx Tutorial',
      long_description = long_description,
      author	       = 'Carsten Ebhrecht',
      email            = '',
      license          = 'Apache 2.0',
      packages=find_packages(),
      include_package_data=True,
      zip_safe         = False,
      install_requires = reqs,
      entry_points = {
          'console_scripts': [
              'giza=giza:main',
              ]}

      )
