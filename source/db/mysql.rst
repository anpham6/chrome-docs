=====
MySQL
=====

- `MySQL Community Server <https://dev.mysql.com/downloads/mysql>`_
- **npm** i *@pi-r/mysql*

Interface
=========

.. code-block:: typescript
  :emphasize-lines: 9

  import type { PoolOptions, QueryOptions } from "mysql2/promise";
  import type { SecureContextOptions } from "tls";

  interface MySQLDataSource extends DbDataSource {
      source: "mysql";
      credential: string | MySQLCredential;
      query?: string | QueryOptions;
      params?: unknown;
      preparedStatement?: boolean;
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
      idle_max?: number; // maxIdle
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

.. _mysql-prepared-statements:

- `Prepared Statements <https://sidorares.github.io/node-mysql2/docs/examples/queries/prepared-statements>`_

::

  [
    { "query": "SELECT 1" }, // 1
    { "query": "SELECT * FROM `users` WHERE `name` = ?", "params": ["John"], "preparedStatement": true }, // OK
    { "params": ["Herbert"] }, // OK
    { "query": "SELECT 1", "params": ["Cactus"] }, // 1
    { "query": "SELECT * FROM `users` WHERE `age` > ?", "params": [33], "preparedStatement": true }, // OK
    { "params": ["Phillip"] }, // ERROR
    { "query": "SELECT 1", "preparedStatement": false }, // 1
    { "params": [36] } // ERROR
  ]

.. note:: Queries cannot be run in **parallel** and only with **connectOnce** enabled.

@pi-r/mysql
===========

.. versionadded:: 0.11.1

  - *MySQLDataSource* property **preparedStatement** as :alt:`boolean` for initiating a series of repetitive queries was created.

.. versionadded:: 0.11.0

  - *PoolConfig* property **idle_max** as :alt:`maxIdle` was implemented.

.. versionadded:: 0.10.0

  - *DbPool* static property **CACHE_IGNORE** through :target:`@pi-r/mysql/client/pool` as :alt:`keyof PoolOptions` was implemented.

.. versionadded:: 0.8.0

  - *DbPool* static property **CACHE_UNUSED** through :target:`@pi-r/mysql/client/pool` as :alt:`keyof PoolOptions` was implemented.
  - *SslOptions* property **ca** with Amazon RDS CA [#]_ cert for *host* :alt:`rds.amazonaws.com` is attached when installed.

.. [#] npm i aws-ssl-profiles