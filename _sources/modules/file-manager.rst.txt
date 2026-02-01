==================
@e-mc/file-manager
==================

Interface
=========

.. highlight:: typescript

.. code-block::
  :caption: `View Source <https://www.unpkg.com/@e-mc/types/lib/index.d.ts>`_
  :emphasize-lines: 165

  import type { ChecksumValue, DataSource, IncrementalMatch, TaskAction } from "./squared";

  import type { DocumentConstructor, HostConstructor, ICloud, ICompress, IDocument, IHost, IImage, IModule, IRequest, ITask, IWatch, ImageConstructor, TaskConstructor, WatchConstructor } from "./index";
  import type { ExternalAsset, FileCommand, FileData, IFileThread, OutputFinalize } from "./asset";
  import type { IPermission, PermissionReadWrite } from "./core";
  import type { AssetContentOptions, CheckHashOptions, ChecksumOptions, DeleteFileAddendum, FileOutput, FinalizeResult, FindAssetOptions, IHttpDiskCache, IHttpMemoryCache, InstallData, PostFinalizeCallback, ReplaceOptions } from "./filemanager";
  import type { ExecCommand } from "./logger";
  import type { CopyFileOptions, CreateDirOptions, DeleteFileOptions, MoveFileOptions, ReadFileOptions, RemoveDirOptions, WriteFileOptions } from "./module";
  import type { RequestData, Settings } from "./node";
  import type { Aria2Options, BufferFormat, OpenOptions, RcloneOptions } from "./request";
  import type { CloudModule, CompressModule, DbModule, DocumentModule, HttpConnectSettings, HttpMemorySettings, ImageModule, RequestModule, TaskModule, WatchModule } from "./settings";

  import type { SpawnOptions } from "node:child_process";
  import type { NoParamCallback } from "node:fs";

  interface IFileManager extends IHost, Set<string> {
      processTimeout: number;
      Request: IRequest<RequestModule>;
      Document: InstallData<IDocument<IFileManager, ExternalAsset>, DocumentConstructor<IFileManager, ExternalAsset>>[];
      Task: InstallData<ITask, TaskConstructor>[];
      Image: Map<string, InstallData<IImage, ImageConstructor>> | null;
      Cloud: ICloud | null;
      Watch: WatchInstance<ExternalAsset> | null;
      Compress: ICompress<CompressModule> | null;
      readonly documentAssets: ExternalAsset[];
      readonly taskAssets: (ExternalAsset & Required<TaskAction>)[];
      readonly dataSourceItems: DataSource[];
      readonly files: Set<string>;
      readonly filesQueued: Set<string>;
      readonly filesToRemove: Set<string>;
      readonly filesToCompare: Map<ExternalAsset, string[]>;
      readonly contentToAppend: Map<string, string[]>;
      readonly contentToReplace: Map<string, string[]>;
      readonly processing: IFileThread[];
      readonly fetchedAssets: ExternalAsset[];
      readonly copiedAssets: ExternalAsset[];
      readonly emptyDir: Set<string>;
      readonly cacheToDisk: IHttpDiskCache<ExternalAsset>;
      readonly cacheToMemory: IHttpMemoryCache<ExternalAsset>;
      install(name: "document", handler: string, module?: DocumentModule, ...args: unknown[]): IDocument | undefined;
      install(name: "document", target: DocumentConstructor, module?: DocumentModule, ...args: unknown[]): IDocument | undefined;
      install(name: "task", handler: string, module?: TaskModule, ...args: unknown[]): ITask | undefined;
      install(name: "task", target: TaskConstructor, module?: TaskModule, ...args: unknown[]): ITask | undefined;
      install(name: "cloud", handler: string, module?: CloudModule, ...args: unknown[]): ICloud | undefined;
      install(name: "cloud", module?: CloudModule, ...args: unknown[]): ICloud | undefined;
      install(name: "image", handler: string, module?: ImageModule, ...args: unknown[]): IImage | undefined;
      install(name: "image", target: ImageConstructor, module?: ImageModule, ...args: unknown[]): IImage | undefined;
      install(name: "image", targets: Map<string, ImageConstructor>, module?: ImageModule): void;
      install(name: "watch", handler: string, module?: WatchModule, ...args: unknown[]): IWatch | undefined;
      install(name: "watch", target: WatchConstructor, module?: WatchModule, ...args: unknown[]): IWatch | undefined;
      install(name: "watch", module: WatchModule): IWatch | undefined;
      install(name: "compress", module?: CompressModule): ICompress<CompressModule> | undefined;
      install(name: string, ...args: unknown[]): IModule | undefined;
      using(...items: ExternalAsset[] | [boolean, ...ExternalAsset[]]): this;
      contains(item: ExternalAsset, condition?: (target: ExternalAsset) => boolean): boolean;
      removeCwd(value: unknown): string;
      findAsset(value: string | URL, instance: IModule | null): ExternalAsset | undefined;
      findAsset(value: string | URL, options?: FindAssetOptions<ExternalAsset>): ExternalAsset | undefined;
      removeAsset(file: ExternalAsset): boolean;
      replace(file: ExternalAsset, replaceWith: string, mimeType: string | undefined): boolean;
      replace(file: ExternalAsset, replaceWith: string, options?: ReplaceOptions): boolean;
      rename(file: ExternalAsset, value: string): boolean;
      performAsyncTask(): void;
      removeAsyncTask(): void;
      completeAsyncTask(err?: unknown, uri?: string, parent?: ExternalAsset, type?: number): void;
      performFinalize(override?: boolean): void;
      hasDocument(instance: IModule, document: string | string[] | undefined): boolean;
      getDocumentAssets(instance: IModule, condition?: (target: ExternalAsset) => boolean): ExternalAsset[];
      getDataSourceItems(instance: IModule, condition?: (target: DataSource) => boolean): DataSource[];
      checkFilename(file: ExternalAsset, pathname?: string): string;
      setLocalUri(file: ExternalAsset, replace?: boolean): FileOutput;
      getLocalUri(data: FileData<ExternalAsset>): string;
      getMimeType(data: FileData<ExternalAsset>): string;
      openThread(instance: IModule, data: IFileThread, timeout?: number): boolean;
      closeThread(instance: IModule | null, data: IFileThread, callback?: (...args: unknown[]) => void): boolean;
      addProcessTimeout(instance: IModule, file: ExternalAsset, timeout: number): void;
      removeProcessTimeout(instance: IModule, file: ExternalAsset): void;
      getProcessTimeout(handler: InstallData): number;
      clearProcessTimeout(): void;
      scheduleTask(uri: string | URL, data: unknown, priority: number): Promise<unknown>;
      scheduleTask(uri: string | URL, data: unknown, thenCallback?: (...args: unknown[]) => unknown, catchCallback?: (...args: unknown[]) => unknown, priority?: number): Promise<unknown>;
      setTaskLimit(value: number): void;
      addDownload(value: number | Buffer | string, encoding: BufferEncoding): number;
      addDownload(value: number | Buffer | string, type?: number | BufferEncoding, encoding?: BufferEncoding): number;
      getDownload(type?: number): [number, number];
      checkHash(checksum: ChecksumValue, options: CheckHashOptions): boolean;
      checkHash(checksum: ChecksumValue, data: Bufferable | null, uri: string | URL | undefined): boolean;
      checkHash(checksum: ChecksumValue, data: Bufferable, options?: CheckHashOptions): boolean;
      transformAsset(data: IFileThread, parent?: ExternalAsset, override?: boolean): Promise<boolean>;
      addCopy(data: FileCommand<ExternalAsset>, saveAs?: string, replace?: boolean): string | undefined;
      handleFilePermission(file: ExternalAsset): void;
      findMime(file: ExternalAsset, rename?: boolean): Promise<string>;
      getUTF8String(file: ExternalAsset, uri?: string): string;
      getBuffer(file: ExternalAsset, minStreamSize?: number): Promise<Buffer | null> | Buffer | null;
      getCacheDir(url: string | URL, createDir?: boolean): string;
      setAssetContent(file: ExternalAsset, content: string, options?: AssetContentOptions): string;
      getAssetContent(file: ExternalAsset, content?: string): string | undefined;
      writeBuffer(file: ExternalAsset, options?: WriteFileOptions): Buffer | null;
      writeImage(document: string | string[], output: OutputFinalize<ExternalAsset>): boolean;
      compressFile(file: ExternalAsset, overwrite?: boolean): Promise<unknown>;
      fetchObject(uri: string | URL, format: BufferFormat): Promise<object | null>;
      fetchObject(uri: string | URL, options?: OpenOptions): Promise<object | null>;
      fetchBuffer(uri: string | URL, options?: OpenOptions): Promise<Buffer | string | null>;
      fetchFiles(uri: string | URL, pathname: string): Promise<string[]>;
      fetchFiles(uri: string | URL, options?: Aria2Options | RcloneOptions): Promise<string[]>;
      updateProgress(name: "request", id: number | string, receivedBytes: number, totalBytes: number, dataTime?: HighResolutionTime): void;
      start(emptyDir?: boolean): Promise<FinalizeResult>;
      processAssets(emptyDir?: boolean, using?: ExternalAsset[]): void;
      deleteFile(src: string, promises: boolean): Promise<void>;
      deleteFile(src: string, options: DeleteFileOptions & DeleteFileAddendum, promises: boolean): Promise<void>;
      deleteFile(src: string, callback?: NoParamCallback): unknown;
      deleteFile(src: string, options: DeleteFileOptions & DeleteFileAddendum, callback?: NoParamCallback): unknown;
      restart(recursive?: boolean | "abort", emptyDir?: boolean): void;
      restart(recursive?: boolean | "abort", exclusions?: string[], emptyDir?: boolean): void;
      finalizeCompress(assets: ExternalAsset[]): Promise<void>;
      finalizeDocument(): Promise<void>;
      finalizeTask(assets: (ExternalAsset & Required<TaskAction>)[]): Promise<void>;
      finalizeCloud(): Promise<void>;
      finalizeChecksum(): Promise<void>;
      finalizeCleanup(): Promise<void>;
      finalize(): Promise<void>;
      removeFiles(): void;
      close(): void;
      reset(): boolean;
      get baseDirectory(): string;
      get config(): RequestData;
      get assets(): ExternalAsset[];
      get incremental(): IncrementalMatch;
      set restarting(value);
      get restarting(): boolean;
      get delayed(): number;
      set cleared(value);
      get cleared(): boolean;
      set finalizeState(value);
      get finalizeState(): number;
      get retryLimit(): number;

      /* Set */
      add(value: string, parent?: ExternalAsset, type?: number): this;
      delete(value: string, emptyDir?: boolean): boolean;
      has(value: unknown): value is string;

      /* EventEmitter */
      on(event: "end", listener: PostFinalizeCallback): this;
      on(event: "asset:permission", listener: (file: ExternalAsset) => void): this;
      once(event: "end", listener: PostFinalizeCallback): this;
      once(event: "asset:permission", listener: (file: ExternalAsset) => void): this;
      emit(event: "end", result: FinalizeResult): boolean;
      emit(event: "asset:permission", file: ExternalAsset): boolean;
  }

  interface FileManagerConstructor extends HostConstructor {
      purgeMemory(percent?: number, limit?: number | boolean, parent?: number | boolean): Promise<number>;
      loadSettings(settings: Settings, password?: string): boolean;
      loadSettings(settings: Settings, permission?: PermissionReadWrite, password?: string): boolean;
      sanitizeAssets(assets: ExternalAsset[], exclusions?: string[]): ExternalAsset[];
      writeChecksum(root: string, options: ChecksumOptions): Promise<string[]>;
      writeChecksum(root: string, to?: string, options?: ChecksumOptions): Promise<string[] | null>;
      verifyChecksum(root: string, options: ChecksumOptions): Promise<[string[], string[], number] | null>;
      verifyChecksum(root: string, from?: string, options?: ChecksumOptions): Promise<[string[], string[], number] | null>;
      createFileThread(host: IFileManager, file: ExternalAsset): IFileThread;
      setTimeout(options: Record<string, number | string>): void;
      defineHttpCache(options: HttpMemorySettings, disk?: boolean): void;
      defineHttpConnect(options: HttpConnectSettings): void;
      generateSessionId(): string;
      readonly prototype: IFileManager;
      new(baseDirectory: string, config: RequestData, postFinalize?: PostFinalizeCallback): IFileManager;
      new(baseDirectory: string, config: RequestData, permission?: IPermission | null, postFinalize?: PostFinalizeCallback): IFileManager;
  }

