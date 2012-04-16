from wordpress_xmlrpc.base import *
from wordpress_xmlrpc.wordpress import WordPressBlog, WordPressAuthor, WordPressUser


class GetUserInfo(AuthenticatedMethod):
    """
    Retrieve information about the connected user.

    Parameters:
        None

    Returns: instance of :class:`WordPressUser` representing the user whose credentials are being used with the XML-RPC API.
    """
    method_name = 'blogger.getUserInfo'
    results_class = WordPressUser


class GetUsersBlogs(AuthenticatedMethod):
    """
    Retrieve list of blogs that this user belongs to.

    Parameters:
        None

    Returns: `list` of :class:`WordPressBlog` instances.
    """
    method_name = 'wp.getUsersBlogs'
    results_class = WordPressBlog

    def get_args(self, client):
        # strip off first (blog_id) parameter
        return super(GetUsersBlogs, self).get_args(client)[1:]


class GetAuthors(AuthenticatedMethod):
    """
    Retrieve list of authors in the blog.

    Parameters:
        None

    Returns: `list` of :class:`WordPressAuthor` instances.
    """
    method_name = 'wp.getAuthors'
    results_class = WordPressAuthor
