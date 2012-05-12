class ServerConnectionError(Exception):
    """
    An error while attempting to connect to the XML-RPC endpoint.
    """
    pass


class UnsupportedXmlrpcMethodError(Exception):
    """
    An error while attempting to call a method that is not
    supported by the XML-RPC server.
    """
    pass


class XmlrpcDisabledError(Exception):
    """
    An error when XML-RPC services are disabled in WordPress.
    """
    pass


class InvalidCredentialsError(Exception):
    """
    An error when the XML-RPC server rejects the user's credentials
    (username/password combination).
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
        return self.field_name
