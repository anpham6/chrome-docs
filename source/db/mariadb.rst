=======
MariaDB
=======

- `MariaDB Server <https://mariadb.org/download>`_
- **npm** i *@pi-r/mariadb*

Interface
=========

.. code-block:: typescript

  import type { PoolConfig, QueryConfig } from "mariadb";
  import type { SecureContextOptions } from "tls";

  interface MariaDBDataSource extends DbDataSource {
      source: "mariadb";
      credential: string | MariaDBCredential;
      query?: string | QueryConfig;
      params?: unknown;
  }

  interface MariaDBCredential extends ServerAuth, PoolConfig {
      ssl?: boolean | string | SecureContextOptions & { rejectUnauthorized?: boolean };
  }

Pool
----

.. code-block:: typescript

  import type { PoolConfig } from "mariadb";

  interface PoolConfig {
      min?: number; // minimumIdle
      max?: number; // connectionLimit
      idle?: number; // idleTimeout
      queue_idle?: number; // acquireTimeout
      timeout?: number; // connectTimeout
      socket_timeout?: number; // socketTimeout
  }

Authentication
==============

- `Connection <https://github.com/mariadb-corporation/mariadb-connector-nodejs/blob/master/documentation/promise-api.md#connection-options>`_

::

  {
    "dataSource": {
      "uri": "<username>:<password>@localhost:3306/<database>",
      /* OR */
      "credential": "main", // squared.db.json
      /* OR */
      "credential": {
        "host": "localhost", // Required
        "port": 3306, // Required
        "user": "**********", // Required
        "password": "**********",
        "database": "example"
      },
      /* OR */
      "credential": {
        "socketPath": "/var/run/mysqld/mysql.sock",
        "user": "**********",
        "password": "**********",
        "database": "example"
      }
    }
  }

Example usage
=============

- `Query <https://github.com/mariadb-corporation/mariadb-connector-nodejs/blob/master/documentation/promise-api.md#connection-api>`_

::

  {
    "selector": "img",
    "type": "attribute",
    "dataSource": {
      "source": "mariadb",
      "credential": {/* Authentication */},

      "query": "SELECT * FROM table WHERE id = ? AND value = ?",
      "query": "./path/to/statement.sql", // Extension ".sql" (settings.directory.sql + users/username/?)
      "params": [1, "escaped"],
      /* OR */
      "query": { "namedPlaceholders": true, "sql": "SELECT * FROM table WHERE id = :id AND value = :value" },
      "params": { "id": 1, "value": "escaped" },

      /* Result: { "item_src": "mariadb.png", "item_alt": "MariaDB" } */
      "value": {
        "src": "item_src",
        "alt": "item_alt"
      },

      "usePool": true,
      "options": {
        "minimumIdle": 0,
        "connectionLimit": 10
      }
    }
  }

@pi-r/mariadb
=============

.. versionadded:: 0.8.0

  - *DbPool* static property **CACHE_UNUSED** through :target:`@pi-r/mariadb/client/pool` as :alt:`string[]` was implemented.
  - *SecureContextOptions* (:alt:`NodeJS.tls`) property **ca** with Amazon RDS CA [#]_ cert for *host* :alt:`rds.amazonaws.com` is attached when installed.

.. versionadded:: 0.6.2

  - *PoolConfig* property **queue_idle** was implemented.
  
.. [#] npm i aws-ssl-profiles