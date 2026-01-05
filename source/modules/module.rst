============
@e-mc/module
============

Interface
=========

.. highlight:: typescript

.. code-block::
  :caption: `View Source <https://www.unpkg.com/@e-mc/types/lib/index.d.ts>`_
  :emphasize-lines: 24,82-84,129,132,140,143,151,154,190,194

  import type { LogStatus } from "./squared";

  import type { IHost } from "./index";
  import type { IAbortComponent, IPermission } from "./core";
  import type { ExecCommand, LogArguments, LogComponent, LogDate, LogFailOptions, LogMessageOptions, LogOptions, LogProcessOptions, LogTime, LogType, LogValue, LoggerFormat, StatusType } from "./logger";
  import type { AsHashOptions, CheckSemVerOptions, CopyDirOptions, CopyDirResult, CopyFileOptions, CreateDirOptions, DeleteFileOptions, DirectoryActionType, FileActionType, GetTempDirOptions, GlobDirOptions, MoveFileOptions, ParseFunctionOptions, PermissionOptions, ProtocolType, ReadBufferOptions, ReadFileCallback, ReadFileOptions, ReadHashOptions, ReadTextOptions, RemoveDirOptions, WriteFileOptions } from "./module";
  import type { ErrorCode, Settings } from "./node";
  import type { LoggerFormatSettings } from "./settings";

  import type { SpawnOptions } from "node:child_process";
  import type { BinaryLike, HashOptions } from "node:crypto";
  import type { NoParamCallback } from "node:fs";
  import type { FileTypeResult } from "file-type";

  import type * as EventEmitter from "node:events";

  type BufferView = Buffer | string | NodeJS.ArrayBufferView;
  type CpuUsage = NodeJS.CpuUsage;

  interface IModule extends EventEmitter, IAbortComponent {
      readonly status: LogStatus<StatusType>[];
      readonly errors: unknown[];
      supported(major: number, minor?: number, patch?: number, lts?: boolean): boolean;
      supports(name: string, value?: boolean, locked?: boolean): boolean;
      getTempDir(options: GetTempDirOptions): string;
      getTempDir(uuidDir: boolean, createDir: boolean): string;
      getTempDir(pathname: string, createDir: boolean): string;
      getTempDir(uuidDir: boolean, filename?: string, createDir?: boolean): string;
      getTempDir(pathname?: string, filename?: string, createDir?: boolean): string;
      canRead(uri: string | URL, options?: PermissionOptions): boolean;
      canWrite(uri: string | URL, options?: PermissionOptions): boolean;
      readFile(src: string | URL): Buffer | undefined;
      readFile(src: string | URL, options?: ReadFileOptions): Promise<Buffer | string> | Buffer | string | undefined;
      readFile(src: string | URL, promises: true): Promise<Buffer | undefined>;
      readFile(src: string | URL, options: ReadFileOptions, promises: true): Promise<Buffer | string | undefined>;
      readFile(src: string | URL, callback: ReadFileCallback<Buffer | string>): Buffer | string | undefined;
      readFile(src: string | URL, options: ReadFileOptions, callback: ReadFileCallback<Buffer | string>): Buffer | string | undefined;
      writeFile(src: string | URL, data: BufferView, options?: WriteFileOptions): boolean;
      writeFile(src: string | URL, data: BufferView, promises: true): Promise<boolean>;
      writeFile(src: string | URL, data: BufferView, options: WriteFileOptions, promises: true): Promise<boolean>;
      writeFile(src: string | URL, data: BufferView, callback: NoParamCallback): void;
      writeFile(src: string | URL, data: BufferView, options: WriteFileOptions, callback: NoParamCallback): void;
      deleteFile(src: string | URL, options?: DeleteFileOptions): boolean;
      deleteFile(src: string | URL, promises: true): Promise<boolean>;
      deleteFile(src: string | URL, options: DeleteFileOptions, promises: true): Promise<boolean>;
      deleteFile(src: string | URL, callback: NoParamCallback): void;
      deleteFile(src: string | URL, options: DeleteFileOptions, callback: NoParamCallback): void;
      copyFile(src: string | URL, dest: string | URL, options?: CopyFileOptions): boolean;
      copyFile(src: string | URL, dest: string | URL, promises: true): Promise<boolean>;
      copyFile(src: string | URL, dest: string | URL, options: CopyFileOptions, promises: true): Promise<boolean>;
      copyFile(src: string | URL, dest: string | URL, callback: NoParamCallback): void;
      copyFile(src: string | URL, dest: string | URL, options: CopyFileOptions, callback: NoParamCallback): void;
      moveFile(src: string | URL, dest: string | URL, options?: MoveFileOptions): boolean;
      moveFile(src: string | URL, dest: string | URL, promises: true): Promise<boolean>;
      moveFile(src: string | URL, dest: string | URL, options: MoveFileOptions, promises: true): Promise<boolean>;
      moveFile(src: string | URL, dest: string | URL, callback: NoParamCallback): void;
      moveFile(src: string | URL, dest: string | URL, options: MoveFileOptions, callback: NoParamCallback): void;
      createDir(src: string | URL, options?: CreateDirOptions): boolean;
      createDir(src: string | URL, promises: true): Promise<boolean>;
      createDir(src: string | URL, options: CreateDirOptions, promises: true): Promise<boolean>;
      createDir(src: string | URL, callback: NoParamCallback): void;
      createDir(src: string | URL, options: CreateDirOptions, callback: NoParamCallback): void;
      removeDir(src: string | URL, options?: RemoveDirOptions): boolean;
      removeDir(src: string | URL, promises: true): Promise<boolean>;
      removeDir(src: string | URL, options: RemoveDirOptions, promises: true): Promise<boolean>;
      removeDir(src: string | URL, callback: NoParamCallback): void;
      removeDir(src: string | URL, options: RemoveDirOptions, callback: NoParamCallback): void;
      allSettled(values: readonly PromiseLike<unknown>[], rejected?: LogValue, type?: LogType): Promise<PromiseFulfilledResult<unknown>[]>;
      allSettled(values: readonly PromiseLike<unknown>[], rejected?: LogValue, options?: LogFailOptions): Promise<PromiseFulfilledResult<unknown>[]>;
      formatMessage(type: LogType, title: string, value: LogValue, message?: unknown, options?: LogMessageOptions): void;
      formatFail(type: LogType, title: string, value: LogValue, message?: unknown, options?: LogFailOptions): void;
      writeFail(value: LogValue, message: unknown, options: LogFailOptions): void;
      writeFail(value: LogValue, message?: unknown, type?: LogType | LogFailOptions): void;
      writeTimeProcess(title: string, value: string, startTime: LogTime, options?: LogProcessOptions): void;
      writeTimeElapsed(title: string, value: LogValue, startTime: LogTime, options?: LogMessageOptions): void;
      checkPackage(err: unknown, name: string | undefined, options: LogType): boolean;
      checkPackage(err: unknown, name: string | undefined, options: LogFailOptions): boolean;
      checkPackage(err: unknown, name: string | undefined, value?: LogValue, options?: LogFailOptions | LogType): boolean;
      checkFail(message: unknown, options: LogFailOptions): LogArguments | false | undefined;
      writeLog(component: LogComponent, queue?: boolean): void;
      writeLog(type: StatusType, value: unknown, options: LogOptions): void;
      writeLog(type: StatusType, value: unknown, from: string, source?: string): void;
      writeLog(type: StatusType, value: unknown, timeStamp?: LogDate, from?: string, source?: string): void;
      writeLog(type: StatusType, value: unknown, timeStamp?: LogDate, duration?: number, from?: string, source?: string): void;
      addLog(component: LogComponent, queue?: boolean): void;
      addLog(type: StatusType, value: unknown, options: LogOptions): void;
      addLog(type: StatusType, value: unknown, from: string, source?: string): void;
      addLog(type: StatusType, value: unknown, timeStamp?: LogDate, from?: string, source?: string): void;
      addLog(type: StatusType, value: unknown, timeStamp?: LogDate, duration?: number, from?: string, source?: string): void;
      getLog(...type: StatusType[]): LogStatus<StatusType>[];
      flushLog(): void;
      willAbort(value: unknown): boolean;
      /** @deprecated hasPermission("fs") */
      hasOwnPermission(): boolean;
      hasPermission(type: "fs" | "memory" | "memory.user" | "worker" | string, ...values: unknown[]): boolean;
      isFatal(err?: unknown): boolean;
      detach(): void;
      reset(): void;
      get moduleName(): string;
      set host(value);
      get host(): IHost | null;
      set permission(value);
      get permission(): IPermission | null;
      get aborted(): boolean;
      set abortable(value);
      get abortable(): boolean;
      get threadable(): boolean;
      set sessionId(value);
      get sessionId(): string;
      set broadcastId(value);
      get broadcastId(): string | string[];
      set silent(value);
      get silent(): boolean;
      get logType(): LogType;
      set logLevel(value: number | string);
      get logLevel(): number;
      get statusType(): StatusType;
      set tempDir(value);
      get tempDir(): string;

      /* EventEmitter */
      on(event: "exec", listener: (command: ExecCommand, options?: SpawnOptions) => void): this;
      on(event: "error", listener: (err: Error) => void): this;
      on(event: "file:read", listener: (src: string, data: Buffer | string, options?: ReadFileOptions) => void): this;
      on(event: "file:write", listener: (src: string, options?: WriteFileOptions) => void): this;
      on(event: "file:delete", listener: (src: string, options?: DeleteFileOptions) => void): this;
      on(event: "file:copy", listener: (dest: string, options?: CopyFileOptions) => void): this;
      on(event: "file:move", listener: (dest: string, options?: MoveFileOptions) => void): this;
      on(event: "file:permission", listener: (src: string, type?: FileActionType) => void): this;
      on(event: "dir:create", listener: (src: string, options?: CreateDirOptions) => void): this;
      on(event: "dir:remove", listener: (src: string, options?: RemoveDirOptions) => void): this;
      on(event: "dir:permission", listener: (src: string, type?: DirectoryActionType) => void): this;
      once(event: "exec", listener: (command: ExecCommand, options?: SpawnOptions) => void): this;
      once(event: "error", listener: (err: Error) => void): this;
      once(event: "file:read", listener: (src: string, data: Buffer | string, options?: ReadFileOptions) => void): this;
      once(event: "file:write", listener: (src: string, options?: WriteFileOptions) => void): this;
      once(event: "file:delete", listener: (src: string, options?: DeleteFileOptions) => void): this;
      once(event: "file:copy", listener: (dest: string, options?: CopyFileOptions) => void): this;
      once(event: "file:move", listener: (dest: string, options?: MoveFileOptions) => void): this;
      once(event: "file:permission", listener: (src: string, type?: FileActionType) => void): this;
      once(event: "dir:create", listener: (src: string, options?: CreateDirOptions) => void): this;
      once(event: "dir:remove", listener: (src: string, options?: RemoveDirOptions) => void): this;
      once(event: "dir:permission", listener: (src: string, type?: DirectoryActionType) => void): this;
      emit(event: "exec", command: ExecCommand, options?: SpawnOptions): boolean;
      emit(event: "error", err: Error): boolean;
      emit(event: "file:read", src: string, data: Buffer | string, options?: ReadFileOptions): boolean;
      emit(event: "file:write", src: string, options?: WriteFileOptions): boolean;
      emit(event: "file:delete", src: string, options?: DeleteFileOptions): boolean;
      emit(event: "file:copy", dest: string, options?: CopyFileOptions): boolean;
      emit(event: "file:move", dest: string, options?: MoveFileOptions): boolean;
      emit(event: "file:permission", src: string, type?: FileActionType): boolean;
      emit(event: "dir:create", src: string, options?: CreateDirOptions): boolean;
      emit(event: "dir:remove", src: string, options?: RemoveDirOptions): boolean;
      emit(event: "dir:permission", src: string, type?: DirectoryActionType): boolean;
  }

  interface ModuleConstructor {
      PROCESS_TIMEOUT: number;
      LOG_STYLE_FAIL: LogMessageOptions;
      LOG_STYLE_SUCCESS: LogMessageOptions;
      LOG_STYLE_INFO: LogMessageOptions;
      LOG_STYLE_WARN: LogMessageOptions;
      LOG_STYLE_NOTICE: LogMessageOptions;
      LOG_STYLE_REVERSE: LogMessageOptions;
      readonly VERSION: string;
      readonly LOG_TYPE: LogType;
      readonly LOG_FORMAT: LoggerFormatSettings<LoggerFormat<number>>;
      readonly STATUS_TYPE: StatusType;
      readonly PLATFORM_WIN32: boolean;
      readonly MAX_TIMEOUT: number;
      readonly TEMP_DIR: string;
      constructorOf(value: unknown, moduleName?: string): value is ModuleConstructor;
      /** @deprecated @e-mc/types */
      supported(major: number, minor?: number, patch?: number, lts?: boolean): boolean;
      formatMessage(type: LogType, title: string, value: LogValue, message?: unknown, options?: LogMessageOptions): void;
      writeFail(value: LogValue, message?: unknown, options?: LogFailOptions | LogType): void;
      enabled(key: string, username?: string): boolean;
      parseFunction(value: unknown, options?: ParseFunctionOptions): ((...args: unknown[]) => Promise<unknown> | unknown) | null;
      parseFunction(value: unknown, absolute: boolean, sync?: boolean): ((...args: unknown[]) => Promise<unknown> | unknown) | null;
      asString(value: unknown, cacheKey?: boolean | "throws"): string;
      asHash(data: BinaryLike, options?: AsHashOptions): string;
      asHash(data: BinaryLike, algorithm?: string, options?: HashOptions): string;
      asHash(data: BinaryLike, algorithm?: string, digest?: BinaryToTextEncoding): string;
      readHash(value: string | URL, options?: ReadHashOptions): Promise<string>;
      toPosix(value: unknown, normalize: boolean): string;
      toPosix(value: unknown, filename?: string, normalize?: boolean): string;
      hasLogType(value: LogType): boolean;
      isURL(value: string, ...exclude: string[]): boolean;
      isFile(value: string | URL, type?: ProtocolType): boolean;
      isDir(value: string | URL, absolute?: boolean): boolean;
      isPath(value: string | URL, type?: "unc" | "unc-exists"): boolean;
      isPath(value: string | URL, isFile?: boolean): boolean;
      /** @deprecated @e-mc/types */
      isErrorCode(err: unknown, ...code: unknown[]): err is Required<ErrorCode>;
      fromLocalPath(value: string): string;
      resolveFile(value: string): string;
      resolvePath(value: string, base: string | URL): string;
      joinPath(...values: [...paths: unknown[], normalize: boolean][]): string;
      joinPath(...values: unknown[]): string;
      normalizePath(value: unknown, flags?: boolean | number): string;
      createDir(value: string | URL, overwrite?: boolean): boolean;
      removeDir(value: string | URL, sinceCreated: number, recursive?: boolean): boolean;
      removeDir(value: string | URL, empty?: boolean, recursive?: boolean): boolean;
      copyDir(src: string | URL, dest: string | URL, move?: boolean, recursive?: boolean): Promise<CopyDirResult>;
      copyDir(src: string | URL, dest: string | URL, options?: CopyDirOptions): Promise<CopyDirResult>;
      globDir(src: string | URL, pattern: string | string[], recursive: boolean | number): Promise<string[]>;
      globDir(src: string | URL, pattern: string | string[], options?: GlobDirOptions): Promise<string[]>;
      renameFile(src: string | URL, dest: string | URL, throws?: boolean): boolean;
      streamFile(value: string | URL, cache: boolean): Promise<Buffer | string>;
      streamFile(value: string | URL, options: ReadBufferOptions): Promise<Buffer | string>;
      streamFile(value: string | URL, cache?: boolean | ReadBufferOptions, options?: ReadBufferOptions): Promise<Buffer | string>;
      readText(value: string | URL, cache: boolean): string;
      readText(value: string | URL, options: ReadTextOptions): Promise<string> | string;
      readText(value: string | URL, encoding?: BufferEncoding | ReadTextOptions, cache?: boolean): string;
      readBuffer(value: string | URL, options: ReadBufferOptions): Promise<Buffer | null> | Buffer | null;
      readBuffer(value: string | URL, cache?: boolean | ReadBufferOptions): Buffer | null;
      resolveMime(data: string | Buffer | Uint8Array | ArrayBuffer): Promise<FileTypeResult | undefined>;
      lookupMime(value: string, extension?: boolean): string;
      initCpuUsage(instance?: IModule): CpuUsage;
      getCpuUsage(start: CpuUsage, format: true): string;
      getCpuUsage(start: CpuUsage, format?: boolean): number;
      getMemUsage(format: true): string;
      getMemUsage(format?: boolean): number;
      formatCpuMem(start: CpuUsage, all?: boolean): string;
      getPackageVersion(name: string | [string, string], options?: PackageVersionOptions): string;
      checkSemVer(name: string | [string, string], options: CheckSemVerOptions): boolean;
      checkSemVer(name: string | [string, string], min: number | string, max?: number | string): boolean;
      checkSemVer(name: string | [string, string], min: number | string, max: number | string, options?: Omit<CheckSemVerOptions, "min" | "max" | "equals">): boolean;
      /** @deprecated @e-mc/types */
      sanitizeCmd(value: string, ...args: unknown[]): string;
      /** @deprecated @e-mc/types */
      sanitizeArgs(value: string, doubleQuote?: boolean): string;
      /** @deprecated @e-mc/types */
      sanitizeArgs(values: string[], doubleQuote?: boolean): string[];
      purgeMemory(percent: number, parent: boolean): Promise<number>;
      purgeMemory(percent: number, limit: number, parent?: boolean): Promise<number>;
      purgeMemory(percent?: number, limit?: number | boolean, parent?: unknown): Promise<number>;
      canWrite(name: "temp" | "home"): boolean;
      loadSettings(settings: Settings, password?: string): boolean;
      readonly prototype: IModule<IHost>;
      new(): IModule<IHost>;
  }

