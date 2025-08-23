========
Settings
========

All packages can be customized per authenticated username using the ``settings.users`` block. The base settings are then searched until something is found.

::

  {
    "document": {
      "chrome": {
        "handler": "@pi-r/chrome",
        "eval": {
          "function": true, // Enable inline functions
          "absolute": false, // Enable absolute paths to local files
          "template": false, // Enable external template functions
          "userconfig": false // Enable functions inside local files from user queries
        },
        "settings": {
          "directory": {
            "package": "../packages" // Override built-in plugins (base directory/ + users/username/? + posthtml.js)
          },
          "users": {
            "username": {
              "html": {
                "posthtml": {/* Same */}
              },
              "css": {
                "postcss": {/* Same */}
              }
            }
          }
        }
      }
    }
  }

.. warning:: ``eval`` is a global setting for all users. Any unsafe execution is disabled by default.

Using built-in transformer
==========================

External plugins per package have to be pre-installed from NPM and may not be available for auto-install.

::

  {
    "document": {
      "chrome": {
        "settings": {
          "transform": {
            "html": {
              "posthtml": { // npm i @pi-r/posthtml
                "transform": {
                  "plugins": [
                    ["posthtml-doctype", { "doctype": "HTML 5" }],
                    ["posthtml-include", { "root": "./", "encoding": "utf-8" }],
                    "posthtml-attrs-sorter",
                    ["htmlnano", { "collapseWhitespace": "conservative" }]
                  ]
                },
                "transform-output": {
                  "directives": [
                    { "name": "?php", "start": "<", "end": ">" }
                  ]
                }
              },
              "prettier": { // npm i @pi-r/prettier
                "beautify": {
                  "parser": "html",
                  "printWidth": 120,
                  "tabWidth": 4
                }
              }
            },
            "js": {
              "rollup": {
                "plugin-example": {
                  "plugins": [
                    "@rollup/plugin-commonjs",
                    ["@rollup/plugin-babel", { "__default__": "babel", "babelHelpers": "bundled" }] // __default__ (@pi-r property)
                  ]
                },
                "plugin-example-output": {
                  "format": "es",
                  "plugins": ["@rollup/plugin-babel", { "__default__": "getBabelOutputPlugin", { "presets": ["@babel/preset-env"] }]
                }
              }
            },
            "css": {
              "postcss": { // npm i @pi-r/postcss
                "transform": {
                  "plugins": [
                    "autoprefixer",
                    ["cssnano", { "preset": ["cssnano-preset-default", { "discardComments": false }] }]
                  ]
                }
              }
            }
          }
        }
      }
    }
  }

Using inline function [#]_
==========================

The suffix "**-output**" is used to create the variable ``options.outputConfig``.

.. code-block::
  :emphasize-lines: 8,16

  {
    "document": {
      "chrome": {
        "settings": {
          "transform": {
            "js": {
              "terser": { // npm i @pi-r/terser
                "minify-example": "async (terser, value, options, require) => await terser.minify(value, options.outputConfig).code;", // Asynchronous
                "minify-example-output": {
                  "keep_classnames": true // "minify-example-output" 
                }
              }
            },
            "css": {
              "sass": { // npm i @pi-r/sass
                "sass-example": "(sass, value, options, resolve, require) => resolve(sass.renderSync({ ...options.outputConfig, data: value }).css);", // Synchronous
                "sass-example-output": {
                  "outputStyle": "compressed",
                  "sourceMap": true,
                  "sourceMapContents": true
                }
              }
            }
          }
        }
      }
    }
  }

.. caution:: Arrow functions are supported for convenience. Explicit **function** use is recommended.

Using local file
================

::

  {
    "document": {
      "chrome": {
        "settings": {
          "transform": {
            "js": {
              "@babel/core": { // npm i @pi-r/babel
                "es5-example": "./es5.js", // JS extension uses Function constructor
                "es5-example-output": {
                  "presets": ["@babel/preset-env"]
                },
                "es5-debug": "./es5-debug.cjs", // CJS extension loaded using "require"
                "es5-debug-output": {
                  "presets": ["@babel/preset-env"]
                },
                "es6-example": "./es6.mjs", // MJS extension loaded using dynamic "import"
              }
            }
          }
        }
      }
    }
  }

.. code-block:: javascript
  :caption: es5.js (function only)

  function (context, value, options, resolve, require) {
    const path = require("path");
    context.transform(value, options.outputConfig, function (err, result) {
      resolve(!err && result ? result.code : "");
    });
  }

.. code-block:: javascript
  :caption: es5-debug.cjs

  const path = require("path");
  let ID = 0;

  module.exports = async function (context, value, options) {
    return await context.transform(`/* ${ID++} */` + value, options.outputConfig).code;
  }

.. code-block:: javascript
  :caption: es6.mjs

  import path from "node:path";
  let ID = 0;

  export default async function (context, value, options) {
    return await context.transform(`/* ${ID++} */` + value, options.outputConfig).code;
  }

.. caution:: The ``.js`` extension uses the "**type**" value in your *package.json* to determine which module loader to use. It is better to be explicit using either ``.cjs`` or ``.mjs``.

Using custom package
====================

You can create or use a package from NPM which will behave like a built-in transformer. The only difference is the context parameter being set to the *Document* module.

::

  {
    "document": {
      "chrome": {
        "settings": {
          "transform": {
            "js": {
              /* Override built-in transformer */
              "@babel/core": {
                /* npm i babel-custom */
                "npm-example": "npm:babel-custom", // function(Document, value, options) { const context = require("babel-custom"); }
                "npm-example-output": {
                  "presets": ["@babel/preset-env"]
                },
                /* OR */
                "npm-example-output": "npm:babel-custom-output" // Not recommended (npm i babel-custom-output)
              }
            },
            "css": {
              /* npm i sass-custom */
              "sass-custom": {
                "transform": { // options.baseConfig
                  "sourceMap": true
                }
              }
            }
          }
        }
      }
    }
  }

You can create aliases with your own handling routine to wrap any *NPM* package.

::

  {
    "document": {
      "chrome": {
        "settings": {
          "transform": {
            "imports": {
              /* @pi-r - e-mc + squared-express */
              "@babel/core": "@pi-r/babel",

              /* @pi-r2 - e-mc */
              "clean-css": "@pi-r2/clean-css", // Unmaintained
              "csso": "@pi-r2/clean-css",
              "html-minifier": "@pi-r2/html-minifier",
              "html-minifier-terser": "@pi-r2/html-minifier-terser",
              "svgo": "@pi-r2/svgo",
              "uglify-js": "@pi-r2/uglify-js",

              /* Custom - Add */
              "webpack": "webpack-custom",

              /* Custom - Replace */
              "@babel/core": "babel-custom"
            }
          }
        }
      }
    }
  }

.. attention:: The setting name has to match the **NPM** package name.

Using page template
===================

The same concept can be used inline anywhere using a ``script`` tag with the **type** attribute set to "text/template". The script template will be completely removed from the final output.

.. code-block:: html
  :emphasize-lines: 1

  <script type="text/template" data-chrome-template="js::@babel/core::es5-example">
    async function (context, value, options) {
      const options = { ...options.toBaseConfig(), presets: ["@babel/preset-env"], sourceMaps: true };
      const result = await context.transform(value, options);
      if (result) {
        if (result.map) {
          options.sourceMap.nextMap("babel", result.code, result.map);
        }
        return result.code;
      }
    }
  </script>

.. code-block::
  :caption: Alternate

  {
    "selector": "",
    "type": "js",
    "template": {
      "module": "@babel/core",
      "identifier": "es5-example",
      "value": "async function (context, value, options) {/* Same */}" // Arrow functions not supported
    }
  }

.. attention:: Using **data-chrome-template** requires the setting :code:`eval.template = true`.

.. [#] this = NodeJS.process