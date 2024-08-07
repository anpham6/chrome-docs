=====
Image
=====

- https://github.com/jimp-dev/jimp#readme
- **npm** i *@pi-r/jimp*
- **npm** i *@pi-r/tinify* :alt:`(Optional)`

.. note:: *Jimp* is used as the reference implementation for an **Image** module.

Example configuration
=====================

.. code-block::
  :caption: squared.json

  {
    "image": {
      "handler": "@pi-r/jimp",
      "webp": "webp-custom", // IImage handler for "image/webp" (npm i webp-custom)
      "avif": "avif-custom", // IImage handler for "image/avif" (npm i avif-custom)
      "settings": {
        "jimp": {
          "rotate_clockwise": false
        },
        "webp": {
          "path": "/path/to/libwebp" // Optional
        }
      }
    }
  }

.. tip:: *Jimp* rotation is counter-clockwise. Use **{-45}** to achieve a *45-degree* clockwise rotation.

Image conversion can be achieved using the ``commands`` array property in a :ref:`FileAsset <references-squared-base-file>` object.

::

  {
    "selector": "p > img",
    "saveTo": "/static/generated", // Does not replace original image
    "commands": [
      "png(800x600){45}", // width: 800px; height: 600px; rotate: 45deg;
      "jpeg(50,50)!sepia" // left: 50px; top: 50px; method: sepia;
    ]
  }

Supported formats
=================

.. rst-class:: image-format

====== = =
Format R W
====== = =
png    x x
jpeg   x x
webp   x x
bmp    x x
gif    x x
tiff   x 
====== = =

WebP
----

.. rst-class:: image-format

