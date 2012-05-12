from wordpress_xmlrpc.base import *
from wordpress_xmlrpc.wordpress import WordPressOption


class GetOptions(AuthenticatedMethod):
    """
    Retrieve list of blog options.

    Parameters:
        `options`: `list` of option names to retrieve; if empty, all options will be retrieved

    Returns: `list` of :class:`WordPressOption` instances.
    """
    method_name = 'wp.getOptions'
    method_args = ('options',)

    def process_result(self, options_dict):
        options = []
        for key, value in options_dict.items():
            value['name'] = key
            options.append(WordPressOption(value))
        return options


class SetOptions(GetOptions):
    """
    Update the value of an existing blog option.

    Parameters:
        `options`: `dict` of key/value pairs

    Returns: `list` of :class:`WordPressOption` instances representing the updated options.
    """
    method_name = 'wp.setOptions'
    method_args = ('options',)
