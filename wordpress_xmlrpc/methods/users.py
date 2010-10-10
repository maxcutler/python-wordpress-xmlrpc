from wordpress_xmlrpc.base import *
from wordpress_xmlrpc.mixins import *
from wordpress_xmlrpc.wordpress import WordPressBlog

class GetUserInfo(BloggerApiMethodMixin, AuthenticatedMethod):
	method_name = 'blogger.getUserInfo'
	requires_blog = False

class GetUsersBlogs(AuthenticatedMethod):
	method_name = 'wp.getUsersBlogs'
	requires_blog = False

	def process_result(self, blog_list):
		return [WordPressBlog(blog) for blog in blog_list]