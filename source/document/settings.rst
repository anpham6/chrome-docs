========
Settings
========

These are the latest server default settings for the :target:`chrome` framework.

.. code-block::
  :caption: squared.json [#]_

  {
    "apiVersion": "1.5.0",
    "document": {
      "chrome": {
        "handler": "@pi-r/chrome",
        "namespace": "",
        "extensions": [],
        "eval": {
          "function": true,
          "absolute": false,
          "template": false,
          "userconfig": false
        },
        "format": {
          "uuid": {
            "dictionary": "",
            "pathname": "",
            "filename": ""
          }
        },
        "imports": {},
        "settings": {
          "broadcast_id": "",
          "cache_dir": "",
          "imports_strict": false,
          "directory": {
            "template": "",
            "data": "",
            "export": "",
            "schema": "",
            "package": ""
          },
          "purge": {
            "enabled": false,
            "interval": "1h",
            "percent": 0.25,
            "limit": 100,
            "all": false,
            "log": false
          },
          "options": {
            "transform": {
              "cache": {
                "enabled": false,
                "algorithm": "sha256",
                "etag": true,
                "expires": "1h",
                "renew": false,
                "limit": "10mb",
                "include": {},
                "exclude": {}
              },
              "coerce": true,
              "abort": false
            },
            "view_engine": {
              "coerce": true,
              "abort": false
            },
            "cloud": {
              "abort": false,
              "local_file": 0
            },
            "mongodb": {
              "abort": false,
              "local_file": 0
            },
            "redis": {
              "abort": false,
              "local_file": 0
            },            
            "json": {
              "coerce": true,
              "abort": false
            },
            "uri": {
              "cache": 0,
              "coerce": true,
              "abort": false,
              "local_file": 0
            },
            "local": {
              "cache": 0,
              "coerce": true,
              "abort": false
            },
            "export": {
              "cache": 0,
              "coerce": true,
              "abort": false,
              "local_file": 0
            }
          },
          "users": {
            "username": {
              "extensions": null,
              "imports": {},
              "imports_strict": false,
              "pages": {},
              "transform": {},
              "view_engine": {}
            }
          },
          "pages": {},
          "transform": {
            "imports": {
              "@babel/core": "@pi-r/babel",
              "eslint": "@pi-r/eslint",
              "html-validate": "@pi-r/html-validate",
              "postcss": "@pi-r/postcss",
              "posthtml": "@pi-r/posthtml",
              "prettier": "@pi-r/prettier",
              "rollup": "@pi-r/rollup",
              "sass": "@pi-r/sass",
              "stylelint": "@pi-r/stylelint",
              "terser": "@pi-r/terser"
            },
            "html": {
              "posthtml": {
                "transform": {
                  "plugins": []
                },
                "transform-output": {}
              },
              "html-validate": {
                "lint": {
                  "extends": ["html-validate:recommended"]
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
                  "plugins": []
                }
              },
              "stylelint": {
                "lint": {
                  "extends": []
                },
                "lint-rc": {}
              },
              "sass": {
                "compile": {
                  "outputStyle": "expanded",
                  "sourceMap": false,
                  "sourceMapContents": true
                }
              }
            },
            "js": {
              "@babel/core": {
                "es5": {
                  "presets": []
                }
              },
              "eslint": {
                "lint": {
                  "fix": false,
                  "fixTypes": null,
                  "allowInlineConfig": true,
                  "overrideConfigFile": false,
                  "baseConfig": {
                    "languageOptions": {
                      "ecmaVersion": "2020",
                      "sourceType": "module",
                      "parserOptions": {}
                    },
                    "plugins": {},
                    "rules": {}
                  },
                  "overrideConfig": null,
                  "plugins": null
                }
              },
              "prettier": {
                "beautify": {
                  "parser": "babel",
                  "printWidth": 120,
                  "tabWidth": 4
                }
              },
              "terser": {
                "minify": {
                  "toplevel": false,
                  "sourceMap": false
                }
              },
              "rollup": {
                "bundle": {
                  "treeshake": false,
                  "output": {
                    "format": "iife",
                    "sourcemap": false
                  }
                },
                "bundle-es6": {
                  "treeshake": false,
                  "output": {
                    "format": "es",
                    "preserveModules": false,
                    "sourcemap": false
                  }
                }
              }
            }
          },
          "view_engine": {
            "ejs": {
              "name": "ejs",
              "compile": {
                "rmWhitespace": false
              },
              "output": {}
            }
          },
          "export": {}
        },
        "permission": {}
      }
    }
  }

Changelog
=========

.. versionremoved:: 5.4.0

  - Transform plugins **html-minifier-terser** | **svgo** are no longer supported.

.. versionadded:: 5.3.0

  - Transform plugin **eslint** format configuration :target:`lint-v9` was created.

.. versionremoved:: 5.3.0

  - Transform plugins **html-minifier** | **uglify-js** are no longer supported.

References
==========

- https://www.unpkg.com/@pi-r/chrome/types/index.d.ts

.. [#] https://www.unpkg.com/squared-express/dist/squared.json