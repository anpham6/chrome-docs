======
Oracle
======

- `Oracle Database Express Edition <https://www.oracle.com/database/technologies/xe-downloads.html>`_
- **npm** i *@pi-r/oracle*

Interface
=========

.. code-block:: typescript

  import type { BindParameters, ConnectionAttributes, ExecuteOptions, InitialiseOptions, PoolAttributes } from "oracledb";

  interface OracleDataSource extends DbDataSource {
      source: "oracle";
      credential: string | OracleCredential;
      query?: string;
      params?: BindParameters;
      options?: ExecuteOptions;
  }

  interface OracleCredential extends ServerAuth, ConnectionAttributes, PoolAttributes, InitialiseOptions {/* Empty */}

Pool
----

.. code-block:: typescript
  :emphasize-lines: 10

  import type { PoolAttributes } from "oracledb";

  interface PoolConfig {
      min?: number; // poolMin
      max?: number; // poolMax
      idle?: number; // poolTimeout (ms)
      queue_max?: number; // queueMax
      queue_idle?: number; // queueTimeout
      timeout?: number; // connectTimeout (ms)
      init_imeout?: number; // transportConnectTimeout (ms)
  }

Authentication
==============

- `Connection <https://node-oracledb.readthedocs.io/en/latest/user_guide/connection_handling.html#connectionhandling>`_
- `Service names <https://node-oracledb.readthedocs.io/en/latest/user_guide/connection_handling.html#net-service-names-for-connection-strings>`_

::

  {
    "dataSource": {
      "uri": "<username>:<password>@localhost:1521/database", // Alias for "connectString" | "poolAlias"
      /* OR */
      "credential": "main", // squared.db.json
      /* OR */
      "credential": {
        "connectString": "localhost:1521/database",
        "user": "**********",
        "password": "**********",
        "walletLocation": "/home/username/oracle/wallet", // Optional
        "walletPassword": "**********"
      },
      /* OR */
      "credential": {
        "connectString": "nodejs_high",
        "configDir": "/opt/oracle/config", // Location of user tnsnames.ora
        "libDir": "/opt/oracle/instantclient_19_11" // Not recommended
      },
      /* OR */
      "credential": {
        "connectString": "localhost:1521/database",
        "externalAuth": true
      }
    }
  }

Example usage
=============

- `Query <https://node-oracledb.readthedocs.io/en/latest/user_guide/installation.html#example-a-sql-select-statement-in-node-js>`_

::

  {
    "selector": "img",
    "type": "attribute",
    "dataSource": {
      "source": "oracle",
      "credential": {/* Authentication */},

      "query": "SELECT * FROM table WHERE id = :id AND value = :value",
      "query": "./path/to/statement.sql", // Extension ".sql" (settings.directory.sql + users/username/?)

      "params": [1, "escaped"],

      /* Result: { "ITEM_SRC": "oracle.png", "ITEM_ALT": "Oracle" } */
      "value": {
        "src": "ITEM_SRC",
        "alt": "ITEM_ALT"
      },

      "usePool": true,
      "options": {
        "poolMin": 0,
        "poolMax": 10
      }
    }
  }

.. _db-oracle-thick-mode:

Thick Mode
==========

- `Initialization <https://node-oracledb.readthedocs.io/en/latest/user_guide/initialization.html>`_

.. code-block:: javascript
  :caption: using process.env

  NODE_ORACLEDB_DRIVER_MODE = "thick";
  NODE_ORACLEDB_CLIENT_LIB_DIR = "/opt/oracle/product/21c/dbhomeXE"; // libDir (overrides ORACLE_HOME)
  NODE_ORACLEDB_CLIENT_CONFIG_DIR = ""; // configDir
  NODE_ORACLEDB_CLIENT_DRIVER_NAME = ""; // driverName
  NODE_ORACLEDB_CLIENT_ERROR_URL = ""; // errorUrl

.. important:: These are not official Oracle environment variables and are used to initialize the client only when the module is first loaded.

.. code-block:: typescript

  interface InitialiseOptions {
      /**
       * This specifies the directory in which the Optional Oracle Net Configuration and Optional Oracle Client Configuration files reside. It is equivalent to setting the Oracle environment variable TNS_ADMIN to this value. Any value in that environment variable prior to the call to oracledb.initOracleClient() is ignored. If this attribute is not set, Oracle’s default configuration file search heuristics are used.
       */
      configDir?: string | undefined;
      /**
       * This specifies the driver name value shown in database views, such as V$SESSION_CONNECT_INFO. It can be used by applications to identify themselves for tracing and monitoring purposes. The convention is to separate the product name from the product version by a colon and single space characters. If this attribute is not specified, the value “node-oracledb : version” is used.
       *
       * @see https://oracle.github.io/node-oracledb/doc/api.html#otherinit
       */
      driverName?: string | undefined;
      /**
       * This specifies the URL that is included in the node-oracledb exception message if the Oracle Client libraries cannot be loaded. This allows applications that use node-oracledb to refer users to application-specific installation instructions. If this attribute is not specified, then the node-oracledb installation instructions URL is used.
       *
       * @see https://oracle.github.io/node-oracledb/doc/api.html#otherinit
       */
      errorUrl?: string | undefined;
      /**
       * This specifies the directory containing the Oracle Client libraries. If libDir is not specified, the default library search mechanism is used. If your client libraries are in a full Oracle Client or Oracle Database installation, such as Oracle Database “XE” Express Edition, then you must have previously set environment variables like ORACLE_HOME before calling initOracleClient().
       *
       * @see https://oracle.github.io/node-oracledb/doc/api.html#oracleclientloading
       */
      libDir?: string | undefined;
  }

@pi-r/oracle
============

.. versionadded:: 0.10.0

  - *DbPool* static property **CACHE_IGNORE** through :target:`@pi-r/oracle/client/pool` as :alt:`keyof PoolAttributes` was implemented.

.. versionadded:: 0.8.0

  - *DbPool* static property **CACHE_UNUSED** through :target:`@pi-r/oracle/client/pool` as :alt:`keyof PoolAttributes` was implemented.
  - *OracleCredential* property **connectString** | **connectionString** with `Centralized Configuration Providers <https://node-oracledb.readthedocs.io/en/latest/user_guide/connection_handling.html#connecting-using-centralized-configuration-providers>`_ is supported.