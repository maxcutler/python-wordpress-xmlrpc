from wordpress_xmlrpc.base import *
from wordpress_xmlrpc.mixins import *
from wordpress_xmlrpc.wordpress import WordPressBlog, WordPressAuthor, WordPressUser


class GetUserInfo(BloggerApiMethodMixin, AuthenticatedMethod):
    """
    Retrieve information about the connected user.

    Parameters:
        None

    Returns: instance of `WordPressUser` representing the user whose credentials are being used with the XML-RPC API.
    """
    method_name = 'blogger.getUserInfo'
    requires_blog = False
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
