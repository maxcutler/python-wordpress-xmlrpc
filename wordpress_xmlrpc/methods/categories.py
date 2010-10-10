from wordpress_xmlrpc.base import *
from wordpress_xmlrpc.mixins import *
from wordpress_xmlrpc.wordpress import WordPressCategory

class GetCategories(AuthenticatedMethod):
	method_name = 'wp.getCategories'
	# results_class = WordPressCategory

class NewCategory(AuthenticatedMethod):
	method_name = 'wp.newCategory'
	method_args = ('category',)

class DeleteCategory(AuthenticatedMethod):
	method_name = 'wp.deleteCategory'
	method_args = ('category_id',)