===============
Microsoft Azure
===============

- **npm** i *@pi-r/azure*

.. tip:: The alias :target:`az` can be used in place of "*azure*" for the **service** property.

Storage
=======

- https://azure.microsoft.com/en-us/free/storage

Interface
---------

.. code-block:: typescript

  interface AzureStorage extends CloudStorage {
      service: "azure" | "az";
      credential: string | AzureStorageCredential;
      bucket: string;
  }

  interface AzureStorageCredential {
      accountName?: string;
      accountKey?: string;
      connectionString?: string;
      sharedAccessSignature?: string;
  }

API
^^^

.. code-block:: typescript

  type Metadata = Record<string, string>;
  type Tags = Record<string, string>;

Authentication
--------------

- `Credentials <https://www.npmjs.com/package/@azure/storage-blob#create-the-blob-service-client>`_

.. code-block:: javascript
  :caption: using process.env

  AZURE_TENANT_ID = ""; // DefaultAzureCredential
  AZURE_CLIENT_ID = "";
  AZURE_CLIENT_SECRET = "";

::

  {
    "dataSource": {
      "credential": "main", // squared.cloud.json
      /* OR */
      "credential": {
        "accountName": "nodejs", // +1 password option (required)
        "accountKey": "**********",
        /* OR */
        "connectionString": "DefaultEndpointsProtocol=http;AccountName=nodejs;AccountKey=**********;BlobEndpoint=http://127.0.0.1:10000/nodejs;",
        /* OR */
        "sharedAccessSignature": "https://nodejs.blob.core.windows.net/bucket?...", // Full URL with SAS token
        /* OR */
        // DefaultAzureCredential from @azure/identity
      }
    }
  }

.. code-block:: javascript
  :caption: using process.env

  AZURE_STORAGE_ACCOUNT = "";
  AZURE_STORAGE_KEY = "";
  AZURE_STORAGE_CONNECTION_STRING = "";
  AZURE_STORAGE_SAS_TOKEN = "";

.. note:: |env-apply|

Example usage
-------------

- `Storage Blob Client API <https://learn.microsoft.com/en-us/javascript/api/@azure/storage-blob>`_

::

  {
    "selector": "html", // Any resource
    "cloudStorage": [{
      "service": "azure",
      "bucket": "nodejs-001",
      "credential": {/* Authentication */},
      "admin": {
        "publicRead": true, // Same as "blob" (access)
        /* OR */
        "acl": "container",

        "configBucket": {
          "website": { // azure.setProperties{staticWebsite}
            "indexPage": "index.html", // indexDocument
            "indexPath": "home.html", // defaultIndexDocumentPath
            "errorPath": "errors/404.html" // errorDocument404Path
          },
          /* During call to "upload" */
          "create": { // azure.create
            "access": "container", // Same as "acl"
            "metadata": {/* Metadata */}
          },
          "retentionPolicy": [{ // azure.setAccessPolicy
            "id": "policy1",
            "accessPolicy": {
              "expiresOn": "new Date('2025-01-01')", // Permission "coerce" required when through web service
              "permissions": "none",
              "startsOn": "new Date('2024-01-01')"
            }
          }]
        }
      },
      "upload": {
        /* Not supported */
        "publicRead": false,
        "acl": "none",

        "options": { // BlockBlobUploadOptions
          "blobHTTPHeaders": {
            "blobContentType": "text/html"
          },
          /* All objects except when "metadata" or "tags" is defined */
          "metadata": {/* Metadata */},
          "tags": {/* Tags */}
        },

        /* Primary object only */
        "metadata": {/* Metadata */},
        "tags": {/* Tags */},

        /* azure.uploadFile{maxSingleShotSize} */
        "chunkSize": "32mb", // Aligned to 1mb
        "chunkLimit": 4 // Same as "concurrency"
      },
      "download": {
        /* azure.downloadToFile */
        "chunkSize": "2gb", // Set to at least 2gb
        "versionId": "2011-03-09T01:42:34.9360000Z", // Alias for "snapshot" (optional)

        /* azure.downloadToBuffer{blockSize} */
        "chunkSize": "256mb", // Aligned to 1mb
        "chunkLimit": 4, // Same as "concurrency"
        "options": { // BlobDownloadToBufferOptions
          "concurrency": 4
        },

        "deleteObject": {/* ContainerDeleteMethodOptions */} // azure.delete
      }
    }]
  }

Database
========

- https://azure.microsoft.com/en-us/products/cosmos-db

Interface
---------

