=============
Miscellaneous
=============

.. _document-miscellaneous-merge-conflicts:

Merge conflicts
===============

Only one command per element is supported :lower:`(except data sources)` when using :ref:`sqd.config <build-using-sqd-config>`. The last selector always takes precedence except when **mergeType** is defined. [#]_

.. code-block::
  :caption: "ordinal": 1 | index.html*

  [
    {
      "selector": "img#picture1",
      "attributes": { "alt": "Picture 1" },
      "commands": ["png@"]
    },
    {
      "selector": "img#picture2",
      "attributes": { "loading": "lazy", "alt": "Picture 2" },
      "commands": ["webp%"]
    }
  ]

.. code-block::
  :caption: "ordinal": 2 | \*\*/\*.html?output=prod
  :emphasize-lines: 4,12,20,28

  [
    {
      "selector": "img",
      "mergeType": "under",
      "hash": "sha256", // Merged
      "attributes": { "alt": "Picture 1" }, // No effect
      "commands": ["jpeg@"] // No effect
    },
    /* OR */
    {
      "selector": "img",
      "mergeType": "preserve",
      "hash": "sha256", // Merged
      "attributes": { "loading": "lazy", "alt": "Picture 1" }, // Merged as "Picture 1"
      "commands": ["jpeg@"] // No effect
    },
    /* OR */
    {
      "selector": "img",
      "mergeType": "over",
      "hash": "sha256", // Merged
      "attributes": { "loading": "lazy", "alt": "Picture 2" }, // Merged as "Picture 2"
      "commands": ["jpeg@"] // All images will be JPEG
    },
    /* OR */
    {
      "selector": "img",
      "mergeType": "none",
      "hash": "sha256", // No effect
      "attributes": { "alt": "Picture 1" }, // No effect
      "commands": ["jpeg@"] // No effect
    }
  ]

.. _document-miscellaneous-image-dimensions:

Image dimensions
================

.. rst-class:: miscellaneous-image

=============================== ==== === === ==== === ==== === === ==== ==== ====
 NPM                            JPEG GIF PNG WebP BMP TIFF PSD ICO AVIF HEIC HEIF
=============================== ==== === === ==== === ==== === === ==== ==== ====
image-size [#]_                   x   x   x    x   x    x   x   x    x    x    x
probe-image-size [#]_             x   x   x    x   x    x   x   x    x    x    x
:doc:`jimp </image/index>` [#]_   x   x   x        x    x
=============================== ==== === === ==== === ==== === === ==== ==== ====

.. attention:: Element **width** OR **height** including **max-width** :alt:`(px)` AND **max-height** :alt:`(px)` being set will not be processed due to the likeliness of distortion.

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
  :caption: *http://localhost:3000/project/index.html?className=active*

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

.. _document-miscellaneous-manifest:

Manifest
========

The web app manifest [#]_ is downloaded by default and possibly modified when searching for embedded image assets::

  {
    "icons": [],
    "shortcuts": [{ "icons": [] }],
    "screenshots": []
  }

.. tip:: Image compression is supported.

It is not integrated with the *NodeJS* build system and the images might not appear as expected due to URL rewriting. You can disable this behavior by using either command::

  {
    "selector": "link[rel=manifest]",
    "download": false
  }

.. code-block:: html
  :caption: Inline

  <head>
    <link rel="manifest" href="/manifest.json" data-chrome-file="ignore">
  </head>

squared
=======

.. versionadded:: 5.2.0

  *AssetCommand* property **mergeType** option value "*preserve*" was created.

.. versionadded:: 5.1.5

  *AssetCommand* property **attributes** hash map values can be replaced using search **{{params}}** syntax.

@pi-r/chrome
============

.. versionadded:: 0.6.4

  *NPM* package **image-size** is optionally supported for image dimensions.

.. [#] When using server hosted directory based sqd.config.
.. [#] npm i image-size
.. [#] npm i probe-image-size
.. [#] Jimp is not recommended for detecting image dimensions.
.. [#] https://web.dev/articles/add-manifest