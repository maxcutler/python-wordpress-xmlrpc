#!/usr/bin/python

import xmlrpclib
import urllib

class WordPressPost(object):
    def __init__(self, xmlrpc=None):
        if xmlrpc:
            self.id = xmlrpc['postid']
            self.user = xmlrpc['userid']
            self.date_created = xmlrpc['dateCreated']
            self.slug = xmlrpc['wp_slug']
            self.post_status = xmlrpc['post_status']
            self.title = xmlrpc['title']
            self.description = xmlrpc['description']
            self.excerpt = xmlrpc['mt_excerpt']
            self.extended_text = xmlrpc['mt_text_more']
            self.link = xmlrpc['link']
            self.permalink = xmlrpc['permaLink']
            self.allow_comments = xmlrpc['mt_allow_comments'] == 1
            self.allow_pings = xmlrpc['mt_allow_pings'] == 1
            self.tags = xmlrpc['mt_keywords']
            self.categories = xmlrpc['categories']
            self.custom_fields = xmlrpc['custom_fields']
        else:
            self.id = None
            self.user = None
            self.date_created = None
            self.slug = ''
            self.post_status = ''
            self.title = ''
            self.description = ''
            self.excerpt = ''
            self.extended_text = ''
            self.link = ''
            self.permalink = ''
            self.allow_comments = False
            self.allow_pings = False
            self.tags = ''
            self.categories = ['Uncategorized']
            self.custom_fields = []

    @property
    def content_struct(self):
        struct = {
            'post_type': 'post',
            'wp_author_id': self.user,
            'title': self.title,
            'description': self.description,
            'mt_excerpt': self.excerpt,
            'mt_text_more': self.extended_text,
            'mt_keywords': self.tags,
            'mt_allow_comments': int(self.allow_comments),
            'mt_allow_pings': int(self.allow_pings),
            'categories': self.categories,
        }

        if self.post_status:
            struct['post_status'] = self.post_status

        if self.date_created:
            struct['dateCreated'] = xmlrpclib.DateTime(self.date_created)

        if self.slug:
            struct['wp_slug'] = self.slug

        if self.custom_fields:
            struct['custom_fields'] = self.custom_fields

        return struct

    def __str__(self):
        return '%s (id=%s)' % (self.slug, self.id)


class Client(object):
    def __init__(self, url, username, password, blog_id=0):
        self.url = url
        self.username = username
        self.password = password
        self.blog_id = blog_id

        self.server = xmlrpclib.ServerProxy(url, use_datetime=True)

    def supported_methods(self):
        """
        Retrieve list of supported XML-RPC methods.
        """
        return self.server.mt.supportedMethods()

    def call(self, method):
        server_method = getattr(self.server, method.method_name)
        args = method.get_args(self)
        print method.method_name, args
        raw_result = server_method(*args)
        return method.process_result(raw_result)

class XmlrpcMethod(object):
    method_name = None
    method_args = None
    default_args_position = 0

    def __init__(self, *args):
        if self.method_args:
            if len(args) != len(self.method_args):
                raise Exception, "Invalid number of parameters to %s" % self.method_name

            for i, arg_name in enumerate(self.method_args):
                setattr(self, arg_name, args[i])

    def default_args(self, client):
        return tuple()

    def get_args(self, client):
        default_args = self.default_args(client)

        if self.method_args:
            args = tuple(getattr(self, arg) for arg in self.method_args)
            return args[:self.default_args_position] + default_args + args[self.default_args_position:]
        else:
            return default_args

    def process_result(self, raw_result):
        return raw_result

class AnonymousMethod(XmlrpcMethod):
    pass

class AuthenticatedMethod(XmlrpcMethod):
    requires_blog = True

    def default_args(self, client):
        if self.requires_blog:
            return (client.blog_id, client.username, client.password)
        else:
            return (client.username, client.password)

class AuthParamsOffsetMixin(object):
    requires_blog = False
    default_args_position = 1

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

def main():
    pass

if __name__ == '__main__':
    main()
