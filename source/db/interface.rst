=========
Interface
=========

- `Encoding <https://nodejs.org/api/buffer.html#buffers-and-character-encodings>`_

.. code-block:: typescript

  interface DataSource {
      source: string;

      uri?: string; // Connection string
      limit?: number; // Max rows in result
      query?: unknown; // SELECT statement or equivalent syntax
      encoding?: BufferEncoding;

      ignoreCache?: boolean; // Bypass cache without saving
      ignoreCache?: 0 | 1; // 0 - renew cache expiration | 1 - purge cache with saving
      ignoreCache?: [number, number?, number?]; // <= min + max > + renew|purge

      /* Module: Document */
      index?: number; // Pick one specific row
      removeEmpty?: boolean; // Remove element when rows equals 0
      postQuery?: string | ((result: unknown[], item: DataSource) => Void<unknown[]>); // Modify arguments or logging (parseable)
      preRender?: string | ((output: string, item: DataSource) => Void<string>);
      whenEmpty?: string | ((result: unknown[], item: DataSource) => Void<unknown[]>);

      /* Internal */
      transactionState?: number;
      transactionFail?: boolean;
  }

.. code-block:: typescript

  interface DbDataSource extends DataSource {
      source: string; // Built-in alias | NPM package name

      name?: string; // Database identifier
      table?: string;

      credential?: string; // Stored settings by name
      credential?: PlainObject; // Client supplied by request

      parallel?: boolean; // Active with batched queries (implicit: true)
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

.. seealso:: For any non-standard named definitions check :doc:`References </references>`.

Global
======

.. code-block:: typescript

  interface ServerAuth {
      protocol?: string;
      server?: string;
      hostname?: string;
      port?: number;
      database?: string;
      username?: string;
      password?: string;
  }

.. attention:: Enabling usePool with a UUID key will also copy the value into credential.uuidKey [#]_.

.. [#] Does not override other existing uuidKey sessions.