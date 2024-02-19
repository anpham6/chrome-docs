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

=========================== ==== === === ==== === ==== === === ==== ==== ====
 NPM                        JPEG GIF PNG WebP BMP TIFF PSD ICO AVIF HEIC HEIF
=========================== ==== === === ==== === ==== === === ==== ==== ====
image-size [#]_               x   x   x    x   x    x   x   x    x    x    x
probe-image-size [#]_         x   x   x    x   x    x   x   x    x    x    x
:doc:`jimp </image/index>`    x   x   x        x    x
=========================== ==== === === ==== === ==== === === ==== ==== ====

.. attention:: Element **width** or **height** including **max-width** or **max-height** being set will not be processed due to the likeliness of distortion.

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

  <img src="probe.png" />

.. code-block:: html
  :caption: Output

  <img src="probe.png" width="800" height="600" loading="lazy" />

.. _document-miscellaneous-element-content:

Element content
===============

.. code-block::
  :caption: `http://localhost:3000/project/index.html?className=active` [#]_

  {
    "selector": "p.inactive",
    "type": "replace",
    "textContent": "<b>content</b>",
    "attributes": {
      "class": "{{className}}"
    }
  }

.. code-block:: html
  :caption: Source
  :emphasize-lines: 1,3

  <p class="inactive">paragraph 1</p>
  <p>paragraph 2</p>
  <p class="inactive">paragraph 3</p>

.. code-block:: html
  :caption: Output
  :emphasize-lines: 1,3

  <p class="active"><b>content</b></p>
  <p>paragraph 2</p>
  <p class="active"><b>content</b></p>

.. caution:: Editing local files with complex :ref:`nested tag content <document-append-build-options>` is not recommended. Try using an element "**id**" when there are errors building.

@pi-r/chrome
============

.. versionadded:: 0.6.4

  *NPM* package **image-size** is optionally supported for image dimensions.

.. [#] When using server hosted directory based sqd.config.
.. [#] npm i image-size
.. [#] npm i probe-image-size
.. [#] Jimp is not recommended for detecting image dimensions.
.. [#] Attibute value replacement. (squared 5.1.5)