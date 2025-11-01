==============
@e-mc/document
==============

Interface
=========

.. highlight:: typescript

.. code-block::
  :caption: `View Source <https://www.unpkg.com/@e-mc/types/lib/index.d.ts>`_

  import type { DataSource, ViewEngine } from "./squared";

  import type { IFileManager, IScopeOrigin } from "./index";
  import type { ExternalAsset, FileCommand, IFileThread, OutputFinalize } from "./asset";
  import type { HostInitConfig, IClient } from "./core";
  import type { AsSourceFileOptions, ConfigOrTransformer, CustomizeOptions, GenerateLintTableOptions, LintMessage, PluginConfig, SourceCode, SourceInput, SourceMap, SourceMapOptions, TransformAction, TransformCallback, TransformOutput, TransformResult, UpdateGradleOptions } from "./document";
  import type { PostFinalizeCallback } from "./filemanager";
  import type { LogComponent } from "./logger";
  import type { DocumentComponent, DocumentComponentOption, DocumentModule } from "./settings";
  import type { IFileGroup, WatchInitResult } from "./watch";

  interface IDocument extends IClient<IFileManager, DocumentModule, TransformCallback<IFileManager, ExternalAsset>> {
      Db: IDb | null;
      assets: ExternalAsset[];
      config: Record<string, any>;
      init(assets: ExternalAsset[], config?: HostInitConfig): this;
      customize(options?: CustomizeOptions): void;
      findConfig(data: object, name: string, type?: string): PluginConfig;
      loadConfig(data: object, name: string): ConfigOrTransformer | undefined;
      asSourceFile(value: string, cache: boolean): unknown;
      asSourceFile(value: string, options?: AsSourceFileOptions): unknown;
      findVersion(name: string | string[], fallback?: string): string;
      findSourceScope(uri: string, imports: Record<string, unknown>): StringMap[];
      findSourceRoot(uri: string, imports?: StringMap): string | undefined;
      resolveDir(name: string, ...paths: string[]): string | undefined;
      locateSourceFiles(file: ExternalAsset, code?: string, bundleContent?: string[]): ((imports?: StringMap) => SourceInput | undefined);
      resolveSourceFile(file: ExternalAsset): ((code?: string, imports?: StringMap) => SourceInput<string> | undefined);
      tryParse(source: string, format: string, options?: PlainObject): unknown;
      forDb(item: DataSource): boolean;
      hasEval(name: string): boolean;
      settingsOf(name: keyof DocumentComponent, option: keyof DocumentComponentOption): unknown;
      parseTemplate(viewEngine: ViewEngine | string, template: string, data: unknown[]): Promise<string | null>;
      transform(type: string, code: string, format: string | string[], options?: TransformOutput & TransformAction): Promise<TransformResult | void>;
      abort(err: Error): void;
      abort(name?: keyof DocumentComponent, reason?: unknown): void;
      restart(): void;
      using?(data: IFileThread): Promise<unknown>;
      setLocalUri?(file: ExternalAsset, replace?: boolean): void;
      resolveUri?(file: ExternalAsset, source: string): string;
      resolveUri?(file: ExternalAsset, source: string, trailing: string): [string, string];
      resolveImports?(file: ExternalAsset, code: string, baseFile?: string | ExternalAsset): string | undefined;
      replaceContent?(source: string, statement: RegExpExecArray | string, mimeType?: string): string | undefined;
      addCopy?(data: FileCommand<ExternalAsset>, saveAs: string, replace?: boolean): string | undefined;
      writeImage?(output: OutputFinalize<ExternalAsset>): boolean;
      cloudInit?(state: IScopeOrigin<IFileManager, ICloud>): void;
      cloudObject?(state: IScopeOrigin<IFileManager, ICloud>, file: ExternalAsset): boolean;
      cloudUpload?(state: IScopeOrigin<IFileManager, ICloud>, file: ExternalAsset, url: string, active: boolean): Promise<boolean>;
      cloudFinalize?(state: IScopeOrigin<IFileManager, ICloud>): Promise<unknown[]>;
      watchInit?(watch: IFileGroup<ExternalAsset>, assets: ExternalAsset[], sanitize?: boolean): WatchInitResult | undefined;
      watchModified?(watch: IFileGroup<ExternalAsset>, assets?: ExternalAsset[], recursive?: [string, string[]][]): PostFinalizeCallback;
      set dataSource(value: DataSource[]);
      get dataSource(): DataSource[];
      set imports(value);
      get imports(): StringMap;
      get watching(): boolean;
      set host(value);
      get host(): IFileManager | null;
  }

  interface DocumentConstructor extends ModuleConstructor {
      finalize(this: IFileManager, instance: IDocument): Promise<unknown>;
      createSourceMap(code: string, remove: boolean): SourceMap;
      createSourceMap(code: string, uri?: string, remove?: boolean): SourceMap;
      writeSourceMap(uri: string, data: SourceCode, options?: SourceMapOptions): string | undefined;
      updateGradle(source: string, namespaces: string[], value: string, upgrade: boolean): string;
      updateGradle(source: string, namespaces: string[], value: string, options?: UpdateGradleOptions): string;
      generateLintTable(messages: LintMessage[], options: GenerateLintTableOptions): LogComponent[];
      cleanup?(this: IFileManager, instance: IDocument): Promise<unknown>;
      sanitizeAssets?(assets: ExternalAsset[], exclusions?: unknown[]): ExternalAsset[];
      readonly prototype: IDocument;
      new(module?: DocumentModule, ...args: unknown[]): IDocument;
  }

