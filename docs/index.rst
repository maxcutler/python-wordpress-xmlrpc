Welcome to python-wordpress-xmlrpc's documentation!
===================================================

Python library to interface with a WordPress blog's `XML-RPC API`__.

__ http://codex.wordpress.org/XML-RPC_Support

An implementation of the standard `WordPress API methods`__ is provided,
but the library is designed for easy integration with custom
XML-RPC API methods provided by plugins.

__ http://codex.wordpress.org/XML-RPC_WordPress_API

A set of :doc:`classes <ref/wordpress>` are provided that wrap the standard WordPress data
types (e.g., Blog, Post, User). The provided :doc:`method implementations <ref/methods>`
return these objects when possible.

.. note::

	In Wordpress 3.5+, the XML-RPC API is enabled by default and cannot be disabled.
	In Wordpress 0.70-3.42, the XML-RPC API is disabled by default. To enable it,
	go to Settings->Writing->Remote Publishing and check the box for XML-RPC.

.. warning::

	python-wordpress-xmlrpc 2.0+ is not fully backwards-compatible with 1.x versions of the library.

Getting Started
---------------
.. toctree::
	:maxdepth: 2

	overview
	examples

Reference
---------
.. toctree::
	:maxdepth: 2

	ref/client
	ref/wordpress
	ref/methods

Internals/Development
---------------------
.. toctree::
	:maxdepth: 2

	dev/changelog
	dev/testing

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
