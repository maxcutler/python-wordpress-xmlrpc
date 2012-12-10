Working with Posts
==============================

python-wordpress-xmlrpc supports all registered `WordPress post types`__.

__ http://codex.wordpress.org/Post_Types

Behind the scenes in WordPress, all post types are based on a single "post" database table, and all of the functionality is exposed through the `posts methods`__ in the XML-RPC API.

__ http://codex.wordpress.org/XML-RPC_WordPress_API/Posts

For consistency, the same approach is adopted by python-wordpress-xmlrpc.

.. note::

	Posts will be sent as drafts by default. If you want to publish a post, set `post.post_status = 'publish'`.

Normal Posts
------------

First, let's see how to retrieve normal WordPress posts::

	from wordpress_xmlrpc import Client
	from wordpress_xmlrpc.methods import posts

	client = Client(...)
	posts = client.call(posts.GetPosts())
	# posts == [WordPressPost, WordPressPost, ...]

And here's how to create and edit a new post::

	from wordpress_xmlrpc import WordPressPost

	post = WordPressPost()
	post.title = 'My post'
	post.content = 'This is a wonderful blog post about XML-RPC.'
	post.id = client.call(posts.NewPost(post))

	# whoops, I forgot to publish it!
	post.post_status = 'publish'
	client.call(posts.EditPost(post.id, post))

Pages
-----

Out of the box, WordPress supports a post type called "page" for static non-blog pages on a WordPress site. Let's see how to do the same actions for pages::

	from wordpress_xmlrpc import WordPressPage

	pages = client.call(posts.GetPosts({'post_type': 'page'}, results_class=WordPressPage))
	# pages == [WordPressPage, WordPressPage, ...]

Note two important differences:

	1. The ``filter`` parameter's ``post_type`` option is used to limit the query to objects of the desired post type.
	2. The constructor was passd a ``results_class`` keyword argument that told it what class to use to interpret the response values.

And here's how to create and edit a page::

	page = WordPressPage()
	page.title = 'About Me'
	page.content = 'I am an aspiring WordPress and Python developer.'
	page.post_status = 'publish'
	page.id = client.call(posts.NewPost(page))

	# no longer aspiring
	page.content = 'I am a WordPress and Python developer.'
	client.call(posts.EditPost(page))

Custom Post Types
-----------------

While the pages example used its own ``results_class``, that was a unique situation because pages are special in WordPress and have fields directly in the posts table. 

Most custom post types instead use post `custom fields`__ to store their additional information, and custom fields are already exposed on :class:`WordPressPost`.

__ http://codex.wordpress.org/Custom_Fields

For this example, let's assume that your plugin or theme has added an ``acme_product`` custom post type to WordPress:

.. code-block:: python

	# first, let's find some products
	products = client.call(posts.GetPosts({'post_type': 'acme_product', 'number': 100}))

	# calculate the average price of these 100 widgets
	sum = 0
	for product in products:
		# note: product is a WordPressPost object
		for custom_field in product.custom_fields:
			if custom_field['key'] == 'price':
				sum = sum + custom_field['value']
				break
	average = sum / len(products)

	# now let's create a new product
	widget = WordPressPost()
	widget.post_type = 'acme_product'
	widget.title = 'Widget'
	widget.content = 'This is the widget's description.'
	widget.custom_fields = []
	widget.custom_fields.append({
		'key': 'price',
		'value': 2
	})
	widget.id = client.call(posts.NewPost(widget))

Advanced Querying
-----------------

By default, :class:`wordpress_xmlrpc.methods.posts.GetPosts` returns 10 posts in reverse-chronological order (based on their publish date). However, using the ``filter`` parameter, posts can be queried in other ways.

Result Paging
~~~~~~~~~~~~~

If you want to iterate through all posts in a WordPress blog, a server-friendly technique is to use result paging using the ``number`` and ``offset`` options::

	# get pages in batches of 20
	offset = 0
	increment = 20
	while True:
		posts = client.call(posts.GetPosts({'number': increment, 'offset': offset}))
		if len(posts) == 0:
			break  # no more posts returned
		for post in posts:
			do_something(post)
		offset = offset + increment

Ordering
~~~~~~~~

If you don't want posts sorted by ``post_date``, then you can use ``orderby`` and ``order`` options to change that behavior.

For example, in sync scenarios you might want to look for posts by modification date instead of publish date::

	recently_modified = client.call(posts.GetPosts({'orderby': 'post_modified', 'number': 100}))

Or if you want your ACME products sorted alphabetically::

	products = client.call(posts.GetPosts({'post_type': 'acme_product', 'orderby': 'title', 'order': 'ASC'}))

Post Status
~~~~~~~~~~~

Another common scenario is that you only want published posts::

	published_posts = client.call(posts.GetPosts({'post_status': 'publish'}))

Or only draft posts::

	draft_posts = client.call(posts.GetPosts({'post_status': 'draft'}))

You can find the set of valid ``post_status`` by using the :class:`wordpress_xmlrpc.methods.posts.GetPostStatusList` method.
