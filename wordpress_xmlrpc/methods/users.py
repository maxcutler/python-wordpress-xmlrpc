from wordpress_xmlrpc.base import *
from wordpress_xmlrpc.mixins import *
from wordpress_xmlrpc.wordpress import WordPressBlog, WordPressAuthor, WordPressUser


class GetUserInfo(AuthenticatedMethod):
    """
    Retrieve information about the connected user.

    Parameters:
        None

    Returns: instance of `WordPressUser` representing the user whose credentials are being used with the XML-RPC API.
    """
    method_name = 'wp.getUserInfo'
    results_class = WordPressUser


class GetUsersBlogs(AuthenticatedMethod):
    """
    Retrieve list of blogs that this user belongs to.

    Parameters:
        None

    Returns: `list` of `WordPressBlog` instances.
    """
    method_name = 'wp.getUsersBlogs'
    requires_blog = False
    results_class = WordPressBlog


class GetAuthors(AuthenticatedMethod):
    """
    Retrieve list of authors in the blog.

    Parameters:
        None

    Returns: `list` of `WordPressAuthor` instances.
    """
    method_name = 'wp.getAuthors'
    results_class = WordPressAuthor


class GetUsers(AuthenticatedMethod):
    """
    Retrieve list of users in the blog.

    Parameters:
        `filter`: (optional) `dict` of filters to modify the query. Valid keys are 'number', 'offset', and 'role'.
        `fields`: (optional) `list` of fields to return. Specific fields, or groups 'basic' or 'all'.

    Returns: `list` of `WordPressUser` instances.
    """
    method_name = 'wp.getUsers'
    optional_args = ('filter', 'fields')
    results_class = WordPressUser


class GetUser(AuthenticatedMethod):
    """
    Retrieve an individual user.

    Parameters:
        `user_id`: ID of the user
        `fields`: (optional) `list` of fields to return. Specific fields, or groups 'basic' or 'all'.

    Returns: `WordPressUser` instance.
    """
    method_name = 'wp.getUser'
    method_args = ('user_id',)
    optional_args = ('fields',)
    results_class = WordPressUser
