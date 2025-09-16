=====
Redis
=====

- `Redis Stack <https://redis.io/downloads/#redis-stack-downloads>`_
- **npm** i *@pi-r/redis*

Interface
=========

.. code-block:: typescript

  import type { RediSearchSchema, RedisClientOptions, SearchOptions } from "redis";

  import type { CommandOptions } from "@redis/client/dist/lib/client/commands-queue";
  import type { ScanOptions } from "@redis/client/dist/lib/commands/SCAN";
  import type { XReadOptions, XReadStreams } from '@redis/client/dist/lib/commands/XREAD';
  import type { JsonGetOptions } from "@redis/json/dist/lib/commands/GET";
  import type { CreateOptions } from "@redis/search/dist/lib/commands/CREATE";
  import type { FtAggregateOptions } from "@redis/search/dist/lib/commands/AGGREGATE";
  import type { FtSearchOptions } from "@redis/search/dist/lib/commands/SEARCH";

  interface RedisDataSource extends DbDataSource {
      source: "redis";

      uri: string; // redis://<username>:<password>@hostname:6379
      username?: string; // redis://hostname:6379
      password?: string;
      credential?: string | ServerAuth;
      database?: number;

      format?: "HASH" | "JSON" | "HKEYS" | "HVALS" | "HSCAN" | "SMEMBERS"; // Default is "HASH"
      key?: RedisArgument | RedisArgument[];
      field?: RedisArgument;
      path?: string; // JSONPath

      /* Scan */
      cursor?: RedisArgument | RedisArgument[] | number | number[];
      iterations?: number | number[];

      search?: {
          index: string; // Preexisting schema
          query: string;
          schema?: RediSearchSchema; // Temporary schema
          schema?: string; // settings.directory.schema + users/username/?
          options?: CreateOptions;
      };
      aggregate?: {/* Same */};

      streams?: XReadStreams;

      options?: {
          client?: RedisClientOptions;
          command?: CommandOptions; // client.commandOptions
          get?: JsonGetOptions;
          search?: FtSearchOptions;
          aggregate?: FtAggregateOptions;
          xread?: XReadOptions;
          scan?: ScanOptions;
      };

      update?: RedisSetValue | RedisSetValue[] | RedisJSONValue | RedisJSONValue[]; // @pi-r/redis/types
      update?: {
          format: "JSON";
          key: string;
          value: unknown | unknown[]; // https://docs.redis.com/latest/stack/json/commands

          command?: "DEL" | "FORGET" | "MERGE" | "MSET" | "NUMINCRBY" | "NUMMULTBY" | "SET" | "STRAPPEND"; // Default is "SET"

          command?: "ARRAPPEND" | "ARRINDEX" | "ARRINSERT" | "ARRPOP" | "ARRTRIM";
          start?: number;
          stop?: number;
          index?: number;
      };
  }

  type RedisArgument = string | Buffer;
  type RedisCredential = ServerAuth;

Pool
----

.. code-block:: typescript

  import type { RedisPoolOptions } from "redis";

  interface PoolConfig { // using RedisPoolOptions
      min?: number; // minimum
      max?: number; // maximum
      timeout?: number; // acquireTimeout
  }

Authentication
==============

.. code-block::
  :caption: squared.db.json

  {
    "redis": {
      "main": {
        "protocol": "", // Default is "redis:"
        "hostname": "", // Default is "localhost"
        "port": "", // Default is "6379"
        "username": "",
        "password": "",
        "database": 0 // SELECT index (number > 0)
      }
    },
    "settings": {
      "imports": {
        "redis": "@pi-r2/redis" // Optional
      }
    }
  }

::

  {
    "dataSource": {
      "uri": "redis://localhost:6379",
      "username": "**********",
      "password": "**********",
      /* OR */
      "uri": "redis://<username>:<password>@localhost:6379/<database>",
      /* OR */
      "credential": "main",
      /* OR */
      "credential": {
        "protocol": "redis:",
        "server": "localhost:6379",
        "username": "**********",
        "password": "**********",
        "database": 1
      }
    }
  }

Example usage
=============

- `Query <https://github.com/redis/node-redis/tree/master/packages/search>`_
- `JSONPath <https://redis.io/docs/data-types/json/path>`_

::

  {
    "selector": "img",
    "type": "attribute",
    "dataSource": {
      "source": "redis",
      "credential": {/* Authentication */},

      "key": "demo:1",
      "format": "JSON",
      /* OR */
      "search": {
        "schema": {
          "name": {
            "type": "TEXT", // SchemaFieldTypes.TEXT
            "sortable": true
          },
          "state": "TAG", // SchemaFieldTypes.TAG
          "age": "NUMERIC" // SchemaFieldTypes.NUMERIC
        },
        /* OR */
        "schema": "./path/to/data.json", // yaml + json5 + toml + xml + cjs

        "query": "@state:{CA}",
        "options": {
          "ON": "HASH", // JSON
          "PREFIX": "noderedis:demo"
        }
      },

      /* Result: { "item_src": "redis.png", "item_alt": "Redis" } */
      "value": {
        "src": "item_src",
        "alt": "item_alt"
      },

      "usePool": true
    }
  }

.. note:: Search will only return the **value** object with the **id** field appended as ``__id__``.

@pi-r/redis
===========

.. versionadded:: 0.11.0

  - *NPM* package ``redis`` was upgraded to **5.8.0**.
  - *RedisDataSource* property **streams** as :alt:`XReadStreams` was implemented.
  - *RedisDataSource* property **format** with type "**SMEMBERS**" using :target:`key` as :alt:`string` was implemented.

.. versionadded:: 0.10.1

  - *DbPool* static property **CACHE_IGNORE** through :target:`@pi-r/redis/client/pool` as :alt:`keyof RedisClientOptions` was implemented.

.. versionadded:: 0.8.0

  - *RedisDataSource* property **format** with type "**HSCAN**" and optional argument :target:`cursor` | :target:`iterations` was implemented.

@pi-r2/redis
============

.. versionchanged:: 0.3.0

  - Package will be published under ``@pi-r/redis`` and developed under ``pi-r2/src/db/redis`` for future releases.

.. versionadded:: 0.2.0

  - Staging package for the ``redis 5.x`` release was created.