Changelog
=========

.. versionchanged:: 0.13.6

  - ``BREAKING`` *IFileManager* properties **permission** | **sessionId** are permanently locked in the constructor.
  - *FileManagerConstructor* :alt:`function` **generateSessionId** for host sessionId tracking was created.

.. versionchanged:: 0.13.2

  - *FileManagerConstructor* :alt:`function` **writeChecksum** | **verifyChecksum** options properties **ignore** | **ignoreRoot** as :alt:`string[]` can evaluate relative glob patterns.

.. versionadded:: 0.13.0

  - *IFileManager* :alt:`function` **checkHash** for file integrity validation was created.
  - *IFileManager* :alt:`function` **removeFiles** for deleting unused files queued as :alt:`filesToRemove` was created.
  - *IFileManager* :alt:`function` **handleFilePermission** for emitting event :alt:`file:permission` was created.
  - *IFileManager* :alt:`class` **EventEmitter** can send and receive events from:

    .. hlist::
      :columns: 1

      - asset:permission

.. versionchanged:: 0.13.0

  - ``BREAKING`` *IFileManager* when parsing an invalid encoding :alt:`(BufferEncoding)` will process the file as a `Buffer <https://nodejs.org/api/buffer.html#buffers-and-typedarrays>`_ instead of assuming "**utf-8**".
  - *FileManagerConstructor* :alt:`function` **writeChecksum** | **verifyChecksum** options property :target:`include` as :alt:`string[]` can be prefixed with "**!**" to negate a subset of glob paths.

