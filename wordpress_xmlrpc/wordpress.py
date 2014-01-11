import sys
from .compat import *
from .fieldmaps import FieldMap, IntegerFieldMap, DateTimeFieldMap, TermsListFieldMap
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
            except Exception:
                e = sys.exc_info()[1]
                raise FieldConversionError(key, e)
            if converted_value is not None:
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
        return '<%s: %s>' % (self.__class__.__name__, str(self).encode('utf-8'))


class WordPressTaxonomy(WordPressBase):
    definition = {
        'name': FieldMap('name', default=''),
        'label': 'label',
        'labels': 'labels',
        'hierarchical': 'hierarchical',
        'public': 'public',
        'show_ui': 'show_ui',
        'cap': 'cap',
        'is_builtin': '_builtin',
        'object_type': 'object_type'
    }

    def __str__(self):
        if hasattr(self, 'name'):
            return self.name
        return unicode('')


class WordPressTerm(WordPressBase):
    definition = {
        'id': 'term_id',
        'group': 'term_group',
        'taxonomy': 'taxonomy',
        'taxonomy_id': 'term_taxonomy_id',
        'name': FieldMap('name', default=''),
        'slug': 'slug',
        'description': 'description',
        'parent': 'parent',
        'count': IntegerFieldMap('count')
    }

    def __str__(self):
        if hasattr(self, 'name'):
            return self.name
        return unicode('')


class WordPressPost(WordPressBase):
    definition = {
        'id': 'post_id',
        'user': 'post_author',
        'date': DateTimeFieldMap('post_date_gmt'),
        'date_modified': DateTimeFieldMap('post_modified_gmt'),
        'slug': 'post_name',
        'post_status': 'post_status',
        'title': FieldMap('post_title', default='Untitled'),
        'content': 'post_content',
        'excerpt': 'post_excerpt',
        'link': 'link',
        'comment_status': 'comment_status',
        'ping_status': 'ping_status',
        'terms': TermsListFieldMap(WordPressTerm, 'terms'),
        'terms_names': 'terms_names',
        'custom_fields': 'custom_fields',
        'enclosure': 'enclosure',
        'password': 'post_password',
        'post_format': 'post_format',
        'thumbnail': 'post_thumbnail',
        'sticky': 'sticky',
        'post_type': FieldMap('post_type', default='post'),
        'parent_id': 'post_parent',
        'menu_order': IntegerFieldMap('menu_order'),
        'guid': 'guid',
        'mime_type': 'post_mime_type',
    }

    def __str__(self):
        if hasattr(self, 'title'):
            return self.title
        return unicode('')


class WordPressPage(WordPressPost):
    definition = dict(WordPressPost.definition, **{
        'template': 'wp_page_template',
        'post_type': FieldMap('post_type', default='page'),
    })


class WordPressComment(WordPressBase):
    definition = {
        'id': 'comment_id',
        'user': 'user_id',
        'post': 'post_id',
        'post_title': 'post_title',
        'parent': 'comment_parent',
        'date_created': DateTimeFieldMap('date_created_gmt'),
        'status': 'status',
        'content': FieldMap('content', default=''),
        'link': 'link',
        'author': 'author',
        'author_url': 'author_url',
        'author_email': 'author_email',
        'author_ip': 'author_ip',
    }

    def __str__(self):
        if hasattr(self, 'content'):
            return self.content
        return unicode('')


class WordPressBlog(WordPressBase):
    definition = {
        'id': 'blogid',
        'name': FieldMap('blogName', default=''),
        'url': 'url',
        'xmlrpc': 'xmlrpc',
        'is_admin': FieldMap('isAdmin', default=False),
    }

    def __str__(self):
        if hasattr(self, 'name'):
            return self.name
        return unicode('')


class WordPressAuthor(WordPressBase):
    definition = {
        'id': 'user_id',
        'user_login': 'user_login',
        'display_name': FieldMap('display_name', default=''),
    }

    def __str__(self):
        if hasattr(self, 'display_name'):
            return self.display_name
        return unicode('')


class WordPressUser(WordPressBase):
    definition = {
        'id': 'user_id',
        'username': 'username',
        'roles': 'roles',
        'nickname': 'nickname',
        'url': 'url',
        'first_name': 'first_name',
        'last_name': 'last_name',
        'registered': DateTimeFieldMap('registered'),
        'bio': 'bio',
        'email': 'email',
        'nicename': 'nicename',
        'display_name': 'display_name',
    }

    def __str__(self):
        if hasattr(self, 'nickname'):
            return self.nickname
        return unicode('')


class WordPressMedia(WordPressBase):
    definition = {
        'id': 'attachment_id',
        'parent': 'parent',
        'title': FieldMap('title', default=''),
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
        return unicode('')


class WordPressOption(WordPressBase):
    definition = {
        'name': FieldMap('name', default=''),
        'description': 'desc',
        'value': FieldMap('value', default=''),
        'read_only': FieldMap('readonly', default=False),
    }

    def __str__(self):
        if hasattr(self, 'name') and hasattr(self, 'value'):
            return '%s="%s"' % (self.name, self.value)
        return unicode('')


class WordPressPostType(WordPressBase):
    definition = {
        'name': 'name',
        'label': FieldMap('label', default=''),
        'labels': 'labels',
        'cap': 'cap',
        'map_meta_cap': 'map_meta_cap',
        'hierarchical': 'hierarchical',
        'menu_icon': 'menu_icon',
        'menu_position': 'menu_position',
        'public': 'public',
        'show_in_menu': 'show_in_menu',
        'taxonomies': 'taxonomies',
        'is_builtin': '_builtin',
        'supports': 'supports',
    }

    def __str__(self):
        if hasattr(self, 'name'):
            return self.name
        return unicode('')
