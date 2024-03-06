===========
@e-mc/cloud
===========

- **npm** i *@e-mc/cloud*

Interface
=========

.. highlight:: typescript

.. code-block::
  :caption: `View Source <https://www.unpkg.com/@e-mc/types/lib/index.d.ts>`_

  import type { IHost, IScopeOrigin } from "./index";
  import type { ExternalAsset } from "./asset";
  import type { BucketWebsiteOptions, CloudDatabase, CloudFeatures, CloudFunctions, CloudService, CloudStorage, CloudStorageDownload, CloudStorageUpload } from "./cloud";
  import type { ClientDbConstructor, IClientDb } from "./core";
  import type { BatchQueryResult, QueryResult } from "./db";
  import type { LogMessageOptions } from "./logger";
  import type { CloudAuthSettings, CloudModule, CloudServiceOptions, CloudSettings, DbCoerceSettings } from "./settings";

  interface ICloud extends IClientDb<IHost, CloudModule, CloudDatabase, CloudServiceOptions, DbCoerceSettings & CloudAuthSettings> {
      module: CloudModule;
      readonly uploaded: string[];
      readonly downloaded: string[];
      createBucket(service: string, credential: unknown, bucket: string, acl?: unknown, options?: unknown): Promise<boolean>;
      createBucket(service: string, credential: unknown, bucket: string, publicRead?: boolean): Promise<boolean>;
      setBucketPolicy(service: string, credential: unknown, bucket: string, options: unknown): Promise<boolean>;
      setBucketTagging(service: string, credential: unknown, bucket: string, options: unknown): Promise<boolean>;
      setBucketWebsite(service: string, credential: unknown, bucket: string, options: BucketWebsiteOptions): Promise<boolean>;
      deleteObjects(service: string, credential: unknown, bucket: string, recursive?: boolean): Promise<void>;
      uploadObject(service: string, credential: unknown, bucket: string, upload: CloudStorageUpload, localUri: string, beforeResolve?: ((value: string) => Promise<void> | void)): Promise<string>;
      downloadObject(service: string, credential: unknown, bucket: string, download: CloudStorageDownload, beforeResolve?: ((value: Buffer | string | null) => Promise<string | undefined> | void)): Promise<Buffer | string>;
      getStorage(action: CloudFunctions, data: CloudStorage[] | undefined): CloudStorage | undefined;
      hasStorage(action: CloudFunctions, storage: CloudStorage): CloudStorageUpload | false;
      getDatabaseRows(item: CloudDatabase, ignoreErrors: boolean, sessionKey?: string): Promise<QueryResult>;
      getDatabaseRows(item: CloudDatabase, sessionKey?: string): Promise<QueryResult>;
      getDatabaseBatchRows(batch: CloudDatabase[], ignoreErrors: boolean, sessionKey?: string): Promise<BatchQueryResult>;
      getDatabaseBatchRows(batch: CloudDatabase[], sessionKey?: string): Promise<BatchQueryResult>;
      hasCredential(feature: CloudFeatures, data: CloudService, credential?: unknown): boolean;
      getCredential(item: CloudService, unused?: boolean): PlainObject;
      getSettings(service: string): Record<string, unknown> | undefined;
      settingsOf(service: string, name: "coerce", component: keyof DbCoerceSettings): unknown;
      settingsOf(service: string, name: "auth", component: keyof CloudAuthSettings): unknown;
      getUploadHandler(service: string, credential: unknown): (...args: unknown[]) => void;
      getDownloadHandler(service: string, credential: unknown): (...args: unknown[]) => void;
      resolveService(service: string, folder?: string): string;
      get settings(): CloudSettings;
  }

  interface CloudConstructor extends ClientDbConstructor<IHost> {
      LOG_CLOUD_FAIL: LogMessageOptions;
      LOG_CLOUD_COMMAND: LogMessageOptions;
      LOG_CLOUD_WARN: LogMessageOptions;
      LOG_CLOUD_UPLOAD: LogMessageOptions;
      LOG_CLOUD_DOWNLOAD: LogMessageOptions;
      LOG_CLOUD_DELETE: LogMessageOptions;
      LOG_CLOUD_DELAYED: LogMessageOptions;
      finalize(this: IHost, instance: ICloud): Promise<unknown>;
      uploadAsset(state: IScopeOrigin<IFileManager, ICloud>, file: ExternalAsset, options: UploadAssetOptions): Promise<unknown>[];
      uploadAsset(state: IScopeOrigin<IFileManager, ICloud>, file: ExternalAsset, ignoreProcess: boolean): Promise<unknown>[];
      uploadAsset(state: IScopeOrigin<IFileManager, ICloud>, file: ExternalAsset, contentType?: string, ignoreProcess?: boolean): Promise<unknown>[];
      sanitizeAssets(assets: ExternalAsset[]): ExternalAsset[];
      readonly prototype: ICloud;
      new(module?: CloudModule, database?: CloudDatabase[], ...args: unknown[]): ICloud;
  }

  interface ICloudServiceClient {
      CLOUD_SERVICE_NAME: string;
      CLOUD_UPLOAD_DISK?: boolean;
      CLOUD_UPLOAD_STREAM?: boolean;
      CLOUD_UPLOAD_CHUNK?: boolean;
      CLOUD_DOWNLOAD_CHUNK?: boolean;
      validateStorage?(credential: unknown, data?: CloudService): boolean;
      validateDatabase?(credential: unknown, data?: CloudService): boolean;
      createStorageClient?(this: IModule, credential: unknown, service?: string): unknown;
      createDatabaseClient?(this: IModule, credential: unknown, data?: CloudService): unknown;
      createBucket?(this: IModule, credential: unknown, bucket: string, publicRead?: boolean, service?: string, sdk?: string): Promise<boolean>;
      createBucketV2?(this: IModule, credential: unknown, bucket: string, acl?: unknown, options?: unknown, service?: string, sdk?: string): Promise<boolean>;
      setBucketPolicy?(this: IModule, credential: unknown, bucket: string, options: unknown, service?: string, sdk?: string): Promise<boolean>;
      setBucketTagging?(this: IModule, credential: unknown, bucket: string, options: unknown, service?: string, sdk?: string): Promise<boolean>;
      setBucketWebsite?(this: IModule, credential: unknown, bucket: string, options: BucketWebsiteOptions, service?: string, sdk?: string): Promise<boolean>;
      deleteObjects?(this: IModule, credential: unknown, bucket: string, service?: string, sdk?: string, recursive?: boolean): Promise<void>;
      deleteObjectsV2?(this: IModule, credential: unknown, bucket: string, recursive?: boolean, service?: string, sdk?: string): Promise<void>;
      executeQuery?(this: ICloud, credential: unknown, data: CloudDatabase, sessionKey?: string): Promise<QueryResult>;
      executeBatchQuery?(this: ICloud, credential: unknown, batch: CloudDatabase[], sessionKey?: string): Promise<BatchQueryResult>;
  }

