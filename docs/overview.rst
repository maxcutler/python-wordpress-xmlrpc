Overview
========

Installation
------------

1. Verify you meet the following requirements:

	* WordPress 3.4+ **OR** WordPress 3.0-3.3 with the `XML-RPC Modernization Plugin`__.

	__ http://wordpress.org/extend/plugins/xml-rpc-modernization/

	* Python 2.6+ **OR** Python 3.x

2. Install from `PyPI`__ using ``easy_install python-wordpress-xmlrpc`` or ``pip install python-wordpress-xmlrpc``.

__ http://pypi.python.org/pypi/python-wordpress-xmlrpc


Quick Start
-----------

Create an instance of the ``Client`` class with the URL of the
WordPress XML-RPC endpoint and user credentials. Then pass an
``XmlrpcMethod`` object into its ``call`` method to execute the
remote call and return the result.

::

	>>> from wordpress_xmlrpc import Client, WordPressPost
	>>> from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
	>>> from wordpress_xmlrpc.methods.users import GetUserInfo

	# if your site is hosted on wordpress.com, possibly this URL scheme should be https://
	>>> wp = Client('http://mysite.wordpress.com/xmlrpc.php', 'username', 'password')
	>>> wp.call(GetPosts())
	[<WordPressPost: hello-world (id=1)>]

	>>> wp.call(GetUserInfo())
	<WordPressUser: max>

	>>> post = WordPressPost()
	>>> post.title = 'My new title'
	>>> post.content = 'This is the body of my new post.'
	>>> post.terms_names = {
	>>>   'post_tag': ['test', 'firstpost'],
	>>>   'category': ['Introductions', 'Tests']
	>>> }
	>>> wp.call(NewPost(post))
	5

Notice that properties of ``WordPress`` objects are accessed directly,
and not through the ``definition`` attribute defined in the source code.

When a ``WordPress`` object is used as a method parameter, its ``struct``
parameter is automatically extracted for consumption by XML-RPC. However,
if you use an object in a list or other embedded data structure used as
a parameter, be sure to use ``obj.struct`` or else WordPress will not receive
data in the format it expects.

Custom XML-RPC Methods
~~~~~~~~~~~~~~~~~~~~~~

To interface with a non-standard XML-RPC method (such as one added
by a plugin), you must simply extend ``wordpress_xmlrpc.XmlrpcMethod``
or one of its subclasses (``AnonymousMethod`` or ``AuthenticatedMethod``).

The ``XmlrpcMethod`` class provides a number of properties which you
can override to modify the behavior of the method call.

Sample class to call a custom method added by a ficticious plugin::

	from wordpress_xmlrpc import AuthenticatedMethod

	class MyCustomMethod(AuthenticatedMethod):
		method_name = 'custom.MyMethod'
		method_args = ('arg1', 'arg2')

See :doc:`examples/custom-methods` for more details.
