========
Built-In
========

*JS* and *CSS* files can be optimized further using these settings:

#. compile
#. bundle[-es6]
#. lint[-v9]
#. es5
#. transform
#. beautify
#. minify
#. es5-minify
#. minify-svg
#. custom name

You can define or undefine your own optimizations in ``squared.json``:

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
  * - `html-minifier-terser <https://github.com/DanielRuf/html-minifier-terser>`_
    - @pi-r/html-minifier-terser
    - 7
  * - `svgo <https://github.com/svg/svgo>`_
    - @pi-r/svgo
    - 9

CSS
===

.. list-table::
  :width: 400px
  :widths: 40 50 10

  * - `postcss <https://github.com/postcss/postcss>`_
    - @pi-r/postcss
    - 5
  * - `clean-css <https://github.com/jakubpawlowicz/clean-css>`_
    - @pi-r/clean-css
    - 6
  * - `csso <https://github.com/css/csso>`_
    - @pi-r/csso
    - 7
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
- Local file using export default :alt:`(e.g. ".mjs")` [#v010]_
- Local plain file with single function :alt:`(e.g. ".js")`
- Inline function

Deprecated
----------

.. list-table::
  :width: 400px
  :widths: 40 50 10

  * - `html-minifier <https://github.com/kangax/html-minifier>`_
    - @pi-r/html-minifier [#]_
    - 0.7.3
  * - `uglify-js <https://github.com/mishoo/UglifyJS>`_
    - @pi-r/uglify-js [#]_
    - 0.7.3

Environment Variables
=====================

========== ====================== ======== ========
  Plugin    Name                   Value    Default
========== ====================== ======== ========
eslint     ESLINT_USE_FLAT_CONFIG  boolean     none
eslint     ESLINT_FORMATTER_NAME       any     none
stylelint  STYLELINT_OPTIONS_FIX   boolean    false
========== ====================== ======== ========

.. [#] settings.transform.imports
.. [#] Substitute: @pi-r/html-minifier-terser
.. [#] Substitute: @pi-r/terser
.. [#v010] e-mc 0.10 (minimum)