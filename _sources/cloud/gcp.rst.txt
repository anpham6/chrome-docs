=====================
Google Cloud Platform
=====================

- **npm** i *@pi-r/gcp*

.. tip:: The alias :target:`gcloud` can be used in place of "*gcp*" for the **service** property.

Storage
=======

- https://cloud.google.com/storage
- https://firebase.google.com/products/storage

.. note:: **npm** i *firebase* && **npm** i *firebase-admin* (optional)

Interface
---------

.. code-block:: typescript

  import type { StorageOptions } from "@google-cloud/storage";
  import type { FirebaseOptions } from "@firebase/app";
  import type { ServiceAccount } from "firebase-admin/app";

  interface GCPStorage extends CloudStorage {
      service: "gcp" | "gcloud";
      credential: string | GCPStorageCredential;
      bucket: string;
  }

  interface GCPStorageCredential extends StorageOptions, FirebaseOptions {
      product?: "firebase";
      admin?: boolean | string | ServiceAccount;
  }

API
^^^
.. code-block:: typescript

  type Document = Record<string, any>;
  type Metadata = Record<string, any>;

Authentication
--------------

- `Credentials <https://cloud.google.com/docs/authentication/client-libraries>`_

.. code-block:: javascript
  :caption: using process.env

  GOOGLE_APPLICATION_CREDENTIALS = "";

::

  {
    "dataSource": {
      "credential": "main", // squared.cloud.json
      /* OR */
      "credential": {
        "keyFilename": "./gcp.json", // Path to JSON credentials
        "projectId": "nodejs"
      },
      /* OR */
      "credential": {
        "projectId": "nodejs",
        "credentials": {
          "client_email": "**********",
          "private_key": "**********",
          "type": "service_account", // Optional
          "project_id": "nodejs"
        }
      },
      /* OR */
      "credential": {
        "projectId": "nodejs", // When using GOOGLE_APPLICATION_CREDENTIALS
        "scopes": "https://www.googleapis.com/auth/cloud-platform" // Optional
      },
      /* OR */
      "credential": {
        "projectId": "nodejs",
        "apiKey": "**********",
        "authDomain": "<project-id>.firebaseapp.com",
        /* OR */
        "product": "firebase" // When using GOOGLE_APPLICATION_CREDENTIALS
      }
    }
  }

Example usage
-------------

- `Storage Client API <https://googleapis.dev/nodejs/storage/latest>`_
- `Firebase Client API <https://firebase.google.com/docs/reference/node/firebase.storage>`_
- `Class ACL <https://cloud.google.com/nodejs/docs/reference/storage/latest/storage/acl>`_

