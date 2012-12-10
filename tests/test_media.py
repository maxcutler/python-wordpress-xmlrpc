import mimetypes

from nose.plugins.attrib import attr

from tests import WordPressTestCase

from wordpress_xmlrpc.compat import xmlrpc_client
from wordpress_xmlrpc.methods import media
from wordpress_xmlrpc.wordpress import WordPressMedia


class TestMedia(WordPressTestCase):

    @attr('media')
    @attr('pycompat')
    def test_media_repr(self):
        media = WordPressMedia()
        repr(media)

    @attr('media')
    def test_get_media_library(self):
        num_items = 10
        library = self.client.call(media.GetMediaLibrary({'number': num_items}))
        self.assert_list_of_classes(library, WordPressMedia)
        self.assertTrue(len(library) <= num_items)

    @attr('media')
    def test_get_media_item(self):
        # this method cannot yet be tested, as it's impossible to get an ID to query against
        # media_item = self.client.call(media.GetMediaItem(__))
        # self.assertTrue(isinstance(media_item, WordPressMedia))
        pass

    @attr('media')
    def test_upload_file(self):
        # note: due to limitations in the XML-RPC API, this test will always create a new media item
        filename = 'wordpress_logo.png'
        with open('tests/files/' + filename, "rb") as img:
            data = {
                'name': filename,
                'bits': xmlrpc_client.Binary(img.read()),
                'type': mimetypes.read_mime_types(filename) or mimetypes.guess_type(filename)[0],
            }
            response = self.client.call(media.UploadFile(data))
            self.assertTrue(isinstance(response, dict))