Changelog
=========

.. versionadded:: 0.13.6

  - *IModule* :alt:`function` **supports** argument :target:`locked` as :alt:`boolean` can **permanently** lock these properties:

    .. hlist::
      :columns: 1

      - sessionId
      - broadcastId
      - permission

.. versionadded:: 0.13.0

  - *IModule* :alt:`class` **EventEmitter** can send and receive events from:

    .. hlist::
      :columns: 1

      - file\:permission
      - dir:permission

.. versionchanged:: 0.13.0

  - *ModuleConstructor* :alt:`function` **isDir** argument :target:`absolute` as :alt:`boolean` was created.
  - *IModule* :alt:`function` **writeLog** uses same method signature as :alt:`function` **addLog**.

.. deprecated:: 0.13.0

  - *ModuleConstructor* :alt:`function` **isErrorCode** was relocated into :doc:`types`.

.. versionchanged:: 0.12.7/0.11.10/0.10.14/0.9.22

  - ``BREAKING`` *ModuleConstructor* :alt:`function` **joinPath** did not preserve leading and trailing spaces for Unix paths.

.. versionchanged:: 0.12.2/0.11.9/0.10.13

  - ``BREAKING`` *ModuleConstructor* :alt:`function` **isURL** no longer uses :target:`URL.canParse` for validation. The native method accepted values without the "**://**" convention.

