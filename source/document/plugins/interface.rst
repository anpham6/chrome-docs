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

  interface ITransformSeries extends IModule, TransformOutput {
      type: "html" | "css" | "js";
      baseConfig: PlainObject;
      outputConfig: PlainObject; // Same as baseConfig when using an inline transformer
      sourceMap: SourceMap; // Primary sourceMap
      code: string;
      metadata: PlainObject; // Custom request values and modifiable per transformer
      productionRelease: boolean;
      supplementChunks: ChunkData[];
      imported: boolean; // ESM detected
      createSourceMap(code: string): SourceMap; // Use "nextMap" method for sourceMap (additional sourceMaps)
      upgrade(context: unknown, dirname?: string, pkgname?: string): unknown; // Use exact dependency installed with package

      /* ESM */
      getMainFile(code?: string, imports?: StringMap): SourceInput<string> | undefined;
      getSourceFiles(imports?: StringMap): SourceInput<[string, string?, string?][]> | undefined;
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

      /* Module */
      host: IFileManager;
      username: string;
  }

Changelog
=========

.. versionadded:: 0.10.0

  - *ITransformSeries* method **upgradeESM** for using internal dependencies was created.