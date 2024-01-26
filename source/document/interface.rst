Interface
=========

.. code-block:: typescript

  interface OutputModifiers {
      inline?: boolean; // type: js | css | image (base64) | font (base64)
      blob?: boolean; // format: base64
      preserve?: boolean; // type: html | css | append/js (cross-origin) | append/css (cross-origin)
      extract?: boolean; // type: css
      module?: boolean; // type: js (esm) | css
      dynamic?: boolean; // type: image (srcset) | element (non-void)
      static?: boolean; // Removes URL search params
      remove?: boolean; // Removes element from HTML page
      ignore?: boolean;
      exclude?: boolean; // type: js | css (remove from HTML)
  }

.. code-block:: typescript

  import type { CloudDatabase, CloudService } from "../cloud/interface";

  interface AssetCommand extends OutputModifiers {
      selector: string;

      saveAs?: string; // js | css | image
      exportAs?: string; // js | css
      saveTo?: string; // image | video | audio (transforms create multiple files and are given generated filename)
      pathname?: string; // alias for "saveTo"
      filename?: string; // pathname + filename = "saveAs"

      process?: string[]; // html | js | css
      template?: {
          module: string; // Document > Plugins > Settings > Using page template
          identifier?: string;
          value?: string;
      };

      commands?: string[]; // image
      tasks?: string[]; // All assets

      attributes?: Record<string, string | null | undefined>;
      rewrite?: false; // Overrides preserveCrossOrigin
      rewrite?: URLData; // Writable string properties in URL class

      download?: boolean; // Forces processing for unknown types (implicitly is "true" for known types)
      dynamic?: boolean; // Will ignore misplaced child elements prerendered in the browser

      hash?: "md5" | "sha1" | "sha224" | "sha256" | "sha384" | "sha512"; // md5[8] will shorten hash to the first 8 characters

      checksum?: string | { algorithm: string, value: string, digest?: string }; // Download URI + Default is "sha256"
      checksumOutput?: string | {/* Same */}; // Expected locally transformed result

      incremental?: false | "none" | "staging" | "etag" | "exists"; // Will override batch request.incremental
      incremental?: true; // Will override request.incremental = false

      metadata?: PlainObject; // Custom values passed to transformers
      metadata?: { "__sourcemap__": "inline" }; // System post processing command

      mergeType?: "none" | "over" | "under"; // Used when different selectors target same element

      watch?: boolean | { interval?: number, expires?: string }; // type: js | css | image (expires: 1h 1m 1s)

      cloudStorage?: CloudService[];

      type?: "html" | "js" | "css" | "data"; // Script templates
      type?: "append/js" | "append/css" | "append/[tagName]"; // Includes "prepend"

      type?: "text" | "attribute" | "display"; // dynamic is valid only with "text"
      dataSource?: CloudDatabase; // source: "cloud"
      dataSource?: {
          source: "mongodb" | "redis" | "mysql" | "postgres" | "oracle" | "mssql" | "mariadb" | "uri" | "local" | "export";
          postQuery?: string;
          preRender?: string;
          whenEmpty?: string;
      };

      type?: "replace";
      textContent?: string; // Replace element.innerHTML

      document?: string | string[]; // Usually "chrome" by framework (override)
  }

Global
------

.. code-block:: typescript

  type PlainObject = Record<string | number | symbol, unknown>;