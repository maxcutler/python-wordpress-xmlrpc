import collections
import sys

from wordpress_xmlrpc.compat import xmlrpc_client, dict_type
from wordpress_xmlrpc.exceptions import ServerConnectionError, UnsupportedXmlrpcMethodError, InvalidCredentialsError, XmlrpcDisabledError


class Client(object):
    """
    Connection to a WordPress XML-RPC API endpoint.

    To execute XML-RPC methods, pass an instance of an
    `XmlrpcMethod`-derived class to `Client`'s `call` method.
    """

    def __init__(self, url, username, password, blog_id=0, transport=None):
        self.url = url
        self.username = username
        self.password = password
        self.blog_id = blog_id

        try:
            self.server = xmlrpc_client.ServerProxy(url, allow_none=True, transport=transport)
            self.supported_methods = self.server.mt.supportedMethods()
        except xmlrpc_client.ProtocolError:
            e = sys.exc_info()[1]
            raise ServerConnectionError(repr(e))

    def call(self, method):
        if method.method_name not in self.supported_methods:
            raise UnsupportedXmlrpcMethodError(method.method_name)

        server_method = getattr(self.server, method.method_name)
        args = method.get_args(self)

        try:
            raw_result = server_method(*args)
        except xmlrpc_client.Fault:
            e = sys.exc_info()[1]
            if e.faultCode == 403:
                raise InvalidCredentialsError(e.faultString)
            elif e.faultCode == 405:
                raise XmlrpcDisabledError(e.faultString)
            else:
                raise
        return method.process_result(raw_result)


class XmlrpcMethod(object):
    """
    Base class for XML-RPC methods.

    Child classes can override methods and properties to customize behavior:

    Properties:
        * `method_name`: XML-RPC method name (e.g., 'wp.getUserInfo')
        * `method_args`: Tuple of method-specific required parameters
        * `optional_args`: Tuple of method-specific optional parameters
        * `results_class`: Python class which will convert an XML-RPC response dict into an object
    """
    method_name = None
    method_args = tuple()
    optional_args = tuple()
    results_class = None

    def __init__(self, *args, **kwargs):
        if self.method_args or self.optional_args:
            if self.optional_args:
                max_num_args = len(self.method_args) + len(self.optional_args)
                if not (len(self.method_args) <= len(args) <= max_num_args):
                    raise ValueError("Invalid number of parameters to %s" % self.method_name)
            else:
                if len(args) != len(self.method_args):
                    raise ValueError("Invalid number of parameters to %s" % self.method_name)

            for i, arg_name in enumerate(self.method_args):
                setattr(self, arg_name, args[i])

            if self.optional_args:
                for i, arg_name in enumerate(self.optional_args, start=len(self.method_args)):
                    if i >= len(args):
                        break
                    setattr(self, arg_name, args[i])

        if 'results_class' in kwargs:
            self.results_class = kwargs['results_class']

    def default_args(self, client):
        """
        Builds set of method-non-specific arguments.
        """
        return tuple()

    def get_args(self, client):
        """
        Builds final set of XML-RPC method arguments based on
        the method's arguments, any default arguments, and their
        defined respective ordering.
        """
        default_args = self.default_args(client)

        if self.method_args or self.optional_args:
            optional_args = getattr(self, 'optional_args', tuple())
            args = []
            for arg in (self.method_args + optional_args):
                if hasattr(self, arg):
                    obj = getattr(self, arg)
                    if hasattr(obj, 'struct'):
                        args.append(obj.struct)
                    else:
                        args.append(obj)
            args = list(default_args) + args
        else:
            args = default_args

        return args

    def process_result(self, raw_result):
        """
        Performs actions on the raw result from the XML-RPC response.

        If a `results_class` is defined, the response will be converted
        into one or more object instances of that class.
        """
        if self.results_class and raw_result:
            if isinstance(raw_result, dict_type):
                return self.results_class(raw_result)
            elif isinstance(raw_result, collections.Iterable):
                return [self.results_class(result) for result in raw_result]

        return raw_result


class AnonymousMethod(XmlrpcMethod):
    """
    An XML-RPC method for which no authentication is required.
    """
    pass


class AuthenticatedMethod(XmlrpcMethod):
    """
    An XML-RPC method for which user authentication is required.

    Blog ID, username and password details will be passed from
    the `Client` instance to the method call.
    """

    def default_args(self, client):
        return (client.blog_id, client.username, client.password)
