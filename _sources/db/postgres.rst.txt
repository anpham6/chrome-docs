==========
PostgreSQL
==========

- `PostgreSQL Server <https://www.postgresql.org/download>`_
- **npm** i *@pi-r/postgres*

Interface
=========

.. code-block:: typescript
  :emphasize-lines: 8

  import type { QueryArrayConfig, PoolConfig } from "pg";

  interface PostgresDataSource extends DbDataSource {
      source: "postgres";
      credential: string | PostgresCredential;
      query?: string | QueryArrayConfig;
      params?: unknown[];
      options?: QueryStreamConfig;
  }

  interface PostgresCredential extends ServerAuth, PoolConfig {
      password?: string | (() => string | Promise<string>);
  }

Pool
----

.. code-block:: typescript

  import type { PoolConfig } from "pg";

  interface PoolConfig {
      min?: number; // min
      max?: number; // max
      idle?: number; // idleTimeoutMillis
      timeout?: number; // connectionTimeoutMillis
  }

Authentication
==============

- `Connection <https://node-postgres.com/features/connecting>`_

::

  {
    "dataSource": {
      "uri": "postgresql://<username>:<password>@localhost:5432/<database>", // Alias for "connectionString"
      /* OR */
      "credential": "main", // squared.db.json
      /* OR */
      "credential": {
        "host": "localhost", // Required
        "port": 5432,
        "user": "**********", // Required
        "password": "**********",
        "database": "example"
      }
    }
  }

Example usage
=============

- `Query <https://node-postgres.com/features/queries>`_

::

  {
    "selector": "img",
    "type": "attribute",
    "dataSource": {
      "source": "postgres",
      "credential": {/* Authentication */},

      "query": "SELECT * FROM table WHERE id = $1 AND value = $2",
      "query": "./path/to/statement.sql", // Extension ".sql" (settings.directory.sql + users/username/?)

      "params": [1, "escaped"],

      "streamRow": true,
      "query": "SELECT * FROM table", // string
      "options": { "batchSize": 10 }, // QueryStreamConfig

      /* Result: { "item_src": "postgres.png", "item_alt": "PostgreSQL" } */
      "value": {
        "src": "item_src",
        "alt": "item_alt"
      },

      "usePool": true,
      "options": {
        "min": 0,
        "max": 10
      }
    }
  }

@pi-r/postgres
==============

.. versionadded:: 0.12.0

  - *QueryStream* constructor supports using property **options** as :alt:`QueryStreamConfig`.

.. versionadded:: 0.8.0

  - *DbPool* static property **CACHE_UNUSED** through :target:`@pi-r/postgres/client/pool` as :alt:`string[]` was implemented.
  - *ConnectionOptions* :alt:`(NodeJS.tls)` property **ca** with Amazon RDS CA [#]_ cert for *host* :alt:`rds.amazonaws.com` is attached when installed.

.. [#] npm i aws-ssl-profiles