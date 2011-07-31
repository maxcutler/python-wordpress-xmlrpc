from nose.plugins.attrib import attr

from tests import WordPressTestCase

from wordpress_xmlrpc.methods import posts
from wordpress_xmlrpc.wordpress import WordPressPost


class TestPosts(WordPressTestCase):

    @attr('posts')
    def test_get_post_status_list(self):
        status_list = self.client.call(posts.GetPostStatusList())
        self.assertTrue(isinstance(status_list, dict))

    @attr('posts')
    def test_get_post_formats(self):
        formats = self.client.call(posts.GetPostFormats())
        self.assertTrue(isinstance(formats, dict))
        self.assertTrue('all' in formats)
        self.assertTrue('supported' in formats)

    @attr('posts')
    def test_get_recent_posts(self):
        num_posts = 10
        recent_posts = self.client.call(posts.GetRecentPosts(num_posts))
        self.assert_list_of_classes(recent_posts, WordPressPost)
        self.assertTrue(len(recent_posts) <= num_posts)

    @attr('posts')
    def test_post_lifecycle(self):
        # create a post object
        post = WordPressPost()
        post.title = 'Test post'
        post.slug = 'test-post'
        post.description = 'This is test post using the XML-RPC API.'
        post.allow_comments = True
        post.user = self.userid

        # create the post as a draft
        post_id = self.client.call(posts.NewPost(post, False))
        self.assertTrue(post_id)

        # fetch the newly-created post
        post2 = self.client.call(posts.GetPost(post_id))
        self.assertTrue(isinstance(post2, WordPressPost))
        self.assertEqual(str(post2.id), post_id)

        # publish the post
        response = self.client.call(posts.PublishPost(post_id))
        self.assertEqual(str(response), post_id)

        # update the post
        post2.description += '<br><b>Updated:</b> This post has been updated.'
        response = self.client.call(posts.EditPost(post_id, post2, True))
        self.assertTrue(response)

        # delete the post
        response = self.client.call(posts.DeletePost(post_id))
        self.assertTrue(response)
