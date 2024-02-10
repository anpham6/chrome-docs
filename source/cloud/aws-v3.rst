===================
Amazon Web Services
===================

- **npm** i *@pi-r/aws-v3*

Storage
=======

- https://aws.amazon.com/s3

Interface
---------

.. code-block:: typescript

  import type { CloudStorage } from "./interface";
  import type { AwsAuthInputConfig } from "@aws-sdk/middleware-signing";
  import type { S3ClientConfig } from "@aws-sdk/client-s3";

  interface AWSStorage extends CloudStorage {
      service: "aws-v3";
      credential: string | AWSStorageCredential;
      bucket: string;
  }

  interface AWSBaseCredential extends AwsAuthInputConfig {
      provider?: {
          http?: unknown;
          ini?: unknown;
          cognitoIdentity?: unknown;
          cognitoIdentityPool?: unknown;
          temporaryCredentials?: unknown;
          webToken?: unknown;
          containerMetadata?: unknown;
          instanceMetadata?: unknown;
          process?: unknown;
          tokenFile?: unknown;
          sso?: unknown;
          env?: unknown;
          nodeProviderChain?: unknown;
      };
  }

  interface AWSStorageCredential extends S3ClientConfig, AWSBaseCredential {/* Empty */}

Authentication
--------------

- `Credentials <https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/setting-credentials-node.html>`_
- `Standardized <https://docs.aws.amazon.com/sdkref/latest/guide/standardized-credentials.html>`_
- `Providers <https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/Package/-aws-sdk-credential-providers>`_

.. code-block:: javascript
  :caption: using process.env

  /* Same as AWS */

  AWS_CREDENTIAL_EXPIRATION = ""; // fromEnv
  AWS_CREDENTIAL_SCOPE = "";

  AWS_CONTAINER_CREDENTIALS_RELATIVE_URI = ""; // fromHttp
  AWS_CONTAINER_CREDENTIALS_FULL_URI = "";
  AWS_CONTAINER_AUTHORIZATION_TOKEN_FILE = "";
  AWS_CONTAINER_AUTHORIZATION_TOKEN = "";

::

  {
    "dataSource": {
      "credential": "main", // squared.cloud.json
      /* OR */
      "credential": {
        "credentials": {
          "accessKeyId": "**********", // Legacy V2
          "secretAccessKey": "**********",
          "sessionToken": "", // Optional
          "expiration": "2025-1-1",
          "credentialScope": ""
        },
        "region": "ap-northeast-1"
      },
      /* OR */
      "credential": {
        "provider": {
          "http": true, // AWS_CONTAINER
          "http": {
            "awsContainerCredentialsRelativeUri": "<AWS_CONTAINER_CREDENTIALS_RELATIVE_URI>",
            "awsContainerCredentialsFullUri": "<AWS_CONTAINER_CREDENTIALS_FULL_URI>",
            "awsContainerAuthorizationToken": "<AWS_CONTAINER_AUTHORIZATION_TOKEN>",
            "awsContainerAuthorizationTokenFile": "<AWS_CONTAINER_AUTHORIZATION_TOKEN_FILE>"
          },
          /* OR */
          "ini": {/* params */},
          /* OR */
          "cognitoIdentity": {/* params */},
          /* OR */
          "cognitoIdentityPool": {/* params */},
          /* OR */
          "temporaryCredentials": {/* params */},
          /* OR */
          "webToken": {/* params */},
          /* OR */
          "containerMetadata": {/* params */},
          /* OR */
          "instanceMetadata": {/* params */},
          /* OR */
          "process": {/* params */},
          /* OR */
          "tokenFile": {/* params */},
          /* OR */
          "sso": {/* params */},
          /* OR */
          "env": true, // AWS_ACCESS_KEY_ID + AWS_SECRET_ACCESS_KEY + AWS_SESSION_TOKEN
          /* OR */
          "ini": true, // AWS_SDK_LOAD_CONFIG = "1"
          /* ALSO */
          "nodeProviderChain": true, // Optional
          "nodeProviderChain": {/* params */}
        },
        "region": "ap-northeast-1"
      }
    }
  }

Example usage
-------------

- `S3 Client API <https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/s3>`_
- `Canned ACL <https://docs.aws.amazon.com/AmazonS3/latest/userguide/acl-overview.html#canned-acl>`_

