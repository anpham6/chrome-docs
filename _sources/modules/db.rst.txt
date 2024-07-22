========
@e-mc/db
========

- **npm** i *@e-mc/db*

Interface
=========

.. highlight:: typescript

.. code-block::
  :caption: `View Source <https://www.unpkg.com/@e-mc/types/lib/index.d.ts>`_
  :emphasize-lines: 76-79

  import type { DbDataSource } from "./squared";

  import type { IHost } from "./index";
  import type { ClientDbConstructor, IClientDb } from "./core";
  import type { DB_TYPE, SQL_COMMAND, BatchQueryResult, ErrorQueryCallback, ExecuteBatchQueryOptions, ExecuteQueryOptions, HandleFailOptions, ProcessRowsOptions, QueryResult } from "./db";
  import type { AuthValue } from "./http";
  import type { DbCoerceSettings, DbModule, DbSourceOptions, PoolConfig } from "./settings";

  import type { SecureContextOptions } from "tls";

  interface IDb extends IClientDb<IHost, DbModule, DbDataSource, DbSourceOptions, DbCoerceSettings> {
      setCredential(item: DbDataSource): Promise<void>;
      getCredential(item: DbDataSource): PlainObject;
      hasSource(source: string, ...type: number[]): boolean;
      applyCommand(...items: DbDataSource[]): void;
      executeQuery(item: DbDataSource, callback: ErrorQueryCallback): Promise<QueryResult>;
      executeQuery(item: DbDataSource, sessionKey: string): Promise<QueryResult>;
      executeQuery(item: DbDataSource, options?: ExecuteQueryOptions | string): Promise<QueryResult>;
      executeBatchQuery(batch: DbDataSource[], callback: ErrorQueryCallback, outResult?: BatchQueryResult): Promise<BatchQueryResult>;
      executeBatchQuery(batch: DbDataSource[], sessionKey: string, outResult?: BatchQueryResult): Promise<BatchQueryResult>;
      executeBatchQuery(batch: DbDataSource[], options?: ExecuteBatchQueryOptions | string, outResult?: BatchQueryResult): Promise<BatchQueryResult>;
      processRows(batch: DbDataSource[], tasks: Promise<QueryResult | null>[], parallel: boolean): Promise<BatchQueryResult>;
      processRows(batch: DbDataSource[], tasks: Promise<QueryResult | null>[], options?: ProcessRowsOptions, outResult?: BatchQueryResult): Promise<BatchQueryResult>;
      handleFail(err: unknown, item: DbDataSource, options?: HandleFailOptions): boolean;
      readTLSCert(value: unknown, cache?: boolean): string;
      readTLSConfig(options: SecureContextOptions, cache?: boolean): void;
      settingsOf(source: string, name: keyof Omit<DbSourceOptions, "coerce">): unknown;
      settingsOf(source: string, name: "coerce", component: keyof DbCoerceSettings): unknown;
      settingsKey(source: string, name: keyof Omit<DbSourceOptions, "coerce">): unknown;
      settingsKey(source: string, name: "coerce", component: keyof DbCoerceSettings): unknown;
      getPoolConfig(source: string, uuidKey?: string): Required<PoolConfig> | undefined;
      get sourceType(): DB_TYPE;
      get commandType(): SQL_COMMAND;
  }

  interface DbConstructor extends ClientDbConstructor<IHost> {
      setPoolConfig(value: Record<string, PoolConfig>): void;
      getPoolConfig(source: string): Required<PoolConfig> | undefined;
      readonly prototype: IDb;
      new(module?: DbModule, database?: DbDataSource[], ...args: unknown[]): IDb;
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
      set parent(value: Record<string, IDbPool>);
  }

  interface DbPoolConstructor {
      CACHE_UNUSED: readonly string[];
      asString(credential: unknown): string;
      sanitize(credential: unknown): unknown;
      removeUUIDKey(credential: unknown): unknown;
      findKey(pools: Record<string, IDbPool>, uuidKey: unknown, poolKey: string | undefined, ...items: DbDataSource[]): Record<string, IDbPool> | null;
      validateKey(pools: Record<string, IDbPool>, username: string, uuidKey: unknown): [string, Record<string, IDbPool> | null];
      checkTimeout(pools: Record<string, IDbPool>, value: number, limit?: number): Promise<number>;
      readonly prototype: IDbPool;
      new(pool: unknown, poolKey: string, uuidKey?: AuthValue | null): IDbPool;
  }