.. versionadded:: 0.12.0

  - *Node.js Permission Model* was implemented with one compatibility difference. **moveFile** uses :alt:`fs-read` and :alt:`fs-write` on the source file with :target:`--permission`.
  - *ModuleConstructor* :alt:`function` **constructorOf** for universal detection using symbols was created.
  - *IModule* :alt:`function` **hasPermission** for context resolution was created.

.. versionchanged:: 0.12.0

  - *IModule* :alt:`function` **isFatal** validates error objects are an instance of :ref:`Error <references-mdn-error>`.

.. versionremoved:: 0.12.0

  - ``BREAKING`` *ModuleConstructor* :alt:`function` **getPackageVersion** optional arguments **unstable** | **startDir** | **baseDir** are only available in :target:`options` as :alt:`PackageVersionOptions`.

.. deprecated:: 0.12.0

  - *ModuleConstructor* :alt:`function` **sanitizeCmd** | **sanitizeArgs** were relocated into :doc:`types`.
  - *IModule* :alt:`function` **hasOwnPermission** can be called through :target:`hasPermission("fs")`.

.. versionremoved:: 0.11.0

  - ``BREAKING`` *ModuleConstructor* :alt:`function` **checkSemVer** optional arguments **unstable** | **startDir** are only available in :target:`options` as :alt:`CheckSemVerOptions`.

