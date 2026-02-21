===============
Inline commands
===============

Bundles can be created with these *HTML* tag names.

- **saveAs**: html + script + link + raw assets
- **exportAs**: script + style
- **exclude**: script + link + style

*JS* and *CSS* files with the same path and filename will automatically create a bundle when there are no conflicts in call ordering. [#]_

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
  :caption: Key-Value [#v523]_

  <link rel="stylesheet" href="css/dev.css" data-chrome-file='saveAs: css/prod.css; process: ["lint", "beautify"]' />

.. code-block::
  :caption: Inline (legacy)

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
    - js: Rendered inline with **<script>**
    - css: Rendered inline with **<style>**
    - image: Rendered as base64 from file
* module [#]_
    - js: ESM
    - css: SASS
* incremental [#v523]_
    - boolean
    - none
    - staging
    - etag
    - exist
* extract
    - css: @import rules are inlined into parent file :lower:`(same origin)`
* blob
    - image: HTML and CSS from **base64**
    - font: CSS from **base64**
* dynamic
    - image: "srcset" uses query parameters with an image resizer
    - element :lower:`(non-void)`: mixed content which uses a view engine template :alt:`(e.g. ejs)`
* compress (array)
    - image: tinify + imagemin [#]_
    - font: woff + woff2
    - gz: Gzip
    - br: Brotli
* static
    - all: Remove query string from URL
* crossorigin
    - all: Same as preserveCrossOrigin :lower:`[download: false]`
* download [#]_
    - all: Source files that are not usually downloaded :alt:`(e.g. link[rel=alternate])`
* hash [#]_ [#]_
    - js
    - css
    - map
    - img
    - font
    - audio
    - video
* worker
    - image
    - font
* remove
    - all: Remove element during finalization
* charset :lower:`(string)`
    - utf-8 :lower:`(default)`
    - utf-16
    - utf-16le
    - latin1
    - utf-16be :lower:`(unsupported)`

.. code-block::
  :caption: JSON [#]_

  <style data-chrome-options='{ "preserve": true, "hash": "md5", "compress": [{ "format": "gz" }], "incremental": "etag", "encoding": "utf-16" }'>
    body {
      font: 1em/1.4 Helvetica, Arial, sans-serif;
      background-color: #fafafa;
    }
  </style>

.. code-block::
  :caption: Key-Value [#]_

  <link rel="stylesheet" href="css/dev.css" data-chrome-options='preserve: true; hash: md5; compress: [{ "format": "gz" }]; incremental: etag; encoding: utf-16; }' />

.. code-block::
  :caption: Inline (legacy)

  <link rel="stylesheet" href="css/dev.css" data-chrome-options="preserve|md5|compress[gz]|incremental[etag]|utf-16">

.. tip:: Whitespace can be used between anything for readability.

data-chrome-metadata
====================

.. code-block::
  :caption: Any plain object [#]_

  <script
    src="/common/util.js"
    data-chrome-metadata='{ "rollup-custom": { "import-maps": {} }, "terser-custom": { "config": {} } }'>
  </script>

Inline commands are usually sufficient for simple web pages. More advanced configurations are possible using a JSON :alt:`(yaml)` external configuration file.

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
.. [#] data-chrome-file='*"exportAs": "css/prod.css", "process": ["lint", "beautify"]*'
.. [#] Do not use the built-in transformers per document.
.. [#] boolean - config | "no-module" - inline
.. [#] @pi-r/tinify | @pi-r2/imagemin
.. [#] "true" - explicit | "false"
.. [#] filename + content hash (productionRelease=true)
.. [#] Value can be limited to the starting prefix. (e.g. md5[8] - Minimum is 4)
.. [#] data-chrome-options='*"preserve": true, "hash": "md5", "compress": [{ "format": "gz" }], "encoding": "utf-16"*'
.. [#] Nested objects and arrays use strict JSON formatted attributes and strings.
.. [#] data-chrome-metadata='*"rollup-custom": { "import-maps": {} }, "terser-custom": { "config": {} }*'
.. [#v523] squared 5.2.3 (minimum)