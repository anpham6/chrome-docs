===========
@e-mc/image
===========

Interface
=========

.. highlight:: typescript

.. code-block::
  :caption: `View Source <https://www.unpkg.com/@e-mc/types/lib/index.d.ts>`_
  :emphasize-lines: 13

  import type { IHost, ModuleConstructor } from "./index";
  import type { IFileThread } from "./asset";
  import type { CommandData, CropData, QualityData, ResizeData, RotateData, TransformOptions } from "./image";
  import type { ImageModule } from "./settings";

  interface IImage extends IClient<IHost, ImageModule> {
      resizeData?: ResizeData | null;
      cropData?: CropData | null;
      rotateData?: RotateData | null;
      qualityData?: QualityData | null;
      methodData?: [string, unknown[]?][] | null;
      opacityValue?: number;
      outputType?: string;
      setCommand(value: string | CommandData, outputAs?: string): void;
      getCommand(): string;
      parseCommand(value: string): CommandData;
      parseMethod(value: string): [string, unknown[]?][] | null | undefined;
      parseResize(value: string): ResizeData | null | undefined;
      parseCrop(value: string): CropData | null | undefined;
      parseRotate(value: string): RotateData | null | undefined;
      parseQuality(value: string): QualityData | null | undefined;
      parseOpacity(value: string): number;
      using?(data: IFileThread, command: string): Promise<unknown>;
      get outputAs(): string;
  }

  interface ImageConstructor extends ModuleConstructor {
      readonly REGEXP_SIZERANGE: RegExp;
      transform(file: string | Buffer, command: string, options: { tempFile: true }): Promise<string>;
      transform(file: string | Buffer, command: string, options?: TransformOptions): Promise<Buffer | null>;
      clamp(value: unknown, min?: number, max?: number): number;
      isBinary(mime: unknown): mime is string;
      toABGR(buffer: Uint8Array | Buffer): Buffer;
      readonly prototype: IImage;
      new(module?: ImageModule): IImage;
  }

Changelog
=========

.. versionadded:: 0.11.0

  - *IImage* property **outputType** for storing MIME write was created.

Settings
========

.. code-block::
  :caption: `View JSON <https://www.unpkg.com/squared-express/dist/squared.json>`_

  import type { PermittedDirectories } from "./core";

  interface ImageModule {
      // handler: "@pi-r/jimp";
      webp?: string;
      settings?: {
          broadcast_id?: string | string[];
          cache?: boolean;
          jimp?: {
              exec?: {
                  uid?: number;
                  gid?: number;
              };
              cache_expires?: number | string;
              rotate_clockwise?: boolean;
          };
          webp?: {
              path?: string;
              cwebp?: string[];
              gif2webp?: string[];
          };
      };
      permission?: PermittedDirectories;
  }

Example usage
-------------

- :doc:`@pi-r/jimp </image/index>`

.. note:: Usage without a **Host** is conducted through static methods. The **using** class method is called by the **Host** to perform the transformation.

References
==========

- https://www.unpkg.com/@e-mc/types/lib/asset.d.ts
- https://www.unpkg.com/@e-mc/types/lib/image.d.ts
- https://www.unpkg.com/@e-mc/types/lib/settings.d.ts