.. versionadded:: 0.10.5

  - *ModuleConstructor* :alt:`function` **globDir** for recursive file searches was created.

.. versionadded:: 0.10.0

  - *ModuleConstructor* :alt:`property` **PLATFORM_WIN32** was created.
  - *IModule* :alt:`property` accessor **silent** for console messages was created.

.. versionchanged:: 0.10.0

  - *ModuleConstructor* :alt:`function` **asHash** argument :target:`minLength` was replaced with :target:`digest` as :alt:`BinaryToTextEncoding`.

.. deprecated:: 0.10.0

  - *ModuleConstructor* :alt:`function` **supported** was relocated into :doc:`types`.

.. versionadded:: 0.9.0

  - *ModuleConstructor* :alt:`property` **LOG_FORMAT** was created.

.. versionchanged:: 0.9.0

  - *IModule* :alt:`function` **src** and **dest** arguments can accept a :ref:`URL <references-nodejs-url>` instance:

    .. hlist::
      :columns: 4

      - canRead
      - canWrite
      - readFile
      - writeFile
      - deleteFile
      - copyFile
      - moveFile
      - createDir
      - removeDir
      - streamFile :alt:`(static)`

.. versionadded:: 0.8.7

  - *IModule* :alt:`function` **getPackageVersion** argument :target:`baseDir` as :alt:`string` was created.

