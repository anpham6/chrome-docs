==========
@e-mc/task
==========

- **npm** i *@e-mc/task*

Interface
=========

.. code-block:: typescript

  import type { IFileManager, IHost, ModuleConstructor } from "./index";
  import type { ExternalAsset, IFileThread } from "./asset";
  import type { IClient } from "./core";
  import type { TaskModule } from "./settings";
  import type { Command, SpawnResult } from "./task";

  interface ITask extends IClient<IHost, TaskModule> {
      using?(data: IFileThread): Promise<unknown>;
      collect?(items: unknown[], preceding?: boolean): Promise<SpawnResult>[];
      map?(tasks: Command[]): Promise<SpawnResult | undefined>[];
      series?(tasks: Command[]): Promise<unknown>;
      parallel?(tasks: Command[]): Promise<unknown>;
      spawn?(task: Record<string | number | symbol, unknown>, callback: (result?: SpawnResult) => void): void;
      execute?(manager: IFileManager, task: Record<string | number | symbol, unknown>, callback: (value?: unknown) => void): void;
  }

  interface TaskConstructor extends ModuleConstructor {
      finalize(this: IHost, instance: ITask, assets: ExternalAsset[]): Promise<unknown>;
      readonly prototype: ITask;
      new(module?: TaskModule, ...args: unknown[]): ITask;
  }

References
==========

* https://www.unpkg.com/@e-mc/types/lib/index.d.ts

- https://www.unpkg.com/@e-mc/types/lib/asset.d.ts
- https://www.unpkg.com/@e-mc/types/lib/core.d.ts
- https://www.unpkg.com/@e-mc/types/lib/settings.d.ts
- https://www.unpkg.com/@e-mc/types/lib/task.d.ts