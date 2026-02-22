===========
@e-mc/cloud
===========

Interface
=========

.. highlight:: typescript

.. code-block::
  :caption: `View Source <https://www.unpkg.com/@e-mc/types/lib/index.d.ts>`_
  :emphasize-lines: 20,53,55

  import type { IFileManager, IHost, IScopeOrigin } from "./index";
  import type { ExternalAsset } from "./asset";
  import type { BucketWebsiteOptions, CloudDatabase, CloudFeatures, CloudFunctions, CloudService, CloudStorage, CloudStorageDownload, CloudStorageUpload, CopyObjectOptions, DeleteObjectsOptions } from "./cloud";
  import type { ClientDbConstructor, IClientDb } from "./core";
  import type { BatchQueryResult, QueryResult } from "./db";
  import type { LogFailOptions, LogMessageOptions } from "./logger";
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
      deleteObjects(service: string, credential: unknown, bucket: string, options: DeleteObjectsOptions): Promise<void>;
      deleteObjects(service: string, credential: unknown, bucket: string, recursive?: boolean | DeleteObjectsOptions): Promise<void>;
      copyObject(service: string, credential: unknown, bucketSource: string, keySource: string, bucket: string, key: string, options?: CopyObjectOptions): Promise<void>;
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
      LOG_CLOUD_SUCCESS: LogMessageOptions;
      LOG_CLOUD_FAIL: LogMessageOptions;
      LOG_CLOUD_COMMAND: LogMessageOptions;
      LOG_CLOUD_WARN: LogMessageOptions;
      LOG_CLOUD_UPLOAD: LogMessageOptions;
      LOG_CLOUD_DOWNLOAD: LogMessageOptions;
      LOG_CLOUD_DELETE: LogMessageOptions;
      LOG_CLOUD_DELAYED: LogMessageOptions;
      finalize(this: IHost, instance: ICloud): Promise<void>;
      uploadAsset(state: IScopeOrigin<IFileManager, ICloud>, file: ExternalAsset, options: UploadAssetOptions): Promise<void>[];
      uploadAsset(state: IScopeOrigin<IFileManager, ICloud>, file: ExternalAsset, ignoreProcess: boolean): Promise<void>[];
      uploadAsset(state: IScopeOrigin<IFileManager, ICloud>, file: ExternalAsset, contentType?: string, ignoreProcess?: boolean): Promise<void>[];
      uploadAssetSuccess(state: IScopeOrigin<IFileManager, ICloud>, file: ExternalAsset, active?: boolean): (value: string) => Promise<void> | void;
      sanitizeAssets(assets: ExternalAsset[]): ExternalAsset[];
      optionsLogMessage(type: "SUCCESS" | "FAIL" | "COMMAND" | "WARN" | "UPLOAD" | "DOWNLOAD" | "DELETE" | "DELAYED", options?: LogMessageOptions & LogFailOptions): LogMessageOptions & LogFailOptions;
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
      /** @deprecated */
      createBucket?(this: IModule, credential: unknown, bucket: string, publicRead?: boolean, service?: string, sdk?: string): Promise<boolean>;
      createBucketV2?(this: IModule, credential: unknown, bucket: string, acl?: unknown, options?: unknown, service?: string, sdk?: string): Promise<boolean>;
      setBucketPolicy?(this: IModule, credential: unknown, bucket: string, options: unknown, service?: string, sdk?: string): Promise<boolean>;
      setBucketTagging?(this: IModule, credential: unknown, bucket: string, options: unknown, service?: string, sdk?: string): Promise<boolean>;
      setBucketWebsite?(this: IModule, credential: unknown, bucket: string, options: BucketWebsiteOptions, service?: string, sdk?: string): Promise<boolean>;
      /** @deprecated */
      deleteObjects?(this: IModule, credential: unknown, bucket: string, service?: string, sdk?: string, recursive?: boolean): Promise<void>;
      /** @deprecated */
      deleteObjectsV2?(this: IModule, credential: unknown, bucket: string, recursive?: boolean, service?: string, sdk?: string): Promise<void>;
      deleteObjectsV3?(this: IModule, credential: unknown, bucket: string, options?: DeleteObjectsOptions, service?: string, sdk?: string): Promise<void>;
      copyObject?(this: IModule, credential: unknown, bucketSource: string, keySource: string, bucket: string, key: string, options?: unknown, service?: string, sdk?: string): Promise<void>;
      executeQuery?(this: ICloud, credential: unknown, data: CloudDatabase, sessionKey?: string): Promise<QueryResult>;
      executeBatchQuery?(this: ICloud, credential: unknown, batch: CloudDatabase[], sessionKey?: string): Promise<BatchQueryResult>;
  }

Changelog
=========

.. versionadded:: 0.13.0

  - *ICloud* :alt:`function` **copyObject** was created.
  - *ICloudServiceClient* :alt:`function` **copyObject** :alt:`(optional)` was created.
  - *CloudConstructor* :alt:`function` **optionsLogMessage** was created.
  - *CloudConstructor* :alt:`function` **uploadAssetSuccess** for alternate post-upload file management was created.

.. versionchanged:: 0.13.0

  - ``BREAKING`` *CloudConstructor* :target:`override` :alt:`function` **toPosix** for preserving backslashes and spaces in :target:`object` paths when transacting from a *Win32* platform.

    .. hlist::
      :columns: 1

      - joinPath
      - normalizePath
      - globDir

.. caution:: Using these outside a **Cloud** environment is not recommended. Calling them from other modules :alt:`(e.g. FileManager)` have no change in behavior.

.. versionadded:: 0.11.0

  - *ICloudServiceClient* :alt:`function` **deleteObjectsV3** :alt:`(optional)` was created.

.. versionchanged:: 0.11.0

  - *ICloud* :alt:`function` **deleteObjects** argument :target:`recursive` was supplemented with :target:`options` as :alt:`DeleteObjectsOptions`.

.. deprecated:: 0.11.0

  - :alt:`interface` **ICloudServiceClient** :alt:`function` **deleteObjectsV2** is changing to the V3 signature.

.. deprecated:: 0.10.2

  - :alt:`interface` **ICloudServiceClient** :alt:`function` **createBucket** | **deleteObjects** are changing to the V2 signature.

.. versionchanged:: 0.10.0

  - *CloudConstructor* :alt:`function` **finalize** return value was modified to :target:`Promise<void>`.
  - *CloudConstructor* :alt:`function` **uploadAsset** return value was modified to :target:`Promise<void>[]`.

.. versionadded:: 0.9.0

  - *ICloud* :alt:`function` **setBucketTagging** was created.
  - *ICloudServiceClient* global **CLOUD_UPLOAD_DISK** replaced *CLOUD_UPLOAD_FROMDISK*.

.. versionremoved:: 0.9.0

  - *ICloudServiceClient* global **CLOUD_UPLOAD_FROMDISK** was renamed.

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
      oci?: CloudStoredCredentials;
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
          oci?: CloudServiceOptions;
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