from nose.plugins.attrib import attr

from tests import WordPressTestCase

from wordpress_xmlrpc.methods import users
from wordpress_xmlrpc.wordpress import WordPressUser, WordPressBlog, WordPressAuthor


class TestUsers(WordPressTestCase):

    @attr('users')
    def test_get_user_info(self):
        user = self.client.call(users.GetUserInfo())
        self.assertTrue(isinstance(user, WordPressUser))
        self.assertEqual(user.nickname, self.username)

    @attr('users')
    def test_get_user_blogs(self):
        blogs = self.client.call(users.GetUsersBlogs())
        self.assert_list_of_classes(blogs, WordPressBlog)

    @attr('users')
    def test_get_authors(self):
        authors = self.client.call(users.GetAuthors())
        self.assert_list_of_classes(authors, WordPressAuthor)
