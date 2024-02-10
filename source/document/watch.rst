=====
Watch
=====

File watching is available with **copy** methods and uses HTTP HEAD requests to determine modifications. You can watch any file served with HTTP including files from another server.

Hot module replacement is only available for ``<link>`` and ``<img>`` elements. It is disabled by default due to possible conflicts with preloaded JavaScript.

Using JSON config [#]_
======================

::

  {
    "selector": "link",
    "type": "css", // html | js | image
    "watch": {
      "interval": 100, // Time between HTTP requests (ms)
      "interval": "1m",
      "start": "Dec 7, 2023 5:00:00 PM", // Empty is immediate
      "expires": "1w 1d 1h 1m 1s", // Empty is never (includes "start")
      "main": false // Will rebuild the entire bundle
      "id": "watch1", // Resets an existing watch when it is the first active socket
      "reload": true, // Uses server defaults
      /* OR */
      "reload": {
        "socketId": "111-111-111", // Use same id to reload multiple pages
        "port": 80,
        "secure": false, // Requires TLS/SSL key and cert
        "module": false, // "img" and "link" only
        "always": false // Ignore errors
      }
    },
    "process": [
      "bundle",
      "lint",
      "minify"
    ]
  }

Using copyTo options
====================

.. code-block:: javascript

  squared.copyTo("/local/user/www", {
    watch: true,
    saveAs: {
      script: {
        pathname: "../js",
        process: ["es5", "es5-minify"],
        watch: true
      },
      link: {
        pathname: "css",
        filename: "bundle.css",
        watch: { interval: 500 }
      }
    }
  });

Using JWT authentication
========================

::

  {
    "watch": {
      "settings": {
        "users": {
          "username": {
            "http://localhost:3000/index.html": { "interval": 100 }, // Order of precedence
            "http://localhost:3000/**/*": {/* Same */},
            "/path/to/project/file": {/* Same */}, // Local
            "/path/to/project/**/*": {/* Same */},
            "image/png": {/* Same */}, // MIME
            "image/*": {/* Same */}
          }
        }
      }
    }
  }

.. code-block:: javascript

  squared.auth('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...');
  squared.copyTo("/local/user/www", {
    watch: true,
    saveAs: {
      script: { watch: true }
    }
  });

data-chrome-watch
=================

.. code-block:: html

  <link rel="stylesheet" href="/common/util.css" data-chrome-watch="1000::1h 30m::111-111-111:8080[module|secure|always]">
  <!-- OR -->
  <link rel="stylesheet" href="/common/util.css" data-chrome-watch="~::~::[secure|always]">

  <script src="/common/util.js" data-chrome-watch='{ "interval": 100, "expires": "1w 1d 1h 1m 1s", "reload": { "port": 443, "secure": true } }'></script>

.. tip:: "**~**" can be used with "**::**" for default server value.

Options
=======

useOriginalHtmlPage = true
--------------------------

HTML only has partial watch support since most local modifications will alter the original element index position stored on the server.

- script + link -> Inside source file
- script + style (inline) -> Unbundled
- elements (configured + data source) -> Uneditable

If you configure an ``<img>`` tag (or any tag group) then you cannot add or remove other ``<img>`` elements without adding an element "**id**" to every element in the group.

.. [#] YAML config is also available.