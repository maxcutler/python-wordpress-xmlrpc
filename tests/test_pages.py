from nose.plugins.attrib import attr

from tests import WordPressTestCase

from wordpress_xmlrpc.methods import pages, posts
from wordpress_xmlrpc.wordpress import WordPressPage


class TestPages(WordPressTestCase):

    @attr('pages')
    def test_get_page_status_list(self):
        status_list = self.client.call(pages.GetPageStatusList())
        self.assertTrue(isinstance(status_list, dict))

    @attr('pages')
    def test_get_page_templates(self):
        templates = self.client.call(pages.GetPageTemplates())
        self.assertTrue(isinstance(templates, dict))
        self.assertTrue('Default' in templates)

    @attr('pages')
    def test_get_pages(self):
        page_list = self.client.call(posts.GetPosts({'post_type': 'page'}, results_class=WordPressPage))
        self.assert_list_of_classes(page_list, WordPressPage)

    @attr('pages')
    def test_page_lifecycle(self):
        page = WordPressPage()
        page.title = 'Test Page'
        page.content = 'This is my test page.'

        # create the page
        page_id = self.client.call(posts.NewPost(page))
        self.assertTrue(page_id)

        # fetch the newly created page
        page2 = self.client.call(posts.GetPost(page_id, results_class=WordPressPage))
        self.assertTrue(isinstance(page2, WordPressPage))
        self.assertEqual(str(page2.id), page_id)

        # edit the page
        page2.content += '<br><b>Updated:</b> This page has been updated.'
        response = self.client.call(posts.EditPost(page_id, page2))
        self.assertTrue(response)

        # delete the page
        response = self.client.call(posts.DeletePost(page_id))
        self.assertTrue(response)
