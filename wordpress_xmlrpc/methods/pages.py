from wordpress_xmlrpc.base import *
from wordpress_xmlrpc.mixins import *
from wordpress_xmlrpc.wordpress import WordPressPage

##
# NOTE: ssteinerX
#
#   These all use the native WordPress xmlrpc stuff which, internally,
# makes sure we're asking for "page" type posts and passes it off to
# the *post() functions.
#
# NOTE: ssteinerX
#       these are in the order that they're 
#       defined in the wp_xmlrpc_server file's methods array
#       to make it easier to cross reference and for no other
#       reason.
##

# NOTE: ssteinerX
#
# class GetRecentPages(AuthenticatedMethod):
#     # NOTE: this doesn't work right, returns posts
#     #       GetPages() in this file gets pages, but I don't
#     #       see the "most recent" filtering working
#     """
#     Retrieve most recent pages from the blog.

#     Parameters:
#         `num_posts`: Number of blog pages to return.

#     Returns: `list` of `WordPressPage` instances.
#     """
#     method_name = 'metaWeblog.getRecentPosts'
#     method_args = ('num_posts',)
#     results_class = WordPressPage



class GetPage(AuthenticatedMethod):
    """
    Retreive an individual blog page.

    Parameters:
        'blog_id': ID of blog from which to get page
        `page_id`: ID of the blog page to retrieve

    Returns: `WordPressPage` instance.

    """
    method_name = 'wp.getPage'
    method_args = ('blog_id', 'page_id',)
    results_class = WordPressPage



class GetPages(AuthenticatedMethod):
    """
    Retrieve most recent pages from the blog.

    Parameters:
        `blog_id`: ID of the blog from which to get pages
        `num_posts`: Number of blog posts to retrieve

    Returns: `list` of `WordPressPage` instances.

    """
    method_name = 'wp.getPages'
    method_args = ('blog_id', 'num_pages',)
    results_class = WordPressPage



class NewPage(AuthenticatedMethod):
    """
    Create a new page on the blog.

    Parameters:
        `content`: A `WordPressPage` instance with at least the `title` and `description` values set.
        `publish`: Boolean indicating whether the blog post should be published upon creation.

    Returns: ID of the newly-created blog page (an integer).

    NOTE: WP API does not currently support blog_id since it
          routes all page creation through the old mw_newPost() 
          internally
    """
    method_name = 'wp.newPage'
    method_args = ('content', 'publish')



class DeletePage(AuthenticatedMethod):
    """
    Delete a blog page.

    Parameters:
        `blog_id`: ID of the blog from which to delete page
        `page_id`: ID of the blog page to delete.

    Returns: `True` on successful deletion.
    """
    method_name = 'wp.deletePage'
    method_args = ('blog_id', 'page_id',)



class EditPage(AuthenticatedMethod):
    """
    Edit an existing blog page.

    Parameters:
        `blog_id`: ID of the blog in which to edit page
        `page_id`: ID of the blog page to edit.
        `content`: A `WordPressPage` instance with the new values for the blog page.
        `publish`: Boolean indicating whether the blog page should be published upon being updated.

    Returns: `True` on successful edit.
    """
    method_name = 'wp.editPage'
    method_args = ('blog_id', 'page_id', 'content', 'publish')



class GetPageList(AuthenticatedMethod):
    """
    Get list of pages in selected blog.

    Parameters:
        `blog_id`: ID of the blog

    Returns: list of pages
    """
    method_name = 'wp.getPageList'
    method_args = ('blog_id',)
    results_class = WordPressPage



class GetPageStatusList(AuthenticatedMethod):
    """
    Retrieve the set of possible blog page statuses (e.g., "draft," "private," "publish").

    Parameters:
        `blog_id`: ID of the blog

    Returns: `dict` of values and their pretty names.

    Example:
        >>> client.call(GetPageStatusList())
        {'draft': 'Draft', 'private': 'Private', 'pending': 'Pending Review', 'publish': 'Published'}

    """
    method_name = 'wp.getPageStatusList'
    method_args = ('blog_id',)



class GetPageTemplates(AuthenticatedMethod):
    """

    """
    method_name = 'wp.getPageTemplates'
    method_args = ('blog_id',)
