=========
Interface
=========

.. code-block:: typescript

  import type { DeleteObjectsOptions } from "../types/cloud";

  interface DataSource {
      source: string;
      uri?: string;
      index?: number;
      limit?: number;
      query?: unknown;
      postQuery?: string | (...args: unknown[]) => unknown;
      preRender?: string | (...args: unknown[]) => unknown;
      whenEmpty?: string | (...args: unknown[]) => unknown;
      removeEmpty?: boolean;
      ignoreCache?: boolean | number | number[];
      transactionState?: number;
      transactionFail?: boolean;
  }

  interface DbDataSource extends DataSource {
      name?: string;
      table?: string;
      credential?: string | unknown;
      options?: unknown;
      update?: unknown;
      flat?: number;
      willAbort?: boolean;
      streamRow?: boolean | string | ((row: unknown) => Error | false | void) | null;
  }

  interface CloudDatabase extends DbDataSource {
      source: "cloud";
      service: string;
      id?: string;
      params?: unknown;
  }

.. code-block:: typescript

  import type { CopyObjectAction } from "../types/cloud";

  interface CloudStorage {
      service: string;
      credential: unknown;
      bucket?: string;
      admin?: CloudStorageAdmin;
      upload?: CloudStorageUpload;
      download?: CloudStorageDownload;
  }

  interface CloudStorageAdmin extends CloudStorageACL {
      emptyBucket?: DeleteObjectsOptions | boolean;
      configBucket?: {
          create?: unknown;
          policy?: unknown;
          website?: {
              indexPage?: string;
              errorPage?: string;
              indexPath?: string;
              errorPath?: string;
          };
          retentionPolicy?: unknown;
      };
      /** @deprecated */
      recursive?: boolean;
      preservePath?: boolean;
  }

  interface CloudStorageAction {
      pathname?: string;
      filename?: string;
      minStreamSize?: number | string;
      chunkSize?: number | string;
      chunkLimit?: number;
      flags?: number;
      active?: boolean;
      overwrite?: boolean;
      admin?: CloudStorageAdmin;
  }

  interface CloudStorageUpload extends CloudStorageACL, CloudStorageAction, CopyObjectAction {
      buffer?: Buffer | null;
      contentType?: string;
      metadata?: Record<string, string>;
      tags?: Record<string, string> | false;
      options?: unknown;
      fileGroup?: [Buffer | string, string, string?][];
      localStorage?: boolean;
      endpoint?: string;
      all?: boolean;
  }

  interface CloudStorageACL {
      publicRead?: boolean | 0;
      acl?: string;
  }

  interface CloudStorageDownload extends CloudStorageAction, CopyObjectAction {
      keyname?: string;
      versionId?: string;
      options?: unknown;
      deleteObject?: unknown;
      waitStatus?: boolean;
  }

Changelog
=========

.. versionadded:: 0.13.0

  - *CloudStorageUpload* property **copyObject | copyObject[]** for alternate bucket location was implemented.
  - *CloudStorageDownload* property **copyObject | copyObject[]** for emulating move/rename and delete semantics was implemented.

.. versionadded:: 0.11.0

  - *CloudStorageAdmin* property **emptyBucket** for directory listing with :alt:`DeleteObjectsOptions` was amended.

.. deprecated:: 0.11.0

  - *CloudStorageAdmin* property **recursive** for directory traversal was replaced with :target:`emptyBucket` as :alt:`DeleteObjectsOptions`.

.. versionadded:: 0.9.0

  - *CloudStorageAction* property **chunkSize** | **chunkLimit** for parallel multipart operations were created.
  - *CloudStorageDownload* property **options** for the provider client was created.
  - *CloudStorageDownload* property **keyname** for file to be downloaded and subsequently renamed to **filename**.

Shared properties
=================

Storage
-------

