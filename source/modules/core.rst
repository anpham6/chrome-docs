==========
@e-mc/core
==========

Interface
=========

.. highlight:: typescript

.. code-block::
  :caption: `View Source <https://www.unpkg.com/@e-mc/types/lib/index.d.ts>`_
  :emphasize-lines: 131-172

  import type { DataSource, LogStatus } from "./squared";

  import type { IHost, IModule, ModuleConstructor } from "./index";
  import type { AddEventListenerOptions, CacheOptions, HostInitConfig, JoinQueueOptions, PermissionReadWrite, ResumeThreadOptions, StoreResultOptions, ThreadCountStat, WorkerChannelResponse } from "./core";
  import type { QueryResult, TimeoutAction } from "./db";
  import type { LogState, StatusType } from "./logger";
  import type { Settings } from "./node";
  import type { ClientDbSettings, ClientModule, ClientSettings, DbCacheValue, DbCoerceSettings, DbCoerceValue, DbSourceOptions } from "./settings";

  import type { TransferListItem, Worker } from "node:worker_threads";

  import type * as EventEmitter from "node:events";

  interface IHost extends IModule {
      restartable: boolean;
      readonly modules: Set<IModule>;
      readonly subProcesses: Set<IModule>;
      readonly startTime: number;
      using(...items: unknown[] | [boolean, ...unknown[]]): this;
      contains(item: unknown, condition?: (...args: any[]) => boolean): boolean;
      find(name: string): IModule | undefined;
      findAll(name: string): IModule[];
      willLog(name: string): boolean;
      ignoreLog(values: boolean | string | string[]): void;
      collectLog(level?: boolean): LogStatus<StatusType>[];
      pauseLog(type?: string): void;
      resumeLog(type?: string): void;
      hasLog(type: string): boolean;
      delayMessage(...args: unknown[]): void;
      willAbort(value: string | IModule): boolean;
      loadModule(name: string, ...args: any[]): IModule | null;
      retain(process: IModule): void;
      release(process: IModule, log?: boolean): boolean;
      restart(...args: unknown[]): void;
      joinQueue(options?: JoinQueueOptions): boolean;
      updateProgress(name: string, ...args: unknown[]): void;
      resumeThread?(options: ResumeThreadOptions): void;
      set host(value);
      get host(): null;
      get config(): Readonly<HostInitConfig>;
      get username(): string;
      get ipV4(): string;
      get ipV6(): string;
      set done(value);
      get done(): boolean;
      get queued(): boolean;
      get logState(): LogState;
      get errorCount(): number;
  }

  interface HostConstructor extends ModuleConstructor {
      loadSettings(settings: Settings, password?: string): boolean;
      loadSettings(settings: Settings, permission?: PermissionReadWrite, password?: string): boolean;
      isPermission(value: unknown): value is IPermission;
      createPermission(all?: boolean, freeze?: boolean): IPermission;
      kill(username: string, iv: BinaryLike, all: true): number;
      kill(username: string, iv: BinaryLike, pid: number | number[]): number;
      getThreadCount(full: true): ThreadCountStat;
      getThreadCount(username: string, iv?: BinaryLike): ThreadCountStat;
      getThreadCount(username?: string | boolean, iv?: BinaryLike): number;
      getPermissionFromSettings(): IPermission;
      readonly prototype: IHost;
      new(config?: HostInitConfig): IHost;
  }

  interface IClient extends IModule<IHost> {
      module: ClientModule;
      init(...args: unknown[]): this;
      getUserSettings(): unknown;
      get settings(): ClientSettings;
      set cacheDir(value: string);
      get cacheDir(): string;
      set extensions(values: unknown[]);
      get extensions(): ((...args: unknown[]) => unknown)[];
  }

  interface ClientConstructor extends ModuleConstructor {
      readonly prototype: IClient;
      new(module?: ClientModule): IClient;
  }

  interface IClientDb extends IClient<IHost, ClientModule<ClientDbSettings>> {
      database: DataSource[];
      cacheExpires: number;
      add(item: DataSource, state?: number): void;
      hasCache(source: string, sessionKey?: string): boolean;
      hasCoerce(source: string, component: keyof DbCoerceSettings, uuidKey: string | undefined): boolean;
      hasCoerce(source: string, component: keyof DbCoerceSettings, credential?: unknown): boolean;
      getQueryResult(source: string, credential: unknown, queryString: string, renewCache: boolean): QueryResult | undefined;
      getQueryResult(source: string, credential: unknown, queryString: string, sessionKey: string | undefined, renewCache?: boolean): QueryResult | undefined;
      getQueryResult(source: string, credential: unknown, queryString: string, options?: CacheOptions, renewCache?: boolean): QueryResult | undefined;
      setQueryResult(source: string, credential: unknown, queryString: string, result: unknown, sessionKey: string | undefined): QueryResult;
      setQueryResult(source: string, credential: unknown, queryString: string, result: unknown, options?: CacheOptions): QueryResult;
      getCacheResult(source: string, credential: unknown, queryString: string, cacheValue: CacheOptions, ignoreCache?: unknown): QueryResult | undefined;
      applyState(items: DataSource | DataSource[], value: number, as?: boolean): void;
      commit(items?: DataSource[]): Promise<boolean>;
      valueOfKey(credential: unknown, name: keyof DbSourceOptions, component?: keyof DbCoerceSettings): unknown;
      settingsOf(source: string, name: keyof DbSourceOptions, component?: keyof DbCoerceSettings): unknown;
      settingsKey(uuidKey: string, name: keyof DbSourceOptions, component?: keyof DbCoerceSettings): unknown;
      get pending(): DataSource[];
      get committed(): DataSource[];
      get failed(): DataSource[];
  }

  interface ClientDbConstructor extends ClientConstructor<IHost, ClientModule> {
      STORE_RESULT_PARTITION_SIZE: number;
      STORE_RESULT_PARTITION_MULT: number;
      readonly TRANSACTION_ACTIVE: number;
      readonly TRANSACTION_PARTIAL: number;
      readonly TRANSACTION_COMMIT: number;
      readonly TRANSACTION_TERMINATE: number;
      readonly TRANSACTION_ABORT: number;
      readonly TRANSACTION_FAIL: number;
      loadSettings(settings: Pick<Settings, "process" | "memory">, password?: string) : boolean;
      getTimeout(value: number | string | TimeoutAction | undefined): number;
      convertTime(value: number | string): number;
      findResult(source: string, credential: unknown, queryString: string, timeout: number, sessionKey?: string | boolean, renewCache?: boolean): QueryResult | undefined;
      storeResult(source: string, credential: unknown, queryString: string, result: QueryResult, options: StoreResultOptions): QueryResult;
      storeResult(source: string, credential: unknown, queryString: string, result: QueryResult, cache: DbCacheValue): QueryResult;
      storeResult(source: string, credential: unknown, queryString: string, result: QueryResult, cache: DbCacheValue | undefined, options?: StoreResultOptions): QueryResult;
      storeResult(source: string, credential: unknown, queryString: string, result: QueryResult, sessionKey?: string, sessionExpires?: number): QueryResult;
      purgeResult(prefix?: string): Promise<number>;
      extractUUID(credential: unknown): string;
      setPoolConfig(value: unknown): void;
      getPoolConfig(source: string): unknown;
      keyOfResult(source: string, credential: unknown, uuidOnly?: boolean): string;
      readonly prototype: IClientDb;
      new(module?: ClientModule, database?: DataSource[]): IClientDb;
  }

  interface IWorkerChannel {
      [Symbol.iterator](): IteratorObject<Worker, BuiltinIteratorReturn>;
      sendObject(data: unknown, transferList?: TransferListItem[], callback?: WorkerChannelResponse<unknown>, ...returnArgs: unknown[]): Worker;
      sendBuffer(data: Buffer, shared?: boolean, callback?: WorkerChannelResponse<unknown>, ...returnArgs: unknown[]): Worker | null;
      send(data: unknown, transferList?: TransferListItem[]): Promise<unknown>;
      drop(count?: number): Promise<number>;
      kill(count?: number): Promise<number>;
      isEmpty(): boolean;
      set min(value);
      get min(): number;
      set max(value);
      get max(): number;
      get filename(): string;
      get workers(): Worker[];
      get pending(): number;
      get available(): number;
      get detached(): boolean;
      get timeoutMs(): number;
      get lastAccessed(): Date;
      get timesAccessed(): number;
      get frequencyAccessed(): number;
      get size(): number;

      /* EventEmitter */
      on(event: "error" | "messageerror" | "abort", listener: (err: Error) => void): this;
      on(event: "exit", listener: (exitCode: number) => void): this;
      on(event: "online", listener: () => void): this;
      on(event: "message", listener: (value: any) => void): this;
      on(event: "data", listener: (data: unknown) => void): this;
      on(event: "pass", listener: (data: unknown, transferList: TransferListItem[] | undefined) => void): this;
      once(event: "error" | "messageerror" | "abort", listener: (err: Error) => void): this;
      once(event: "exit", listener: (exitCode: number) => void): this;
      once(event: "online", listener: () => void): this;
      once(event: "message", listener: (value: any) => void): this;
      once(event: "data", listener: (data: unknown) => void): this;
      once(event: "pass", listener: (data: unknown, transferList: TransferListItem[] | undefined) => void): this;
  }

  interface WorkerChannelConstructor {
      readonly prototype: IWorkerChannel;
      new(filename: string, max?: number, timeoutMs?: number): IWorkerChannel;
  }

  interface IAbortComponent extends AbortController {
      reset(): void;
      get aborted(): boolean;
  }

  interface AbortComponentConstructor {
      attach(instance: IAbortComponent, signal: AbortSignal, options?: AddEventListenerOptions): void;
      detach(instance: IAbortComponent, signal: AbortSignal): void;
      readonly prototype: IAbortComponent;
      new(): IAbortComponent;
  }

  interface IPermission {
      setDiskRead(pathname?: string | string[], enabled?: boolean): void;
      setDiskWrite(pathname?: string | string[], enabled?: boolean): void;
      setUNCRead(pathname?: string | string[], enabled?: boolean): void;
      setUNCWrite(pathname?: string | string[], enabled?: boolean): void;
      getDiskRead(): string | string[];
      getDiskWrite(): string | string[];
      getUNCRead(): string | string[];
      getUNCWrite(): string | string[];
      hasDiskRead(pathname: string): boolean;
      hasDiskWrite(pathname: string): boolean;
      hasUNCRead(pathname: string): boolean;
      hasUNCWrite(pathname: string): boolean;
      get diskRead(): boolean;
      get diskWrite(): boolean;
      get uncRead(): boolean;
      get uncWrite(): boolean;
  }

