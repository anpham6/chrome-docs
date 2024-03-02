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

Command line options ``--compat-v4`` and ``--no-compat-v4`` are also available and will override the value in settings.

.. attention:: ``node.compat.v4`` will be disabled by default when using `squared-express` **3.2.0**.

@e-mc/compat-v4
===============

.. code-block::
  :caption: package.json

  {
    "dependencies": {
      "@e-mc/compat-v4": "^0.8.0"
    }
  }

Include once in the main process before using ``require`` with packages that use or inherit from `squared-functions`.

.. warning:: Deprecated settings from `squared-functions` were removed. Misplaced properties that are undetected will use the default unoptimized value.