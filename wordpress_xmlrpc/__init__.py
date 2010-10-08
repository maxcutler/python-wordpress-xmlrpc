#!/usr/bin/python
""""
  Copyright 2010 Max Cutler. All Rights Reserved.

  For license information please check the LICENSE page of the package.
"""

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
            self.categories = []
            self.custom_fields = []

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

def main():
    pass

if __name__ == '__main__':
    main()
