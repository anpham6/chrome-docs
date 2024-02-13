==============
@e-mc/document
==============

- **npm** i *@e-mc/document*

Interface
=========

.. code-block:: typescript

  import type { DataSource, ViewEngine } from "./squared";

  import type { IFileManager, IScopeOrigin } from "./index";
  import type { ExternalAsset, FileCommand, IFileThread, OutputFinalize } from "./asset";
  import type { HostInitConfig, IClient } from "./core";
  import type { AsSourceFileOptions, ConfigOrTransformer, CustomizeOptions, GenerateLintTableOptions, LintMessage, PluginConfig, SourceCode, SourceInput, SourceMap, SourceMapOptions, TransformAction, TransformCallback, TransformOutput, TransformResult, UpdateGradleOptions } from "./document";
  import type { PostFinalizeCallback } from "./filemanager";
  import type { LogComponent } from "./logger";
  import type { ClientModule, DocumentComponent, DocumentComponentOption, DocumentModule } from "./settings";
  import type { IFileGroup, WatchInitResult } from "./watch";

  interface IDocument extends IClient<IFileManager, ClientModule, TransformCallback<IFileManager, ExternalAsset>> {
      Db: IDb | null;
      assets: ExternalAsset[];
      config: Record<string, any>;
      init(assets: ExternalAsset[], config?: HostInitConfig): this;
      customize(options?: CustomizeOptions): void;
      findConfig(data: object, name: string, type?: string): PluginConfig;
      loadConfig(data: object, name: string): ConfigOrTransformer | null | undefined;
      asSourceFile(value: string, options?: AsSourceFileOptions | boolean): unknown;
      findVersion(name: string | string[], fallback?: string): string;
      findSourceScope(uri: string, imports: Record<string, unknown>): Record<string, string | undefined>[];
      findSourceRoot(uri: string, imports?: Record<string, string | undefined>): string | undefined;
      resolveDir(name: string, ...paths: string[]): string | undefined;
      locateSourceFiles(file: ExternalAsset, code?: string, bundleContent?: string[]): (imports?: Record<string, string | undefined>) => SourceInput | undefined;
      resolveSourceFile(file: ExternalAsset): (code?: string, imports?: Record<string, string | undefined>) => SourceInput<string> | undefined;
      tryParse(source: string, format: string, options?: Record<string | number | symbol, unknown>): unknown;
      forDb(item: DataSource): boolean;
      hasEval(name: string): boolean;
      settingsOf(name: keyof DocumentComponent, option: keyof DocumentComponentOption): unknown;
      parseTemplate(viewEngine: ViewEngine | string, template: string, data: unknown[]): Promise<string | null>;
      transform(type: string, code: string, format: string | string[], options?: TransformOutput & TransformAction): Promise<TransformResult | void>;
      abort(name?: keyof DocumentComponent | Error, reason?: unknown): void;
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
      watchModified?(watch: IFileGroup<ExternalAsset>, assets?: ExternalAsset[]): PostFinalizeCallback;
      set dataSource(value: DataSource[]);
      get dataSource(): DataSource[];
      set imports(value);
      get imports(): Record<string, string | undefined>;
      get watching(): boolean;
  }

  interface DocumentConstructor extends ModuleConstructor {
      finalize(this: IFileManager, instance: DocumentInstance): Promise<unknown>;
      createSourceMap(code: string, remove: boolean): SourceMap;
      createSourceMap(code: string, uri?: string, remove?: boolean): SourceMap;
      writeSourceMap(uri: string, data: SourceCode, options?: SourceMapOptions): string | undefined;
      updateGradle(source: string, namespaces: string[], value: string, options?: UpdateGradleOptions | boolean): string;
      generateLintTable(messages: LintMessage[], options: GenerateLintTableOptions): LogComponent[];
      cleanup?(this: IFileManager, instance: DocumentInstance): Promise<unknown>;
      sanitizeAssets?(assets: ExternalAsset[], exclusions?: ExternalAsset[]): ExternalAsset[];
      readonly prototype: DocumentInstance;
      new(module?: ClientModule, ...args: unknown[]): DocumentInstance;
  }

  type DocumentInstance = IDocument<IFileManager, ExternalAsset, ClientModule, DocumentComponent, DocumentComponentOption, ICloud>;

References
==========

* https://www.unpkg.com/@e-mc/types/lib/index.d.ts

- https://www.unpkg.com/@e-mc/types/lib/squared.d.ts
- https://www.unpkg.com/@e-mc/types/lib/asset.d.ts
- https://www.unpkg.com/@e-mc/types/lib/core.d.ts
- https://www.unpkg.com/@e-mc/types/lib/document.d.ts
- https://www.unpkg.com/@e-mc/types/lib/filemanager.d.ts
- https://www.unpkg.com/@e-mc/types/lib/logger.d.ts
- https://www.unpkg.com/@e-mc/types/lib/settings.d.ts
- https://www.unpkg.com/@e-mc/types/lib/watch.d.ts