Settings
========

.. code-block::
  :caption: `View JSON <https://www.unpkg.com/squared-express/dist/squared.json>`_

  import type { BackgroundColor, ForegroundColor, LogMessageOptions, LogTypeValue, LoggerProgress, LoggerStatus } from "./logger";
  import type { LoggerProcessSettings } from "./settings";

  import type { BinaryLike, CipherGCMTypes } from "crypto";
  import type { SecureVersion } from "tls";

  interface NodeModule {
      process?: {
          cpu_usage?: boolean;
          memory_usage?: boolean;
          inline?: boolean;
      };
      require?: {
          ext?: string | string[] | boolean;
          npm?: boolean;
          inline?: boolean;
      };
      posix?: {
          strict?: boolean;
      };
      settings?: {
          package_manager?: "npm" | "yarn" | "pnpm";
      };
  }

  interface ProcessModule {
      env?: {
          apply?: boolean;
      };
      cipher?: {
          algorithm?: CipherGCMTypes;
          key?: BinaryLike;
          iv?: BinaryLike;
      };
      password?: string;
  }

  interface MemoryModule {
      settings?: {
          users?: boolean | string[];
          cache_disk?: {
              enabled?: boolean;
              min_size?: number | string;
              max_size?: number | string;
              include?: string[];
              exclude?: string[];
              expires?: number | string;
          };
      };
  }

  interface PermissionModule {
      home_read?: boolean;
      home_write?: boolean;
      process_exec?: (string | ExecOptions)[];
  }

  interface ErrorModule {
      out?: string | (err: Error, data: LogTypeValue, require?: NodeRequire) => void;
      fatal?: boolean;
      settings?: {
          trap_exceptions?: boolean;
      };
  }

  interface TempModule {
      dir?: string;
      env?: string;
      os?: boolean;
      write?: boolean;
  }

  interface LoggerModule {
      enabled?: boolean;
      level?: number,
      production?: string[];
      format?: {
          title?: {
              width?: number;
              color?: ForegroundColor;
              bg_color?: BackgroundColor;
              bold?: boolean;
              justify?: "left" | "center" | "right";
              braces?: string;
              as?: StringMap;
          };
          value?: {
              width?: number;
              color?: ForegroundColor;
              bg_color?: BackgroundColor;
              bold?: boolean;
              justify?: "left" | "center" | "right";
          },
          hint?: {
              width?: number;
              color?: ForegroundColor;
              bg_color?: BackgroundColor;
              bold?: boolean;
              braces?: [string, string];
              as?: StringMap;
              unit?: "auto" | "s" | "ms";
          };
          message?: {
              width?: number;
              color?: ForegroundColor;
              bg_color?: BackgroundColor;
              bold?: boolean;
              braces?: [string, string];
          };
          meter?: {
              color?: ForegroundColor;
              bg_color?: BackgroundColor;
              bg_alt_color?: BackgroundColor;
              bold?: boolean;
          };
          error?: {
              color?: ForegroundColor;
              alt_color?: ForegroundColor;
              bg_color?: BackgroundColor;
              braces?: [string, string];
          };
      };
      meter?: {
          http?: number;
          image?: number;
          compress?: number;
          process?: number;
      };
      broadcast?: {
          enabled?: boolean;
          out?: string | (value: string, options: LogMessageOptions, require?: NodeJS.Require) => void;
          color?: boolean;
          port?: number | number[];
          secure?: {
              port?: number | number[];
              ca?: string;
              key?: string;
              cert?: string;
              version?: SecureVersion
          };
      };
      status?: boolean | LoggerStatus;
      progress?: LoggerProgress;
      color?: boolean;
      message?: boolean;
      stdout?: boolean;
      abort?: boolean;
      unknown?: boolean | LoggerColor;
      system?: boolean | LoggerColor;
      process?: boolean | LoggerProcessSettings;
      image?: boolean | LoggerColor;
      compress?: boolean | LoggerColor;
      watch?: boolean | LoggerColor;
      file?: boolean | LoggerColor;
      cloud?: boolean | LoggerColor;
      db?: boolean | LoggerColor;
      time_elapsed?: boolean | LoggerColor;
      time_process?: boolean | LoggerColor;
      exec?: boolean | LoggerColor;
      http?: boolean | LoggerColor;
      node?: boolean | LoggerColor;
      session_id?: boolean | number;
      stack_trace?: boolean | number;
  }

