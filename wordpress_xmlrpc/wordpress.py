from .fieldmaps import FieldMap, IntegerFieldMap, DateTimeFieldMap
from wordpress_xmlrpc.exceptions import FieldConversionError


class WordPressBase(object):
    """
    Base class for representing a WordPress object. Handles conversion
    of an XML-RPC response to an object, and construction of a `struct`
    to use in XML-RPC requests.

    Child classes should define a `definition` property that contains
    the list of fields and a `FieldMap` instance to handle conversion
    for XML-RPC calls.
    """
    definition = {}

    def __init__(self, xmlrpc=None):
        # create private variable containing all FieldMaps for the `definition`
        self._def = {}

        for key, value in self.definition.items():
            # if the definition was not a FieldMap, create a simple FieldMap
            if isinstance(value, FieldMap):
                self._def[key] = value
            else:
                self._def[key] = FieldMap(value)

            # convert and store the value on this instance if non-empty
            try:
                converted_value = self._def[key].convert_to_python(xmlrpc)
            except Exception, e:
                raise FieldConversionError(key, e)
            if converted_value:
                setattr(self, key, converted_value)

    @property
    def struct(self):
        """
        XML-RPC-friendly representation of the current object state
        """
        data = {}
        for var, fmap in self._def.items():
            if hasattr(self, var):
                data.update(fmap.get_outputs(getattr(self, var)))
        return data

    def __repr__(self):
        return '<%s: %s>' % (self.__class__.__name__, unicode(self).encode('utf-8'))


class WordPressPost(WordPressBase):
    definition = {
        'id': 'postid',
        'user': 'wp_author_id',
        'date_created': DateTimeFieldMap('dateCreated'),
        'slug': 'wp_slug',
        'post_status': 'post_status',
        'title': 'title',
        'description': 'description',
        'excerpt': 'mt_excerpt',
        'extended_text': 'mt_text_more',
        'link': 'link',
        'permalink': 'permaLink',
        'allow_comments': IntegerFieldMap('mt_allow_comments'),
        'allow_pings': IntegerFieldMap('mt_allow_pings'),
        'tags': 'mt_keywords',
        'categories': 'categories',
        'custom_fields': 'custom_fields',
        'post_type': FieldMap('post_type', default='post'),
        'password': 'wp_password',
        'post_format': 'wp_post_format',
    }

    def __str__(self):
        if hasattr(self, 'title'):
            return self.title
        else:
            return ''


class WordPressPage(WordPressBase):
    definition = {
        'id': 'page_id',
        'user': 'wp_author_id',
        'author': 'wp_author_display_name',
        'date_created': DateTimeFieldMap('dateCreated'),
        'slug': 'wp_slug',
        'page_status': 'page_status',
        'title': 'title',
        'description': 'description',
        'excerpt': 'excerpt',
        'extended_text': 'text_more',
        'link': 'link',
        'permalink': 'permaLink',
        'allow_comments': IntegerFieldMap('mt_allow_comments'),
        'allow_pings': IntegerFieldMap('mt_allow_pings'),
        'tags': 'mt_keywords',
        'categories': 'categories',
        'custom_fields': 'custom_fields',
        'template': 'wp_page_template',
        'parent_id': IntegerFieldMap('wp_page_parent_id'),
        'parent_title': 'wp_page_parent_title',
        'order': IntegerFieldMap('wp_page_order'),
        'password': 'wp_password',
    }

    def __str__(self):
        if hasattr(self, 'title'):
            return self.title
        else:
            return ''

class WordPressComment(WordPressBase):
    definition = {
        'id': 'comment_id',
        'user': 'user_id',
        'post': 'post_id',
        'post_title': 'post_title',
        'parent': 'comment_parent',
        'date_created': DateTimeFieldMap('dateCreated'),
        'status': 'status',
        'content': 'content',
        'link': 'link',
        'author': 'author',
        'author_url': 'author_url',
        'author_email': 'author_email',
        'author_ip': 'author_ip',
    }

    def __str__(self):
        if hasattr(self, 'content'):
            return self.content
        else:
            return ''


class WordPressBlog(WordPressBase):
    definition = {
        'id': 'blogid',
        'name': 'blogName',
        'url': 'url',
        'xmlrpc': 'xmlrpc',
        'is_admin': FieldMap('isAdmin', default=False),
    }

    def __str__(self):
        if hasattr(self, 'name'):
            return self.name
        else:
            return ''


class WordPressAuthor(WordPressBase):
    definition = {
        'user_id': 'user_id',
        'user_login': 'user_login',
        'display_name': 'display_name',
    }

    def __str__(self):
        if hasattr(self, 'display_name'):
            return self.display_name
        else:
            return ''


class WordPressUser(WordPressBase):
    definition = {
        'user_id': 'userid',
        'nickname': 'nickname',
        'url': 'url',
        'first_name': 'firstname',
        'last_name': 'lastname',
    }

    def __str__(self):
        if hasattr(self, 'nickname'):
            return self.nickname
        else:
            return ''


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
        if hasattr(self, 'name'):
            return self.name
        else:
            return ''

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
        if hasattr(self, 'name'):
            return self.name
        else:
            return ''


class WordPressMedia(WordPressBase):
    definition = {
        'parent': 'parent',
        'title': 'title',
        'description': 'description',
        'caption': 'caption',
        'date_created': DateTimeFieldMap('date_created_gmt'),
        'link': 'link',
        'thumbnail': 'thumbnail',
        'metadata': 'metadata',
    }

    def __str__(self):
        if hasattr(self, 'title'):
            return self.title
        else:
            return ''


class WordPressOption(WordPressBase):
    definition = {
        'name': 'name',
        'description': 'desc',
        'value': 'value',
        'read_only': FieldMap('readonly', default=False),
    }

    def __str__(self):
        if hasattr(self, 'name') and hasattr(self, 'value'):
            return '%s="%s"' % (self.name, self.value)
        else:
            return ''
