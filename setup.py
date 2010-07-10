#!/usr/bin/env python
# encoding: utf-8
from distutils.core import setup

try:
    import json
    require = ''
except ImportError:
    require = 'simplejson'

setup(name='uTorrent.Py',
      version='0.1.1',
      description='Mobile Notifications for Transmission Downloads',
      author='Rob Crowther',
      author_email='weilawei@gmail.com',
      url='http://github.com/micahr/uTorrent.Py/',
      packages=['uTorrent'],
      scripts=['bin/ut2il.py'],
      requires=require,
      license='GNU LGPL',
      classifiers = (
                "Development Status :: 3 - Alpha",
		        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
		        "Programming Language :: Python",
		        "Programming Language :: Python :: 2.5",
		        "Programming Language :: Python :: 2.6",
      )
     )