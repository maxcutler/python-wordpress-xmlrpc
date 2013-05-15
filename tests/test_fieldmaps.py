import datetime
import unittest

from nose.plugins.attrib import attr

from wordpress_xmlrpc.compat import xmlrpc_client
from wordpress_xmlrpc.exceptions import FieldConversionError
from wordpress_xmlrpc.fieldmaps import DateTimeFieldMap
from wordpress_xmlrpc.wordpress import WordPressBase


class SampleModel(WordPressBase):
    definition = {
        'date_created': DateTimeFieldMap('dateCreated'),
    }


class FieldMapsTestCase(unittest.TestCase):

    @attr('fieldmaps')
    def test_date_conversion(self):
        response = {
            'dateCreated': xmlrpc_client.DateTime('20111009T08:07:06'),
        }
        obj = SampleModel(response)

        self.assertTrue(hasattr(obj, 'date_created'))
        self.assertTrue(isinstance(obj.date_created, datetime.datetime))
        self.assertTrue(isinstance(obj.struct['dateCreated'], xmlrpc_client.DateTime))

    @attr('fieldmaps')
    def test_malformed_date_conversion(self):
        response = {
            'dateCreated': xmlrpc_client.DateTime('-0001113TT0::0::00'),
        }
        self.assertRaises(FieldConversionError, SampleModel, response)

    @attr('fieldmaps')
    def test_empty_date_with_timezone_is_accepted(self):
        response = {
            'dateCreated': xmlrpc_client.DateTime('00000000T00:00:00Z'),
        }
        obj = SampleModel(response)
        self.assertTrue(hasattr(obj, 'date_created'))
        self.assertEqual(obj.date_created, datetime.datetime(1, 1, 1, 0, 0))
