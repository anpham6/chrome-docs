=====
Image
=====

- https://jimp-dev.github.io/jimp
- **npm** i *@pi-r/jimp* :alt:`(0.x)`
- **npm** i *@pi-r2/jimp* :alt:`(1.x)`

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
          "rotate_clockwise": false,
          "cache_expires": "1w",
          "gifwrap_quantize": "none",
          /* 1.x */
          "options": {
            "decode": {
              "image/jpeg": { // @jimp/js-jpeg{DecodeJpegOptions}
                "colorTransform": true,
                "formatAsRGBA": true
              }
            },
            "encode": {
              "image/jpeg": { // @jimp/js-jpeg{JPEGOptions}
                "quality": 75
              }
            }
          },
          "worker": { // Settings will override process.env
            "min": 2, // PIR2_JIMP_WORKER_MIN
            "max": 8, // PIR2_JIMP_WORKER_MAX
            "expires": "1m" // PIR2_JIMP_WORKER_TIMEOUT
          }
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

.. rst-class:: center-data

====== === ===
Format 0.x 1.x
====== === ===
png    r/w r/w
jpeg   r/w r/w
bmp    r/w r/w
gif    r   r/w
tiff   r   r/w
====== === ===

WebP
----

.. rst-class:: center-data

========== = = ==================== ========== =======
Library    R W         NPM           CJS [#]_    ESM
========== = = ==================== ========== =======
dwebp      x   dwebp-bin [#webp]_   1.0.0       2.0.0
cwebp        x cwebp-bin [#webp]_   6.0.0       8.0.0
gif2webp     x gif2webp-bin         3.0.0       5.0.0
webpmux    x x node-webpmux         3.2.0       3.2.0
========== = = ==================== ========== =======

There can be transparency issues for *WebP* animated transformations due to the *WebP* compression algorithm. **node-webpmux** is used to extract the raw data from the *WebP* image and to reconstruct the frames.

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
* ( width(:lower:`n|auto`) x height(:lower:`n|auto`) [:lower:`bilinear|bicubic|hermite|bezier|nearest|none`]? ^(:lower:`cover|contain|scale`)?[:lower:`left|center|right|top|middle|bottom`]? #background-color? )
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

0.x and 1.x
-----------

Methods in *italic* are ``0.x`` only.

.. list-table::
  :width: 600px
  :widths: 25 8 25 8 25 8

  * - autocrop
    - **au**
    - background
    - **bg**
    - *backgroundQuiet*
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
    - *colorType*
    - **ce**
  * - composite [#]_
    - **cp**
    - contain [#]_
    - **ct**
    - contrast
    - **cn**
  * - convolute
    - **cl**
    - convolution
    - **cu**
    - cover
    - **cv**
  * - crop
    - **cr**
    - *cropQuiet*
    - **cq**
    - *deflateLevel*
    - **dl**
  * - displace
    - **dp**
    - *dither565*
    - **dt**
    - fade
    - **fa**
  * - *filterType*
    - **ft**
    - *fishEye*
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
    - *mirror*
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
    - *rgba*
    - **rg**
  * - rotate
    - **ro**
    - scale
    - **sc**
    - scaleToFit
    - **sf**
  * - sepia
    - **se**
    - *shadow*
    - **sh**
    - threshold
    - **th**

1.x only
--------

.. list-table::
  :width: 600px
  :widths: 25 8 25 8 25 8

  * - dither
    - **dt**
    - fisheye
    - **fe**
    - quantize
    - **qu**

Behavior differences
====================

================ ========= =======
 Command         0.x       1.x
================ ========= =======
ResizeStrategy   nearest   none
Workers          none      0.2.0
DecodeOptions    none      0.2.0
EncodeOptions    none      0.2.0
================ ========= =======

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

.. code-block:: html
  :caption: Workers (timeout 10s) [#v1]_

  <img src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/12005/harbour1.jpg"
       data-chrome-file="saveAs:images/harbour.png"
       data-chrome-commands="png@!sepia{45}"
       data-chrome-options='{ "worker": 10000 }'>

.. tip:: Multiple transformations use "**::**" as the separator.

Transformations are given a *UUID* filename except when "**@**" or "**%**" are used. Leaving **data-chrome-file** empty will save the transformations to the current image directory.

@pi-r/jimp
==========

.. versionadded:: 0.10.0

  - *Jimp* rotate strategy mode **nearest** | **none** were implemented.

.. versionchanged:: 0.9.4

  - *NPM* binaries for **WebP** :alt:`(ESM)` are supported.

.. versionadded:: 0.8.1

  - *ImageModule* settings property **jimp.gifwrap_quantize** was implemented using these method types:

    .. hlist::
      :columns: 4

      - :target:`sorokin`
      - wu
      - dekker
      - none

@pi-r2/jimp
===========

.. versionadded:: 0.2.0

  - *ImageModule* settings **jimp.options** for MIME-based decode and encode optimizations was implemented.
  - Workers :alt:`(experimental)` for native Jimp commands was implemented. [#]_
  - *ImageModule* settings **jimp.worker** for available threads was implemented.
  - *NPM* binaries for **WebP** :alt:`(ESM)` are supported.

.. versionadded:: 0.1.0

  - Experimental package for the ``1.x`` releases was created.

.. [#webp] https://developers.google.com/speed/webp/download
.. [#v1] Jimp 1.x
.. [#] Until: pi-r 0.9.4 | pi-r2 0.2
.. [#] cwebp options: -q -preset -near_lossless
.. [#] Method with no arguments. (e.g. sepia)
.. [#] No expressions or native objects.
.. [#] https://jimp-dev.github.io/jimp/api/jimp/classes/jimp
.. [#] srcOver | dstOver | multiply | add | screen | overlay | darken | lighten | hardLight | difference | exclusion
.. [#] left - 1 | center - 2 | right - 4 | top - 8 | middle - 16 | bottom - 32
.. [#] Limitations: Methods with 0 arguments + 1 rotation only + Native read/write