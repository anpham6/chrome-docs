==========
Attributes
==========

There are possible scenarios when a transformation into another format will require new attribute values. [#]_

.. highlight:: html

::

  <link rel="alternate" type="text/plain" href="css/dev.sass" />

.. code-block:: json
  :caption: JSON

  {
    "selector": "link[rel=alternate]",
    "type": "css",
    "filename": "prod.css",
    "download": true, // Required when rel="alternate"
    "hash": "md5", // prod-8ba5cde2c04d6628dd6b0d62b0a3cac9.css
    "attributes": {
      "rel": "stylesheet",
      "type": "text/css",
      "title": "",
      "disabled": null,
      /* SRI */
      "integrity": "sha512", // CORS required (sha256 | sha384 | sha512)
      "crossorigin": "anonymous"
    },
    "process": ["compile"]
  }

.. code-block::
  :caption: Inline

  <link rel="alternate" type="text/plain" href="css/dev.sass" data-chrome-file='{ "saveAs": "css/prod.css", "process": ["compile"] }' data-chrome-attributes='{ "rel": "stylesheet", "type": "text/css", "title": "", "disabled": null, "integrity": "sha512", "crossorigin": "anonymous" }' data-chrome-options="download" />

.. code-block::
  :caption: Output

  <link rel="stylesheet" type="text/css" title="" disabled href="css/prod.css" integrity="sha512-365M9279XHmH5iUcnWAVLXbLCqmntex51g5yp+jrzci79PhUOZyK/ebMIzoR46y7okDgZYZhTImDt7/06IhxQw==" crossorigin="anonymous" />

You can also use the workspace feature in `squared-express <https://github.com/anpham6/squared-express#readme>`_ to precompile any text format and stream the transformed output directly into the source.

.. [#] Setting an attribute to "undefined" will remove it from the HTML output.