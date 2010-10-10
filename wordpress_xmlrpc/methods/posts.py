from wordpress_xmlrpc.base import *
from wordpress_xmlrpc.mixins import *
from wordpress_xmlrpc.wordpress import WordPressPost

class GetRecentPosts(AuthenticatedMethod):
    method_name = 'metaWeblog.getRecentPosts'
    method_args = ('num_posts',)
    results_class = WordPressPost

class GetPost(AuthParamsOffsetMixin, AuthenticatedMethod):
    method_name = 'metaWeblog.getPost'
    method_args = ('post_id',)
    results_class = WordPressPost

class NewPost(AuthenticatedMethod):
    method_name = 'metaWeblog.newPost'
    method_args = ('content', 'publish')

class EditPost(AuthParamsOffsetMixin, AuthenticatedMethod):
    method_name = 'metaWeblog.editPost'
    method_args = ('post_id', 'content', 'publish')

class DeletePost(BloggerApiMethodMixin, AuthParamsOffsetMixin, AuthenticatedMethod):
    method_name = 'blogger.deletePost'
    method_args = ('post_id', )

class GetPostStatusList(AuthenticatedMethod):
    method_name = 'wp.getPostStatusList'

class GetRecentPostTitles(AuthenticatedMethod):
    method_name = 'mt.getRecentPostTitles'
    method_args = ('num_posts',)

class PublishPost(AuthParamsOffsetMixin, AuthenticatedMethod):
    method_name = 'mt.publishPost'
    method_args = ('post_id',)