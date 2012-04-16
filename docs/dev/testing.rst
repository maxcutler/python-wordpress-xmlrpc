Testing
=======

Requirements
------------

``nose`` is used as the test runner. Use ``easy_install`` or ``pip`` to install::

	pip nose


Configuring against your server
-------------------------------

To test this library, we must perform XML-RPC requests against an
actual WordPress server. To configure against your own server:

* Copy the included ``wp-config-sample.cfg`` file to ``wp-config.cfg``.
* Edit ``wp-config.cfg`` and fill in the necessary values.

Running Tests
-------------

Note: Be sure to have installed ``nose`` and created your ``wp-config.cfg``.

To run the entire test suite, run the following from the root of the repository::

	nosetests

To run a sub-set of the tests, you can specify a specific feature area::

	nosetests -a posts

You can run against multiple areas::

	nosetests -a posts -a comments

Or you can run everything except a specific area::

	nosetests -a '!comments'

You can use all the normal ``nose`` command line options. For example, to increase output level::

	nosetests -a demo --verbosity=3

Full usage details:

* `nose`__

__ http://readthedocs.org/docs/nose/en/latest/usage.html

Contributing Tests
------------------

If you are submitting a patch for this library, please be sure to include
one or more tests that cover the changes.

if you are adding new test methods, be sure to tag them with the appropriate
feature areas using the ``@attr()`` decorator.
