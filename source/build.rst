=============
Build Options
=============

General processing options use **E-mc** functionality with :external+android:doc:`squared-express <document/build>`.

.. attention:: These examples are only relevant to the :target:`chrome` framework.

Example usage
=============

.. highlight:: javascript

.. code-block::

  squared.saveAs("index.zip", {
    productionRelease: true, // Ignore local URL rewriting and use actual path
    productionRelease: "/path/to/wwwroot/", // Move assets outside base directory to server root directory
    serverRootMapping: {
      "images/": "common/images", // output/images/ -> /path/to/wwwroot/common/images/ (move - no trailing slash)
      "images/png/": "main/data/" // output/images/png/ -> /path/to/wwwroot/main/data/images/png/ (append)
    },
    productionIncremental: true, // Use cached data when processing transformed files

    preserveCrossOrigin: true, // Ignore local assets hosted on other domains
    preserveCrossOrigin: { // URL class attributes
      hostname: "docs.github.com",
      pathname: "/repositories"
    },

    useOriginalHtmlPage: false, // Use browser validated in memory static page DOM for build
    useOriginalHtmlPage: "textarea|code", // Ignore tags causing parsing errors

    useUnsafeReplace: "html", // Use when there are no element tags inside comments and <script>
    useUnsafeReplace: "css", // Use when there are no comments or block delimiters inside property values (e.g. "{" "}")
    useUnsafeReplace: true, // Alias for ["html", "css"]

    stripCommentsAndCDATA: true, // Remove unused code and non-void tags from HTML
    stripCommentsAndCDATA: "script|picture", // Additional tags to remove using RegExp group notation

    /* Use when there are parsing errors */
    normalizeHtmlOutput: true, // Escape illegal tags and remove unnecessary trailing spaces
    normalizeHtmlOutput: "?%", // Tags to ignore using RegExp negated characters when escaping (e.g. <?php ?> | <%= ejs %>)

    escapeReservedCharacters: true, // Escape reserved characters inside attributes (e.g. "<")
    ignoreServerCodeBlocks: ["<%", "%>", "<?php", ";", "<?php", "?>"], // May produce better results with dynamic content (<% %> | <?php ; | <?php ?>)
    sanitizeFramework: ["*", "android"], // Remove global and android dataset UI attributes

    removeBinaries: false, // Remove all script tags with src="squared.js"

    removeInlineStyles: false, // Strip style="" attribute from all elements (useOriginalHtmlPage=false)
    removeUnusedClasses: false, // Selectors without :pseudo-class
    removeUnusedPseudoClasses: false, // Selectors with :pseudo-class (lowercase only)
    removeUnusedVariables: false, // --custom-variables
    removeUnusedFontFace: false, // @font-face
    removeUnusedKeyframes: false, // @keyframes
    removeUnusedMedia: false, // @media
    removeUnusedSupports: false, // @supports
    removeUnusedContainer: false, // @container
    removeUnusedScope: false, // @scope

    /* Styles which are still being used */
    retainUsedStyles: {
      "selectors": [], // Same without separators
      "variables": [],
      "pseudoClass": false, // Will keep "li a:hover" + "li a:visited" when "li a" is a used selector
      "@font-face": [],
      "@keyframes": [],
      "@media": [],
      "@supports": [],
      "@container": [],
      "@scope": []
    },
    /* OR */
    retainUsedStyles: [
      /* CSS selectors (string | RegExp) */,
      /* CSS variables (string prefixed with '--') */,
      /* CSS @font-face (string enclosed within '|font-face:Times New Roman|') */,
      /* CSS @keyframes (string enclosed within '|keyframes:animationName|') */,
      /* CSS @media (string enclosed within '|media:only screen and (min-width: 800px)|') */,
      /* CSS @supports (string enclosed within '|supports:(display: grid)|') */,
      /* CSS @container (string enclosed within '|container:(min-width: 800px)|') */,
      /* CSS @scope (string enclosed within '|scope:selector-start|') */
    ],

    imports: {
      "http://localhost:3000/build/": "./build", // Starts with "http"
      "http://localhost:3000/dist/chrome.framework.js": "/path/project/build/framework/chrome/src/main.js" // Full file path
    }
  });