::

  {
    "selector": "html", // Any resource
    "cloudStorage": [{
      "service": "gcp",
      "bucket": "nodejs-001",
      "credential": {/* Authentication */},
      "admin": {
        "publicRead": true, // New buckets only
        /* OR */
        "acl": "private", // See "policy"

        "emptyBucket": { // gcp.(deleteFiles | getFiles){GetFilesOptions}
          "recursive": true // Optional
        },
        "configBucket": {
          "policy": { // MakeBucketPrivateOptions
            "acl": "private", // makePrivate + includeFiles + projectPrivate
            "acl": "projectPrivate", // makePrivate + allUsers (delete) + allAuthenticatedUsers (delete)
            "acl": "authenticatedRead", // projectPrivate + allAuthenticatedUsers:READER
            "acl": "publicRead", // makePublic + includeFiles
            "acl": "publicReadWrite", // publicRead + allUsers:WRITER
            "acl": [{ "entity": "allUsers", "role": "READER" } /* add */, { "entity": "allAuthenticatedUsers" } /* delete */], // Custom

            /* Unofficial aliases - gcp.setMetadata{iamConfiguration} */
            "acl": "bucketAccessUniform", // Enable uniform bucket-level access
            "acl": "bucketAccessACL" // Revert uniform bucket-level access (within 90 days)
          },
          "tags": { // gcp.setMetadata{labels}
            "key_1": "value",
            "key_2": "value"
          },
          "tags": {}, // gcp.setMetadata{labels=null}
          "website": { // gcp.setMetadata{website}
            "indexPage": "index.html", // mainPageSuffix
            "errorPage": "404.html" // notFoundPage
          },
          /* During call to "upload" */
          "create": { // gcp.createBucket{CreateBucketRequest}
            "location": "ASIA",
            "storageClass": "STANDARD" // "NEARLINE" | "COLDLINE" | "ARCHIVE"
          },
          "lifecycle": [/* LifecycleRule */], // gcp.addLifecycleRule
          "lifecycle": [/* LifecycleRule */, false], // options.append = false
          "lifecycle": [], // Delete all rules
          "cors": [/* Cors */], // gcp.setCorsConfiguration
          "cors": [], // Delete all rules
          "retentionPolicy": 0, // gcp.removeRetentionPeriod
          "retentionPolicy": 86400 // gcp.setRetentionPeriod (seconds)
        }
      },
      "upload": {
        "publicRead": true, // Will not clobber existing ACLs
        "publicRead": 0, // Remove ACL without affecting other ACLs
        /* OR */
        "acl": "authenticatedRead", // "bucketOwnerFullControl" | "bucketOwnerRead" | "private" | "projectPrivate" | "publicRead"

        /* gcp.save */
        "options": { // UploadOptions
          "contentType": "text/html",
          "predefinedAcl": "publicRead", // Supplementary are public
          "metadata": {/* Metadata */} // All objects except when "metadata" is defined
        },

        /* gcp.uploadFileInChunks{chunkSizeBytes} */
        "chunkSize": "8mb", // Aligned to 1mb
        "chunkLimit": 5, // Same as "concurrencyLimit"
        "options": {
          "contentType": "image/png",
          "metadata": {/* Metadata */},
          /* UploadFileInChunksOptions - shared */
          "headers": {
            "Authorization": "",
            "x-goog-user-project": ""
          },
          "maxQueueSize": 5,
          "concurrencyLimit": 5
        },

        /* firebase.uploadBytes */
        "options": { // UploadMetadata
          "contentType": "text/html",
          "customMetadata": {/* Metadata */} // All objects except when "metadata" is defined
        },

        /* Primary object only */
        "metadata": {
          "key": "value",
          "key_delete": null
        }
      },
      "download": {
        /* gcp.createReadStream */
        "chunkSize": "", // Empty
        "chunkLimit": 1, // Will only stream when value is 1

        /* gcp.downloadFileInChunks{chunkSizeBytes} */
        "chunkSize": "32mb", // Aligned to 1mb
        "chunkLimit": 5, // Same as "concurrencyLimit"
        "options": {
          "concurrencyLimit": 5
        }
        /* Same as interface - gcp.download + firebase.getDownloadURL */
      }
    }]
  }

.. attention:: *Firebase* does not support any bucket operations except ``emptyBucket`` and ``metadata``.

Database
========

Interface
---------

.. code-block:: typescript

  import type { GoogleAuthOptions } from "google-auth-library";
  import type { AggregateSpec } from "@google-cloud/firestore";
  import type { PathType } from "@google-cloud/datastore";
  import type { entity } from "@google-cloud/datastore/build/src/entity";

  interface GCPDatabaseQuery extends CloudDatabase {
      source: "cloud";
      service: "gcp" | "gcloud";
      credential: string | GCPDatabaseCredential;
      product?: "firestore" | "bigquery" | "bigtable" | "datastore" | "spanner" | "firebase";
      id?: string | string[] | number;
      params?: string | unknown[] | Document;
      database?: string;
      updateType?: 0 | 1 | 2 | 3;
      columns?: string[];
      keys?: DatastoreKey | DatastoreKey[];
      kind?: string | string[];
      orderBy?: unknown[][];
      aggregateSpec?: AggregateSpec;
      flags?: number;
  }

  interface GCPDatabaseCredential extends GoogleAuthOptions {/* Empty */}

  type DatastoreKey = string | PathType[] | entity.KeyOptions;
  type Document = Record<string, any>;

Authentication
--------------

::

  {
    "dataSource": {
      "credential": "main", // squared.cloud.json
      /* OR */
      "credential": {/* Same as Storage */},
      /* OR */
      "credential": {
        "projectId": "nodejs",
        "apiKey": "**********",
        "authDomain": "<project-id>.firebaseapp.com",
        "databaseURL": "https://<database-name>.firebaseio.com" // Required
      }
    }
  }

