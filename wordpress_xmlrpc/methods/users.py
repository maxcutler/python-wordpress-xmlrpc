from wordpress_xmlrpc.base import *
from wordpress_xmlrpc.wordpress import WordPressBlog, WordPressAuthor, WordPressUser


class GetUsers(AuthenticatedMethod):
    """
    Retrieve list of users in the blog.

    Parameters:
        `filter`: optional `dict` of filters:
            * `number`
            * `offset`
            * `role`

        `fields`: optional `list` of fields to return. Specific fields, or groups 'basic' or 'all'.

    Returns: `list` of :class:`WordPressUser` instances.
    """
    method_name = 'wp.getUsers'
    optional_args = ('filter', 'fields')
    results_class = WordPressUser


class GetUser(AuthenticatedMethod):
    """
    Retrieve an individual user.

    Parameters:
        `user_id`: ID of the user
        `fields`: (optional) `list` of fields to return. Specific fields, or groups 'basic' or 'all'.

    Returns: :class:`WordPressUser` instance.
    """
    method_name = 'wp.getUser'
    method_args = ('user_id',)
    optional_args = ('fields',)
    results_class = WordPressUser


class GetProfile(AuthenticatedMethod):
    """
    Retrieve information about the connected user.

    Parameters:
        None

    Returns: instance of :class:`WordPressUser` representing the user whose credentials are being used with the XML-RPC API.
    """
    method_name = 'wp.getProfile'
    results_class = WordPressUser


class EditProfile(AuthenticatedMethod):
    """
    Edit profile fields of the connected user.

    Parameters:
        `user`: `WordPressUser` instance.

    Returns: `True` on successful edit.
    """
    method_name = 'wp.editProfile'
    method_args = ('user',)


class GetUserInfo(GetProfile):
    """Alias for GetProfile for backwards compatibility"""
    pass


class GetUsersBlogs(AuthenticatedMethod):
    """
    Retrieve list of blogs that this user belongs to.

    Parameters:
        None

    Returns: `list` of :class:`WordPressBlog` instances.
    """
    method_name = 'wp.getUsersBlogs'
    results_class = WordPressBlog

    def get_args(self, client):
        # strip off first (blog_id) parameter
        return super(GetUsersBlogs, self).get_args(client)[1:]


class GetAuthors(AuthenticatedMethod):
    """
    Retrieve list of authors in the blog.

    Parameters:
        None

    Returns: `list` of :class:`WordPressAuthor` instances.
    """
    method_name = 'wp.getAuthors'
    results_class = WordPressAuthor


class GetUsers(AuthenticatedMethod):
    """
    Retrieve list of users in the blog.

    Parameters:
        `filter`: optional `dict` of filters:
            * `number`
            * `offset`
            * `role`

        `fields`: optional `list` of fields to return. Specific fields, or groups 'basic' or 'all'.

    Returns: `list` of :class:`WordPressUser` instances.
    """
    method_name = 'wp.getUsers'
    optional_args = ('filter', 'fields')
    results_class = WordPressUser


class GetUser(AuthenticatedMethod):
    """
    Retrieve an individual user.

    Parameters:
        `user_id`: ID of the user
        `fields`: (optional) `list` of fields to return. Specific fields, or groups 'basic' or 'all'.

    Returns: :class:`WordPressUser` instance.
    """
    method_name = 'wp.getUser'
    method_args = ('user_id',)
    optional_args = ('fields',)
    results_class = WordPressUser


class NewUser(AuthenticatedMethod):
    """
    Create new user on the blog.

    Parameters:
        `user`: A :class:`WordPressUser` instance with at least `username`, `password`, and `email`.
        `send_mail`: (optional) Send a confirmation email to the new user.

    Returns: ID of the newly-created blog user (an integer).
    """
    method_name = 'wp.newUser'
    method_args = ('user',)
    optional_args = ('send_mail',)


class EditUser(AuthenticatedMethod):
    """
    Edit an existing blog post.

    Parameters:
        `user_id`: ID of the user to edit.
        `user`: `WordPressUser` instance.

    Returns: `True` on successful edit.
    """
    method_name = 'wp.editUser'
    method_args = ('user_id', 'user')


class DeleteUser(AuthenticatedMethod):
    """
    Delete a blog user.

    Parameters:
        `user_id`: ID of the blog user to delete.
        `reassign_id`: ID of the blog user to reassign this user's posts to.

    Returns: `True` on successful deletion.
    """
    method_name = 'wp.deleteUser'
    method_args = ('user_id',)
    optional_args = ('reassign_id',)