Changelog
=========

.. versionadded:: 0.13.0

  - Hash object based function transformers by :target:`format` name can be exported including a **default** export for :ref:`document plugins <document-plugins-settings-es6-hash>`.

.. versionadded:: 0.12.0

  - *ViewEngine* :alt:`function` **compile** | **compileSync** can be called with an Array of arguments :alt:`(options.compile)`.

.. versionchanged:: 0.12.0

  - *IDocument* :alt:`function` **watchModified** argument :target:`recursive` as :alt:`[string, string[]][]` for directory watchers was created.

.. versionchanged:: 0.9.0

  - *IDocument* :alt:`property` **config** was made abstract.

Settings
========

.. code-block::
  :caption: `View JSON <https://www.unpkg.com/squared-express/dist/squared.json>`_

  import type { PermittedDirectories } from "./core";
  import type { DbModule, DbSettings, DocumentComponentOptions, PurgeComponent } from "./settings";

  interface DocumentModule {
      // handler: "@pi-r/chrome";
      extensions?: string[];
      db?: DbModule<DbSettings>;
      eval?: {
          function?: boolean;
          absolute?: boolean;
          template?: boolean;
          userconfig?: boolean;
      };
      format?: {
          uuid?: {
              dictionary?: string;
              pathname?: string;
              filename?: string;
          };
      };
      imports?: StringMap;
      settings?: {
          broadcast_id?: string | string[];
          users?: Record<string, {
              extensions?: string[] | null;
              imports?: StringMap;
              imports_strict?: boolean;
              pages?: unknown;
              transform?: unknown;
              view_engine?: unknown;
          }>;
          cache_dir?: string;
          imports_strict?: boolean;
          directory?: {
              template?: string;
              data?: string;
              export?: string;
              schema?: string;
              package?: string;
          };
          purge?: PurgeComponent;
          options?: DocumentComponentOptions<boolean | number>;
          pages?: Record<string, Record<string, unknown>>;
          transform?: {
              html?: Record<string, Record<string, unknown>>;
              css?: Record<string, Record<string, unknown>>;
              js?: Record<string, Record<string, unknown>>;
          };
          view_engine?: Record<string, Record<string, unknown>>;
          export?: Record<string, string | (...args: unknown[]) => unknown>;
      };
      permission?: PermittedDirectories;
  }

Example usage
-------------

.. code-block:: javascript
  :caption: Abstract class

  const Document = require("@e-mc/document"); // @pi-r/chrome

  const assets = [
    { pathname: "output", filename: "image1.png", uri: "http://hostname/path/document1.png" },
    { pathname: "output", filename: "image2.png", uri: "http://hostname/path/document2.png" }
  ];

  const instance = new Document({
    eval: {
      function: true,
      template: true
    },
    imports: {
      "http://hostname/path/": "build/"
    },
    settings: {
      imports_strict: true,
      users: {
        "nodejs-001": {
          imports_strict: false,
          imports: {
            "http://hostname/path": "build"
          }
        }
      },
      directory: {
        template: "../chrome/template" // ../chrome/template/users/nodejs-001
      }
    }
  });
  // instance.host = new Host();
  instance.init(assets);

.. attention:: **@e-mc/document** is an abstract base class and cannot be instantiated. :target:`Document` is more commonly called through :doc:`@pi-r/chrome </document/index>`.

References
==========

- https://www.unpkg.com/@e-mc/types/lib/squared.d.ts
- https://www.unpkg.com/@e-mc/types/lib/asset.d.ts
- https://www.unpkg.com/@e-mc/types/lib/core.d.ts
- https://www.unpkg.com/@e-mc/types/lib/document.d.ts
- https://www.unpkg.com/@e-mc/types/lib/filemanager.d.ts
- https://www.unpkg.com/@e-mc/types/lib/logger.d.ts
- https://www.unpkg.com/@e-mc/types/lib/settings.d.ts
- https://www.unpkg.com/@e-mc/types/lib/watch.d.ts