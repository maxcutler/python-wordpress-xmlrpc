from nose.plugins.attrib import attr

from tests import WordPressTestCase

from wordpress_xmlrpc.methods import taxonomies
from wordpress_xmlrpc.wordpress import WordPressTaxonomy


class TestTaxonomies(WordPressTestCase):

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
