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

    @attr('users')
    def test_user_lifecycle(self):
        user = WordPressUser()
        user.username = 'harrietsmith'
        user.password = 'mysecretpassword'
        user.email = 'harriet.smith@example.com'
        user.role = 'subscriber'
        user.last_name = 'Smith'
        user_id = self.client.call(users.NewUser(user))
        self.assertTrue(user_id)
        user.user_id = user_id

        user.first_name = 'Harriet'
        response = self.client.call(users.EditUser(user.user_id, user))
        self.assertTrue(response)

        # re-fetch to confirm
        user2 = self.client.call(users.GetUser(user.user_id))
        self.assertEqual(user.first_name, user2.first_name)

        response = self.client.call(users.DeleteUser(user.user_id))
        self.assertTrue(response)
