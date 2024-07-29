=====
MySQL
=====

- `MySQL Community Server <https://dev.mysql.com/downloads/mysql>`_
- **npm** i *@pi-r/mysql*

Interface
=========

.. code-block:: typescript

  import type { PoolOptions, QueryOptions } from "mysql2/promise";
  import type { SecureContextOptions } from "tls";

  interface MySQLDataSource extends DbDataSource {
      source: "mysql";
      credential: string | MySQLCredential;
      query?: string | QueryOptions;
      params?: unknown;
  }

  interface MySQLCredential extends ServerAuth, PoolOptions {
      ssl?: boolean | string | SecureContextOptions & { rejectUnauthorized?: boolean };
  }

Pool
----

.. code-block:: typescript

  import type { PoolOptions } from "mysql2/promise";

  interface PoolConfig {
      max?: number; // connectionLimit
      idle?: number; // idleTimeout
      queue_max?: number; // queueLimit
      timeout?: number; // connectTimeout
  }

Authentication
==============

- `Connection <https://sidorares.github.io/node-mysql2/docs/examples/connections/create-connection>`_

::

  {
    "dataSource": {
      "uri": "mysql://<username>:<password>@localhost:3306/<database>",
      /* OR */
      "credential": "main", // squared.db.json
      /* OR */
      "credential": {
        "host": "localhost", // Required
        "port": 3306,
        "user": "**********", // Required
        "password": "**********",
        "database": "example"
      },
      /* OR */
      "credential": {
        "socketPath": "/tmp/mysql.sock",
        "user": "**********",
        "password": "**********",
        "database": "example"
      }
    }
  }

Example usage
=============

- `Query <https://sidorares.github.io/node-mysql2/docs/examples/queries/simple-queries/select>`_

::

  {
    "selector": "img",
    "type": "attribute",
    "dataSource": {
      "source": "mysql",
      "credential": {/* Authentication */},

      "query": "SELECT * FROM table WHERE id = ? AND value = ?",
      "query": "./path/to/statement.sql", // Extension ".sql" (settings.directory.sql + users/username/?)
      "params": [1, "escaped"],
      /* OR */
      "query": "SELECT * FROM table WHERE id = :id AND value = :value",
      "params": { "id": 1, "value": "escaped" },

      /* Result: { "item_src": "mysql.png", "item_alt": "MySQL" } */
      "value": {
        "src": "item_src",
        "alt": "item_alt"
      },

      "usePool": true,
      "options": {
        "connectionLimit": 10,
        "waitForConnections": true
      }
    }
  }

@pi-r/mysql
===========

.. versionadded:: 0.8.0

  - *DbPool* interface with static property **CACHE_UNUSED** through :target:`@pi-r/mysql/client/pool` as :alt:`string[]` was implemented.
  - *SslOptions* property **ca** with Amazon RDS CA [#]_ cert for *host* :alt:`rds.amazonaws.com` is attached when installed.

.. [#] npm i aws-ssl-profiles