.. caution:: Import maps [#]_ are supported from a file system perspective.

Example "saveAs"
================

The entire page can be transformed as a group with the same functionality as JSON :alt:`(yaml)` configuration except where highlighted.

.. code-block::
  :emphasize-lines: 8-9,33

  squared.copyTo("/path/to/target", {    
    saveAs: {
      html: { filename: "index.html", process: ["beautify"], attributes: { lang: "en" } },
      script: {
        pathname: "../js",
        filename: "bundle.js", // Only for first bundle
        process: ["es5", "es5-minify"],
        ignoring: ["text/template"], // MIME types
        inlineAction: false // script + link + image
      },
      link: {
        pathname: "css"
        filename: "bundle.css",
        inline: true,
        preserve: true,
        attributes: { rel: "stylesheet", media: "all" },
        inlineAction: true, // merge + override
        inlineAction: "merge", // { media: "screen" } -> { rel: "stylesheet", media: "screen" }
        inlineAction: "override" // { rel: "alternate" } -> { rel: "alternate" }
      },
      image: {
        attributes: { loading: "lazy", width: "detect", height: "detect" },
        commands: ["webp(480x300)"], // Only valid for binary images
        process: ["minify-svg"], // Only valid for text based images (e.g. SVG)
        worker: 10000 // 10s timeout
      },
      font: {
        pathname: "fonts",
        compress: "woff2", // truetype | opentype | woff | woff2
        blob: false, // Save base64 as file
        blob: "fonts/blob", // Overrides pathname for blob only
        inline: false, // Write file as data:font/ttf;base64
        worker: true,
        customize: (uri, mimeType, command) => { // script | link | image | font
          if (mimeType === "font/ttf") {
            command.blob = true; // Does not alter font object
            return "filename.ttf";
          }
          return ""; // Do not alter filename
          /* OR */
          return null; // Ignore file
        }
      }
    }
  });

.. note:: ``inlineAction`` applies to the entire ``data-chrome-*`` namespace except **data-chrome-file** and **data-chrome-template**.

Example cloud storage
=====================

::

  squared.saveAs("index.zip", {
    config: "http://localhost:3000/chrome/bundle.yml",
    saveAs: {
      html: {
        cloudStorage: [{ // Create static website
          service: "aws-v3",
          bucket: "nodejs-001",
          credential: {
            credentials: {
              accessKeyId: "**********", // Only access key logins are supported with v3
              secretAccessKey: "**********",
              sessionToken: ""
            },
            region: "us-west-2"
          },
          upload: {
            active: true,
            endpoint: "https://nodejs-001.s3.us-west-2.amazonaws.com", // Optional
            overwrite: true
          }
        }]
      },
      image: { // Non-element images using url() method
        cloudStorage: [{
          service: "aws",
          bucket: "nodejs-001",
          settings: "main",
          upload: {
            active: true
          }
        }]
      }
    }
  });

.. tip:: Use "**endpoint**" when your uploaded files are not used by other buckets or web pages.

Example remote configuration
============================

::

  squared.saveAs("bundle.zip", { config: { uri: "http://hostname/chrome/bundle.txt", mimeType: "text/yaml" } }); // "mimeType" is optional
  /* OR */
  squared.saveAs("bundle.zip", { config: "http://hostname/chrome/bundle.yml" }); // Detect by file extension (default is "json")

.. code-block::
  :caption: *http://hostname/pathname/example.html -to- http://hostname/pathname/example.html.json*

  squared.saveAs("example.zip", { config: { mimeType: "json" } });
  /* OR */
  squared.saveAs("example.zip", { config: "json" }); // json | yaml

.. tip:: **JSON5** [#]_ and **TOML** [#]_ file formats are also supported.

Example incremental
===================

Build time during development can be optimized at the global and asset level.

::

  squared.saveAs("example.zip", {
    incremental: false, // Cache is not used (explicit)
    incremental: "none", // Will rebuild all assets and use available cache
    incremental: "staging", // Same as "none" but does not use cache (archive)
    incremental: "etag", // Will use current file found only if the ETag is still the same
    incremental: "exists", // Will always use current file if found at destination

    incrementalMap: {
      pathname: {
        "images/": "exists", // Not recursive
        "js/**": "etag" // Glob is supported
      },
      extension: {
        js: "etag",
        mjs: false
      },
      mime: {
        "image/png": "exists", // First match will quit search
        "image/*": "etag"
      },
      overwrite: false // Only when undefined
    }
  });

.. _build-external-authentication:

External authentication
=======================

Non-JWT access is supported when using **squared-express** [#]_ and `Express 5 <https://expressjs.com>`_. *Firebase* is used as the reference implementation and requires additional configuration.

- **npm** i *firebase* (username|token)
- **npm** i *firebase-admin* (uid|token)

.. code-block:: json
  :caption: squared.auth.json

  {
    "providers": {
      "firebase": { // FirebaseOptions
        "projectId": "squared-123456",", // API Keys (https://console.cloud.google.com/apis/credentials)
        "apiKey": "PbzaryCxqzE2smem1pPzvExwfJRaXA81h0FdB42
        "authDomain": "squared-123456.firebaseapp.com",
        "storageBucket": "squared-123456.appspot.com"
      },
      "firebase-admin": { // ServiceAccount
        "projectId": "squared-123456", // Keys (https://console.cloud.google.com/iam-admin/serviceaccounts/details)
        "privateKey": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBK\n-----END PRIVATE KEY-----\n",
        "clientEmail": "firebase-adminsdk-fbsvc@squared-123456.iam.gserviceaccount.com",
      },
      "firebase-admin": "./cloud/auth/gcp/squared-123456-4e1c2290e638.json",
      "firebase-admin": true, // FIREBASE_CONFIG
      "cognito": "./cloud/auth/aws/cognito.cjs" // User extension method
    },
    "settings": {
      "exclude": {
        "realm": ["firebase-admin"], // Use only username and not domain (e.g. username@domain.com)
        "users": ["osaka"] // Do not permit user "osaka" from authenticating
      }
    }
  }

.. tip:: Use ``squared.auth.cjs`` to define inline asynchronous methods for any authentication provider.

.. code-block::
  :caption: Username

  squared.saveAs("output.zip", {
    auth: {
      username: "mongodb",
      password: "fighters",
      realm: "firebase" // Same as authProvider
    }
  });

.. code-block::
  :caption: Custom JWT token

  squared.saveAs("output.zip", {
    auth: "xxxxx.yyyyy.zzzzz"
    authProvider: "firebase" // Recommended
  });

.. code-block::
  :caption: UID

  squared.saveAs("output.zip", {
    auth: "7EymzDz4X7UJKmDDITeqfZl0nNKv"
    authProvider: "firebase-admin"
  });

.. _build-using-sqd-config:

Using sqd.config
================

The base folder level configuration file is a hash map of URL globs which can match multiple items. Given these two configurations:

.. code-block:: none
  :caption: *http://hostname/path/sqd.config*

  http://hostname/path/example1.html
  http://hostname/path/example2.html

.. code-block:: none
  :caption: *http://hostname/path/sub/sqd.config*

  http://hostname/path/sub/example3.html
  http://hostname/path/sub/example4.html

The hash key ``**/example*\\.html`` will only match either 1 and 2 or 3 and 4.

.. code-block:: json
  :caption: sqd.config

  {
    "111-111-111": [{ "selector": "html", "type": "html" }], // Key

    "/project/example.html*": { // Glob
      "ordinal": 1,
      "useOriginalHtmlPage": true
      "elements": [{
        "selector": "html",
        "type": "html",
        "attributes": { "lang": "en" }
      }]
    },
    "/project/example.html?id=1": {
      "ordinal": 2,
      "elements": [{
        "selector": "html",
        "type": "html",
        "hash": "sha256",
        "attributes": { "lang": "ja", "class": "main" },
        "mergeType": "none", // lang=en
        "mergeType": "under", // hash=sha256,lang=en
        "mergeType": "preserve", // hash=sha256,lang=en,class=main
        "mergeType": "over" // hash=sha256,lang=ja,class=main
      }]
    },

    "example.html?id=1": [{ "selector": "html", "type": "html" }], // "elements"
    "example.html": [{ "selector": "html", "type": "html" }], // Does not match "?id=1"

    "**/*\\.html*": [{ "selector": "html", "type": "html" }], // Glob
    "**/*\\.html\\?id=1": [{ "selector": "html", "type": "html" }] // Ignored without "ordinal" or "inherit"
  }

.. attention:: Escaping **RegExp** special characters :alt:`(e.g. `-|{}()[]^$+\*?.)` is required except when using key match.

Example usage
-------------

The order of precedence when using :target:`inherit` is resolved through the asset command property :ref:`mergeType <document-miscellaneous-merge-conflicts>`.

.. code-block::
  :caption: First glob match

  squared.copyTo("/path/output", { config: true }); // inherit is "false"

.. code-block::
  :caption: Globs are concatenated

  squared.saveAs("output.zip", {
    config: {
      uri: true,
      inherit: true, // Duplicate selectors are replaced
      inherit: "append" // Resolve duplicates with "mergeType"
    }
  });

.. code-block::
  :caption: Hash key

  squared.copyTo("/path/output", {
    config: {
      uri: true,
      key: "111-111-111"
    }
  });

.. tip:: The filename ``sqd.config`` is configurable using **settings.outputConfigName**.

Example data source
-------------------

There is no difference between using :doc:`data sources <document/data>` for a web page and for configuration. *JSON* stored in ``key-value`` document format is the same as unstructured *JSON* stored in a file.

.. code-block::
  :caption: DB

  squared.copyTo("/path/output", {
    config: {
      inherit: {
        preserve: true, // Cascade into all object properties
        append: true, // Concatenate arrays
        depth: 1 // Nested arrays (e.g. "elements")
      },
      document: "chrome", // Required with DB
      dataSource: [{
        source: "redis",
        uri: "redis://redis-6379.redislabs.com:6379",
        username: "squared",
        password: "************",
        key: "config:1",
        format: "JSON"
      },
      {
        source: "redis",
        uri: "redis://redis-6379.redislabs.com:6379",
        username: "squared",
        password: "************",
        key: "config:2",
        format: "JSON"
      }]
    }
  });

.. tip:: When using "**preserve**" the first config is used as the base. Each subsequent config fills :target:`undefined` properties to existing objects and creates new objects.

.. code-block::
  :caption: Cloud

  squared.copyTo("/path/output", {
    config: {
      dataSource: [{
        source: "cloud",
        service: "aws-v3",
        credential: {
          credentials: {
            accessKeyId: "************",
            secretAccessKey: "************"
          }
        },
        table: "demo",
        query: {
          KeyConditionExpression: "#name = :value",
          ExpressionAttributeNames: {
            "#name": "id"
          },
          ExpressionAttributeValues: {
            ":value": 1
          }
        },
        limit: 1
      },
      {
        source: "cloud",
        service: "gcp",
        credential: "firestore-config",
        query: "demo",
        orderBy: [
          [
            "orderByKey"
          ],
          [
            "limitToFirst",
            1
          ]
        ]
      }]
    }
  });

.. [#] https://developer.mozilla.org/docs/Web/HTML/Element/script/type/importmap
.. [#] npm i json5
.. [#] npm i toml
.. [#] squared-express 4.0 + sqd-serve 0.18