.. versionadded:: 0.9.0

  *ICloud* method **setBucketTagging** was created.

.. deprecated:: 0.9.0

  *ICloudServiceClient* static property **CLOUD_UPLOAD_FROMDISK** was renamed :target:`CLOUD_UPLOAD_DISK`.

Settings
========

.. code-block::
  :caption: `View JSON <https://www.unpkg.com/squared-express/dist/squared.cloud.json>`_

  import type { PermittedDirectories } from "./core";
  import type { CloudServiceOptions, DbSourceOptions, PurgeComponent } from "./settings";

  interface CloudModule {
      // handler: "@e-mc/cloud";
      extensions?: string[];
      atlas?: CloudStoredCredentials;
      aws?: CloudStoredCredentials;
      "aws-v3"?: CloudStoredCredentials;
      azure?: CloudStoredCredentials; // az
      gcp?: CloudStoredCredentials; // gcloud
      ibm?: CloudStoredCredentials;
      oci?: CloudStoredCredentials;
      minio?: CloudStoredCredentials;
      settings?: {
          broadcast_id?: string | string[];
          users?: Record<string, Record<string, unknown>>;
          cache_dir?: string;
          session_expires?: number;
          user_key?: Record<string, DbSourceOptions>;
          imports?: StringMap;
          purge?: PurgeComponent;
          atlas?: CloudServiceOptions;
          aws?: CloudServiceOptions;
          "aws-v3"?: CloudServiceOptions;
          azure?: CloudServiceOptions;
          gcp?: CloudServiceOptions;
          ibm?: CloudServiceOptions;
          oci?: CloudServiceOptions;
          minio?: CloudServiceOptions;
      };
      permission?: PermittedDirectories;
  }

  type CloudStoredCredentials = Record<string, Record<string, unknown>>;

Example usage
-------------

.. code-block:: javascript
  :caption: Using @pi-r/aws

  const Cloud = require("@e-mc/cloud");

  const instance = new Cloud({
    aws: {
      main: {
        accessKeyId: "**********",
        secretAccessKey: "**********"
      }
    },
    "aws-v3": {
      main: {
        credentials: {
          accessKeyId: "**********",
          secretAccessKey: "**********",
          region: "ap-northeast-1"
        }
      }
    }
  });
  // instance.host = new Host();
  instance.init();

  const options = {
    contentType: "application/tar",
    acl: "authenticated-read",
    chunkSize: "8mb",
    overwrite: false, // Default
    tags: { key_1: "value", key_2: "value" }
  };
  Promise.all([
    // nodejs-001/archive.tar
    instance.uploadObject("aws", "main", "nodejs-001", options, "/tmp/archive.tar"),
    // nodejs-001/2024/01-01.tar
    instance.uploadObject("aws", "main", "nodejs-001", { ...options, publicRead: true, pathname: "2024", filename: "01-01.tar" }, "/tmp/archive.tar"),
    // nodejs-001/archive_1.tar
    instance.uploadObject("aws", { accessKeyId: "*****", secretAccessKey: "*****" }, "nodejs-001", { overwrite: false }, "/tmp/archive.tar")
  ]);

  const rows = await instance.getDatabaseRows({ service: "aws-v3", credential: "main", table: "demo", key: { id: 1 } });

References
==========

- https://www.unpkg.com/@e-mc/types/lib/asset.d.ts
- https://www.unpkg.com/@e-mc/types/lib/cloud.d.ts
- https://www.unpkg.com/@e-mc/types/lib/core.d.ts
- https://www.unpkg.com/@e-mc/types/lib/db.d.ts
- https://www.unpkg.com/@e-mc/types/lib/logger.d.ts
- https://www.unpkg.com/@e-mc/types/lib/settings.d.ts