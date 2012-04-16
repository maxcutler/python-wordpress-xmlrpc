Working with Media
==================

Uploading a File
----------------

The :class:`wordpress_xmlrpc.methods.media.UploadFile` method can be used to upload new files to a WordPress blog::

	from wordpress_xmlrpc import Client, WordPressPost
	from wordpress_xmlrpc.compat import xmlrpc_client
	from wordpress_xmlrpc.methods import media, posts

	client = Client(...)

	# set to the path to your file
	filename = '/path/to/my/picture.jpg'

	# prepare metadata
	data = {
		'name': 'picture.jpg',
		'type': 'image/jpg',  # mimetype
	}

	# read the binary file and let the XMLRPC library encode it into base64
	with open(filename, 'rb') as img:
		data['bits'] = xmlrpc_clent.Binary(img.read())

	response = client.call(media.UploadFile(data))
	# response == {
	# 	'id': 6,
	# 	'file': 'picture.jpg'
	#	'url': 'http://www.example.com/wp-content/uploads/2012/04/16/picture.jpg',
	#	'type': 'image/jpg',
	# }
	attachment_id = response['id']

This newly-uploaded attachment can then be set as the thumbnail for a post::

	post = WordPressPost()
	post.title = 'Picture of the Day'
	post.content = 'What a lovely picture today!'
	post.post_status = 'publish'
	post.post_thumbnail = attachment_id
	post.id = client.call(posts.NewPost(post))

.. note::

	If you do not know the mimetype at development time, you can use the :mod:`mimetypes <python:mimetypes>` library in Python::

		data['type'] = mimetypes.read_mime_types(filename) or mimetypes.guess_type(filename)[0]

Querying
--------

Use :class:`wordpress_xmlrpc.methods.media.GetMediaLibrary` and :class:`wordpress_xmlrpc.methods.media.GetMediaItem` to retrieve information about attachments.