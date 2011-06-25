from wordpress_xmlrpc.base import *
from wordpress_xmlrpc.wordpress import WordPressComment


class GetComment(AuthenticatedMethod):
    """
    Retrieve an individual comment.

    Parameters:
        `comment_id`: ID of the comment to retrieve.

    Returns: `WordPressPost` instance.
    """
    method_name = 'wp.getComment'
    method_args = ('comment_id',)
    results_class = WordPressComment


class NewComment(AuthenticatedMethod):
    """
    Create a new comment on a post.

    Parameters:
        `post_id`: The id of the post to add a comment to.
        `comment`: A `WordPressComment` instance with at least the `content` value set.

    Returns: ID of the newly-created comment (an integer).
    """
    method_name = 'wp.newComment'
    method_args = ('post_id', 'comment',)


class EditComment(AuthenticatedMethod):
    """
    Edit an existing comment.

    Parameters:
        `comment_id`: The idea of the comment to edit.
        `comment`: A `WordPressComment` instance with at least the `content` value set.

    Returns: `True` on successful edit.
    """
    method_name = 'wp.editComment'
    method_args = ('comment_id', 'comment',)


class DeleteComment(AuthenticatedMethod):
    """
    Delete an existing comment.

    Parameters:
        `comment_id`: The id of the comment to be deleted.

    Returns: `True` on successful deletion.
    """
    method_name = 'wp.deleteComment'
    method_args = ('comment_id', )
