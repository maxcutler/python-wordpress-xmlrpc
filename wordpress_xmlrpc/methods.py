from base import *
from mixins import *
from wordpress import *

class SayHello(AnonymousMethod):
    method_name = 'demo.sayHello'

class AddTwoNumbers(AnonymousMethod):
    method_name = 'demo.addTwoNumbers'
    method_args = ('number1', 'number2')

class GetRecentPosts(AuthenticatedMethod):
    method_name = 'metaWeblog.getRecentPosts'
    method_args = ('num_posts',)

    def process_result(self, post_list):
        return [WordPressPost(post) for post in post_list]

class GetPost(AuthParamsOffsetMixin, AuthenticatedMethod):
    method_name = 'metaWeblog.getPost'
    method_args = ('post_id',)

    def process_result(self, raw_post):
        return WordPressPost(raw_post)

class NewPost(AuthenticatedMethod):
    method_name = 'metaWeblog.newPost'
    method_args = ('content', 'publish')

class EditPost(AuthParamsOffsetMixin, AuthenticatedMethod):
    method_name = 'metaWeblog.editPost'
    method_args = ('post_id', 'content', 'publish')

class DeletePost(BloggerApiMethodMixin, AuthParamsOffsetMixin, AuthenticatedMethod):
    method_name = 'blogger.deletePost'
    method_args = ('post_id', )