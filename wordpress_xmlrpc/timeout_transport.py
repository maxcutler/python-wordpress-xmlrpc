import httplib
import socket
import xmlrpclib


class TimeoutHTTPConnection(httplib.HTTPConnection):

    def connect(self):
        httplib.HTTPConnection.connect(self)
        self.sock.settimeout(self.timeout)


class TimeoutHTTP(httplib.HTTP):
    _connection_class = TimeoutHTTPConnection

    def set_timeout(self, timeout):
        self._conn.timeout = timeout


class TimeoutTransport(xmlrpclib.Transport):

    def __init__(self, timeout=socket._GLOBAL_DEFAULT_TIMEOUT,
                 *args, **kwargs):
        xmlrpclib.Transport.__init__(self, *args, **kwargs)
        self.timeout = timeout

    def make_connection(self, host):
        if self._connection and host == self._connection[0]:
            return self._connection[1]

        chost, self._extra_headers, x509 = self.get_host_info(host)
        self._connection = host, httplib.HTTPConnection(chost)
        return self._connection[1]
