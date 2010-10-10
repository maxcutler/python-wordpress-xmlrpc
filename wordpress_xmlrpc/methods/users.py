from wordpress_xmlrpc.base import *
from wordpress_xmlrpc.mixins import *
from wordpress_xmlrpc.wordpress import *

class GetUserInfo(BloggerApiMethodMixin, AuthenticatedMethod):
	method_name = 'blogger.getUserInfo'
	requires_blog = False
