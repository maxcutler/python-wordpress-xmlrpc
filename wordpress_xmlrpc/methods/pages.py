from wordpress_xmlrpc.base import *
from wordpress_xmlrpc.wordpress import WordPressPage


class GetPage(AuthenticatedMethod):
    """
    Retrieve an individual blog page.

    Parameters:
        `page_id`: ID of the blog page to retrieve.

    Returns: `WordPressPage` instance.
    """
    method_name = 'wp.getPage'
    method_args = ('page_id',)
    results_class = WordPressPage

    def get_args(self, client):
        return (client.blog_id, self.page_id, client.username, client.password)


class GetPages(AuthenticatedMethod):
    """
    Retrieve list of blog pages.

    Parameters:
        `num_pages`: Number of blog pages to return.

    Returns: `list` of `WordPressPage` instances.
    """
    method_name = 'wp.getPages'
    method_args = ('num_pages',)
    results_class = WordPressPage


class NewPage(AuthenticatedMethod):
    """
    Create a new page on the blog.

    Parameters:
        `content`: A `WordPressPage` instance.
        `publish`: Boolean indicating whether the blog page should be published upon creation.

    Returns: ID of the newly-created blog page (an integer).
    """
    method_name = 'wp.newPage'
    method_args = ('content', 'publish')


class EditPage(AuthenticatedMethod):
    """
    Edit an existing blog page.

    Parameters:
        `page_id`: ID of the blog page to edit.
        `content`: A `WordPressPage` instance with the new values for the blog page.
        `publish`: Boolean indicating whether the blog page should be published upon being updated.

    Returns: `True` on successful edit.
    """
    method_name = 'wp.editPage'
    method_args = ('page_id', 'content', 'publish')

    def get_args(self, client):
        return (client.blog_id, self.page_id, client.username, client.password, self.content.struct, self.publish)


class DeletePage(AuthenticatedMethod):
    """
    Delete a blog page.

    Parameters:
        `page_id`: ID of the blog page to delete.

    Returns: `True` on successful deletion.
    """
    method_name = 'wp.deletePage'
    method_args = ('page_id', )


class GetPageStatusList(AuthenticatedMethod):
    """
    Retrieve the set of possible blog page statuses (e.g., "draft," "private," "publish").

    Parameters:
        None

    Returns: `dict` of values and their pretty names.

    Example:
        >>> client.call(GetPageStatusList())
        {'draft': 'Draft', 'private': 'Private', 'publish': 'Published'}
    """
    method_name = 'wp.getPageStatusList'


class GetPageTemplates(AuthenticatedMethod):
    """
    Retrieve the list of blog templates.

    Parameters:
        None

    Returns: `dict` of values and their paths.

    Example:
        >>> client.call(GetPageTemplates())
        {'Default': 'default', 'Sidebar Template': 'sidebar-page.php', 'Showcase Template': 'showcase.php'}
    """
    method_name = 'wp.getPageTemplates'
