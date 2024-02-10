=========
Breakdown
=========

Plugins are simply *options* pass-through calls to a *context* wrapper method. The only part which might not be intuitive is consuming an existing source map and then saving it for further processing.

Code
====

.. code-block:: typescript
  :caption: @pi-r/clean-css
  :linenos:
  :emphasize-lines: 5,16

  import type { ITransformSeries, RawSourceMap } from "@e-mc/types/lib/document";

  import type * as cc from "clean-css";

  export default function transform(context: typeof cc, value: string, options: ITransformSeries<cc.OptionsOutput>) {
      context = options.upgrade(context, __dirname);
      const sourceMap = options.sourceMap;
      const baseConfig = options.toBaseConfig(/* true */); // Use "false" for only outputConfig
      let map: RawSourceMap<string> | undefined;
      if (baseConfig.sourceMap === false) {
          sourceMap.reset();
      }
      else if (map = sourceMap.map) {
          baseConfig.sourceMap = true;
      }
      const result = new context(baseConfig).minify(value, map);
      if (result) {
          if (result.sourceMap) {
              sourceMap.nextMap("clean-css", result.styles, result.sourceMap.toString());
          }
          return result.styles;
      }
  }

.. note:: There are only three lines of relevant TypeScript being used to check for upgrade compatibility. Local file ".cjs" transformers offer the same functionality.

Comments
========

#. Typings (optional)
#. *none*
#. *none*
#. *none*
#. **context** = require("clean-css"), **value** = source code, **options** = *TransformSeries* instance
#. When base installation (process.cwd()) uses a different major package version (optional)
#. Main *sourceMap* from previous consumer
#. Applies **options.external** AND **options.outputConfig** to **options.baseConfig** (optional)
#. *none*
#. Delete current *sourceMap* as requested using ``sourceMap.reset``
#. *none*
#. *none*
#. Check if there is an existing sourceMap and pass it through
#. *none*
#. *none*
#. Call package transform method with **baseConfig** and **value**
#. Check if method succeeded
#. Check if a *sourceMap* was generated
#. Pass *sourceMap* output values to ``sourceMap.nextMap`` chain method
#. *none*
#. Return modified transformed *source code*