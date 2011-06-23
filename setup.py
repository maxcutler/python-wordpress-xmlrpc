#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='wordpress_xmlrpc',
      version='1.1',
      description='WordPress XML-RPC API Integration Library',
      author='Max Cutler',
      author_email='max@maxcutler.com',
      url='https://github.com/maxcutler/python-wordpress-xmlrpc/',
      packages=['wordpress_xmlrpc', 'wordpress_xmlrpc.methods'],
      license='BSD',
     )