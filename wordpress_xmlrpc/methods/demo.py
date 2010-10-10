from wordpress_xmlrpc.base import *


class SayHello(AnonymousMethod):
    method_name = 'demo.sayHello'


class AddTwoNumbers(AnonymousMethod):
    method_name = 'demo.addTwoNumbers'
    method_args = ('number1', 'number2')
