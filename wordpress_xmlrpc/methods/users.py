from wordpress_xmlrpc.base import *
from wordpress_xmlrpc.mixins import *
from wordpress_xmlrpc.wordpress import WordPressBlog, WordPressAuthor

class GetUserInfo(BloggerApiMethodMixin, AuthenticatedMethod):
	method_name = 'blogger.getUserInfo'
	requires_blog = False

class GetUsersBlogs(AuthenticatedMethod):
	method_name = 'wp.getUsersBlogs'
	requires_blog = False
	results_class = WordPressBlog

class GetAuthors(AuthenticatedMethod):
	method_name = 'wp.getAuthors'
	results_class = WordPressAuthor
