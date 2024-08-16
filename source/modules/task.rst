==========
@e-mc/task
==========

Interface
=========

.. highlight:: typescript

.. code-block::
  :caption: `View Source <https://www.unpkg.com/@e-mc/types/lib/index.d.ts>`_

  import type { IFileManager, IHost, ModuleConstructor } from "./index";
  import type { ExternalAsset, IFileThread } from "./asset";
  import type { IClient } from "./core";
  import type { TaskModule } from "./settings";
  import type { Command, SpawnResult } from "./task";

  interface ITask extends IClient<IHost, TaskModule> {
      using?(data: IFileThread): Promise<unknown>;
      collect?(items: unknown[], preceding?: boolean): Promise<SpawnResult>[];
      map?(tasks: Command[]): Promise<SpawnResult | void>[];
      series?(tasks: Command[]): Promise<unknown>;
      parallel?(tasks: Command[]): Promise<unknown>;
      spawn?(task: PlainObject, callback: (result?: SpawnResult) => void): void;
      execute?(manager: IFileManager, task: PlainObject, callback: (value?: unknown) => void): void;
  }

  interface TaskConstructor extends ModuleConstructor {
      finalize(this: IHost, instance: ITask, assets: ExternalAsset[]): Promise<void>;
      readonly prototype: ITask;
      new(module?: TaskModule, ...args: unknown[]): ITask;
  }

Changelog
=========

.. versionchanged:: 0.10.0

  - *TaskConstructor* method **finalize** return value was modified to :target:`Promise<void>`:

Settings
========

.. code-block::
  :caption: `View JSON <https://www.unpkg.com/squared-express/dist/squared.json>`_

  import type { PermittedDirectories } from "./core";

  interface TaskModule {
      // handler: "@pi-r/gulp";
      settings?: {
          broadcast_id?: string | string[];
          users?: Record<string, Record<string, unknown>>;
          exec?: {
              uid?: number;
              gid?: number;
          };
      };
      permission?: PermittedDirectories;
  }

Example usage
-------------

- :doc:`@pi-r/gulp </task/index>`

.. note:: Usage without a **Host** is conducted through static methods. The **using** class method is called by the **Host** to perform the transformation.

References
==========

- https://www.unpkg.com/@e-mc/types/lib/asset.d.ts
- https://www.unpkg.com/@e-mc/types/lib/core.d.ts
- https://www.unpkg.com/@e-mc/types/lib/settings.d.ts
- https://www.unpkg.com/@e-mc/types/lib/task.d.ts