======== = = ============
Library  R W     NPM
======== = = ============
dwebp    x   dwebp-bin [#webp]_
cwebp      x cwebp-bin [#webp]_
gif2webp   x gif2webp-bin
webpmux  x x node-webpmux
======== = = ============

There can be transparency issues for *WebP* animated transformations due to the *WebP* compression algorithm. **node-webpmux** is only used to extract the raw data from the *WebP* image and to reconstruct the frames.

.. note:: **libwebp** [#webp]_ is supported locally for *WebP* transforms through ``settings.webp.path``.

Command syntax
==============

Placing an "**@**" symbol after the **format** :alt:`(e.g. png@)` will replace the original file inside the project. Using the "**%**" symbol will choose the smaller of the two files.

All segments are optional except **format**. Outer groupings and inner brackets are required.

- :target:`format`

.. rst-class:: compressed

* \| *choose one* \|
    * **@**
    * **%**
* ~size(:lower:`n`)(:lower:`w|x`) :alt:`(chrome only)`
* ( minSize(:lower:`n,0`) , maxSize(:lower:`n,*`)? )
* ( width(:lower:`n|auto`) x height(:lower:`n|auto`) [:lower:`bilinear|bicubic|hermite|bezier`]? ^(:lower:`cover|contain|scale`)?[:lower:`left|center|right|top|middle|bottom`]? #background-color? )
* ( left(:lower:`+|-n`) , top(:lower:`+|-n`) | cropWidth(:lower:`n`) x cropHeight(:lower:`n`) )
* { ...rotate(:lower:`n|-n`) #background-color? }
* \| *choose one* \|
    * opacity(:lower:`0.0-1.0`)
    * jpeg_quality(:lower:`0-100`)
    * webp_quality(:lower:`0-100?[photo|picture|drawing|icon|text]?[0-100]?`) [#]_
* !method [#]_
* !method(:lower:`1, "string_arg2", [1, 2], true, { "a": 1, "b": "\\}" }, ...args?`) [#]_

Example commands
================

Methods use simple bracket matching and does not fully check inside quoted strings. Unescaped "**\\\\**" with unpaired ("**{}**" or "**[]**") will fail to parse.

.. code-block:: none

  webp(50000)(800x600[bezier]^contain[right|bottom]#FFFFFF)(-50,50|200x200){45,-45,215,315#FFFFFF}|0.5||100[photo][75]|!sepia

  webp!opacity(0.5)
  webp!op(0.5)

  webp~800w(800x600)
  webp~2x(1024x768)

.. tip:: The "**~**" is used to target the ``<img srcset>`` attribute.

Method aliases [#]_
===================

.. list-table::
  :widths: 25 8 25 8 25 8

  * - autocrop
    - **au**
    - background
    - **bg**
    - backgroundQuiet
    - **bq**
  * - blit
    - **bt**
    - blur
    - **bl**
    - brightness
    - **br**
  * - circle
    - **ci**
    - color
    - **co**
    - colorType
    - **ce**
  * - composite [#]_
    - **cp**
    - contain [#]_
    - **ct**
    - contrast
    - **cn**
  * - convolute
    - **cl**
    - cover
    - **cv**
    - crop
    - **cr**
  * - cropQuiet
    - **cq**
    - deflateLevel
    - **dl**
    - deflateStrategy
    - **ds**
  * - displace
    - **dp**
    - dither565
    - **dt**
    - fade
    - **fa**
  * - filterType
    - **ft**
    - fishEye
    - **fe**
    - flip
    - **fl**
  * - gaussian
    - **ga**
    - greyscale
    - **gr**
    - invert
    - **in**
  * - mask
    - **ma**
    - mirror
    - **mi**
    - normalize
    - **no**
  * - opacity
    - **op**
    - opaque
    - **oq**
    - pixelate
    - **px**
  * - posterize
    - **po**
    - resize
    - **re**
    - rgba
    - **rg**
  * - rotate
    - **ro**
    - scale
    - **sc**
    - scaleToFit
    - **sf**
  * - sepia
    - **se**
    - shadow
    - **sh**
    - threshold
    - **th**

Compression
===========

`Tinify <https://tinypng.com/developers>`_ web service is used for image compression [#]_. The first 500 images are free each month with a developer API key.

.. code-block::
  :caption: squared.json
  
  {
    "compress": {
      "tinify": {
        "api_key": "**********", // Default API key (optional)
        "proxy": ""
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
          "apiKey": "**********" // Overrides settings
        }
      }
    ]
  }

Other formats can be compressed similarly using `imagemin <https://github.com/imagemin/imagemin#readme>`_.

::

  {
    "selector": "p > img",
    "compress": [
      {
        "format": "png",
        "plugin": "imagemin-pngquant", // npm i imagemin-pngquant
        "options": {
          "quality": [0.6, 0.8]
        }
      }
    ]
  }

When *format* is not defined the plugin will be applied to all images. [#]_ Multiple plugins of the same *MIME* will be processed in a series.

data-chrome-commands
====================

.. code-block:: html
  :caption: img | video | audio | source | track | object | embed | iframe

  <img src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/12005/harbour1.jpg"
       data-chrome-file="saveAs:images/harbour.webp"
       data-chrome-options="inline"> <!-- data:image/webp;base64 -->

You can use image commands with **saveTo** (directory) on any element where the image is the primary display output.

.. code-block:: html
  :caption: img | object | embed | iframe

  <img src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/12005/harbour1.jpg"
       data-chrome-file="saveTo:../images/harbour"
       data-chrome-commands="png(10000,75000)(800x600[bezier]^contain[right|bottom])::webp|0.5|">

.. tip:: Multiple transformations use "**::**" as the separator.

Transformations are given a *UUID* filename except when "**@**" or "**%**" are used. Leaving **data-chrome-file** empty will save the transformations to the current image directory.

@pi-r/jimp
==========

.. versionadded:: 0.8.1

  - *ImageModule* settings property **jimp.gifwrap_quantize** [#]_ was implemented using these method types:

    .. hlist::
      :columns: 4

      - :target:`sorokin`
      - wu
      - dekker
      - none

.. [#webp] https://developers.google.com/speed/webp/download
.. [#] cwebp options: -q -preset -near_lossless
.. [#] Method with no arguments. (e.g. sepia)
.. [#] No expressions or native objects.
.. [#] https://github.com/jimp-dev/jimp/tree/main/packages/jimp#methods
.. [#] srcOver | dstOver | multiply | add | screen | overlay | darken | lighten | hardLight | difference | exclusion
.. [#] left - 1 | center - 2 | right - 4 | top - 8 | middle - 16 | bottom - 32
.. [#] png | jpeg | webp
.. [#] e-mc 0.10
.. [#] https://github.com/jimp-dev/gifwrap#GifUtil.quantizeDekker