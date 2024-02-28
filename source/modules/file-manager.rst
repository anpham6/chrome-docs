==================
@e-mc/file-manager
==================

- **npm** i *@e-mc/file-manager*

Interface
=========

.. highlight:: typescript

.. code-block::
  :caption: `View Source <https://www.unpkg.com/@e-mc/types/lib/index.d.ts>`_

  import type { DataSource, IncrementalMatch, TaskAction } from "./squared";

  import type { DocumentConstructor, HostConstructor, ICloud, ICompress, IDocument, IHost, IImage, IModule, IRequest, ITask, ImageConstructor, TaskConstructor, WatchInstance } from "./index";
  import type { ExternalAsset, FileCommand, FileData, IFileThread, OutputFinalize } from "./asset";
  import type { IPermission, PermissionReadWrite } from "./core";
  import type { AssetContentOptions, ChecksumOptions, DeleteFileAddendum, FileOutput, FinalizeResult, FindAssetOptions, IHttpDiskCache, IHttpMemoryCache, InstallData, PostFinalizeCallback, ReplaceOptions } from "./filemanager";
  import type { ExecCommand } from "./logger";
  import type { CopyFileOptions, CreateDirOptions, DeleteFileOptions, MoveFileOptions, ReadFileOptions, RemoveDirOptions, WriteFileOptions } from "./module";
  import type { RequestData, Settings } from "./node";
  import type { Aria2Options, BufferFormat, OpenOptions } from "./request";
  import type { CloudModule, CompressModule, DbModule, DocumentModule, HttpConnectSettings, HttpMemorySettings, ImageModule, RequestModule, TaskModule, WatchModule } from "./settings";

  import type { SpawnOptions } from "child_process";
  import type { NoParamCallback } from "fs";

  interface IFileManager extends IHost, Set<string> {
      processTimeout: number;
      cacheToDisk: IHttpDiskCache<ExternalAsset>;
      cacheToMemory: IHttpMemoryCache<ExternalAsset>;
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
      install(name: "document", target: DocumentConstructor<IFileManager, ExternalAsset>, module?: DocumentModule): IDocument<IFileManager, ExternalAsset> | undefined;
      install(name: "task", target: TaskConstructor, module?: TaskModule): ITask | undefined;
      install(name: "cloud", handler: string, module?: CloudModule): ICloud | undefined;
      install(name: "cloud", module?: CloudModule): ICloud | undefined;
      install(name: "db", module?: DbModule): IDb | undefined;
      install(name: "image", targets: Map<string, ImageConstructor>, module?: ImageModule): void;
      install(name: "watch", module: WatchModule): WatchInstance<ExternalAsset> | undefined;
      install(name: "watch", interval?: number | string, port?: number | string, securePort?: number | string, extensions?: unknown[]): WatchInstance<ExternalAsset> | undefined;
      install(name: "compress", module?: CompressModule): ICompress<CompressModule> | undefined;
      install(name: string, ...args: unknown[]): IModule | undefined;
      using(...items: ExternalAsset[] | [boolean, ...ExternalAsset[]]): this;
      contains(item: ExternalAsset, condition?: (target: ExternalAsset) => boolean): boolean;
      removeCwd(value: unknown): string;
      findAsset(value: string | URL, instance: IModule | null): ExternalAsset | undefined;
      findAsset(value: string | URL, options?: FindAssetOptions<ExternalAsset>): ExternalAsset | undefined;
      removeAsset(file: ExternalAsset): boolean;
      replace(file: ExternalAsset, replaceWith: string, options: ReplaceOptions): boolean;
      replace(file: ExternalAsset, replaceWith: string, mimeType?: string | ReplaceOptions): boolean;
      rename(file: ExternalAsset, value: string): boolean;
      performAsyncTask(): void;
      removeAsyncTask(): void;
      completeAsyncTask(err?: unknown, uri?: string, parent?: ExternalAsset, type?: number): void;
      performFinalize(override?: boolean): void;
      hasDocument(instance: IModule, document: string | string[] | undefined): boolean;
      getDocumentAssets(instance: IModule, condition?: (target: ExternalAsset) => boolean): ExternalAsset[];
      getDataSourceItems(instance: IModule, condition?: (target: DataSource) => boolean): DataSource[];
      setLocalUri(file: ExternalAsset, replace?: boolean): FileOutput;
      getLocalUri(data: FileData<ExternalAsset>): string;
      getMimeType(data: FileData<ExternalAsset>): string;
      openThread(instance: IModule, data: IFileThread, timeout?: number): boolean;
      closeThread(instance: IModule | null, data: IFileThread, callback?: (...args: unknown[]) => void): boolean;
      addProcessTimeout(instance: IModule, file: ExternalAsset, timeout: number): void;
      removeProcessTimeout(instance: IModule, file: ExternalAsset): void;
      getProcessTimeout(handler: InstallData): number;
      clearProcessTimeout(): void;
      scheduleTask(url: string | URL, data: unknown, priority: number): Promise<unknown>;
      scheduleTask(url: string | URL, data: unknown, thenCallback?: (...args: unknown[]) => unknown, catchCallback?: (...args: unknown[]) => unknown, priority?: number): Promise<unknown>;
      setTaskLimit(value: number): void;
      addDownload(value: number | Buffer | string, encoding: BufferEncoding): number;
      addDownload(value: number | Buffer | string, type?: number | BufferEncoding, encoding?: BufferEncoding): number;
      getDownload(type?: number): [number, number];
      transformAsset(data: IFileThread, parent?: ExternalAsset): Promise<void>;
      addCopy(data: FileCommand<ExternalAsset>, saveAs?: string, replace?: boolean): string | undefined;
      findMime(file: ExternalAsset, rename?: boolean): Promise<string>;
      getUTF8String(file: ExternalAsset, uri?: string): string;
      getBuffer(file: ExternalAsset, minStreamSize?: number): Promise<Buffer> | Buffer | null;
      getCacheDir(url: string | URL, createDir?: boolean): string;
      setAssetContent(file: ExternalAsset, content: string, options?: AssetContentOptions): string;
      getAssetContent(file: ExternalAsset, content?: string): string | undefined;
      writeBuffer(file: ExternalAsset, options?: WriteFileOptions): Buffer | null;
      writeImage(document: string | string[], output: OutputFinalize<ExternalAsset>): boolean;
      compressFile(file: ExternalAsset, overwrite?: boolean): Promise<unknown>;
      fetchObject(uri: string | URL, format: BufferFormat): Promise<object | null>;
      fetchObject(uri: string | URL, options?: OpenOptions | BufferFormat): Promise<object | null>;
      fetchBuffer(uri: string | URL, options?: OpenOptions): Promise<Buffer | string | null>;
      fetchFiles(uri: string | URL, pathname: string): Promise<string[]>;
      fetchFiles(uri: string | URL, options?: Aria2Options): Promise<string[]>;
      updateProgress(name: "request", id: number | string, receivedBytes: number, totalBytes: number, dataTime?: HighResolutionTime): void;
      start(emptyDir?: boolean): Promise<FinalizeResult>;
      processAssets(emptyDir?: boolean, using?: ExternalAsset[]): void;
      deleteFile(src: string, promises: boolean): Promise<void>;
      deleteFile(src: string, options: DeleteFileOptions & DeleteFileAddendum, promises: boolean): Promise<void>;
      deleteFile(src: string, callback?: NoParamCallback): unknown;
      deleteFile(src: string, options: DeleteFileOptions & DeleteFileAddendum, callback?: NoParamCallback): unknown;
      restart(recursive?: boolean | "abort", emptyDir?: boolean): void;
      restart(recursive?: boolean | "abort", exclusions?: string[], emptyDir?: boolean): void;
      finalizeCompress(assets: ExternalAsset[]): Promise<unknown>;
      finalizeDocument(): Promise<unknown>;
      finalizeTask(assets: (ExternalAsset & Required<TaskAction>)[]): Promise<unknown>;
      finalizeCloud(): Promise<unknown>;
      finalizeCleanup(): Promise<unknown>;
      finalize(): Promise<void>;
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

      /* Set */
      add(value: string, parent?: ExternalAsset, type?: number): this;
      delete(value: string, emptyDir?: boolean): boolean;
      has(value: unknown): value is string;

      /* EventEmitter */
      on(event: "end", listener: PostFinalizeCallback): this;
      on(event: "exec", listener: (command: ExecCommand, options?: SpawnOptions) => void): this;
      on(event: "error", listener: (err: Error) => void): this;
      on(event: "file:read", listener: (src: string, data: Buffer | string, options?: ReadFileOptions) => void): this;
      on(event: "file:write", listener: (src: string, options?: WriteFileOptions) => void): this;
      on(event: "file:delete", listener: (src: string, options?: DeleteFileOptions) => void): this;
      on(event: "file:copy", listener: (dest: string, options?: CopyFileOptions) => void): this;
      on(event: "file:move", listener: (dest: string, options?: MoveFileOptions) => void): this;
      on(event: "dir:create", listener: (src: string, options?: CreateDirOptions) => void): this;
      on(event: "dir:remove", listener: (src: string, options?: RemoveDirOptions) => void): this;
      once(event: "end", listener: PostFinalizeCallback): this;
      once(event: "exec", listener: (command: ExecCommand, options?: SpawnOptions) => void): this;
      once(event: "error", listener: (err: Error) => void): this;
      once(event: "file:read", listener: (src: string, data: Buffer | string, options?: ReadFileOptions) => void): this;
      once(event: "file:write", listener: (src: string, options?: WriteFileOptions) => void): this;
      once(event: "file:delete", listener: (src: string, options?: DeleteFileOptions) => void): this;
      once(event: "file:copy", listener: (dest: string, options?: CopyFileOptions) => void): this;
      once(event: "file:move", listener: (dest: string, options?: MoveFileOptions) => void): this;
      once(event: "dir:create", listener: (src: string, options?: CreateDirOptions) => void): this;
      once(event: "dir:remove", listener: (src: string, options?: RemoveDirOptions) => void): this;
      emit(event: "end", result: FinalizeResult): boolean;
      emit(event: "exec", command: ExecCommand, options?: SpawnOptions): boolean;
      emit(event: "error", err: Error): boolean;
      emit(event: "file:read", src: string, data: Buffer | string, options?: ReadFileOptions): boolean;
      emit(event: "file:write", src: string, options?: WriteFileOptions): boolean;
      emit(event: "file:delete", src: string, options?: DeleteFileOptions): boolean;
      emit(event: "file:copy", dest: string, options?: CopyFileOptions): boolean;
      emit(event: "file:move", dest: string, options?: MoveFileOptions): boolean;
      emit(event: "dir:create", src: string, options?: CreateDirOptions): boolean;
      emit(event: "dir:remove", src: string, options?: RemoveDirOptions): boolean;
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
      readonly prototype: IFileManager;
      new(baseDirectory: string, config: RequestData, postFinalize?: PostFinalizeCallback): IFileManager;
      new(baseDirectory: string, config: RequestData, permission?: IPermission | null, postFinalize?: PostFinalizeCallback): IFileManager;
  }

.. versionadded:: 0.9.0

  *IFileManager* methods were created:

    .. hlist::
      :columns: 3

      - scheduleTask
      - setTaskLimit
      - updateProgress

Settings
========

.. code-block::
  :caption: `View JSON <https://www.unpkg.com/squared-express/dist/squared.json>`_

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
      recursion_limit?: number;
  }

  interface LoggerModule {
      session_id?: boolean | number;
  }

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