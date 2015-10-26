#!/usr/bin/env python

from distutils.core import setup

setup(name='chemview',
      version='0.3',
      description='Interactive molecular viewer for IPython notebook',
      author='Gabriele Lanaro',
      author_email='gabriele.lanaro@gmail.com',
      url='https://github.com/gabrielelanaro/chemview',
      packages=['chemview', 'chemview.static'],
      package_data={'chemview.static': ['*.js', "*.css"]},
      include_package_data=True
      )
