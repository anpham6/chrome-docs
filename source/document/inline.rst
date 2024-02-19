===============
Inline commands
===============

Bundles can be created with these HTML tag names.

- **saveAs**: html + script + link + raw assets
- **exportAs**: script + style
- **exclude**: script + link + style

JS and CSS files with the same path and filename will automatically create a bundle when there are no conflicts in call ordering. [#]_

data-chrome-file
================

1. path/filename
    a. saveAs [#]_
    b. exportAs
2. ``::``
3. format... [#]_

.. highlight:: html

.. code-block::
  :caption: JSON [#]_

  <style data-chrome-file='{ "exportAs": "css/prod.css", "process": ["lint", "beautify"] }'>
    body {
      font: 1em/1.4 Helvetica, Arial, sans-serif;
      background-color: #fafafa;
    }
  </style>

.. code-block::
  :caption: Inline

  <link rel="stylesheet" href="css/dev.css" data-chrome-file="saveAs:css/prod.css::lint+beautify" />

.. code-block::
  :caption: Output

  <link rel="stylesheet" href="css/prod.css" />

data-chrome-options
===================

* preserve [#]_
    - html
    - css
* inline
    - js: Rendered inline with <script>
    - css: Rendered inline with <style>
    - image: Rendered as base64 from file
* module [#]_
    - js: ESM
    - css: SASS
* extract
    - css: @import rules are inlined into parent file (same origin)
* blob
    - image: HTML and CSS from base64
    - font: CSS from base64
* dynamic
    - image: "srcset" uses query parameters with an image resizer
    - element (non-void): mixed content which uses a view engine template (e.g. ejs)
* compress (array)
    - image: imagemin [#]_
    - font: woff + woff2
    - png: TinyPNG service (jpeg + webp)
    - gz: Gzip + Zopfli
    - br: Brotli
* static
    - all: Remove query string from URL
* crossorigin
    - all: Same as preserveCrossOrigin [download: false]
* download [#]_
    - all: Source files that are not usually downloaded (e.g. link[rel=alternate])
* hash [#]_ [#]_
    - js
    - css
    - map
    - img
    - font
    - audio
    - video
* remove
    - all: Remove element during finalization
* charset (string)
    - utf-8 (default)
    - utf-16
    - utf-16le
    - latin1
    - utf-16be (unsupported)

.. code-block::
  :caption: JSON

  <style data-chrome-options='{ "preserve": true, "hash": "md5", "compress": [{ "format": "gz", "algorithm": "zopfli", "level": 15 }], "encoding": "utf-16" }'>
    body {
      font: 1em/1.4 Helvetica, Arial, sans-serif;
      background-color: #fafafa;
    }
  </style>

.. code-block::
  :caption: Inline

  <link rel="stylesheet" href="css/dev.css" data-chrome-options="preserve|md5|compress[gz]|utf-16">

.. tip:: Whitespace can be used between anything for readability.

data-chrome-metadata
====================

.. code-block::
  :caption: Any plain object

  <script src="/dist/squared.js" data-chrome-metadata='{ "rollup-custom": { "import-maps": {} }, "terser-custom": { "config": {} } }'></script>

Inline commands are usually sufficient for simple web pages. More advanced configurations are possible using a JSON/YAML external configuration file.

.. code-block:: json

  {
    "selector": "head > script:nth-of-type(2), head > script:nth-of-type(3)",
    "type": "js",
    "saveAs": "js/modules2.js",
    "process": ["minify"],
    "metadata": { "custom-prop": true }
  }

.. [#] MIME (mimeType) is required when bundling torrents.
.. [#] Use "~" for current path and filename. 
.. [#] Multiple transformations per bundle can be chained using the "+" symbol.
.. [#] <style data-chrome-file='"exportAs": "css/prod.css", "process": ["lint", "beautify"]'></style>
.. [#] Do not use the built-in transformers per document.
.. [#] "true" | "false" - config | "no-module" - inline
.. [#] Optionally installed NPM plugins are required. (e.g. imagemin-pngquant)
.. [#] "true" - explicit | "false"
.. [#] filename + content hash (productionRelease=true)
.. [#] Value can be limited to the starting prefix. (e.g. md5[8] - Minimum is 4)