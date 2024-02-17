=============
Build Options
=============

General processing options use *E-mc* functionality with `squared-express <https://squared.readthedocs.io/en/latest/document/build.html>`_.

.. attention:: These examples are only relevant to the **chrome** framework.

Example usage
=============

.. highlight:: javascript

::

  squared.saveAs("index.zip", {
    productionRelease: true, // Ignore local URL rewriting and use actual path
    productionRelease: "/path/to/wwwroot/", // Move assets outside base directory to server root directory
    productionIncremental: true, // Use cached data when processing transformed files

    preserveCrossOrigin: true, // Ignore locally integrating assets hosted on other domains
    preserveCrossOrigin: { // URLData
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

    incremental: false, // No cache is used ("true" is implicit)
    incremental: "none", // Will rebuild all assets and use available cache
    incremental: "staging", // Same as "none" but does not use cache
    incremental: "etag", // Will use current file if the ETag is still the same
    incremental: "exists", // Will always use current file if found

    removeInlineStyles: false, // Strip style="" attribute from all elements (useOriginalHtmlPage=false)
    removeUnusedClasses: false, // Selectors without :pseudo-class
    removeUnusedPseudoClasses: false, // Selectors with :pseudo-class (lowercase only)
    removeUnusedVariables: false, // --custom-variables
    removeUnusedFontFace: false, // @font-face
    removeUnusedKeyframes: false, // @keyframes
    removeUnusedMedia: false, // @media
    removeUnusedContainer: false, // @container
    removeUnusedSupports: false, // @supports

    /* Styles which are still being used */
    retainUsedStyles: {
      "selectors": [], // Same without separators
      "variables": [],
      "pseudoClass": false, // Will keep "li a:hover" + "li a:visited" when "li a" is a used selector
      "@font-face": [],
      "@keyframes": [],
      "@media": [],
      "@container": [],
      "@supports": []
    },
    /* OR */
    retainUsedStyles: [
      /* CSS selectors (string | RegExp) */,
      /* CSS variables (string prefixed with '--') */,
      /* CSS @font-face (string enclosed within '|font-face:Times New Roman|') */,
      /* CSS @keyframes (string enclosed within '|keyframes:animationName|') */,
      /* CSS @media (string enclosed within '|media:only screen and (min-width: 800px)|') */,
      /* CSS @container (string enclosed within '|container:(min-width: 800px)|') */,
      /* CSS @supports (string enclosed within '|supports:(display: grid)|') */
    ],

    imports: {
      "http://localhost:3000/build/": "./build", // Starts with "http"
      "http://localhost:3000/dist/chrome.framework.js": "/path/project/build/framework/chrome/src/main.js" // Full file path
    }
  });

.. caution:: Import maps [#]_ are supported from a file system perspective.

Example "saveAs"
================

The entire page can be transformed as a group with the same functionality as JSON/YAML configuration except where highlighted.

.. code-block::
  :emphasize-lines: 2,8,9,32

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
        inlineAction: "merge", // { "media": "screen" } -> { "rel": "stylesheet", "media": "screen" }
        inlineAction: "override" // { "rel": "alternate" } -> { "rel": "alternate" }
      },
      image: {
        attributes: { loading: "lazy", width: "detect", height: "detect" },
        commands: ["webp(480x300)"], // Only valid for binary images
        process: ["minify-svg"] // Only valid for text based images (e.g. SVG)
      },
      font: {
        pathname: "fonts",
        compress: "woff2", // truetype | opentype | woff | woff2
        blob: false, // Save base64 as file
        blob: "fonts/blob", // Overrides pathname for blob only
        inline: false, // Write file as data:font/ttf;base64
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

.. tip:: Use "endpoint" when your uploaded files are not used by other buckets or web pages.

Example remote configuration
============================

::

  squared.saveAs("bundle.zip", { config: { uri: "http://hostname/chrome/bundle.txt", mimeType: "text/yaml" } }); // "mimeType" is optional
  /* OR */
  squared.saveAs("bundle.zip", { config: "http://hostname/chrome/bundle.yml" }); // Detect by file extension (default is "json")

.. code-block::
  :caption: `http://hostname/pathname/example.html` -to- `http://hostname/pathname/example.html.json`

  squared.saveAs("example.zip", { config: { mimeType: "json" } });
  /* OR */
  squared.saveAs("example.zip", { config: "json" }); // json | yml | yaml

.. tip:: JSON5 [#]_ and TOML [#]_ file formats are also supported.

.. _build-using-sqd-config:

Using sqd.config
================

The base folder level configuration file is a hash map of URL globs which can match multiple items.

.. code-block::
  :caption: `http://hostname/pathname/example.html` -to- `http://hostname/pathname/sqd.config`

  squared.saveAs("example.zip", { config: true }); // Uses first match found
  /* OR */
  squared.saveAs("example.zip", {
    config: {
      uri: true,
      inherit: true | "append" // Globs are concatenated
    }
  });

.. tip:: The filename ``sqd.config`` is configurable using **settings.outputConfigName**.

The order of precedence when using **inherit** is resolved through the asset command property :ref:`mergeType <document-miscellaneous-merge-conflicts>`.

.. [#] https://developer.mozilla.org/docs/Web/HTML/Element/script/type/importmap
.. [#] npm i json5
.. [#] npm i toml