from wordpress_xmlrpc.base import *
from wordpress_xmlrpc.wordpress import WordPressComment


class GetComment(AuthenticatedMethod):
    """
    Retrieve an individual comment.

    Parameters:
        `comment_id`: ID of the comment to retrieve.

    Returns: :class:`WordPressPost` instance.
    """
    method_name = 'wp.getComment'
    method_args = ('comment_id',)
    results_class = WordPressComment


class NewComment(AuthenticatedMethod):
    """
    Create a new comment on a post.

    Parameters:
        `post_id`: The id of the post to add a comment to.
        `comment`: A :class:`WordPressComment` instance with at least the `content` value set.

    Returns: ID of the newly-created comment (an integer).
    """
    method_name = 'wp.newComment'
    method_args = ('post_id', 'comment')


class NewAnonymousComment(AnonymousMethod):
    """
    Create a new comment on a post without authenticating.

    NOTE: Requires support on the blog by setting the following filter in a plugin or theme:

        add_filter( 'xmlrpc_allow_anonymous_comments', '__return_true' );

    Parameters:
        `post_id`: The id of the post to add a comment to.
        `comment`: A :class:`WordPressComment` instance with at least the `content` value set.

    Returns: ID of the newly-created comment (an integer).
    """
    method_name = 'wp.newComment'
    method_args = ('post_id', 'comment')


class EditComment(AuthenticatedMethod):
    """
    Edit an existing comment.

    Parameters:
        `comment_id`: The id of the comment to edit.
        `comment`: A :class:`WordPressComment` instance with at least the `content` value set.

    Returns: `True` on successful edit.
    """
    method_name = 'wp.editComment'
    method_args = ('comment_id', 'comment')


class DeleteComment(AuthenticatedMethod):
    """
    Delete an existing comment.

    Parameters:
        `comment_id`: The id of the comment to be deleted.

    Returns: `True` on successful deletion.
    """
    method_name = 'wp.deleteComment'
    method_args = ('comment_id',)


class GetCommentStatusList(AuthenticatedMethod):
    """
    Retrieve the set of possible blog comment statuses (e.g., "approve," "hold," "spam").

    Parameters:
        None

    Returns: `dict` of values and their pretty names.

    Example:
        >>> client.call(GetCommentStatusList())
        {'hold': 'Unapproved', 'approve': 'Approved', 'spam': 'Spam'}
    """
    method_name = 'wp.getCommentStatusList'


class GetCommentCount(AuthenticatedMethod):
    """
    Retrieve comment count for a specific post.

    Parameters:
        `post_id`: The id of the post to retrieve comment count for.

    Returns: `dict` of comment counts for the post divided by comment status.

    Example:
        >>> client.call(GetCommentCount(1))
        {'awaiting_moderation': '2', 'total_comments': 23, 'approved': '18', 'spam': 3}
    """
    method_name = 'wp.getCommentCount'
    method_args = ('post_id',)


class GetComments(AuthenticatedMethod):
    """
    Gets a set of comments for a post.

    Parameters:
        `filter`: a `dict` with the following values:
            * `post_id`: the id of the post to retrieve comments for
            * `status`: type of comments of comments to retrieve (optional, defaults to 'approve')
            * `number`: number of comments to retrieve (optional, defaults to 10)
            * `offset`: retrieval offset (optional, defaults to 0)

    Returns: `list` of :class:`WordPressComment` instances.
    """
    method_name = 'wp.getComments'
    method_args = ('filter',)
    results_class = WordPressComment
