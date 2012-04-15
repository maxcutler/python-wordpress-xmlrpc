from nose.plugins.attrib import attr

from tests import WordPressTestCase

from wordpress_xmlrpc.methods import categories, posts
from wordpress_xmlrpc.wordpress import WordPressCategory, WordPressTag, WordPressPost


class TestCategories(WordPressTestCase):

    @attr('categories')
    def test_get_tags(self):
        tags = self.client.call(categories.GetTags())
        self.assert_list_of_classes(tags, WordPressTag)

    @attr('categories')
    def test_get_categories(self):
        cats = self.client.call(categories.GetCategories())
        self.assert_list_of_classes(cats, WordPressCategory)

    @attr('categories')
    def test_category_lifecycle(self):
        # Create category object
        cat = WordPressCategory()
        cat.name = 'Test Category'

        # Create the category in WordPress
        cat_id = self.client.call(categories.NewCategory(cat))
        self.assertTrue(cat_id)
        cat.cat_id = cat_id

        # Check that the new category shows in category suggestions
        suggestions = self.client.call(categories.SuggestCategories('test', 10))
        self.assertTrue(isinstance(suggestions, list))
        found = False
        for suggestion in suggestions:
            if suggestion['category_id'] == str(cat_id):
                found = True
                break
        self.assertTrue(found)

        # Delete the category
        response = self.client.call(categories.DeleteCategory(cat_id))
        self.assertTrue(response)

    @attr('categories')
    def test_category_post(self):
        # create a test post
        post = WordPressPost()
        post.title = 'Test Post'
        post.slug = 'test-post'
        post.user = self.userid
        post_id = self.client.call(posts.NewPost(post))

        # create a test category
        cat = WordPressCategory()
        cat.name = 'Test Category'
        cat.cat_id = self.client.call(categories.NewCategory(cat))

        # set category on post
        response = self.client.call(categories.SetPostCategories(post_id, [cat.struct]))
        self.assertTrue(response)

        # fetch categories for the post to verify
        post_cats = self.client.call(categories.GetPostCategories(post_id))
        self.assert_list_of_classes(post_cats, WordPressCategory)
        self.assertEqual(post_cats[0].cat_id, str(cat.cat_id))

        # cleanup
        self.client.call(categories.DeleteCategory(cat.cat_id))
        self.client.call(posts.DeletePost(post_id))
