from wordpress_xmlrpc.base import *
from wordpress_xmlrpc.wordpress import WordPressTaxonomy, WordPressTerm


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


class GetTerms(AuthenticatedMethod):
    """
    Retrieve the list of available terms for a taxonomy.

    Parameters:
        `taxonomy_name`: name of the taxonomy
        `filter`: optional `dict` of filters:
            `number`
            `offset`
            `orderby`
            `order`: 'ASC' or 'DESC'
            `hide_empty`: Whether to return terms with count==0
            `search`: Case-insensitive search on term names

    Returns: `list` of `WordPressTerm` instances.
    """
    method_name = 'wp.getTerms'
    method_args = ('taxonomy_name',)
    optional_args = ('filter',)
    results_class = WordPressTerm


class GetTerm(AuthenticatedMethod):
    """
    Retrieve an individual term.

    Parameters:
        `taxonomy_name`: name of the taxonomy
        `term_id`: ID of the term

    Returns: `WordPressTerm` instance.
    """
    method_name = 'wp.getTerm'
    method_args = ('taxonomy_name', 'term_id')
    results_class = WordPressTerm


class NewTerm(AuthenticatedMethod):
    """
    Create new term.

    Parameters:
        `term`: instance of `WordPressTerm`

    Returns: ID of newly-created term (an integer).
    """
    method_name = 'wp.newTerm'
    method_args = ('term',)


class EditTerm(AuthenticatedMethod):
    """
    Edit an existing term.

    Parameters:
        `term_id`: ID of the term to edit.
        `content`: A `WordPressTerm` instance with the new values for the term.

    Returns: `True` on successful edit.
    """
    method_name = 'wp.editTerm'
    method_args = ('term_id', 'content')


class DeleteTerm(AuthenticatedMethod):
    """
    Delete a term.

    Parameters:
        `taxonomy_name`: name of the taxonomy
        `term_id`: ID of the term to delete.

    Returns: `True` on successful deletion.
    """
    method_name = 'wp.deleteTerm'
    method_args = ('taxonomy_name', 'term_id')
