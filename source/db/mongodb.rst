MongoDB
=======

- `MongoDB Community Server <https://www.mongodb.com/try/download/community>`_
- **npm** i *@pi-r/mongodb*

.. note:: MongoDB Atlas installations can also use the "mongodb" source format.

Interface
---------

.. code-block:: typescript

  import type * as "m" from "mongodb";

  interface MongoDBDataSource extends DbDataSource {
      source: "mongodb";
      table: string;

      uri: string; // Connection string
      /* OR */
      credential: string | MongoDBCredential;

      id?: string; // Uses ObjectId
      query?: m.Filter<m.Document> | MongoDBFilterValue;
      query?: { value: m.Filter<m.Document>, options: m.CommandOperationOptions }; // "value" is required when using "options"
      aggregate?: m.Document[] | { pipeline: m.Document[], options: m.AggregateOptions };

      command?: m.Document | m.Document[]; // Calls m.runCommand before any queries

      update?: m.UpdateFilter<m.Document> | m.OptionalUnlessRequiredId<unknown>[];
      updateType?: 0 | 1 | 2 | 3; // 0 - update | 1 - insert | 2 - replace | 3 - delete

      options?: m.MongoClientOptions | m.UpdateFilter<m.Document> | m.OptionalUnlessRequiredId<unknown>[];
      client?: {
          db?: m.DbOptions; // Used as options with "name"
          collection?: m.CollectionOptions; // Used as options with "table"
          command?: m.RunCommandOptions; // Used as options with "command"
      };
      execute?: {
          insert?: m.BulkWriteOptions; // Used as options with "update - insert"
          update?: m.UpdateOptions; // Used as options with "update"
      };

      sort?: string | m.Sort | { value: m.Sort, direction: m.SortDirection };
  }

  interface MongoDBCredential extends ServerAuth, m.MongoClientOptions {/* Empty */}

Pool
~~~~

.. code-block:: typescript

  import type { MongoClientOptions } from "mongodb";

  interface PoolConfig {
      min?: number; // minPoolSize
      max?: number; // maxPoolSize
      idle?: number; // maxIdleTimeMS
      queue_max?: number; // maxConnecting
      queue_idle?: number; // waitQueueTimeoutMS
      timeout?: number; // connectTimeoutMS
      socket_timeout?: number; // socketTimeoutMS
  }

Authentication
--------------

- `Connection <https://www.mongodb.com/docs/drivers/node/current/fundamentals/authentication/mechanisms>`__

.. code-block::

  {
    "dataSource": {
      "uri": "mongodb://<username>@<password>:localhost:27017",
      /* OR */
      "credential": "main", // squared.db.json
      /* OR */
      "credential": {
        "server": "localhost:27017", // OR: 0.0.0.0
        /* OR */
        "hostname": "cluster0.abcdef.mongodb.net", // Required
        "port": 8080, // Default is "27017"

        "username": "**********",
        "password": "**********",
        /* OR */
        "auth": {
          "username": "**********",
          "password": "**********"
        },

        /* Optional */
        "protocol": "mongodb+srv:", // "mongodb:" (default)

        "authMechanism": "MONGODB-AWS",
        "authMechanismProperties": { "AWS_SESSION_TOKEN": "**********" },
        "authSource": "$external",

        "tlsCertificateKeyFile": "/path/to/tls/x509/key.pem",
        "tlsCertificateKeyFilePassword": "",
        "tlsCAFile": "",
        "tlsCRLFile": "",
        "tlsAllowInvalidHostnames": false,
        "tlsAllowInvalidCertificates": false,
        "tlsInsecure": false
      }
    }
  }

Example usage
-------------

- `Query <https://www.mongodb.com/docs/compass/master/query/filter>`__

.. code-block::

  {
    "selector": "img",
    "type": "attribute",
    "dataSource": {
      "source": "mongodb",
      "credential": {/* Authentication */},
      "table": "demo",

      "name": "nodejs", // Database name (optional)

      "id": "1", // Alias for "_id"
      /* OR */
      "query": {
        "id": {
          "$eq": "1"
        },
        "name": {
          "$regex": "mongodb.*\\.com", // $regex: /mongodb.*\.com/si
          "$options": "si"
        },
        "start_date": {
          "$gt": "new Date('2021-01-01')" // new Date("2021-01-01")
        },
        "$in": ["new RegExp(^mongodb, i)"], // Quotes are optional [/^mongodb/i]
        "$where": "function() { return this.name == 'mongodb.com'; }" // "async" is supported
      },

      /* Result: { "item_src": "mongo.png", "item_alt": "MongoDB" } */
      "value": {
        "src": "item_src",
        "alt": "item_alt"
      },

      "usePool": true, // Optional
      "options": {
        "minPoolSize": 0,
        "maxPoolSize": 10
      },

      /* Update */
      "id": "1", // Same as item retrieved
      /* OR */
      "query": {/* Filter<Document> */},

      "updateType": 0, // db.findOneAndUpdate
      "updateType": 1, // limit > 1 ? db.updateMany : db.findOneAndUpdate
      "updateType": 2, // db.findOneAndReplace
      "updateType": 3, // db.findOneAndDelete
      "update": {/* UpdateFilter<Document> */},

      "update": [/* Document */, /* Document */] // Not related to query (db.insertMany)
    }
  }