from wordpress_xmlrpc.base import *


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
