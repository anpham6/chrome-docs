Built-In
========

JS and CSS files can be optimized further using these settings:

- beautify
- lint
- minify
- es5
- es5-minify
- minify-svg
- compile
- custom name

You can define or undefine your own optimizations in ``squared.json``:

HTML
----

- `posthtml <https://github.com/postcss/postcss>`_ -> @pi-r/posthtml
- `html-validate <https://gitlab.com/html-validate/html-validate>`_ -> @pi-r/html-validate
- `html-minifier-terser <https://github.com/DanielRuf/html-minifier-terser>`_ -> @pi-r/html-minifier-terser
- `html-minifier <https://github.com/kangax/html-minifier>`_ -> @pi-r/html-minifier
- `svgo <https://github.com/svg/svgo>`_ -> @pi-r/svgo

CSS
---

- `postcss <https://github.com/postcss/postcss>`_ -> @pi-r/postcss
- `prettier <https://github.com/prettier/prettier>`_ -> @pi-r/prettier
- `clean-css <https://github.com/jakubpawlowicz/clean-css>`_ -> @pi-r/clean-css
- `csso <https://github.com/css/csso>`_ -> @pi-r/csso
- `stylelint <https://github.com/stylelint/stylelint>`_ -> @pi-r/stylelint
- `sass <https://github.com/sass/dart-sass>`_ -> @pi-r/sass

JS
--

- `@babel/core <https://github.com/babel/babel>`_ -> @pi-r/babel
- `eslint <https://github.com/eslint/eslint>`_ -> @pi-r/eslint
- `uglify-js <https://github.com/mishoo/UglifyJS>`_ -> @pi-r/uglify-js
- `rollup <https://github.com/rollup/rollup>`_ -> @pi-r/rollup
- `terser <https://github.com/terser/terser>`_ -> @pi-r/terser

These plugins can be configured using a plain object ``settings.transform[html|css|js]``. Import maps [#]_ are available for plugins which transpile using a modular loading system. Other non-builtin transpilers can similarly be applied and chained by defining a custom function.

- NPM custom package
- Local file using module.exports (e.g. ".cjs")
- Local plain file with single function (e.g. ".js")
- Inline function

More advanced plugins can be written and installed through NPM.

.. [#] settings.transform.imports