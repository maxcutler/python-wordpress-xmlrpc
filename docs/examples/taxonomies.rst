Working with Taxonomies
=======================

`Taxonomies`__ in WordPress are a means of classifying content. Out of the box, WordPress has two primary taxonomies, categories (``category``) and tags (``post_tag``). Plugins and themes can specify additional custom taxonomies.

__ http://codex.wordpress.org/Taxonomies

Taxonomies
----------

To retrieve a list of taxonomies for a WordPress blog, use :class:`wordpress_xmlrpc.methods.taxonomies.GetTaxonomies`::

	from wordpress_xmlrpc import Client
	from wordpress_xmlrpc.methods import taxonomies

	client = Client(...)
	taxes = client.call(taxonomies.GetTaxonomies())
	# taxes == [WordPressTaxonomy, WordPressTaxonomy, ...]

An individual taxonomy can be retrieved by name::

	category_tax = client.call(taxonomies.GetTaxonomy('category'))

.. note::

	Taxonomies can only be created and modified within WordPress using hooks in plugins or themes. The XML-RPC API permits only reading of taxonomy metadata.

Terms
-----

Terms are the individual entries in a taxonomy. 

For example, to retrieve all blog categories::

	categories = client.call(taxonomies.GetTerms('category'))

And to create a new tag::

	from wordpress_xmlrpc import WordPressTerm

	tag = WordPressTerm()
	tag.taxonomies = 'post_tag'
	tag.name = 'My New Tag'
	tag.id = client.call(taxonomies.NewTerm(tag))

Or to create a child category::

	parent_cat = client.call(taxonomies.GetTerm('category', 3))

	child_cat = WordPressTerm()
	child_cat.taxonomy = 'category'
	child_cat.parent = parent_cat.id
	child_cat.name = 'My Child Category'
	child_cat.id = client.call(taxonomies.NewTerm(child_cat))

Terms and Posts
---------------

Terms are of little use on their own, they must actually be assigned to posts.

If you already have :class:`WordPressTerm` objects, use ``terms`` property of :class:`WordPressPost`::

	tags = client.call(taxonomies.GetTerms('post_tag', {...}))

	post = WordPressPost()
	post.title = 'Post with Tags'
	post.content = '...'
	post.terms = tags
	post.id = client.call(posts.NewPost(post))

If you want to add a category to an existing post::

	category = client.call(taxonomies.GetTerm('category', 3))
	post = client.call(posts.GetPost(5))

	post.terms.append(category)
	client.call(posts.EditPost(post.id, post))

But what if you have not yet retrieved the terms or want to create new terms? For that, you can use the ``terms_names`` property of :class:`WordPressPost`::

	post = WordPressPost()
	post.title = 'Post with new tags'
	post.content = '...'
	post.terms_names = {
		'post_tag': ['tagA', 'another tag'],
		'category': ['My Child Category'],
	}
	post.id = client.call(posts.NewPost(post))

Note that ``terms_names`` is a dictionary with taxonomy names as keys and list of strings as values. WordPress will look for existing terms with these names or else create new ones. Be careful with hierarchical taxonomies like ``category`` because of potential name ambiguities (multiple terms can have the same name if they have different parents); if WordPress detects ambiguity, it will throw an error and ask that you use ``terms`` instead with a proper :class:`WordPressTerm`.

Advanced Querying
-----------------

By Count
~~~~~~~~

To find the 20 most-used tags::

	tags = client.call(taxonomies.GetTerms('post_tag', {'number': 20, 'orderby': 'count', 'order': 'DESC'}))

	for tag in tags:
		print tag.name, tag.count

Searching/Autocomplete
~~~~~~~~~~~~~~~~~~~~~~

To perform case-insensitive searching against term names, use the ``search`` option for ``filter``::

	user_input = 'wor'  # e.g., from UI textbox
	tags = client.call(taxonomies.GetTerms('post_tag', {'search': user_input, 'orderby': 'count', 'number': 5}))

	suggestions = [tag.name for tag in tags]
	# suggestions == ['word', 'WordPress', 'world']