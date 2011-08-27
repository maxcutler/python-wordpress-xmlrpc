class ServerConnectionError(Exception):
    """
    An error while attempting to connect to the XML-RPC endpoint.
    """
    pass


class FieldConversionError(Exception):
    """
    An error while converting field Python value to XML-RPC value type.

    Attributes:
        `field_name`: name of the field
        `input_value`: value that was passed to the conversion function
    """
    def __init__(self, field_name, error):
        self.field_name = field_name
        self.error = error

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return u'%s (%s)' % (self.field_name, str(self.error))
