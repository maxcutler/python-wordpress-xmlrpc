import random

from nose.plugins.attrib import attr

from tests import WordPressTestCase

from wordpress_xmlrpc.methods import comments, posts
from wordpress_xmlrpc.wordpress import WordPressComment, WordPressPost


class TestComments(WordPressTestCase):

    def setUp(self):
        super(TestComments, self).setUp()

        post = WordPressPost()
        post.title = 'Comments Test Post'
        post.slug = 'comments-test-post'
        post.user = self.userid
        self.post_id = self.client.call(posts.NewPost(post))

    @attr('comments')
    @attr('pycompat')
    def test_comment_repr(self):
        comment = WordPressComment()
        repr(comment)

    @attr('comments')
    def test_get_comment_status_list(self):
        status_list = self.client.call(comments.GetCommentStatusList())
        self.assertTrue(isinstance(status_list, dict))

    @attr('comments')
    def test_comment_lifecycle(self):
        comment = WordPressComment()
        comment.content = 'This is a test comment.'
        comment.user = self.userid

        # create comment
        comment_id = self.client.call(comments.NewComment(self.post_id, comment))
        self.assertTrue(comment_id)

        # edit comment
        comment.content = 'This is an edited comment.'
        response = self.client.call(comments.EditComment(comment_id, comment))
        self.assertTrue(response)

        # delete comment
        response = self.client.call(comments.DeleteComment(comment_id))
        self.assertTrue(response)

    @attr('comments')
    def test_post_comments(self):
        # create a bunch of comments
        comment_list = []

        counter = 0
        for i in range(1, random.randint(6, 15)):
            comment = WordPressComment()
            comment.content = 'Comment #%s' % counter
            comment.user = self.userid

            comment_id = self.client.call(comments.NewComment(self.post_id, comment))
            comment_list.append(comment_id)
            counter += 1

        # retrieve comment count
        comment_counts = self.client.call(comments.GetCommentCount(self.post_id))
        self.assertEqual(comment_counts['total_comments'], counter)

        # fetch a subset of the comments
        num_comments = 5
        post_comments = self.client.call(comments.GetComments({'post_id': self.post_id, 'number': num_comments}))
        self.assert_list_of_classes(post_comments, WordPressComment)
        self.assertEqual(num_comments, len(post_comments))

        # cleanup
        for comment in comment_list:
            self.client.call(comments.DeleteComment(comment))

    def tearDown(self):
        self.client.call(posts.DeletePost(self.post_id))
        super(WordPressTestCase, self).tearDown()
