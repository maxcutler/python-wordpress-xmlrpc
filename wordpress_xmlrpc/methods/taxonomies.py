from wordpress_xmlrpc.base import *
from wordpress_xmlrpc.wordpress import WordPressTaxonomy, WordPressTerm


class GetTaxonomies(AuthenticatedMethod):
    """
    Retrieve the list of available taxonomies for the blog.

    Parameters:
        None

    Returns: `list` of :class:`WordPressTaxonomy` instances.
    """
    method_name = 'wp.getTaxonomies'
    results_class = WordPressTaxonomy


class GetTaxonomy(AuthenticatedMethod):
    """
    Retrieve an individual taxonomy.

    Parameters:
        `taxonomy`: name of the taxonomy

    Returns: :class:`WordPressTaxonomy` instance.
    """
    method_name = 'wp.getTaxonomy'
    method_args = ('taxonomy',)
    results_class = WordPressTaxonomy


class GetTerms(AuthenticatedMethod):
    """
    Retrieve the list of available terms for a taxonomy.

    Parameters:
        `taxonomy`: name of the taxonomy

        `filter`: optional `dict` of filters:
            * `number`
            * `offset`
            * `orderby`
            * `order`: 'ASC' or 'DESC'
            * `hide_empty`: Whether to return terms with count==0
            * `search`: Case-insensitive search on term names

    Returns: `list` of :class:`WordPressTerm` instances.
    """
    method_name = 'wp.getTerms'
    method_args = ('taxonomy',)
    optional_args = ('filter',)
    results_class = WordPressTerm


class GetTerm(AuthenticatedMethod):
    """
    Retrieve an individual term.

    Parameters:
        `taxonomy`: name of the taxonomy

        `term_id`: ID of the term

    Returns: :class:`WordPressTerm` instance.
    """
    method_name = 'wp.getTerm'
    method_args = ('taxonomy', 'term_id')
    results_class = WordPressTerm


class NewTerm(AuthenticatedMethod):
    """
    Create new term.

    Parameters:
        `term`: instance of :class:`WordPressTerm`

    Returns: ID of newly-created term (an integer).
    """
    method_name = 'wp.newTerm'
    method_args = ('term',)


class EditTerm(AuthenticatedMethod):
    """
    Edit an existing term.

    Parameters:
        `term_id`: ID of the term to edit.

        `term`: A :class:`WordPressTerm` instance with the new values for the term.

    Returns: `True` on successful edit.
    """
    method_name = 'wp.editTerm'
    method_args = ('term_id', 'term')


class DeleteTerm(AuthenticatedMethod):
    """
    Delete a term.

    Parameters:
        `taxonomy`: name of the taxonomy

        `term_id`: ID of the term to delete.

    Returns: `True` on successful deletion.
    """
    method_name = 'wp.deleteTerm'
    method_args = ('taxonomy', 'term_id')
