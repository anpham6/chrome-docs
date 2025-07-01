====
Pool
====

Each data source provider will associate each client setting with their equivalent system pool setting.

.. code-block:: typescript
  :caption: squared.db.json

  interface PoolConfig {
      min?: number; // Minimum connections
      max?: number; // Maximum connections
      idle?: number; // Maximum idle time before closing connection (ms)
      queue_max?: number; // Maximum clients that can be waiting for a connection
      queue_idle?: number; // Maximum time a client can be waiting for a connection (ms)
      timeout?: number; // Maximum time to establish a database connection (ms)
      socket_timeout?: number; // Maximum time without data being sent or received (ms)
      server_timeout?: number; //  Maximum time to establish a server connection (ms) 

      /* Module: Db */
      purge?: number; // Will check pool idle time when global memory is purged
  }

.. note:: Not all properties are supported per provider.