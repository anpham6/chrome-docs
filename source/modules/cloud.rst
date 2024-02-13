===========
@e-mc/cloud
===========

- **npm** i *@e-mc/cloud*

Interface
=========

.. code-block:: typescript

  import type { IHost, IScopeOrigin } from "./index";
  import type { ExternalAsset } from "./asset";
  import type { BucketWebsiteOptions, CloudDatabase, CloudFeatures, CloudFunctions, CloudService, CloudStorage, CloudStorageDownload, CloudStorageUpload } from "./cloud";
  import type { ClientDbConstructor, IClientDb } from "./core";
  import type { BatchQueryResult, QueryResult } from "./db";
  import type { LogMessageOptions } from "./logger";
  import type { ClientModule, CloudServiceAuthSettings, CloudModule, CloudServiceOptions, CloudSettings, DbCoerceSettings } from "./settings";

  interface ICloud extends IClientDb<IHost, CloudModule, CloudDatabase, CloudServiceOptions, DbCoerceSettings & CloudServiceAuthSettings> {
      module: ClientModule;
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
      getCredential(item: CloudService, unused?: boolean): Record<string | number | symbol, unknown>;
      getSettings(service: string): Record<string, unknown> | undefined;
      settingsOf(service: string, name: "coerce", component: keyof DbCoerceSettings): unknown;
      settingsOf(service: string, name: "auth", component: keyof CloudServiceAuthSettings): unknown;
      getUploadHandler(service: string, credential: unknown): (...args: unknown[]) => void;
      getDownloadHandler(service: string, credential: unknown): (...args: unknown[]) => void;
      resolveService(service: string, folder?: string): string;
      getUserSettings(): unknown;
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
      finalize(this: IHost, instance: ICloud<IHost, CloudModule, CloudDatabase>): Promise<unknown>;
      uploadAsset(state: IScopeOrigin<IFileManager, ICloud<IFileManager>>, file: ExternalAsset, ignoreProcess: boolean): Promise<unknown>[];
      uploadAsset(state: IScopeOrigin<IFileManager, ICloud<IFileManager>>, file: ExternalAsset, contentType?: string, ignoreProcess?: boolean): Promise<unknown>[];
      sanitizeAssets(assets: ExternalAsset[]): ExternalAsset[];
      readonly prototype: ICloud<IHost, CloudModule, CloudDatabase>;
      new(module?: CloudModule, database?: CloudDatabase[], ...args: unknown[]): ICloud<IHost, CloudModule, CloudDatabase>;
  }

.. versionadded:: 0.9.0

  - *ICloud* method **setBucketTagging** was created.

References
==========

* https://www.unpkg.com/@e-mc/types/lib/index.d.ts

- https://www.unpkg.com/@e-mc/types/lib/asset.d.ts
- https://www.unpkg.com/@e-mc/types/lib/cloud.d.ts
- https://www.unpkg.com/@e-mc/types/lib/core.d.ts
- https://www.unpkg.com/@e-mc/types/lib/db.d.ts
- https://www.unpkg.com/@e-mc/types/lib/logger.d.ts
- https://www.unpkg.com/@e-mc/types/lib/settings.d.ts