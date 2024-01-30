=============
MongoDB Atlas
=============

- https://www.mongodb.com/cloud/atlas/register
- **npm** i *@pi-r/atlas*

.. tip:: Atlas connections are compatible with the :doc:`@pi-r/mongodb <../db/mongodb>` plugin.

Interface
=========

.. code-block:: typescript

  import type { MongoDBDataSource } from "../db/mongodb";
  import type { MongoClientOptions } from "mongodb";

  interface AtlasDatabaseQuery extends MongoDBDataSource {
      source: "cloud";
      service: "atlas";
      uri: string;
      credential: string | AtlasDatabaseCredential;
      table: string;
  }

  interface AtlasDatabaseCredential extends AuthValue, MongoClientOptions {/* Empty */}

Authentication
==============

- `Connection <https://www.mongodb.com/docs/drivers/node/current/fundamentals/authentication/mechanisms>`_

.. code-block::

  {
    "dataSource": {
      "uri": "mongodb+srv://<username>:<password>@cluster0.abcdef.mongodb.net/<database>", // Required
      /* OR */
      "credential": "main", // squared.cloud.json
      /* OR */
      "credential": {
        "server": "localhost:27017", // OR: 0.0.0.0
        /* OR */
        "hostname": "cluster0.abcdef.mongodb.net",
        "port": 8080, // Default is "27017"

        "username": "**********",
        "password": "**********",
        /* OR */
        "auth": {
          "username": "**********",
          "password": "**********"
        },

        /* Same as @pi-r/mongodb */
      }
    }
  }

Example usage
=============

- `Query <https://www.mongodb.com/docs/compass/master/query/filter>`_

.. code-block::

  {
    "selector": "img",
    "type": "attribute",
    "dataSource": {
      "source": "cloud",
      "service": "atlas",
      "credential": {/* Authentication */},
      "table": "demo",

      "name": "nodejs", // Database name (optional)

      "id": "1", // Alias for "_id"
      /* OR */
      "query": {
        "id": {
          "$eq": "1"
        },
        "start_date": {
          "$gt": "new Date('2021-01-01')" // When using web service
        },
        "$in": ["new RegExp(^mongodb, i)"], // Quotes are optional [/^mongodb/i]
        "$where": "function() { return this.name == 'mongodb.com'; }" // async is supported
      },

      "value": "<b>${title}</b>: ${description}", // See "/document/data.html"

      /* Update */
      "id": "1", // Same as item above
      /* OR */
      "query": {/* Filter<Document> */},

      "updateType": 0, // findOneAndUpdate
      "updateType": 1, // limit > 1 ? updateMany : findOneAndUpdate
      "updateType": 2, // findOneAndReplace
      "updateType": 3, // findOneAndDelete
      "update": {/* UpdateFilter<Document> */},

      "update": [/* Document */, /* Document */] // Not related to query (insertMany)
    }
  }