===========================
Oracle Cloud Infrastructure
===========================

- **npm** i *@pi-r/oci*

Storage
=======

- https://www.oracle.com/cloud/storage/object-storage

.. note:: Uses :doc:`S3 <aws>` [#s3]_ compatibility API (AWS v2) and signature (v4).

Interface
---------

.. code-block:: typescript

  import type { CloudStorage } from "./interface";
  import type { ConfigurationOptions } from "aws-sdk/lib/core";

  interface OCIStorage extends CloudStorage {
      service: "oci";
      credential: string | OCIStorageCredential;
      bucket: string;
  }

  interface OCIStorageCredential extends ConfigurationOptions {
      accessKeyId: string;
      secretAccessKey: string;
      region?: string;
      endpoint?: string;
      namespace?: string;
  }

Authentication
--------------

- `Credentials <https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/s3compatibleapi.htm>`_

.. code-block::

  {
    "dataSource": {
      "credential": "main", // squared.cloud.json
      /* OR */
      "credential": {
        "accessKeyId": "**********",
        "secretAccessKey": "**********",
        /* OR */
        "namespace": "nodejs", // Unofficial
        "region": "ap-tokyo-1",
        /* OR */
        "endpoint": "https://<namespace>.compat.objectstorage.<region>.oraclecloud.com"
      }
    }
  }

Example usage
-------------

- :doc:`AWS S3 v2 <aws>`

.. code-block::

  {
    "selector": "html", // Any resource
    "cloudStorage": [{
      "service": "oci",
      "bucket": "nodejs-001",
      "credential": {/* Authentication */},
      "admin": {
        /* Same as AWS */
        "configBucket": {/* Except "policy" | "website" | "cors" | "lifecycle" | "retentionPolicy" */}
      },
      "upload": {/* Same as AWS - Except "tags" */},
      "download": {/* Same as AWS */}
    }]
  }

.. attention:: OCI does not permit creating new *public* buckets through the :doc:`S3 <aws>` [#S3]_ compatibility layer.

Database
========

- https://www.oracle.com/autonomous-database/autonomous-json-database

.. important:: :any:`Thick mode <db-oracle-thick-mode>` environment variables are shared with :doc:`@pi/oracle <../db/oracle>`.

Interface
---------

.. code-block:: typescript

  import type { CloudDatabase } from "./interface";
  import type { BindParameters, ConnectionAttributes, ExecuteOptions, InitialiseOptions } from "oracledb";

  interface OCIDatabaseQuery extends CloudDatabase {
      source: "cloud";
      service: "oci";
      credential: string | OCIDatabaseCredential;
      table?: string;
      query?: string | Record<string, any>;
      options?: ExecuteOptions;
      params?: BindParameters;
      update?: Record<string, any>;
      streamRow?: boolean;
  }

  interface OCIDatabaseCredential extends ConnectionAttributes, InitialiseOptions {/* Empty */}

Authentication
--------------

- `Connection <https://node-oracledb.readthedocs.io/en/latest/user_guide/connection_handling.html#connection-strings>`_

.. code-block::

  {
    "dataSource": {
      "credential": "main", // squared.cloud.json
      /* OR */
      "credential": {
        "user": "nodejs",
        "password": "**********",
        "walletLocation": "/home/user/oracle/wallet", // Optional
        "walletPassword": "**********",
        "connectString": "tcps://adb.ap-tokyo-1.oraclecloud.com:1522/abcdefghijklmno_nodejs_high.adb.oraclecloud.com"
      },
      /* OR */
      "credential": {
        "connectString": "nodejs_high",
        "configDir": "/opt/oracle/config", // Location of user tnsnames.ora
        "libDir": "/opt/oracle/instantclient_19_11" // Not recommended
      }
    }
  }

.. warning:: **libDir** is ignored without ``NODE_ORACLEDB_DRIVER_MODE = "thick"``. See :doc:`@pi-r/oracle <../db/oracle>`.

Example usage
-------------

- `SODA Client API <https://node-oracledb.readthedocs.io/en/latest/api_manual/sodacollection.html>`_
- `Query <https://node-oracledb.readthedocs.io/en/latest/user_guide/sql_execution.html>`_
- `Filter <https://docs.oracle.com/en/database/oracle/simple-oracle-document-access/adsdi/soda-filter-specifications-reference.html>`_

.. tip:: SELECT queries are compatible with the :doc:`@pi-r/oracle <../db/oracle>` plugin.

.. code-block::

  {
    "selector": "h1",
    "type": "text",
    "dataSource": {
      "source": "cloud",
      "service": "oci",
      "credential": {/* Authentication */},

      "table": "demo",
      /* AND */
      "id": "1", // SODA.key
      /* OR */
      "query": { "id": { "$eq": "1" } },  // SODA.filter

      "query": "SELECT * FROM demo WHERE id = :id AND value = :value", // oracledb.execute
      "params": [1, "escaped"],
      "options": {/* ExecuteOptions */},
      /* OR */
      "query": "SELECT d.* from demo NESTED json_document COLUMNS(id, title, description) d WHERE d.id = :id", // SODA.execute (required - "thick" mode)
      "params": [1],
      "options": {/* ExecuteOptions */},

      "value": "<b>${title}</b>: ${description}", // See "/document/data.html"

      "update": {/* Record<string, any> */}, // SODA.replaceOne
      "id": "1" // Same as item being retrieved
    }
  }

.. note:: Column names might be UPPERCASED when using the **query** syntax.

@pi-r/oci
=========

.. versionadded:: 0.7.0

  - **configBucket.tags** using *PutBucketTaggingRequest* was implemented.

.. deprecated:: 0.6.2

  - *OCIDatabaseCredential* property **username** is a duplicate of **user** will be removed in **0.7.0**.

.. [#s3] https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/s3compatibleapi.htm