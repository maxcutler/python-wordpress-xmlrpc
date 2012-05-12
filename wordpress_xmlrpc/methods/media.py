from wordpress_xmlrpc.base import *
from wordpress_xmlrpc.wordpress import WordPressMedia


class GetMediaLibrary(AuthenticatedMethod):
    """
    Retrieve filtered list of media library items.

    Parameters:
        `filter`: `dict` with optional keys:
            * `number`: number of media items to retrieve
            * `offset`: query offset
            * `parent_id`: ID of post the media item is attached to.
                         Use empty string (default) to show all media items.
                         Use `0` to show unattached media items.
            * `mime_type`: file mime-type to filter by (e.g., 'image/jpeg')

    Returns: `list` of :class:`WordPressMedia` instances.
    """
    method_name = 'wp.getMediaLibrary'
    method_args = ('filter',)
    results_class = WordPressMedia


class GetMediaItem(AuthenticatedMethod):
    """
    Retrieve an individual media item.

    Parameters:
        `attachment_id`: ID of the media item.

    Returns: :class:`WordPressMedia` instance.
    """
    method_name = 'wp.getMediaItem'
    method_args = ('attachment_id',)
    results_class = WordPressMedia


class UploadFile(AuthenticatedMethod):
    """
    Upload a file to the blog.

    Note: the file is not attached to or inserted into any blog posts.

    Parameters:
        `data`: `dict` with three items:
            * `name`: filename
            * `type`: MIME-type of the file
            * `bits`: base-64 encoded contents of the file. See xmlrpclib.Binary()
            * `overwrite` (optional): flag to override an existing file with this name

    Returns: `dict` with keys `id`, `file` (filename), `url` (public URL), and `type` (MIME-type).
    """
    method_name = 'wp.uploadFile'
    method_args = ('data',)
