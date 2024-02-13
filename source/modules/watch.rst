===========
@e-mc/watch
===========

- **npm** i *@e-mc/watch*

Interface
=========

.. code-block:: typescript

  import type { IFileManager, ModuleConstructor } from "./index";
  import type { ExternalAsset } from "./asset";
  import type { IClient, IPermission } from "./core";
  import type { FinalizeResult, PostFinalizeCallback } from "./filemanager";
  import type { WatchModule } from "./settings";
  import type { IFileGroup, ModifiedPostFinalizeListener, SecureOptions, WatchInitResult } from "./watch";

  import type * as ws from "ws";

  interface IWatch extends IClient<IFileManager, WatchModule, ModifiedPostFinalizeListener> {
      connectTimeout: number;
      start(assets: ExternalAsset[], permission?: IPermission): void;
      modified(watch: IFileGroup<ExternalAsset>): Promise<FinalizeResult | void>;
      configureServer(options: SecureOptions): boolean;
      setCA(value: string): boolean;
      setSSLKey(value: string): boolean;
      setSSLCert(value: string): boolean;
      hasSecureProtocol(): boolean;
      whenModified?(assets: ExternalAsset[], postFinalize: PostFinalizeCallback): IFileManager<U>;
      whenModified?(assets: ExternalAsset[], sanitize?: boolean | PostFinalizeCallback, postFinalize?: PostFinalizeCallback): IFileManager;
      set assets(value: ExternalAsset[]);
      get assets(): ExternalAsset[];
      set interval(value);
      get interval(): number;
      set port(value);
      get port(): number;
      set securePort(value);
      get securePort(): number;
  }

  interface WatchConstructor extends ModuleConstructor {
      createServer(port: number, active: boolean): ws.Server | null;
      createServer(port: number, secure?: SecureOptions | null, active?: boolean): ws.Server | null;
      shutdown(): void;
      setTimeout(value: number | string): void;
      checkTimeout(client: ws): boolean;
      readonly prototype: WatchInstance;
      new(module?: WatchModule): WatchInstance;
      new(interval?: number, port?: number, securePort?: number, extensions?: unknown[]): WatchInstance;
  }

  type WatchInstance = IWatch<IFileManager, ExternalAsset, WatchModule, ModifiedPostFinalizeListener>;

References
==========

* https://www.unpkg.com/@e-mc/types/lib/index.d.ts

- https://www.unpkg.com/@e-mc/types/lib/asset.d.ts
- https://www.unpkg.com/@e-mc/types/lib/core.d.ts
- https://www.unpkg.com/@e-mc/types/lib/filemanager.d.ts
- https://www.unpkg.com/@e-mc/types/lib/settings.d.ts
- https://www.unpkg.com/@e-mc/types/lib/watch.d.ts