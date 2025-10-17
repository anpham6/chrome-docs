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
  import type { ChunkData, SourceInput, SourceMap } from "../../types/document";

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
      upgrade(context: unknown, startDir?: string, packageName?: string): unknown; // Use exact dependency installed with package
      findModule(startDir: string, packageName?: string): string;

      /* ESM */
      getMainFile(code?: string, imports?: Record<string, string>): SourceInput<string> | undefined;
      getSourceFiles(imports?: Record<string, string>): SourceInput<[string, string?, string?][]> | undefined;
      upgradeESM(context: unknown, dirname?: string, pkgname?: string): Promise<unknown>; // Dynamic import with "require" fallback

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

.. versionadded:: 0.10.0

  - *ITransformSeries* method **upgradeESM** for using internal dependencies was created.