===================
Amazon Web Services
===================

- **npm** i *@pi-r/aws*

Storage
=======

- https://aws.amazon.com/s3

Interface
---------

.. code-block:: typescript

  import type { CloudStorage } from "./interface";
  import type { ConfigurationOptions } from "aws-sdk/lib/core";

  interface AWSStorage extends CloudStorage {
      service: "aws";
      credential: string | AWSStorageCredential;
      bucket: string;
  }

  interface AWSStorageCredential extends ConfigurationOptions {
      profile?: string;
      fromPath?: string;
  }

Authentication
--------------

- `Credentials <https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/setting-credentials-node.html>`_
- `Access Keys <https://docs.aws.amazon.com/sdkref/latest/guide/feature-static-credentials.html>`_
- `Provider Chain <https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/CredentialProviderChain.html>`_

.. code-block:: javascript
  :caption: using process.env

  AWS_ACCESS_KEY_ID = "";
  AWS_SECRET_ACCESS_KEY = "";
  AWS_SESSION_TOKEN = ""; // Optional

  AWS_SDK_LOAD_CONFIG = "<any>"; // AWS.SharedIniFileCredentials
  AWS_SHARED_CREDENTIALS_FILE = "<default>"; // Default is "~/.aws/credentials"
  AWS_PROFILE = "<default>";

  AWS_WEB_IDENTITY_TOKEN_FILE = ""; // AWS.TokenFileWebIdentityCredentials

  AWS_CONTAINER_CREDENTIALS_RELATIVE_URI = ""; // AWS.RemoteCredentials
  AWS_CONTAINER_CREDENTIALS_FULL_URI = "";

::

  {
    "dataSource": {
      "credential": "main", // squared.cloud.json
      /* OR */
      "credential": {
        "accessKeyId": "**********",
        "secretAccessKey": "**********",
        "region": "ap-northeast-1",
        "sessionToken": ""
      },
      /* OR */
      "credential": {
        "profile": "work-account"
      },
      /* OR */
      "credential": {
        "fromPath": "./config.json" // Current request only (read permission)
      }
    }
  }

Example usage
-------------

- `S3 Client API <https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/S3.html>`_
- `Canned ACL <https://docs.aws.amazon.com/AmazonS3/latest/userguide/acl-overview.html#canned-acl>`_

::

  {
    "selector": "html", // Any resource
    "cloudStorage": [{
      "service": "aws",
      "bucket": "nodejs-001",
      "credential": {/* Authentication */},
      "admin": {
        "publicRead": true, // Bucket + uploaded objects
        /* OR */
        "publicRead": 1, // Bucket only (s3::ListBucket*)
        /* OR */
        /* Will modify existing bucket (equivalent policy) + uploaded objects */
        "acl": "private", // Canned ACL - Bucket

        "configBucket": {
          "policy": {
            "Policy": "", // s3.putBucketPolicy
            /* OR */
            "ACL": "authenticated-read", // s3.putBucketAcl
            /* OR */
            "PublicAccessBlockConfiguration": { // s3.putPublicAccessBlock
              "BlockPublicAcls": false,
              "BlockPublicPolicy": false,
              "IgnorePublicAcls": false,
              "RestrictPublicBuckets": false
            }
          },
          "tags": { // s3.putBucketTagging
            "Tagging": {
              "TagSet": [{
                "Key": "key_1",
                "Value": "value_1"
              }]
            }
          },
          "tags": { // s3.deleteBucketTagging
            "Tagging": {
              "TagSet": []
            }
          },
          "website": { // s3.putBucketWebsite
            "indexPage": "index.html", // IndexDocument
            "errorPage": "404.html" // ErrorDocument
          },
          /* During call to "upload" */
          "create": { // s3.createBucket
            "ACL": "public-read",
            "CreateBucketConfiguration": {
              "LocationConstraint": "ap-northeast-3"
            }
          },
          "cors": {
            "CORSRules": [/* Rule */], // s3.putBucketCors{CORSConfiguration}
            "CORSRules": [] // s3.deleteBucketCors
          },
          "lifecycle": {
            "Rules": [/* Rule */], // s3.putBucketLifecycleConfiguration{LifecycleConfiguration}
            "Rules": [] // s3.deleteBucketLifecycle
          },
          "retentionPolicy": {/* DefaultRetention */} // s3.putObjectLockConfiguration{ObjectLockConfiguration[Rule]}
        }
      },
      "upload": { // s3.upload
        "publicRead": true, // Will overwrite primary options.ACL
        /* OR */
        "acl": "private" // Canned ACL - Object

        "options": { // PutObjectRequest
          "ContentType": "text/html", // Primary object only
          "ACL": "private", // All objects
          "Metadata": {/* Record<string, string> */}, // All objects except when "metadata" is defined
          "ExpectedBucketOwner": ""
        },

        /* Primary object only */
        "metadata": {
          "Content-Type": "text/html; charset=UTF-8",
          "Content-Encoding": "gzip",
          "Expires": "Wed, 21 Oct 2015 07:28:00 GMT"
        },
        "tags": { // s3.putObjectTagging{TagSet}
          "key_1": "value",
          "key_2": "value"
        },
        "tags": {}, // s3.deleteObjectTagging
        "tags": false
      },
      "download": {
        /* s3.getObject */
        "options": { // GetObjectRequest
          "ExpectedBucketOwner": "",
          "IfMatch": ""
        }
        /* Same as interface */
      }
    }]
  }

