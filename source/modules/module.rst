============
@e-mc/module
============

- **npm** i *@e-mc/module*

Interface
=========

.. code-block:: typescript

  import type { LogStatus } from "./squared";

  import type { IHost } from "./index";
  import type { IAbortComponent, IPermission } from "./core";
  import type { ExecCommand, LOG_TYPE, LogArguments, LogComponent, LogDate, LogFailOptions, LogMessageOptions, LogOptions, LogProcessOptions, LogTime, LogType, LogValue, STATUS_TYPE, StatusType } from "./logger";
  import type { AsHashOptions, CheckSemVerOptions, CopyDirOptions, CopyDirResult, CopyFileOptions, CreateDirOptions, DeleteFileOptions, GetTempDirOptions, MoveFileOptions, NormalizeFlags, ParseFunctionOptions, PermissionOptions, ProtocolType, ReadBufferOptions, ReadFileCallback, ReadFileOptions, ReadHashOptions, ReadTextOptions, RemoveDirOptions, WriteFileOptions } from "./module";
  import type { Settings } from "./node";

  import type { NoParamCallback } from "fs";
  import type { SpawnOptions } from "child_process";
  import type { BinaryLike } from "crypto";

  import type * as EventEmitter from "events";

  import type { FileTypeResult } from "file-type";

  type BufferView = Buffer | string | NodeJS.ArrayBufferView;
  type CpuUsage = NodeJS.CpuUsage;

  interface IModule extends EventEmitter, IAbortComponent {
      readonly status: LogStatus<StatusType>[];
      readonly errors: unknown[];
      supported(major: number, minor?: number, patch?: number, lts?: boolean): boolean;
      supports(name: string, value?: boolean): boolean;
      getTempDir(options: GetTempDirOptions): string;
      getTempDir(uuidDir: boolean, createDir?: boolean): string;
      getTempDir(pathname: string, createDir?: boolean): string;
      getTempDir(uuidDir: boolean, filename: string, createDir?: boolean): string;
      getTempDir(pathname?: string, filename?: string, createDir?: boolean): string;
      canRead(uri: string, options?: PermissionOptions): boolean;
      canWrite(uri: string, options?: PermissionOptions): boolean;
      readFile(src: string): Buffer | undefined;
      readFile(src: string, options?: ReadFileOptions): Promise<Buffer | string> | Buffer | string | undefined;
      readFile(src: string, promises: true): Promise<Buffer | undefined>;
      readFile(src: string, options: ReadFileOptions, promises: true): Promise<Buffer | string | undefined>;
      readFile(src: string, callback: ReadFileCallback<Buffer>): Buffer | undefined;
      readFile(src: string, options: ReadFileOptions, callback: ReadFileCallback<Buffer | string>): Buffer | string | undefined;
      writeFile(src: string, data: BufferView, options?: WriteFileOptions): boolean;
      writeFile(src: string, data: BufferView, promises: true): Promise<boolean>;
      writeFile(src: string, data: BufferView, options: WriteFileOptions, promises: true): Promise<boolean>;
      writeFile(src: string, data: BufferView, callback: NoParamCallback): void;
      writeFile(src: string, data: BufferView, options: WriteFileOptions, callback: NoParamCallback): void;
      deleteFile(src: string, options?: DeleteFileOptions): boolean;
      deleteFile(src: string, promises: true): Promise<boolean>;
      deleteFile(src: string, options: DeleteFileOptions, promises: true): Promise<boolean>;
      deleteFile(src: string, callback: NoParamCallback): void;
      deleteFile(src: string, options: DeleteFileOptions, callback: NoParamCallback): void;
      copyFile(src: string, dest: string, options?: CopyFileOptions): boolean;
      copyFile(src: string, dest: string, promises: true): Promise<boolean>;
      copyFile(src: string, dest: string, options: CopyFileOptions, promises: true): Promise<boolean>;
      copyFile(src: string, dest: string, callback: NoParamCallback): void;
      copyFile(src: string, dest: string, options: CopyFileOptions, callback: NoParamCallback): void;
      moveFile(src: string, dest: string, options?: MoveFileOptions): boolean;
      moveFile(src: string, dest: string, promises: true): Promise<boolean>;
      moveFile(src: string, dest: string, options: MoveFileOptions, promises: true): Promise<boolean>;
      moveFile(src: string, dest: string, callback: NoParamCallback): void;
      moveFile(src: string, dest: string, options: MoveFileOptions, callback: NoParamCallback): void;
      createDir(src: string, options?: CreateDirOptions): boolean;
      createDir(src: string, promises: true): Promise<boolean>;
      createDir(src: string, options: CreateDirOptions, promises: true): Promise<boolean>;
      createDir(src: string, callback: NoParamCallback): void;
      createDir(src: string, options: CreateDirOptions, callback: NoParamCallback): void;
      removeDir(src: string, options?: RemoveDirOptions): boolean;
      removeDir(src: string, promises: true): Promise<boolean>;
      removeDir(src: string, options: RemoveDirOptions, promises: true): Promise<boolean>;
      removeDir(src: string, callback: NoParamCallback): void;
      removeDir(src: string, options: RemoveDirOptions, callback: NoParamCallback): void;
      allSettled(values: readonly PromiseLike<unknown>[], rejected?: LogValue, options?: LogFailOptions | LogType): Promise<PromiseFulfilledResult<unknown>[]>;
      formatMessage(type: LogType, title: string, value: LogValue, message?: unknown, options?: LogMessageOptions): void;
      formatFail(type: LogType, title: string, value: LogValue, message?: unknown, options?: LogFailOptions): void;
      writeFail(value: LogValue, message?: unknown, options?: LogFailOptions | LogType): void;
      writeTimeProcess(title: string, value: string, startTime: LogTime, options?: LogProcessOptions): void;
      writeTimeElapsed(title: string, value: LogValue, startTime: LogTime, options?: LogMessageOptions): void;
      checkPackage(err: unknown, name: string | undefined, options?: LogFailOptions | LogType): boolean;
      checkPackage(err: unknown, name: string | undefined, value?: LogValue, options?: LogFailOptions | LogType): boolean;
      checkFail(message: unknown, options: LogFailOptions): LogArguments | false | undefined;
      writeLog(component: LogComponent, queue?: boolean): void;
      writeLog(type: StatusType, value: unknown, options?: LogOptions): void;
      writeLog(type: StatusType, value: unknown, timeStamp?: LogDate, duration?: number): void;
      addLog(component: LogComponent, queue?: boolean): void;
      addLog(type: StatusType, value: unknown, from: string, source?: string): void;
      addLog(type: StatusType, value: unknown, options?: LogOptions): void;
      addLog(type: StatusType, value: unknown, timeStamp?: LogDate, from?: string, source?: string): void;
      addLog(type: StatusType, value: unknown, timeStamp?: LogDate, duration?: number, from?: string, source?: string): void;
      getLog(...type: StatusType[]): LogStatus<StatusType>[];
      flushLog(): void;
      willAbort(value: unknown): boolean;
      hasOwnPermission(): boolean;
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
      get logType(): LOG_TYPE;
      set logLevel(value: number | string);
      get logLevel(): number;
      get statusType(): STATUS_TYPE;
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
      on(event: "dir:create", listener: (src: string, options?: CreateDirOptions) => void): this;
      on(event: "dir:remove", listener: (src: string, options?: RemoveDirOptions) => void): this;
      once(event: "exec", listener: (command: ExecCommand, options?: SpawnOptions) => void): this;
      once(event: "error", listener: (err: Error) => void): this;
      once(event: "file:read", listener: (src: string, data: Buffer | string, options?: ReadFileOptions) => void): this;
      once(event: "file:write", listener: (src: string, options?: WriteFileOptions) => void): this;
      once(event: "file:delete", listener: (src: string, options?: DeleteFileOptions) => void): this;
      once(event: "file:copy", listener: (dest: string, options?: CopyFileOptions) => void): this;
      once(event: "file:move", listener: (dest: string, options?: MoveFileOptions) => void): this;
      once(event: "dir:create", listener: (src: string, options?: CreateDirOptions) => void): this;
      once(event: "dir:remove", listener: (src: string, options?: RemoveDirOptions) => void): this;
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

  interface ModuleConstructor {
      PROCESS_TIMEOUT: number;
      LOG_STYLE_FAIL: LogMessageOptions;
      LOG_STYLE_SUCCESS: LogMessageOptions;
      LOG_STYLE_INFO: LogMessageOptions;
      LOG_STYLE_WARN: LogMessageOptions;
      LOG_STYLE_NOTICE: LogMessageOptions;
      LOG_STYLE_REVERSE: LogMessageOptions;
      readonly VERSION: string;
      readonly LOG_TYPE: LOG_TYPE;
      readonly STATUS_TYPE: STATUS_TYPE;
      readonly MAX_TIMEOUT: number;
      readonly TEMP_DIR: string;
      supported(major: number, minor?: number, patch?: number, lts?: boolean): boolean;
      formatMessage(type: LogType, title: string, value: LogValue, message?: unknown, options?: LogMessageOptions): void;
      writeFail(value: LogValue, message?: unknown, options?: LogFailOptions | LogType): void;
      enabled(key: string, username?: string): boolean;
      parseFunction(value: unknown, options?: ParseFunctionOptions): ((...args: unknown[]) => Promise<unknown> | unknown) | null;
      parseFunction(value: unknown, absolute: boolean, sync?: boolean): ((...args: unknown[]) => Promise<unknown> | unknown) | null;
      asString(value: unknown, cacheKey?: boolean | "throws"): string;
      asHash(data: BinaryLike, options: AsHashOptions): string;
      asHash(data: BinaryLike, minLength: number): string;
      asHash(data: BinaryLike, algorithm?: number | string | AsHashOptions, minLength?: number | AsHashOptions): string;
      readHash(value: string | URL, options?: ReadHashOptions): Promise<string>;
      toPosix(value: unknown, normalize: boolean): string;
      toPosix(value: unknown, filename?: string, normalize?: boolean): string;
      hasLogType(value: LogType): boolean;
      isURL(value: string, ...exclude: string[]): boolean;
      isFile(value: string | URL, type?: ProtocolType): boolean;
      isDir(value: string | URL): boolean;
      isPath(value: string | URL, type?: "unc" | "unc-exists"): boolean;
      isPath(value: string | URL, isFile?: boolean): boolean;
      isErrorCode(err: unknown, ...code: string[]): boolean;
      fromLocalPath(value: string): string;
      resolveFile(value: string): string;
      resolvePath(value: string, base: string | URL): string;
      joinPath(...values: [...paths: unknown[], normalize: boolean][]): string;
      joinPath(...values: unknown[]): string;
      normalizePath(value: unknown, flags?: boolean | NormalizeFlags): string;
      createDir(value: string | URL, overwrite?: boolean): boolean;
      removeDir(value: string | URL, sinceCreated: number, recursive?: boolean): boolean;
      removeDir(value: string | URL, empty?: boolean, recursive?: boolean): boolean;
      copyDir(src: string | URL, dest: string | URL, options: CopyDirOptions): Promise<CopyDirResult>;
      copyDir(src: string | URL, dest: string | URL, move?: boolean, recursive?: boolean): Promise<CopyDirResult>;
      renameFile(src: string | URL, dest: string | URL, throws?: boolean): boolean;
      streamFile(src: string, cache: boolean): Promise<Buffer | string>;
      streamFile(src: string, options: ReadBufferOptions): Promise<Buffer | string>;
      streamFile(src: string, cache?: boolean | ReadBufferOptions, options?: ReadBufferOptions): Promise<Buffer | string>;
      readText(value: string | URL, cache: boolean): string;
      readText(value: string | URL, options: ReadTextOptions): Promise<string> | string;
      readText(value: string | URL, encoding?: BufferEncoding | boolean | ReadTextOptions, cache?: boolean): string;
      readBuffer(value: string | URL, options: ReadBufferOptions): Promise<Buffer | null> | Buffer | null;
      readBuffer(value: string | URL, cache?: boolean): Buffer | null;
      resolveMime(data: string | Buffer | Uint8Array | ArrayBuffer): Promise<FileTypeResult | undefined>;
      lookupMime(value: string, extension?: boolean): string;
      initCpuUsage(instance?: IModule): CpuUsage;
      getCpuUsage(start: CpuUsage, format: true): string;
      getCpuUsage(start: CpuUsage, format?: boolean): number;
      getMemUsage(format: true): string;
      getMemUsage(format?: boolean): number;
      formatCpuMem(start: CpuUsage, all?: boolean): string;
      getPackageVersion(name: string | [string, string], startDir: string): string;
      getPackageVersion(name: string | [string, string], unstable?: boolean, startDir?: string): string;
      checkSemVer(name: string | [string, string], options: CheckSemVerOptions): boolean;
      checkSemVer(name: string | [string, string], min: number | string, max: number | string, options: CheckSemVerOptions): boolean;
      checkSemVer(name: string | [string, string], min: number | string, max?: number | string, unstable?: boolean, startDir?: string): boolean;
      sanitizeCmd(value: string): string;
      sanitizeArgs(value: string, doubleQuote?: boolean): string;
      sanitizeArgs(values: string[], doubleQuote?: boolean): string[];
      purgeMemory(percent: number, parent: boolean | number): Promise<number>;
      purgeMemory(percent?: number, limit?: number, parent?: boolean | number): Promise<number>;
      canWrite(name: "temp" | "home"): boolean;
      loadSettings(settings: Settings, password?: string): boolean;
      readonly prototype: IModule<IHost>;
      new(): IModule<IHost>;
  }

References
==========

* https://www.unpkg.com/@e-mc/types/lib/index.d.ts

- https://www.unpkg.com/@e-mc/types/lib/core.d.ts
- https://www.unpkg.com/@e-mc/types/lib/logger.d.ts
- https://www.unpkg.com/@e-mc/types/lib/module.d.ts
- https://www.unpkg.com/@e-mc/types/lib/node.d.ts