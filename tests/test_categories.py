from nose.plugins.attrib import attr

from tests import WordPressTestCase

from wordpress_xmlrpc.methods import taxonomies, posts
from wordpress_xmlrpc.wordpress import WordPressTerm, WordPressPost


class TestCategories(WordPressTestCase):

    @attr('categories')
    def test_get_tags(self):
        tags = self.client.call(taxonomies.GetTerms('post_tag'))
        for tag in tags:
            self.assertTrue(isinstance(tag, WordPressTerm))
            self.assertEquals(tag.taxonomy, 'post_tag')

    @attr('categories')
    def test_get_categories(self):
        cats = self.client.call(taxonomies.GetTerms('category'))
        for cat in cats:
            self.assertTrue(isinstance(cat, WordPressTerm))
            self.assertEquals(cat.taxonomy, 'category')

    @attr('categories')
    def test_category_lifecycle(self):
        # Create category object
        cat = WordPressTerm()
        cat.name = 'Test Category'
        cat.taxonomy = 'category'

        # Create the category in WordPress
        cat_id = self.client.call(taxonomies.NewTerm(cat))
        self.assertTrue(cat_id)
        cat.id = cat_id

        try:
            # Check that the new category shows in category suggestions
            suggestions = self.client.call(taxonomies.GetTerms('category', {'search': 'test'}))
            self.assertTrue(isinstance(suggestions, list))
            found = False
            for suggestion in suggestions:
                if suggestion.id == cat_id:
                    found = True
                    break
            self.assertTrue(found)
        finally:
            # Delete the category
            response = self.client.call(taxonomies.DeleteTerm(cat.taxonomy, cat.id))
            self.assertTrue(response)

    @attr('categories')
    def test_category_post(self):
        # create a test post
        post = WordPressPost()
        post.title = 'Test Post'
        post.slug = 'test-post'
        post.user = self.userid
        post.id = self.client.call(posts.NewPost(post))

        # create a test category
        cat = WordPressTerm()
        cat.name = 'Test Category'
        cat.taxonomy = 'category'
        cat.id = self.client.call(taxonomies.NewTerm(cat))

        # set category on post
        try:
            post.terms = [cat]
            response = self.client.call(posts.EditPost(post.id, post))
            self.assertTrue(response)

            # fetch categories for the post to verify
            post2 = self.client.call(posts.GetPost(post.id, ['terms']))
            post_cats = post2.terms
            self.assert_list_of_classes(post_cats, WordPressTerm)
            self.assertEqual(post_cats[0].id, cat.id)
        finally:
            # cleanup
            self.client.call(taxonomies.DeleteTerm(cat.taxonomy, cat.id))
            self.client.call(posts.DeletePost(post.id))
