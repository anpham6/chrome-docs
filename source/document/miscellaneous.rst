=============
Miscellaneous
=============

.. _document-miscellaneous-merge-conflicts:

Merge conflicts
===============

Only one command per element is supported (except data sources) when using ``sqd.config``. The last selector always takes precedence except when **mergeType** is defined. [#]_

.. code-block::
  :caption: "ordinal": 1 | index.html*

  [
    {
      "selector": "img#picture1",
      "commands": ["png@"]
    },
    {
      "selector": "img#picture2",
      "commands": ["webp%"]
    }
  ]

.. code-block::
  :caption: "ordinal": 2 | \*\*/\*.html?output=prod

  [
    {
      "selector": "img",
      "mergeType": "under",
      "hash": "sha256", // Merged
      "commands": ["jpeg@"] // No effect
    },
    /* OR */
    {
      "selector": "img",
      "mergeType": "over",
      "hash": "sha256", // Merged
      "commands": ["jpeg@"] // All images will be JPEG
    },
    /* OR */
    {
      "selector": "img",
      "mergeType": "none",
      "hash": "sha256", // No effect when "dev" is present
      "commands": ["jpeg@"] // Same
    }
  ]

.. _document-miscellaneous-image-dimensions:

Image dimensions
================

- **npm** i *probe-image-size*

::

  {
    "selector": "img",
    "filename": "probe.png",
    /* OR */
    "mimeType": "image/png", // "image/unknown"
    "attributes": {
      "width": "detect",
      "height": "detect", 
      "loading": "lazy" // Optional
    }
  }

.. note:: :doc:`Jimp </image/index>` is used secondarily to detect dimensions but with limited file type support.

.. _document-miscellaneous-element-content:

Element content
===============

::

  {
    "selector": "p.inactive",
    "type": "replace",
    "textContent": "<b>content</b>", // <p class="active"><b>content</b></p>
    "attributes": {
      "class": "active"
    }
  }

.. [#] When using server hosted directory based sqd.config.