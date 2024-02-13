========
@e-mc/db
========

- **npm** i *@e-mc/db*

Interface
=========

.. code-block:: typescript

  import type { DbDataSource } from "./squared";

  import type { IHost } from "./index";
  import type { ClientDbConstructor, IClientDb } from "./core";
  import type { BatchQueryResult, DB_TYPE, ExecuteBatchQueryOptions, ExecuteQueryOptions, HandleFailOptions, ProcessRowsOptions, QueryResult, SQL_COMMAND } from "./db";
  import type { AuthValue } from "./http";
  import type { DbCoerceSettings, DbModule, DbSourceOptions, PoolConfig } from "./settings";

  import type { SecureContextOptions } from "tls";

  interface IDb extends IClientDb<IHost, DbModule, DbDataSource, DbSourceOptions, DbCoerceSettings> {
      setCredential(item: DbDataSource): Promise<void>;
      getCredential(item: DbDataSource): Record<string | number | symbol, unknown>;
      hasSource(source: string, ...type: number[]): boolean;
      applyCommand(...items: DbDataSource[]): void;
      executeQuery(item: DbDataSource, sessionKey: string): Promise<QueryResult>;
      executeQuery(item: DbDataSource, options?: ExecuteQueryOptions | string): Promise<QueryResult>;
      executeBatchQuery(batch: DbDataSource[], sessionKey: string, outResult?: BatchQueryResult): Promise<BatchQueryResult>;
      executeBatchQuery(batch: DbDataSource[], options?: ExecuteBatchQueryOptions | string, outResult?: BatchQueryResult): Promise<BatchQueryResult>;
      processRows(batch: DbDataSource[], tasks: Promise<QueryResult | null>[], parallel: boolean): Promise<BatchQueryResult>;
      processRows(batch: DbDataSource[], tasks: Promise<QueryResult | null>[], options?: ProcessRowsOptions, outResult?: BatchQueryResult): Promise<BatchQueryResult>;
      handleFail(err: unknown, item: DbDataSource, options?: HandleFailOptions): boolean;
      readTLSCert(value: unknown, cache?: boolean): string;
      readTLSConfig(options: SecureContextOptions, cache?: boolean): void;
      settingsOf(source: string, name: keyof Omit<DbSourceOptions, "coerce">): unknown;
      settingsOf(source: string, name: "coerce", component: keyof X): unknown;
      settingsKey(source: string, name: keyof Omit<DbSourceOptions, "coerce">): unknown;
      settingsKey(source: string, name: "coerce", component: keyof X): unknown;
      getPoolConfig(source: string, uuidKey?: string): Required<PoolConfig> | undefined;
      get sourceType(): DB_TYPE;
      get commandType(): SQL_COMMAND;
  }

  interface DbConstructor extends ClientDbConstructor<IHost> {
      setPoolConfig(value: Record<string, PoolConfig>): void;
      getPoolConfig(source: string): Required<PoolConfig> | undefined;
      readonly prototype: IDb<IHost, DbModule, DbDataSource>;
      new(module?: DbModule, database?: DbDataSource[], ...args: unknown[]): IDb<IHost, DbModule, DbDataSource>;
  }

  interface IDbSourceClient {
      DB_SOURCE_NAME: string;
      DB_SOURCE_CLIENT: boolean;
      DB_SOURCE_TYPE: number;
      setCredential(this: IDb, item: DbDataSource): Promise<void>;
      executeQuery(this: IDb, item: DbDataSource, options?: ExecuteQueryOptions | string): Promise<QueryResult>;
      executeBatchQuery(this: IDb, batch: DbDataSource[], options?: ExecuteBatchQueryOptions | string, outResult?: BatchQueryResult): Promise<BatchQueryResult>;
      checkTimeout?(this: IDbSourceClient, value: number, limit?: number): Promise<number>;
  }

  interface IDbPool {
      client: unknown;
      lastAccessed: number;
      success: number;
      failed: number;
      poolKey: string;
      uuidKey: AuthValue | null;
      add(item: DbDataSource, uuidKey?: string): this;
      has(item: DbDataSource): boolean;
      getConnection(): Promise<unknown>;
      remove(): void;
      detach(force?: boolean): Promise<void>;
      close(): Promise<void>;
      isIdle(timeout: number): boolean;
      isEmpty(): boolean;
      set connected(value: boolean);
      get persist(): boolean;
      get closed(): boolean;
      get closeable(): boolean;
      set parent(value: Record<string, IDbPool<DbDataSource>>);
  }

  interface DbPoolConstructor {
      findKey(pools: Record<string, IDbPool>, uuidKey: unknown, poolKey: string | undefined, ...items: DbDataSource[]): Record<string, IDbPool> | null;
      validateKey(pools: Record<string, IDbPool>, username: string, uuidKey: unknown): [string, Record<string, IDbPool> | null];
      checkTimeout(pools: Record<string, IDbPool>, value: number, limit?: number): Promise<number>;
      readonly prototype: IDbPool<DbDataSource, unknown, unknown>;
      new(pool: unknown, poolKey: string, uuidKey?: AuthValue | null): IDbPool<DbDataSource, unknown, unknown>;
  }

References
==========

* https://www.unpkg.com/@e-mc/types/lib/index.d.ts

- https://www.unpkg.com/@e-mc/types/lib/squared.d.ts
- https://www.unpkg.com/@e-mc/types/lib/core.d.ts
- https://www.unpkg.com/@e-mc/types/lib/db.d.ts
- https://www.unpkg.com/@e-mc/types/lib/http.d.ts
- https://www.unpkg.com/@e-mc/types/lib/settings.d.ts