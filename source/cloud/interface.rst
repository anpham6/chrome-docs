=========
Interface
=========

.. code-block:: typescript

  import type { DbDataSource } from "../db/interface";

  interface CloudDatabase extends Omit<DbDataSource, "parallel" | "withCommand" | "usePool"> {
      source: "cloud";
      service: string;
      id?: string;
      params?: unknown;
  }

.. code-block:: typescript
  :emphasize-lines: 31,32,57,59

  interface CloudStorage {
      service: string;
      credential: unknown;
      bucket?: string;
      admin?: CloudStorageAdmin;
      upload?: CloudStorageUpload;
      download?: CloudStorageDownload;
  }

  interface CloudStorageAdmin extends CloudStorageACL {
      emptyBucket?: boolean;
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

  interface CloudStorageUpload extends CloudStorageACL, CloudStorageAction {
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

  interface CloudStorageDownload extends CloudStorageAction {
      keyname?: string;
      versionId?: string;
      options?: unknown;
      deleteObject?: unknown;
      waitStatus?: boolean;
  }

.. versionadded:: 0.9.0

  - *CloudStorageAction* property **chunkSize** | **chunkLimit** for parallel multipart operations.
  - *CloudStorageDownload* property **options** to customize the provider download client.
  - *CloudStorageDownload* property **keyname** for file to be downloaded and subsequently renamed to **filename**.

.. seealso:: For any non-standard named definitions check :doc:`References </references>`.

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

        "endpoint": "http://hostname/nodejs-001" // Required when different from credential
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
        "deleteObject": {/* service-interface */}
      }
    }]
  }

.. tip:: Any properties in **admin.configBucket.website** set to ``true`` uses the upload HTML page element.

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

.. versionadded:: 0.9.0

  Credentials validation bypass settings in **squared.cloud.json** :alt:`(1.4.0)` were created.

Storage
-------

.. rst-class:: cloud-service

=========== =================== ================== ====================
Service     CLOUD_UPLOAD_STREAM CLOUD_UPLOAD_CHUNK CLOUD_DOWNLOAD_CHUNK
=========== =================== ================== ====================
aws                  X                  X
aws-v3               X                  X
azure                X                  X                    X
gcp                  X                  X                    X
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