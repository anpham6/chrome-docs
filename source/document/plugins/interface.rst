=========
Interface
=========

.. highlight:: typescript

::

  interface TransformOutput {
      pathname?: string;
      filename?: string;
      mimeType?: string;
      sourceFile?: string;
      sourcesRelativeTo?: string;
      metadata?: unknown;
      external?: PlainObject;
  }

.. code-block::

  import type { IModule } from "../../types/lib";
  import type { ChunkData, FindModuleOptions, SourceInput, SourceMap } from "../../types/document";

  interface ITransformSeries extends IModule, TransformOutput {
      type: "html" | "css" | "js";
      baseConfig: PlainObject;
      outputConfig: PlainObject; // Same as baseConfig when using an inline transformer
      sourceMap: SourceMap; // Primary sourceMap
      code: string;
      metadata: PlainObject; // Custom request values and modifiable per transformer
      options: TransformOutput;
      productionRelease: boolean;
      supplementChunks: ChunkData[];
      imported: boolean; // ESM detected
      createSourceMap(code: string): SourceMap; // Use "nextMap" method for sourceMap (additional sourceMaps)
      toBaseConfig(all?: boolean): PlainObject;
      upgrade(context: unknown, options: FindModuleOptions): unknown; // Use exact dependency installed with package
      upgrade(context: unknown, startDir?: string, packageName?: string, version?: string): unknown;
      findModule(startDir: string, packageName?: string, version?: string): string;

      /* ESM */
      getMainFile(code?: string, imports?: Record<string, string>): SourceInput<string> | undefined;
      getSourceFiles(imports?: Record<string, string>): SourceInput<[string, string?, string?][]> | undefined;
      upgradeESM(context: unknown, options: FindModuleOptions): Promise<unknown>; // Dynamic import with "require" fallback
      upgradeESM(context: unknown, dirname?: string, pkgname?: string, version?: string): Promise<unknown>;

      /* Return values */
      out: {
          sourceFiles?: string[]; // ESM (e.g. files to watch)
          ignoreCache?: boolean;
          messageAppend?: string;
          logAppend?: LogStatus[];
          logQueued?: LogStatus[];
      };

      version: string; // Requested version

      packageName: string;
      packageVersion: string; // Context version

      /* IModule */
      host: IFileManager;
      username: string;
      getTempDir(): string; // pathname: packageName + createDir: true
  }

Changelog
=========

.. versionchanged:: 0.13.0

  - *ITransformSeries* :alt:`function` **upgrade** | **upgradeESM** can specify a version range to locate a hoisted package:

    ========== ========================
     Type       Version
    ========== ========================
    first      latest
    exact      1.1.0
    startsWith 1.1.
    RegExp ^   "^1\\\\.[0-9]\\\\."
    RegExp $   "\\\\.[0-9]\\\\.\\\\d+$"
    ========== ========================

  - *ITransformSeries* symbol name for :alt:`constructorOf` was changed from **transformseries** to :target:`document:transform:series`.

.. versionadded:: 0.10.0

  - *ITransformSeries* :alt:`function` **upgradeESM** for using internal dependencies was created.