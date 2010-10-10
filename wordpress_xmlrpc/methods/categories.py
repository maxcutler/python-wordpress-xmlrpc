from wordpress_xmlrpc.base import *
from wordpress_xmlrpc.mixins import *
from wordpress_xmlrpc.wordpress import WordPressCategory, WordPressTag


class GetCategories(AuthenticatedMethod):
    """
    Retrieve the list of available categories for the blog.

    Parameters:
        None

    Returns: `list` of `WordPressCategory` instances.
    """
    method_name = 'wp.getCategories'
    results_class = WordPressCategory


class NewCategory(AuthenticatedMethod):
    """
    Create new category.

    Parameters:
        `category`: instance of `WordPressCategory`

    Returns: ID of newly-created category (an integer).
    """
    method_name = 'wp.newCategory'
    method_args = ('category',)


class DeleteCategory(AuthenticatedMethod):
    """
    Delete a category.

    Parameters:
        `category_id`: ID of the category to delete.

    Returns: Mixed. See: http://codex.wordpress.org/Function_Reference/wp_delete_category
    """
    method_name = 'wp.deleteCategory'
    method_args = ('category_id',)


class SuggestCategories(AuthenticatedMethod):
    """
    Retrieve list of categories that are similar to a string.

    Parameters:
        `category`: string name to check against
        `max_results`: the maximum number of categories to return

    Returns: `list` of `dict`s with keys: `category_id` and `category_name`
    """
    method_name = 'wp.suggestCategories'
    method_args = ('category', 'max_results')


class GetPostCategories(AuthParamsOffsetMixin, AuthenticatedMethod):
    """
    Retrieve list of categories assigned to a blog post.

    Parameters:
        `post_id`: ID of the blog post

    Returns: `list` of `WordPressCategory` instances.
    """
    method_name = 'mt.getPostCategories'
    method_args = ('post_id',)
    results_class = WordPressCategory


class SetPostCategories(AuthParamsOffsetMixin, AuthenticatedMethod):
    """
    Assign a set of categories to a blog post.

    Parameters:
        `post_id`: ID of the blog post
        `categories`: `list` of `WordPressCategory` instances to assign

    Returns: `True` on successful category assignment.
    """
    method_name = 'mt.setPostCategories'
    method_args = ('post_id', 'categories',)


class GetTags(AuthenticatedMethod):
    """
    Retrieve list of all tags in the blog.

    Parameters:
        None

    Returns: `list` of `WordPressTag` instances.
    """
    method_name = 'wp.getTags'
    results_class = WordPressTag
