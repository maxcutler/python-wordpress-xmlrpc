from wordpress_xmlrpc.base import *
from wordpress_xmlrpc.mixins import *
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

    Returns: `list` of `WordPressTerm` instances.
    """
    method_name = 'wp.getTerms'
    method_args = ('taxonomy_name',)
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


class GetPostTerms(AuthenticatedMethod):
    """
    Retrieve list of terms assigned to a blog post.

    Parameters:
        `post_id`: ID of the blog post
        `group_by_taxonomy`: `bool` specifying whether to return terms grouped by taxonomy name
                             in a `dict` or as a flat list of `WordPressTerm`s

    Returns: Depends on value of `group_by_taxonomy`:
                True: `dict`, with taxonomy names as keys and `list` of `WordPressTerm` instances as values.
                False: `list` of `WordPressTerm` instances.
    """
    method_name = 'wp.getPostTerms'
    method_args = ('post_id', 'group_by_taxonomy')
    results_class = WordPressTerm

    def process_result(self, raw_result):
        if not self.group_by_taxonomy:
            # flat list, so normal processing
            return super(GetPostTerms, self).process_result(raw_result)
        else:
            # dictionary of taxonomy/terms. process each value individually
            result = {}
            for taxonomy, terms in raw_result.items():
                result[taxonomy] = super(GetPostTerms, self).process_result(terms)
            return result


class SetPostTerms(AuthenticatedMethod):
    """
    Assign a set of terms to a blog post.

    Parameters:
        `post_id`: ID of the blog post
        `terms`: `dict` with taxonomy names as keys and `list` of term IDs as values

    Returns: `True` on successful category assignment.

    Example:
        >>> client.call(SetPostTerms(15, {
                'category': [1, 4, 199],
                'post_tag': [6, 21, 39],
                'custom_tax': [384]
            }))
        True
    """
    method_name = 'wp.setPostTerms'
    method_args = ('post_id', 'terms',)
