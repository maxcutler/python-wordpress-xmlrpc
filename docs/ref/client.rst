Client
======

The :class:`Client` class is the gateway to your WordPress blog's XML-RPC interface.

Once initialized with your blog URL and user credentials, the client object is ready
to execute XML-RPC methods against your WordPress blog using its :meth:`Client.call` method.

Client
------
.. class:: Client(url, username, password[, blog_id])

	:param url: URL of the blog's XML-RPC endpoint (e.g., http://www.example.com/xmlrpc.php)
	:param username: Username of a valid user account on the WordPress blog
	:param password: The password for this user account

	.. method:: call(method)

		:param method: :class:`wordpress_xmlrpc.XmlrpcMethod`-derived class

XML-RPC Method Classes
----------------------

.. automodule:: wordpress_xmlrpc

	.. autoclass:: XmlrpcMethod()
		:members:

	.. autoclass:: AnonymousMethod()

	.. autoclass:: AuthenticatedMethod()
