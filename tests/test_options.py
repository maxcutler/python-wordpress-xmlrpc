from nose.plugins.attrib import attr

from tests import WordPressTestCase

from wordpress_xmlrpc.methods import options
from wordpress_xmlrpc.wordpress import WordPressOption


class TestOptions(WordPressTestCase):

    @attr('options')
    @attr('pycompat')
    def test_option_repr(self):
        option = WordPressOption()
        repr(option)

    @attr('options')
    def test_get_all_options(self):
        opts = self.client.call(options.GetOptions([]))
        self.assert_list_of_classes(opts, WordPressOption)
        self.assertTrue(len(opts) > 0)

    @attr('options')
    def test_get_specific_options(self):
        desired_opts = ['date_format', 'time_format']
        opts = self.client.call(options.GetOptions(desired_opts))
        self.assert_list_of_classes(opts, WordPressOption)
        self.assertEqual(len(desired_opts), len(opts))
        self.assertEqual(set(desired_opts), set([opt.name for opt in opts]))

    @attr('options')
    def test_set_option(self):
        # get current value
        old_tagline = self.client.call(options.GetOptions('blog_tagline'))[0].value

        # change value
        new_tagline = 'New tagline'
        opts = self.client.call(options.SetOptions({'blog_tagline': new_tagline}))
        self.assertEqual(opts[0].value, new_tagline)

        # set back to original value
        response = self.client.call(options.SetOptions({'blog_tagline': old_tagline}))
        self.assertTrue(response)
