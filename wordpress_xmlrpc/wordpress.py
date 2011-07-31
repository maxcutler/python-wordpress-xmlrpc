import xmlrpclib


class FieldMap(object):
    """
    Container for settings mapping a WordPress XML-RPC request/response struct
    to a Python, programmer-friendly class.
    """

    def __init__(self, inputName, outputNames=None, default=None, conversion=None):
        self.name = inputName
        self.output_names = outputNames or [inputName]
        self.default = default
        self.conversion = conversion


class WordPressBase(object):
    """
    Base class for representing a WordPress object. Handles conversion
    of an XML-RPC response to an object, and construction of a `struct`
    to use in XML-RPC requests.

    Child classes should define a `definition` property that contains
    the list of fields and a `FieldMap` instance to handle conversion
    for XML-RPC calls.
    """

    def __init__(self, xmlrpc=None):
        if self.definition:
            self._def = {}
            for key, value in self.definition.items():
                if isinstance(value, FieldMap):
                    self._def[key] = value
                else:
                    self._def[key] = FieldMap(value)

                fmap = self._def[key]
                if xmlrpc:
                    setattr(self, key, xmlrpc.get(fmap.name, fmap.default))
                elif fmap.default:
                    setattr(self, key, fmap.default)

    @property
    def struct(self):
        data = {}
        for var, fmap in self._def.items():
            if hasattr(self, var):
                for output in fmap.output_names:
                    if fmap.conversion:
                        data[output] = fmap.conversion(getattr(self, var))
                    else:
                        data[output] = getattr(self, var)
        return data

    def __repr__(self):
        return '<%s: %s>' % (self.__class__.__name__, unicode(self).encode('utf-8'))


class WordPressPost(WordPressBase):
    definition = {
        'id': 'postid',
        'user': 'wp_author_id',
        'date_created': FieldMap('dateCreated', conversion=xmlrpclib.DateTime),
        'slug': 'wp_slug',
        'post_status': 'post_status',
        'title': 'title',
        'description': 'description',
        'excerpt': 'mt_excerpt',
        'extended_text': 'mt_text_more',
        'link': 'link',
        'permalink': 'permaLink',
        'allow_comments': FieldMap('mt_allow_comments', conversion=int),
        'allow_pings': FieldMap('mt_allow_pings', conversion=int),
        'tags': 'mt_keywords',
        'categories': 'categories',
        'custom_fields': 'custom_fields',
        'post_type': FieldMap('post_type', default='post'),
        'password': 'wp_password',
        'post_format': 'wp_post_format',
    }

    def __str__(self):
        return self.title


class WordPressPage(WordPressBase):
    definition = {
        'id': 'page_id',
        'user': 'wp_author_id',
        'author': 'wp_author_display_name',
        'date_created': FieldMap('dateCreated', conversion=xmlrpclib.DateTime),
        'slug': 'wp_slug',
        'page_status': 'page_status',
        'title': 'title',
        'description': 'description',
        'excerpt': 'excerpt',
        'extended_text': 'text_more',
        'link': 'link',
        'permalink': 'permaLink',
        'allow_comments': FieldMap('mt_allow_comments', conversion=int),
        'allow_pings': FieldMap('mt_allow_pings', conversion=int),
        'tags': 'mt_keywords',
        'categories': 'categories',
        'custom_fields': 'custom_fields',
        'template': 'wp_page_template',
        'parent_id': FieldMap('wp_page_parent_id', conversion=int),
        'parent_title': 'wp_page_parent_title',
        'order': FieldMap('wp_page_order', conversion=int),
        'password': 'wp_password',
    }

    def __str__(self):
        return self.title


class WordPressComment(WordPressBase):
    definition = {
        'id': 'comment_id',
        'user': 'user_id',
        'post': 'post_id',
        'post_title': 'post_title',
        'parent': 'comment_parent',
        'date_created': FieldMap('dateCreated', conversion=xmlrpclib.DateTime),
        'status': 'status',
        'content': 'content',
        'link': 'link',
        'author': 'author',
        'author_url': 'author_url',
        'author_email': 'author_email',
        'author_ip': 'author_ip',
    }

    def __str__(self):
        return self.content


class WordPressBlog(WordPressBase):
    definition = {
        'id': 'blogid',
        'name': 'blogName',
        'url': 'url',
        'xmlrpc': 'xmlrpc',
        'is_admin': FieldMap('isAdmin', default=False),
    }

    def __str__(self):
        return self.name


class WordPressAuthor(WordPressBase):
    definition = {
        'user_id': 'user_id',
        'user_login': 'user_login',
        'display_name': 'display_name',
    }

    def __str__(self):
        return self.display_name


class WordPressUser(WordPressBase):
    definition = {
        'user_id': 'userid',
        'nickname': 'nickname',
        'url': 'url',
        'first_name': 'firstname',
        'last_name': 'lastname',
    }

    def __str__(self):
        return self.nickname


class WordPressCategory(WordPressBase):
    definition = {
        'cat_id': 'categoryId',
        'parent_id': FieldMap('parentId', ['parentId', 'parent_id']),
        'name': FieldMap('categoryName', ['categoryName', 'name']),
        'description': 'categoryDescription',
        'url': 'htmlUrl',
        'rss': 'rssUrl',
    }

    def __str__(self):
        return self.name


class WordPressTag(WordPressBase):
    definition = {
        'tag_id': 'tag_id',
        'name': 'name',
        'count': 'count',
        'slug': 'slug',
        'url': 'html_url',
        'rss': 'rss_url',
    }

    def __str__(self):
        return self.name


class WordPressMedia(WordPressBase):
    definition = {
        'parent': 'parent',
        'title': 'title',
        'description': 'description',
        'caption': 'caption',
        'date_created': FieldMap('date_created_gmt', conversion=xmlrpclib.DateTime),
        'link': 'link',
        'thumbnail': 'thumbnail',
        'metadata': 'metadata',
    }

    def __str__(self):
        return self.title


class WordPressOption(WordPressBase):
    definition = {
        'name': 'name',
        'description': 'desc',
        'value': 'value',
        'read_only': FieldMap('readonly', default=False),
    }

    def __str__(self):
        return '%s="%s"' % (self.name, self.value)
