========
Finalize
========

You can exclude unnecessary processing files using the dataset attribute in these tags:

- script
- link
- style

Other elements can be excluded only through a configuration file.

.. highlight:: html

.. code-block::
  :caption: Inline

  <script src="/dist/squared.js" data-chrome-file="exclude"></script>
  <script src="/dist/squared.base.js" data-chrome-file="exclude"></script>
  <script src="/dist/chrome.framework.js" data-chrome-file="exclude"></script>
  <script data-chrome-file="exclude">
    squared.setFramework(chrome);
    squared.save();
  </script>

There is a simpler way to exclude the same tags by using an *HTML* comment block when inside the ``<head>`` element. [#]_

.. code-block::
  :caption: Comment block
  :emphasize-lines: 3,17

  <head>
    <title></title>
    <!-- EXCLUDE: start -->
    <meta charset="utf-8"> <!-- not excluded -->
    <script src="/dist/squared.js"></script>
    <script src="/dist/squared.base.js"></script>
    <script src="/dist/chrome.framework.js"></script>
    <script>
      squared.setFramework(chrome);
      squared.save();
    </script>
    <style>
      body {
        max-width: 1920px;
      }
    </style>
    <!-- EXCLUDE: end -->
    <link rel="stylesheet" href="/common/util.css">
  </head>

You can similarly prevent any element from being downloaded or transformed using the value "**ignore**".

::

  <iframe src="https://www.google.com/maps" data-chrome-file="ignore"></iframe>

.. [#] Cannot be used with "stripCommentsAndCDATA = true".