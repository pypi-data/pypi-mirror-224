validators - Python Data Validation for Humans™
===============================================

|Tests| |Bandit| |Version Status| |Downloads|

Python has all kinds of data validation tools, but every one of them
seems to require defining a schema or form. I wanted to create a simple
validation library where validating a simple value does not require
defining a form or a schema.

.. code:: python

   >>> import validators

   >>> validators.email('someone@example.com')
   True

Resources
---------

-  `Documentation <https://python-validators.github.io/validators/>`__
-  `Issue
   Tracker <https://github.com/python-validators/validators/issues>`__
-  `Security <https://github.com/python-validators/validators/blob/master/SECURITY.md>`__
-  `Code <https://github.com/python-validators/validators/>`__

.. |Tests| image:: https://github.com/python-validators/validators/actions/workflows/main.yml/badge.svg
   :target: https://github.com/python-validators/validators/actions/workflows/main.yml
.. |Bandit| image:: https://github.com/python-validators/validators/actions/workflows/bandit.yml/badge.svg
   :target: https://github.com/python-validators/validators/actions/workflows/bandit.yml
.. |Version Status| image:: https://img.shields.io/pypi/v/validators.svg
   :target: https://pypi.python.org/pypi/validators/
.. |Downloads| image:: https://img.shields.io/pypi/dm/validators.svg
   :target: https://pypi.python.org/pypi/validators/


.. toctree::
   :hidden:
   :maxdepth: 2
   :caption: Reference:
   :glob:

   reference/*