Changelog
---------

.. versionchanged:: 0.13.0

  - *MemoryModule* settings property **cache_disk.include** can be prefixed with "**!**" to negate a subset of glob paths.

.. versionchanged:: 0.12.0

  - *NodeModule* property **posix.strict** was enabled by default.
  - *LoggerProcessSettings* property **enabled** was implemented.

.. versionadded:: 0.11.2

  - *NodeModule* group **posix** property **strict** for mixed pattern expressions with Windows was created.

.. versionadded:: 0.11.0

  - *TempModule* property **os** for system global temp directory was created.
  - *ErrorModule* settings property **trap_exceptions** for global process error handling was created.
  - *NodeModule* settings property **package_manager** for module installations was created.

.. versionchanged:: 0.11.0

  - *MemoryModule* settings property **cache_disk.exclude** can be prefixed with "**!**" to negate a subset of glob paths.

.. versionadded:: 0.10.0

  - *LoggerModule* group **format** block :target:`error` for output display was created.
  - *LoggerModule* group **format** property **braces** for text separation was implemented.
  - *LoggerModule* group **progress** for summary data was created.
  - *TempModule* property **env** for system user local temp directory was  was created.

.. versionadded:: 0.8.6

  - *PermissionModule* properties **home_read** | **home_write** were implemented.

References
==========

- https://www.unpkg.com/@e-mc/types/lib/core.d.ts
- https://www.unpkg.com/@e-mc/types/lib/logger.d.ts
- https://www.unpkg.com/@e-mc/types/lib/module.d.ts
- https://www.unpkg.com/@e-mc/types/lib/node.d.ts
- https://www.unpkg.com/@e-mc/types/lib/settings.d.ts

* https://www.npmjs.com/package/@types/node