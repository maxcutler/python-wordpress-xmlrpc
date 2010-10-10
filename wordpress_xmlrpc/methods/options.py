from wordpress_xmlrpc.base import *
from wordpress_xmlrpc.mixins import *
from wordpress_xmlrpc.wordpress import WordPressOption

class GetOptions(AuthenticatedMethod):
	method_name = 'wp.getOptions'
	method_args = ('options',)

	def process_result(self, options_dict):
		options = []
		for key, value in options_dict.items():
			value['name'] = key
			options.append(WordPressOption(value))
		return options

class SetOptions(GetOptions):
	method_name = 'wp.setOptions'