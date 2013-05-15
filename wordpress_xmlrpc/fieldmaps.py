import datetime

from wordpress_xmlrpc.compat import xmlrpc_client


class FieldMap(object):
    """
    Container for settings mapping a WordPress XML-RPC request/response struct
    to a Python, programmer-friendly class.

    Parameters:
        `inputName`: name of the field in XML-RPC response.
        `outputNames`: (optional) list of field names to use when generating new XML-RPC request. defaults to `[inputName]`
        `default`: (optional) default value to use when none is supplied in XML-RPC response. defaults to `None`
        `conversion`: (optional) function to convert Python value to XML-RPC value for XML-RPC request.
    """

    def __init__(self, inputName, outputNames=None, default=None, conversion=None):
        self.name = inputName
        self.output_names = outputNames or [inputName]
        self.default = default
        self.conversion = conversion

    def convert_to_python(self, xmlrpc=None):
        """
        Extracts a value for the field from an XML-RPC response.
        """
        if xmlrpc:
            return xmlrpc.get(self.name, self.default)
        elif self.default:
            return self.default
        else:
            return None

    def convert_to_xmlrpc(self, input_value):
        """
        Convert a Python value to the expected XML-RPC value type.
        """
        if self.conversion:
            return self.conversion(input_value)
        else:
            return input_value

    def get_outputs(self, input_value):
        """
        Generate a set of output values for a given input.
        """
        output_value = self.convert_to_xmlrpc(input_value)

        output = {}
        for name in self.output_names:
            output[name] = output_value

        return output


class IntegerFieldMap(FieldMap):
    """
    FieldMap pre-configured for handling integer fields.
    """

    def __init__(self, *args, **kwargs):
        if 'conversion' not in kwargs:
            kwargs['conversion'] = int

        super(IntegerFieldMap, self).__init__(*args, **kwargs)


class DateTimeFieldMap(FieldMap):
    """
    FieldMap pre-configured for handling DateTime fields.
    """

    def __init__(self, *args, **kwargs):
        if 'conversion' not in kwargs:
            kwargs['conversion'] = xmlrpc_client.DateTime

        super(DateTimeFieldMap, self).__init__(*args, **kwargs)

    def convert_to_python(self, xmlrpc=None):
        if xmlrpc:
            # make sure we have an `xmlrpc_client.DateTime` instance
            raw_value = xmlrpc.get(self.name, self.default)
            if not isinstance(raw_value, xmlrpc_client.DateTime):
                raw_value = xmlrpc_client.DateTime(raw_value)

            # extract its timetuple and convert to datetime
            try:
                tt = raw_value.timetuple()
            except ValueError:
                # Workaround for a combination of Python and WordPress bug
                # which would return a null date for Draft posts. This is not
                # the case for recent versions of WP, but drafts created a that
                # time still have a null date.
                # The python bug is http://bugs.python.org/issue2623 and
                # affects xmlrpclib when fed a timezone aware DateTime
                if str(raw_value) == "00000000T00:00:00Z":
                    raw_value = xmlrpc_client.DateTime("00010101T00:00:00")
                    tt = raw_value.timetuple()
                else:
                    raise
            return datetime.datetime(*tuple(tt)[:6])
        elif self.default:
            return self.default
        else:
            return None


class TermsListFieldMap(FieldMap):
    """
    FieldMap that converts to/from WordPress objects.
    """
    def __init__(self, object_class, *args, **kwargs):
        self.object_class = object_class
        super(TermsListFieldMap, self).__init__(*args, **kwargs)

    def convert_to_python(self, xmlrpc=None):
        if xmlrpc and self.name in xmlrpc:
            values = []
            for value in xmlrpc.get(self.name):
                values.append(self.object_class(value))
            return values
        else:
            return []

    def convert_to_xmlrpc(self, input_value):
        if input_value:
            values = {}
            for term in input_value:
                if term.taxonomy not in values:
                    values[term.taxonomy] = []
                values[term.taxonomy].append(int(term.id))
            return values
        else:
            return None
