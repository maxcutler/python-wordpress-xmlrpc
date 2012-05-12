Overview
========

Python library to interface with a WordPress blog's `XML-RPC API`__.

__ http://codex.wordpress.org/XML-RPC_Support

An implementation of the standard WordPress API methods is provided,
but the library is designed for easy integration with custom
XML-RPC API methods provided by plugins.

A set of classes are provided that wrap the standard WordPress data
types (e.g., Blog, Post, User). The provided method implementations
return these objects when possible.

This branch of python-wordpress-xmlrpc is tested on trunk of
WordPress 3.4 with the wp-xmlrpc-modernization plugin installed.

Please see docs for more information: http://python-wordpress-xmlrpc.rtfd.org
