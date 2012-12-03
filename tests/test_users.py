from nose.plugins.attrib import attr

from tests import WordPressTestCase

from wordpress_xmlrpc.methods import users
from wordpress_xmlrpc.wordpress import WordPressUser, WordPressBlog, WordPressAuthor


class TestUsers(WordPressTestCase):

    @attr('users')
    @attr('pycompat')
    def test_user_repr(self):
        user = WordPressUser()
        repr(user)

    @attr('users')
    @attr('pycompat')
    def test_author_repr(self):
        author = WordPressAuthor()
        repr(author)

    @attr('users')
    def test_get_user(self):
        user = self.client.call(users.GetUser(self.userid))
        self.assertTrue(isinstance(user, WordPressUser))
        self.assertEqual(user.username, self.username)

    @attr('users')
    def test_get_users(self):
        user_list = self.client.call(users.GetUsers())
        self.assert_list_of_classes(user_list, WordPressUser)
        found = False
        for user in user_list:
            if user.id == self.userid:
                found = True
                break
        self.assertTrue(found)

    @attr('users')
    def test_get_profile(self):
        user = self.client.call(users.GetProfile())
        self.assertTrue(isinstance(user, WordPressUser))
        self.assertEqual(user.username, self.username)

    @attr('users')
    def test_edit_profile(self):
        user = self.client.call(users.GetProfile())
        self.assertTrue(isinstance(user, WordPressUser))
        old_first_name = user.first_name
        new_first_name = 'Foo bar'
        user.first_name = new_first_name
        result = self.client.call(users.EditProfile(user))
        self.assertTrue(result)

        # check that the value changed
        user2 = self.client.call(users.GetProfile())
        self.assertEqual(new_first_name, user2.first_name)

        # cleanup
        user.first_name = old_first_name
        self.client.call(users.EditProfile(user))

    @attr('users')
    def test_get_user_blogs(self):
        blogs = self.client.call(users.GetUsersBlogs())
        self.assert_list_of_classes(blogs, WordPressBlog)

    @attr('users')
    def test_get_authors(self):
        authors = self.client.call(users.GetAuthors())
        self.assert_list_of_classes(authors, WordPressAuthor)