.. code-block:: typescript

  import type { CosmosClientOptions, FeedOptions, PartitionKey, PatchRequestBody, RequestOptions, SqlQuerySpec } from "@azure/cosmos";

  interface AzureDatabaseQuery extends CloudDatabase {
      source: "cloud";
      service: "azure" | "az";
      credential: string | AzureDatabaseCredential;
      name: string;
      table: string;
      query?: string | SqlQuerySpec;
      params?: unknown[];
      partitionKey?: PartitionKey;
      options?: FeedOptions | RequestOptions;
      update?: PatchRequestBody | Reord<string, unknown>;
      storedProcedureId?: string;
  }

  interface AzureDatabaseCredential extends CosmosClientOptions {
      username?: string;
      password?: string;
      tenantId?: string;
      clientId?: string;
  }

Authentication
--------------

- `Connection <https://www.npmjs.com/package/@azure/cosmos#get-account-credentials>`_
- `Azure AD <https://learn.microsoft.com/en-us/dotnet/api/azure.identity.usernamepasswordcredential.-ctor?view=azure-dotnet#azure-identity-usernamepasswordcredential-ctor(system-string-system-string-system-string-system-string)>`_

::

  {
    "dataSource": {
      "credential": "main", // squared.cloud.json
      /* OR */
      "credential": {
        "endpoint": "https://nodejs.documents.azure.com:443",
        "key": "**********"
      },
      /* OR */
      "credential": {
        "endpoint": "https://nodejs.documents.azure.com:443",
        "username": "nodejs", // Azure AD
        "password": "**********",
        "tenantId": "azure-id", // Optional with AZURE_TENANT_ID
        "clientId": "cosmos-id" // Optional with AZURE_CLIENT_ID
      }
    }
  }

.. code-block:: javascript
  :caption: using process.env

  AZURE_COSMOS_ENDPOINT = "";
  AZURE_COSMOS_KEY = "";

.. note:: |env-apply|

Example usage
-------------

- `Cosmos Client API <https://learn.microsoft.com/en-us/javascript/api/@azure/cosmos>`_
- `Query <https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/query>`_
- `JSON Patch <http://jsonpatch.com>`_

::

  {
    "selector": "h1",
    "type": "text",
    "dataSource": {
      "source": "cloud",
      "service": "azure",
      "credential": {/* Authentication */},
      "name": "nodejs", // Database name
      "table": "demo",

      "id": "1",
      "partitionKey": "Pictures", // Optional
      "partitionKey": ["Pictures", "Azure"],
      "options": {/* RequestOptions */},
      /* OR */
      "storedProcedureId": "spGetItems",
      "params": [1, "value"],
      "partitionKey": "Pictures", // Optional
      "options": {/* RequestOptions */},
      /* OR */
      "query": "SELECT * FROM c WHERE c.id = '1'", // Calls "readAll" when not defined
      "query": { // SqlQuerySpec
        "query": "SELECT * FROM c WHERE c.lastName = @lastName AND c.address.state = @addressState",
        "parameters": [
          { "name": "@lastName", "value": "Wakefield" },
          { "name": "@addressState", "value": "CA" }
        ]
      },
      "options": {/* FeedOptions */},

      "value": "<b>${title}</b>: ${description}",

      "update": {/* PatchRequestBody */}, // JSON Patch
      "id": "1", // Same as item being retrieved
      /* OR */
      "query": "SELECT * FROM c WHERE c.id = '1'",
      "update": {/* Record<string, unknown> */},
      /* WITH */
      "partitionKey": "Pictures" // Optional
    }
  }

@pi-r/azure
===========

.. versionadded:: 0.8.1

  - *CosmoDB* items method **upsert** document as :target:`Record<string, unknown>` was implemented.

.. versionadded:: 0.7.0

  - **CLOUD_UPLOAD_STREAM** attribute in *ICloudServiceClient* was enabled.
  - **CLOUD_UPLOAD_CHUNK** attribute in *ICloudServiceClient* was enabled.
  - **CLOUD_DOWNLOAD_CHUNK** attribute in *ICloudServiceClient* was enabled.
  - **chunkSize** | **chunkLimit** in *CloudStorageUpload* were implemented.
  - **chunkSize** | **chunkLimit** in *CloudStorageDownload* were implemented.

.. versionadded:: 0.6.2

  - Identity authentication with Azure AD (**aadCredentials**) was implemented.

.. |env-apply| replace:: These are not official *Azure* environment variables and require :code:`process.env.apply = true` in :target:`squared.json`.