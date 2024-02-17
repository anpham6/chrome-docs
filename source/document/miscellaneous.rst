=============
Miscellaneous
=============

.. _document-miscellaneous-merge-conflicts:

Merge conflicts
===============

Only one command per element is supported (except data sources) when using :ref:`sqd.config <build-using-sqd-config>`. The last selector always takes precedence except when **mergeType** is defined. [#]_

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
      "hash": "sha256", // No effect
      "commands": ["jpeg@"] // No effect
    }
  ]

.. _document-miscellaneous-image-dimensions:

Image dimensions
================

.. rst-class:: miscellaneous-image

=============================== === === === ==== === ==== === === ==== ==== ====
 NPM                            JPG GIF PNG WebP BMP TIFF PSD ICO AVIF HEIC HEIF
=============================== === === === ==== === ==== === === ==== ==== ====
probe-image-size [#]_            x   x   x    x   x    x   x   x    x    x    x
:doc:`jimp </image/index>` [#]_  x   x   x        x    x
=============================== === === === ==== === ==== === === ==== ==== ====

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

.. code-block:: html
  :caption: Source

  <img src="image.png" />

.. code-block:: html
  :caption: Output

  <img src="image.png" width="800" height="600" loading="lazy" />

.. _document-miscellaneous-element-content:

Element content
===============

.. code-block::
  :caption: `http://localhost:3000/project/index.html?className=active` [#]_

  {
    "selector": "p.inactive",
    "type": "replace",
    "textContent": "<b>content</b>", // <p class="active"><b>content</b></p>
    "attributes": {
      "class": "{{className}}"
    }
  }

.. caution:: Editing complex layouts with nested tag content is not recommended. Try using an element "**id**" when there are errors building.

.. [#] When using server hosted directory based sqd.config.
.. [#] npm i probe-image-size
.. [#] Jimp is used secondarily to detect dimensions.
.. [#] Attibute value replacement. (squared 5.1.5)