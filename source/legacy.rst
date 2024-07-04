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

.. attention:: It will be disabled as of :target:`squared 5.2.0` in *squared.json*.

Settings
--------

Deprecated settings from *squared-functions* were removed. Misplaced properties that are undetected will use the default **E-mc** value.

.. option:: --migrations

  Will be required as of :target:`squared-express 3.2.0` for projects which have not made the suggested conversions. [#]_

.. option:: --no-migrations

  Ignore unsupported and possibly incorrect values from previous installations. [#]_

@e-mc/compat-v4
===============

When not using *squared-express* you will have to include it in the main process before using ``require`` with packages that use or inherit from *squared-functions*.

.. code-block::
  :caption: package.json

  {
    "dependencies": {
      "@e-mc/compat-v4": "^0.9.0"
    }
  }

.. attention:: It will not installed by default [#]_ as of :target:`squared 5.2.0` in *package.json*.

sqd-serve
---------

The module is no longer directly loadable as of **0.14.0**. Migration for settings are still available through **node.compat.v4** or command line options.

.. [#] squared-express 3.2 + sqd-serve 0.14 (alternative \-\-compat-v4)
.. [#] squared-express 3.1 + sqd-serve 0.13
.. [#] npm i @e-mc/compat-v4