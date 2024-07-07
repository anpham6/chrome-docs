===========
@e-mc/watch
===========

- **npm** i *@e-mc/watch*

Interface
=========

.. highlight:: typescript

.. code-block::
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
      start(assets: ExternalAsset[], permission?: IPermission | null): void;
      modified(watch: IFileGroup<ExternalAsset>): Promise<FinalizeResult | void>;
      configureServer(options: SecureOptions): boolean;
      setCA(value: string): boolean;
      setSSLKey(value: string): boolean;
      setSSLCert(value: string): boolean;
      hasSecureProtocol(): boolean;
      whenModified?(assets: ExternalAsset[], postFinalize: PostFinalizeCallback): IFileManager;
      whenModified?(assets: ExternalAsset[], sanitize?: boolean, postFinalize?: PostFinalizeCallback): IFileManager;
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

.. versionremoved:: 0.9.0

  - Constructor **new(interval, port, securePort, extensions)** did not conform with ``Module.init()``. 

Settings
========

.. code-block::
  :caption: `View JSON <https://www.unpkg.com/squared-express/dist/squared.json>`_

  import type { PermittedDirectories } from "./core";

  import type { SecureVersion } from "tls";

  interface WatchModule {
      // handler: "@e-mc/watch";
      extensions?: string[];
      timeout?: number | string;
      interval?: number | string;
      port?: number;
      secure?: {
          port?: number;
          ca?: string;
          key?: string;
          cert?: string;
          passphrase?: string;
          version?: SecureVersion;
      };
      settings?: {
          broadcast_id?: string | string[];
          users?: Record<string, Record<string, unknown>>;
      };
      permission?: PermittedDirectories;
  }

Example usage
-------------

.. code-block:: javascript

  const Watch = require("@e-mc/watch");

  const instance = new Watch({ interval: 100, port: 8080 });
  instance.init();

  instance.whenModified = (assets) => {
    assets.forEach(item => console.log(item.uri));
  };

  const assets = [
    { localUri: "/path/workspace/output/image1.png", uri: "http://hostname/path/document1.png", watch: true },
    { localUri: "/path/workspace/output/image2.png", uri: "http://hostname/path/document2.png", watch: true }
  ];

  instance.start(assets, { disk_read: ["/path/workspace/output/**"] });

References
==========

- https://www.unpkg.com/@e-mc/types/lib/asset.d.ts
- https://www.unpkg.com/@e-mc/types/lib/core.d.ts
- https://www.unpkg.com/@e-mc/types/lib/filemanager.d.ts
- https://www.unpkg.com/@e-mc/types/lib/settings.d.ts
- https://www.unpkg.com/@e-mc/types/lib/watch.d.ts

* https://www.npmjs.com/package/@types/node
* https://www.npmjs.com/package/@types/ws