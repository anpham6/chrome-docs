=========
Interface
=========

.. code-block:: typescript
  :emphasize-lines: 60

  interface AssetCommand {
      selector: string;

      saveAs?: string; // js | css | image
      exportAs?: string; // js | css
      saveTo?: string; // image | video | audio (transforms are given auto-generated filename)
      pathname?: string; // alias for "saveTo"
      filename?: string; // pathname + filename = "saveAs"

      process?: string[]; // html | js | css
      commands?: string[]; // image
      tasks?: string[];
      cloudStorage?: CloudService[];

      inline?: boolean; // js | css | image (base64) | font (base64)
      blob?: boolean; // format: base64
      preserve?: boolean; // html | css | append/js (cross-origin) | append/css (cross-origin)
      extract?: boolean; // css (@import)
      module?: boolean; // js (esm) | css
      dynamic?: boolean; // image (srcset) | element (non-void)
      static?: boolean; // Removes URL search params
      remove?: boolean; // Removes element from HTML page
      ignore?: boolean;
      exclude?: boolean; // js | css (ignore + remove)

      attributes?: Record<string, string | null | undefined>;
      rewrite?: false; // Overrides preserveCrossOrigin
      rewrite?: URLData; // Replace certain URL components (e.g. hostname)
      download?: boolean; // Forces processing for unknown types (default is "true" for known types)

      hash?: "md5" | "sha1" | "sha224" | "sha256" | "sha384" | "sha512";
      hash?: "md5[8]" // Will shorten hash to the first 8 characters

      checksum?: string | { algorithm: string; value: string; digest?: string }; // Download URI (default is "sha256")
      checksumOutput?: string | {/* Same */}; // Expected locally transformed result

      incremental?: false | "none" | "staging" | "etag" | "exists"; // Will override parent.incremental
      incremental?: true; // Will override parent.incremental = false

      metadata?: PlainObject; // Custom values passed to transformers
      metadata?: { "__sourcemap__": "inline" }; // System post processing command

      mergeType?: "none" | "over" | "under"; // Used when different selectors target same element

      watch?: boolean | { interval?: number; expires?: string }; // js | css | image

      document?: string | string[]; // Usually "chrome" by framework (override)

      type: "html" | "js" | "css" | "data"; // Script templates
      template: {
          module?: string;
          identifier?: string;
          value?: string;
      };

      type: "append/js" | "append/css" | "append/[tagName]"; // Includes "prepend"

      type: "text" | "attribute" | "display"; // dynamic is valid only with "text"
      dataSource: {
          source: "uri" | "local" | "export" | "json";
          source: "cloud";
          source: "mariadb" | "mongodb" | "mssql" | "mysql" | "oracle" | "postgres" | "redis";
          postQuery?: string;
          preRender?: string;
          whenEmpty?: string;
      };

      type: "replace";
      textContent: string; // Replace element.innerHTML
  }

.. seealso:: For any non-standard named definitions check :doc:`References </references>`.

@pi-r/chrome
============

.. versionadded:: 0.7.0

  *DataSource* property ``source`` option "**json**" as *JSONDataSource* was implemented.