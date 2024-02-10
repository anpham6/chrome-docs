=====
MinIO
=====

- https://min.io/download
- **npm** i *@pi-r/minio*

Interface
=========

.. code-block:: typescript

  import type { CloudStorage } from "./interface";
  import type { ClientOptions } from "minio";

  interface MinIOStorage extends CloudStorage {
      service: "minio";
      credential: string | MinIOStorageCredential;
      bucket: string;
  }

  type MinIOStorageCredential = Partial<ClientOptions>;

Authentication
==============

- `Credentials <https://min.io/docs/minio/linux/developers/javascript/minio-javascript.html>`_

.. code-block::

  {
    "credential": "main", // squared.cloud.json
    /* OR */
    "credential": {
      "accessKey": "**********",
      "secretKey": "**********",
      "endPoint": "127.0.0.1",
      "port": 9000,
      "useSSL": false, // Required with "http"
      "region": "us-west-1" // Default is "us-east-1"
    }
  }

.. code-block:: javascript
  :caption: using process.env

  MINIO_ACCESS_KEY = "";
  MINIO_SECRET_KEY = "";
  MINIO_SESSION_TOKEN = "";
  MINIO_ENDPOINT = ""; // Default is "localhost"

.. important:: These are not official MinIO environment variables and require :code:`process.env.apply = true` in *squared.json*.

Example usage
=============

- `Client API <https://min.io/docs/minio/linux/developers/javascript/API.html>`_
- `Policy <https://min.io/docs/minio/linux/administration/identity-access-management/policy-based-access-control.html>`_

.. code-block::

  {
    "selector": "img",
    "cloudStorage": [{
      "service": "minio",
      "bucket": "nodejs-001",
      "credential": {/* Authentication */},
      "admin": {
        "publicRead": true, // Will create a compatible S3 "public-read" policy
        /* OR */
        "acl": "readonly", // "writeonly" | "readwrite" (creates compatible MinIO policy)

        "configBucket": {
          /* minio.setBucketPolicy */
          "policy": "readonly", // "writeonly" | "readwrite" (Canned ACL)
          "policy": "public-read", // Same as AWS
          "policy": {
            "Version": "2012-10-17",
            "Statement": [{
              "Sid": "PublicRead",
              "Effect": "Allow",
              "Principal": {
                "AWS": ["*"]
              },
              "Action": ["s3:GetObject"],
              "Resource": ["arn:aws:s3:::nodejs-001/*"]
            }
          },
          "tags": { // minio.setBucketTagging
            "key_1": "value",
            "key_2": "value"
          },
          "tags": {}, // minio.removeBucketTagging
          /* During call to "upload" */
          "create": {
            "versioningConfig": { // minio.setBucketVersioning
              "Status": "Enabled"
            },
            "replicationConfig": { // minio.setBucketReplication
              "role": "arn:minio:replication::b22d653b-e4fb-4c5d-8140-7694c8e72ed4:dest-bucket",
              "rules": [/* Rule */]
            },
            "encryptionConfig": { // minio.setBucketEncryption
              "Rule": [/* Rule */] // Default is "AES256"
            },
            "tags": { // minio.setBucketTagging
              "key_1": "value",
              "key_2": "value"
            }
          },
          "lifecycle": {
            "Rule": [/* Rule */], // minio.setBucketLifecycle
            "Rule": [] // minio.removeBucketLifecycle
          },
          "retentionPolicy": { // minio.setObjectLockConfig
            "mode": "COMPLIANCE",
            "unit": "Days",
            "validity": 10
          }
        }
      },
      "upload": {
        "publicRead": true, // S3 request header "x-amz-acl" to "public-read"
        /* OR */
        "acl": "authenticated-read", // "aws-exec-read" | "bucket-owner-full-control" | "bucket-owner-read" | "private" | "public-read" | "public-read-write" (S3 Object Canned ACL)

        "options": {
          "Content-Type": "image/webp" // All objects except when "metadata" is defined
        },

        /* Primary object only */
        "metadata": {
          "Content-Type": "image/png"
        },
        "tags": { // minio.setObjectTagging
          "key_1": "value",
          "key_2": "value"
        },
        "tags": {}, // minio.removeObjectTagging
        "tags": false
      },
      "download": {
        "deleteObject": { // minio.removeObject
          "versionId": "12345",
          "governanceBypass": true
        }
      }
    }]
  }

.. note:: Some variations of functionality are more thoroughly documented in the :doc:`AWS <aws>` examples.

Admin
-----

Streaming was enabled by default due to its lower memory usage requirements. It is slower for small file transfers which is typical for a static web page.

.. code-block:: javascript
  :caption: Buffer

  const minio = require("@pi-r/minio");
  minio.CLOUD_UPLOAD_STREAM = false;

.. warning:: Reading a buffer from disk has **2GB** file size limit.

@pi-r/minio
===========

.. versionadded:: 0.7.0

  - **CLOUD_UPLOAD_STREAM** attribute in *ICloudServiceClient* was enabled.
  - **configBucket.tags** using *TagList* was implemented.
  - **configBucket.lifecycle** using *LifecycleConfig* was implemented.
  - **configBucket.create** functionality was implemented.