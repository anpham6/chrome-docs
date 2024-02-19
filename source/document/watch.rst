=====
Watch
=====

File watching is available with **copy** methods and uses HTTP HEAD requests to determine modifications. You can watch any file served with HTTP including files from another server.

Hot module replacement is only available for ``<link>`` and ``<img>`` elements. It is disabled by default due to possible conflicts with preloaded JavaScript.

Using JSON config
=================

::

  {
    "selector": "link",
    "type": "css", // html | js | image
    "watch": {
      "interval": 100, // Time between HTTP requests (ms)
      "interval": "1m",
      "start": "Apr 29, 2024 5:00:00 PM", // Empty is immediate
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
  :caption: JSON [#]_

  <script
    src="/common/util.js"
    data-chrome-watch='{ "interval": 100, "expires": "1w 1d 1h 1m 1s", "reload": { "port": 443, "secure": true } }'>
  </script>

.. code-block:: html
  :caption: interval `::` expires `::` reload

  <link rel="stylesheet" href="/common/util.css" data-chrome-watch="1000::1h 30m::111-111-111:8080[module|secure|always]">

.. code-block:: html
  :caption: Settings

  <link rel="stylesheet" href="/common/util.css" data-chrome-watch="~">
  <!-- OR -->
  <link rel="stylesheet" href="/common/util.css" data-chrome-watch="~::~::[secure|always]">

.. tip:: "**~**" can be used between "**::**" for default server value.

Build Options
=============

useOriginalHtmlPage = true
--------------------------

HTML only has partial watch support since most local modifications will alter the original element index position stored in memory. Inline source ``<script>`` and ``<style>`` cannot be edited when they are part of a bundle.

Elements that are configured (e.g. dataSource) are not editable as the original request values will be used on a reload.

::

  {
    "selector": "p",
    "attributes": {
      "class": "active"
    }
  }

.. code-block:: html
  :caption: Source

  <p>content</p>

.. code-block:: html
  :caption: Build output

  <p class="active">content</p>

.. code-block:: html
  :caption: Edit source

  <p class="inactive" style="display: none;">content</p>

.. code-block:: html
  :caption: Watch output

  <p class="active" style="display: none;">content</p>

.. attention:: If you configure an ``<img>`` tag (or any tag group) then you cannot add or remove other ``<img>`` elements without adding an element "**id**" to every element in the group.

.. [#] data-chrome-watch='*"interval": 100, "expires": "1w 1d 1h 1m 1s", "reload": { "port": 443, "secure": true }*'