import datetime
import unittest
import xmlrpclib

from nose.plugins.attrib import attr

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
            'dateCreated': xmlrpclib.DateTime('20111009T08:07:06'),
        }
        obj = SampleModel(response)

        self.assertTrue(hasattr(obj, 'date_created'))
        self.assertTrue(isinstance(obj.date_created, datetime.datetime))
        self.assertTrue(isinstance(obj.struct['dateCreated'], xmlrpclib.DateTime))

    @attr('fieldmaps')
    def test_malformed_date_conversion(self):
        response = {
            'dateCreated': xmlrpclib.DateTime('-0001113TT0::0::00'),
        }
        self.assertRaises(FieldConversionError, SampleModel, response)