.. note:: All glob paths are evaluated with negation acting as a secondary subset filter.

.. versionchanged:: 0.12.0

  - *IFileManager* :alt:`function` **fetchFiles** using the :target:`rclone:?` protocol supports `Rclone <https://rclone.org>`_ copy commands.
  - *IFileManager* :alt:`property` getter **retryLimit** for failed attempts was created.

.. versionchanged:: 0.11.0

  - *FileManagerConstructor* :alt:`function` **writeChecksum** | **verifyChecksum** options property :target:`exclude` as :alt:`string[]` can be prefixed with "**!**" to negate a subset of glob paths.
  - *IFileManager* :alt:`function` **install** with name :alt:`watch` injected with an *NPM* package or *Watch* constructor was implemented.
  - *IFileManager* :alt:`property` **cacheToDisk** | **cacheToMemory** were made :alt:`readonly` references.

.. versionremoved:: 0.11.0

  - *IFileManager* :alt:`function` **install** with name :alt:`watch` injected with spread parameters does not conform with *Client* constructor.

.. versionadded:: 0.10.0

  - *IFileManager* :alt:`function` **checkFilename** for duplicate destination renames was created.
  - *IFileManager* :alt:`function` **finalizeChecksum** for directory hash validation was created.

.. versionchanged:: 0.10.0

  - *IFileManager* :alt:`function` return value was modified to :target:`Promise<void>`:

    .. hlist::
      :columns: 3

      - finalize
      - finalizeCompress
      - finalizeCleanup
      - finalizeCloud
      - finalizeDocument
      - finalizeTask

