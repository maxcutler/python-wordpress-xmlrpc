try:
    import xmlrpclib as xmlrpc_client  # py2.x
except ImportError:
    from xmlrpc import client as xmlrpc_client  # py3.x


import types
try:
    dict_type = types.DictType  # py2.x
except AttributeError:
    dict_type = dict  # py3.x


try:
    from ConfigParser import ConfigParser  # py2.x
except ImportError:
    from configparser import ConfigParser  # py3.x

try:
    unicode('test')
except NameError:
    def unicode(s):
        return s
