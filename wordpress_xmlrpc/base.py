import xmlrpclib
import collections, types

class Client(object):
    def __init__(self, url, username, password, blog_id=0):
        self.url = url
        self.username = username
        self.password = password
        self.blog_id = blog_id

        self.server = xmlrpclib.ServerProxy(url, use_datetime=True)
        self.supported_methods = self.server.mt.supportedMethods()

    def call(self, method):
        assert (method.method_name in self.supported_methods)
        server_method = getattr(self.server, method.method_name)
        args = method.get_args(self)
        # print method.method_name, args
        raw_result = server_method(*args)
        return method.process_result(raw_result)

class XmlrpcMethod(object):
    method_name = None
    method_args = None
    args_start_position = 0
    default_args_position = 0
    results_class = None

    def __init__(self, *args):
        if self.method_args:
            if len(args) != len(self.method_args):
                raise Exception, "Invalid number of parameters to %s" % self.method_name

            for i, arg_name in enumerate(self.method_args):
                setattr(self, arg_name, args[i])

    def default_args(self, client):
        return tuple()

    def get_args(self, client):
        default_args = self.default_args(client)

        if self.method_args:
            args = tuple(getattr(self, arg) for arg in self.method_args)
            args = args[:self.default_args_position] + default_args + args[self.default_args_position:]
        else:
            args = default_args

        return ((0,)*self.args_start_position) + args

    def process_result(self, raw_result):
        if self.results_class and raw_result:
            if isinstance(raw_result, types.DictType):
                return self.results_class(raw_result)
            elif isinstance(raw_result, collections.Iterable):
                return [self.results_class(result) for result in raw_result]

        return raw_result

class AnonymousMethod(XmlrpcMethod):
    pass

class AuthenticatedMethod(XmlrpcMethod):
    requires_blog = True

    def default_args(self, client):
        if self.requires_blog:
            return (client.blog_id, client.username, client.password)
        else:
            return (client.username, client.password)