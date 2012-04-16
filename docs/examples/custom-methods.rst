Custom XML-RPC Methods
======================

See the `WordPress Codex`__ for details on how to write a WordPress plugin that adds
custom XML-RPC method to WordPress.

__ http://codex.wordpress.org/XML-RPC_Extending

The following examples will use the sample methods from that codex page.

Anonymous Methods
-----------------

To use the ``mynamespace.subtractTwoNumbers`` method, create a class derived from :class:`wordpress_xmlrpc.AnonymousMethod`::

	from wordpress_xmlrpc import AnonymousMethod

	class SubtractTwoNumbers(AnonymousMethod):
		method_name = 'mynamespace.subtractTwoNumbers'
		method_args = ('number1', 'number2')

This class can then be used with :meth:`Client.call`::

	from wordpress_xmlrpc import Client

	client = Client('http://www.example.com/xmlrpc.php', 'harrietsmith', 'mypassword')
	difference = client.call(SubtractTwoNumbers(10, 5))
	# difference == 5

Authenticated Methods
---------------------

If your custom authenticated method follows the common ``method(blog_id, username, password, *args)`` structure, then you can use :class:`wordpress_xmlrpc.AuthenticatedMethod`::

	from wordpress_xmlrpc import AuthenticatedMethod

	class GetUserID(AuthenticatedMethod):
		method_name = 'mynamespace.getUserID'

Again, this class can then be used with :meth:`Client.call`::

	user_id = client.call(GetUserID())
	# user_id == 3

Note that you do not have to supply ``blog_id``, ``username``, or ``password`` to the class constructor, since these are automatically added by the `AuthenticatedMethod`. Custom method classes only require arguments specified by ``method_args`` and the optional ``optional_args``.