Example usage
-------------

Firestore
^^^^^^^^^

- https://cloud.google.com/firestore
- `Client API <https://googleapis.dev/nodejs/firestore/latest>`__

::

  {
    "selector": "h1",
    "type": "text",
    "dataSource": {
      "source": "cloud",
      "service": "gcp",
      "product": "firestore",
      "credential": {/* Authentication */},
      "table": "demo",

      /* a = fs.collection(table) | b = fs.collectionGroup(table){flags & 1} */
      "id": "8Qnt83DSNW0eNykpuzcQ", // a.doc
      /* OR */
      "id": ["8Qnt83DSNW0eNykpuzcQ", "aahiEBE4qHM73JE7jom3"], // fs.getAll (table/id)
      "options": {/* ReadOptions */},
      /* OR */
      "params": ["column", "column.sub"], // a.findNearest
      "query": [1, 2],
      "options": {
        "limit": 1000, // Optional
        "distanceMeasure": "EUCLIDEAN"
      },
      /* OR */
      "options": { // a.findNearest{VectorQueryOptions} (not cached)
        "vectorField": "column",
        "queryVector": [1, 2],
        "limit": 1000, // Optional
        "distanceMeasure": "EUCLIDEAN"
      },
      /* OR */
      "query": [
        ["where", "group", "==", "Firestore"],
        ["where", "id", "==", "8Qnt83DSNW0eNykpuzcQ"],
        ["findNearest", "column", [1, 2], { "limit": 1000, "distanceMeasure": "EUCLIDEAN" }],
        ["limitToLast", 2],
        ["orderBy", "title", "asc"]
      ],
      "query": [
        ["whereAnd", // Unofficial
          ["group", "==", "Firestore"],
          ["id", "==", "8Qnt83DSNW0eNykpuzcQ"]
        ],
        ["limitToLast", 2]
      ],
      "query": [
        ["whereOr", // Unofficial
          ["id", "==", "8Qnt83DSNW0eNykpuzcQ"],
          ["id", "==", "aahiEBE4qHM73JE7jom3"]
        ],
        ["orderBy", "title", "asc"]
      ],
      "orderBy": [
        ["title", "asc"]
      ],
      "id": 1, // b.getPartitions(id){number}
      /* OR */
      "aggregateSpec": {/* AggregateSpec */}, // (a | b).aggregate (not cached)

      "updateType": 0, // 0 - update{exists} | 1 - create | 2 - set | 3 - set{merge}
      "update": {/* Document */}, // fs.update
      "update": {
        "key1": "__delete__", // FieldValue.delete()
        "key2": "__increment__", // FieldValue.increment(1)
        "key2": "__increment<number>__", // FieldValue.increment(number)
        "key3": "__serverTimestamp__", // FieldValue.serverTimestamp()
        "key4": "__vector<1, 2, 3>__", // FieldValue.vector([1, 2, 3])
        "key4": "__arrayUnion<a, b, c>__", // FieldValue.arrayUnion("a", "b", "c")
        "key4": "__arrayRemove<1, [2\\, 3\\, 4], 5>__" // FieldValue.arrayRemove(1, [2, 3, 4], 5)
      },
      "id": "8Qnt83DSNW0eNykpuzcQ" // Same as item being retrieved
    }
  }

.. hlist::
  :columns: 4

  - endAt
  - endBefore
  - limit
  - limitToLast
  - offset
  - orderBy
  - select
  - startAfter
  - startAt
  - where
  - **whereAnd**
  - **whereOr**
  - withConverter

BigQuery
^^^^^^^^

- https://cloud.google.com/bigquery
- `Client API <https://googleapis.dev/nodejs/bigquery/latest>`__

.. note:: **npm** i *@google-cloud/bigquery*

::

  {
    "selector": "h1",
    "type": "text",
    "dataSource": {
      "source": "cloud",
      "service": "gcp",
      "product": "bigquery",
      "credential": {/* Authentication */},

      "database": "nodejs", // Dataset (optional)
      "table": "demo", // Destination table (optional)

      "query": "SELECT name, count FROM `demo.names_2014` WHERE gender = 'M' ORDER BY count DESC LIMIT 10", // bq.getQueryResults

      "params": { "name": "value" },
      "params": ["arg0" /* ? */, "arg1" /* ? */],
      "options": {/* IQuery */},

      "update": "SELECT name, state FROM `bigquery-public-data.usa_names.usa_1910_current` LIMIT 10" // "database" | "database" + "table" (bq.setMetadata)
    }
  }

