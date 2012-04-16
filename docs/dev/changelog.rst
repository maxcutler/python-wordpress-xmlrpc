History/CHANGELOG
=================

2.0
---

(April 16, 2012)

* Major rewrite to support new XML-RPC features in WordPress 3.4.
	* Rewrote ``WordPressPost`` and ``methods.posts`` module.
	* Removed CRUD methods for pages.
	* Added ``WordPressTaxonomy`` and ``WordPressTerm`` classes.
	* Added ``methods.taxonomies`` module.
	* Removed ``WordPressCategory`` and ``WordPressTag`` classes.
	* Removed ``methods.categories`` module.
	* Added ``id`` field to ``WordPressMedia``.
* Removed support for legacy-style (e.g., Blogger) methods.
	* Removed ``args_start_position`` and ``default_args_position`` parameters on ``XmlrpcMethod``.
	* Removed ``requires_blog`` parameter on ``AuthenticatedMethod``.
* Set default values on all fields that are used in ``str``/``unicode`` to avoid ``AttributeError`` exceptions.
* Fixed bug with ``FieldMap`` that caused ``False`` boolean values to be ignored.
* Added ability to override ``results_class`` via a method class constructor kwarg.
* Added support for optional method arguments.

1.5
---

(August 27, 2011)

* Refactored ``FieldMap`` to be more flexible.
* Added new ``Exception`` subclasses for more specific error handling.

1.4
---

(July 31, 2011)

* Added support for post formats.
* Added support for media methods.

1.3
---

(July 31, 2011)

* Created test suite.
* Added support for page methods.
* Added support for post/page passwords.

1.2
---

(June 25, 2011)

* Added support for comments methods.

1.1
---

(October 11, 2010)

* Implemented automatic conversion of WordPress objects in method invocations.

1.0
---

(October 10, 2010)

* Initial release.