from nose.plugins.attrib import attr

from tests import WordPressTestCase

from wordpress_xmlrpc.methods import demo


class TestDemo(WordPressTestCase):

    @attr('demo')
    def test_say_hello(self):
        response = self.client.call(demo.SayHello())
        self.assertEqual(response, "Hello!")

    @attr('demo')
    def test_add_two_numbers(self):
        sum = self.client.call(demo.AddTwoNumbers(2, 3))
        self.assertEqual(sum, 5)
