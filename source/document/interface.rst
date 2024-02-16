=========
Interface
=========

squared
=======

.. highlight:: typescript

.. code-block::
  :caption: chrome
  :emphasize-lines: 60,62

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
      dynamic?: boolean; // Will ignore misplaced child elements prerendered in the browser

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
          module: string; // Inline transformer
          identifier?: string;
          value?: string;
      };

      type: "append/js" | "append/css" | "append/[tagName]"; // Includes "prepend"

      type: "text" | "attribute" | "display"; // dynamic is valid only with "text"
      dataSource: {
          source: "cloud" | "uri" | "local" | "json" | "export";
          source: "mariadb" | "mongodb" | "mssql" | "mysql" | "oracle" | "postgres" | "redis"; // DB providers
          postQuery?: string;
          preRender?: string;
          whenEmpty?: string;
      };

      type: "replace";
      textContent: string; // Replace element.innerHTML
  }

@pi-r/chrome
============

.. code-block::
  :caption: dataSource
  :emphasize-lines: 5,27,28,29,30

  import type { DataSource as IDataSource } from "../db/interface";

  interface DataSource extends IDataSource {
      source: "cloud" | "uri" | "local" | "json" | "export" | string;
      type?: "text" | "attribute" | "display";
      query?: string;
      value?: string | string[] | Record<string, unknown>;
      template?: string;
      viewEngine?: ViewEngine | string;
      dynamic?: boolean;
      ignoreEmpty?: boolean;
  }

  interface UriDataSource extends DataSource, CascadeAction {
      source: "uri";
      format?: string;
      options?: PlainObject;
  }

  interface LocalDataSource extends DataSource, CascadeAction {
      source: "local";
      format?: string;
      pathname?: string;
      options?: PlainObject;
  }

  interface JSONDataSource extends DataSource, CascadeAction {
      source: "json";
      items?: Record<string, unknown>[];
  }

  interface ExportDataSource extends DataSource, CascadeAction {
      source: "export";
      execute?: (...args: unknown[]) => unknown;
      pathname?: string;
      settings?: string;
      params?: unknown;
      persist?: boolean;
  }

.. versionadded:: 0.7.0

  - *DataSource* property *source* option "**json**" as *JSONDataSource* was implemented.

.. seealso:: For any non-standard named definitions check :doc:`References </references>`.