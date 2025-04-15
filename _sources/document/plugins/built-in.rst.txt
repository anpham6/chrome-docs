========
Built-In
========

*JS* and *CSS* files can be optimized further using these settings:

#. compile
#. bundle[-es6]
#. lint
#. es5
#. transform
#. beautify
#. minify
#. es5-minify
#. custom name

You can define or undefine your own optimizations in ``squared.json``.

HTML
====

.. list-table::
  :width: 400px
  :widths: 40 50 10

  * - `posthtml <https://github.com/postcss/postcss>`_
    - @pi-r/posthtml
    - 5
  * - `prettier <https://github.com/prettier/prettier>`_
    - @pi-r/prettier
    - 6
  * - `html-validate <https://gitlab.com/html-validate/html-validate>`_
    - @pi-r/html-validate
    - 3

CSS
===

.. list-table::
  :width: 400px
  :widths: 40 50 10

  * - `postcss <https://github.com/postcss/postcss>`_
    - @pi-r/postcss
    - 5
  * - `stylelint <https://github.com/stylelint/stylelint>`_
    - @pi-r/stylelint
    - 3
  * - `sass <https://github.com/sass/dart-sass>`_
    - @pi-r/sass
    - 1

JS
==

.. list-table::
  :width: 400px
  :widths: 40 50 10

  * - `@babel/core <https://github.com/babel/babel>`_
    - @pi-r/babel
    - 4
  * - `eslint <https://github.com/eslint/eslint>`_
    - @pi-r/eslint
    - 3
  * - `prettier <https://github.com/prettier/prettier>`_
    - @pi-r/prettier
    - 6
  * - `rollup <https://github.com/rollup/rollup>`_
    - @pi-r/rollup
    - 2
  * - `terser <https://github.com/terser/terser>`_ 
    - @pi-r/terser
    - 7

These plugins can be configured using a plain object in ``settings.transform``. Import maps [#]_ are available for plugins which resolve imports through the file system. Other non-builtin transpilers can similarly be integrated by defining a custom function.

- NPM custom package
- Local file using module.exports :alt:`(e.g. ".cjs")`
- Local file using export default :alt:`(e.g. ".mjs")`
- Local plain file with single function :alt:`(e.g. ".js")`
- Inline function

Unmaintained
------------

The source for these packages are located in a separate repository `Pi-r2 <https://github.com/anpham6/pi-r2>`_. Once per year they are published with each major NodeJS release in April.

.. list-table::
  :width: 300px
  :widths: 70 20 10

  * - @pi-r/html-minifier
    - 0.7.x
    - N
  * - @pi-r/uglify-js
    - 0.7.x
    - Y [#Y]_
  * - @pi-r/html-minifier-terser
    - 0.8.x
    - N
  * - @pi-r/svgo
    - 0.8.x
    - Y [#Y]_
  * - @pi-r/clean-css
    - 0.9.x
    - N
  * - @pi-r/csso
    - 0.9.x
    - N

.. tip:: `Pi-r2` packages are compatible with the latest `E-mc` and can be used as is without any problems.

Environment Variables
=====================

.. rst-class:: first-center

========== =================================== ============
  Plugin    Name                                Value
========== =================================== ============
eslint     ESLINT_USE_FLAT_CONFIG              boolean
eslint     ESLINT_FORMATTER_NAME               any
sass [#]_  SASS_OPTIONS_IMPORTER_NODE_PACKAGE  path/boolean
stylelint  STYLELINT_OPTIONS_CWD               path
stylelint  STYLELINT_OPTIONS_CONFIG_FILE       path
stylelint  STYLELINT_OPTIONS_CONFIG_BASEDIR    path
stylelint  STYLELINT_OPTIONS_VALIDATE          boolean
stylelint  STYLELINT_OPTIONS_FIX               boolean
stylelint  STYLELINT_OPTIONS_FORMATTER         string
========== =================================== ============

Pre-Installed
=============

.. rst-class:: first-center

========== ================================ ============ =======
  Plugin    Name                             Alias        Pi-r
========== ================================ ============ =======
postcss    autoprefixer                                   0.10.0
postcss    postcss-import                   import        0.10.0
rollup     @rollup/plugin-commonjs          commonjs      0.10.0
rollup     @rollup/plugin-node-resolve      node-resolve  0.10.0
========== ================================ ============ =======

.. code-block::
  :caption: squared.json
  :emphasize-lines: 6-8,15

  {
    "rollup": {
      "bundle-es6": {
        "treeshake": true,
        "plugins": [
          "node-resolve",
          "@rollup/plugin-commonjs", // "commonjs"
          ["babel", { "__default__": "babel", "babelHelpers": "bundled" }] // __default__ (@pi-r property)
        ],
        "output": {
          "format": "es",
          "preserveModules": false,
          "sourcemap": true,
          "plugins": [
            ["@rollup/plugin-terser", { "keep_classnames": true }] // npm i @rollup/plugin-terser
          ]
        }
      }
    }
  }

.. [#] settings.transform.imports
.. [#Y] Package with dependencies (e.g. @e-mc/document)
.. [#] metadata: { "__nodepackageimporter__": true }