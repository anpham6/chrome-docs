========
Settings
========

Unsafe execution is disabled by default. ``eval`` is a global setting for all users.

.. code-block::

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

All packages can be customized per authenticated username using the ``settings.users`` block. 

Using built-in transformer
==========================

External plugins per package have to be pre-installed from NPM and are not available for auto-install.

.. code-block::

  {
    "document": {
      "chrome": {
        "settings": {
          "transform": {
            "html": {
              "posthtml": {
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
              "prettier": {
                "beautify": {
                  "parser": "html",
                  "printWidth": 120,
                  "tabWidth": 4
                }
              }
            },
            "css": {
              "postcss": {
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

The suffix "-output" is used to create the variable ``options.outputConfig``.

.. code-block::

  {
    "document": {
      "chrome": {
        "settings": {
          "transform": {
            "js": {
              /* asynchronous */
              "terser": { // npm i @pi-r/terser
                "minify-example": "async (terser, value, options, require) => await terser.minify(value, options.outputConfig).code;",
                "minify-example-output": {
                  "keep_classnames": true // "minify-example-output" 
                }
              }
            },
            "css": {
              /* synchronous */
              "sass": { // npm i @pi-r/sass
                "sass-example": "(sass, value, options, resolve, require) => resolve(sass.renderSync({ ...options.outputConfig, data: value }).css);",
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

Using local file
================

.. code-block::

  {
    "document": {
      "chrome": {
        "settings": {
          "transform": {
            "js": {
              "@babel/core": {
                "es5-example": "./es5.js" // Local file - startsWith("./ | ../")
                "es5-example-output": {
                  "presets": ["@babel/preset-env"]
                },
                "es5-debug": "./es5-debug.cjs" // CJS extension
                "es5-debug-output": {
                  "presets": ["@babel/preset-env"]
                }
              }
            }
          }
        }
      }
    }
  }

.. code-block:: javascript

  // es5.js
  function (context, value, options, resolve, require) {
    context.transform(value, options.outputConfig, function (err, result) {
      resolve(!err && result ? result.code : "");
    });
  }

.. code-block:: javascript

  // es5-debug.cjs
  const path = require('path');
  
  module.exports = async function (context, value, options) {
    return await context.transform(value, options.outputConfig).code;
  }

Using custom package
====================

You can create or use a package from NPM which will behave like a built-in transformer. The only difference is the context parameter being set to the Document module.

The name of the setting has to match the NPM name of the package.

.. code-block::

  {
    "document": {
      "chrome": {
        "settings": {
          "transform": {
            "js": {
              /* Override built-in transformer */
              "@babel/core": {
                "npm-example": "npm:babel-custom", // function(Document, value, options) (npm i babel-custom)
                "npm-example-output": "npm:babel-custom-output", // Configuration object (npm i babel-custom-output)
                /* OR */
                "npm-example-output": {
                  "presets": ["@babel/preset-env"]
                }
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

Using page template
===================

The same concept can be used inline anywhere using a ``script`` tag with the *type* attribute set to **text/template**. The script template will be completely removed from the final output.

.. code-block:: html

  <script type="text/template" data-chrome-template="js::@babel/core::es5-example">
    async function (context, value, options, require) {
      const options = { ...options.outputConfig, presets: ["@babel/preset-env"], sourceMaps: true };
      const result = await context.transform(value, options);
      if (result) {
        if (result.map) {
          options.sourceMap.nextMap("babel", result.code, result.map);
        }
        return result.code;
      }
    }
  </script>

.. warning:: ``data-chrome-template`` usage requires the setting :code:`eval.template = true`.

.. [#] this = NodeJS.process
.. [#] https://babeljs.io/docs/en/options