.. versionadded:: 0.9.0

  - *IFileManager* :alt:`function` **transformAsset** argument :target:`override` as :alt:`boolean` was created.
  - *IFileManager* :alt:`function` were created:

    .. hlist::
      :columns: 3

      - scheduleTask
      - setTaskLimit
      - updateProgress

.. versionchanged:: 0.9.0

  - *IFileManager* :alt:`function` **install** with **name** :alt:`"image"` and **target** as :alt:`ImageConstructor`.
  - *IFileManager* :alt:`function` **install** with **name** :alt:`"document" | "image" | "task"` and **handler** as :alt:`string`.
  - *IFileManager* :alt:`function` **transformAsset** return value was modified to :target:`Promise<boolean>`.

Settings
========

.. code-block::
  :caption: `View JSON <https://www.unpkg.com/squared-express/dist/squared.json>`_

  import type { BackgroundColor, ForegroundColor, LoggerProgress } from "./logger";

  interface ProcessModule {
      thread?: {
          sub_limit?: number;
      };
  }

  interface RequestModule {
      timeout?: number | string;
      disk?: {
          enabled?: boolean;
          expires?: number | string;
          limit?: number | string;
          include?: string[];
          exclude?: string[];
      };
      buffer?: {
          enabled?: boolean;
          expires?: number | string;
          limit?: number | string;
          include?: string[];
          exclude?: string[];
          limit_all?: number | string;
          purge_amount?: number | string;
          to_disk?: number | string | [number | string, (number | string)?];
      };
      connect?: {
          timeout?: number | string;
          retry_wait?: number | string;
          retry_after?: number | string;
          retry_limit?: number;
          redirect_limit?: number;
      };
  }

  interface ErrorModule {
      retry_limit?: number;
  }

  interface LoggerModule {
      progress?: LoggerProgress;
      session_id?: boolean | number;
  }

