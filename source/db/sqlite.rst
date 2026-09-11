======
SQLite
======

- `NodeJS v26 <https://nodejs.org/api/sqlite.html#sqlite>`_ :alt:`(node:sqlite)`
- **npm** i *@pi-r/sqlite*

Interface
=========

.. code-block:: typescript

  import type { AggregateOptions, DatabaseSyncOptions, PrepareOptions, SQLInputValue } from "node:sqlite";

  interface SQLiteDataSource extends DbDataSource {
      source: "sqlite";
      query?: string;
      params?: SQLInputValue | SQLInputValue[];
      options?: PrepareOptions;
      create?: string | string[];
      update?: string | SQLiteUpdateObject;
  }

  interface SQLiteDatabaseConfig {
      memory?: boolean;
      path?: string;
      options?: DatabaseSyncOptions;
      extras?: {
          backup_access?: boolean | string;
          aggregate?: Record<string, AggregateOptions>;
          aggregate_module?: boolean;
          session_timeout?: number | string;
      };
      roles?: Record<string, SQLiteAuthorization>;
      users?: Record<string, SQLiteUserPrivileges>;
  }

  interface SQLiteAuthorization {
      allow?: string[];
      deny?: string[];
      ignore?: string[];
  }

  interface SQLiteUserPrivileges extends SQLiteAuthorization {
      roles?: string[];
  }

  interface SQLiteUpdateObject {
      sql: string;
      params: SQLInputValue[][];
      options?: PrepareOptions;
  }

Authentication
==============

- `Connection <https://nodejs.org/api/sqlite.html#new-databasesyncpath-options>`_
- `Date Format <https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_date-format>`_

::

  {
    "dataSource": {
      "credential": null, // auto-populated through server settings + Host authentication
      "name": "main"
    }
  }

.. code-block::
  :caption: squared.db.json

  {
    "sqlite": {
      "main": {
        "path": "./data/db/demo.sqlite3",
        "options": {
          "readOnly": false,
          "allowBareNamedParameters": true
        },
        "extras": {
          "session_timeout": "1h" // Calls db.close() + Clears user cache
        },
        "roles": {
          "admin": {
            "allow": ["*"]
          },
          "reader": {
            "allow": ["READ", "SELECT"],
            "ignore": ["COPY"] // Does not cancel subsequent actions
          },
          "all_users": { // Inherited first by all sessions
            "deny": ["*"]
          }
        },
        "users": {
          "username": { // JWT authentication
            "roles": ["reader"],
            "allow": ["INSERT", "UPDATE"]
          }
        }
      },
      "daemon": {
        "memory": true,
        "path": "./data/db/init.sql", // Optional
        "extras": {
          "backup_access": "./data/backup/daemon-%Y-%m-%d.sqlite3", // Numeric specifiers only
          "session_timeout": 0 // Not used
        },
        "roles": {/* Same */},
        "users": {/* Same */}
      }
    }
  }

- `Authorization action codes <https://nodejs.org/api/sqlite.html#authorization-action-codes>`_

.. list-table::
  :width: 600px
  :widths: 33 33 33

  * - SQLITE_CREATE_INDEX
    - SQLITE_CREATE_TABLE
    - SQLITE_CREATE_TEMP_INDEX
  * - SQLITE_CREATE_TEMP_TABLE
    - SQLITE_CREATE_TEMP_TRIGGER
    - SQLITE_CREATE_TEMP_VIEW
  * - SQLITE_CREATE_TRIGGER
    - SQLITE_CREATE_VIEW
    - SQLITE_DELETE
  * - SQLITE_DROP_INDEX
    - SQLITE_DROP_TABLE
    - SQLITE_DROP_TEMP_INDEX
  * - SQLITE_DROP_TEMP_TABLE
    - SQLITE_DROP_TEMP_TRIGGER
    - SQLITE_DROP_TEMP_VIEW
  * - SQLITE_DROP_TRIGGER
    - SQLITE_DROP_VIEW
    - SQLITE_INSERT
  * - SQLITE_PRAGMA
    - SQLITE_READ
    - SQLITE_SELECT
  * - SQLITE_TRANSACTION
    - SQLITE_UPDATE
    - SQLITE_ATTACH
  * - SQLITE_DETACH
    - SQLITE_ALTER_TABLE
    - SQLITE_REINDEX
  * - SQLITE_ANALYZE
    - SQLITE_CREATE_VTABLE
    - SQLITE_DROP_VTABLE
  * - SQLITE_FUNCTION
    - SQLITE_SAVEPOINT
    - SQLITE_COPY
  * - SQLITE_RECURSIVE
    -  
    -  

Example usage
=============

- `Query <https://sqlite.org/lang.html>`_

::

  {
    "selector": "img",
    "type": "attribute",
    "dataSource": {
      "source": "sqlite",
      "name": "main",

      "create": [
        "CREATE TABLE demo (id int, title varchar(50)); CREATE TABLE user (id int, name varchar(50));", // db.exec()
        "INSERT INTO demo VALUES (1, 'Hello'); INSERT INTO demo VALUES (2, 'World');"
      ],

      "update": {
        "sql": "INSERT INTO demo VALUES (?, ?)", // db.prepare()
        "params": [
          [1, "Hello"], // run(1, "Hello")
          [2, "World"]  // run(2, "World")
        ]
      },

      "query": "SELECT * FROM ? WHERE ID = ?", // db.prepare().all("demo", 2)
      "options": {
        "allowBareNamedParameters": false
      }
    }
  }

@pi-r/sqlite
============

.. versionadded:: 0.13.1

  - Initial release under ``@pi-r/sqlite`` with a :alt:`NodeJS 24.10` requirement.