Datastore
^^^^^^^^^

- https://cloud.google.com/datastore
- `Client API <https://googleapis.dev/nodejs/datastore/latest>`__

.. note:: **npm** i *@google-cloud/datastore*

::

  {
    "selector": "h1",
    "type": "text",
    "dataSource": {
      "source": "cloud",
      "service": "gcp",
      "product": "datastore",
      "credential": {/* Authentication */},

      "keys": "task", // ds.get
      "keys": ["task", "sampletask1"], // PathType[]
      "keys": { // KeyOptions
        "namespace": "nodejs",
        "path": ["task", "sampletask3"]
      },
      "keys": ["task", ["task", "sampletask2"]],
      /* OR */
      "name": "<namespace>", // With "kind" (optional)
      "kind": "Task", // ds.runQuery (at least one parameter)
      "kind": ["Task1", "Task2"],
      "query": [
        ["filter", "done", "=", false],
        ["filter", "priority", ">=", 4],
        ["order", "priority", { "descending": true }]
      ],
      "options": {/* RunQueryOptions */},

      "update": {/* Document */}, // ds.save
      "keys": "task", // Same as item being retrieved
      /* OR */
      "kind": "Task",
      "query": [/* Same */]
    }
  }

.. hlist::
  :columns: 4

  - end
  - filter
  - groupBy
  - hasAncestor
  - limit
  - offset
  - order
  - select
  - start

Bigtable
^^^^^^^^

- https://cloud.google.com/bigtable
- `Client API <https://googleapis.dev/nodejs/bigtable/latest>`__

.. note:: **npm** i *@google-cloud/bigtable*

::

  {
    "selector": "h1",
    "type": "text",
    "dataSource": {
      "source": "cloud",
      "service": "gcp",
      "product": "bigtable",
      "credential": {/* Authentication */},
      "name": "nodejs", // Instance
      "table": "demo",

      "id": "rowKey1", // bt.get
      "columns": ["column1", "column2"],
      /* OR */
      "id": "<empty>", // bt.createReadStream

      "query": {/* Filter */}, // Overrides "filter" in GetRowOptions
      "options": {/* GetRowOptions */},

      "update": {/* Document */}, // bt.save
      "id": "rowKey1" // Same as item being retrieved
    }
  }

Spanner
^^^^^^^

- https://cloud.google.com/spanner
- `Client API <https://googleapis.dev/nodejs/spanner/latest>`__

.. note:: **npm** i *@google-cloud/spanner*

::

  {
    "selector": "h1",
    "type": "text",
    "dataSource": {
      "source": "cloud",
      "service": "gcp",
      "product": "spanner",
      "credential": {/* Authentication */},
      "name": "nodejs", // Instance

      "database": "sample", // Required
      "options": {
        "databasePool": {/* session-pool.SessionPoolOptions */},
        "databaseQuery": {/* protos.IQueryOptions */}
      },

      "table": "demo", // sp.table.read
      "columns": ["col1", "col2"], // Overrides "columns" in ReadRequest
      "query": { // ReadRequest
        "columns": [],
        "keys": []
      },
      "options": {
        "tableRead": {/* TimestampBounds */}
      },
      /* OR */
      "table": "<empty>", // sp.run
      "flags": 2, // sp.runStream
      "query": "SELECT 1", // DML
      "query": { // ExecuteSqlRequest
        "sql": "SELECT 1",
        "params": { "p1": 0, "p2": 1 },
        "types": {
          "p1": "numeric" // date | float | float32 | int | protoEnum | protoMessage | struct | pgJsonb | pgNumeric | timestamp
        }
      },

      "table": "demo", // sp.table.update
      "update": {/* Document */},
      "updateType": 0, // 0 - update | 1 - insert | 2 - replace
      "options": {
        "tableUpdate": {/* UpdateRowsOptions */}
      },
      /* OR */
      "table": "<empty>", // sp.runUpdate
      "update": "SELECT 1",
      "update": { "sql": "SELECT 1", "params": { "p1": 0, "p2": 1 } }
    }
  }

