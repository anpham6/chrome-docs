=================
squared-functions
=================

squared-express
===============

.. code-block::
  :caption: squared.json

  {
    "node": {
      "compat": {
        "v4": true
      }
    }
  }

.. option:: --compat-v4

  Override **node.compat.v4** and enable compatibility with *squared-functions*.

.. option:: --no-compat-v4

  Override **node.compat.v4** and disable compatibility with *squared-functions*.

.. attention:: **node.compat.v4** will be disabled as of :target:`squared 5.2.0` in *squared.json*.

Settings
--------

Deprecated settings from *squared-functions* were removed. Misplaced properties that are undetected will use the default :target:`E-mc` value.

.. option:: --migrations

  Will be required as of :target:`squared-express 3.2.0` for those who still have not to made the suggested conversions. [#]_

.. option:: --no-migrations

  Ignore unsupported and possibly incorrect values from previous installations. [#]_

@e-mc/compat-v4
===============

.. code-block::
  :caption: package.json

  {
    "dependencies": {
      "@e-mc/compat-v4": "^0.8.0"
    }
  }

Include once in the main process before using ``require`` with packages that use or inherit from *squared-functions*.

.. attention:: It is not a dependency [#]_ as of :target:`squared 5.2.0` and will be removed from :target:`E-mc` once the API is stable.

sqd-serve
---------

The module is no longer directly loadable as of **0.14.0**. Migration for settings are still available using **node.compat.v4** or command line options.

.. [#] squared-express 3.2 + sqd-serve 0.14 (alternative \-\-compat-v4)
.. [#] squared-express 3.1 + sqd-serve 0.13
.. [#] npm i @e-mc/compat-v4