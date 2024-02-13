==========
@e-mc/core
==========

- **npm** i *@e-mc/core*

Interface
=========

.. code-block:: typescript

  import type { DataSource, LogStatus } from "./squared";

  import type { IHost, IModule, ModuleConstructor } from "./index";
  import type { CacheOptions, HostInitConfig, JoinQueueOptions, PermissionReadWrite, ResumeThreadOptions, StoreResultOptions, ThreadCountStat } from "./core";
  import type { QueryResult, TimeoutAction } from "./db";
  import type { AddEventListenerOptions } from "./dom";
  import type { LogState, StatusType } from "./logger";
  import type { Settings } from "./node";
  import type { ClientDbSettings, ClientModule, ClientSettings, DbCacheValue, DbCoerceSettings, DbCoerceValue, DbSourceOptions } from "./settings";

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
      pauseLog(): void;
      resumeLog(): void;
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
      kill(username: string, iv: BinaryLike, pid: number | number[] | boolean): number;
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
      readonly prototype: IClient<IHost, ClientModule>;
      new(module?: ClientModule): IClient<IHost, ClientModule>;
  }

  interface IClientDb extends IClient<IHost, ClientModule<ClientDbSettings>> {
      database: DataSource[];
      cacheExpires: number;
      add(item: DataSource, state?: number): void;
      hasCache(source: string, sessionKey?: string, override?: DbCacheValue): boolean;
      hasCoerce(source: string, component: keyof DbCoerceSettings, uuidKey: string | undefined): boolean;
      hasCoerce(source: string, component: keyof DbCoerceSettings, override: DbCoerceValue | null | undefined, credential?: unknown): boolean;
      hasCoerce(source: string, component: keyof DbCoerceSettings, credential?: unknown): boolean;
      getQueryResult(source: string, credential: unknown, queryString: string, renewCache: boolean): QueryResult | undefined;
      getQueryResult(source: string, credential: unknown, queryString: string, sessionKey: string, renewCache?: boolean): QueryResult | undefined;
      getQueryResult(source: string, credential: unknown, queryString: string, options?: CacheOptions | string, renewCache?: boolean): QueryResult | undefined;
      setQueryResult(source: string, credential: unknown, queryString: string, result: unknown, sessionKey: string | undefined): QueryResult;
      setQueryResult(source: string, credential: unknown, queryString: string, result: unknown, options?: CacheOptions | string): QueryResult;
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
      storeResult(source: string, credential: unknown, queryString: string, result: QueryResult, sessionKey: string, sessionExpires: number): QueryResult;
      storeResult(source: string, credential: unknown, queryString: string, result: QueryResult, cache: DbCacheValue): QueryResult;
      storeResult(source: string, credential: unknown, queryString: string, result: QueryResult, cache: DbCacheValue | undefined, options: StoreResultOptions): QueryResult;
      purgeResult(prefix?: string): Promise<number>;
      extractUUID(credential: unknown): string;
      setPoolConfig(value: unknown): void;
      getPoolConfig(source: string): unknown;
      keyOfResult(source: string, credential: unknown, uuidOnly?: boolean): string;
      readonly prototype: IClientDb<IHost, ClientModule, DataSource>;
      new(module?: ClientModule, database?: DataSource[]): IClientDb<IHost, ClientModule, DataSource>;
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

References
==========

* https://www.unpkg.com/@e-mc/types/lib/index.d.ts

- https://www.unpkg.com/@e-mc/types/lib/squared.d.ts
- https://www.unpkg.com/@e-mc/types/lib/core.d.ts
- https://www.unpkg.com/@e-mc/types/lib/db.d.ts
- https://www.unpkg.com/@e-mc/types/lib/dom.d.ts
- https://www.unpkg.com/@e-mc/types/lib/logger.d.ts
- https://www.unpkg.com/@e-mc/types/lib/node.d.ts
- https://www.unpkg.com/@e-mc/types/lib/settings.d.ts