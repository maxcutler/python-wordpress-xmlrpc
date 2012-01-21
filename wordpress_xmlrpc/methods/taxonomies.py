from wordpress_xmlrpc.base import *
from wordpress_xmlrpc.mixins import *
from wordpress_xmlrpc.wordpress import WordPressTaxonomy


class GetTaxonomies(AuthenticatedMethod):
    """
    Retrieve the list of available taxonomies for the blog.

    Parameters:
        None

    Returns: `list` of `WordPressTaxonomy` instances.
    """
    method_name = 'wp.getTaxonomies'
    results_class = WordPressTaxonomy


class GetTaxonomy(AuthenticatedMethod):
    """
    Retrieve an individual taxonomy.

    Parameters:
        `taxonomy_name`: name of the taxonomy

    Returns: `WordPressTaxonomy` instance.
    """
    method_name = 'wp.getTaxonomy'
    method_args = ('taxonomy_name',)
    results_class = WordPressTaxonomy