Admin
-----

Any changes made to ``@pi-r/aws`` are inherited by :doc:`@pi-r/ibm <ibm>` and :doc:`@pi-r/oci <oci>`.

Stream
^^^^^^

Streaming was enabled by default due to its lower memory usage requirements. It is slower for small file transfers which is typical for a static web page.

Setting the storage property :code:`upload.minStreamSize = -1` will also disable streaming for the current request.

.. code-block:: javascript
  :caption: Buffer

  const aws = require("@pi-r/aws");
  aws.CLOUD_UPLOAD_STREAM = false;

.. warning:: Reading a buffer from disk has **2GB** file size limit.

Chunk
^^^^^

Parallel transfers was enabled by default to accommodate large files. The old behavior is used when **chunkSize** is empty and opens only one request per file.

.. code-block:: javascript
  :caption: Sequential

  const aws = require("@pi-r/aws");
  aws.CLOUD_UPLOAD_CHUNK = false;
  aws.CLOUD_DOWNLOAD_CHUNK = false;

.. note:: Chunking is only active when the upload file size is greater than **chunkSize**.

Database
========

- https://aws.amazon.com/dynamodb

Interface
---------

.. code-block:: typescript

  import type { CloudDatabase } from "./interface";
  import type { ServiceConfigurationOptions } from "aws-sdk/lib/service";
  import type { BatchGetItemInput, Key, QueryInput, ScanInput, UpdateItemInput } from "aws-sdk/clients/dynamodb";

  interface AWSDatabaseQuery extends CloudDatabase {
      source: "cloud";
      service: "aws";
      credential: string | AWSDatabaseCredential;
      key?: string | Key;
      query?: QueryInput | Key[];
      params?: BatchGetItemInput | ScanInput;
      options?: Record<string, unknown>;
      update?: UpdateItemInput;
  }

  interface AWSDatabaseCredential extends AWSStorageCredential, ServiceConfigurationOptions {/* Empty */}

Authentication
--------------

.. code-block:: javascript

  /* Same as Storge */

  AWS_REGION = "";

::

  {
    "dataSource": {
      "credential": "main", // squared.cloud.json
      /* OR */
      "credential": {/* Same as Storage */}
    }
  }

Example usage
-------------

- `DynamoDB Client API <https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/DynamoDB.html>`_
- `Query <https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/dynamodb-example-query-scan.html>`_

::

  {
    "selector": "h1",
    "type": "text",
    "dataSource": {
      "source": "cloud",
      "service": "aws",
      "credential": {/* Authentication */},
      "table": "demo",

      "query": { // db.query
        "KeyConditionExpression": "#name = :value",
        "ExpressionAttributeNames": { "#name": "id" },
        "ExpressionAttributeValues": { ":value": "1" }
      },
      /* OR */      
      "query": [{ "name": { "S": "value" } }], // db.batchGet{BatchGetItemInput[RequestItems]}
      "query": "<empty>", // db.scan
      "params": { // BatchGetItemInput | ScanInput
        "ProjectionExpression": "name"
      },
      /* OR */
      "key": { // db.get{GetItemInput[Key]}
        "a": "value",
        "b": 1
      },
      /* OR */
      "key": "c", // { "c": 1 }
      "id": 1,

      "value": "<b>${title}</b>: ${description}", // See "/document/data.html"

      "update": { // db.update
        "TableName": "<table>",
        "Key": "<key>"
      },
      "key": "c" // Same as item being retrieved
    }
  }

@pi-r/aws
=========

.. versionadded:: 0.7.0

  - **CLOUD_UPLOAD_STREAM** attribute in *ICloudServiceClient* was enabled.
  - **CLOUD_UPLOAD_CHUNK** attribute in *ICloudServiceClient* was enabled.
  - **configBucket.tags** using *PutBucketTaggingRequest* was implemented.
  - **configBucket.cors** using *CORSConfiguration* was implemented.
  - **configBucket.lifecycle** using *LifecycleConfiguration* was implemented.

.. versionadded:: 0.6.2

  - Default providers *web identity token* and *remote credentials* environment variables are detected.
  - **AWS_SDK_LOAD_CONFIG** is enabled with any non empty value.

.. deprecated:: 0.6.2

  - **AWS_SESSION_TOKEN** is not used when validating credentials and was removed in **0.6.2**.
  - DynamoDB using *AWS.config.loadFromPath* to parse **fromPath** will be revised in **0.7.0**.
  - **AWS_DEFAULT_REGION** is not recognized in *AWS NodeJS SDK* and will be removed in **0.7.0**.
  - *AWSDatabaseQuery* property **partitionKey** is a duplicate of **key** will be removed in **0.7.0**.