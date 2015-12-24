Methods
=======

See :doc:`/examples` for guidance on how to use the following method classes.

methods.posts
-------------

.. automodule:: wordpress_xmlrpc.methods.posts

	.. autoclass:: GetPosts([filter, fields])
	.. autoclass:: GetPost(post_id[, fields])
	.. autoclass:: NewPost(content)
	.. autoclass:: EditPost(post_id, content)
	.. autoclass:: DeletePost(post_id)
	.. autoclass:: GetPostStatusList()
	.. autoclass:: GetPostFormats()
	.. autoclass:: GetPostTypes()
	.. autoclass:: GetPostType(post_type)

methods.pages
-------------

.. automodule:: wordpress_xmlrpc.methods.pages
	
	.. autoclass:: GetPageStatusList()
	.. autoclass:: GetPageTemplates()

methods.taxonomies
------------------

.. automodule:: wordpress_xmlrpc.methods.taxonomies
	
	.. autoclass:: GetTaxonomies()
	.. autoclass:: GetTaxonomy(taxonomy)
	.. autoclass:: GetTerms(taxonomy[, filter])
	.. autoclass:: GetTerm(taxonomy, term_id)
	.. autoclass:: NewTerm(term)
	.. autoclass:: EditTerm(term_id, term)
	.. autoclass:: DeleteTerm(taxonomy, term_id)

methods.comments
----------------

.. automodule:: wordpress_xmlrpc.methods.comments
	
	.. autoclass:: GetComments(filter)
	.. autoclass:: GetComment(comment_id)
	.. autoclass:: NewComment(post_id, comment)
	.. autoclass:: NewAnonymousComment(post_id, comment)
	.. autoclass:: EditComment(comment_id, comment)
	.. autoclass:: DeleteComment(comment_id)
	.. autoclass:: GetCommentStatusList()
	.. autoclass:: GetCommentCount(post_id)

methods.users
-------------

.. automodule:: wordpress_xmlrpc.methods.users

	.. autoclass:: GetUser(user_id[, fields])
	.. autoclass:: GetUsers([filter, fields])
	.. autoclass:: GetProfile()
	.. autoclass:: EditProfile(user)
	.. autoclass:: GetUsersBlogs()
	.. autoclass:: GetAuthors()

methods.media
-------------

.. automodule:: wordpress_xmlrpc.methods.media
	
	.. autoclass:: GetMediaLibrary([filter])
	.. autoclass:: GetMediaItem(attachmend_id)
	.. autoclass:: UploadFile(data)

methods.options
---------------

.. automodule:: wordpress_xmlrpc.methods.options
	
	.. autoclass:: GetOptions(options)
	.. autoclass:: SetOptions(options)

methods.demo
------------

.. automodule:: wordpress_xmlrpc.methods.demo

	.. autoclass:: SayHello()
	.. autoclass:: AddTwoNumbers(number1, number2)
