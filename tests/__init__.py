from testconfig import config
import unittest

from wordpress_xmlrpc import Client


class WordPressTestCase(unittest.TestCase):

    def setUp(self):
        self.xmlrpc_url = config['wordpress']['url']
        self.username = config['wordpress']['username']
        self.userid = config['wordpress']['userid']
        self.client = Client(self.xmlrpc_url,
                             self.username,
                             config['wordpress']['password'])

    def assert_list_of_classes(self, lst, kls):
        """
        Verifies that a list contains objects of a specific class.
        """
        self.assertTrue(isinstance(lst, list))

        for obj in lst:
            self.assertTrue(isinstance(obj, kls))
