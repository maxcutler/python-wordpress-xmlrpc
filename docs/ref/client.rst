Client
======

The :class:`Client` class is the gateway to your WordPress blog's XML-RPC interface.

Once initialized with your blog URL and user credentials, the client object is ready
to execute XML-RPC methods against your WordPress blog using its :meth:`Client.call` method.

Client
------
.. class:: Client(url, username, password[, blog_id, transport])

	:param url: URL of the blog's XML-RPC endpoint (e.g., http://www.example.com/xmlrpc.php)
	:param username: Username of a valid user account on the WordPress blog
	:param password: The password for this user account
	:param blog_id: The blog's ID (note: WordPress ignores this value, but it is retained for backwards compatibility)
	:param transport: Custom XML-RPC transport implementation. See `Python2`_ or `Python3`_ documentation.

	.. _Python2: https://docs.python.org/2/library/xmlrpclib.html#example-of-client-usage
	.. _Python3: https://docs.python.org/3/library/xmlrpc.client.html#example-of-client-usage

	.. method:: call(method)

		:param method: :class:`wordpress_xmlrpc.XmlrpcMethod`-derived class

XML-RPC Method Classes
----------------------

.. automodule:: wordpress_xmlrpc

	.. autoclass:: XmlrpcMethod()
		:members:

	.. autoclass:: AnonymousMethod()

	.. autoclass:: AuthenticatedMethod()