Realtime Database
^^^^^^^^^^^^^^^^^

- https://firebase.google.com/products/realtime-database
- `Client API <https://firebase.google.com/docs/reference/js/database.md#database_package>`__

.. note:: **npm** i *firebase* && **npm** i *firebase-admin* (optional)

::

  {
    "selector": "h1",
    "type": "text",
    "dataSource": {
      "source": "cloud",
      "service": "gcp",
      "product": "firebase",
      "credential": {/* Authentication */},

      "query": "path/to/ref", // rd.child
      /* OR */
      "query": "path/to/ref", // rd.query
      "orderBy": [
        ["orderByChild", "path/to/child"],
        ["startAfter", 5, "name"],
        ["limitToFirst", 1]
      ],

      "update": {/* Document */}, // rd.update
      "query": "path/to/ref" // Same as item being retrieved (rd.child)
    }
  }

.. hlist::
  :columns: 4

  - endBefore
  - endAt
  - equalTo
  - limitToFirst
  - limitToLast
  - orderByChild
  - orderByKey
  - orderByPriority
  - orderByValue
  - startAt
  - startAfter

@pi-r/gcp
=========

.. versionadded:: 0.11.0

  - *GCPStorage* properties **upload** | **download** extended :target:`CopyObjectAction` as :alt:`copyObject | copyObject[]`.

.. versionadded:: 0.10.1

  - *Spanner* method **runStream** for SQL requests was implemented.  

.. versionchanged:: 0.10.0

  - *GCPStorage* property **admin.configBucket.retentionPolicy** as `0` calls the method :target:`removeRetentionPeriod`.
  - *Firebase Admin* authentication using a path to a JSON file or an object representing a service account key is supported.
  - *Firestore* aggregate and collection group partition queries are supported. 
  - *Firestore* method **findNearest** for vector queries as :alt:`VectorQueryOptions` was implemented.

.. versionadded:: 0.9.0

  - *GCPStorage* property **emptyBucket** for directory listing as :alt:`GetListOptions` was implemented.

.. versionadded:: 0.8.0

  - *GCPStorage* action **download** using **createReadStream** with :alt:`chunkLimit` was implemented.
  - *Firestore* method **findNearest** as a *VectorQuery* and *Query* is supported.
  - *Firestore* property **update** supports using *FieldValue<"vector" | "arrayUnion" | "arrayRemove">* methods.

.. versionadded:: 0.7.1

  - *Firestore* methods **where** | **orderBy** | **select** supports using *FieldPath* params.

.. versionadded:: 0.7.0

  - **CLOUD_UPLOAD_STREAM** attribute in *ICloudServiceClient* was enabled.
  - **CLOUD_UPLOAD_CHUNK** attribute in *ICloudServiceClient* was enabled.
  - **CLOUD_DOWNLOAD_CHUNK** attribute in *ICloudServiceClient* was enabled.
  - **chunkSize** | **chunkLimit** in *CloudStorageUpload* were implemented.
  - **chunkSize** | **chunkLimit** in *CloudStorageDownload* were implemented.
  - *GCPStorage* **configBucket.tags** using *Metadata* was implemented.
  - *GCPStorage* **configBucket.cors** using *Cors* was implemented.
  - *GCPStorage* **configBucket.lifecycle** using *LifecycleRule* was implemented.
  - *Firestore* property **update** supports using *FieldValue<"delete" | "increment" | "serverTimestamp">* methods.
  - *Firestore* property **update** supports using property **updateType** enum values.

.. versionremoved:: 0.7.0

  - *GCPStorageCredential* no longer extends **CreateBucketRequest**.

.. versionadded:: 0.6.3

  - *Firestore* property **id** supports multiple document references.
  - *Firestore* property **query** supports using *Filter<"and" | "or">* conditional groups for *where*.

.. versionadded:: 0.6.2

  - *GoogleAuthOptions* properties **authClient** and **credentials** were not detected during credential validation.
  - *Datastore* method **createQuery** with :target:`namespace` and :target:`kind` parameter is supported.