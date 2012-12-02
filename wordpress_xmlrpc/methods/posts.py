from wordpress_xmlrpc.base import *
from wordpress_xmlrpc.wordpress import WordPressPost, WordPressPostType


class GetPosts(AuthenticatedMethod):
    """
    Retrieve posts from the blog.

    Parameters:
       `filter`: optional `dict` of filters:
            * `number`
            * `offset`
            * `orderby`
            * `order`: 'ASC' or 'DESC'
            * `post_type`: Defaults to 'post'
            * `post_status`

    Returns: `list` of :class:`WordPressPost` instances.
    """
    method_name = 'wp.getPosts'
    optional_args = ('filter', 'fields')
    results_class = WordPressPost


class GetPost(AuthenticatedMethod):
    """
    Retrieve an individual blog post.

    Parameters:
        `post_id`: ID of the blog post to retrieve.

    Returns: :class:`WordPressPost` instance.
    """
    method_name = 'wp.getPost'
    method_args = ('post_id',)
    optional_args = ('fields',)
    results_class = WordPressPost


class NewPost(AuthenticatedMethod):
    """
    Create a new post on the blog.

    Parameters:
        `content`: A :class:`WordPressPost` instance with at least the `title` and `content` values set.

    Returns: ID of the newly-created blog post (an integer).
    """
    method_name = 'wp.newPost'
    method_args = ('content',)


class EditPost(AuthenticatedMethod):
    """
    Edit an existing blog post.

    Parameters:
        `post_id`: ID of the blog post to edit.
        `content`: A :class:`WordPressPost` instance with the new values for the blog post.

    Returns: `True` on successful edit.
    """
    method_name = 'wp.editPost'
    method_args = ('post_id', 'content')


class DeletePost(AuthenticatedMethod):
    """
    Delete a blog post.

    Parameters:
        `post_id`: ID of the blog post to delete.

    Returns: `True` on successful deletion.
    """
    method_name = 'wp.deletePost'
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


class GetPostTypes(AuthenticatedMethod):
    """
    Retrieve a list of post types used by the blog.

    Parameters:
        None

    Returns: `dict` with names as keys and :class:`WordPressPostType` instances as values.
    """
    method_name = 'wp.getPostTypes'
    results_class = WordPressPostType

    def process_result(self, raw_result):
        result = {}
        for name, raw_value in raw_result.items():
            result[name] = self.results_class(raw_value)
        return result


class GetPostType(AuthenticatedMethod):
    """
    Retrieve an individual blog post type.

    Parameters:
        `post_type`: Name of the blog post type to retrieve.

    Returns: :class:`WordPressPostType` instance.
    """
    method_name = 'wp.getPostType'
    method_args = ('post_type',)
    results_class = WordPressPostType


class GetRevisions(AuthenticatedMethod):
    """
    Retrieve all revisions of a post.

    Parameters:
        `post_id`: ID of the post.

    Returns: `list` of :class:`WordPressPost` instances.
    """
    method_name = 'wp.getRevisions'
    method_args = ('post_id',)
    optional_args = ('fields',)
    results_class = WordPressPost


class RestoreRevision(AuthenticatedMethod):
    """
    Restores a post to a previous revision.

    Parameters:
        `revision_id`: ID of the revision to revert to.

    Returns: `True` on successful reversion.
    """
    method_name = 'wp.restoreRevision'
    method_args = ('revision_id',)
