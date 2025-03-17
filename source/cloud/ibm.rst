=========
IBM Cloud
=========

- **npm** i *@pi-r/ibm*

.. warning:: Maintenence officially ended with the ``pi-r 0.8.3`` release on **October 12, 2024**. This product is no longer part of the reference implementation.

Storage
=======

- https://www.ibm.com/products/cloud-object-storage

.. note:: Uses :doc:`S3 <aws>` [#]_ compatibility API :lower:`(AWS v2)` and signature **iam**.

Interface
---------

.. code-block:: typescript

  import type { ConfigurationOptions } from "ibm-cos-sdk/lib/config-base";

  interface IBMStorage extends CloudStorage {
      service: "ibm"
      credential: string | IBMStorageCredential;
      bucket: string;
  }

  interface IBMStorageCredential extends ConfigurationOptions {
      apiKeyId: string;
      serviceInstanceId: string;
      region: string;
      endpoint?: string;
  }

Authentication
--------------

- `Credentials <https://cloud.ibm.com/docs/cloud-object-storage?topic=cloud-object-storage-service-credentials>`_

::

  {
    "dataSource": {
      "credential": "main", // squared.cloud.json
      /* OR */
      "credential": {
        "apiKeyId": "**********",
        "serviceInstanceId": "**********",
        "region": "jp-tok",
        /* OR */
        "endpoint": "https://s3.<region>.cloud-object-storage.appdomain.cloud"
      }
    }
  }

Example usage
-------------

- https://cloud.ibm.com/apidocs/cos/cos-compatibility?code=node
- :doc:`AWS S3 v2 <aws>`

::

  {
    "selector": "html", // Any resource
    "cloudStorage": [{
      "service": "ibm",
      "bucket": "nodejs-001",
      "credential": {/* Authentication */},
      "admin": {
        /* Same as AWS */
        "configBucket": {/* Except "policy{putBucketPolicy}" | "tags" | "retentionPolicy" */}
      },
      "upload": {/* Same as AWS */},
      "download": {/* Same as AWS */}
    }]
  }

Database
========

- https://cloud.ibm.com/docs/Cloudant?topic=Cloudant-databases

Interface
---------

.. code-block:: typescript

  import type { PostAll, PostFind, PostSearch, PostView } from "@pi-r/ibm/types";

  import type { UserOptions } from "ibm-cloud-sdk-core";
  import type { PostDocumentParams } from "@ibm-cloud/cloudant/cloudant/v1";
  import type { Options as BearerTokenOptions } from "ibm-cloud-sdk-core/auth/authenticators/bearer-token-authenticator";
  import type { Options as ContainerOptions } from "ibm-cloud-sdk-core/auth/authenticators/container-authenticator";
  import type { Options as IamOptions } from "ibm-cloud-sdk-core/auth/authenticators/iam-authenticator";
  import type { Options as VpcOptions } from "ibm-cloud-sdk-core/auth/authenticators/vpc-instance-authenticator";

  interface IBMDatabaseQuery extends CloudDatabase {
      source: "cloud";
      service: "ibm";
      credential: string | IBMDatabaseCredential;
      query?: PostFind | PostSearch | PostView;
      update?: PostDocumentParams;
      params?: PostDocumentParams | PostAll;
      partitionKey?: string;
  }

  interface IBMDatabaseCredential extends AuthValue, UserOptions, Partial<IamOptions>, ContainerOptions, VpcOptions, BearerTokenOptions {
      authType?: "basic" | "iam" | "bearertoken" | "container" | "vpc" | "mcsp" | "cp4d" | "couchdb";
      authUrl?: string;
  }

Authentication
--------------

- `Connection <https://github.com/IBM/node-sdk-core/blob/main/Authentication.md>`_

::

  {
    "dataSource": {
      "credential": "main", // squared.cloud.json
      /* OR */
      "credential": {
        "url": "https://<username>.cloudantnosqldb.appdomain.cloud" // Required (except with "authUrl")

        "username": "**********", // basic
        "password": "**********",
        "serviceName": "nodejs", // Default is "CLOUDANT"
        /* OR */
        "apikey": "**********", // iam
        /* OR */
        "bearerToken": "**********", // bearertoken
        /* OR */
        "authType": "couchdb",
        "username": "**********",
        "password": "**********",
        /* OR */
        "authType": "container", // "vpc" | "mcsp" | "cp4d"
        "authUrl": "https://iam.cloud.ibm.com", // Used in place of Authenticator.url property
        "iamProfileName": "iam-user123" // All properties are identical
      }
    }
  }

Example usage
-------------

- `Cloudant Client API <https://ibm.github.io/cloudant-node-sdk/docs/latest/modules/cloudant_v1.html>`_
- `Query <https://cloud.ibm.com/apidocs/cloudant?code=node#postfind>`_

::

  {
    "selector": "h1",
    "type": "text",
    "dataSource": {
      "source": "cloud",
      "service": "oci",
      "credential": {/* Authentication */},

      /* ibm.getDocument */
      "name": "demo", // "db" property
      "id": "1", // "docId" property

      /* OR */
      "query": { // ibm.postFind
        "db": "demo", // When using "name" (optional)
        "selector": {
          "id": { "$eq": "1" }
        },
        "partitionKey": "" // ibm.postPartitionFind
      },
      "query": { // ibm.postView
        "db": "demo",
        "ddoc": "demo-doc",
        "view": "demo-view", // 
        "partitionKey": "" // ibm.postPartitionView
      },
      "query": { // ibm.postSearch
        "db": "demo",
        "ddoc": "demo-doc",
        "index": "demo-index",
        "query": "id:'1' AND title:'Bristol'", // Lucene syntax
        "partitionKey": "" // ibm.postPartitionSearch
      },
      /* OR */
      "query": { // ibm.postViewQueries
        "db": "demo",
        "ddoc": "demo-doc",
        "view": "demo-view",
        "queries": [{ "key": "1" }] // ViewQuery[]
      },

      /* When "query" undefined */

      "params": { // ibm.postAllDocs
        "db": "demo"
      },
      "params": { // ibm.postPartitionAllDocs
        "db": "demo",
        "partitionKey": "Partition1"
      },
      "params": { // ibm.postBulkGet
        "db": "demo",
        "docs": [{ "id": "1" }] // BulkGetQueryDocument[]
      },
      "params": { // ibm.postExplain
        "db": "demo",
        "selector": { // [ExplainResult]
          "year": {
            "$gt": "2024"
          }
        }
      },
      "params": { // ibm.postAllDocsQueries
        "db": "demo",
        "queries": [{ "key": "1" }] // AllDocsQuery[]
      },

      "value": "<b>${title}</b>: ${description}",

      "update": { // ibm.postDocument{PostDocumentParams}
        "document": {/* Record<string, any> */}
      },
      "id": "1" // Same as item being retrieved
    }
  }

@pi-r/ibm
=========

.. versionremoved:: 0.9.0

  - Package is no longer supported due to maintenance priorities with newer projects. [#]_

.. versionadded:: 0.8.0

  - *Cloudant* method **postExplain** as a single *ExplainResult* is supported.

.. versionchanged:: 0.8.0

  - NPM packages upgraded with a minimum :alt:`NodeJS 18` requirement:

    ======================= ====== =====
            Package           From    To
    ======================= ====== =====
    **@ibm-cloud/cloudant**    0.9  0.10
    **ibm-cloud-sdk-core**     4.3   5.0
    ======================= ====== =====

.. versionadded:: 0.7.0

  - **CLOUD_UPLOAD_STREAM** attribute in *ICloudServiceClient* was enabled.
  - **CLOUD_UPLOAD_CHUNK** attribute in *ICloudServiceClient* was enabled.
  - **configBucket.cors** using *CORSConfiguration* was implemented.
  - **configBucket.lifecycle** using *LifecycleConfiguration* was implemented.

@pi-r2/ibm
==========

.. versionadded:: 0.1.0

  - NPM: Unmaintained and untested source with :alt:`@ibm-cloud/cloudant 0.12.2` was released.

.. [#] https://cloud.ibm.com/docs/cloud-object-storage?topic=cloud-object-storage-compatibility-api
.. [#] https://github.com/anpham6/pi-r2/src/cloud/ibm