Changelog
=========

.. versionadded:: 0.10.0

  - *DbPoolConstructor* static property **CACHE_UNUSED** for unused pool attributes was created.
  - *DbPoolConstructor* static methods **asString** | **sanitize** | **removeUUIDKey** for pool keys were created.

.. versionadded:: 0.9.0

  - *IDb* methods **executeQuery** | **executeBatchQuery** with argument :target:`callback` as :alt:`ErrorQueryCallback`.

Settings
========

.. code-block::
  :caption: `View JSON <https://www.unpkg.com/squared-express/dist/squared.db.json>`_

  import type { DbSourceOptions, PurgeComponent } from "./settings";

  interface DbModule {
      // handler: "@e-mc/db";
      mariadb?: DbStoredCredentials;
      mongodb?: DbStoredCredentials;
      mssql?: DbStoredCredentials;
      mysql?: DbStoredCredentials;
      oracle?: DbStoredCredentials;
      postgres?: DbStoredCredentials;
      redis?: DbStoredCredentials;
      settings?: {
          broadcast_id?: string | string[];
          users?: Record<string, Record<string, unknown>>;
          cache_dir?: string;
          session_expires?: number;
          user_key?: Record<string, DbSourceOptions>;
          imports?: StringMap;
          purge?: PurgeComponent;
          mariadb?: DbSourceOptions;
          mongodb?: DbSourceOptions;
          mssql?: DbSourceOptions;
          mysql?: DbSourceOptions;
          oracle?: DbSourceOptions;
          postgres?: DbSourceOptions;
          redis?: DbSourceOptions;
      };
  }

  type DbStoredCredentials = Record<string, Record<string, unknown>>;

Example usage
-------------

.. code-block:: javascript
  :caption: Using @pi-r/mongodb

  const Db = require("@e-mc/db");

  const instance = new Db({
    mongodb: {
      main: {
        server: "localhost:27017",
        auth: {
          username: "**********",
          password: "**********"
        },
        authMechanism: "SCRAM-SHA-1"
      }
    },
    settings: {
      mongodb: {
        pool: {
          max: 10,
          idle: 60 * 1000,
          queue_max: 4,
          queue_idle: 30 * 1000,
          timeout: 10 * 1000
        },
        cache: {
          timeout: "1d",
          when_empty: false
        },
        coerce: {
          credential: false,
          options: true
        }
      }
    }
  });
  // instance.host = new Host();
  instance.init();

  const item = {
    source: "mongodb",
    credential: "main",
    table: "demo",
    name: "nodejs",
    query: {
      id: {
        "$eq": "1"
      }
    },
    willAbort: true
  };
  await instance.setCredential(item);

  const rows = await instance.executeQuery(item, (err, item) => {
    if (err.code === "E11000") {
      return true; // throw err;
    }
    return false; // return [];
  });

  const [rows1, rows2] = await instance.executeBatchQuery([
      { ...item, usePool: true },
      { ...item, query: { id: { "$eq": "2" } } }
    ],
    { parallel: true, connectOnce: true }
  );

References
==========

- https://www.unpkg.com/@e-mc/types/lib/squared.d.ts
- https://www.unpkg.com/@e-mc/types/lib/core.d.ts
- https://www.unpkg.com/@e-mc/types/lib/db.d.ts
- https://www.unpkg.com/@e-mc/types/lib/http.d.ts
- https://www.unpkg.com/@e-mc/types/lib/settings.d.ts

* https://www.npmjs.com/package/@types/node