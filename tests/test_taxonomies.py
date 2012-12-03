from nose.plugins.attrib import attr

from tests import WordPressTestCase

from wordpress_xmlrpc.methods import taxonomies
from wordpress_xmlrpc.wordpress import WordPressTaxonomy, WordPressTerm


class TestTaxonomies(WordPressTestCase):

    @attr('taxonomies')
    @attr('pycompat')
    def test_taxonomy_repr(self):
        tax = WordPressTaxonomy()
        repr(tax)

    @attr('taxonomies')
    @attr('pycompat')
    def test_term_repr(self):
        term = WordPressTerm()
        repr(term)

    @attr('taxonomies')
    def test_get_taxonomies(self):
        taxs = self.client.call(taxonomies.GetTaxonomies())
        self.assert_list_of_classes(taxs, WordPressTaxonomy)

    @attr('taxonomies')
    def test_get_taxonomy(self):
        tax = self.client.call(taxonomies.GetTaxonomy('category'))
        self.assertTrue(isinstance(tax, WordPressTaxonomy))

    @attr('taxonomies')
    def test_taxonomy_fields_match(self):
        """
        Check that the fields returned by singular and plural versions are the same.
        """
        tax1 = self.client.call(taxonomies.GetTaxonomy('category'))
        tax2 = None

        # find category taxonomy in the list of all taxonomies
        taxs = self.client.call(taxonomies.GetTaxonomies())
        for tax in taxs:
            if tax.name == 'category':
                tax2 = tax
                break
        self.assertTrue(tax2 is not None)

        # compare the two field-by-field
        for field in tax1.definition.keys():
            self.assertEqual(getattr(tax1, field), getattr(tax2, field))

    @attr('taxonomies')
    @attr('terms')
    def test_get_terms(self):
        terms = self.client.call(taxonomies.GetTerms('category'))
        self.assert_list_of_classes(terms, WordPressTerm)

    @attr('taxonomies')
    @attr('terms')
    def test_get_term(self):
        term = self.client.call(taxonomies.GetTerm('category', 1))
        self.assertTrue(isinstance(term, WordPressTerm))

    @attr('taxonomies')
    @attr('terms')
    def test_term_lifecycle(self):
        term = WordPressTerm()
        term.name = 'Test Term'
        term.taxonomy = 'category'

        # create the term
        term_id = self.client.call(taxonomies.NewTerm(term))
        self.assertTrue(term_id)
        term.id = term_id

        # re-fetch to verify
        term2 = self.client.call(taxonomies.GetTerm(term.taxonomy, term.id))
        self.assertEqual(term.name, term2.name)

        # set a description and save
        term.description = "My test term"
        response = self.client.call(taxonomies.EditTerm(term.id, term))
        self.assertTrue(response)

        # re-fetch to verify
        term3 = self.client.call(taxonomies.GetTerm(term.taxonomy, term.id))
        self.assertEqual(term.description, term3.description)

        # delete the term
        response = self.client.call(taxonomies.DeleteTerm(term.taxonomy, term.id))
        self.assertTrue(response)

    @attr('taxonomies')
    @attr('terms')
    def test_term_parent_child(self):
        parent = WordPressTerm()
        parent.taxonomy = 'category'
        parent.name = 'Test Parent Term'

        parent_id = self.client.call(taxonomies.NewTerm(parent))
        self.assertTrue(parent_id)
        parent.id = parent_id

        child = WordPressTerm()
        child.taxonomy = parent.taxonomy
        child.name = 'Test Child Term'
        child.parent = parent.id

        child_id = self.client.call(taxonomies.NewTerm(child))
        self.assertTrue(child_id)
        child.id = child_id

        try:
            # re-fetch to verify
            child2 = self.client.call(taxonomies.GetTerm(child.taxonomy, child.id))
            self.assertEqual(child.parent, child2.parent)
        finally:
            # cleanup
            self.client.call(taxonomies.DeleteTerm(child.taxonomy, child.id))
            self.client.call(taxonomies.DeleteTerm(parent.taxonomy, parent.id))

    @attr('taxonomies')
    @attr('terms')
    def test_term_search(self):
        tag1 = WordPressTerm()
        tag1.taxonomy = 'post_tag'
        tag1.name = 'Test FoobarA'

        tag1_id = self.client.call(taxonomies.NewTerm(tag1))
        self.assertTrue(tag1_id)
        tag1.id = tag1_id

        tag2 = WordPressTerm()
        tag2.taxonomy = 'post_tag'
        tag2.name = 'Test FoobarB'

        tag2_id = self.client.call(taxonomies.NewTerm(tag2))
        self.assertTrue(tag2_id)
        tag2.id = tag2_id

        try:
            results = self.client.call(taxonomies.GetTerms('post_tag', {'search': 'foobarb'}))
            found_tag1 = False
            found_tag2 = False
            for tag in results:
                if tag.id == tag1_id:
                    found_tag1 = True
                elif tag.id == tag2_id:
                    found_tag2 = True
            self.assertFalse(found_tag1)
            self.assertTrue(found_tag2)
        finally:
            # cleanup
            self.client.call(taxonomies.DeleteTerm(tag1.taxonomy, tag1.id))
            self.client.call(taxonomies.DeleteTerm(tag2.taxonomy, tag2.id))
