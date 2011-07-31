from wordpress_xmlrpc.base import *
from wordpress_xmlrpc.mixins import *
from wordpress_xmlrpc.wordpress import WordPressPost


class GetRecentPosts(AuthenticatedMethod):
    """
    Retrieve most recent posts from the blog.

    Parameters:
        `num_posts`: Number of blog posts to return.

    Returns: `list` of `WordPressPost` instances.
    """
    method_name = 'metaWeblog.getRecentPosts'
    method_args = ('num_posts',)
    results_class = WordPressPost


class GetPost(AuthParamsOffsetMixin, AuthenticatedMethod):
    """
    Retrieve an individual blog post.

    Parameters:
        `post_id`: ID of the blog post to retrieve.

    Returns: `WordPressPost` instance.
    """
    method_name = 'metaWeblog.getPost'
    method_args = ('post_id',)
    results_class = WordPressPost


class NewPost(AuthenticatedMethod):
    """
    Create a new post on the blog.

    Parameters:
        `content`: A `WordPressPost` instance with at least the `title` and `description` values set.
        `publish`: Boolean indicating whether the blog post should be published upon creation.

    Returns: ID of the newly-created blog post (an integer).
    """
    method_name = 'metaWeblog.newPost'
    method_args = ('content', 'publish')


class EditPost(AuthParamsOffsetMixin, AuthenticatedMethod):
    """
    Edit an existing blog post.

    Parameters:
        `post_id`: ID of the blog post to edit.
        `content`: A `WordPressPost` instance with the new values for the blog post.
        `publish`: Boolean indicating whether the blog post should be published upon being updated.

    Returns: `True` on successful edit.
    """
    method_name = 'metaWeblog.editPost'
    method_args = ('post_id', 'content', 'publish')


class DeletePost(BloggerApiMethodMixin, AuthParamsOffsetMixin, AuthenticatedMethod):
    """
    Delete a blog post.

    Parameters:
        `post_id`: ID of the blog post to delete.

    Returns: `True` on successful deletion.
    """
    method_name = 'blogger.deletePost'
    method_args = ('post_id', )


class GetPostStatusList(AuthenticatedMethod):
    """
    Retrieve the set of possible blog post statuses (e.g., "draft," "private," "publish").

    Parameters:
        None

    Returns: `dict` of values and their pretty names.

    Example:
        >>> client.call(GetPostStatusList())
        {'draft': 'Draft', 'private': 'Private', 'pending': 'Pending Review', 'publish': 'Published'}
    """
    method_name = 'wp.getPostStatusList'


class GetPostFormats(AuthenticatedMethod):
    """
    Retrieve the set of post formats used by the blog.

    Parameters:
        None

    Returns: `dict` containing a `dict` of all blog post formats (`all`)
             and a list of formats `supported` by the theme.

    Example:
        >>> client.call(GetPostFormats())
        {'all': {'status': 'Status', 'quote': 'Quote', 'image': 'Image', 'aside': 'Aside', 'standard': 'Standard', 'link': 'Link', 'chat': 'Chat', 'video': 'Video', 'audio': 'Audio', 'gallery': 'Gallery'},
         'supported': ['aside', 'link', 'gallery', 'status', 'quote', 'image']}
    """
    method_name = 'wp.getPostFormats'

    def get_args(self, client):
        args = super(GetPostFormats, self).get_args(client)
        args += ({'show-supported': True},)
        return args


class PublishPost(AuthParamsOffsetMixin, AuthenticatedMethod):
    """
    Mark a blog post as published.

    Parameters:
        `post_id`: ID of the blog post to publish.

    Returns: ID of the published blog post.
    """
    method_name = 'mt.publishPost'
    method_args = ('post_id',)
