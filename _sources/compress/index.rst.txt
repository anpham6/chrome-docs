========
Compress
========

Tinify
======

- https://tinypng.com/developers
- **npm** i *@pi-r/tinify*

*TinyPNG* is a web service for image compression. The first 500 images are free each month with a developer API key.

.. code-block::
  :caption: squared.json

  {
    "compress": {
      "tinify": {
        "api_key": "**********", // Default API key (optional)
        "proxy": "",
        "expires": "1h"
      },
      "settings": {
        "tinify_api_key": "**********" // Alternate
      }
    }
  }

::

  {
    "selector": "p > img",
    "compress": [
      {
        "format": "png", // png | jpeg | webp
        "plugin": "tinify",
        "options": {
          "apiKey": "**********", // Overrides settings
          "expires": "30m" // Caches validation for multiple transactions
        }
      }
    ]
  }

Imagemin
========

- https://github.com/imagemin/imagemin
- **npm** i *@pi-r2/imagemin*

Images are transcoded locally using *MIME* detection to automatically choose the appropriate plugin. 

.. code-block::
  :caption: squared.json

  {
    "compress": {
      "imagemin": {
        "mozjpeg": {/* default */}, // https://npmjs.com/package/imagemin-mozjpeg#api
        "jpegtran": null, // https://npmjs.com/package/imagemin-jpegtran#api
        "pngquant": {/* default */}, // https://npmjs.com/package/imagemin-pngquant#api
        "optipng": null, // https://npmjs.com/package/imagemin-optipng#api
        "webp": {/* default */}, // https://npmjs.com/package/imagemin-webp#api
        "gifsicle": {/* default */}, // https://npmjs.com/package/imagemin-gifsicle#api
        "svgo": {/* default */} // https://npmjs.com/package/imagemin-svgo#api
      }
    }
  }

.. note:: Any ``null`` values being truthy will override the default transformer when "**metadata.package**" [#]_ is ``undefined``.

::

  {
    "selector": "p > img",
    "compress": [
      {
        "format": "png", // Recommended
        "plugin": "imagemin",
        "worker": true, // Experimental
        "options": {
          "speed": 11, // imagemin-pngquant (default)
          "quality": [0.3, 0.5]
        }
      },
      {
        "format": "png",
        "plugin": "imagemin",
        "metadata": {
          "package": "imagemin-optipng", // Alias "optipng"
          "mimeType": "image/png" // Optional (auto-detect)
        },
        "options": {
          "optimizationLevel": 7,
          "interlaced": true
        }
      }
    ]
  }

.. caution:: When *format* is not defined the plugin will be applied to all images. Multiple plugins of the same *MIME* will be processed in a series.

Other formats can be compressed similarly using *imagemin-like* plugins directly.

::

  {
    "selector": "p > img",
    "compress": [
      {
        "format": "png",
        "plugin": "imagemin-gif2webp", // npm i imagemin-gif2webp
        "options": {
          "lossy": true,
          "quality": 75
        }
      },
      /* OR */
      {
        "format": "png",
        "plugin": "imagemin",
        "metadata": {
          "package": "imagemin-gif2webp" // With settings "gif2webp"
        }
      }
    ]
  }

.. important:: Settings are used only when **options** is ``undefined``.

Environment Variables
=====================

============================ =======
 Name                         Value
============================ =======
EMC_COMPRESS_WORKER_MIN      number
EMC_COMPRESS_WORKER_MAX      number
EMC_COMPRESS_WORKER_TIMEOUT  minute
============================ =======

.. [#] Metadata interface is plugin independent.