Changelog
=========

.. versionadded:: 0.12.0

  - *IWorkerChannel* and *WorkerChannelConstructor* were created.

.. versionadded:: 0.11.0

  - *IHost* property getters **ipV4** | **ipV6** for remote client address were created.

.. versionadded:: 0.10.0

  - *IClientDb* method **getCacheResult** was created.

.. versionchanged:: 0.10.0

  - *IHost* methods **pauseLog** | **resumeLog** argument :target:`type` as :alt:`string` was implemented.

.. versionadded:: 0.9.0

  - *IHost* methods were created:

    .. hlist::
      :columns: 3

      - pauseLog
      - resumeLog
      - hasLog
      - delayMessage
      - updateProgress

  - *IHost* property **logState** was created.

.. versionremoved:: 0.9.0

  - *IClientDb* method **hasCache** argument :target:`override` as :alt:`DbCacheValue`.
  - *IClientDb* method **hasCoerce** argument :target:`override` as :alt:`DbCoerceValue`.

Settings
========

.. code-block::
  :caption: `View JSON <https://www.unpkg.com/squared-express/dist/squared.json>`_
  :emphasize-lines: 21-23

  import type { ExecOptions } from "./settings";

  import type { MinimatchOptions } from "minimatch";
  import type { PicomatchOptions } from "picomatch";

  interface ProcessModule {
      thread?: {
          admin: {
              users?: string[];
              private?: boolean;
          };
          queue?: {
              limit?: number;
              expires?: number | string;
              priority: {
                  bypass?: number;
                  min?: number;
                  max?: number;
              };
          };
          workers?: {
              channel?: { min?: number; max?: number; expires?: number | string };
          };
          limit?: number;
          expires?: number | string;
      };
  }

  interface PermissionModule {
      disk_read?: string | string[];
      disk_write?: string | string[];
      unc_read?: string | string[];
      unc_write?: string | string[];
      settings?: {
          broadcast_id?: string | string[];
          picomatch?: PicomatchOptions | null;
          minimatch?: MinimatchOptions | null;
      };
  }

Example usage
-------------

.. code-block:: javascript
  :caption: Abstract class

  const { Host } = require("@e-mc/core");

  Host.loadSettings({ // Global
    process: {
      thread: { limit: 8 }
    },
    permission: {
      disk_read: ["**/*"],
      disk_write: ["/tmp/**"]
    }
  });

.. attention:: **@e-mc/core** is mostly a collection of abstract base classes which cannot be instantiated. :target:`Host` is more commonly called through :doc:`@e-mc/file-manager <file-manager>`.

References
==========

- https://www.unpkg.com/@e-mc/types/lib/squared.d.ts
- https://www.unpkg.com/@e-mc/types/lib/core.d.ts
- https://www.unpkg.com/@e-mc/types/lib/db.d.ts
- https://www.unpkg.com/@e-mc/types/lib/dom.d.ts
- https://www.unpkg.com/@e-mc/types/lib/logger.d.ts
- https://www.unpkg.com/@e-mc/types/lib/node.d.ts
- https://www.unpkg.com/@e-mc/types/lib/settings.d.ts

* https://www.npmjs.com/package/@types/node
* https://www.npmjs.com/package/minimatch
* https://www.npmjs.com/package/picomatch