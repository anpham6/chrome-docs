===========
@e-mc/image
===========

- **npm** i *@e-mc/image*

Interface
=========

.. code-block:: typescript

  import type { IHost, ModuleConstructor } from "./index";
  import type { IFileThread } from "./asset";
  import type { CommandData, CropData, QualityData, ResizeData, RotateData, TransformOptions } from "./image";
  import type { ImageModule } from "./settings";

  interface IImage extends IClient<IHost, ImageModule> {
      resizeData?: ResizeData;
      cropData?: CropData;
      rotateData?: RotateData;
      qualityData?: QualityData;
      methodData?: [string, unknown[]?][];
      opacityValue?: number;
      setCommand(value: string | CommandData, outputAs?: string): void;
      getCommand(): string;
      parseCommand(value: string): CommandData;
      parseMethod(value: string): [string, unknown[]?][] | undefined;
      parseResize(value: string): ResizeData | undefined;
      parseCrop(value: string): CropData | undefined;
      parseRotate(value: string): RotateData | undefined;
      parseQuality(value: string): QualityData | undefined;
      parseOpacity(value: string): number;
      using?(data: IFileThread, command: string): Promise<unknown>;
      get outputAs(): string;
  }

  interface ImageConstructor extends ModuleConstructor {
      readonly REGEXP_SIZERANGE: RegExp;
      transform(file: string, command: string, options?: TransformOptions): Promise<Buffer | string | null>;
      clamp(value: unknown, min?: number, max?: number): number;
      isBinary(mime: unknown): mime is string;
      toABGR(buffer: Uint8Array | Buffer): Buffer;
      readonly prototype: IImage;
      new(module?: ImageModule): IImage;
  }

References
==========

* https://www.unpkg.com/@e-mc/types/lib/index.d.ts

- https://www.unpkg.com/@e-mc/types/lib/asset.d.ts
- https://www.unpkg.com/@e-mc/types/lib/image.d.ts
- https://www.unpkg.com/@e-mc/types/lib/settings.d.ts