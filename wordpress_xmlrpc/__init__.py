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
            'post_status': self.post_status,
            'mt_excerpt': self.excerpt,
            'mt_text_more': self.extended_text,
            'mt_keywords': self.tags,
            'mt_allow_comments': int(self.allow_comments),
            'mt_allow_pings': int(self.allow_pings),
            'dateCreated': xmlrpclib.DateTime(self.date_created),
            'categories': self.categories,
        }

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

        self.server = xmlrpclib.ServerProxy(url)

    def supported_methods(self):
        """
        Retrieve list of supported XML-RPC methods.
        """
        return self.server.mt.supportedMethods()

    def get_post(self, id):
        return WordPressPost(self.server.metaWeblog.getPost(id, self.username, self.password))

    def get_recent_posts(self, num_posts=10):
        posts = self.server.metaWeblog.getRecentPosts(self.blog_id, self.username, self.password, num_posts)
        return [WordPressPost(post) for post in posts]

    def new_post(self, post, publish=True):
        return self.server.metaWeblog.newPost(self.blog_id, self.username, self.password, post.content_struct, publish)

    def edit_post(self, post, publish=True):
        return self.server.metaWeblog.editPost(post.id, self.username, self.password, post.content_struct, publish)

def main():
    pass

if __name__ == '__main__':
    main()
