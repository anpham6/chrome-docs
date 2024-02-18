========
E-mc 0.8
========

.. toctree::
  :maxdepth: 1

  features
  document/index
  image/index
  cloud/index
  db/index
  task/index
  build
  modules/index
  references
  versions
  squared-functions <legacy>

Examples use **squared** 4/5 and **chrome** as the reference framework. These concepts can be used with any NodeJS (>=14) application.

.. note:: Using `squared <https://squared.readthedocs.io>`_ or squared-express is not required.

NodeJS 14 LTS
=============

Optional fail safe dependencies are going to be removed when **NodeJS 22** starts development in April 2024. The code itself will still be **ES2020** and will continue to work equivalently if these dependencies are self-installed.

Abort Controller
----------------

.. highlight:: bash

.. code-block::
  :caption: Under 15.4 + 16.0

  npm i abort-controller event-target-shim

.. code-block::
  :caption: Minimum 14.17 + 15.0

  node --experimental-abortcontroller serve.js

UUID
----

.. code-block::
  :caption: Under 14.17 + 15.6

  npm i uuid

Release date for **E-mc 0.9** is April 29, 2024.

License
=======

BSD 3-Clause