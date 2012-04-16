WordPress Objects
=================

WordPressPost
-------------
.. class:: WordPressPost

	Represents a post, page, or other registered custom post type in WordPress.

		* id
		* user
		* date (`datetime`)
		* date_modified (`datetime`)
		* slug
		* post_status
		* title
		* content
		* excerpt
		* link
		* comment_status
		* ping_status
		* terms (`list` of :class:`WordPressTerm`\s)
		* custom_fields (`dict`)
		* enclosure (`dict`)
		* password
		* post_format
		* thumbnail
		* sticky
		* post_type

WordPressPage
~~~~~~~~~~~~~
.. class:: WordPressPage
	
	Derived from :class:`WordPressPost`, represents a WordPress page. Additional fields:

		* template
		* parent_id
		* parent_title
		* order (`int`)
		* post_type = 'page'

WordPressPostType
-----------------
.. class:: WordPressPostType

	Metadata for registered WordPress post type.

		* name
		* label
		* labels (`dict`)
		* cap (`dict`)
		* capability_type
		* description
		* exclude_from_search
		* has_archive
		* hierarchical
		* menu_icon
		* menu_position
		* public
		* publicly_queryable
		* query_var
		* rewrite
		* show_in_menu
		* show_in_nav_menus
		* show_ui
		* taxonomies (`list`)
		* is_builtin
		* supports (`list`)

WordPressTaxonomy
-----------------
.. class:: WordPressTaxonomy

	Metadata for registered WordPress taxonomy.

		* name
		* labels (`dict`)
		* hierarchical
		* public
		* query_var
		* rewrite (`dict`)
		* show_ui
		* show_tagcloud
		* show_in_nav_menus
		* cap (`dict`)
		* is_builtin

WordPressTerm
-------------
.. class:: WordPressTerm

	Represents a term (e.g., tag or category) in a WordPress taxonomy.

		* id
		* group
		* taxonomy
		* taxonomy_id
		* name
		* slug
		* description
		* parent
		* count (`int`)

WordPressBlog
-------------
.. class:: WordPressBlog

	Represents a WordPress blog/site.

		* id
		* name
		* url
		* xmlrpc
		* is_admin (`bool`)

WordPressAuthor
---------------
.. class:: WordPressAuthor

	Minimal representation of a WordPress post author.

		* id
		* user_login
		* display_name

WordPressUser
-------------
.. class:: WordPressUser

	Basic representation of a WordPress user.

		* id
		* nickname
		* url
		* first_name
		* last_name

WordPressComment
----------------
.. class:: WordPressComment

	Represents a WordPress comment.

		* id
		* user
		* post
		* post_title
		* parent
		* date_created (`datetime`)
		* status
		* content
		* link
		* author
		* author_url
		* author_email
		* author_ip

WordPressMedia
--------------
.. class:: WordPressMedia

	Represents a WordPress post media attachment.

		* id
		* parent
		* title
		* description
		* caption
		* date_created (`datetime`)
		* link
		* thumbnail
		* metadata

WordPressOption
---------------
.. class:: WordPressOption

	Represents a WordPress blog setting/option.

		* name
		* description
		* value
		* read_only (`bool`)
