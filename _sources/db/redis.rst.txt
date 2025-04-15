=====
Redis
=====

- `Redis Stack <https://redis.io/downloads/#redis-stack-downloads>`_
- **npm** i *@pi-r/redis*

Interface
=========

.. code-block:: typescript

  import type { CommandOptions } from "@redis/client/dist/lib/command-options";
  import type { ClientCommandOptions } from "@redis/client/dist/lib/client";
  import type { ScanOptions } from "@redis/client/dist/lib/commands/generic-transformers";
  import type { RedisClientOptions } from "@redis/client";
  import type { RediSearchSchema, SearchOptions } from "redis";

  import type { CreateOptions } from "@redis/search/dist/commands/CREATE"; // Internal
  import type { AggregateOptions } from "@redis/search/dist/commands/AGGREGATE";

  interface RedisDataSource extends DbDataSource {
      source: "redis";

      uri: string; // redis://<username>:<password>@hostname:6379
      username?: string; // redis://hostname:6379
      password?: string;
      credential?: string | ServerAuth;
      database?: number;

      format?: "HASH" | "JSON" | "HKEYS" | "HVALS" | "HSCAN"; // Default is "HASH"
      key?: string | Buffer | (string | Buffer)[];
      field?: string | Buffer;
      path?: string; // JSONPath

      cursor?: number | number[]; // Scan
      iterations?: number | number[];

      search?: {
          index: string; // Preexisting schema
          schema?: RediSearchSchema; // Temporary schema
          schema?: string; // settings.directory.schema + users/username/?
          query: string;
          options?: CreateOptions;
      };
      aggregate?: {/* Same */};

      options?: {
          client?: RedisClientOptions;
          command?: RedisCommandOptions;
          get?: PlainObject;
          search?: SearchOptions;
          aggregate?: AggregateOptions;
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

  type RedisCredential = ServerAuth;

Pool
----

.. code-block:: typescript

  import type { RedisClientOptions } from "redis";

  interface PoolConfig { // using isolationPoolOptions
      min?: number; // min
      max?: number; // max
      idle?: number; // idleTimeoutMillis
      queue_max?: number; // maxWaitingClients
      queue_idle?: number; // softIdleTimeoutMillis
      timeout?: number; // acquireTimeoutMillis
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

      "usePool": true,
      "options": {
        "client": {
          "isolationPoolOptions": {
            "min": 0,
            "max": 10
          }
        }
      }
    }
  }

.. note:: Search will only return the **value** object with the **id** field appended as ``__id__``.

@pi-r/redis
===========

.. versionadded:: 0.8.0

  - *RedisDataSource* property **format** with type "**HSCAN**" and optional argument :target:`cursor` | :target:`iterations` was implemented.