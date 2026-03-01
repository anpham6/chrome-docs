=========
Interface
=========

.. highlight:: typescript

.. code-block::

  interface DataSource {
      source: string;

      uri?: string; // Connection string
      limit?: number; // Max rows in result
      query?: unknown; // SELECT statement or equivalent syntax
      encoding?: BufferEncoding;

      ignoreCache?: boolean; // Bypass cache without saving
      ignoreCache?: 0 | 1; // 0 - renew cache expiration | 1 - purge cache with saving
      ignoreCache?: [number, number?, number?]; // n <= min | n > max | renew=0,bypass=1,purge=2

      /* Module: Document */
      index?: number; // Pick one specific row
      removeEmpty?: boolean; // Remove element when rows equals 0
      postQuery?: string | ((result: unknown[], item: DataSource) => unknown[] | void); // Modify arguments or logging (parseable)
      preRender?: string | ((output: string, item: DataSource) => string | void);
      whenEmpty?: string | ((result: unknown[], item: DataSource) => unknown[] | void);

      /* Internal */
      transactionState?: number;
      transactionFail?: boolean;
  }

::

  interface DbDataSource extends DataSource {
      source: string; // Built-in alias | NPM package name

      name?: string; // Database identifier
      table?: string;

      credential?: string; // Stored settings by name
      credential?: PlainObject; // Client supplied by request

      parallel?: boolean; // Active with batched queries (implicit: true)
      flat?: number; // Apply Array.flat(depth) to rows
      streamRow?: boolean; // Read streaming when available
      streamRow?: string | ((row: unknown) => Error | false | void); // Modify row + exclude (parseable)

      update?: unknown; // Syntax by provider
      options?: PlainObject; // Used to configure get commands

      /* Module: Db */
      withCommand?: string | [string, string]; // Will assign PlainObject from "User = settings.users[username]" to target
      withCommand: string; // Equivalent to [name:table || table || name || document, string]
      withCommand: [string, string]; // User.db.commands["0"]["1"] = { query: unknown }

      usePool?: boolean; // Globally managed and released
      usePool?: string; // UUIDv1-5 shared session key (db.settings.user_key: username@server/database)

      /* Module: Document */
      willAbort?: boolean; // Abort is called bypassing settings
  }

Changelog
=========

.. versionadded:: 0.13.6

  - *DataSource* property **ignoreCache** as :alt:`number[]` can bypass storage and retrieval when result length is not within the specified range.

.. note:: Backported: 0.12.14 / 0.11.14 / 0.10.18 / 0.9.27 / 0.8.28 [#]_

.. versionadded:: 0.10.1

  - *DbDataSource* property **flat** for concatenating multiple results was created.

Global
======

::

  interface ServerAuth {
      protocol?: string;
      server?: string;
      hostname?: string;
      port?: number;
      database?: string;
      username?: string;
      password?: string;
  }

.. attention:: Enabling **usePool** with a *UUID* key will also copy the value into ``credential.uuidKey`` [#]_.

.. [#] Purging is supported only when using **0.13.x**.
.. [#] Does not override other existing uuidKey sessions.