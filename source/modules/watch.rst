===========
@e-mc/watch
===========

- **npm** i *@e-mc/watch*

Interface
=========

.. code-block:: typescript
  :caption: `View Source <https://www.unpkg.com/@e-mc/types/lib/index.d.ts>`_

  import type { IFileManager, ModuleConstructor } from "./index";
  import type { ExternalAsset } from "./asset";
  import type { HostInitConfig, IClient, IPermission } from "./core";
  import type { FinalizeResult, PostFinalizeCallback } from "./filemanager";
  import type { WatchModule } from "./settings";
  import type { IFileGroup, ModifiedPostFinalizeListener, SecureOptions } from "./watch";

  import type * as ws from "ws";

  interface IWatch extends IClient<IFileManager, WatchModule, ModifiedPostFinalizeListener> {
      connectTimeout: number;
      init(config?: HostInitConfig): this; 
      start(assets: ExternalAsset[], permission?: IPermission): void;
      modified(watch: IFileGroup<ExternalAsset>): Promise<FinalizeResult | void>;
      configureServer(options: SecureOptions): boolean;
      setCA(value: string): boolean;
      setSSLKey(value: string): boolean;
      setSSLCert(value: string): boolean;
      hasSecureProtocol(): boolean;
      whenModified?(assets: ExternalAsset[], postFinalize: PostFinalizeCallback): IFileManager;
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
      readonly prototype: IWatch;
      new(module?: WatchModule): IWatch;
  }

.. deprecated:: 0.8.4

  Constructor **new(interval, port, securePort, extensions)** does not conform with ``Module.init()`` and will be removed in **0.9.0**. 

References
==========

- https://www.unpkg.com/@e-mc/types/lib/asset.d.ts
- https://www.unpkg.com/@e-mc/types/lib/core.d.ts
- https://www.unpkg.com/@e-mc/types/lib/filemanager.d.ts
- https://www.unpkg.com/@e-mc/types/lib/settings.d.ts
- https://www.unpkg.com/@e-mc/types/lib/watch.d.ts