Changelog
---------

.. deprecated:: 0.12.0

  - *ErrorModule* property **recursion_limit** was renamed :target:`retry_limit`.

.. versionadded:: 0.10.0

  - *LoggerModule* property group **progress** for summary data was implemented.

.. versionadded:: 0.9.0

  - *ProcessModule* sub-property **thread.sub_limit** for maximum simultaneous downloads was implemented.

Example usage
-------------

.. code-block:: javascript

  const FileManager = require("@e-mc/file-manager");

  FileManager.loadSettings({ // Global
    process: {
      thread: { sub_limit: 16 }
    },
    request: {
      timeout: "15s",
      disk: {
        enabled: true,
        limit: "1gb", // Content-Length
        expires: "1d",
        exclude: ["https://github.com", "zip"]
      },
      buffer: {
        enabled: true,
        limit: "64mb",
        limit_all: "512mb",
        expires: "1h",
        purge_amount: 0.25 // When limit_all exceeded
      }
    },
    permission: {
      disk_read: ["**/*"],
      disk_write: ["/tmp/**"]
    }
  });

  const requestData = {
    assets: [
      { uri: "http://hostname/path/document1.png" }, // /path/workspace/document1.png
      { pathname: "output", uri: "http://hostname/path/unknown", mimeType: "image/png" }, // /path/workspace/output/unknown.png
      { pathname: "output", filename: "image2.png", uri: "http://hostname/path/document2.png" } // /path/workspace/output/image2.png
    ],
    incremental: "etag",
    threads: 8,
    log: {
      showSize: true,
      showProgress: true,
      showDiff: [
        "**/assets/*.js", // Local path
        "javascript", // application/javascript | text/javascript
        "text/css"
      ]
    }
  };

  const instance = new FileManager("/path/workspace", requestData, { disk_write: ["/path/workspace/output/**"] });
  await instance.start();

.. caution:: :target:`FileManager` is a sub-class of :doc:`Host <core>` and :doc:`Module <module>`. Their ``loadSettings`` will be called as well which forms a combined :ref:`Settings <references-e-mc-types-lib-node>` object.

References
==========

- https://www.unpkg.com/@e-mc/types/lib/squared.d.ts
- https://www.unpkg.com/@e-mc/types/lib/asset.d.ts
- https://www.unpkg.com/@e-mc/types/lib/core.d.ts
- https://www.unpkg.com/@e-mc/types/lib/filemanager.d.ts
- https://www.unpkg.com/@e-mc/types/lib/logger.d.ts
- https://www.unpkg.com/@e-mc/types/lib/module.d.ts
- https://www.unpkg.com/@e-mc/types/lib/node.d.ts
- https://www.unpkg.com/@e-mc/types/lib/request.d.ts
- https://www.unpkg.com/@e-mc/types/lib/settings.d.ts

* https://www.npmjs.com/package/@types/node