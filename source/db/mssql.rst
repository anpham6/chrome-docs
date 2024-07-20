==========
SQL Server
==========

- `SQL Server 2022 Express <https://www.microsoft.com/en-us/sql-server/sql-server-downloads>`_
- **npm** i *@pi-r/mssql*

Interface
=========

.. code-block:: typescript

  import type { ConnectionConfiguration } from 'tedious';
  import type { DataType, ParameterData } from "tedious/lib/data-type";
  import type { PoolConfig } from "@e-mc/mssql/types/pool"; // From "@types/tedious-connection-pool"

  interface MSSQLDataSource extends DbDataSource {
      source: "mssql";
      credential: string | MSSQLCredential;
      query?: string;
      params?: MSSQLRequestParameters | MSSQLRequestWithOutputParameters;
      storedProc?: boolean;
      usePool?: boolean | string | PoolConfig; // External pool provider configurable options
  }

  interface MSSQLCredential extends ServerAuth, ConnectionConfiguration {/* Empty */}

  interface MSSQLRequestWithOutputParameters {
      input?: MSSQLRequestParameters;
      output?: MSSQLRequestParameters;
  }

  interface MSSQLRequestParameterValue {
      name?: string;
      value?: unknown;
      type?: DataType;
      options?: ParameterData;
  }

  type MSSQLRequestParameters = MSSQLRequestParameterValue[] | ObjectMap<MSSQLRequestParameterValue>;

Pool
----

.. code-block:: typescript

  import type { PoolConfig } from "@e-mc/mssql/types/pool";

  interface PoolConfig {
      min?: number; // min
      max?: number; // max
      idle?: number; // idleTimeout
      queue_idle?: number; // acquireTimeout
  }

Authentication
==============

- `Connection <https://tediousjs.github.io/tedious/api-connection.html>`_

.. code-block:: javascript

  {
    "dataSource": {
      "uri": "<username>:<password>@localhost:1433/<database>", // authentication.options@server:options
      /* OR */
      "credential": "main", // squared.db.json
      /* OR */
      "credential": {
        "server": "localhost",
        "options": {
          "port": 1433,
          "database": "example",
          "trustServerCertificate": true, // Local development

          /* Azure */
          "encrypt": true,
          "enableArithAbort": true,
          "connectionIsolationLevel": 2 // ISOLATION_LEVEL.READ_UNCOMMITTED
        },
        "authentication": {
          "type": "default",
          "options": {
            "userName": "**********",
            "password": "**********"
          }
        }
      }
    }
  }

Example usage
=============

- `Query <https://learn.microsoft.com/en-us/sql/t-sql/queries/select-transact-sql>`_
- `Parameters <http://tediousjs.github.io/tedious/parameters.html>`_

::

  {
    "selector": "img",
    "type": "attribute",
    "dataSource": {
      "source": "mssql",
      "credential": {/* Authentication */},

      "query": "SELECT * FROM table WHERE id = @name AND value = @value", // db.execSql
      "query": "./path/to/statement.sql", // Extension ".sql" (settings.directory.sql + users/username/?)
      /* OR */
      "query": "uspGetItems", // db.callProcedure
      "storedProc": true,

      "params": { "a": { "value": "1", "type": "VarChar", "options": { "length": 50 } }, "b": 2 /* Implicit: Int */ }, // MSSQLRequestParameters
      "params": [{ "name": "c", "type": "Decimal", "value": 12.345, "options": { "precision": 10, "scale": 2 } }],
      "params": [{ "name": "d", "type": "TVP", "value": { "columns": [/* MSSQLRequestParameters[] */], "rows": [/* unknown[][] */] }],
      "params": {
        "input": {/* MSSQLRequestParameters */}, // Two keys only for object detection (required)
        "output": {/* MSSQLRequestParameters */} // Last row i{/* MSSQLRequestParameters */}n result (data["__returnvalue__"] = true)
      },

      /* Result: { "item_src": "mssql.png", "item_alt": "SQL Server" } */
      "value": {
        "src": "item_src",
        "alt": "item_alt"
      },

      "usePool": true,
      "usePool": { // tedious-connection-pool2
        "min": 0,
        "max": 10
      }
    }
  }

@pi-r/mssql
===========

.. versionadded:: 0.8.0

  - NPM package **tedious** was upgraded from **16.7** to :target:`18.3` with minimum :alt:`NodeJS 20` requirement.