Overview
==========

Python library to interface with a WordPress blog's [XML-RPC API](http://codex.wordpress.org/XML-RPC_Support).

An implementation of the standard WordPress API methods is provided,
but the library is designed for easy integration with custom
XML-RPC API methods provided by plugins.

A set of classes are provided that wrap the standard WordPress data
types (e.g., Blog, Post, User). The provided method implementations
return these objects when possible.

NOTE: The XML-RPC API is disabled in WordPress by default. To enable,
go to Settings->Writing->Remote Publishing and check the box for
XML-RPC.

This library was developed against and tested on WordPress 3.0.
This library is only compatible with Python 2.x.

Usage
==========

Create an instance of the `Client` class with the URL of the
WordPress XML-RPC endpoint and user credentials. Then pass an
`XmlrpcMethod` object into its `call` method to execute the
remote call and return the result.

	>>> from wordpress_xmlrpc import Client, WordPressPost
	>>> from wordpress_xmlrpc.methods.posts import GetRecentPosts, NewPost
	>>> from wordpress_xmlrpc.methods.users import GetUserInfo

	>>> wp = Client('http://mysite.wordpress.com/xmlrpc.php', 'username', 'password')
	>>> wp.call(GetRecentPosts(10))
	[<WordPressPost: hello-world (id=1)>]

	>>> wp.call(GetUserInfo())
	<WordPressUser: max>

	>>> post = WordPressPost()
	>>> post.title = 'My new title'
	>>> post.description = 'This is the body of my new post.'
	>>> post.tags = 'test, firstpost'
	>>> post.categories = ['Introductions', 'Tests']
	>>> wp.call(NewPost(post, True))
	5

Notice that properties of `WordPress` objects are accessed directly,
and not through the `definition` attribute defined in the source code.

When a `WordPress` object is used as a method parameter, its `struct`
parameter is automatically extracted for consumption by XML-RPC. However,
if you use an object in a list of other embedded data structure used as
a parameter, be sure to use `obj.struct` or else WordPress will not receive
data in the format it expects.

	>>> from wordpress_xmlrpc import Client, WordPressCategory
	>>> from wordpress_xmlrpc.categories import NewCategory, SetPostCategories

	>>> wp = Client('http://mysite.wordpress.com/xmlrpc.php', 'username', 'password')
	>>> new_category = WordPressCategory()
	>>> new_category.name = 'My new category'
	>>> new_category.cat_id = wp.call(NewCategory(new_category))

	>>> another_category = WordPressCategory()
	>>> another_category.name = 'Another new category'
	>>> another_category.cat_id = wp.call(NewCategory(another_category))

	>>> wp.call(SetPostCategories(5, [new_category.struct, another_category.struct]))
	True

Custom XML-RPC Methods
==========

To interface with a non-standard XML-RPC method (such as one added
by a plugin), you must simply extend `wordpress_xmlrpc.XmlrpcMethod`
or one of its subclasses (`AnonymousMethod` or `AuthenticatedMethod`).

The `XmlrpcMethod` class provides a number of properties which you
can override to modify the behavior of the method call.

Sample class to call a custom method added by a ficticious plugin:

	from wordpress_xmlrpc import AuthenticatedMethod

	class MyCustomMethod(AuthenticatedMethod):
		method_name = 'custom.MyMethod'
		method_args = ('arg1', 'arg2')

See `base.py` for more details.

Reference
==========

WordPress Classes
----------

See `wordpress.py` for full details.

Available classes:

* WordPressPost
* WordPressBlog
* WordPressAuthor
* WordPressUser
* WordPressCategory
* WordPressComment
* WordPressTag
* WordPressOption

XML-RPC Methods
----------

See files in the `methods` folder for details on exact
method parameters and return values.

### methods.posts

* GetRecentPosts(num_posts)
* GetPost(post_id)
* NewPost(content, publish)
* EditPost(post_id, content, publish)
* DeletePost(post_id)
* GetPostStatusList()
* PublishPost(post_id)
* UploadFile(data)

### methods.categories

* GetCategories()
* NewCategory(category)
* DeleteCategory(category_id)
* SuggestCategories(category, max_results)
* GetPostCategories(post_id)
* SetPostCategories(post_id, categories)
* GetTags()

### methods.comments

* GetComment(comment_id)
* NewComment(post_id, comment_id)
* EditComment(comment_id, comment)
* DeleteComment(comment_id)

### methods.users

* GetUserInfo()
* GetUsersBlogs()
* GetAuthors()

### methods.options

* GetOptions(options)
* SetOptions(options)

### methods.demo

* SayHello()
* AddTwoNumbers(number1, number2)

### To Be Implemented

* methods.pages
* methods.pingbacks