::

  {
    "selector": "html", // Any resource
    "cloudStorage": [{
      "service": "aws-v3",
      "bucket": "nodejs-001",
      "credential": {/* Authentication */},
      "admin": {
        /* Same as AWS */
        "configBucket": {
          "policy": {
            "Policy": "", // s3.PutBucketPolicyCommand
            /* OR */
            "ACL": "authenticated-read", // s3.PutBucketAclCommand
            /* OR */
            "PublicAccessBlockConfiguration": { // s3.PutPublicAccessBlockCommand
              "BlockPublicAcls": false,
              "BlockPublicPolicy": false,
              "IgnorePublicAcls": false,
              "RestrictPublicBuckets": false
            }
          },
          "tags": { // s3.PutBucketTaggingCommand
            "Tagging": {
              "TagSet": [{
                "Key": "key_1",
                "Value": "value_1"
              }]
            }
          },
          "tags": { // s3.DeleteBucketTaggingCommand
            "Tagging": {
              "TagSet": []
            }
          },
          "website": { // s3.PutBucketWebsiteCommand
            "indexPage": "index.html", // IndexDocument
            "errorPage": "404.html" // ErrorDocument
          },
          /* During call to "upload" */
          "create": { // s3.CreateBucketCommand
            "ACL": "public-read",
            "CreateBucketConfiguration": {
              "LocationConstraint": "ap-northeast-3"
            }
          },
          "cors": {
            "CORSRules": [/* Rule */], // s3.PutBucketCorsCommand{CORSConfiguration}
            "CORSRules": [] // s3.DeleteBucketCorsCommand
          },
          "lifecycle": {
            "Rules": [/* Rule */], // s3.PutBucketLifecycleConfigurationCommand{BucketLifecycleConfiguration}
            "Rules": [] // s3.DeleteBucketLifecycleCommand
          },
          "retentionPolicy": {/* DefaultRetention */} // s3.PutObjectLockConfigurationCommand{ObjectLockConfiguration[Rule]}
        }
      },
      "upload": {/* Same as AWS */},
      "download": {/* Same as AWS */}
    }]
  }

Admin
-----

Streaming was enabled by default due to its lower memory usage requirements. It is slower for small file transfers which is typical for a static web page.

.. code-block:: javascript
  :caption: Buffer

  const aws = require("@pi-r/aws-v3");
  aws.CLOUD_UPLOAD_STREAM = false;

.. warning:: Reading a buffer from disk has **2GB** file size limit.

Database
========

- https://aws.amazon.com/dynamodb

Interface
---------

.. code-block:: typescript

  import type { CloudDatabase } from "./interface";
  import type { DynamoDBClientConfig, QueryCommandInput, ScanCommandInput } from "@aws-sdk/client-dynamodb";
  import type { BatchGetCommandInput, TranslateConfig, UpdateCommandInput } from "@aws-sdk/lib-dynamodb";
  import type { NativeAttributeValue } from "@aws-sdk/util-dynamodb";

  interface AWSDatabaseQuery extends CloudDatabase {
      source: "cloud";
      service: "aws-v3";
      credential: string | AWSDatabaseCredential;
      key?: string | AttributeKey;
      query?: QueryCommandInput | ObjectMap<NativeAttributeValue>[];
      params?: BatchGetCommandInput | ScanCommandInput;
      update?: UpdateCommandInput;
  }

  interface AWSDatabaseCredential extends DynamoDBClientConfig, AWSBaseCredential {
      translateConfig?: TranslateConfig;
  }

  type AttributeKey = Record<string, NativeAttributeValue>;

Authentication
--------------

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

- `DynamoDB Client API <https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/dynamodb>`_
- `Query <https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/dynamodb-example-query-scan.html>`_

::

  {
    "selector": "h1",
    "type": "text",
    "dataSource": {
      "source": "cloud",
      "service": "aws-v3",
      "credential": {/* Authentication */},
      "table": "demo",

      "query": { // db.QueryCommand
        "KeyConditionExpression": "#name = :value",
        "ExpressionAttributeNames": { "#name": "id" },
        "ExpressionAttributeValues": { ":value": "1" }
      },
      /* OR */      
      "query": [{ "name": { "S": "value" } }], // db.BatchGetCommand{BatchGetCommandInput[RequestItems]}
      "query": "<empty>", // db.ScanCommand
      "params": { // BatchGetCommandInput | ScanCommandInput
        "ProjectionExpression": "name"
      },
      /* OR */
      "key": { // db.GetCommand{GetCommandInput[Key]}
        "a": "value",
        "b": 1
      },
      /* OR */
      "key": "c", // { "c": 1 }
      "id": 1,

      "value": "<b>${title}</b>: ${description}", // See "/document/data.html"

      "update": { // db.UpdateCommand
        "TableName": "<table>",
        "Key": "<key>"
      },
      "key": "c" // Same as item being retrieved
    }
  }

@pi-r/aws-v3
============

.. versionadded:: 0.7.0

  - **CLOUD_UPLOAD_STREAM** attribute in *ICloudServiceClient* was enabled.
  - **configBucket.tags** using *PutBucketTaggingRequest* was implemented.
  - **configBucket.cors** using *CORSConfiguration* was implemented.
  - **configBucket.lifecycle** using *BucketLifecycleConfiguration* was implemented.

.. versionadded:: 0.6.2

  - Credential providers "from" methods through the property **provider** were implemented.
  - Credential **expiration** as a date string in the property **credentials** is supported.

.. deprecated:: 0.6.2

  - **AWS_DEFAULT_REGION** is not recognized in *AWS NodeJS SDK* and will be removed in **0.7.0**.
  - Unofficial credential properties from V2 (e.g. profile) will be removed in **0.7.0**.
  - *AWSDatabaseQuery* property **partitionKey** is a duplicate of **key** will be removed in **0.7.0**.