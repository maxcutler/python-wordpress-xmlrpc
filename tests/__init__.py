import os
import unittest
import collections

from wordpress_xmlrpc import Client
from wordpress_xmlrpc.compat import ConfigParser


class WordPressTestCase(unittest.TestCase):

    def setUp(self):
        config = ConfigParser()
        with open('wp-config.cfg', 'r') as f:
            config.readfp(f)

        self.xmlrpc_url = config.get('wordpress', 'url')
        self.username = config.get('wordpress', 'username')
        self.userid = config.get('wordpress', 'userid')
        self.client = Client(self.xmlrpc_url,
                             self.username,
                             config.get('wordpress', 'password'))

    def assert_list_of_classes(self, lst, kls):
        """
        Verifies that a list contains objects of a specific class.
        """
        self.assertTrue(isinstance(lst, collections.Iterable))

        for obj in lst:
            self.assertTrue(isinstance(obj, kls))
