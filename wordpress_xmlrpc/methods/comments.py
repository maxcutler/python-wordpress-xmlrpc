from wordpress_xmlrpc.base import *
from wordpress_xmlrpc.mixins import *
from wordpress_xmlrpc.wordpress import WordPressComment

class GetComment(AuthenticatedMethod):
    """
    Retreive an individual comment.

    Parameters:
        `blog_id`: ID of the blog hosting the comment.
        `comment_id`: ID of the comment to retrieve.

    Returns: `WordPressPost` instance.
    """
    method_name = 'wp.getComment'
    method_args = ('post_id', )
    results_class = WordPressComment

class NewComment(AuthenticatedMethod):
    """
    Create a new comment

    Parameters:
        `comment`: A `WordPressComment` instance with at least the `content` value set.

    Returns: ID of the newly-created comment (an integer).
    """
    method_name = 'metaWeblog.newPost'
    method_args = ('comment', )
