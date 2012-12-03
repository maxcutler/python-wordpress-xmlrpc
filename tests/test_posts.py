from nose.plugins.attrib import attr

from tests import WordPressTestCase

from wordpress_xmlrpc.methods import posts
from wordpress_xmlrpc.wordpress import WordPressPost, WordPressPostType


class TestPosts(WordPressTestCase):

    @attr('posts')
    @attr('pycompat')
    def test_post_repr(self):
        post = WordPressPost()
        repr(post)

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
    def test_get_posts(self):
        num_posts = 10
        recent_posts = self.client.call(posts.GetPosts({'number': num_posts}))
        self.assert_list_of_classes(recent_posts, WordPressPost)
        self.assertTrue(len(recent_posts) <= num_posts)

    @attr('posts')
    def test_post_lifecycle(self):
        # create a post object
        post = WordPressPost()
        post.title = 'Test post'
        post.slug = 'test-post'
        post.content = 'This is test post using the XML-RPC API.'
        post.comment_status = 'open'
        post.user = self.userid

        # create the post as a draft
        post_id = self.client.call(posts.NewPost(post))
        self.assertTrue(post_id)

        # fetch the newly-created post
        post2 = self.client.call(posts.GetPost(post_id))
        self.assertTrue(isinstance(post2, WordPressPost))
        self.assertEqual(str(post2.id), post_id)

        # update the post
        post2.content += '<br><b>Updated:</b> This post has been updated.'
        post2.post_status = 'publish'
        response = self.client.call(posts.EditPost(post_id, post2))
        self.assertTrue(response)

        # delete the post
        response = self.client.call(posts.DeletePost(post_id))
        self.assertTrue(response)

    @attr('post_types')
    def test_get_post_types(self):
        post_types = self.client.call(posts.GetPostTypes())
        self.assert_list_of_classes(post_types.values(), WordPressPostType)
        for name, post_type in post_types.items():
            self.assertEqual(name, post_type.name)

    @attr('post_types')
    def test_get_post_type(self):
        post_type = self.client.call(posts.GetPostType('post'))
        self.assertTrue(isinstance(post_type, WordPressPostType))

    @attr('posts')
    @attr('revisions')
    def test_revisions(self):
        original_title = 'Revisions test'
        post = WordPressPost()
        post.title = original_title
        post.slug = 'revisions-test'
        post.content = 'This is a test post using the XML-RPC API.'
        post_id = self.client.call(posts.NewPost(post))
        self.assertTrue(post_id)

        post.title = 'Revisions test updated'
        post.content += ' This is a second revision.'
        response = self.client.call(posts.EditPost(post_id, post))
        self.assertTrue(response)

        # test wp.getRevisions
        revision_list = self.client.call(posts.GetRevisions(post_id, ['post']))
        self.assert_list_of_classes(revision_list, WordPressPost)

        # workaround for WP bug #22686/22687
        # an auto-draft revision will survive wp.newPost, so pick the 2nd revision
        self.assertEqual(2, len(revision_list))
        real_rev = revision_list[1]
        self.assertTrue(real_rev)
        self.assertNotEquals(post_id, real_rev.id)

        # test wp.restoreRevision
        response2 = self.client.call(posts.RestoreRevision(real_rev.id))
        self.assertTrue(response2)
        post2 = self.client.call(posts.GetPost(post_id))
        self.assertEquals(original_title, post2.title)

        # cleanup
        self.client.call(posts.DeletePost(post_id))