::

  {
    "cloudStorage": [{
      "service": "aws", // Built-in alias | NPM package name
      "bucket": "nodejs-001",
      "credential": {/* service-interface */}

      "admin": {
        "publicRead": true, // Public access (before upload #3)
        /* OR */
        "acl": "service-value", // ACL access permissions

        "emptyBucket": true, // Delete all objects (before upload #1)
        "recursive": false, // Default is "true" (emptyBucket)
        /* OR */
        "emptyBucket": {
          /* service-interface */
          "recursive": true // Optional
        },

        "configBucket": {
          "create": {/* service-interface */}, // New bucket (before upload #2)
          "retentionPolicy": {/* service-interface */}, // Bucket initialization (before upload #4)
          "policy": {/* service-interface */}, // Modify policy (after upload)

          "website": { // Main HTML page only
             "indexPage": "index.html", // Usage varies by service
             "errorPage": "404.html",
             "indexPath": "home.html",
             "errorPath": "errors/404.html"
          }
        }
      },
      "upload": {
        "active": false, // Will not overwrite ACL
        "active": true, // Rewrites "src" to storage location + Will overwrite ACL (public-read)
        "localStorage": false, // Remove current file from archive or local disk

        "all": true, // Include descendants + transforms + torrents

        "pathname": "2024", // nodejs-001/2024/picture.png
        "filename": "picture.png", // Choose a different filename for bucket
        "overwrite": false, // If exists then picture_{1,2,3}.png
        /* OR */
        "overwrite": true, // Always use current filename

        "contentType": "image/png", // Metadata has higher precedence (default is "application/octet-stream")

        "minStreamSize": 0, // Always use readable stream
        "minStreamSize": "512mb", // Detect when to use readable stream (not limited to 2gb)
        "minStreamSize": -1, // Prefer transfer by Buffer (small files)

        "chunkSize": "8mb", // Part size of a parallel upload operation
        "chunkLimit": 4, // Concurrent parts uploading

        "endpoint": "http://hostname/nodejs-001", // Required when different from credential

        "copyObject": [{
          "bucket": "nodejs-002", // nodejs-002/2024/picture.png (required)
          /* OR */
          "filename": "001.png", // nodejs-002/2024/001.png
          /* OR */
          "pathname": "images", // nodejs-002/images/001.png
          "filename": "001.png",
          /* OR */
          "pathname": "", // nodejs-002/001.png (override "2024")
          "filename": "001.png",

          "options": {/* service-interface */}
        }]
      },
      "download": {
        "filename": "alternate.png", // Required
        "versionId": "12345", // Retrieve a previous file snapshot

        "chunkSize": "32mb", // Part size of a parallel download operation
        "chunkSize": 33554432, // 32 * 1024 * 1024
        "chunkLimit": 4, // Concurrent parts downloading

        "active": false,
        "overwrite": false, // If local file exists then skip download
        /* OR */
        "active": true, // Always write file or replace local file when same extension

        "waitStatus": true, // Delay build until file is completely downloaded

        "pathname": "download/images", // Relative only (base directory/pathname)
        /* OR */
        "preservePath": false, // Use base directory
        "preservePath": true, // Use asset directory

        "keyname": "", // bucket/alternate.png to download/images/alternate.png
        "keyname": "picture.png", // bucket/picture.png to download/images/alternate.png

        "deleteObject": true, // Delete from bucket after successful download
        "deleteObject": {/* service-interface */},

        "copyObject": [{/* same as upload */}]
      }
    }]
  }

.. tip:: Any properties in **admin.configBucket.website** set to ``true`` uses the upload *HTML* page element.

Database
--------

::

  {
    "dataSource": { // DbDataSource
      "source": "cloud",
      "service": "aws", // Built-in alias | NPM package name
      "credential": {/* service-interface */},

      // Excluding "parallel" | "withCommand" | "usePool"
    }
  }

Admin
=====

Auth
----

Internal use of these libraries that do not require credentials validation during service client API initialization can disable this behavior through settings. There are also cases where an unsupported authorization scheme is necessary which has not been implemented.

.. caution:: These are global settings and affect every connection per service.

.. code-block::
  :caption: squared.cloud.json

  {
    "settings": {
      "aws": {
        "auth": {
          "storage": true, // Default behavior
          "database": false // Explicit to disable
        }
      }
    }
  }

Storage
-------

.. rst-class:: cloud-service

=========== =================== ================== ====================
Service     CLOUD_UPLOAD_STREAM CLOUD_UPLOAD_CHUNK CLOUD_DOWNLOAD_CHUNK
=========== =================== ================== ====================
aws                  X                  X                  
aws-v3               X                  X                  
azure                X                  X                   X
gcp                  X                  X                   X
ibm                  X                  X                  
minio                X
oci                  X                  X                  
=========== =================== ================== ====================

.. caution:: Setting :code:`process.env.EMC_CLOUD_UPLOAD_BUFFER = "true"` will enable the legacy behavior for :doc:`Document </document/index>` based uploads.

Stream
^^^^^^

Streaming was enabled by default due to its lower memory usage requirements. It is slower for small file transfers which is typical for a static web page.

.. tip:: Setting :code:`upload.minStreamSize = -1` will disable streaming for the current request.

.. code-block:: javascript
  :caption: Buffer

  const aws = require("@pi-r/aws");
  aws.CLOUD_UPLOAD_STREAM = false;

.. warning:: Reading a buffer from disk has **2gb** file size limit.

Chunk
^^^^^

Parallel transfers were enabled by default to accommodate large files. The old behavior is used when **chunkSize** is empty and will open one request per file.

.. code-block:: javascript
  :caption: Sequential

  const azure = require("@pi-r/azure");
  azure.CLOUD_UPLOAD_CHUNK = false;
  azure.CLOUD_DOWNLOAD_CHUNK = false;

.. note:: Chunking is only active when the upload file size is greater than **chunkSize**.