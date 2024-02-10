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
      chunkSize?: number | string; // Only Azure + GCP
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
      versionId?: string;
      options?: unknown;
      deleteObject?: unknown;
      waitStatus?: boolean;
  }

.. versionadded:: 0.9.0

  - *CloudStorageAction* property **chunkSize** for parallel operations.
  - *CloudStorageDownload* property **options** for to customize the download method.

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

        "filename": "picture.png", // Choose a different filename for bucket
        "overwrite": false, // If exists then picture{1,2,3}.png
        /* OR */
        "overwrite": true, // Always use current filename

        "contentType": "image/png", // Metadata has higher precedence (default is "application/octet-stream")
        "minStreamSize": 10485760, // Detect when to use readable stream (not limited to 2gb)
        "minStreamSize": "10mb",

        "chunkSize": "8mb", // Minimum part size of a parallel upload operation
        "chunkSize": 33554432, // 8 * 1024 * 1024

        "endpoint": "http://hostname/nodejs-001" // Required when different from credential
      },
      "download": {
        "filename": "alternate.png", // Required
        "versionId": "12345", // Retrieve a previous file snapshot

        "chunkSize": "32mb", // Minimum part size of a parallel download operation
        "chunkSize": 33554432, // 32 * 1024 * 1024

        "active": false,
        "overwrite": false, // If local file exists then skip download
        /* OR */
        "active": true, // Always write file or replace local file when same extension

        "waitStatus": true, // Delay build until file is completely downloaded

        "pathname": "download/images", // Relative only (base directory/pathname)
        /* OR */
        "preservePath": false, // Use base directory
        "preservePath": true, // Use asset directory

        "deleteObject": true, // Delete from bucket after successful download
        "deleteObject": {/* service-interface */}
      }
    }]
  }

.. tip:: Any properties in **admin.configBucket.website** set to **true** uses the upload HTML page element.

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